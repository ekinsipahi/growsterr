"""Pages outside the platform x service grid (articles), intent pages and split content files."""
from django.test import TestCase, override_settings

from apps.pages import dimensions as dims
from apps.pages.checks import validate
from apps.pages.registry import Variant, content_modules

from .helpers import jsonld, page_data, registry, urlconf


def article(key="can-you-buy-instagram-followers", kind="guide", slug="guides/can-you-buy-instagram-followers", **extra):
    data = {k: v for k, v in page_data().items() if k not in ("service", "quantity", "modifier", "country")}
    data.update({"article": key, "kind": kind, "slug": slug, "label": "Can you buy Instagram followers?",
                 "title": "Can You Buy Instagram Followers? The Honest Answer",
                 "description": "Yes, and most of what's sold is bots. What buying followers really gets you, what it costs your account, and the alternative that works."})
    data.update(extra)
    return data


def errors(reg):
    return [f"{p.where}: {p.message}" for p in validate(reg, live=False) if p.level == "error"]


class ArticleRegistryTests(TestCase):
    def test_an_article_is_its_own_page_paired_across_languages_by_key(self):
        reg = registry({("en", "articles"): [article()],
                        ("de", "articles"): [article(slug="ratgeber/instagram-follower-kaufen")]})
        en, de = reg.pages
        self.assertEqual(en.variant, Variant("instagram", article="can-you-buy-instagram-followers"))
        self.assertFalse(en.variant.is_hub)
        self.assertEqual(en.path, "/guides/can-you-buy-instagram-followers/")
        self.assertEqual(reg.alternates(en), [("en", en.path), ("de", de.path), ("x-default", en.path)])
        self.assertEqual(reg.ancestors(en), [])

    def test_article_mistakes_are_reported(self):
        reg = registry({("en", "articles"): [article(), article(kind="essay", slug="a"), article(key="Bad Key", slug="b"),
                                             {**article(slug="c"), "service": "followers"},
                                             article(slug="d")]})
        problems = [str(p) for p in reg.problems]
        self.assertTrue(any("'kind' must be one of" in p for p in problems), problems)
        self.assertTrue(any("'article' must be a key" in p for p in problems), problems)
        self.assertTrue(any("an article has no 'service'" in p for p in problems), problems)
        self.assertTrue(any("is defined twice" in p for p in problems), problems)

    def test_a_guide_renders_as_an_article_with_its_jsonld(self):
        reg = registry({("en", "instagram"): [page_data()], ("en", "articles"): [article()]})
        with override_settings(ROOT_URLCONF=urlconf(reg)):
            html = self.client.get("/guides/can-you-buy-instagram-followers/").content.decode()
        types = [block["@type"] for block in jsonld(html)]
        self.assertIn("Article", types)
        self.assertNotIn("Product", types)
        self.assertIn(">Guide<", html)

    def test_articles_are_in_the_sitemap(self):
        reg = registry({("en", "instagram"): [page_data()], ("en", "articles"): [article()]})
        paths = [entry["path"] for entry in reg.sitemap_entries("en")]
        self.assertIn("/guides/can-you-buy-instagram-followers/", paths)


class IntentPageTests(TestCase):
    def intent(self, modifier, **extra):
        data = page_data(service="followers")
        data.update({"modifier": modifier, "slug": f"instagram/followers/{modifier}"}, **extra)
        return data

    def test_an_intent_page_may_use_its_own_word_only(self):
        free = self.intent("free", title="Free Instagram Followers: What You Really Get",
                           intro="Free followers apps hand your password to bots. Here is what works instead, and why it isn't free.")
        reg = registry({("en", "instagram"): [page_data(), page_data(service="followers"), free]})
        found = errors(reg)
        self.assertFalse([e for e in found if "copy rule (free)" in e], found)
        guaranteed = self.intent("free", intro="We guarantee free followers to everyone who signs up today, no questions asked.")
        reg = registry({("en", "instagram"): [page_data(), page_data(service="followers"), guaranteed]})
        self.assertTrue([e for e in errors(reg) if "copy rule (guarantee)" in e])

    def test_other_pages_still_may_not(self):
        cheap = self.intent("cheap", intro="Free followers are bots. Here is what a real follower costs with a monthly package instead.")
        reg = registry({("en", "instagram"): [page_data(), page_data(service="followers"), cheap]})
        self.assertTrue([e for e in errors(reg) if "copy rule (free)" in e])

    def test_modifiers_limited_to_some_services(self):
        self.assertTrue(dims.modifier_allowed("comment-likes", "instagram", "likes"))
        self.assertFalse(dims.modifier_allowed("comment-likes", "instagram", "followers"))
        self.assertFalse(dims.modifier_allowed("reels", "youtube", "likes"))
        self.assertTrue(dims.modifier_allowed("high-retention", "youtube", "views"))


class ContentModuleTests(TestCase):
    def test_a_language_may_split_its_pages_into_parts(self):
        names = content_modules("apps.pages.content.en")
        self.assertIn("instagram", names)
        self.assertNotIn("ui", names)
        self.assertNotIn("__init__", names)
        self.assertTrue(all(n.split("_")[0] in dims.PLATFORMS or n.startswith("articles") for n in names))


class LocalIntentWordTests(TestCase):
    def test_an_intent_page_may_use_its_own_word_in_its_language_only(self):
        from apps.pages.checks import forbidden_in

        self.assertEqual(forbidden_in("Gratis volgers? Die bestaan niet.", "nl", allow=("free",)), [])
        found = forbidden_in("Gratis volgers, gegarandeerd.", "nl", allow=("free",))
        self.assertEqual([word for _, word in found], ["gegarandeerd"])
        self.assertTrue(forbidden_in("Ücretsiz takipçi yok.", "tr"))  # not an intent page: still forbidden


class AuthorBoxTests(TestCase):
    def test_every_page_says_who_is_behind_it(self):
        from apps.pages.registry import REGISTRY

        html = self.client.get("/instagram/followers/").content.decode()
        self.assertIn("Who&#x27;s behind this page", html)
        self.assertIn('href="https://www.instagram.com/dt.ekinsipahi/"', html)
        self.assertIn("Dt. Ekin Sipahi (@dt.ekinsipahi)", html)
        self.assertIn('<time datetime="2026-11-08">', html)
        tr = REGISTRY.find("tr", "instagram", "followers")
        self.assertIn("Bu sayfanın arkasında kim var", self.client.get(tr.path).content.decode())

    def test_a_guide_names_its_publisher_and_founder(self):
        from apps.pages.registry import REGISTRY

        guide = next(p for p in REGISTRY.pages_in("en") if p.data.get("kind") == "guide")
        article = next(b for b in jsonld(self.client.get(guide.path).content.decode()) if b["@type"] == "Article")
        self.assertEqual(article["publisher"]["founder"]["sameAs"], ["https://www.instagram.com/dt.ekinsipahi/"])
        self.assertEqual(article["publisher"]["parentOrganization"]["name"], "Sterr Agency")
