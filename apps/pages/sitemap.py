"""Sitemap contract: /sitemap.xml (apps.pages) calls entries() of every app's sitemap module.

entries() -> list of dicts:
    {"path": "/pricing/",                 # absolute path, starts and ends with "/"
     "lastmod": date | None,
     "alternates": [("de", "/de/pricing/"), ...]}   # hreflang set incl. x-default, [] if none
Only public, indexable pages; never account, order or admin URLs.

The money pages: every page of every language (/sitemap.xml lists them one section per language)."""


def entries():
    from .registry import REGISTRY

    return REGISTRY.sitemap_entries()
