from django.conf import settings

from .languages import DEFAULT, LANG_BY_CODE


def site(request):
    lang = LANG_BY_CODE[DEFAULT]
    return {
        "SITE_URL": settings.SITE_URL,
        "canonical_url": settings.SITE_URL + request.path,
        "contact_email": settings.CONTACT_EMAIL,
        # Pages in another language set lang/rtl/alternates in their own context (they win).
        "lang": lang.code,
        "rtl": lang.rtl,
        "alternates": [],
    }
