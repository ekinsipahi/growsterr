from django.conf import settings

from .company import COMPANY
from .languages import DEFAULT, LANG_BY_CODE


def site(request):
    lang = LANG_BY_CODE[DEFAULT]
    return {
        "SITE_URL": settings.SITE_URL,
        "canonical_url": settings.SITE_URL + request.path,
        "contact_email": settings.CONTACT_EMAIL,
        "whatsapp_digits": "".join(c for c in settings.WHATSAPP_NUMBER if c.isdigit()),  # the fixed WhatsApp button
        # Pages in another language set lang/rtl/alternates (and lang_links for the language
        # switcher: [(Lang, path)]) in their own context (they win). base.html takes the chrome's
        # strings and links from that lang (apps.core.i18n), or from ui_lang when a page sets it
        # (an English legal page reached from another language).
        "lang": lang.code,
        "rtl": lang.rtl,
        "alternates": [],
        "company": COMPANY,
    }
