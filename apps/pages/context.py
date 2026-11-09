"""Everything a page template needs: the content with its placeholders filled from the
packages, the package the page preselects, images, the quantity pace, breadcrumbs, related
pages and JSON-LD. resolve_page() needs no request, so check_pages checks exactly what
visitors see; build() adds the rest of the template context.
"""
import math
import re
from functools import lru_cache
from types import SimpleNamespace
from urllib.parse import urlencode

from django.conf import settings
from django.contrib.staticfiles import finders
from django.templatetags.static import static
from django.urls import Resolver404, resolve, reverse
from django.utils import formats, translation
from django.utils.encoding import iri_to_uri

from apps.core.languages import DEFAULT, LANG_BY_CODE

from . import dimensions as dims
from . import jsonld
from .images import IMAGES

PLACEHOLDER = re.compile(r"\{([a-z0-9_]+)\}")
PLAN_FIELDS = ("name", "price", "audience", "likes", "comments")
BASIC_NAMES = ("platform", "audience", "follow", "profile", "handle", "content", "service", "service_name", "quantity")
# Filled inside the UI by the pace builder (and by the tools, in the browser), not per page.
PACE_NAMES = ("n", "low", "high", "range", "rate")
INCLUDED_ORDER = ("audience", "likes", "comments", "views", "days", "dashboard")
# Icons of the design system ({% icon %}, templates/partials/icon.html) for each block.
ICONS = {"audience": "user-plus", "likes": "heart", "comments": "comment", "views": "eye", "days": "calendar",
         "dashboard": "chart", "check": "check"}
PACE_MONTHS = (3, 6)  # the pace chart shows at least / at most this many months


# --- Placeholders -------------------------------------------------------------------------
def count(n, lang):
    """1000 -> '1,000' / '1.000' / '1 000' in the page language."""
    with translation.override("nb" if lang == "no" else lang):
        return formats.number_format(n, use_l10n=True, force_grouping=True)


def span(low, high, lang):
    return f"{count(low, lang)}–{count(high, lang)}"


def fill(value, values):
    """Replace {name} placeholders in every string of a nested value; unknown ones stay as they are."""
    if isinstance(value, str):
        return PLACEHOLDER.sub(lambda m: str(values[m.group(1)]) if m.group(1) in values else m.group(0), value)
    if isinstance(value, dict):
        return {key: fill(item, values) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return type(value)(fill(item, values) for item in value)
    return value


def strings(value):
    """Every string inside a nested value (for the checks)."""
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for item in value.values():
            yield from strings(item)
    elif isinstance(value, (list, tuple)):
        for item in value:
            yield from strings(item)


def known_names(plan_keys):
    """Every placeholder name a content file or a UI may use."""
    names = set(BASIC_NAMES) | set(PACE_NAMES) | {"from_price"}
    for key in [*plan_keys, "pick"]:
        names |= {f"{key}_{field}" for field in PLAN_FIELDS}
    return names


def _word(ui, table, key):
    words = ui.get(table)
    return words.get(key, "") if isinstance(words, dict) else ""


def basic_values(page, ui):
    """The placeholders any string of a page may use, its link label included."""
    v = page.variant
    values = {"platform": dims.PLATFORM_NAMES[v.platform]}
    for name in ("audience", "follow", "profile", "handle", "content"):
        values[name] = _word(ui, name, v.platform)
    if v.service:
        values["service"] = _word(ui, "service_words", v.service)
        values["service_name"] = _word(ui, "service_names", v.service)
    if v.quantity:
        values["quantity"] = count(v.quantity, page.lang)
    return values


def _plan_fields(raw, shown, lang):
    """A package's placeholders: its name and price as the cards show them, its typical monthly
    ranges from apps.growth.plan.PLANS (formatted for the page language)."""
    def typical(metric):
        value = raw.get(metric)
        if isinstance(value, (list, tuple)) and len(value) == 2:
            return span(value[0], value[1], lang)
        return shown.get(metric, "") if isinstance(shown.get(metric), str) else ""

    audience = "subscribers" if "subscribers" in raw else "followers"
    return {"name": shown["name"], "price": shown["amount"], "audience": typical(audience),
            "likes": typical("likes"), "comments": typical("comments")}


def plan_values(plans, pick_key, plans_raw, lang):
    shown = {p["key"]: p for p in plans}
    values = {}
    for raw in plans_raw:
        fields = _plan_fields(raw, shown[raw["key"]], lang)
        values.update({f"{raw['key']}_{name}": value for name, value in fields.items()})
        if raw["key"] == pick_key:
            values.update({f"pick_{name}": value for name, value in fields.items()})
    cheapest = min(plans_raw, key=lambda p: p["price"])["key"]
    values["from_price"] = shown[cheapest]["amount"]
    return values


# --- The package a page preselects --------------------------------------------------------
def metric_for(service, plans_raw):
    """The package figure a quantity of this service is counted in; None without a typical ratio (views)."""
    if not service:
        return None
    metric = dims.METRIC.get(dims.family(service))
    if metric == "followers" and service == "subscribers" and all("subscribers" in p for p in plans_raw):
        metric = "subscribers"
    return metric if metric and all(metric in p for p in plans_raw) else None


def choose_plan(page, plans_raw, default=None):
    """The page's "plan", else for a quantity the smallest package whose typical month reaches
    it (the middle of its range), else the default (most popular) package."""
    keys = [p["key"] for p in plans_raw]
    if page.data.get("plan") in keys:
        return page.data["plan"]
    metric = metric_for(page.variant.service, plans_raw)
    if page.variant.quantity and metric:
        ordered = sorted(plans_raw, key=lambda p: p["price"])
        for p in ordered:
            low, high = p[metric]
            if (low + high) / 2 >= page.variant.quantity:
                return p["key"]
        return ordered[-1]["key"]
    if default in keys:
        return default
    return next((p["key"] for p in plans_raw if p.get("popular")), keys[0])


def resolve_page(page, registry):
    """The page's content and UI with every placeholder filled, and its packages. No request."""
    from apps.growth import plan as growth_plan
    from apps.growth.content import ui_for as growth_ui

    raw_ui = registry.ui_for(page.lang)
    gu = growth_ui(page.lang, page.variant.platform)
    plans = growth_plan.for_page(page.lang, gu)
    plans_raw = list(growth_plan.PLANS)
    pick_key = choose_plan(page, plans_raw, getattr(growth_plan, "DEFAULT_PLAN", None))
    pick = next(p for p in plans if p["key"] == pick_key)
    values = {**basic_values(page, raw_ui), **plan_values(plans, pick_key, plans_raw, page.lang)}
    return SimpleNamespace(page=page, lang=page.lang, ui=fill(raw_ui, values), p=fill(page.data, values),
                           values=values, gu=gu, plans=plans, plans_raw=plans_raw, pick=pick)


def label(page, registry):
    """A page's link text, as other pages show it."""
    return fill(page.data.get("label") or page.slug, basic_values(page, registry.ui_for(page.lang)))


# --- Building blocks ------------------------------------------------------------------------
@lru_cache(maxsize=None)
def _found(src):
    return finders.find(src) is not None


def image_exists(src):
    """Whether the image file is in static/ (cached in production; DEBUG sees new files at once)."""
    return finders.find(src) is not None if settings.DEBUG else _found(src)


def image(ref, uid, eager=False):
    """An image slot: the file when it exists, else a placeholder drawing in the same shape."""
    if not isinstance(ref, dict):
        return None
    spec = IMAGES.get(ref.get("image"))
    if spec is None:
        return None
    return {"url": static(spec["src"]) if image_exists(spec["src"]) else "", "alt": ref.get("alt", ""),
            "width": spec["width"], "height": spec["height"], "art": spec.get("art") or "growth",
            "uid": uid, "eager": eager}


def headline(value):
    """h1 is "text" or ("text", "highlighted text")."""
    if isinstance(value, (list, tuple)):
        parts = [str(part) for part in value][:2]
        return tuple(parts + [""] * (2 - len(parts)))
    return (str(value or ""), "")


def faq_list(value):
    return [(q, a) for item in value or [] if isinstance(item, (list, tuple)) and len(item) == 2
            for q, a in [item] if q and a]


def sections(r):
    out = []
    for number, section in enumerate(r.p.get("sections") or [], 1):
        if not isinstance(section, dict):
            continue
        paragraphs = section.get("p") or []
        out.append({"h2": section.get("h2", ""), "p": [paragraphs] if isinstance(paragraphs, str) else paragraphs,
                    "ul": section.get("ul") or [], "image": image(section.get("image"), f"s{number}")})
    return out


def included(r):
    custom = r.p.get("included")
    if custom:
        return [{"icon": ICONS["check"], "title": title, "text": text} for title, text in custom]
    items = r.ui.get("included_items") or {}
    service = r.page.variant.service
    first = dims.family(service) if service else "audience"
    order = [first] + [key for key in INCLUDED_ORDER if key != first]
    return [{"icon": ICONS[key], "title": items[key][0], "text": items[key][1]} for key in order if key in items]


def _pct(value, top):
    return f"{min(value / top * 100, 100):.2f}%"


def pace(r):
    """Quantity pages: how a monthly package gets there, month by month (typical ranges)."""
    q = r.page.variant.quantity
    if not q:
        return None
    ui, lang = r.ui, r.lang
    out = {"title": ui.get("quantity_title", ""), "lead": ui.get("quantity_lead", ""),
           "text": r.p.get("quantity_text", ""), "note": ui.get("pace_note", "")}
    metric = metric_for(r.page.variant.service, r.plans_raw)
    if metric is None:
        out["fallback"] = ui.get("views_pace", "")
        return out
    shown = {p["key"]: p for p in r.plans}
    by_plan = []
    for raw in r.plans_raw:
        low, high = raw[metric]
        fast, slow = max(math.ceil(q / high), 1), max(math.ceil(q / low), 1)
        if slow == 1:
            when = ui.get("when_first", "")
        elif fast == slow:
            when = fill(ui.get("when_about", ""), {"n": count(slow, lang)})
        else:
            when = fill(ui.get("when_range", ""), {"low": count(fast, lang), "high": count(slow, lang)})
        by_plan.append({"name": shown[raw["key"]]["name"], "amount": shown[raw["key"]]["amount"],
                        "range": fill(ui.get("a_month", "{range}"), {"range": span(low, high, lang)}),
                        "when": when, "pick": raw["key"] == r.pick["key"]})
    low, high = next(p for p in r.plans_raw if p["key"] == r.pick["key"])[metric]
    months = min(max(math.ceil(q / low), PACE_MONTHS[0]), PACE_MONTHS[1])
    top = max(high * months, q)
    out.update({
        "pace_title": ui.get("pace_title", ""), "by_plan_title": ui.get("by_plan_title", ""),
        "goal": _pct(q, top), "goal_label": ui.get("pace_goal", ""), "by_plan": by_plan,
        "rows": [{"label": fill(ui.get("pace_month", "{n}"), {"n": count(m, lang)}), "range": span(low * m, high * m, lang),
                  "start": _pct(low * m, top), "end": _pct(high * m, top), "reached": low * m >= q}
                 for m in range(1, months + 1)],
    })
    return out


def home_path(lang):
    """The home page of a language: /<code>/ once the site has it, else /."""
    if lang == DEFAULT:
        return "/"
    try:
        resolve(f"/{lang}/")
    except Resolver404:
        return "/"
    return f"/{lang}/"


def order_url(plan_key, platform, lang):
    return f"{reverse('growth:order')}?{urlencode({'plan': plan_key, 'platform': platform, 'lang': lang})}"


def breadcrumbs(page, registry, ui):
    """[(label, path)]: home, the hub, the service page, this page."""
    return ([(ui.get("home", "Home"), home_path(page.lang))]
            + [(label(above, registry), above.path) for above in registry.ancestors(page)]
            + [(label(page, registry), page.path)])


def related(page, registry, ui):
    titles = {**(ui.get("related") or {}), "answers": (ui.get("article_eyebrows") or {}).get("intent", "")}
    return [{"title": titles.get(group, ""), "name": group,
             "links": [{"label": label(p, registry), "url": p.path, "platform": p.variant.platform} for p in pages]}
            for group, pages in registry.related(page)]


def hub_services(r, registry):
    out = []
    for service, base, children in registry.tree(r.page):
        family = dims.family(service)
        out.append({"service": service, "icon": ICONS[family], "name": _word(r.ui, "service_names", service),
                    "teaser": _word(r.ui, "teasers", family),
                    "url": base.path if base else "", "label": label(base, registry) if base else "",
                    "children": [{"label": label(child, registry), "url": child.path} for child in children]})
    return out


def tool_plans(r):
    """For the growth calculator: each package's typical monthly range of new followers."""
    shown = {p["key"]: p for p in r.plans}
    return [{"name": shown[raw["key"]]["name"], "low": raw["followers"][0], "high": raw["followers"][1],
             "url": order_url(raw["key"], r.page.variant.platform, r.lang)} for raw in r.plans_raw]


def founder():
    from apps.core.company import COMPANY

    handle = COMPANY["founder_instagram"]
    return {"name": f"Dt. {COMPANY['founder']}", "handle": handle, "url": f"https://www.instagram.com/{handle}/"}


def updated(page):
    """The page's last real change, in its language's date format."""
    if not page.lastmod:
        return None
    with translation.override(LANG_BY_CODE[page.lang].django):
        return {"iso": page.lastmod.isoformat(), "text": formats.date_format(page.lastmod, "DATE_FORMAT")}


def eyebrow(r, kind):
    v = r.page.variant
    if v.article:
        return (r.ui.get("article_eyebrows") or {}).get(kind, "")
    return r.ui.get("eyebrow_hub" if v.is_hub else "eyebrow", "")


def build(request, page, registry):
    r = resolve_page(page, registry)
    v = page.variant
    site = settings.SITE_URL
    canonical = site + iri_to_uri(page.path)
    hero = image(r.p.get("hero"), "hero", eager=True)
    crumbs = breadcrumbs(page, registry, r.ui)
    faqs = faq_list(r.p.get("faqs"))
    prices = {p["key"]: f"{p['price']:.2f}" for p in r.plans_raw}
    offers = [{"name": p["name"], "price": prices[p["key"]], "url": site + order_url(p["key"], v.platform, page.lang)}
              for p in r.plans]
    kind = page.data.get("kind", "") if v.article else ""
    image_url = site + hero["url"] if hero and hero["url"] else ""
    if kind == "guide":
        main = jsonld.article("".join(headline(r.p.get("h1"))), r.p.get("description", ""), canonical,
                              page.lastmod, image=image_url)
    else:
        main = jsonld.service(r.ui.get("product_name", ""), r.p.get("description", ""), canonical, offers, site, image=image_url)
    blocks = [jsonld.breadcrumbs(crumbs, site), main]
    if faqs:
        blocks.append(jsonld.faq(faqs))
    ctx = {
        "page": page, "p": r.p, "pu": r.ui, "gu": r.gu, "plans": r.plans, "pick": r.pick,
        "platform": v.platform, "lang": page.lang, "rtl": LANG_BY_CODE[page.lang].rtl, "is_hub": v.is_hub,
        "nav_active": v.platform, "og_locale": LANG_BY_CODE[page.lang].og_locale,
        "alternates": registry.alternates(page), "lang_links": registry.lang_links(page), "canonical_url": canonical,
        "h1": headline(r.p.get("h1")), "eyebrow": eyebrow(r, kind),
        "kind": kind, "tool": r.p.get("tool", ""), "tool_plans": tool_plans(r),
        "founder": founder(), "updated": updated(page),
        "hero": hero, "sections": sections(r), "included": included(r),
        "steps": r.p.get("steps") or r.ui.get("steps") or [],
        "compare": {"caption": r.ui.get("compare_title", ""), "cols": r.ui.get("compare_cols", ("", "", "")),
                    "rows": r.p.get("compare") or r.ui.get("compare") or []},
        "quantity": pace(r), "faqs": faqs, "crumbs": crumbs, "related": related(page, registry, r.ui),
        "order_url": order_url(r.pick["key"], v.platform, page.lang),
        "jsonld": [jsonld.dump(block) for block in blocks],
    }
    if v.is_hub:
        ctx["services"] = hub_services(r, registry)
        ctx["goals"] = [{"title": s["name"], "links": s["children"]} for s in ctx["services"] if s["children"]]
        ctx["other_hubs"] = [{"label": label(hub, registry), "url": hub.path, "platform": hub.variant.platform}
                             for hub in registry.hubs(page.lang) if hub is not page]
    return ctx
