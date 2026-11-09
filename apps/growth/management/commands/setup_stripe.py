"""Stripe setup for Growsterr's monthly growth packages. Safe to run again.

The Stripe account is shared with Sterr Agency, Linksterr and other sites, so this touches
only Growsterr's own objects:

- One product ("Growsterr · <package>") + one monthly USD price per package (3 in all; the
  platform is chosen at checkout and kept in the subscription's metadata), found again by
  the lookup key `growsterr_<package>_monthly`. A changed amount in plan.py gets a new price
  and the lookup key moves to it (transfer_lookup_key: only ever our own growsterr_* keys).
- Growsterr's customer portal configuration (card, invoices, cancel at period end), tagged
  metadata.app = growsterr so billing.portal_url finds it. Other configurations are never
  read for changes or updated.
- Growsterr's webhook endpoint ({SITE_URL}/growth/stripe/webhook/): created, or its events
  updated. Endpoints with any other URL are never touched. A new endpoint's signing secret
  is written to .env (STRIPE_WEBHOOK_SECRET), never printed.

    python manage.py setup_stripe
"""
import re
from pathlib import Path

import stripe
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from apps.growth import plan
from apps.growth.billing import PORTAL_TAG, SITE_TAG, lookup_key, metadata, product_name

WEBHOOK_PATH = "/growth/stripe/webhook/"
WEBHOOK_DESCRIPTION = "Growsterr growth packages"
WEBHOOK_EVENTS = [
    "checkout.session.completed",
    "checkout.session.async_payment_succeeded",
    "invoice.paid",
    "invoice.payment_failed",
    "invoice.upcoming",
    "customer.subscription.updated",
    "customer.subscription.deleted",
    "charge.dispute.created",
    "charge.dispute.closed",
]


class Command(BaseCommand):
    help = "Create Growsterr's package products/prices, its customer portal configuration and its webhook in Stripe."

    def add_arguments(self, parser):
        parser.add_argument("--site-url", default=settings.SITE_URL, help="Public origin for the webhook URL.")
        parser.add_argument("--env-file", default=str(Path(settings.BASE_DIR) / ".env"))

    def handle(self, *args, **opts):
        if not settings.STRIPE_SECRET_KEY:
            raise CommandError("STRIPE_SECRET_KEY is not set.")
        client = stripe.StripeClient(settings.STRIPE_SECRET_KEY)
        site = opts["site_url"].rstrip("/")

        for package in plan.PLANS:
            key = lookup_key(package["key"])
            existing = client.v1.prices.list(params={"lookup_keys": [key], "active": True, "limit": 1}).data
            if existing and existing[0].unit_amount == plan.cents(package) and existing[0].recurring:
                self.stdout.write(f"Price exists: {key} ({existing[0].id})")
                continue
            low, high = package["followers"]
            product = client.v1.products.create(params={
                "name": product_name(package["key"]),
                "description": (f"Monthly growth package for Instagram, TikTok or YouTube, spread over 30 days: real "
                                f"people who follow or subscribe, like, watch and comment (typically {low:,}-{high:,} "
                                f"new followers or subscribers a month). No bots, no password."),
                "metadata": {"site": SITE_TAG, "plan": package["key"]},
                # The account is shared: without this the card statement shows another brand's
                # name, the usual cause of "I don't recognise this charge" disputes.
                "statement_descriptor": "GROWSTERR",
            })
            price = client.v1.prices.create(params={
                "product": product.id, "currency": "usd", "unit_amount": plan.cents(package),
                "recurring": {"interval": "month"}, "lookup_key": key, "transfer_lookup_key": True,
                "metadata": {"site": SITE_TAG, "plan": package["key"]},
            })
            self.stdout.write(f"Created {key}: ${package['price']} / month ({price.id})")

        portal = {
            "business_profile": {"headline": "Growsterr: manage your growth package",
                                 "privacy_policy_url": f"{site}/privacy/", "terms_of_service_url": f"{site}/terms/"},
            "features": {
                "customer_update": {"enabled": True, "allowed_updates": ["email", "address"]},
                "invoice_history": {"enabled": True},
                "payment_method_update": {"enabled": True},
                "subscription_cancel": {"enabled": True, "mode": "at_period_end",
                                        "cancellation_reason": {"enabled": True, "options": [
                                            "too_expensive", "unused", "switched_service", "other"]}},
            },
            "metadata": {"app": PORTAL_TAG, "site": SITE_TAG},
        }
        found = [c for c in client.v1.billing_portal.configurations.list(params={"active": True, "limit": 100}).data
                 if metadata(c).get("app") == PORTAL_TAG]
        if found:
            client.v1.billing_portal.configurations.update(found[0].id, params=portal)
            self.stdout.write(f"Portal configuration {found[0].id}: updated")
        else:
            conf = client.v1.billing_portal.configurations.create(params=portal)
            self.stdout.write(f"Created portal configuration {conf.id}")

        url = f"{site}{WEBHOOK_PATH}"
        endpoints = [w for w in client.v1.webhook_endpoints.list(params={"limit": 100}).data if w.url == url]
        if endpoints:
            client.v1.webhook_endpoints.update(endpoints[0].id, params={"enabled_events": WEBHOOK_EVENTS,
                                                                        "description": WEBHOOK_DESCRIPTION})
            self.stdout.write(f"Webhook {endpoints[0].id}: events updated ({', '.join(WEBHOOK_EVENTS)})")
            return
        endpoint = client.v1.webhook_endpoints.create(params={"url": url, "enabled_events": WEBHOOK_EVENTS,
                                                              "description": WEBHOOK_DESCRIPTION,
                                                              "metadata": {"site": SITE_TAG}})
        self._write_env(opts["env_file"], "STRIPE_WEBHOOK_SECRET", endpoint.secret)
        self.stdout.write(f"Created webhook {endpoint.id} → {url}; its secret is in {opts['env_file']} "
                          "(copy STRIPE_WEBHOOK_SECRET to Render → Environment)")

    def _write_env(self, path, name, value):
        env = Path(path)
        text = env.read_text(encoding="utf-8") if env.exists() else ""
        line = f"{name}={value}"
        text = re.sub(rf"^{name}=.*$", line, text, flags=re.M) if re.search(rf"^{name}=", text, re.M) else text.rstrip("\n") + f"\n{line}\n"
        env.write_text(text, encoding="utf-8")
