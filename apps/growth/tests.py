import json
import re
from datetime import timedelta
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
from unittest import mock
from urllib.parse import quote

import requests
import stripe
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core import mail
from django.core.management import call_command
from django.test import RequestFactory, SimpleTestCase, TestCase, override_settings
from django.urls import reverse
from django.utils import timezone

from apps.core.languages import LANGS
from apps.core.net import client_ip

from . import billing, evidence, linksterr
from .constants import PLATFORMS, TERMS_VERSION
from .content import PLATFORM_UI, UI, platform_keys, ui_for
from .forms import clean_handle, valid_handle
from .models import AccountActivity, AgencySubscription, Customer, Dispute, StripeEvent, SubscriptionStat
from .plan import PLANS, for_page
from .validate import check, has_file

WEBHOOK_SECRET = "whsec_test"
MAIL = dict(TEAM_NOTIFY_EMAILS=["owner@example.com"], GROWTH_NOTIFY_EMAILS=["ekinsipahi8@gmail.com"],
            EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend")
STRIPE_ON = dict(GROWTH_PAYMENTS=True, STRIPE_SECRET_KEY="sk_test_x", STRIPE_WEBHOOK_SECRET=WEBHOOK_SECRET, **MAIL)
STRIPE_OFF = dict(GROWTH_PAYMENTS=False, STRIPE_SECRET_KEY="", **MAIL)
CODES = {lang.code for lang in LANGS}
PERIOD_END = int((timezone.now() + timedelta(days=30)).timestamp())
OURS = {"site": "growsterr"}


def stripe_sub(status="active", sub_id="sub_1", **extra):
    """A Stripe subscription as webhooks deliver it (period end on the items, as in newer API versions)."""
    return {"id": sub_id, "object": "subscription", "status": status, "customer": "cus_1", "cancel_at_period_end": False,
            "items": {"data": [{"current_period_end": PERIOD_END}]}, "metadata": dict(OURS), **extra}


class ContentTests(SimpleTestCase):
    def test_every_language_file_belongs_to_a_site_language(self):
        # Translations arrive one language at a time: UI holds the languages that have a file.
        self.assertIn("en", UI)
        self.assertLessEqual(set(UI), CODES)
        self.assertEqual(set(PLATFORM_UI), set(UI))
        for code in UI:
            self.assertEqual(set(PLATFORM_UI[code]), {"youtube"}, code)

    def test_a_site_language_without_a_file_falls_back_to_english(self):
        missing = sorted(CODES - set(UI)) or ["xx"]  # once every language has its file, an unknown code
        for code in missing:
            with self.subTest(code=code):
                for platform in PLATFORMS:
                    self.assertEqual(ui_for(code, platform), ui_for("en", platform))
                self.assertEqual(platform_keys(code), platform_keys("en"))

    def test_every_language_passes_the_ui_check(self):
        for code in sorted(UI):
            with self.subTest(code=code):
                self.assertEqual(check(code), [])

    def test_the_check_command(self):
        out = StringIO()
        with_file = [lang.code for lang in LANGS if has_file(lang.code)]  # now: translators add files as they go
        call_command("check_growth_ui", stdout=out)
        self.assertEqual(out.getvalue().count(": OK"), len(with_file))
        out = StringIO()
        call_command("check_growth_ui", "de", "ar", stdout=out)
        self.assertIn("ar: OK", out.getvalue())

    def test_influencer_packages(self):
        self.assertEqual([p["key"] for p in PLANS], ["starter", "rising", "pro"])
        self.assertEqual([str(p["price"]) for p in PLANS], ["79.99", "149.99", "279.99"])
        self.assertEqual(PLANS[0]["followers"], (1000, 4000))
        for p in PLANS:  # 2–3 likes per new follower, about one comment per 10
            self.assertEqual(p["likes"], (p["followers"][0] * 2, p["followers"][1] * 3))
            self.assertEqual(p["comments"], (p["followers"][0] // 10, p["followers"][1] // 10))

    def test_youtube_speaks_of_subscribers_in_every_language(self):
        en = for_page("en", ui_for("en", "youtube"))
        self.assertEqual(en[0]["headline"], "1,000–4,000 subscribers / month")
        self.assertEqual(en[0]["items"][0], "1,000–4,000 new subscribers")
        self.assertEqual(ui_for("en", "instagram")["audience"], "followers")
        self.assertEqual(ui_for("en", "youtube")["audience"], "subscribers")
        self.assertEqual(ui_for("tr", "youtube")["f_handle"], ui_for("tr", "youtube")["f_handle"].replace("{platform}", ""))
        for code in CODES:
            for platform in PLATFORMS:
                gu = ui_for(code, platform)
                text = json.dumps(gu, ensure_ascii=False)
                self.assertNotIn("{platform}", text, (code, platform))
                self.assertNotIn("{audience}", text, (code, platform))
            # The plan cards (shared with the pages) keep their keys on every platform.
            cards = for_page(code, ui_for(code, "youtube"))
            self.assertEqual(len(cards), 3)
            self.assertTrue(all(c["items"] and c["headline"] and c["name"] for c in cards))
        self.assertIn("Abonnenten", for_page("de", ui_for("de", "youtube"))[0]["headline"])
        self.assertIn("abone", for_page("tr", ui_for("tr", "youtube"))[0]["headline"])

    def test_handle_cleaning(self):
        for raw in ("@Brand.Name", "brand.name", "https://www.instagram.com/brand.name/?igsh=abc", "instagram.com/brand.name",
                    "https://www.tiktok.com/@brand.name?lang=en", "tiktok.com/brand.name", "https://www.youtube.com/@brand.name/videos",
                    "youtube.com/@Brand.Name", "m.youtube.com/@brand.name?si=x"):
            self.assertEqual(clean_handle(raw).lower(), "brand.name")

    def test_youtube_handle_rules(self):
        for ok in ("abc", "my-channel.tv", "Brand_Name-2", "a" * 30):
            self.assertTrue(valid_handle(ok, "youtube"), ok)
        for bad in ("ab", "a" * 31, "has space", "émoji", "brand!", ""):
            self.assertFalse(valid_handle(bad, "youtube"), bad)
        self.assertFalse(valid_handle("my-brand", "instagram"))  # hyphens are YouTube only
        self.assertTrue(valid_handle("x", "tiktok"))

    def test_period_end_in_old_and_new_api_shapes(self):
        self.assertEqual(billing.period_end({"current_period_end": PERIOD_END}).timestamp(), PERIOD_END)
        self.assertEqual(billing.period_end(stripe_sub()).timestamp(), PERIOD_END)
        self.assertEqual(billing.invoice_subscription({"subscription": "sub_1"}), "sub_1")
        self.assertEqual(billing.invoice_subscription({"parent": {"subscription_details": {"subscription": "sub_2"}}}), "sub_2")

    def test_no_account_pages_in_the_sitemap(self):
        from .sitemap import entries
        self.assertEqual(entries(), [])

    def test_tests_never_reach_the_outside(self):
        self.assertEqual((settings.LINKSTERR_AGENCY_TOKEN, settings.STRIPE_SECRET_KEY, settings.GOOGLE_OAUTH_CLIENT_SECRET), ("", "", ""))


class ClientIpTests(SimpleTestCase):
    def test_forwarded_for_then_remote_addr_and_garbage_is_dropped(self):
        rf = RequestFactory()
        self.assertEqual(client_ip(rf.get("/", HTTP_X_FORWARDED_FOR="203.0.113.7, 10.0.0.1")), "203.0.113.7")
        self.assertEqual(client_ip(rf.get("/", REMOTE_ADDR="198.51.100.2")), "198.51.100.2")
        self.assertEqual(client_ip(rf.get("/", HTTP_X_FORWARDED_FOR="unknown", REMOTE_ADDR="198.51.100.2")), "198.51.100.2")
        self.assertIsNone(client_ip(rf.get("/", HTTP_X_FORWARDED_FOR="nope", REMOTE_ADDR="")))
        self.assertEqual(client_ip(rf.get("/", HTTP_X_FORWARDED_FOR="2001:db8::1")), "2001:db8::1")


class FreshCache:
    """The IP rate limit lives in the cache; every test starts with a clean one."""

    def setUp(self):
        from django.core.cache import cache
        cache.clear()
        super().setUp()


def order_data(**extra):
    data = {"lang": "en", "platform": "instagram", "plan": "rising", "handle": "@My.Brand",
            "location": "Berlin, Germany", "phone": "+49 (151) 234-56789", "email": "Buyer@Example.com",
            "password": "s3cret-pass", "consent": "on"}
    data.update(extra)
    return data


@override_settings(**STRIPE_OFF)
class OrderPageTests(FreshCache, TestCase):
    def test_the_query_preselects_package_platform_and_language(self):
        r = self.client.get(reverse("growth:order") + "?plan=pro&platform=youtube&lang=de")
        self.assertEqual(r.status_code, 200)
        html = r.content.decode()
        self.assertRegex(html, r'name="plan" value="pro"[^>]*checked')
        self.assertRegex(html, r'name="platform" value="youtube" checked')
        self.assertIn('<html lang="de"', html)
        self.assertIn(ui_for("de", "youtube")["f_handle"], html)
        self.assertIn("Abonnenten", html)
        self.assertIn('<meta name="robots" content="noindex, nofollow">', html)
        for amount in ("$79.99", "$149.99", "$279.99"):
            self.assertIn(amount, html)
        # The other platforms' words travel along for the platform switch (static/js/app.js).
        data = json.loads(re.search(r'<script id="growth-platform-ui" type="application/json">(.*?)</script>', html, re.S).group(1))
        self.assertEqual(set(data), set(PLATFORMS))
        self.assertIn("Follower", data["instagram"]["ui"]["f_location"])
        self.assertIn("Abonnenten", data["youtube"]["plans"]["starter"]["headline"])

    def test_defaults_and_the_form_fields(self):
        html = self.client.get(reverse("growth:order")).content.decode()
        self.assertRegex(html, r'name="plan" value="rising"[^>]*checked')
        self.assertRegex(html, r'name="platform" value="instagram" checked')
        for text in ("Instagram username", "Where should your new followers be from?", UI["en"]["f_location_help"],
                     UI["en"]["f_phone_help"], 'type="tel"', 'name="email"', 'name="password"', 'name="consent"',
                     'href="/terms/#subscription"', "Send my request"):
            self.assertIn(text, html)
        self.assertNotIn("Continue with Google", html)  # Google sign-in is off without its keys

    def test_bad_values_fall_back_and_arabic_is_right_to_left(self):
        html = self.client.get(reverse("growth:order") + "?plan=mega&platform=myspace&lang=ar").content.decode()
        self.assertIn('dir="rtl"', html)
        self.assertRegex(html, r'name="plan" value="rising"[^>]*checked')
        self.assertRegex(html, r'name="platform" value="instagram" checked')

    def test_language_links_keep_the_choices(self):
        html = self.client.get(reverse("growth:order") + "?plan=starter&platform=tiktok").content.decode()
        self.assertIn("/order/?lang=de&amp;platform=tiktok&amp;plan=starter", html)
        # Only the languages the growth pages speak are offered; the others would show English.
        for code in CODES - set(UI):
            self.assertNotIn(f"/order/?lang={code}&amp;", html)

    def test_canceled_checkout_note(self):
        self.assertContains(self.client.get(reverse("growth:order") + "?lang=en&canceled=1"), "Payment was canceled")


@override_settings(**STRIPE_OFF)
class RequestModeTests(FreshCache, TestCase):
    def test_order_records_where_it_came_from(self):
        # static/js/app.js fills these: the page whose button led to the form, the visitor's first page,
        # the outside site that sent them, and when they first came.
        self.client.post(reverse("growth:order"), order_data(
            source_page="/instagram/followers/cheap/", landing_page="/guides/can-you-buy-instagram-followers/",
            referrer="google.com", first_visit_at="2026-11-01T09:30:00.000Z", utm_source="newsletter"))
        sub = AgencySubscription.objects.get()
        self.assertEqual((sub.source_page, sub.landing_page, sub.referrer),
                         ("/instagram/followers/cheap/", "/guides/can-you-buy-instagram-followers/", "google.com"))
        self.assertEqual(sub.first_visit_at.isoformat(), "2026-11-01T09:30:00+00:00")
        team = next(m for m in mail.outbox if "başvurusu" in m.subject)
        self.assertIn("Satın aldığı sayfa: /instagram/followers/cheap/", team.body)
        self.assertIn("İlk geldiği sayfa: /guides/can-you-buy-instagram-followers/  (01.11.2026)", team.body)
        self.assertIn("Nereden geldi: google.com", team.body)
        self.assertIn("Kampanya: newsletter", team.body)

    def test_order_without_a_known_source_says_so(self):
        self.client.post(reverse("growth:order"), order_data(first_visit_at="2999-01-01T00:00:00Z"))
        sub = AgencySubscription.objects.get()
        self.assertIsNone(sub.first_visit_at)  # a time in the future is not believed
        team = next(m for m in mail.outbox if "başvurusu" in m.subject)
        self.assertIn("Nereden geldi: doğrudan", team.body)

    def test_order_creates_account_and_request(self):
        r = self.client.post(reverse("growth:order"), order_data())
        sub = AgencySubscription.objects.get()
        self.assertRedirects(r, f"{reverse('growth:success')}?lang=en&platform=instagram&sub={sub.pk}", fetch_redirect_response=False)
        self.assertEqual((sub.status, sub.handle, sub.plan, str(sub.amount)), ("requested", "my.brand", "rising", "149.99"))
        user = get_user_model().objects.get(username="buyer@example.com")
        self.assertEqual(sub.user, user)
        self.assertTrue(Customer.objects.filter(user=user, lang="en").exists())
        self.assertTrue(sub.notified)
        subjects = [m.subject for m in mail.outbox]
        self.assertIn("We received your request: Rising Influencer for @my.brand on Instagram", subjects)
        self.assertEqual(sub.phone, "+4915123456789")
        self.assertEqual((sub.terms_version, sub.location), (TERMS_VERSION, "Berlin, Germany"))
        team = next(m for m in mail.outbox if "başvurusu" in m.subject)
        self.assertIn("Telefon: +4915123456789  (https://wa.me/4915123456789)", team.body)
        self.assertEqual(team.to, ["owner@example.com", "ekinsipahi8@gmail.com"])
        customer_mail = next(m for m in mail.outbox if m.subject.startswith("We received your request"))
        self.assertNotIn("Sterr", customer_mail.body)
        self.assertIn("Growsterr", customer_mail.body)
        page = self.client.get(r["Location"]).content.decode()
        self.assertIn("lead-event", page)
        self.assertIn("signup-event", page)
        self.assertIn("Rising Influencer", page)

    def test_phone_is_required_and_checked(self):
        for phone in ("", "12-34", "call me"):
            r = self.client.post(reverse("growth:order"), order_data(phone=phone))
            self.assertEqual(r.status_code, 400)
        self.assertFalse(AgencySubscription.objects.exists())
        self.assertContains(self.client.post(reverse("growth:order"), order_data(phone="12")), "Enter a valid phone number", status_code=400)
        self.client.post(reverse("growth:order"), order_data(phone="0090 532 123 45 67"))
        self.assertEqual(AgencySubscription.objects.get().phone, "+905321234567")

    def test_existing_email_needs_the_right_password(self):
        get_user_model().objects.create_user("buyer@example.com", "buyer@example.com", "the-real-one")
        r = self.client.post(reverse("growth:order"), order_data())
        self.assertEqual(r.status_code, 400)
        self.assertFalse(AgencySubscription.objects.exists())
        r = self.client.post(reverse("growth:order"), order_data(password="the-real-one", platform="tiktok", plan="starter"))
        self.assertEqual(r.status_code, 302)
        self.assertEqual(AgencySubscription.objects.get().platform, "tiktok")

    def test_signed_in_order_needs_no_email_or_password(self):
        user = get_user_model().objects.create_user("me@example.com", "me@example.com", "pass-word-1")
        self.client.force_login(user)
        data = order_data()
        del data["email"], data["password"]
        self.assertContains(self.client.get(reverse("growth:order")), "Signed in as me@example.com")
        self.assertEqual(self.client.post(reverse("growth:order"), data).status_code, 302)
        self.assertEqual(AgencySubscription.objects.get().email, "me@example.com")

    def test_invalid_plan_platform_and_short_password(self):
        r = self.client.post(reverse("growth:order"), order_data(plan="mega", password="short"))
        self.assertEqual(r.status_code, 400)
        r = self.client.post(reverse("growth:order"), order_data(platform="myspace"))
        self.assertContains(r, "Choose a platform.", status_code=400)
        self.assertFalse(get_user_model().objects.exists())

    def test_terms_box_is_required(self):
        data = order_data()
        del data["consent"]
        self.assertEqual(self.client.post(reverse("growth:order"), data).status_code, 400)
        self.assertFalse(AgencySubscription.objects.exists())

    def test_a_form_error_keeps_the_language_and_platform(self):
        r = self.client.post(reverse("growth:order"), order_data(lang="tr", platform="youtube", handle="x"))
        self.assertEqual(r.status_code, 400)
        html = r.content.decode()
        self.assertIn('<html lang="tr"', html)
        self.assertIn(ui_for("tr", "youtube")["err_handle"], html)
        self.assertRegex(html, r'name="platform" value="youtube" checked')

    def test_honeypot(self):
        self.client.post(reverse("growth:order"), order_data(fax="bot"))
        self.assertFalse(AgencySubscription.objects.exists())

    def test_rate_limit(self):
        for i in range(8):
            self.client.post(reverse("growth:order"), order_data(handle=f"brand{i}"))
        r = self.client.post(reverse("growth:order"), order_data(handle="brand9"))
        self.assertContains(r, "Too many attempts", status_code=400)
        self.assertEqual(AgencySubscription.objects.count(), 8)

    def test_get_and_post_only(self):
        self.assertEqual(self.client.put(reverse("growth:order")).status_code, 405)


@override_settings(**STRIPE_ON)
class CheckoutTests(FreshCache, TestCase):
    session = SimpleNamespace(id="cs_test_1", url="https://checkout.stripe.com/c/pay/cs_test_1")

    def signed_in(self):
        user = get_user_model().objects.create_user("me@example.com", "me@example.com", "pass-word-1")
        Customer.objects.create(user=user, email_verified=True)
        self.client.force_login(user)
        return user

    def test_unverified_email_gets_a_link_that_goes_straight_to_payment(self):
        r = self.client.post(reverse("growth:order"), order_data(plan="pro"))
        self.assertEqual(r["Location"], f"{reverse('growth:account')}?lang=en&verify=sent")
        sub = AgencySubscription.objects.get()
        self.assertEqual((sub.status, sub.plan), ("pending", "pro"))
        self.assertTrue(mail.outbox[-1].subject.startswith("Confirm your email to start your package"))
        link = re.search(r"https?://[^/\s]+(/account/verify/\S+/)", mail.outbox[-1].body).group(1)
        self.client.logout()
        with mock.patch("apps.growth.billing.create_checkout", return_value=self.session) as create:
            r = self.client.get(link)
        self.assertEqual((r.status_code, r["Location"]), (303, self.session.url))
        self.assertEqual(create.call_args.args[0].pk, sub.pk)
        self.assertTrue(Customer.objects.get().email_verified)
        sub.refresh_from_db()
        self.assertEqual(sub.stripe_checkout_session_id, "cs_test_1")
        self.assertIsNotNone(sub.terms_accepted_at)
        self.assertEqual(sub.terms_version, TERMS_VERSION)
        self.assertIn("cancel", create.call_args.kwargs["note"])

    def test_verified_customer_goes_straight_to_stripe_and_retries_reuse_the_unpaid_one(self):
        self.signed_in()
        data = order_data(platform="tiktok", plan="starter")
        del data["email"], data["password"]
        with mock.patch("apps.growth.billing.create_checkout", return_value=self.session) as create:
            r = self.client.post(reverse("growth:order"), data)
            self.client.post(reverse("growth:order"), {**data, "plan": "pro", "location": "Paris"})
        self.assertEqual((r.status_code, r["Location"]), (303, self.session.url))
        sub = AgencySubscription.objects.get()
        self.assertEqual((sub.platform, sub.plan, str(sub.amount), sub.location), ("tiktok", "pro", "279.99", "Paris"))
        self.assertEqual(create.call_count, 2)
        success_url, cancel_url = create.call_args.args[1:3]
        self.assertEqual(cancel_url, f"{settings.SITE_URL}/order/?lang=en&platform=tiktok&plan=pro&canceled=1")
        self.assertIn(f"/growth/success/?lang=en&platform=tiktok&sub={sub.pk}&session_id={{CHECKOUT_SESSION_ID}}", success_url)
        self.assertFalse([m for m in mail.outbox if "owner@example.com" in m.to])  # unpaid: no team email

    def test_stripe_down_shows_the_form_again(self):
        self.signed_in()
        data = order_data()
        del data["email"], data["password"]
        with mock.patch("apps.growth.billing.create_checkout", side_effect=stripe.APIConnectionError("down")):
            r = self.client.post(reverse("growth:order"), data)
        self.assertContains(r, "We couldn&#x27;t start the payment", status_code=502)

    def test_success_page_activates_once(self):
        user = self.signed_in()
        sub = AgencySubscription.objects.create(user=user, email=user.email, handle="brand", location="Rome", plan="starter",
                                                amount="79.99", stripe_checkout_session_id="cs_ok")
        session = SimpleNamespace(id="cs_ok", status="complete", payment_status="paid", subscription="sub_1")
        url = f"{reverse('growth:success')}?lang=en&platform=instagram&sub={sub.pk}&session_id=cs_ok"
        with mock.patch("apps.growth.billing.retrieve_checkout", return_value=session), \
             mock.patch("apps.growth.billing.retrieve_subscription", return_value=stripe_sub()):
            first = self.client.get(url).content.decode()
            second = self.client.get(url).content.decode()
        self.assertIn("purchase-event", first)
        self.assertIn("Payment received. Your growth has started.", first)
        self.assertNotIn("purchase-event", second)
        sub.refresh_from_db()
        self.assertEqual((sub.status, sub.stripe_subscription_id, sub.stripe_customer_id), ("active", "sub_1", "cus_1"))
        self.assertEqual(int(sub.current_period_end.timestamp()), PERIOD_END)
        subjects = [m.subject for m in mail.outbox]
        self.assertEqual(subjects.count("Your campaign has started: Starter Creator for @brand on Instagram"), 1)
        self.assertEqual(sum("(ödendi)" in s for s in subjects), 1)

    def test_billing_portal(self):
        user = self.signed_in()
        AgencySubscription.objects.create(user=user, email=user.email, handle="brand", location="Rome", amount="79.99",
                                          status="active", stripe_customer_id="cus_1")
        with mock.patch("apps.growth.billing.portal_url", return_value="https://billing.stripe.com/p/x") as portal:
            r = self.client.post(reverse("growth:billing"), {"lang": "en"})
        self.assertEqual((r.status_code, r["Location"]), (303, "https://billing.stripe.com/p/x"))
        self.assertEqual(portal.call_args.args[0], "cus_1")
        self.assertContains(self.client.get(reverse("growth:account") + "?lang=en"), "Manage billing or cancel")

    def test_start_now_for_a_saved_subscription(self):
        user = self.signed_in()
        sub = AgencySubscription.objects.create(user=user, email=user.email, handle="brand", location="Rome", plan="rising",
                                                amount="149.99")
        self.assertContains(self.client.get(reverse("growth:account") + "?lang=en"), reverse("growth:pay", args=[sub.pk]))
        with mock.patch("apps.growth.billing.create_checkout", return_value=self.session):
            r = self.client.post(reverse("growth:pay", args=[sub.pk]), {"lang": "en"})
        self.assertEqual((r.status_code, r["Location"]), (303, self.session.url))


@override_settings(**STRIPE_ON)
class StripePriceTests(TestCase):
    def setUp(self):
        from django.core.cache import cache
        cache.clear()
        self.sub = AgencySubscription.objects.create(email="a@example.com", handle="brand", location="Rome", platform="tiktok",
                                                     plan="pro", amount="279.99")

    def checkout_params(self, prices):
        client = mock.Mock()
        client.v1.prices.list.return_value = SimpleNamespace(data=prices)
        client.v1.checkout.sessions.create.return_value = SimpleNamespace(id="cs", url="u")
        with mock.patch("apps.growth.billing._client", return_value=client):
            billing.create_checkout(self.sub, "https://s/ok", "https://s/cancel")
        self.assertEqual(client.v1.prices.list.call_args.kwargs["params"]["lookup_keys"], ["growsterr_pro_monthly"])
        return client.v1.checkout.sessions.create.call_args.kwargs["params"]

    def test_uses_the_monthly_price_from_setup_stripe(self):
        params = self.checkout_params([SimpleNamespace(id="price_pro", unit_amount=27999)])
        self.assertEqual(params["payment_method_options"], {"card": {"request_three_d_secure": "any"}})
        self.assertEqual(params["mode"], "subscription")
        self.assertEqual(params["line_items"], [{"quantity": 1, "price": "price_pro"}])
        for meta in (params["metadata"], params["subscription_data"]["metadata"]):
            self.assertEqual((meta["site"], meta["subscription_id"], meta["platform"]), ("growsterr", str(self.sub.pk), "tiktok"))
        self.assertTrue(params["subscription_data"]["description"].startswith("Growsterr · Pro Influencer · TikTok for @brand"))

    def test_portal_configuration_from_real_stripe_objects(self):
        confs = [stripe.StripeObject.construct_from({"id": "bpc_other", "metadata": {"app": "sterr-growth"}}, "sk"),
                 stripe.StripeObject.construct_from({"id": "bpc_ours", "metadata": {"app": billing.PORTAL_TAG}}, "sk")]
        client = mock.Mock()
        client.v1.billing_portal.configurations.list.return_value = SimpleNamespace(data=confs)
        with mock.patch("apps.growth.billing._client", return_value=client):
            self.assertEqual(billing.portal_configuration(), "bpc_ours")

    def test_retrieve_subscription_with_decimal_fields(self):
        # A real Stripe subscription: price.unit_amount_decimal comes back as a Decimal.
        sub = stripe.Subscription.construct_from({"id": "sub_1", "object": "subscription", "status": "active", "metadata": OURS, "items": {
            "object": "list", "data": [{"object": "subscription_item", "current_period_end": 1700000000,
                                        "price": {"object": "price", "id": "p", "unit_amount_decimal": "7999"}}]}}, "sk")
        client = mock.Mock()
        client.v1.subscriptions.retrieve.return_value = sub
        with mock.patch("apps.growth.billing._client", return_value=client):
            data = billing.retrieve_subscription("sub_1")
        self.assertEqual(data["items"]["data"][0]["price"]["unit_amount_decimal"], "7999")
        self.assertIsNotNone(billing.period_end(data))
        self.assertTrue(billing.ours(data) and billing.ours(sub))

    def test_falls_back_to_inline_monthly_price_when_missing_or_outdated(self):
        params = self.checkout_params([SimpleNamespace(id="price_old", unit_amount=9900)])
        data = params["line_items"][0]["price_data"]
        self.assertEqual((data["unit_amount"], data["recurring"]), (27999, {"interval": "month"}))
        self.assertEqual(data["product_data"]["name"], "Growsterr · Pro Influencer")


def signed(payload):
    body = json.dumps(payload)
    return body, stripe.WebhookSignature.generate_signature_header(body, WEBHOOK_SECRET)


@override_settings(**STRIPE_ON)
class WebhookTests(TestCase):
    def setUp(self):
        self.sub = AgencySubscription.objects.create(email="a@example.com", handle="brand", location="Berlin", lang="de",
                                                     plan="rising", amount="149.99", stripe_checkout_session_id="cs_1")

    def send(self, event_id, event_type, obj, stripe_obj=None):
        body, header = signed({"id": event_id, "type": event_type, "data": {"object": obj}})
        with mock.patch("apps.growth.billing.retrieve_subscription", return_value=stripe_obj or stripe_sub()) as retrieve:
            r = self.client.post(reverse("growth:webhook"), body, content_type="application/json", HTTP_STRIPE_SIGNATURE=header)
        r.retrieved = retrieve.call_count
        return r

    def checkout(self, event_id="evt_1", **extra):
        obj = {"id": "cs_1", "mode": "subscription", "payment_status": "paid", "client_reference_id": str(self.sub.pk),
               "subscription": "sub_1", "metadata": {**OURS, "subscription_id": str(self.sub.pk)}, **extra}
        return self.send(event_id, "checkout.session.completed", obj)

    def team(self, words):
        return [m for m in mail.outbox if words in m.subject]

    def test_bad_signature_rejected(self):
        r = self.client.post(reverse("growth:webhook"), "{}", content_type="application/json", HTTP_STRIPE_SIGNATURE="t=1,v1=nope")
        self.assertEqual(r.status_code, 400)

    @override_settings(STRIPE_WEBHOOK_SECRET="")
    def test_off_without_a_secret(self):
        self.assertEqual(self.client.post(reverse("growth:webhook"), "{}", content_type="application/json").status_code, 503)

    def test_paid_checkout_activates_and_emails_once(self):
        self.assertEqual(self.checkout().status_code, 200)
        self.assertEqual(self.checkout().content, b"duplicate")
        self.send("evt_2", "invoice.paid", {"id": "in_1", "subscription": "sub_1", "billing_reason": "subscription_create"})
        self.sub.refresh_from_db()
        self.assertEqual((self.sub.status, self.sub.stripe_subscription_id), ("active", "sub_1"))
        self.assertIsNotNone(self.sub.started_at)
        welcome = [m for m in mail.outbox if m.subject.startswith("Your campaign has started: Rising Influencer")]
        self.assertEqual(len(welcome), 1)
        self.assertIn("discover your profile every day", welcome[0].body)
        self.assertIn("2,000-8,000 new followers", welcome[0].body)
        team = self.team("paketi (ödendi)")
        self.assertEqual(len(team), 1)
        self.assertEqual(team[0].to, ["owner@example.com", "ekinsipahi8@gmail.com"])
        self.assertIn("Rising Influencer", team[0].body)
        self.assertIn("Site: Growsterr", team[0].body)
        self.assertIn(f"/admin/growth/agencysubscription/{self.sub.pk}/change/", team[0].body)
        self.assertEqual(StripeEvent.objects.count(), 2)

    def test_another_sites_checkout_is_skipped(self):
        # Other sites share the Stripe account: a numeric reference that happens to match our id is not ours.
        r = self.checkout(id="cs_other_site", client_reference_id=str(self.sub.pk), metadata={"subscription_id": str(self.sub.pk)})
        self.assertEqual((r.status_code, r.retrieved), (200, 0))
        r = self.send("evt_9", "customer.subscription.updated", stripe_sub(sub_id="sub_other", metadata={"subscription_id": str(self.sub.pk)}))
        self.assertEqual(r.status_code, 200)
        self.sub.refresh_from_db()
        self.assertEqual((self.sub.status, self.sub.stripe_subscription_id), ("pending", ""))
        self.assertFalse(mail.outbox)

    def test_only_our_metadata_counts(self):
        r = self.checkout(event_id="evt_m1", metadata={"site": "sterr", "subscription_id": str(self.sub.pk)})
        self.assertEqual(r.retrieved, 0)
        r = self.send("evt_m2", "checkout.session.completed", {"id": "cs_1", "mode": "subscription", "payment_status": "paid",
                                                                "subscription": "sub_1", "metadata": OURS},
                      stripe_obj=stripe_sub(metadata={"site": "linksterr"}))
        self.assertEqual(r.retrieved, 1)
        self.sub.refresh_from_db()
        self.assertEqual(self.sub.status, "pending")  # a subscription without our tag is never linked

    def test_another_sites_invoices_never_reach_stripe(self):
        for event_type in ("invoice.paid", "invoice.payment_failed"):
            r = self.send(f"evt_{event_type}", event_type, {"id": "in_x", "subscription": "sub_sterr", "billing_reason": "subscription_cycle"})
            self.assertEqual((r.status_code, r.retrieved), (200, 0))
        self.assertFalse(mail.outbox)

    def test_failed_payment_and_its_recovery_are_told_and_linksterr_is_asked_at_once(self):
        with mock.patch("apps.growth.linksterr.ping_soon") as ping:
            with self.captureOnCommitCallbacks(execute=True):
                self.checkout()
            self.assertEqual(ping.call_count, 1)  # first payment: Linksterr opens the campaign now
            with self.captureOnCommitCallbacks(execute=True):
                self.send("evt_f", "invoice.payment_failed", {"id": "in_f", "subscription": "sub_1"}, stripe_sub("past_due"))
            with self.captureOnCommitCallbacks(execute=True):
                self.send("evt_r", "invoice.paid", {"id": "in_r", "subscription": "sub_1", "billing_reason": "subscription_cycle"})
            self.assertEqual(ping.call_count, 3)
            with self.captureOnCommitCallbacks(execute=True):
                self.send("evt_same", "customer.subscription.updated", stripe_sub())
            self.assertEqual(ping.call_count, 3)  # nothing changed: no ping
        self.assertEqual(len(self.team("ödemesi alınamadı")), 1)
        self.assertEqual(len(self.team("ödemesi alındı")), 1)
        self.assertEqual(sum(m.subject == "Payment received: your campaign is running again" for m in mail.outbox), 1)

    def test_unpaid_checkout_does_nothing(self):
        self.checkout(payment_status="unpaid")
        self.sub.refresh_from_db()
        self.assertEqual(self.sub.status, "pending")
        self.assertFalse(mail.outbox)

    def test_renewal_failed_payment_cancel(self):
        self.checkout()
        renewal = {"id": "in_2", "parent": {"subscription_details": {"subscription": "sub_1"}},
                   "billing_reason": "subscription_cycle", "amount_paid": 14999}
        self.send("evt_3", "invoice.paid", renewal)
        self.assertEqual(len(self.team("yenilendi (ödendi)")), 1)
        self.send("evt_4", "invoice.payment_failed", {"id": "in_3", "subscription": "sub_1"}, stripe_sub("past_due"))
        self.sub.refresh_from_db()
        self.assertEqual(self.sub.status, "past_due")
        self.send("evt_5", "customer.subscription.updated", stripe_sub(cancel_at_period_end=True))
        self.sub.refresh_from_db()
        self.assertEqual((self.sub.status, self.sub.cancel_at_period_end), ("active", True))
        self.send("evt_6", "customer.subscription.deleted", stripe_sub("canceled"))
        self.sub.refresh_from_db()
        self.assertEqual(self.sub.status, "canceled")
        self.assertIsNotNone(self.sub.canceled_at)
        self.assertEqual(len(self.team("iptal edildi")), 1)
        self.assertEqual(sum(m.subject.startswith("Your campaign has started") for m in mail.outbox), 1)  # the welcome went out once
        self.assertEqual(len(self.team("ödemesi alınamadı")), 1)  # past_due: the campaign pauses
        self.assertEqual(sum(m.subject.startswith("We couldn't take your payment") for m in mail.outbox), 1)


@override_settings(**STRIPE_ON)
class CancelTests(TestCase):
    """Cancel from the dashboard or the reminder's link, take it back, the 3-day reminder."""

    def setUp(self):
        self.user = get_user_model().objects.create_user("me@example.com", "me@example.com", "pass-word-1")
        self.sub = AgencySubscription.objects.create(
            user=self.user, email="me@example.com", handle="brand", location="Berlin", lang="en", plan="starter",
            amount="79.99", status="active", started_at=timezone.now(), stripe_subscription_id="sub_1",
            stripe_customer_id="cus_1", current_period_end=timezone.now() + timedelta(days=2))
        self.url = reverse("growth:cancel", args=[self.sub.pk])

    def cancel(self, path, data):
        with mock.patch("apps.growth.billing.set_cancel", return_value=stripe_sub(cancel_at_period_end=True)) as set_cancel:
            r = self.client.post(path, data)
        set_cancel.assert_called_once_with("sub_1", True)
        self.sub.refresh_from_db()
        return r

    def team(self, words):
        return [m for m in mail.outbox if words in m.subject]

    def test_cancel_from_the_dashboard(self):
        self.client.force_login(self.user)
        r = self.client.get(reverse("growth:account") + "?lang=en")
        self.assertContains(r, self.url)
        self.assertContains(self.client.get(self.url + "?lang=en"), "Yes, cancel")
        r = self.cancel(self.url, {"lang": "en"})
        self.assertContains(r, "Your subscription is canceled")
        self.assertEqual((self.sub.cancel_at_period_end, self.sub.cancel_source, self.sub.status), (True, "account", "active"))
        self.assertIsNotNone(self.sub.cancel_requested_at)
        team = self.team("iptal talebi")
        self.assertEqual(len(team), 1)
        self.assertIn("hesap panelinden", team[0].body)
        self.assertEqual(len([m for m in mail.outbox if m.subject.startswith("Cancellation confirmed")]), 1)
        # Stripe's own webhook for the same change sends nothing more.
        body, header = signed({"id": "evt_c", "type": "customer.subscription.updated", "data": {"object": stripe_sub(cancel_at_period_end=True)}})
        self.client.post(reverse("growth:webhook"), body, content_type="application/json", HTTP_STRIPE_SIGNATURE=header)
        self.assertEqual(len(self.team("iptal talebi")), 1)
        self.assertContains(self.client.get(reverse("growth:account") + "?lang=en"), reverse("growth:resume", args=[self.sub.pk]))

    def test_cancel_needs_the_owner(self):
        self.assertEqual(self.client.get(self.url).status_code, 302)  # signed out: to the login page
        other = get_user_model().objects.create_user("x@example.com", "x@example.com", "pass-word-1")
        self.client.force_login(other)
        self.assertContains(self.client.get(self.url + "?lang=en"), "This link no longer works")

    def test_reminder_once_per_period(self):
        body, header = signed({"id": "evt_u", "type": "invoice.upcoming", "data": {"object": {
            "parent": {"subscription_details": {"subscription": "sub_1"}}, "amount_due": 7999}}})
        for _ in range(2):
            self.client.post(reverse("growth:webhook"), body, content_type="application/json", HTTP_STRIPE_SIGNATURE=header)
        call_command("send_renewal_reminders", stdout=StringIO())
        reminders = [m for m in mail.outbox if m.subject.startswith("Your Starter Creator package renews in 2 days")]
        self.assertEqual(len(reminders), 1)
        text = reminders[0].body
        self.assertNotIn("cancel", text.split("--")[0].lower())  # only the small note at the very end mentions it
        self.assertIn("manage or cancel your subscription any time in your account", text.split("--")[1])
        self.assertIn("/account/?lang=en", text)

    def test_reminder_command_skips_far_or_canceling(self):
        far = AgencySubscription.objects.create(email="f@example.com", handle="far", location="x", plan="rising", amount="149.99",
                                                status="active", stripe_subscription_id="sub_2",
                                                current_period_end=timezone.now() + timedelta(days=20))
        AgencySubscription.objects.filter(pk=self.sub.pk).update(cancel_at_period_end=True)
        call_command("send_renewal_reminders", stdout=StringIO())
        self.assertFalse(mail.outbox)
        far.refresh_from_db()
        self.assertIsNone(far.reminded_for)

    def test_resume(self):
        AgencySubscription.objects.filter(pk=self.sub.pk).update(cancel_at_period_end=True, cancel_source="account",
                                                                 cancel_requested_at=timezone.now())
        self.client.force_login(self.user)
        with mock.patch("apps.growth.billing.set_cancel", return_value=stripe_sub()) as set_cancel:
            r = self.client.post(reverse("growth:resume", args=[self.sub.pk]), {"lang": "en"})
        set_cancel.assert_called_once_with("sub_1", False)
        self.assertEqual(r["Location"], f"{reverse('growth:account')}?lang=en&resumed=1")
        self.sub.refresh_from_db()
        self.assertEqual((self.sub.cancel_at_period_end, self.sub.cancel_source, self.sub.cancel_requested_at), (False, "", None))
        self.assertEqual(len(self.team("iptali geri alındı")), 1)


@override_settings(**STRIPE_ON)
class DisputeTests(FreshCache, TestCase):
    def setUp(self):
        super().setUp()
        self.user = get_user_model().objects.create_user("me@example.com", "me@example.com", "pass-word-1")
        self.sub = AgencySubscription.objects.create(
            user=self.user, email="me@example.com", handle="brand", location="Berlin", plan="rising", amount="149.99",
            status="active", started_at=timezone.now() - timedelta(days=12), stripe_subscription_id="sub_1",
            stripe_customer_id="cus_1", current_period_end=timezone.now() + timedelta(days=18), ip="203.0.113.9",
            terms_accepted_at=timezone.now() - timedelta(days=12), terms_version=TERMS_VERSION)
        SubscriptionStat.objects.create(subscription=self.sub, date=timezone.now().date(), new_followers=140, impressions=1200,
                                        visits=310, confirms=95, countries={"DE": {"impressions": 900, "visits": 200, "confirms": 70}})

    def dispute(self, event_id, status="needs_response", traced=("sub_1", "cus_1")):
        obj = {"id": "dp_1", "object": "dispute", "amount": 14999, "reason": "product_not_received", "status": status,
               "charge": "ch_1", "payment_intent": "pi_1", "evidence_details": {"due_by": 1767225600}}
        body, header = signed({"id": event_id, "type": f"charge.dispute.{'created' if status == 'needs_response' else 'closed'}",
                               "data": {"object": obj}})
        with mock.patch("apps.growth.billing.dispute_subscription", return_value=traced), \
                mock.patch("apps.growth.billing.stage_evidence") as stage:
            self.client.post(reverse("growth:webhook"), body, content_type="application/json", HTTP_STRIPE_SIGNATURE=header)
        return stage

    def test_dispute_stages_evidence_and_tells_the_team(self):
        self.client.force_login(self.user)  # a sign-in and a dashboard visit are on record
        self.client.get(reverse("growth:account") + "?lang=en")
        stage = self.dispute("evt_d1")
        dispute_id, evidence = stage.call_args.args
        self.assertEqual(dispute_id, "dp_1")
        self.assertIn("@brand", evidence["product_description"])
        self.assertIn("Growsterr Rising Influencer", evidence["product_description"])
        self.assertIn("203.0.113.9", evidence["cancellation_policy_disclosure"])
        self.assertIn("/terms/#subscription", evidence["cancellation_policy_disclosure"])
        self.assertIn("follow step shown 1,200 times", evidence["uncategorized_text"])
        self.assertIn("DE 900", evidence["uncategorized_text"])
        self.assertIn("opened the growth dashboard", evidence["access_activity_log"])
        self.assertIn("never canceled", evidence["cancellation_rebuttal"])
        self.assertTrue(all(len(v) <= 20000 for v in evidence.values()))
        self.assertFalse(any("Sterr " in v for v in evidence.values()))
        d = Dispute.objects.get()
        self.assertEqual((d.subscription_id, str(d.amount), d.evidence_staged), (self.sub.pk, "149.99", True))
        team = [m for m in mail.outbox if "itiraz (dispute) açıldı" in m.subject]
        self.assertEqual(len(team), 1)
        self.assertIn("dashboard.stripe.com/disputes/dp_1", team[0].body)
        self.dispute("evt_d2", status="won")
        self.assertEqual(Dispute.objects.get().status, "won")
        self.assertIn("KAZANILDI", [m for m in mail.outbox if "itirazı sonuçlandı" in m.subject][0].body)

    def test_another_sites_dispute_is_skipped(self):
        stage = self.dispute("evt_d3", traced=("sub_x", "cus_x"))
        stage.assert_not_called()
        self.assertFalse(Dispute.objects.exists())
        self.assertFalse(mail.outbox)

    def test_canceled_subscription_evidence_keeps_growth_obligation(self):
        self.sub.refresh_from_db()
        self.sub.status = "canceled"
        self.sub.cancel_requested_at = timezone.now()
        self.sub.cancel_source = "stripe"
        fields = evidence.build(self.sub)
        for name in ("cancellation_rebuttal", "refund_refusal_explanation", "uncategorized_text"):
            self.assertIn("remains owed", fields[name])
            self.assertIn("no renewed subscription or payment is required", fields[name])
            self.assertIn("illustration, not this customer's measured balance", fields[name])
        self.assertIn("includes the growth shortfall policy", fields["uncategorized_text"])
        self.assertNotIn("was delivered every day", fields["refund_refusal_explanation"])
        self.assertNotIn("No payment was taken after that", fields["cancellation_rebuttal"])

    def test_old_or_missing_acceptance_does_not_claim_new_policy_was_accepted(self):
        self.sub.refresh_from_db()
        for version, accepted_at in (("2026-11-08", self.sub.terms_accepted_at), ("", None), (TERMS_VERSION, None)):
            with self.subTest(version=version, accepted_at=accepted_at):
                self.sub.terms_version = version
                self.sub.terms_accepted_at = accepted_at
                text = evidence.build(self.sub)["uncategorized_text"]
                self.assertIn("do not claim the customer accepted this later wording at purchase", text)
                self.assertNotIn("includes the growth shortfall policy", text)

    def test_evidence_page_in_admin(self):
        admin = get_user_model().objects.create_superuser("boss", "boss@example.com", "pass-word-1")
        self.client.force_login(admin)
        r = self.client.get(reverse("admin:growth_agencysubscription_evidence", args=[self.sub.pk]))
        self.assertContains(r, "Growsterr: service record for @brand")
        self.assertContains(r, "follow step shown 1,200 times")
        self.assertFalse(AccountActivity.objects.filter(user=admin).exists())  # staff sign-ins aren't customer activity

    def test_activity_log_once_an_hour(self):
        self.client.post(reverse("growth:login") + "?lang=en", {"email": "me@example.com", "password": "pass-word-1"},
                         HTTP_X_FORWARDED_FOR="198.51.100.4")
        for _ in range(3):
            self.client.get(reverse("growth:account") + "?lang=en")
        self.assertEqual(sorted(AccountActivity.objects.values_list("kind", flat=True)), ["dashboard", "login"])
        self.assertEqual(AccountActivity.objects.get(kind="login").ip, "198.51.100.4")


@override_settings(GROWTH_API_TOKEN="tok_test", **MAIL)
class StatsApiTests(TestCase):
    def setUp(self):
        self.sub = AgencySubscription.objects.create(email="a@example.com", handle="brand", location="Oslo", amount="79.99",
                                                     status="active", started_at=timezone.now() - timedelta(days=5),
                                                     current_period_end=timezone.now() + timedelta(days=25))

    def post(self, payload, token="tok_test"):
        return self.client.post(reverse("growth:api_stats"), json.dumps(payload), content_type="application/json",
                                HTTP_AUTHORIZATION=f"Bearer {token}")

    def test_token_required(self):
        self.assertEqual(self.post({"subscription_id": self.sub.pk}, token="nope").status_code, 401)
        self.assertEqual(self.client.get(reverse("growth:api_subscriptions")).status_code, 401)

    def test_lists_active_subscriptions_with_their_source(self):
        r = self.client.get(reverse("growth:api_subscriptions"), HTTP_AUTHORIZATION="Bearer tok_test")
        items = r.json()["subscriptions"]
        self.assertEqual([s["handle"] for s in items], ["brand"])
        self.assertEqual(set(items[0]), {"id", "source", "platform", "handle", "location", "status", "plan", "amount",
                                         "started_at", "current_period_end", "cancel_at_period_end", "canceled_at",
                                         "start_followers", "current_followers", "video_url"})
        self.assertEqual(items[0]["source"], "growsterr")

    @override_settings(GROWTH_API_TOKEN="")
    def test_off_without_a_token(self):
        self.assertEqual(self.client.get(reverse("growth:api_subscriptions"), HTTP_AUTHORIZATION="Bearer ").status_code, 401)
        self.assertEqual(self.post({"subscription_id": self.sub.pk}, token="").status_code, 401)

    @override_settings(LINKSTERR_AGENCY_TOKEN="agency-test-token")
    def test_linksterr_token_reads_subscriptions_but_cannot_write(self):
        AgencySubscription.objects.filter(pk=self.sub.pk).update(cancel_at_period_end=True, plan="pro", amount="279.99")
        r = self.client.get(reverse("growth:api_subscriptions") + "?status=active,past_due,canceled",
                            HTTP_AUTHORIZATION="Bearer agency-test-token")
        item = r.json()["subscriptions"][0]
        self.assertEqual((item["plan"], item["amount"], item["cancel_at_period_end"], item["canceled_at"]), ("pro", 279.99, True, None))
        self.assertEqual(item["source"], "growsterr")
        self.assertIsNotNone(item["current_period_end"])
        self.assertEqual(self.post({"subscription_id": self.sub.pk, "new_followers": 5}, token="agency-test-token").status_code, 401)
        self.assertFalse(SubscriptionStat.objects.exists())

    def test_daily_stats(self):
        today = timezone.now().date()
        r = self.post({"updates": [
            {"subscription_id": self.sub.pk, "date": str(today - timedelta(days=2)), "followers": 1200, "likes": 40, "comments": 2},
            {"subscription_id": self.sub.pk, "date": str(today), "followers": 1650, "likes": 300, "comments": 9},
            {"subscription_id": 999999, "likes": 1},
            {"subscription_id": self.sub.pk, "likes": -1},
        ]})
        self.assertEqual(r.status_code, 207)
        self.sub.refresh_from_db()
        self.assertEqual((self.sub.start_followers, self.sub.current_followers, self.sub.gained), (1200, 1650, 450))
        self.post({"subscription_id": self.sub.pk, "date": str(today), "followers": 1700, "likes": 310, "comments": 9})
        self.assertEqual(SubscriptionStat.objects.count(), 2)
        self.sub.refresh_from_db()
        self.assertEqual(self.sub.gained, 500)

    def test_delivery_evidence(self):
        r = self.post({"subscription_id": self.sub.pk, "date": "2026-11-04", "new_followers": 120, "impressions": 1500,
                       "visits": 300, "confirms": 110, "countries": {"no": {"impressions": 1500, "visits": 300, "confirms": 110}}})
        self.assertEqual(r.status_code, 200)
        stat = SubscriptionStat.objects.get()
        self.assertEqual((stat.impressions, stat.visits, stat.confirms), (1500, 300, 110))
        self.assertEqual(stat.countries, {"NO": {"impressions": 1500, "visits": 300, "confirms": 110}})
        r = self.post({"subscription_id": self.sub.pk, "countries": {"Norway": {"impressions": 1}}})
        self.assertEqual(r.status_code, 207)

    def test_our_count_of_new_followers_wins_over_the_follower_count(self):
        today = timezone.now().date()
        self.post({"updates": [
            {"subscription_id": self.sub.pk, "date": str(today - timedelta(days=1)), "followers": 1000, "new_followers": 80},
            {"subscription_id": self.sub.pk, "date": str(today), "followers": 1050, "new_followers": 120},
            {"subscription_id": self.sub.pk, "date": str(today - timedelta(days=2)), "new_followers": 40},
        ]})
        self.sub.refresh_from_db()
        daily = self.sub.daily()
        self.assertEqual([d["followers"] for d in daily], [40, 80, 120])
        self.assertEqual([(d["likes"], d["comments"]) for d in daily], [(None, None)] * 3)  # nothing invented
        self.assertEqual(self.sub.gained, 240)

    def test_dashboard_shows_the_numbers(self):
        user = get_user_model().objects.create_user("a@example.com", "a@example.com", "pass-word-1")
        self.sub.user = user
        self.sub.save()
        today = timezone.now().date()
        self.post({"updates": [{"subscription_id": self.sub.pk, "date": str(today - timedelta(days=3)), "followers": 4200, "likes": 500},
                               {"subscription_id": self.sub.pk, "date": str(today), "followers": 5400, "likes": 1500, "comments": 120}]})
        self.client.force_login(user)
        html = self.client.get(reverse("growth:account") + "?lang=en").content.decode()
        self.assertIn("Today", html)
        self.assertIn("+1,200", html)  # new followers today (count went 4,200 -> 5,400)
        self.assertNotIn("Likes", html)  # never shown: Linksterr does not measure them
        self.assertIn("<rect", html)  # new followers per day
        self.assertIn("Day by day", html)
        self.assertIn("Renews on", html)
        self.assertIn("New followers so far", html)


def linksterr_account(account="instagram:brand", days=(), readings=(), projection=None):
    return {"account": account, "platform": account.split(":")[0], "handle": account.split(":")[1],
            "projection": projection,
            "campaigns": [{"id": 2, "status": "active", "live": True, "period_start": None, "period_end": None,
                           "rate": 0.057, "own_weight": 0.1}] if days else [],
            "readings": list(readings), "days": list(days)}


def linksterr_day(date, new=40, visits=420, impressions=700, confirms=380, countries=None):
    return {"date": str(date), "live": True, "new_followers": new, "visits": visits, "impressions": impressions,
            "confirms": confirms, "countries": countries if countries is not None else {"DE": {"impressions": 500, "visits": 300, "confirms": 250}}}


@override_settings(LINKSTERR_AGENCY_TOKEN="agency-test-token", LINKSTERR_API_URL="https://linksterr.example", **MAIL)
class LinksterrTests(FreshCache, TestCase):
    def setUp(self):
        super().setUp()
        self.user = get_user_model().objects.create_user("me@example.com", "me@example.com", "pass-word-1")
        self.today = timezone.now().date()
        self.sub = AgencySubscription.objects.create(
            user=self.user, email="me@example.com", handle="Brand", location="Berlin", plan="starter", amount="79.99",
            status="active", started_at=timezone.now() - timedelta(days=5), stripe_subscription_id="sub_1",
            current_period_end=timezone.now() + timedelta(days=25))

    def respond(self, *accounts, status=200):
        response = mock.Mock(status_code=status)
        response.json.return_value = {"day": "UTC", "accounts": list(accounts)}
        response.raise_for_status.side_effect = None if status == 200 else requests.HTTPError(str(status))
        return mock.patch("apps.growth.linksterr.requests.get", return_value=response)

    def test_sync_stores_the_days_of_the_package(self):
        start = self.today - timedelta(days=5)
        days = [linksterr_day(start - timedelta(days=1), new=999),  # before the package: not ours
                linksterr_day(start, new=30, countries={"DE": {"impressions": 1, "visits": 2, "confirms": 3}, "": {"visits": 9}}),
                linksterr_day(self.today, new=41)]
        readings = [{"date": str(start - timedelta(days=1)), "followers": 1000}, {"date": str(self.today), "followers": 1071}]
        with self.respond(linksterr_account(days=days, readings=readings)) as get:
            self.assertEqual(linksterr.sync([self.sub]), 1)
        args, kwargs = get.call_args
        self.assertEqual(args[0], "https://linksterr.example/user-api/v1/agency/accounts/")
        self.assertEqual(kwargs["headers"], {"Authorization": "Bearer agency-test-token"})
        self.assertIn(("account", "instagram:brand"), kwargs["params"])
        self.assertIn(("since", str(start)), kwargs["params"])
        self.assertIn(("until", str(self.today)), kwargs["params"])
        rows = {s.date: s for s in SubscriptionStat.objects.filter(subscription=self.sub)}
        self.assertEqual(sorted(rows), [start, self.today])
        self.assertEqual((rows[start].new_followers, rows[start].visits, rows[start].confirms), (30, 420, 380))
        self.assertEqual(rows[start].countries, {"DE": {"impressions": 1, "visits": 2, "confirms": 3}})
        self.assertEqual(rows[self.today].followers, 1071)
        self.assertIsNone(rows[self.today].likes)  # Linksterr does not measure likes
        self.sub.refresh_from_db()
        self.assertEqual((self.sub.start_followers, self.sub.current_followers), (1000, 1071))
        self.assertIsNotNone(self.sub.stats_at)

    def test_settled_days_are_not_rewritten(self):
        old, recent = self.today - timedelta(days=4), self.today - timedelta(days=1)
        with self.respond(linksterr_account(days=[linksterr_day(old, new=30), linksterr_day(recent, new=30)])):
            linksterr.sync([self.sub])
        with self.respond(linksterr_account(days=[linksterr_day(old, new=55), linksterr_day(recent, new=55)])):
            linksterr.sync([self.sub], force=True)
        rows = dict(SubscriptionStat.objects.filter(subscription=self.sub).values_list("date", "new_followers"))
        self.assertEqual(rows, {old: 30, recent: 55})

    def test_fetches_at_most_every_ten_minutes_and_survives_outages(self):
        with self.respond(linksterr_account()) as get:
            linksterr.sync([self.sub])
            linksterr.sync([self.sub])
            self.assertEqual(get.call_count, 1)
            linksterr.sync([self.sub], force=True)
            self.assertEqual(get.call_count, 2)
        with mock.patch("apps.growth.linksterr.requests.get", side_effect=requests.ConnectionError("down")):
            self.assertEqual(linksterr.sync([self.sub], force=True), 0)
        with self.respond(status=500):
            self.assertEqual(linksterr.sync([self.sub], force=True), 0)

    def test_many_subscriptions_go_in_batches_within_linksterrs_limits(self):
        subs = [self.sub] + [AgencySubscription.objects.create(
            email=f"u{i}@example.com", handle=f"brand{i}", location="x", plan="starter", amount="79.99", status="active",
            started_at=timezone.now() - timedelta(days=500)) for i in range(120)]
        with self.respond(linksterr_account()) as get:
            linksterr.sync(subs)
        self.assertEqual(get.call_count, 2)
        for args, kwargs in get.call_args_list:
            params = kwargs["params"]
            self.assertLessEqual(sum(1 for k, _ in params if k == "account"), 100)
            self.assertIn(("since", str(self.today - timedelta(days=399))), params)

    def test_a_day_fetched_while_running_is_fetched_again_later(self):
        day = self.today - timedelta(days=3)
        with self.respond(linksterr_account(days=[linksterr_day(day, new=15)])):
            linksterr.sync([self.sub])
        SubscriptionStat.objects.filter(date=day).update(synced_at=timezone.now() - timedelta(days=3, hours=12))  # mid-day
        with self.respond(linksterr_account(days=[linksterr_day(day, new=45)])) as get:
            linksterr.sync([self.sub], force=True)
        self.assertEqual(SubscriptionStat.objects.get(date=day).new_followers, 45)
        self.assertIn(("since", str(day)), get.call_args.kwargs["params"])
        with self.respond(linksterr_account(days=[linksterr_day(day, new=99)])):
            linksterr.sync([self.sub], force=True)
        self.assertEqual(SubscriptionStat.objects.get(date=day).new_followers, 45)  # now settled

    def test_two_packages_of_one_account_never_count_a_day_twice(self):
        second = AgencySubscription.objects.create(
            user=self.user, email="me@example.com", handle="brand", location="x", plan="pro", amount="279.99",
            status="active", started_at=timezone.now() - timedelta(days=1))
        days = [linksterr_day(self.today - timedelta(days=n), new=10) for n in range(4)]
        with self.respond(linksterr_account(days=days)):
            linksterr.sync([self.sub, second])
        first_days = set(SubscriptionStat.objects.filter(subscription=self.sub).values_list("date", flat=True))
        second_days = set(SubscriptionStat.objects.filter(subscription=second).values_list("date", flat=True))
        self.assertFalse(first_days & second_days)
        self.assertEqual(len(first_days | second_days), 4)

    def test_a_bad_handle_or_a_failed_batch_does_not_stop_the_rest(self):
        odd = AgencySubscription.objects.create(email="x@example.com", handle="not valid!", location="x", plan="starter",
                                                amount="79.99", status="active", started_at=timezone.now())
        with self.respond(linksterr_account(days=[linksterr_day(self.today)])) as get:
            self.assertEqual(linksterr.sync([self.sub, odd]), 1)
        self.assertNotIn(("account", "instagram:not valid!"), get.call_args.kwargs["params"])

    def test_youtube_is_pulled_with_its_handle_rule(self):
        # Linksterr takes youtube:<handle> (3-30 chars, may hold "-"); an Instagram name may not.
        tube = AgencySubscription.objects.create(user=self.user, email="me@example.com", handle="my-channel", location="x",
                                                 platform="youtube", plan="starter", amount="79.99", status="active",
                                                 started_at=timezone.now())
        with self.respond(linksterr_account(account="youtube:my-channel", days=[linksterr_day(self.today)])) as get:
            self.assertEqual(linksterr.sync([tube], force=True), 1)
        self.assertEqual([v for k, v in get.call_args.kwargs["params"] if k == "account"], ["youtube:my-channel"])
        self.assertTrue(tube.stats.exists())
        dashed = AgencySubscription.objects.create(user=self.user, email="me@example.com", handle="my-brand", location="x",
                                                   platform="instagram", plan="starter", amount="79.99", status="active",
                                                   started_at=timezone.now())
        with self.respond(linksterr_account(account="instagram:my-brand")) as get:
            self.assertEqual(linksterr.sync([dashed], force=True), 0)
        get.assert_not_called()

    def test_linksterr_token_sees_only_paid_packages(self):
        AgencySubscription.objects.create(email="p@example.com", handle="unpaid", location="x", plan="starter",
                                          amount="79.99", status="pending")
        AgencySubscription.objects.create(email="o@example.com", handle="oldend", location="x", plan="starter", amount="79.99",
                                          status="canceled", started_at=timezone.now() - timedelta(days=200),
                                          canceled_at=timezone.now() - timedelta(days=120))
        r = self.client.get(reverse("growth:api_subscriptions") + "?status=active,pending,canceled",
                            HTTP_AUTHORIZATION="Bearer agency-test-token")
        self.assertEqual([s["handle"] for s in r.json()["subscriptions"]], ["Brand"])

    @override_settings(LINKSTERR_AGENCY_TOKEN="")
    def test_off_without_a_token(self):
        with mock.patch("apps.growth.linksterr.requests.get") as get:
            self.assertEqual(linksterr.sync([self.sub], force=True), 0)
        get.assert_not_called()

    def test_canceled_package_stops_at_its_last_day(self):
        AgencySubscription.objects.filter(pk=self.sub.pk).update(status="canceled", canceled_at=timezone.now() - timedelta(days=2))
        self.sub.refresh_from_db()
        last = (timezone.now() - timedelta(days=2)).date()
        with self.respond(linksterr_account(days=[linksterr_day(last), linksterr_day(self.today)])):
            linksterr.sync([self.sub])
        self.assertEqual(list(SubscriptionStat.objects.filter(subscription=self.sub).values_list("date", flat=True)), [last])

    def test_ping_asks_linksterr_and_never_raises(self):
        with mock.patch("apps.growth.linksterr.requests.post") as post:
            self.assertTrue(linksterr.ping())
        self.assertEqual(post.call_args.args[0], "https://linksterr.example/user-api/v1/agency/sync/")
        with mock.patch("apps.growth.linksterr.requests.post", side_effect=requests.ConnectionError("down")):
            self.assertFalse(linksterr.ping())

    def test_dashboard_fetches_and_shows_what_they_gained(self):
        self.client.force_login(self.user)
        with self.respond(linksterr_account(days=[linksterr_day(self.today, new=41, visits=420)])) as get:
            html = self.client.get(reverse("growth:account") + "?lang=en").content.decode()
        get.assert_called_once()
        self.assertIn("+41", html)
        self.assertIn("Profile visits", html)
        self.assertIn("420", html)
        self.assertIn("Visits by country:", html)
        self.assertIn('data-region="DE">DE</span> <b>100%</b>', html)
        self.assertIn("These numbers come from our delivery system", html)
        self.assertNotIn("Likes", html)
        self.assertNotIn(">700<", html)  # impressions stay out of the customer's dashboard

    def test_the_30_day_projection_reaches_the_dashboard_and_the_admin(self):
        projection = {"days": 30, "new_followers": 1230, "low": 1160, "high": 1290, "per_day": 41.0}
        self.client.force_login(self.user)
        with self.respond(linksterr_account(days=[linksterr_day(self.today)], projection=projection)):
            html = self.client.get(reverse("growth:account") + "?lang=en").content.decode()
        self.assertIn("Next 30 days at today&#x27;s pace: on average about 1,230 new followers (1,160–1,290)", html)
        self.sub.refresh_from_db()
        self.assertEqual(self.sub.projection, projection)
        boss = get_user_model().objects.create_superuser("boss", "boss@example.com", "pass-word-1")
        self.client.force_login(boss)
        self.assertContains(self.client.get(reverse("admin:growth_agencysubscription_changelist")), "~1.230 takipçi (1.160–1.290)")
        AgencySubscription.objects.filter(pk=self.sub.pk).update(status="canceled", canceled_at=timezone.now())
        self.client.force_login(self.user)
        with self.respond(linksterr_account(days=[linksterr_day(self.today)], projection=projection)):
            self.assertNotIn("Next 30 days", self.client.get(reverse("growth:account") + "?lang=en").content.decode())

    def test_staff_sees_a_customers_dashboard_read_only(self):
        SubscriptionStat.objects.create(subscription=self.sub, date=self.today, new_followers=41, visits=420)
        path = reverse("growth:view_as", args=[self.user.pk]) + "?lang=en"
        self.assertEqual(self.client.get(path).status_code, 302)  # signed out: to the admin login
        self.client.force_login(self.user)
        self.assertEqual(self.client.get(path).status_code, 302)  # a customer cannot use it
        boss = get_user_model().objects.create_user("boss@example.com", "boss@example.com", "pass-word-1", is_staff=True)
        self.client.force_login(boss)
        self.assertEqual(self.client.get(path).status_code, 403)  # staff without the growth permission
        from django.contrib.auth.models import Permission
        boss.user_permissions.add(Permission.objects.get(codename="view_agencysubscription"))
        boss = get_user_model().objects.get(pk=boss.pk)
        self.client.force_login(boss)
        with self.respond(linksterr_account()):
            r = self.client.get(path)
        html = r.content.decode()
        self.assertEqual(r.status_code, 200)
        self.assertIn("me@example.com", html)
        self.assertIn("+41", html)
        self.assertIn("salt okunur", html)
        for action in ("growth:logout", "growth:billing"):
            self.assertNotIn(reverse(action), html)
        self.assertNotIn(reverse("growth:cancel", args=[self.sub.pk]), html)
        self.assertNotIn("csrfmiddlewaretoken", html)  # no form at all
        self.assertIn("no-cache", r["Cache-Control"])
        self.assertFalse(AccountActivity.objects.filter(user=self.user, kind="dashboard").exists())
        self.assertEqual(self.client.get(reverse("growth:view_as", args=[9999])).status_code, 404)

    def test_admin_lists_link_to_the_read_only_dashboard(self):
        Customer.objects.create(user=self.user, lang="de")
        boss = get_user_model().objects.create_superuser("boss", "boss@example.com", "pass-word-1")
        self.client.force_login(boss)
        link = reverse("growth:view_as", args=[self.user.pk])
        self.assertContains(self.client.get(reverse("admin:growth_customer_changelist")), f"{link}?lang=de")
        self.assertContains(self.client.get(reverse("admin:growth_agencysubscription_changelist")), link)

    def test_admin_sync_action(self):
        boss = get_user_model().objects.create_superuser("boss", "boss@example.com", "pass-word-1")
        self.client.force_login(boss)
        with self.respond(linksterr_account(days=[linksterr_day(self.today)])) as get:
            r = self.client.post(reverse("admin:growth_agencysubscription_changelist"),
                                 {"action": "sync_linksterr", "_selected_action": [self.sub.pk]}, follow=True)
        get.assert_called_once()
        self.assertContains(r, "1 abonelik güncellendi")

    def test_sync_command(self):
        with self.respond(linksterr_account(days=[linksterr_day(self.today)])):
            out = StringIO()
            call_command("sync_linksterr", stdout=out)
        self.assertIn("Subscriptions updated: 1 of 1", out.getvalue())

    def test_stats_api_updates_only_the_fields_sent(self):
        SubscriptionStat.objects.create(subscription=self.sub, date=self.today, new_followers=40, impressions=700, visits=420)
        with override_settings(GROWTH_API_TOKEN="tok_test"):
            r = self.client.post(reverse("growth:api_stats"), json.dumps({"subscription_id": self.sub.pk, "date": str(self.today),
                                                                          "followers": 5000}),
                                 content_type="application/json", HTTP_AUTHORIZATION="Bearer tok_test")
        self.assertEqual(r.status_code, 200)
        row = SubscriptionStat.objects.get()
        self.assertEqual((row.followers, row.new_followers, row.impressions, row.visits), (5000, 40, 700, 420))


@override_settings(**STRIPE_OFF)
class YouTubeTests(FreshCache, TestCase):
    """YouTube: handles, subscribers instead of followers, a channel instead of a profile."""

    def test_order_with_a_youtube_handle(self):
        r = self.client.post(reverse("growth:order"), order_data(platform="youtube", handle="ab"))
        self.assertContains(r, "Enter a valid YouTube handle", status_code=400)
        r = self.client.post(reverse("growth:order"), order_data(platform="youtube", handle="https://www.youtube.com/@My-Channel.TV/videos"))
        sub = AgencySubscription.objects.get()
        self.assertEqual((sub.platform, sub.handle, sub.status), ("youtube", "my-channel.tv", "requested"))
        self.assertIn("platform=youtube", r["Location"])
        team = next(m for m in mail.outbox if "başvurusu" in m.subject)
        self.assertIn("Yeni YouTube influencer paketi başvurusu", team.subject)
        self.assertIn("https://www.youtube.com/@my-channel.tv", team.body)
        page = self.client.get(r["Location"]).content.decode()
        self.assertIn("Rising Influencer", page)
        self.assertIn("Thanks, we&#x27;ve got your request.", page)

    def test_emails_speak_of_subscribers_and_the_channel(self):
        from .notifications import confirm_payment
        sub = AgencySubscription.objects.create(email="yt@example.com", platform="youtube", handle="mychannel", location="Paris",
                                                plan="pro", amount="279.99", status="active",
                                                current_period_end=timezone.now() + timedelta(days=30))
        sub.refresh_from_db()
        confirm_payment(sub)
        body = mail.outbox[-1].body
        self.assertIn("discover your channel every day", body)
        self.assertIn("4,000-16,000 new subscribers", body)
        self.assertIn("subscribe, like your videos", body)
        self.assertNotIn("follower", body)

    def test_dashboard_waits_for_the_first_numbers(self):
        user = get_user_model().objects.create_user("yt@example.com", "yt@example.com", "pass-word-1")
        AgencySubscription.objects.create(user=user, email=user.email, platform="youtube", handle="mychannel", location="Paris",
                                          plan="starter", amount="79.99", status="active", started_at=timezone.now(),
                                          current_period_end=timezone.now() + timedelta(days=30))
        self.client.force_login(user)
        with override_settings(LINKSTERR_AGENCY_TOKEN="agency-test-token"), \
                mock.patch("apps.growth.linksterr.requests.get") as get:
            html = self.client.get(reverse("growth:account") + "?lang=en").content.decode()
        get.assert_called_once()  # YouTube channels are asked for too, as youtube:<handle>
        self.assertIn(("account", "youtube:mychannel"), get.call_args.kwargs["params"])
        self.assertIn("Your numbers appear here once delivery starts.", html)
        self.assertIn("Starter Creator · YouTube", html)
        self.assertNotIn("New subscribers so far", html)  # no totals before there is anything measured
        self.assertNotIn("Today", html)

    def test_dashboard_numbers_say_subscribers(self):
        user = get_user_model().objects.create_user("yt@example.com", "yt@example.com", "pass-word-1")
        sub = AgencySubscription.objects.create(user=user, email=user.email, platform="youtube", handle="mychannel", location="Paris",
                                                plan="starter", amount="79.99", status="active", started_at=timezone.now(),
                                                current_period_end=timezone.now() + timedelta(days=30))
        SubscriptionStat.objects.create(subscription=sub, date=timezone.now().date(), new_followers=12, visits=90)
        self.client.force_login(user)
        html = self.client.get(reverse("growth:account") + "?lang=en").content.decode()
        for text in ("New subscribers", "Channel visits", "+12", "New subscribers so far"):
            self.assertIn(text, html)
        self.assertNotIn("New followers", html)

    def test_mixed_audiences_are_never_added_up(self):
        user = get_user_model().objects.create_user("both@example.com", "both@example.com", "pass-word-1")
        for platform in ("instagram", "youtube"):
            sub = AgencySubscription.objects.create(user=user, email=user.email, platform=platform, handle="brand", location="x",
                                                    plan="starter", amount="79.99", status="active", started_at=timezone.now())
            SubscriptionStat.objects.create(subscription=sub, date=timezone.now().date(), new_followers=5)
        self.client.force_login(user)
        html = self.client.get(reverse("growth:account") + "?lang=en").content.decode()
        self.assertNotIn("so far", html)
        self.assertIn("New followers", html)
        self.assertIn("New subscribers", html)

    def test_the_api_lists_youtube(self):
        AgencySubscription.objects.create(email="yt@example.com", platform="youtube", handle="mychannel", location="Paris",
                                          plan="starter", amount="79.99", status="active", started_at=timezone.now())
        with override_settings(LINKSTERR_AGENCY_TOKEN="agency-test-token"):
            r = self.client.get(reverse("growth:api_subscriptions"), HTTP_AUTHORIZATION="Bearer agency-test-token")
        self.assertEqual([(s["platform"], s["source"]) for s in r.json()["subscriptions"]], [("youtube", "growsterr")])

    def test_admin_projection_in_subscribers(self):
        AgencySubscription.objects.create(email="yt@example.com", platform="youtube", handle="mychannel", location="Paris",
                                          plan="starter", amount="79.99", status="active",
                                          projection={"days": 30, "new_followers": 300, "low": 250, "high": 350, "per_day": 10.0})
        boss = get_user_model().objects.create_superuser("boss", "boss@example.com", "pass-word-1")
        self.client.force_login(boss)
        self.assertContains(self.client.get(reverse("admin:growth_agencysubscription_changelist")), "~300 abone (250–350)")


@override_settings(**MAIL)
class AccountTests(FreshCache, TestCase):
    def test_login_logout_and_bad_password(self):
        get_user_model().objects.create_user("me@example.com", "me@example.com", "pass-word-1")
        r = self.client.post(reverse("growth:login") + "?lang=en", {"email": "me@example.com", "password": "wrong-pass"})
        self.assertEqual(r.status_code, 400)
        r = self.client.post(reverse("growth:login") + "?lang=en", {"email": "ME@example.com", "password": "pass-word-1"})
        self.assertEqual(r["Location"], f"{reverse('growth:account')}?lang=en")
        self.assertEqual(self.client.get(r["Location"]).status_code, 200)
        r = self.client.post(reverse("growth:logout"), {"lang": "en"})
        self.assertEqual(r["Location"], "/")
        self.assertEqual(self.client.get(reverse("growth:account")).status_code, 302)
        self.assertEqual(self.client.get(reverse("growth:logout")).status_code, 405)

    def test_login_ignores_offsite_next(self):
        get_user_model().objects.create_user("me@example.com", "me@example.com", "pass-word-1")
        r = self.client.post(reverse("growth:login"), {"email": "me@example.com", "password": "pass-word-1", "next": "https://evil.example/"})
        self.assertTrue(r["Location"].startswith(reverse("growth:account")))

    def test_pages_follow_the_language(self):
        html = self.client.get(reverse("growth:login") + "?lang=tr").content.decode()
        self.assertIn('<html lang="tr"', html)
        self.assertIn(UI["tr"]["login_title"], html)
        html = self.client.get(reverse("growth:signup")).content.decode()  # the session remembers it
        self.assertIn(UI["tr"]["signup_title"], html)
        self.assertIn('<meta name="robots" content="noindex, nofollow">', html)

    def test_password_reset(self):
        get_user_model().objects.create_user("me@example.com", "me@example.com", "pass-word-1")
        self.client.post(reverse("growth:reset") + "?lang=en", {"email": "me@example.com"})
        self.client.post(reverse("growth:reset") + "?lang=en", {"email": "nobody@example.com"})
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn("Growsterr account", mail.outbox[0].body)
        path = re.search(r"https?://[^/\s]+(/account/password/\S+)", mail.outbox[0].body).group(1)
        r = self.client.post(path, {"password": "brand-new-pass"})
        self.assertEqual(r.status_code, 302)
        self.assertTrue(get_user_model().objects.get().check_password("brand-new-pass"))
        self.assertContains(self.client.get(path), "This link has expired")  # used link now shows "invalid"

    def test_signup(self):
        r = self.client.post(reverse("growth:signup") + "?lang=en", {"email": "new@example.com", "password": "pass-word-1", "consent": "on"})
        self.assertEqual(r["Location"], f"{reverse('growth:account')}?lang=en&verify=sent")
        self.assertTrue(mail.outbox[0].subject.startswith("Confirm your email"))
        self.assertIn("growsterr.com", mail.outbox[0].body)
        r = self.client.post(reverse("growth:signup") + "?lang=en", {"email": "new@example.com", "password": "pass-word-1", "consent": "on"})
        self.assertEqual(r.status_code, 400)

    def test_verify_link(self):
        self.client.post(reverse("growth:signup") + "?lang=en", {"email": "new@example.com", "password": "pass-word-1", "consent": "on"})
        link = re.search(r"https?://[^/\s]+(/account/verify/\S+/)", mail.outbox[0].body).group(1)
        self.assertEqual(self.client.get(link)["Location"], f"{reverse('growth:account')}?lang=en&verified=1")
        self.assertTrue(Customer.objects.get().email_verified)
        self.assertIn("verify=invalid", self.client.get(reverse("growth:verify", args=["bad-token"]))["Location"])

    def test_empty_dashboard(self):
        user = get_user_model().objects.create_user("me@example.com", "me@example.com", "pass-word-1")
        self.client.force_login(user)
        html = self.client.get(reverse("growth:account") + "?lang=en").content.decode()
        self.assertIn("No subscriptions yet", html)
        self.assertIn('href="/order/?lang=en"', html)


@override_settings(GOOGLE_OAUTH_CLIENT_ID="cid.apps.googleusercontent.com", GOOGLE_OAUTH_CLIENT_SECRET="GOCSPX-x", **MAIL)
class GoogleSignInTests(FreshCache, TestCase):
    def start(self, next_url="/order/?lang=en&platform=tiktok"):
        r = self.client.get(reverse("growth:google") + "?lang=de&next=" + quote(next_url, safe=""))
        self.assertTrue(r["Location"].startswith("https://accounts.google.com/o/oauth2/v2/auth?"))
        self.assertIn("redirect_uri=http%3A%2F%2Ftestserver%2Faccount%2Fgoogle%2Fcomplete%2F", r["Location"])
        return self.client.session["google_oauth"]["state"]

    def complete(self, state, info):
        token = mock.Mock(json=mock.Mock(return_value={"access_token": "at"}))
        userinfo = mock.Mock(json=mock.Mock(return_value=info))
        with mock.patch("apps.growth.accounts.requests.post", return_value=token), \
             mock.patch("apps.growth.accounts.requests.get", return_value=userinfo):
            return self.client.get(reverse("growth:google_complete") + f"?state={state}&code=abc")

    def test_new_user_is_created_verified_and_sent_back(self):
        state = self.start()
        r = self.complete(state, {"email": "New@Gmail.com", "email_verified": True, "given_name": "Ada"})
        self.assertEqual(r["Location"], "/order/?lang=en&platform=tiktok")
        user = get_user_model().objects.get(username="new@gmail.com")
        self.assertFalse(user.has_usable_password())
        self.assertTrue(user.customer.email_verified)
        self.assertEqual(user.customer.lang, "de")
        self.assertEqual(int(self.client.session["_auth_user_id"]), user.pk)

    def test_existing_account_signs_in(self):
        user = get_user_model().objects.create_user("me@gmail.com", "me@gmail.com", "pass-word-1")
        self.complete(self.start(), {"email": "me@gmail.com", "email_verified": True})
        self.assertEqual(int(self.client.session["_auth_user_id"]), user.pk)
        self.assertTrue(get_user_model().objects.get().check_password("pass-word-1"))

    def test_bad_state_or_unverified_email_fails(self):
        self.start()
        r = self.complete("wrong", {"email": "x@gmail.com", "email_verified": True})
        self.assertIn("google=failed", r["Location"])
        r = self.complete(self.start(), {"email": "x@gmail.com", "email_verified": False})
        self.assertIn("google=failed", r["Location"])
        self.assertFalse(get_user_model().objects.exists())

    def test_canceled_on_googles_screen_goes_back(self):
        self.start()
        r = self.client.get(reverse("growth:google_complete") + "?error=access_denied")
        self.assertEqual(r["Location"], "/order/?lang=en&platform=tiktok")

    def test_button_shows_on_login_and_order_form(self):
        self.assertContains(self.client.get(reverse("growth:login") + "?lang=en"), "Continue with Google")
        self.assertContains(self.client.get(reverse("growth:order") + "?lang=en"), "Continue with Google")


@override_settings(GOOGLE_OAUTH_CLIENT_ID="cid.apps.googleusercontent.com", GOOGLE_OAUTH_CLIENT_SECRET="GOCSPX-x")
class GoogleOrderTests(FreshCache, TestCase):
    """Order details first, then "Continue with Google" instead of email + password."""

    def google_order(self, **extra):
        data = order_data(via="google", platform="tiktok", plan="pro", **extra)
        del data["email"], data["password"]
        r = self.client.post(reverse("growth:order"), data)
        self.assertTrue(r["Location"].startswith(reverse("growth:google") + "?lang=en&order=1&next="))
        self.client.get(r["Location"])
        state = self.client.session["google_oauth"]["state"]
        token = mock.Mock(json=mock.Mock(return_value={"access_token": "at"}))
        userinfo = mock.Mock(json=mock.Mock(return_value={"email": "fan@gmail.com", "email_verified": True}))
        with mock.patch("apps.growth.accounts.requests.post", return_value=token), \
             mock.patch("apps.growth.accounts.requests.get", return_value=userinfo):
            return self.client.get(reverse("growth:google_complete") + f"?state={state}&code=abc")

    @override_settings(**STRIPE_OFF)
    def test_request_mode_places_the_filled_in_order(self):
        r = self.google_order()
        sub = AgencySubscription.objects.get()
        self.assertEqual((sub.email, sub.platform, sub.handle, sub.plan, sub.status),
                         ("fan@gmail.com", "tiktok", "my.brand", "pro", "requested"))
        self.assertIn(f"sub={sub.pk}", r["Location"])
        self.assertNotIn("google_order", self.client.session)

    @override_settings(**STRIPE_ON)
    def test_payments_on_go_straight_to_stripe(self):
        session = SimpleNamespace(id="cs_g", url="https://checkout.stripe.com/c/pay/cs_g")
        with mock.patch("apps.growth.billing.create_checkout", return_value=session) as create:
            r = self.google_order()
        self.assertEqual((r.status_code, r["Location"]), (303, session.url))  # Google verified the email: no extra step
        self.assertEqual(create.call_args.args[0].plan, "pro")

    @override_settings(**STRIPE_OFF)
    def test_details_are_still_required(self):
        data = order_data(via="google", handle="")
        del data["email"], data["password"]
        r = self.client.post(reverse("growth:order"), data)
        self.assertEqual(r.status_code, 400)
        self.assertContains(r, 'name="email"', status_code=400)  # the email/password option is still there
        self.assertNotIn("google_order", self.client.session)

    @override_settings(**STRIPE_OFF)
    def test_plain_sign_in_does_not_place_an_abandoned_order(self):
        data = order_data(via="google")
        del data["email"], data["password"]
        self.client.post(reverse("growth:order"), data)  # went to Google, never came back
        self.client.get(reverse("growth:google") + "?lang=en")  # later: plain sign-in
        self.assertNotIn("google_order", self.client.session)


@override_settings(STRIPE_SECRET_KEY="sk_test_x", SITE_URL="https://growsterr.com")
class SetupStripeTests(SimpleTestCase):
    """The Stripe account is shared: setup_stripe only ever touches Growsterr's own objects."""

    def client_mock(self, endpoints, portals, prices=()):
        client = mock.Mock()
        client.v1.prices.list.return_value = SimpleNamespace(data=list(prices))
        client.v1.products.create.side_effect = lambda params: SimpleNamespace(id=f"prod_{params['metadata']['plan']}")
        client.v1.prices.create.side_effect = lambda params: SimpleNamespace(id=f"price_{params['lookup_key']}")
        client.v1.billing_portal.configurations.list.return_value = SimpleNamespace(data=portals)
        client.v1.billing_portal.configurations.create.return_value = SimpleNamespace(id="bpc_new")
        client.v1.webhook_endpoints.list.return_value = SimpleNamespace(data=endpoints)
        client.v1.webhook_endpoints.create.return_value = SimpleNamespace(id="we_new", secret="whsec_new")
        return client

    def run_command(self, client, env_file):
        with mock.patch("apps.growth.management.commands.setup_stripe.stripe.StripeClient", return_value=client):
            call_command("setup_stripe", env_file=env_file, stdout=StringIO())

    def test_creates_only_growsterr_objects(self):
        others = [SimpleNamespace(id="we_sterr", url="https://sterragency.com/growth/stripe/webhook/")]
        portals = [stripe.StripeObject.construct_from({"id": "bpc_sterr", "metadata": {"app": "sterr-growth"}}, "sk")]
        client = self.client_mock(others, portals)
        with TemporaryDirectory() as tmp:
            env_file = Path(tmp) / ".env"
            env_file.write_text("SECRET_KEY=x\n")
            self.run_command(client, str(env_file))
            self.assertIn("STRIPE_WEBHOOK_SECRET=whsec_new", env_file.read_text())
        names = [c.kwargs["params"]["name"] for c in client.v1.products.create.call_args_list]
        self.assertEqual(names, ["Growsterr · Starter Creator", "Growsterr · Rising Influencer", "Growsterr · Pro Influencer"])
        keys = [c.kwargs["params"]["lookup_key"] for c in client.v1.prices.create.call_args_list]
        self.assertEqual(keys, ["growsterr_starter_monthly", "growsterr_rising_monthly", "growsterr_pro_monthly"])
        self.assertTrue(all(c.kwargs["params"]["metadata"]["site"] == "growsterr" for c in client.v1.prices.create.call_args_list))
        client.v1.billing_portal.configurations.update.assert_not_called()  # Sterr Agency's stays as it is
        self.assertEqual(client.v1.billing_portal.configurations.create.call_args.kwargs["params"]["metadata"]["app"], "growsterr")
        client.v1.webhook_endpoints.update.assert_not_called()
        self.assertEqual(client.v1.webhook_endpoints.create.call_args.kwargs["params"]["url"],
                         "https://growsterr.com/growth/stripe/webhook/")

    def test_updates_its_own_and_leaves_the_rest(self):
        endpoints = [SimpleNamespace(id="we_sterr", url="https://sterragency.com/growth/stripe/webhook/"),
                     SimpleNamespace(id="we_ours", url="https://growsterr.com/growth/stripe/webhook/")]
        portals = [stripe.StripeObject.construct_from({"id": "bpc_sterr", "metadata": {"app": "sterr-growth"}}, "sk"),
                   stripe.StripeObject.construct_from({"id": "bpc_ours", "metadata": {"app": "growsterr"}}, "sk")]
        prices = [SimpleNamespace(id="price_x", unit_amount=7999, recurring={"interval": "month"})]
        client = self.client_mock(endpoints, portals, prices)
        with TemporaryDirectory() as tmp:
            self.run_command(client, str(Path(tmp) / ".env"))
        self.assertEqual([c.args[0] for c in client.v1.webhook_endpoints.update.call_args_list], ["we_ours"])
        self.assertEqual([c.args[0] for c in client.v1.billing_portal.configurations.update.call_args_list], ["bpc_ours"])
        client.v1.webhook_endpoints.create.assert_not_called()
        # Only the starter price matched (7999); the other two packages get their own new prices.
        self.assertEqual(client.v1.prices.create.call_count, 2)
        for call in client.v1.prices.list.call_args_list:
            self.assertTrue(call.kwargs["params"]["lookup_keys"][0].startswith("growsterr_"))


class YouTubeVideoTests(FreshCache, TestCase):
    """The YouTube video new viewers are sent to: picked at checkout, changed in the account, sent to Linksterr."""

    def test_links_are_normalized(self):
        from .forms import clean_video_url

        want = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        for link in ("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "youtube.com/watch?feature=share&v=dQw4w9WgXcQ&t=10",
                     "https://youtu.be/dQw4w9WgXcQ?si=abc", "https://www.youtube.com/shorts/dQw4w9WgXcQ",
                     "https://m.youtube.com/watch?v=dQw4w9WgXcQ", "https://www.youtube.com/live/dQw4w9WgXcQ?feature=share"):
            self.assertEqual(clean_video_url(link), want, link)
        self.assertEqual(clean_video_url("  "), "")
        for bad in ("https://www.youtube.com/@channel", "https://vimeo.com/123", "https://youtu.be/short", "not a link"):
            self.assertIsNone(clean_video_url(bad), bad)

    @override_settings(**STRIPE_OFF)
    def test_checkout_keeps_the_video_for_youtube_only(self):
        self.client.post(reverse("growth:order"), order_data(platform="youtube", handle="mychannel",
                                                             video_url="https://youtu.be/dQw4w9WgXcQ"))
        sub = AgencySubscription.objects.get()
        self.assertEqual(sub.video_url, "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        self.client.logout()
        self.client.post(reverse("growth:order"), order_data(email="ig@example.com", video_url="https://youtu.be/dQw4w9WgXcQ"))
        self.assertEqual(AgencySubscription.objects.get(platform="instagram").video_url, "")

    @override_settings(**STRIPE_OFF)
    def test_a_bad_link_is_an_error_on_the_form(self):
        r = self.client.post(reverse("growth:order"), order_data(platform="youtube", handle="mychannel", video_url="vimeo.com/1"))
        self.assertEqual(r.status_code, 400)
        self.assertContains(r, "Paste a link to a YouTube video", status_code=400)
        self.assertFalse(AgencySubscription.objects.exists())

    @override_settings(LINKSTERR_AGENCY_TOKEN="agency-test-token")
    def test_linksterr_reads_the_video(self):
        AgencySubscription.objects.create(email="y@example.com", platform="youtube", handle="mychannel", location="x",
                                          plan="starter", amount="79.99", status="active", started_at=timezone.now(),
                                          video_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        rows = self.client.get(reverse("growth:api_subscriptions"), HTTP_AUTHORIZATION="Bearer agency-test-token").json()
        row = next(r for r in (rows.get("subscriptions") or rows.get("results") or rows) if r["platform"] == "youtube")
        self.assertEqual(row["video_url"], "https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    def test_the_customer_changes_it_and_linksterr_hears_at_once(self):
        user = get_user_model().objects.create_user("yt@example.com", "yt@example.com", "pass-word-1")
        sub = AgencySubscription.objects.create(user=user, email=user.email, platform="youtube", handle="mychannel",
                                                location="x", plan="starter", amount="79.99", status="active",
                                                started_at=timezone.now())
        self.client.force_login(user)
        url = reverse("growth:video", args=[sub.pk])
        with mock.patch("apps.growth.linksterr.ping_soon") as ping, self.captureOnCommitCallbacks(execute=True):
            r = self.client.post(url, {"lang": "en", "video_url": "youtu.be/dQw4w9WgXcQ"})
        self.assertIn("video=saved", r["Location"])
        sub.refresh_from_db()
        self.assertEqual(sub.video_url, "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        ping.assert_called_once()
        r = self.client.post(url, {"lang": "en", "video_url": "nope"})
        self.assertIn("video=invalid", r["Location"])
        html = self.client.get(r["Location"]).content.decode()
        self.assertIn("Paste a link to a YouTube video", html)
        # Clearing a video they had set tells Linksterr "channel"; the box shows empty again.
        self.client.post(url, {"lang": "en", "video_url": ""})
        sub.refresh_from_db()
        self.assertEqual(sub.video_url, "channel")
        self.assertNotIn('value="channel"', self.client.get(reverse("growth:account") + "?lang=en").content.decode())
        self.client.post(url, {"lang": "en", "video_url": "youtu.be/dQw4w9WgXcQ"})
        other = get_user_model().objects.create_user("x@example.com", "x@example.com", "pass-word-1")
        self.client.force_login(other)
        self.client.post(url, {"lang": "en", "video_url": ""})
        sub.refresh_from_db()
        self.assertEqual(sub.video_url, "https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # not their subscription
