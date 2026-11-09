"""manage.py check_pages: passes on the real content, fails on bad data."""
from io import StringIO
from unittest import mock

from django.core.management import CommandError, call_command
from django.test import TestCase

from apps.pages import checks, images
from apps.pages.checks import validate

from .helpers import page_data, registry


def messages(problems, level="error"):
    return [f"{p.where}: {p.message}" for p in problems if p.level == level]


class CheckPagesCommandTests(TestCase):
    def test_passes_on_the_content(self):
        out = StringIO()
        call_command("check_pages", stdout=out)
        self.assertIn("OK: 0 errors", out.getvalue())
        self.assertIn("(en ", out.getvalue())

    def test_fails_on_bad_content(self):
        bad = registry({("en", "instagram"): [{**page_data(), "title": "Free SEO followers"}]})
        with mock.patch("apps.pages.registry.REGISTRY", bad), self.assertRaises(CommandError):
            call_command("check_pages", stdout=StringIO())


class ValidateTests(TestCase):
    def errors_for(self, *pages, platform="instagram", lang="en", live=False):
        reg = registry({(lang, platform): list(pages)})
        return messages(validate(reg, live=live))

    def assertError(self, errors, text):
        self.assertTrue(any(text in e for e in errors), f"no error containing {text!r} in:\n" + "\n".join(errors))

    def test_required_keys(self):
        data = page_data(service="followers")
        del data["title"], data["faqs"]
        errors = self.errors_for(page_data(), data)
        self.assertError(errors, "'title' is missing")
        self.assertError(errors, "'faqs' is missing")

    def test_unique_slugs_titles_and_variants(self):
        hub, followers = page_data(), page_data(service="followers")
        errors = self.errors_for(hub, followers, {**page_data(service="followers", quantity=1000), "slug": followers["slug"]},
                                 {**followers, "slug": "instagram/followers-again"})
        self.assertError(errors, "slug 'instagram/followers' is already used by en instagram/followers")
        self.assertError(errors, "this page is defined twice")
        reg = registry({("en", "instagram"): [hub, followers,
                                               {**page_data(service="followers", quantity=1000), "title": followers["title"]}]})
        self.assertError(messages(validate(reg, live=False)), "same title as en instagram/followers")

    def test_lengths(self):
        errors = self.errors_for(page_data(), {**page_data(service="followers"), "title": "Too short",
                                               "description": "x" * 200, "label": "y" * 70})
        self.assertError(errors, "title is 9 characters; keep it 20–65")
        self.assertError(errors, "description is 200 characters; keep it 70–160")
        self.assertError(errors, "label is 70 characters")

    def test_copy_rules(self):
        followers = page_data(service="followers")
        followers["intro"] = "Guaranteed free followers with our SEO magic, plus female followers on request."
        followers["faqs"] = followers["faqs"][:2] + [("Is it crypto?", "We take bitcoin.")]
        errors = self.errors_for(page_data(), followers)
        for rule in ("(SEO)", "(guarantee)", "(free)", "(gender targeting)", "(crypto)"):
            self.assertError(errors, rule)
        tr = {**page_data(), "slug": "instagram", "intro": "Ücretsiz ve garantili takipçi, arama motoru dostu."}
        errors = self.errors_for(tr, lang="tr")
        self.assertError(errors, "'Ücretsiz'")

    def test_slug_rules(self):
        errors = self.errors_for(page_data(), {**page_data(service="followers"), "slug": "Instagram/Followers"},
                                 {**page_data(service="followers", quantity=1000), "slug": "de/instagram-followers"},
                                 {**page_data(service="followers"), "service": "likes", "slug": "free-instagram-likes"})
        self.assertError(errors, "must be lower-case words")
        self.assertError(errors, "starts with a language code")
        self.assertError(errors, "copy rule (free) in the slug")

    def test_dimensions(self):
        errors = self.errors_for(page_data(), {**page_data(service="followers"), "service": "subscribers", "slug": "a"},
                                 {**page_data(service="followers"), "modifier": "instant", "slug": "b"},
                                 {**page_data(service="followers"), "quantity": 4, "slug": "c"},
                                 {**page_data(), "quantity": 1000, "slug": "d"})
        self.assertError(errors, "service 'subscribers' must be one of followers, likes, views, comments on instagram")
        self.assertError(errors, "modifier 'instant' isn't in dimensions.MODIFIERS")
        self.assertError(errors, "quantity must be a whole number")
        self.assertError(errors, "need a service")

    def test_placeholders(self):
        errors = self.errors_for(page_data(), {**page_data(service="followers"), "intro": "Reach {quantity} with {nonsense}."})
        self.assertError(errors, "placeholder {quantity} has no value here")  # no quantity on this page
        self.assertError(errors, "placeholder {nonsense} has no value here")

    def test_images(self):
        followers = page_data(service="followers")
        followers["hero"] = {"image": "nope", "alt": ""}
        followers["sections"][0]["image"] = {"image": "instagram-real-people"}
        errors = self.errors_for(page_data(), followers)
        self.assertError(errors, "image 'nope' isn't declared")
        self.assertError(errors, "needs alt text")
        declared = {**images.IMAGES, "instagram-followers": {**images.IMAGES["instagram-followers"], "pending": False}}
        with mock.patch.object(checks, "IMAGES", declared):
            errors = self.errors_for(page_data(), page_data(service="followers"))
        self.assertError(errors, "static/img/pages/instagram/followers.webp doesn't exist")

    def test_routes_and_hreflang_targets(self):
        # A slug another app owns is shadowed: the page would never be reached.
        errors = self.errors_for(page_data(), {**page_data(service="followers"), "slug": "account"}, live=True)
        self.assertError(errors, "/account/ is taken by another URL (growth:account)")
        reg = registry({("en", "instagram"): [page_data(), page_data(service="followers")]})
        page = reg.find("en", "instagram", "followers")
        with mock.patch.object(type(reg), "alternates", return_value=[("de", "/de/missing/")]):
            errors = messages(validate(reg, live=False))
        self.assertError(errors, "hreflang de points to /de/missing/")
        self.assertIsNotNone(page)

    def test_a_language_needs_its_ui(self):
        reg = registry({("de", "instagram"): [page_data()]}, ui={"en": registry({}).ui["en"], "de": {"home": "Start"}})
        errors = messages(validate(reg, live=False))
        self.assertError(errors, "missing keys (English shows instead)")
