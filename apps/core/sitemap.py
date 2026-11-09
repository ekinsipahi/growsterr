"""Sitemap contract: /sitemap.xml (apps.pages) calls entries() of every app's sitemap module.

entries() -> list of dicts:
    {"path": "/pricing/",                 # absolute path, starts and ends with "/"
     "lastmod": date | None,
     "alternates": [("de", "/de/pricing/"), ...]}   # hreflang set incl. x-default, [] if none
Only public, indexable pages; never account, order or admin URLs.

The core pages in every language that has them (apps/core/i18n/<code>.py), in site order;
each lists the whole hreflang set of its page. lastmod is the language module's UPDATED."""
from . import i18n
from .languages import LANGS


def entries():
    return [{"path": i18n.path(page, lang.code), "lastmod": i18n.updated(lang.code), "alternates": i18n.alternates(page)}
            for lang in LANGS for page in i18n.PAGES if i18n.has_page(lang.code, page)]
