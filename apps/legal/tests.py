import re
from datetime import date
from html.parser import HTMLParser

from django.conf import settings
from django.template import Context, Template, TemplateSyntaxError
from django.test import TestCase, override_settings
from django.urls import reverse

from apps.growth.constants import TERMS_VERSION
from apps.growth.plan import NAMES, PLANS, money

from . import sitemap
from .company import COMPANY
from .pages import PAGES
from .views import duration

# Copy rules for every visible string: nothing about search engines or rankings, no "guarantee",
# no "free", no crypto, no verified/celebrity comments, no gender targeting, no reviews or statistics,
# no competitor names.
FORBIDDEN = re.compile(
    r"\bseo\b|\bsearch|\brank|keyword|optimi[sz]|guarantee|\bwarrant|\bfree|crypto|bitcoin|\bverified\b|celebrit"
    r"|gender|testimonial|\brating|statistic|\bbuzzoid|\bfamoid|\btwicsy|\bstormlikes|\buseviral|\bsidesmedia"
    r"|media ?mister|\bsocialwick|\bgoread",
    re.IGNORECASE,
)
PATHS = {"terms": "/terms/", "privacy": "/privacy/", "cookies": "/cookies/", "refunds": "/refunds/"}


class Doc(HTMLParser):
    """What the tests look at in a rendered page: ids, links, headings and the visible text."""

    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.ids, self.anchors, self.toc, self.headings, self.links = [], [], [], [], []
        self.text, self.title, self.description, self.h1 = [], [], "", 0
        self.current = []
        self._main = self._title = self._skip = False
        self.feed(html)
        self.text = re.sub(r"\s+", " ", " ".join(self.text))
        self.title = "".join(self.title).strip()

    def handle_starttag(self, tag, attrs):
        a = {k: v or "" for k, v in attrs}
        if a.get("id"):
            self.ids.append(a["id"])
        if tag == "main":
            self._main = True
        elif tag == "title":
            self._title = True
        elif tag in ("script", "style"):
            self._skip = True
        elif tag == "meta" and a.get("name") == "description":
            self.description = a.get("content", "")
        elif tag == "h1" and self._main:
            self.h1 += 1
        elif tag == "h2" and self._main and a.get("id"):
            self.headings.append(a["id"])
        elif tag == "a" and self._main:
            href = a.get("href", "")
            self.links.append(href)
            if href.startswith("#"):
                self.anchors.append(href[1:])
                if "toc-link" in a.get("class", "").split():
                    self.toc.append(href[1:])
            if a.get("aria-current") == "page":
                self.current.append(href)

    def handle_endtag(self, tag):
        if tag == "main":
            self._main = False
        elif tag == "title":
            self._title = False
        elif tag in ("script", "style"):
            self._skip = False

    def handle_data(self, data):
        if self._title:
            self.title.append(data)
        elif self._main and not self._skip:
            self.text.append(data)


class LegalPagesTests(TestCase):
    def doc(self, key):
        response = self.client.get(PATHS[key])
        self.assertEqual(response.status_code, 200, key)
        return Doc(response.content.decode())

    def test_urls(self):
        for key, path in PATHS.items():
            self.assertEqual(reverse(f"legal:{key}"), path)

    def test_every_page_renders_with_its_title_and_date(self):
        for key, page in PAGES.items():
            with self.subTest(key):
                doc = self.doc(key)
                self.assertEqual(doc.h1, 1)
                self.assertIn(page.title, doc.title)
                self.assertEqual(doc.description, page.description)
                self.assertIn(f"Last updated {page.updated:%-d %B %Y}", doc.text)
                self.assertEqual(doc.current, [PATHS[key]])  # the legal links mark this page

    def test_terms_subscription_anchor_and_version(self):
        doc = self.doc("terms")
        self.assertIn("subscription", doc.ids)
        self.assertIn("subscription", doc.toc)
        self.assertIn(f"Version {TERMS_VERSION}", doc.text)

    def test_toc_and_headings_match_and_every_anchor_resolves(self):
        for key, page in PAGES.items():
            with self.subTest(key):
                doc = self.doc(key)
                sections = [sid for sid, _ in page.sections]
                self.assertEqual(doc.headings, sections)                 # every section, in order
                self.assertEqual(list(dict.fromkeys(doc.toc)), sections)  # the contents list all of them
                self.assertEqual(len(doc.ids), len(set(doc.ids)), "duplicate ids")
                for anchor in doc.anchors:
                    self.assertIn(anchor, doc.ids)

    def test_links_to_sections_of_other_legal_pages_resolve(self):
        docs = {PATHS[key]: self.doc(key) for key in PAGES}
        for path, doc in docs.items():
            for href in doc.links:
                target, _, anchor = href.partition("#")
                if anchor and target in docs:
                    with self.subTest(page=path, href=href):
                        self.assertIn(anchor, docs[target].ids)
        self.assertIn("/terms/#subscription", docs["/refunds/"].links)

    def test_no_forbidden_words(self):
        for key in PAGES:
            with self.subTest(key):
                doc = self.doc(key)
                for text in (doc.title, doc.description, doc.text):
                    self.assertIsNone(FORBIDDEN.search(text), FORBIDDEN.search(text))

    def test_terms_describe_the_service(self):
        text = self.doc("terms").text
        for phrase in ("Instagram, TikTok and YouTube", "real people", "typical monthly ranges, not promises",
                       "We don't use bots", "We never ask for the password", "renews automatically every month",
                       "3 days before each renewal", "Cancel subscription", "until the end of the period you've already paid for",
                       "the month you've paid for isn't refunded", "pause your package until it's paid",
                       "Account activity", "Delivery records", "community guidelines", "We may decline an order",
                       "not affiliated with, endorsed by or sponsored by", "trademarks of their owners",
                       "governed by the laws of Estonia", COMPANY["legal_name"], COMPANY["registry_code"],
                       settings.CONTACT_EMAIL):
            self.assertIn(phrase, text)
        for p in PLANS:
            self.assertIn(f"{NAMES[p['key']]} at {money(p['price'])} a month", text)
        if getattr(settings, "WHATSAPP_NUMBER", ""):  # the contact card shows the WhatsApp line, as Sterr Agency's does
            self.assertIn(settings.WHATSAPP_DISPLAY, text)

    def test_privacy_lists_the_data_and_every_service(self):
        text = self.doc("privacy").text
        for name in ("Stripe", "Google", "Resend", "Supabase", "Render", "Linksterr"):
            self.assertIn(name, text)
        for phrase in ("phone number", "target location", "Delivery numbers", "Account activity", "Art. 6(1)(b)",
                       "Standard Contractual Clauses", "Andmekaitse Inspektsioon", "within one month", "18 or older"):
            self.assertIn(phrase, text)

    def test_cookie_table_follows_the_settings(self):
        text = self.doc("cookies").text
        for phrase in (settings.SESSION_COOKIE_NAME, settings.CSRF_COOKIE_NAME, "messages", "theme",
                       "After 2 weeks, or when you sign out", "After 1 year", "No analytics"):
            self.assertIn(phrase, text)

    @override_settings(SESSION_EXPIRE_AT_BROWSER_CLOSE=True, CSRF_USE_SESSIONS=True,
                       MESSAGE_STORAGE="django.contrib.messages.storage.session.SessionStorage")
    def test_cookie_table_leaves_out_cookies_that_are_not_set(self):
        text = self.doc("cookies").text
        self.assertIn("When you close your browser", text)
        self.assertNotIn(settings.CSRF_COOKIE_NAME, text)
        self.assertNotIn("one-time notice", text)

    def test_refunds_match_the_terms(self):
        text = self.doc("refunds").text
        for phrase in ("the month you've paid for isn't refunded", "3 days before each renewal", "Cancel subscription",
                       "we pause your package", "unused part of the month"):
            self.assertIn(phrase, text)

    def test_sitemap_entries(self):
        entries = sitemap.entries()
        self.assertEqual({e["path"] for e in entries}, set(PATHS.values()))
        for entry in entries:
            self.assertIsInstance(entry["lastmod"], date)
            self.assertEqual(entry["alternates"], [])

    def test_unknown_section_is_an_error(self):
        template = Template('{% load legal_tags %}{% section "nope" %}text{% endsection %}')
        with self.assertRaises(TemplateSyntaxError):
            template.render(Context({"toc": [{"id": "who-we-are", "title": "Who we are", "number": 1}]}))

    def test_duration(self):
        self.assertEqual(duration(1209600), "2 weeks")
        self.assertEqual(duration(31449600), "1 year")
        self.assertEqual(duration(86400 * 3), "3 days")
        self.assertEqual(duration(3600), "1 hour")
