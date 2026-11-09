import re
import sys
import types
from datetime import date
from functools import lru_cache
from html.parser import HTMLParser
from io import StringIO
from unittest import mock

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.staticfiles import finders
from django.core.management import call_command
from django.core.management.base import CommandError
from django.template import Context, Template
from django.template.loader import render_to_string
from django.test import RequestFactory, SimpleTestCase, TestCase, override_settings
from django.urls import include, path

from apps.core import i18n, i18n_check, sitemap
from apps.core import urls as core_urls
from apps.core.languages import LANG_BY_CODE, LANGS

PAGES = {
    "/": "Grow with",
    "/pricing/": "Simple monthly packages.",
    "/how-it-works/": "Real people discover you.",
    "/about/": "A growth agency for creators.",
}
# Never on the site, in any language (see apps/core/i18n/en.py and docs/I18N.md). "Instant" is allowed: we say we aren't.
BANNED = [r"\bseo\b", r"guarante", r"\bfree\b", r"search engine", r"\brankings?\b", r"\bkeywords?\b",
          r"\bcrypto", r"\bverified\b", r"\bcelebrit", r"\btestimonial", r"\breviews?\b", r"\brating"]


class _VisibleText(HTMLParser):
    """Text a visitor (or a screen reader, or a search result) sees: page text, title,
    meta description, alt/title/aria-label/placeholder attributes. Scripts and styles are skipped."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts, self.skip = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1
        attrs = dict(attrs)
        for key in ("alt", "title", "aria-label", "placeholder"):
            if attrs.get(key):
                self.parts.append(attrs[key])
        if tag == "meta" and attrs.get("name") == "description":
            self.parts.append(attrs.get("content", ""))

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip -= 1

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)


def visible_text(html):
    parser = _VisibleText()
    parser.feed(html)
    return re.sub(r"\s+", " ", " ".join(parser.parts))


class CoreTests(TestCase):
    def test_health_check_answers_any_host(self):
        response = self.client.get("/healthz", HTTP_HOST="10.0.0.1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"ok")

    @override_settings(ALLOWED_HOSTS=["growsterr.com", "www.growsterr.com"], SITE_URL="https://growsterr.com")
    def test_www_redirects_to_the_canonical_host(self):
        response = self.client.get("/?a=1", HTTP_HOST="www.growsterr.com")
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response["Location"], "https://growsterr.com/?a=1")

    def test_robots_and_favicon(self):
        robots = self.client.get("/robots.txt").content.decode()
        self.assertIn("Disallow: /admin/", robots)
        self.assertIn("Disallow: /account/", robots)
        self.assertIn("Disallow: /order/", robots)
        self.assertRegex(robots, r"Sitemap: https?://\S+/sitemap\.xml")
        self.assertEqual(self.client.get("/favicon.ico").status_code, 301)


class PageTests(TestCase):
    def get(self, path):
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200, path)
        return response.content.decode()

    def test_every_page_renders_with_its_heading(self):
        for path, heading in PAGES.items():
            with self.subTest(path=path):
                html = self.get(path)
                self.assertIn(heading, html)
                self.assertEqual(html.count("<h1"), 1)
                self.assertIn(f'<link rel="canonical" href="https://growsterr.com{path}">', html)

    def test_copy_rules_on_every_page(self):
        for path in [*PAGES, "/pricing/?platform=youtube", "/does-not-exist/"]:
            with self.subTest(path=path):
                html = self.client.get(path).content.decode()
                text = visible_text(html)
                for pattern in BANNED:
                    self.assertIsNone(re.search(pattern, text, re.I), f"{pattern!r} on {path}")
                # Template comments and tags never leak into the page.
                for leak in ("{#", "#}", "{%", "%}", "{{", "}}"):
                    self.assertNotIn(leak, text, path)
                # We never ask for an account password on these pages (only say that we don't).
                self.assertNotIn('type="password"', html)

    def test_header_and_footer(self):
        html = self.get("/about/")
        for href in ("/instagram/", "/tiktok/", "/youtube/", "/pricing/", "/how-it-works/", "/about/",
                     "/terms/", "/privacy/", "/cookies/", "/refunds/", "/order/", "/account/login/"):
            self.assertIn(f'href="{href}', html)
        self.assertIn("Sign in", html)
        self.assertIn("Get started", html)
        self.assertIn('class="brand__logo only-light" src="/static/img/logo.svg"', html)
        self.assertIn('class="brand__logo only-dark" src="/static/img/logo-dark.svg"', html)
        self.assertIn('localStorage.getItem("theme")', html)  # the early theme script
        self.assertIn("data-theme-toggle", html)
        self.assertIn(f"mailto:{settings.CONTACT_EMAIL}", html)  # from .env: Sterr Agency's inbox for now
        self.assertIn('A product of <a href="https://sterragency.com"', html)
        digits = "".join(c for c in settings.WHATSAPP_NUMBER if c.isdigit())
        self.assertIn(f'class="wa-float" href="https://wa.me/{digits}?text=Hi%20Growsterr', html)
        self.assertIn(f"© {date.today().year} Growsterr", html)
        self.assertIn("Sterr Technologies OÜ", html)
        self.assertIn("17591465", html)
        # The mobile menu works without JS: a <details> controlling the panel.
        self.assertIn('<details class="menu" data-menu>', html)
        self.assertIn('aria-controls="site-menu"', html)
        self.assertIn('id="site-menu"', html)

    def test_current_page_is_marked_in_the_nav(self):
        self.assertIn('href="/pricing/" aria-current="page"', self.get("/pricing/"))
        self.assertIn('href="/how-it-works/" aria-current="page"', self.get("/how-it-works/"))
        self.assertNotIn('aria-current="page"', self.get("/"))

    def test_signed_in_visitors_see_their_account(self):
        user_model = get_user_model()
        user = user_model(**{user_model.USERNAME_FIELD: "creator@example.com"})
        if hasattr(user, "email"):
            user.email = "creator@example.com"
        user.set_unusable_password()
        user.save()
        self.client.force_login(user)
        html = self.get("/")
        self.assertIn("My account", html)
        self.assertIn('href="/account/"', html)
        self.assertNotIn(">Sign in<", html)

    def test_home_shows_every_platform_and_the_packages(self):
        html = self.get("/")
        for platform in ("Instagram", "TikTok", "YouTube"):
            self.assertIn(platform, html)
        # Packages for all three platforms are in the page (tabs work without JS too).
        for key in ("instagram", "tiktok", "youtube"):
            self.assertIn(f'id="packages-{key}" data-tab-panel="{key}"', html)
            for plan in ("starter", "rising", "pro"):
                self.assertIn(f"/order/?plan={plan}&amp;platform={key}&amp;lang=en", html)
        self.assertEqual(html.count('class="plan__name"'), 9)
        for price in ("$79.99", "$149.99", "$279.99"):
            self.assertIn(price, html)
        self.assertIn("Most popular", html)
        text = visible_text(html)
        self.assertIn("Instant means bots.", text)
        self.assertIn("Choose a package", text)
        self.assertIn("Your dashboard shows the numbers", text)
        self.assertIn("An illustration of your dashboard", text)
        self.assertIn("We never sell likes, views or comments on their own.", text)
        # The FAQ answers carry the typical monthly ranges, not promises.
        self.assertIn("1,000–4,000 with Starter Creator", text)
        self.assertIn("not a fixed count", text)
        self.assertIn('<details class="faq__item">', html)

    def test_pricing_tabs_and_billing(self):
        html = self.get("/pricing/")
        self.assertIn('class="tabs__panel is-active" id="instagram"', html)
        for key in ("instagram", "tiktok", "youtube"):
            self.assertIn(f'href="#{key}" data-tab="{key}"', html)
        text = visible_text(html)
        for snippet in ("1,000–4,000", "4,000–24,000", "400–1,600", "Priority placement and a direct WhatsApp line",
                        "renews every month until you cancel", "isn't refunded", "Apple Pay"):
            self.assertIn(snippet, text)
        self.assertIn('href="/terms/#subscription"', html)
        self.assertIn('href="/refunds/"', html)

    def test_pricing_opens_the_platform_from_the_query(self):
        html = self.get("/pricing/?platform=tiktok")
        self.assertIn('class="tabs__panel is-active" id="tiktok"', html)
        self.assertIn('class="tabs__panel" id="instagram"', html)
        html = self.get("/pricing/?platform=nope")
        self.assertIn('class="tabs__panel is-active" id="instagram"', html)

    def test_how_it_works(self):
        text = visible_text(self.get("/how-it-works/"))
        for snippet in ("Choose your package", "We start your campaign", "Real people choose to follow",
                        "Your dashboard shows what was measured", "What we never ask for", "Your password",
                        "What a month looks like"):
            self.assertIn(snippet, text)

    def test_about_tells_the_company_facts_in_the_agency_voice(self):
        html = self.get("/about/")
        text = visible_text(html)
        for snippet in ("Sterr Technologies OÜ", "17591465", "Tornimäe tn 5, 10145 Tallinn, Estonia", "Turkey",
                        "Sterr Agency", "Ekin Sipahi", "a dentist", "several projects"):
            self.assertIn(snippet, text)
        self.assertIn('href="https://sterragency.com"', html)
        self.assertIn('href="https://www.instagram.com/dt.ekinsipahi/"', html)
        # Agency voice and gender-neutral founder wording.
        self.assertIsNone(re.search(r"\bI\b|\bI'm\b|\bmy\b", text), "first person on /about/")
        self.assertIsNone(re.search(r"\b(he|she|his|him|her|hers)\b", text, re.I), "gendered founder wording")

    @override_settings(DEBUG=False)
    def test_not_found_page(self):
        response = self.client.get("/no-such-page/")
        self.assertEqual(response.status_code, 404)
        html = response.content.decode()
        self.assertIn("This page took a different path.", html)
        self.assertIn('<meta name="robots" content="noindex">', html)
        self.assertIn('href="/pricing/"', html)

    def test_server_error_page_renders_without_a_request(self):
        html = render_to_string("500.html")
        self.assertIn("Something went wrong on our side.", html)
        self.assertIn('<meta name="robots" content="noindex">', html)
        self.assertNotIn("{#", visible_text(html))


def english_only(test):
    """Hide every core language module but English for one test, whatever translation files exist."""
    i18n.reset()
    test.addCleanup(i18n.reset)
    real_load = i18n.load
    patcher = mock.patch("apps.core.i18n.load", lru_cache(maxsize=None)(lambda code: real_load(code) if code == "en" else None))
    patcher.start()
    test.addCleanup(patcher.stop)


class ChromeTests(TestCase):
    def setUp(self):
        english_only(self)

    def render_base(self, **context):
        request = RequestFactory().get("/de/")
        return render_to_string("base.html", context, request=request)

    def test_language_switcher_appears_with_lang_links(self):
        links = [(LANG_BY_CODE["en"], "/"), (LANG_BY_CODE["de"], "/de/"), (LANG_BY_CODE["ar"], "/ar/")]
        html = self.render_base(lang="de", lang_links=links)
        self.assertIn('<html lang="de">', html)
        self.assertIn('href="/de/" hreflang="de" lang="de" aria-current="true"', html)
        self.assertIn('href="/ar/" hreflang="ar" lang="ar"', html)
        self.assertIn("/static/img/flags/de.png", html)
        self.assertIn('<details class="lang-menu" data-dropdown>', html)
        # A language without chrome strings yet falls back to English.
        self.assertIn("Get started", html)

    def test_rtl_pages(self):
        html = self.render_base(lang="ar", rtl=True)
        self.assertIn('<html lang="ar" dir="rtl">', html)

    def test_alternates(self):
        html = self.render_base(alternates=[("en", "/"), ("de", "/de/"), ("x-default", "/")])
        self.assertIn('<link rel="alternate" hreflang="de" href="https://growsterr.com/de/">', html)
        self.assertIn('<link rel="alternate" hreflang="x-default" href="https://growsterr.com/">', html)

    def test_image_slot_shows_the_image_only_once_the_file_exists(self):
        tpl = Template('{% load growsterr %}{% image_slot path alt="A creator" width=1200 height=800 variant="soft" art="people" %}')
        missing = tpl.render(Context({"path": "img/photos/not-there-yet.webp"}))
        self.assertIn('class="media media--soft"', missing)
        self.assertIn("--ratio: 1200 / 800", missing)
        self.assertNotIn("<img", missing)
        present = tpl.render(Context({"path": "img/logo.svg"}))
        self.assertIn('<img src="/static/img/logo.svg" alt="A creator" width="1200" height="800" loading="lazy"', present)

    def test_icon_tag(self):
        html = Template('{% load growsterr %}{% icon "check" size=18 cls="x" %}').render(Context())
        self.assertIn('class="icon icon--check x"', html)
        self.assertIn('aria-hidden="true"', html)
        self.assertIn('width="18"', html)

    def test_static_files_exist(self):
        for path in ("css/site.css", "js/site.js", "js/theme.js", "site.webmanifest"):
            self.assertTrue(finders.find(path), path)


class SitemapTests(TestCase):
    def setUp(self):
        english_only(self)

    def test_entries(self):
        entries = sitemap.entries()
        self.assertEqual([e["path"] for e in entries], ["/", "/pricing/", "/how-it-works/", "/about/"])
        for entry in entries:
            self.assertTrue(entry["path"].startswith("/") and entry["path"].endswith("/"))
            self.assertNotRegex(entry["path"], r"^/(account|order|admin|growth)/")
            self.assertIsInstance(entry["lastmod"], date)
            self.assertEqual(entry["alternates"], [])
            self.assertEqual(self.client.get(entry["path"]).status_code, 200)


# --- Languages ----------------------------------------------------------------------------------

GERMAN = {
    "UPDATED": date(2026, 11, 9),
    "CHROME": {"get_started": "Jetzt starten", "nav_pricing": "Preise", "language": "Sprache",
               "not_found_h1": "Diese Seite hat einen anderen Weg genommen."},
    "HOME": {"title": "Growsterr | Echtes Wachstum auf Instagram, TikTok und YouTube",
             "description": "Monatliche Wachstumspakete ab {price} im Monat.",
             "h1": ("Wachse mit ", "echten Menschen", ". Jeden Tag."),
             "faqs": [("Frage?", f"Typisch {{starter}} mit Starter Creator. ({n})") for n in range(8)],
             "cta": {"title": ("Bereit für ", "echte Menschen", "?")}},
    "PRICING": {"h1": ("Einfache Monatspakete. ", "Echte Menschen in jedem."), "description": "Ab {price} im Monat."},
}


def language_module(code, sections):
    module = types.ModuleType(i18n.module_name(code))
    for name, value in sections.items():
        setattr(module, name, value)
    return module


def urlconf():
    """The project's URLs with the core routes rebuilt (so they see the languages a test adds)."""
    from config import urls as project

    module = types.ModuleType("core_i18n_test_urls")
    module.urlpatterns = [path("", include((core_urls.build(), "core"))) if getattr(p, "app_name", None) == "core" else p
                          for p in project.urlpatterns]
    module.handler404 = project.handler404
    return module


def without_core_file():
    """A site language nobody has written apps/core/i18n/<code>.py for yet."""
    return next((lang.code for lang in LANGS if not i18n_check.has_file(lang.code)), None)


class LanguageTestCase(TestCase):
    """Only English plus the languages of `languages` (made-up modules) exist for one test, with
    the routes rebuilt: real translation files that arrive later can't change what it sees."""
    languages = {"de": GERMAN}

    def setUp(self):
        modules = {i18n.module_name(code): language_module(code, sections) for code, sections in self.languages.items()}
        patcher = mock.patch.dict(sys.modules, modules)
        patcher.start()
        self.addCleanup(patcher.stop)
        i18n.reset()
        self.addCleanup(i18n.reset)
        real_load, allowed = i18n.load, {"en", *self.languages}

        @lru_cache(maxsize=None)
        def only_these(code):
            return real_load(code) if code in allowed else None

        load_patcher = mock.patch("apps.core.i18n.load", only_these)
        load_patcher.start()
        self.addCleanup(load_patcher.stop)
        settings_override = override_settings(ROOT_URLCONF=urlconf())
        settings_override.enable()
        self.addCleanup(settings_override.disable)

    def get(self, path, status=200):
        response = self.client.get(path)
        self.assertEqual(response.status_code, status, path)
        return response.content.decode()


class EnglishOnlyTests(LanguageTestCase):
    languages = {}

    def test_no_language_switcher_or_hreflang_while_english_is_alone(self):
        for path in ("/", "/pricing/", "/about/"):
            html = self.get(path)
            self.assertNotIn("lang-list", html)
            self.assertNotIn('rel="alternate" hreflang', html)
        self.assertEqual([e["alternates"] for e in sitemap.entries()], [[], [], [], []])


class LanguageVersionTests(LanguageTestCase):
    languages = {"de": GERMAN, "ar": {"HOME": {"h1": ("انمُ مع ", "أشخاص حقيقيين", ".")}}}

    def test_a_language_version_has_lang_canonical_hreflang_and_og_locale(self):
        html = self.get("/de/")
        self.assertIn('<html lang="de">', html)
        self.assertIn('<link rel="canonical" href="https://growsterr.com/de/">', html)
        for code, href in (("en", "/"), ("de", "/de/"), ("ar", "/ar/"), ("x-default", "/")):
            self.assertIn(f'<link rel="alternate" hreflang="{code}" href="https://growsterr.com{href}">', html)
        self.assertIn('<meta property="og:locale" content="de_DE">', html)
        self.assertIn('<meta property="og:locale:alternate" content="en_GB">', html)
        self.assertIn("Wachse mit ", html)
        self.assertIn("Jetzt starten", html)                   # German chrome
        self.assertIn("See the packages", html)                 # a key German leaves out shows in English
        self.assertIn("Typisch 1.000–4.000 mit Starter Creator", visible_text(html))  # filled, German numbers
        self.assertIn("Monatliche Wachstumspakete ab $79.99 im Monat.", html)
        # The language switcher: this page in every language that has it, the current one marked.
        self.assertIn('href="/de/" hreflang="de" lang="de" aria-current="true"', html)
        self.assertIn('href="/" hreflang="en" lang="en"', html)
        self.assertIn('href="/ar/" hreflang="ar" lang="ar"', html)
        # The chrome links stay in the language: its pricing page, the order form in German.
        self.assertIn('href="/de/pricing/"', html)
        self.assertIn('href="/order/?lang=de"', html)
        self.assertIn('href="/terms/?lang=de"', html)

    def test_english_pages_list_their_language_versions(self):
        html = self.get("/")
        self.assertIn('<html lang="en">', html)
        self.assertIn('<link rel="canonical" href="https://growsterr.com/">', html)
        self.assertIn('<link rel="alternate" hreflang="de" href="https://growsterr.com/de/">', html)
        self.assertIn('<link rel="alternate" hreflang="x-default" href="https://growsterr.com/">', html)
        self.assertIn('href="/" hreflang="en" lang="en" aria-current="true"', html)
        # About exists only in English: no hreflang set, and its switcher falls back to each language's home.
        about = self.get("/about/")
        self.assertNotIn('rel="alternate" hreflang', about)
        self.assertIn('href="/de/" hreflang="de"', about)

    def test_only_the_pages_a_language_has_are_served(self):
        self.assertIn("Einfache Monatspakete. ", self.get("/de/pricing/"))
        self.get("/de/how-it-works/", status=404)  # German has no HOW
        self.get("/de/about/", status=404)
        self.get("/ar/pricing/", status=404)

    def test_right_to_left(self):
        html = self.get("/ar/")
        self.assertIn('<html lang="ar" dir="rtl">', html)
        self.assertIn('<meta property="og:locale" content="ar_AR">', html)

    def test_pricing_keeps_the_platform_query_out_of_the_canonical(self):
        html = self.get("/de/pricing/?platform=youtube")
        self.assertIn('<link rel="canonical" href="https://growsterr.com/de/pricing/">', html)
        self.assertIn('class="tabs__panel is-active" id="youtube"', html)
        self.assertIn("/order/?plan=starter&amp;platform=youtube&amp;lang=de", html)

    def test_sitemap_lists_every_language_version_with_hreflang(self):
        entries = {e["path"]: e for e in sitemap.entries()}
        self.assertEqual(list(entries), ["/", "/pricing/", "/how-it-works/", "/about/", "/de/", "/de/pricing/", "/ar/"])
        self.assertEqual(entries["/de/"]["alternates"], [("en", "/"), ("de", "/de/"), ("ar", "/ar/"), ("x-default", "/")])
        self.assertEqual(entries["/de/pricing/"]["alternates"],
                         [("en", "/pricing/"), ("de", "/de/pricing/"), ("x-default", "/pricing/")])
        self.assertEqual(entries["/about/"]["alternates"], [])
        self.assertEqual(entries["/de/"]["lastmod"], date(2026, 11, 9))
        self.assertEqual(entries["/ar/"]["lastmod"], entries["/"]["lastmod"])  # no UPDATED: the English date
        xml = self.client.get("/sitemaps/core.xml").content.decode()
        self.assertIn('<xhtml:link rel="alternate" hreflang="de" href="https://growsterr.com/de/pricing/"/>', xml)

    @override_settings(DEBUG=False)
    def test_not_found_speaks_the_language_of_the_path(self):
        html = self.get("/de/gibt-es-nicht/", status=404)
        self.assertIn('<html lang="de">', html)
        self.assertIn("Diese Seite hat einen anderen Weg genommen.", html)
        self.assertIn('<meta name="robots" content="noindex">', html)

    def test_legal_pages_stay_english_with_the_visitors_chrome(self):
        html = self.get("/terms/?lang=de")
        self.assertIn('<html lang="en">', html)
        self.assertIn('<header class="site-header" lang="de" dir="ltr">', html)
        self.assertIn("Jetzt starten", html)
        self.assertIn('<link rel="canonical" href="https://growsterr.com/terms/">', html)
        self.assertIn('href="/privacy/?lang=de"', html)
        arabic = self.get("/terms/?lang=ar")
        self.assertIn('<header class="site-header" lang="ar" dir="rtl">', arabic)
        # A language without a module (or an unknown code) keeps the English chrome.
        for query in ("?lang=xx", f"?lang={without_core_file() or 'xx'}"):
            html = self.get("/terms/" + query)
            self.assertIn('<header class="site-header">', html)
            self.assertIn("Get started", html)


class TranslationFileTests(SimpleTestCase):
    def test_every_translation_file_is_clean(self):
        """The real files in apps/core/i18n/: missing keys show in English and are fine while a
        translation is in progress; a broken shape, a lost placeholder or a forbidden word is not."""
        checked = 0
        for lang in LANGS:
            if i18n_check.has_file(lang.code):
                checked += 1
                with self.subTest(code=lang.code):
                    self.assertEqual(i18n_check.check(lang.code).problems, [])
        self.assertGreaterEqual(checked, 1)  # English at least


class MissingLanguageTests(TestCase):
    def test_a_core_page_in_a_language_without_a_module_is_a_404(self):
        code = without_core_file()
        if code is None:
            self.skipTest("every language has its core file")
        for path in (f"/{code}/", f"/{code}/pricing/", f"/{code}/how-it-works/", f"/{code}/about/"):
            with self.subTest(path=path):
                self.assertEqual(self.client.get(path).status_code, 404)
        self.assertEqual(i18n.chrome(code), i18n.chrome("en"))  # its chrome is English
        self.assertIsNone(i18n.page(code, "home"))

    def test_a_broken_language_file_falls_back_to_english(self):
        i18n.reset()
        self.addCleanup(i18n.reset)
        real = i18n.import_module

        def broken_german(name):
            if name == i18n.module_name("de"):
                raise SyntaxError("bad file")
            return real(name)

        with mock.patch("apps.core.i18n.import_module", side_effect=broken_german), self.assertLogs("apps.core.i18n"):
            self.assertIsNone(i18n.load("de"))
            self.assertEqual(i18n.chrome("de")["get_started"], "Get started")
            self.assertFalse(i18n.has_page("de", "home"))

    def test_every_site_language_has_a_flag(self):
        for lang in LANGS:
            for path in (lang.flag, lang.flag_2x):
                self.assertTrue(finders.find(path), path)

    def test_the_language_list(self):
        self.assertEqual(len(LANGS), 41)
        self.assertEqual(len({lang.code for lang in LANGS}), 41)
        self.assertEqual(LANGS[0].code, "en")
        self.assertEqual([lang.code for lang in LANGS if lang.rtl], ["ar"])
        self.assertEqual(LANG_BY_CODE["sr"].django, "sr_Latn")
        self.assertEqual(LANG_BY_CODE["mt"].django, "en")


class MergeTests(SimpleTestCase):
    def test_merge_is_key_by_key_and_keeps_the_english_shape(self):
        english = {"a": "A", "t": ("x", "y", "z"), "d": {"p": "P", "q": "Q"}, "l": ["1", "2"]}
        own = {"a": "Ä", "t": "wrong shape", "d": {"q": "Ö"}, "l": ["1"], "extra": "?"}
        self.assertEqual(i18n.merge(english, own), {"a": "Ä", "t": ("x", "y", "z"), "d": {"p": "P", "q": "Ö"}, "l": ["1", "2"]})

    def test_fill_leaves_unknown_braces_alone(self):
        from apps.core.views import fill

        self.assertEqual(fill({"x": ["{price} {nope}"]}, {"price": "$1"}), {"x": ["$1 {nope}"]})


class CheckI18nTests(LanguageTestCase):
    languages = {"de": GERMAN, "ga": {}}
    def test_english_is_complete_and_clean(self):
        report = i18n_check.check("en")
        self.assertTrue(report.ok, report.problems + report.missing)

    def test_a_partial_language_lists_what_is_missing_and_wrong(self):
        broken = {**GERMAN, "HOME": {**GERMAN["HOME"], "description": "Ab {prise} gratis.", "faqs": [("F", "A")]},
                  "PRICNG": {}}
        sys.modules[i18n.module_name("de")] = language_module("de", broken)
        report = i18n_check.check("de")
        self.assertIn("CHROME['meta_title']", report.missing)
        self.assertIn("HOW (the whole section): /de/how-it-works/ isn't served", report.missing)
        problems = "\n".join(report.problems)
        for text in ("lost placeholder {price}", "unknown placeholder {prise}", "forbidden word 'gratis'",
                     "HOME['faqs']: shape differs", "PRICNG: unknown name"):
            self.assertIn(text, problems)

    def test_irish_seo_is_a_word(self):
        irish = {"CHROME": {"footer_tagline": "Is é seo an bealach"}}
        sys.modules[i18n.module_name("ga")] = language_module("ga", irish)
        self.assertEqual(i18n_check.check("ga").problems, [])
        sys.modules[i18n.module_name("ga")] = language_module("ga", {"CHROME": {"footer_tagline": "SEO"}})
        self.assertIn("forbidden word 'SEO'", "\n".join(i18n_check.check("ga").problems))

    def test_the_command(self):
        out = StringIO()
        call_command("check_i18n", "en", stdout=out)
        self.assertIn("en: OK", out.getvalue())
        out = StringIO()
        with self.assertRaises(CommandError):
            call_command("check_i18n", "de", stdout=out)
        self.assertIn("missing  CHROME['meta_title']", out.getvalue())
        self.assertIn("de: to fix", out.getvalue())
        out = StringIO()
        with self.assertRaises(CommandError):  # the overview fails on files to fix: the partial German one here
            call_command("check_i18n", stdout=out)
        for lang in LANGS:  # every language gets its line
            self.assertIn(f"{lang.code} ({lang.name})", out.getvalue())



class I18nCheckPairsTests(TestCase):
    def test_dicts_inside_lists_compare_their_texts_not_their_keys(self):
        # HOW["flow"] is a list of dicts: the check must read the translated texts.
        from apps.core.i18n_check import _pairs

        ref = [{"title": "Choose", "points": ["One", "Two"]}]
        value = [{"title": "Wählen", "points": ["Eins", "Zwei"]}]
        self.assertEqual(_pairs(ref, value), [("Choose", "Wählen"), ("One", "Eins"), ("Two", "Zwei")])
