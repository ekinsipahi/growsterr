"""/sitemap.xml: an index of per-section sitemaps, valid XML, hreflang alternates, public pages only."""
import xml.etree.ElementTree as ET
from datetime import date
from unittest import mock

from django.core.cache import cache
from django.test import TestCase, override_settings

from apps.pages import sitemaps
from apps.pages.registry import REGISTRY

from .helpers import page_data, registry, urlconf

NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9", "xhtml": "http://www.w3.org/1999/xhtml"}
SITE = "https://growsterr.com"


class SitemapTests(TestCase):
    def setUp(self):
        cache.clear()

    def get_xml(self, url):
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, url)
        self.assertTrue(response["Content-Type"].startswith("application/xml"))
        return ET.fromstring(response.content)  # raises on invalid XML

    def test_index_points_at_every_section(self):
        root = self.get_xml("/sitemap.xml")
        self.assertEqual(root.tag, f"{{{NS['sm']}}}sitemapindex")
        locs = [el.text for el in root.findall("sm:sitemap/sm:loc", NS)]
        self.assertIn(f"{SITE}/sitemaps/pages-en.xml", locs)
        for name, entries in sitemaps.app_sections().items():  # every app that lists public pages
            if sitemaps.clean(entries(), name):
                self.assertIn(f"{SITE}/sitemaps/{name}.xml", locs)
        for code in ("de", "tr"):  # a language without pages has no section
            if code not in REGISTRY.languages():
                self.assertNotIn(f"{SITE}/sitemaps/pages-{code}.xml", locs)
        for loc in locs:  # every section it lists exists and is valid
            self.get_xml(loc.removeprefix(SITE))

    def test_pages_section_lists_every_english_page_with_hreflang(self):
        root = self.get_xml("/sitemaps/pages-en.xml")
        self.assertEqual(root.tag, f"{{{NS['sm']}}}urlset")
        urls = {el.find("sm:loc", NS).text: el for el in root.findall("sm:url", NS)}
        self.assertEqual(sorted(urls), sorted(SITE + p.path for p in REGISTRY.pages_in("en")))
        entry = urls[f"{SITE}/instagram/followers/1000/"]
        self.assertEqual(entry.find("sm:lastmod", NS).text, "2026-11-08")
        links = {link.get("hreflang"): link.get("href") for link in entry.findall("xhtml:link", NS)}
        page = REGISTRY.find("en", "instagram", "followers", 1000)
        self.assertEqual(links, {code: SITE + path for code, path in REGISTRY.alternates(page)})
        self.assertEqual(links["x-default"], f"{SITE}/instagram/followers/1000/")

    def test_never_account_order_or_admin_urls(self):
        root = self.get_xml("/sitemap.xml")
        for loc in root.findall("sm:sitemap/sm:loc", NS):
            section = self.get_xml(loc.text.removeprefix(SITE))
            for url in section.findall("sm:url/sm:loc", NS):
                path = url.text.removeprefix(SITE)
                self.assertFalse(path.startswith(sitemaps.PRIVATE), path)

    def test_unknown_or_empty_section_is_404(self):
        self.assertEqual(self.client.get("/sitemaps/nope.xml").status_code, 404)
        self.assertEqual(self.client.get("/sitemaps/pages-xx.xml").status_code, 404)

    def test_clean_drops_private_and_malformed_entries(self):
        entries = [{"path": "/terms/"}, {"path": "/account/"}, {"path": "/order/?plan=pro"}, {"path": "no-slash"},
                   {"nope": 1}, "junk", {"path": "/terms/"}]
        self.assertEqual(sitemaps.clean(entries), [{"path": "/terms/"}])

    def test_other_apps_entries_are_merged(self):
        fake = {"legal": lambda: [{"path": "/terms/", "lastmod": date(2026, 11, 1),
                                   "alternates": [("en", "/terms/"), ("de", "/de/terms/"), ("x-default", "/terms/")]},
                                  {"path": "/account/", "lastmod": None, "alternates": []}]}
        with mock.patch.object(sitemaps, "app_sections", return_value=fake):
            root = self.get_xml("/sitemaps/legal.xml")
        urls = root.findall("sm:url", NS)
        self.assertEqual([u.find("sm:loc", NS).text for u in urls], [f"{SITE}/terms/"])
        self.assertEqual(urls[0].find("sm:lastmod", NS).text, "2026-11-01")
        self.assertEqual(len(urls[0].findall("xhtml:link", NS)), 3)


    def test_an_app_whose_entries_fail_is_left_out(self):
        def broken():
            raise RuntimeError("boom")

        with mock.patch.object(sitemaps, "app_sections", return_value={"legal": broken}), \
                self.assertLogs("apps.pages.sitemaps", level="ERROR"):
            root = self.get_xml("/sitemap.xml")
        locs = [el.text for el in root.findall("sm:sitemap/sm:loc", NS)]
        self.assertNotIn(f"{SITE}/sitemaps/legal.xml", locs)
        self.assertIn(f"{SITE}/sitemaps/pages-en.xml", locs)


class SitemapLanguagesTests(TestCase):
    """A German version of a page gets its own section, and both versions point at each other."""

    def setUp(self):
        cache.clear()
        german = page_data(service="followers")
        german["slug"] = "instagram/follower"
        self.reg = registry({("en", "instagram"): [page_data(), page_data(service="followers")],
                             ("de", "instagram"): [german]})

    def test_language_sections_and_alternates(self):
        with override_settings(ROOT_URLCONF=urlconf(self.reg)):
            index = ET.fromstring(self.client.get("/sitemap.xml").content)
            locs = [el.text for el in index.findall("sm:sitemap/sm:loc", NS)]
            self.assertIn(f"{SITE}/sitemaps/pages-de.xml", locs)
            german = ET.fromstring(self.client.get("/sitemaps/pages-de.xml").content)
        entry = german.find("sm:url", NS)
        self.assertEqual(entry.find("sm:loc", NS).text, f"{SITE}/de/instagram/follower/")
        links = {link.get("hreflang"): link.get("href") for link in entry.findall("xhtml:link", NS)}
        self.assertEqual(links, {"en": f"{SITE}/instagram/followers/", "de": f"{SITE}/de/instagram/follower/",
                                 "x-default": f"{SITE}/instagram/followers/"})
