"""The legal pages. Titles, dates and sections: pages.py; the text: templates/legal/<key>.html.

The text is English only (legal translations need a lawyer). The header and footer follow the
visitor's language: ?lang=<code> (the chrome's legal links carry it) when that language has its
chrome (apps/core/i18n/<code>.py); the page itself stays <html lang="en">, the chrome gets its own lang."""
from urllib.parse import urlsplit

from django.conf import settings
from django.shortcuts import render
from django.urls import reverse

from .company import COMPANY
from .pages import PAGES

DAY = 24 * 60 * 60


def chrome_lang(request):
    """The language the visitor came from (?lang=), when the chrome speaks it; else None (English)."""
    from apps.core import i18n
    from apps.core.languages import DEFAULT, LANG_BY_CODE

    code = request.GET.get("lang")
    if code and code != DEFAULT and code in LANG_BY_CODE and i18n.has_module(code):
        return LANG_BY_CODE[code]
    return None


def page(request, key):
    legal = PAGES[key]
    ui_lang = chrome_lang(request)
    query = f"?lang={ui_lang.code}" if ui_lang else ""
    whatsapp = "".join(c for c in getattr(settings, "WHATSAPP_NUMBER", "") if c.isdigit())
    context = {
        "page": legal,
        "toc": legal.toc(),
        "company": COMPANY,
        "site_host": urlsplit(settings.SITE_URL).hostname or "growsterr.com",
        "whatsapp_display": getattr(settings, "WHATSAPP_DISPLAY", "") if whatsapp else "",
        "whatsapp_url": f"https://wa.me/{whatsapp}" if whatsapp else "",
        "legal_nav": [{"label": p.nav, "url": reverse(f"legal:{k}") + query, "current": k == key} for k, p in PAGES.items()],
    }
    if ui_lang:
        context.update(ui_lang=ui_lang.code, ui_rtl=ui_lang.rtl)
    if key == "terms":
        context.update(_terms())
    elif key == "cookies":
        context.update(_cookies())
    return render(request, f"legal/{key}.html", context)


def _terms():
    # Imported here so a half-finished growth app can only break this page, never the URLconf.
    from apps.growth.constants import TERMS_VERSION
    from apps.growth.plan import NAMES, PLANS, money

    return {"terms_version": TERMS_VERSION,
            "packages": [(NAMES[p["key"]], money(p["price"])) for p in PLANS]}


def duration(seconds):
    """1209600 -> '2 weeks', 31449600 -> '1 year'."""
    days = round(seconds / DAY)
    if days >= 360:
        years = max(1, round(days / 365))
        return "1 year" if years == 1 else f"{years} years"
    if days >= 7 and days % 7 == 0:
        weeks = days // 7
        return "1 week" if weeks == 1 else f"{weeks} weeks"
    if days >= 1:
        return "1 day" if days == 1 else f"{days} days"
    hours = max(1, round(seconds / 3600))
    return "1 hour" if hours == 1 else f"{hours} hours"


def _cookies():
    """The cookie table follows the settings: names, lifetimes, and which cookies exist at all."""
    messages_in_cookie = ("django.contrib.messages" in settings.INSTALLED_APPS
                          and not settings.MESSAGE_STORAGE.endswith("SessionStorage"))
    return {
        "session_cookie": settings.SESSION_COOKIE_NAME,
        "session_expires": ("When you close your browser" if settings.SESSION_EXPIRE_AT_BROWSER_CLOSE
                            else f"After {duration(settings.SESSION_COOKIE_AGE)}, or when you sign out"),
        "csrf_cookie": "" if settings.CSRF_USE_SESSIONS else settings.CSRF_COOKIE_NAME,
        "csrf_expires": ("When you close your browser" if settings.CSRF_COOKIE_AGE is None
                         else f"After {duration(settings.CSRF_COOKIE_AGE)}"),
        "messages_cookie": "messages" if messages_in_cookie else "",
    }
