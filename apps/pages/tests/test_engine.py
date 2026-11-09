"""The registry and the context builder: variants, the preselected package, the pace, related pages."""
from types import SimpleNamespace

from django.test import TestCase

from apps.growth import plan
from apps.growth.content import ui_for
from apps.pages import context
from apps.pages.registry import REGISTRY, Variant

from .helpers import page_data, registry


def fake_page(service="followers", quantity=0, data=None, platform="instagram"):
    return SimpleNamespace(variant=Variant(platform, service, quantity), data=data or {}, lang="en")


class VariantTests(TestCase):
    def test_keys_and_order(self):
        self.assertEqual(Variant("instagram", "followers", 1000, "real").key, "instagram/followers/1000/real")
        self.assertTrue(Variant("youtube").is_hub)
        self.assertTrue(Variant("youtube", "subscribers").is_base)
        self.assertFalse(Variant("youtube", "subscribers", 1000).is_base)
        variants = [Variant("youtube"), Variant("instagram", "likes"), Variant("instagram", "followers", 5000),
                    Variant("instagram"), Variant("instagram", "followers")]
        self.assertEqual([v.key for v in sorted(variants, key=Variant.sort_key)],
                         ["instagram", "instagram/followers", "instagram/followers/5000", "instagram/likes", "youtube"])


class PlanChoiceTests(TestCase):
    def choose(self, *args, **kwargs):
        return context.choose_plan(fake_page(*args, **kwargs), list(plan.PLANS), plan.DEFAULT_PLAN)

    def test_quantity_picks_the_smallest_package_whose_typical_month_reaches_it(self):
        self.assertEqual(self.choose(quantity=1000), "starter")
        self.assertEqual(self.choose(quantity=2500), "starter")
        self.assertEqual(self.choose(quantity=5000), "rising")
        self.assertEqual(self.choose(quantity=10000), "pro")
        self.assertEqual(self.choose(quantity=100000), "pro")
        self.assertEqual(self.choose("subscribers", 1000, platform="youtube"), "starter")
        self.assertEqual(self.choose("likes", 5000), "starter")
        self.assertEqual(self.choose("comments", 1000), "pro")

    def test_default_and_override(self):
        self.assertEqual(self.choose(), "rising")
        self.assertEqual(self.choose("views", 10000), "rising")  # views have no ratio: the default
        self.assertEqual(self.choose(quantity=1000, data={"plan": "pro"}), "pro")


class PaceTests(TestCase):
    def test_typical_pace_month_by_month(self):
        r = context.resolve_page(REGISTRY.find("en", "instagram", "followers", 1000), REGISTRY)
        pace = context.pace(r)
        self.assertEqual([row["label"] for row in pace["rows"]], ["Month 1", "Month 2", "Month 3"])
        self.assertEqual([row["range"] for row in pace["rows"]], ["1,000–4,000", "2,000–8,000", "3,000–12,000"])
        self.assertEqual(pace["goal"], "8.33%")
        self.assertEqual([p["when"] for p in pace["by_plan"]], ["usually within the first month"] * 3)
        self.assertEqual([p["pick"] for p in pace["by_plan"]], [True, False, False])

    def test_bigger_goals_take_months(self):
        page = SimpleNamespace(variant=Variant("instagram", "followers", 10000), data={}, lang="en", slug="x")
        r = SimpleNamespace(page=page, lang="en", ui=REGISTRY.ui["en"], p={}, plans_raw=list(plan.PLANS),
                            plans=plan.for_page("en", ui_for("en", "instagram")), pick={"key": "pro"})
        pace = context.pace(r)
        self.assertEqual([p["when"] for p in pace["by_plan"]],
                         ["usually 3–10 months", "usually 2–5 months", "usually 1–3 months"])
        self.assertEqual(len(pace["rows"]), 3)

    def test_no_pace_without_quantity_and_no_math_for_views(self):
        r = context.resolve_page(REGISTRY.find("en", "instagram", "followers"), REGISTRY)
        self.assertIsNone(context.pace(r))
        views = registry({("en", "instagram"): [page_data(), {**page_data(service="followers", quantity=1000),
                                                              "service": "views", "slug": "instagram/views/1000"}]})
        r = context.resolve_page(views.find("en", "instagram", "views", 1000), views)
        pace = context.pace(r)
        self.assertNotIn("rows", pace)
        self.assertIn("we don't count them in advance", pace["fallback"])


class FillTests(TestCase):
    def test_fill_and_number_format(self):
        self.assertEqual(context.fill({"a": ["{x} and {y}"], "b": ("{x}",)}, {"x": 1}), {"a": ["1 and {y}"], "b": ("1",)})
        self.assertEqual(context.count(10000, "en"), "10,000")
        self.assertEqual(context.count(10000, "de"), "10.000")


class RelatedTests(TestCase):
    def test_groups(self):
        hub, followers, goal = page_data(), page_data(service="followers"), page_data(service="followers", quantity=1000)
        likes = {**followers, "service": "likes", "slug": "instagram/likes", "title": "x" * 30}
        goal_5k = {**goal, "quantity": 5000, "slug": "instagram/followers/5000"}
        real = {**followers, "modifier": "real", "slug": "instagram/real-followers"}
        reg = registry({("en", "instagram"): [hub, followers, goal, goal_5k, likes, real],
                        ("en", "tiktok"): [page_data(platform="tiktok")],
                        ("en", "youtube"): [page_data(platform="youtube"), page_data(platform="youtube", service="subscribers")]})
        groups = dict(reg.related(reg.find("en", "instagram", "followers", 1000)))
        self.assertEqual([p.path for p in groups["platform"]], ["/instagram/followers/", "/instagram/likes/"])
        # TikTok has no followers page: its hub stands in; YouTube has subscribers.
        self.assertEqual([p.path for p in groups["platforms"]], ["/tiktok/", "/youtube/subscribers/"])
        # A deeper page links up and across only: no lists of other goals or modifiers.
        self.assertEqual(set(groups), {"platform", "platforms"})
        groups = dict(reg.related(reg.find("en", "instagram", "followers")))
        # The service page links to a few deeper pages: the ways to grow, then one round goal.
        self.assertEqual([p.path for p in groups["modifiers"]],
                         ["/instagram/real-followers/", "/instagram/followers/1000/", "/instagram/followers/5000/"])
        self.assertEqual(reg.related(reg.find("en", "instagram")), [])
        self.assertEqual([page.path for page in reg.ancestors(reg.find("en", "instagram", "followers", 1000))],
                         ["/instagram/", "/instagram/followers/"])
