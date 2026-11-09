"""/sitemap.xml: a sitemap index with one sitemap per section. Sections come from every app's
sitemap.entries() (the contract is in apps/core/sitemap.py; the section is named after the app)
and from the money pages, one section per language (pages-en, pages-de...).

Only public pages: an entry under a private prefix (account, order, admin) or not shaped like a
path is dropped and logged, whichever app sent it.
"""
import logging
from datetime import date, datetime
from functools import partial
from importlib import import_module
from xml.sax.saxutils import escape, quoteattr

from django.apps import apps as django_apps
from django.utils.encoding import iri_to_uri

logger = logging.getLogger(__name__)

PRIVATE = ("/admin/", "/account/", "/order/", "/growth/")
SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
XHTML_NS = "http://www.w3.org/1999/xhtml"


def app_sections():
    """{app label: entries function} for every project app with a sitemap module, pages excluded."""
    out = {}
    for config in django_apps.get_app_configs():
        if not config.name.startswith("apps.") or config.name == "apps.pages":
            continue
        name = f"{config.name}.sitemap"
        try:
            module = import_module(name)
        except ModuleNotFoundError as error:
            if error.name == name:
                continue
            raise
        if callable(getattr(module, "entries", None)):
            out[config.label] = module.entries
    return out


def sections(registry):
    """{section name: entries function}, in index order."""
    out = app_sections()
    for code in registry.languages():
        out[f"pages-{code}"] = partial(registry.sitemap_entries, code)
    return out


def rows(entries, section=""):
    """A section's entries, cleaned. An app whose entries() fails is logged and left out, so one
    app's bug never takes the whole sitemap down (check_pages reports it)."""
    try:
        raw = entries()
    except Exception:  # noqa: BLE001
        logger.exception("sitemap %s: entries() failed", section)
        return []
    return clean(raw, section)


def clean(entries, section=""):
    """The public, well-formed entries; each path once."""
    out, seen = [], set()
    for entry in entries or []:
        path = entry.get("path") if isinstance(entry, dict) else None
        if not isinstance(path, str) or not path.startswith("/") or path.startswith(PRIVATE):
            logger.warning("sitemap %s: dropped entry %r (not a public page path)", section, entry)
            continue
        if path not in seen:
            seen.add(path)
            out.append(entry)
    return out


def w3c_date(value):
    if isinstance(value, datetime):
        return value.date().isoformat()
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, str) and value:
        try:
            return date.fromisoformat(value[:10]).isoformat()
        except ValueError:
            return None
    return None


def latest(entries):
    dates = [d for d in (w3c_date(e.get("lastmod")) for e in entries) if d]
    return max(dates) if dates else None


def url(site, path):
    return escape(site + iri_to_uri(path))


def urlset(entries, site):
    rows = []
    for entry in entries:
        parts = [f"<loc>{url(site, entry['path'])}</loc>"]
        lastmod = w3c_date(entry.get("lastmod"))
        if lastmod:
            parts.append(f"<lastmod>{lastmod}</lastmod>")
        for code, path in entry.get("alternates") or []:
            parts.append(f'<xhtml:link rel="alternate" hreflang={quoteattr(code)} href="{url(site, path)}"/>')
        rows.append("<url>" + "".join(parts) + "</url>")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<urlset xmlns="{SITEMAP_NS}" xmlns:xhtml="{XHTML_NS}">\n' + "\n".join(rows) + "\n</urlset>\n")


def index(items, site):
    """items: [(sitemap path, lastmod or None)]."""
    rows = []
    for path, lastmod in items:
        tail = f"<lastmod>{lastmod}</lastmod>" if lastmod else ""
        rows.append(f"<sitemap><loc>{url(site, path)}</loc>{tail}</sitemap>")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<sitemapindex xmlns="{SITEMAP_NS}">\n' + "\n".join(rows) + "\n</sitemapindex>\n")
