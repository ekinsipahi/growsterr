"""The core pages (home, pricing, how it works, about) in every language that has them, plus
robots.txt, /favicon.ico and the 404 page. English lives at /, another language at /<code>/
once apps/core/i18n/<code>.py has that page's copy (apps/core/urls.py builds the routes)."""
from django.conf import settings
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.templatetags.static import static
from django.views.decorators.cache import cache_page

from apps.growth.content import ui_for
from apps.growth.plan import LOWEST, for_page, money

from . import content, i18n
from .company import COMPANY
from .languages import DEFAULT, LANG_BY_CODE

PLATFORMS = content.PLATFORMS
PLATFORM_KEYS = tuple(key for key, _ in PLATFORMS)


def packages(lang=DEFAULT, active="instagram"):
    """The packages of every platform for templates/partials/packages_tabs.html."""
    out = []
    for key, name in PLATFORMS:
        gu = ui_for(lang, key)
        out.append({"key": key, "name": name, "title": gu.get("see_packages", name), "gu": gu,
                    "plans": for_page(lang, gu), "active": key == active})
    return out


def _span(plan, name):
    """A plan's typical monthly range as display text ("1,000–4,000"); for_page() already
    formats it in the page's language."""
    value = plan.get(name)
    if isinstance(value, (tuple, list)):
        return f"{value[0]:,}–{value[1]:,}"
    return value or ""


def fill(value, values):
    """Every {key} of `values` replaced in a string, or in every string of a list, tuple or dict.
    Unknown braces are left alone, so a translator's typo can't break the page."""
    if isinstance(value, str):
        for key, text in values.items():
            value = value.replace("{" + key + "}", str(text))
        return value
    if isinstance(value, (list, tuple)):
        return type(value)(fill(v, values) for v in value)
    if isinstance(value, dict):
        return {k: fill(v, values) for k, v in value.items()}
    return value


def _ranges(plans):
    """{price}, {starter}, {rising}, {pro}: the lowest price and each package's follower range."""
    return {"price": money(LOWEST), **{p["key"]: _span(p, "followers") for p in plans}}


def _copy(page, lang):
    """A page's copy in the language, or a 404 when the language doesn't have that page."""
    c = i18n.page(lang, page)
    if c is None:
        raise Http404
    return c


def _context(page, lang, c, **extra):
    """What every core page needs: its copy, the language attributes and its hreflang set."""
    language = LANG_BY_CODE[lang]
    cta = dict(c["cta"])
    cta["secondary_url"] = i18n.site_links(lang)[content.CTA_SECONDARY[page]]
    canonical = settings.SITE_URL + i18n.path(page, lang)
    return {
        "c": c, "cta": cta, "title": c["title"], "description": c["description"],
        "lang": lang, "rtl": language.rtl, "og_locale": language.og_locale,
        "og_alternates": [LANG_BY_CODE[code].og_locale for code in i18n.languages(page) if code != lang],
        "alternates": i18n.alternates(page), "lang_links": i18n.lang_links(page), "canonical_url": canonical,
        **extra,
    }


def home(request, lang=DEFAULT):
    c = _copy("home", lang)
    pkgs = packages(lang)
    c = fill(c, _ranges(pkgs[0]["plans"]))
    platform_cards = [{"key": key, "name": name, "url": i18n.site_links(lang)[key], **content.PLATFORM_CARDS[key],
                       **c["platforms"][key]} for key, name in PLATFORMS]
    dash = {"labels": c["dash"], "bars": content.DASHBOARD_BARS, "caption": c["dash"]["caption"],
            "points": [(icon, title, text) for icon, (title, text) in zip(content.DASHBOARD_ICONS, c["dash"]["points"])]}
    return render(request, "core/home.html", _context(
        "home", lang, c, faqs=c["faqs"], platform_cards=platform_cards, steps=c["steps"], compare=c["compare"],
        dash=dash, packages=pkgs, hero_image=content.HERO_IMAGE))


def pricing(request, lang=DEFAULT):
    c = _copy("pricing", lang)
    active = request.GET.get("platform")
    active = active if active in PLATFORM_KEYS else "instagram"
    pkgs = packages(lang, active=active)
    gu = pkgs[0]["gu"]
    plans = pkgs[0]["plans"]
    c = fill(c, _ranges(plans))
    rows = c["rows"]
    # Package comparison: ranges and extras come from the growth app, so the table follows its data.
    extras = []
    for p in plans:
        for item in gu.get(f"plan_{p['key']}_extra", []):
            if item not in extras:
                extras.append(item)

    def cells(**values):
        return [{"popular": p.get("popular", False), **{k: v(p) for k, v in values.items()}} for p in plans]

    compare = [
        (rows["followers"], cells(text=lambda p: _span(p, "followers"))),
        (rows["likes"], cells(text=lambda p: _span(p, "likes"))),
        (rows["comments"], cells(text=lambda p: _span(p, "comments"))),
        (rows["views"], cells(yes=lambda p: True)),
        (rows["spread"], cells(yes=lambda p: True)),
        (rows["location"], cells(yes=lambda p: True)),
        (rows["dashboard"], cells(yes=lambda p: True)),
    ] + [(item, cells(yes=lambda p, item=item: item in gu.get(f"plan_{p['key']}_extra", []))) for item in extras]
    return render(request, "core/pricing.html", _context(
        "pricing", lang, c, nav_active="pricing", packages=pkgs, plans=plans, compare_rows=compare,
        included=[(icon, title, text) for icon, (title, text) in zip(content.INCLUDED_ICONS, c["included"])],
        price_row=cells(text=lambda p: p["amount"], per=lambda p: gu.get("per_month", "")),
        policy=gu.get("policy", ""), faqs=c["billing_faqs"]))


def how(request, lang=DEFAULT):
    c = _copy("how", lang)
    flow = [{**art, **step} for art, step in zip(content.FLOW, c["flow"])]
    return render(request, "core/how.html", _context("how", lang, c, nav_active="how", flow=flow, faqs=c["faqs"]))


def about(request, lang=DEFAULT):
    raw = _copy("about", lang)
    c = fill(raw, COMPANY)
    # The row that names the sister brand links to its site.
    rows = [(label, value, COMPANY["sister_url"] if "{sister_brand}" in source else "")
            for (label, value), (_, source) in zip(c["rows"], raw["rows"])]
    return render(request, "core/about.html", _context(
        "about", lang, c, nav_active="about", rows=rows, company=COMPANY, image=content.ABOUT_IMAGE,
        values=[(icon, title, text) for icon, (title, text) in zip(content.VALUES_ICONS, c["values"])]))


def not_found(request, exception=None):
    """The 404 page, in the language of the path's prefix when that language has a module."""
    lang = i18n.path_lang(request.path)
    return render(request, "404.html", {"lang": lang, "rtl": LANG_BY_CODE[lang].rtl}, status=404)


@cache_page(60 * 60)
def robots_txt(request):
    lines = ["User-agent: *", "Allow: /", "Disallow: /admin/", "Disallow: /account/", "Disallow: /order/",
             f"Sitemap: {settings.SITE_URL}/sitemap.xml"]
    return HttpResponse("\n".join(lines) + "\n", content_type="text/plain")


def favicon(request):
    """Browsers ask for /favicon.ico; send them to the icon file."""
    response = HttpResponse(status=301)
    response["Location"] = static("img/favicon.ico")
    return response
