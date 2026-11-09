"""Routing, 404 for content that doesn't exist, and what every page shows."""
from apps.pages import dimensions as dims
from django.test import TestCase

from apps.pages.checks import forbidden_in
from apps.pages.registry import REGISTRY

from .helpers import visible_text

ENGLISH = ["/instagram/", "/tiktok/", "/youtube/", "/instagram/followers/", "/instagram/followers/1000/",
           "/tiktok/likes/", "/youtube/subscribers/"]


class RoutingTests(TestCase):
    def test_every_page_answers(self):
        self.assertLessEqual(set(ENGLISH), {p.path for p in REGISTRY.pages_in("en")})
        for page in REGISTRY.pages:
            with self.subTest(page=page.name):
                response = self.client.get(page.path)
                self.assertEqual(response.status_code, 200)
                expected = ("pages/hub.html" if page.variant.is_hub else
                            "pages/article.html" if page.data.get("kind") == "guide" else "pages/page.html")
                self.assertTemplateUsed(response, expected)

    def test_a_variant_without_content_does_not_exist(self):
        # Paths no content file will ever have (the content grows; these tests must not depend on it).
        for url in ("/instagram/followers/2499/", "/instagram/followers/never-a-modifier/", "/tiktok/nothing-here/",
                    "/youtube/likes/123457/", "/xx/instagram/", "/de/instagram/never-a-slug/", "/facebook/"):
            with self.subTest(url=url):
                self.assertEqual(self.client.get(url).status_code, 404)

    def test_missing_trailing_slash_redirects(self):
        response = self.client.get("/instagram/followers")
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response["Location"], "/instagram/followers/")

    def test_registry_paths_for_other_apps(self):
        self.assertEqual(REGISTRY.path("en", "instagram"), "/instagram/")
        self.assertEqual(REGISTRY.path("en", "instagram", "followers", 1000), "/instagram/followers/1000/")
        self.assertIsNone(REGISTRY.path("en", "instagram", "followers", 2499))
        de = REGISTRY.find("de", "instagram")
        self.assertEqual(REGISTRY.path("de", "instagram"), de.path if de else None)


class PageContentTests(TestCase):
    def test_money_page_has_every_block(self):
        html = self.client.get("/instagram/followers/").content.decode()
        self.assertIn('<h1 class="h1" id="page-title">Instagram followers <span class="hl">who chose to follow you.</span></h1>', html)
        self.assertIn('<link rel="canonical" href="https://growsterr.com/instagram/followers/">', html)
        self.assertIn("<title>Buy Real Instagram Followers, Every Month | Growsterr</title>", html)
        self.assertIn('name="description" content="Buy Instagram followers who are real people', html)
        # The most popular package is preselected; the cards link to the order form too.
        self.assertIn('href="/order/?plan=rising&amp;platform=instagram&amp;lang=en"', html)
        self.assertIn("Start with Rising Influencer", html)
        for name in ("Starter Creator", "Rising Influencer", "Pro Influencer"):
            self.assertIn(name, html)
        for block in ("What&#x27;s included", "How it works", "Real people, not bots", "Questions, answered", "Keep exploring"):
            self.assertIn(block, html)
        # Breadcrumbs: home, the hub, this page.
        self.assertIn('<a href="/">Home</a>', html)
        self.assertIn('<a href="/instagram/">Instagram</a>', html)
        self.assertIn('<span aria-current="page">Instagram followers</span>', html)
        # No quantity section on a page without a quantity.
        self.assertNotIn('id="pace"', html)

    def test_quantity_page_preselects_the_package_that_reaches_the_goal(self):
        html = self.client.get("/instagram/followers/1000/").content.decode()
        self.assertIn('href="/order/?plan=starter&amp;platform=instagram&amp;lang=en"', html)
        self.assertIn('id="pace"', html)
        self.assertIn("How you get to 1,000 followers", html)
        self.assertIn("Typical pace with Starter Creator", html)
        self.assertIn("usually within the first month", html)
        self.assertIn("never a promise", html)
        self.assertIn('<a href="/instagram/followers/">Instagram followers</a>', html)
        # Related: the service page above it, and the same service on YouTube (subscribers).
        # The same goal on another platform: that exact page when it exists, else its service page.
        youtube = REGISTRY.find("en", "youtube", "subscribers", 1000) or REGISTRY.find("en", "youtube", "subscribers")
        self.assertIn(f'href="{youtube.path}"', html)

    def test_hub_links_to_its_pages_and_the_other_hubs(self):
        html = self.client.get("/instagram/").content.decode()
        self.assertIn('href="/instagram/followers/"', html)
        self.assertIn('href="/instagram/followers/1000/"', html)
        self.assertIn('href="/tiktok/"', html)
        self.assertIn('href="/youtube/"', html)
        self.assertIn("Inside every package", html)  # likes, views, comments have no page yet

    def test_placeholders_are_filled_from_the_packages(self):
        self.assertIn("1,000–4,000 new followers a month with Starter Creator", self.client.get("/instagram/followers/").content.decode())

    def test_images_wait_as_placeholders_until_the_files_exist(self):
        html = self.client.get("/tiktok/likes/").content.decode()
        self.assertIn('class="media media--violet pg-media" style="--ratio: 1600 / 1200"', html)
        self.assertNotIn("img/pages/tiktok/likes.webp", html)  # pending: no broken <img>

    def test_visible_copy_follows_the_rules(self):
        for page in REGISTRY.pages:
            html = self.client.get(page.path).content.decode()
            # The package cards are the growth app's copy; the rest of <main> is ours.
            # The "answers" links name intent pages in the searcher's words ("Free Instagram likes?").
            text = visible_text(html, skip={"plans", "pg-answers"})
            with self.subTest(page=page.name):
                # An intent page may use its own word ("free" on the free page), nothing else.
                allow = dims.allowed_rules(page.variant, page.data.get("kind", ""))
                self.assertEqual(forbidden_in(text, page.lang, allow), [])
                self.assertNotRegex(text, r"\{[a-z_]+\}")
