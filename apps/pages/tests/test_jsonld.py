"""JSON-LD: valid JSON, the right types, real prices, never ratings or reviews."""
import json

from django.test import TestCase

from apps.growth import plan
from apps.pages import jsonld

from .helpers import jsonld as blocks_of
from .test_routing import ENGLISH


class JsonLdTests(TestCase):
    def test_every_page_has_valid_breadcrumbs_service_and_faq(self):
        prices = sorted(f"{p['price']:.2f}" for p in plan.PLANS)
        for url in ENGLISH:
            with self.subTest(url=url):
                html = self.client.get(url).content.decode()
                blocks = blocks_of(html)  # json.loads on each: invalid JSON fails here
                by_type = {block.get("@type"): block for block in blocks}
                self.assertLessEqual({"BreadcrumbList", "FAQPage", "Service"}, set(by_type))
                self.assertNotIn("Product", by_type)  # a subscription service, not a merchant listing
                for block in (by_type["BreadcrumbList"], by_type["FAQPage"], by_type["Service"]):
                    self.assertEqual(block["@context"], "https://schema.org")
                    text = json.dumps(block).lower()
                    for banned in ("aggregaterating", "review", "ratingvalue"):
                        self.assertNotIn(banned, text)

                crumbs = by_type["BreadcrumbList"]["itemListElement"]
                self.assertEqual([c["position"] for c in crumbs], list(range(1, len(crumbs) + 1)))
                self.assertEqual(crumbs[0]["item"], "https://growsterr.com/")
                self.assertEqual(crumbs[-1]["item"], "https://growsterr.com" + url)

                product = by_type["Service"]
                self.assertEqual(product["url"], "https://growsterr.com" + url)
                self.assertEqual(product["provider"]["name"], "Growsterr")
                self.assertEqual(product["provider"]["parentOrganization"]["name"], "Sterr Agency")
                self.assertEqual(sorted(o["price"] for o in product["offers"]), prices)
                for offer in product["offers"]:
                    self.assertEqual(offer["priceCurrency"], "USD")
                    self.assertTrue(offer["url"].startswith("https://growsterr.com/order/?plan="))
                    self.assertEqual(offer["priceSpecification"]["referenceQuantity"]["unitCode"], "MON")
                self.assertNotIn("image", product)  # images are pending: no placeholder URLs

                questions = by_type["FAQPage"]["mainEntity"]
                self.assertGreaterEqual(len(questions), 3)
                self.assertEqual(html.count('class="faq__item"'), len(questions))
                for q in questions:
                    self.assertTrue(q["name"] and q["acceptedAnswer"]["text"])
                    self.assertNotRegex(q["name"] + q["acceptedAnswer"]["text"], r"\{[a-z_]+\}")

    def test_product_name_and_description_follow_the_page(self):
        html = self.client.get("/youtube/subscribers/").content.decode()
        product = next(b for b in blocks_of(html) if b["@type"] == "Service")
        self.assertEqual(product["name"], "YouTube growth packages")
        self.assertTrue(product["description"].startswith("Buy YouTube subscribers who are real people"))

    def test_dump_cannot_close_the_script_tag(self):
        text = jsonld.dump(jsonld.faq([("</script><script>alert(1)</script>", "a & b <b>")]))
        self.assertNotIn("<", text)
        self.assertNotIn(">", text)
        self.assertEqual(json.loads(text)["mainEntity"][0]["name"], "</script><script>alert(1)</script>")
