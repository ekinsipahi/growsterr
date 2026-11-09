"""JSON-LD for the money pages: built as Python data, dumped safely into <script> tags.
No ratings, no reviews: we never publish any."""
import json

from django.utils.encoding import iri_to_uri
from django.utils.safestring import mark_safe

CONTEXT = "https://schema.org"
BRAND = "Growsterr"


def dump(data):
    """JSON that can't close its <script> tag early."""
    text = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    return mark_safe(text.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026"))


def breadcrumbs(crumbs, site):
    """crumbs: [(label, path)], home first, this page last."""
    return {
        "@context": CONTEXT,
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": position, "name": label, "item": site + iri_to_uri(path)}
            for position, (label, path) in enumerate(crumbs, 1)
        ],
    }


def faq(faqs):
    return {
        "@context": CONTEXT,
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": question, "acceptedAnswer": {"@type": "Answer", "text": answer}}
            for question, answer in faqs
        ],
    }


def article(headline, description, url, modified=None, image=""):
    """A guide: Article, published by Growsterr."""
    data = {
        "@context": CONTEXT,
        "@type": "Article",
        "headline": headline,
        "description": description,
        "url": url,
        "mainEntityOfPage": url,
        "author": [{"@type": "Organization", "name": BRAND},
                   {"@type": "Organization", "name": "Sterr Agency", "url": "https://sterragency.com"}],
        "publisher": {"@type": "Organization", "name": BRAND,
                      "founder": {"@type": "Person", "name": "Ekin Sipahi",
                                  "sameAs": ["https://www.instagram.com/dt.ekinsipahi/"]},
                      "parentOrganization": {"@type": "Organization", "name": "Sterr Agency", "url": "https://sterragency.com"}},
    }
    if modified:
        data["dateModified"] = modified.isoformat()
    if image:
        data["image"] = [image]
    return data


def product(name, description, url, offers, image=""):
    """offers: [{"name", "price" ("79.99"), "url"}]: the monthly packages."""
    data = {
        "@context": CONTEXT,
        "@type": "Product",
        "name": name,
        "description": description,
        "brand": {"@type": "Brand", "name": BRAND},
        "url": url,
        "offers": [
            {
                "@type": "Offer",
                "name": offer["name"],
                "price": offer["price"],
                "priceCurrency": "USD",
                "availability": "https://schema.org/InStock",
                "url": offer["url"],
                "priceSpecification": {
                    "@type": "UnitPriceSpecification",
                    "price": offer["price"],
                    "priceCurrency": "USD",
                    "referenceQuantity": {"@type": "QuantitativeValue", "value": 1, "unitCode": "MON"},
                },
            }
            for offer in offers
        ],
    }
    if image:
        data["image"] = [image]
    return data
