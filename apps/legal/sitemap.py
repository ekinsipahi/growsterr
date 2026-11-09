"""Sitemap contract: /sitemap.xml (apps.pages) calls entries() of every app's sitemap module.

entries() -> list of dicts:
    {"path": "/pricing/",                 # absolute path, starts and ends with "/"
     "lastmod": date | None,
     "alternates": [("de", "/de/pricing/"), ...]}   # hreflang set incl. x-default, [] if none
Only public, indexable pages; never account, order or admin URLs.

The legal pages are English only, so they have no alternates."""
from django.urls import reverse

from .pages import PAGES


def entries():
    return [{"path": reverse(f"legal:{key}"), "lastmod": page.updated, "alternates": []}
            for key, page in PAGES.items()]
