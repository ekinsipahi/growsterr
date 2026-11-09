"""The keyword plan against the content: which planned pages exist, and whether each page
carries its keywords (the "buy" and "get" intents above all).

    python manage.py check_keywords              # summary per content file + problems
    python manage.py check_keywords --write      # also writes docs/keywords/STATUS.md

The plan is docs/keywords/page-plan.csv (one row per English page)."""
import csv
import re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from apps.pages import context as page_context
from apps.pages.archive import ARCHIVED
from apps.pages.registry import REGISTRY, Variant

STOP = {"buy", "get", "the", "a", "an", "for", "on", "in", "of", "to", "with", "and", "my", "your", "com", "now", "online",
        "real", "is", "how", "do", "you", "can", "that", "it", "by", "at", "from", "are", "does", "what", "which"}


def words(text):
    return re.findall(r"[a-z0-9$€]+", text.lower())


def page_text(page):
    r = page_context.resolve_page(page, REGISTRY)
    return " ".join(page_context.strings(r.p)).lower()


def find(row):
    if row["article"]:
        return next((p for p in REGISTRY.pages_in("en") if p.variant.article == row["article"]), None)
    return REGISTRY.get("en", Variant(row["platform"], row["service"], int(row["quantity"] or 0), row["modifier"], row["country"]))


def covered(keyword, text, vocabulary):
    """A keyword counts when most of its meaningful words are on the page."""
    needed = [w for w in words(keyword) if w not in STOP]
    if not needed:
        return True
    return sum(1 for w in needed if w in vocabulary or w.rstrip("s") in vocabulary) / len(needed) >= 0.75


class Command(BaseCommand):
    help = "Planned pages vs content: missing pages and keyword coverage (buy/get intents)."

    def add_arguments(self, parser):
        parser.add_argument("--write", action="store_true", help="write docs/keywords/STATUS.md")

    def handle(self, *args, **opts):
        plan = Path(settings.BASE_DIR) / "docs" / "keywords" / "page-plan.csv"
        with open(plan, encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        by_file = defaultdict(Counter)
        missing, weak, no_buy = [], [], []
        archived = 0
        for row in rows:
            name = row["file"]
            if row["page"] in ARCHIVED:
                by_file[name]["archived"] += 1
                archived += 1
                continue
            page = find(row)
            if page is None:
                by_file[name]["missing"] += 1
                missing.append(row)
                continue
            by_file[name]["done"] += 1
            text = page_text(page)
            vocabulary = set(words(text))
            keywords = [k.strip() for k in row["keywords"].split("|") if k.strip()]
            hits = sum(1 for k in keywords if covered(k, text, vocabulary))
            if keywords and hits / len(keywords) < 0.6:
                weak.append((row["page"], hits, len(keywords)))
            head = " ".join(page_context.strings([page.data.get("title", ""), page.data.get("h1", ""), page.data.get("intro", "")])).lower()
            forms = {"buy": {"buy", "buying"}, "get": {"get", "getting"}}
            for verb in ("buy", "get"):
                if any(k.startswith(verb + " ") for k in keywords) and not forms[verb] & set(words(text)):
                    no_buy.append((row["page"], verb, "nowhere on the page"))
                elif any(k.startswith(verb + " ") for k in keywords) and verb == "buy" and not forms["buy"] & set(words(head)):
                    no_buy.append((row["page"], verb, "not in title, h1 or intro"))

        total_done = sum(c["done"] for c in by_file.values())
        lines = [f"# pSEO status ({date.today().isoformat()})", "",
                 f"English pages from docs/keywords/page-plan.csv: **{total_done} live**, {archived} archived as thin "
                 f"(apps/pages/archive.py), {len(missing)} missing.", "", "| Content file | Live | Archived | Missing |",
                 "|---|---|---|---|"]
        for name in sorted(by_file):
            c = by_file[name]
            lines.append(f"| `{name}` | {c['done']} | {c['archived']} | {c['missing']} |")
        if missing:
            lines += ["", "## Missing pages", ""] + [f"- `{r['page']}` → `{r['file']}`: {r['primary_keyword']}" for r in missing]
        if weak:
            lines += ["", "## Pages that carry few of their keywords (under 60%)", ""] + \
                     [f"- `{p}`: {h} of {n}" for p, h, n in weak]
        if no_buy:
            lines += ["", "## Buy / get intents not visible", ""] + [f"- `{p}`: \"{v}\" {why}" for p, v, why in no_buy]
        lines += ["", "Translations: every page above exists in English only unless apps/pages/content/<lang>/ has it "
                  "(python manage.py check_pages prints pages per language)."]
        report = "\n".join(lines) + "\n"
        self.stdout.write(report)
        if opts["write"]:
            out = Path(settings.BASE_DIR) / "docs" / "keywords" / "STATUS.md"
            out.write_text(report, encoding="utf-8")
            self.stdout.write(f"written: {out}")
