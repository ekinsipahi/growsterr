"""hreflang alternates, the language menu, html lang/dir, for pages in more than one language."""
from django.test import TestCase, override_settings

from apps.pages.registry import Variant

from .helpers import page_data, registry, urlconf

SITE = "https://growsterr.com"


def german(data, slug):
    return {**data, "slug": slug, "title": "Echte Instagram-Follower jeden Monat | Growsterr"}


class AlternatesTests(TestCase):
    def setUp(self):
        hub, followers, goal = page_data(), page_data(service="followers"), page_data(service="followers", quantity=1000)
        self.reg = registry({
            ("en", "instagram"): [hub, followers, goal],
            ("de", "instagram"): [german(hub, "instagram"), german(followers, "instagram/follower")],
            ("ar", "instagram"): [{**followers, "slug": "instagram/followers"}],
        })
        self.en = self.reg.find("en", "instagram", "followers")
        self.de = self.reg.find("de", "instagram", "followers")
        self.goal = self.reg.find("en", "instagram", "followers", 1000)

    def test_alternates_list_every_language_that_has_the_page_plus_x_default(self):
        expected = [("en", "/instagram/followers/"), ("de", "/de/instagram/follower/"), ("ar", "/ar/instagram/followers/"),
                    ("x-default", "/instagram/followers/")]
        self.assertEqual(self.reg.alternates(self.en), expected)
        self.assertEqual(self.reg.alternates(self.de), expected)
        # A page only English has: itself and x-default, never a missing German page.
        self.assertEqual(self.reg.alternates(self.goal), [("en", "/instagram/followers/1000/"),
                                                         ("x-default", "/instagram/followers/1000/")])

    def test_no_x_default_without_an_english_version(self):
        reg = registry({("de", "instagram"): [german(page_data(service="followers"), "instagram/follower")]})
        page = reg.find("de", "instagram", "followers")
        self.assertEqual(reg.alternates(page), [("de", "/de/instagram/follower/")])

    def test_language_menu_falls_back_to_the_nearest_page(self):
        links = {lang.code: path for lang, path in self.reg.lang_links(self.goal)}
        # German has no 1,000 page: its followers page is the nearest; Arabic has the followers page too.
        self.assertEqual(links, {"en": "/instagram/followers/1000/", "de": "/de/instagram/follower/",
                                 "ar": "/ar/instagram/followers/"})
        self.assertEqual(self.reg.nearest("de", Variant("instagram", "likes")).path, "/de/instagram/")

    def test_rendered_head_and_html_attributes(self):
        with override_settings(ROOT_URLCONF=urlconf(self.reg)):
            html = self.client.get("/de/instagram/follower/").content.decode()
            arabic = self.client.get("/ar/instagram/followers/").content.decode()
            self.assertEqual(self.client.get("/de/instagram/followers/1000/").status_code, 404)
        self.assertIn('<html lang="de">', html)
        self.assertIn(f'<link rel="canonical" href="{SITE}/de/instagram/follower/">', html)
        for code, path in (("en", "/instagram/followers/"), ("de", "/de/instagram/follower/"),
                           ("ar", "/ar/instagram/followers/"), ("x-default", "/instagram/followers/")):
            self.assertIn(f'<link rel="alternate" hreflang="{code}" href="{SITE}{path}">', html)
        self.assertIn('href="/order/?plan=rising&amp;platform=instagram&amp;lang=de"', html)
        self.assertIn('<a href="/de/instagram/">', html)  # breadcrumbs stay in the language
        self.assertIn('<html lang="ar" dir="rtl">', arabic)
