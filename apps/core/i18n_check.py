"""Checks one language's core file (apps/core/i18n/<code>.py) against the English source:
what it is missing (keys English has and it doesn't: they show in English) and what is wrong
(a different shape, a lost or unknown placeholder, an unknown key or name, a forbidden word).
Used by `manage.py check_i18n` and the tests. Imports only the file it checks, so a broken
translation elsewhere can't get in the way."""
import re
import sys
from dataclasses import dataclass, field
from datetime import date
from importlib import import_module
from importlib.util import find_spec

from . import i18n

PLACEHOLDER = re.compile(r"\{[a-z_]+\}")
# Texts that are the same in every language (brands, handles, pure placeholders): never "untranslated".
SAME_EVERYWHERE = re.compile(r"Growsterr|Sterr Agency|Sterr Technologies OÜ|Instagram|TikTok|YouTube|WhatsApp|Stripe|"
                             r"Apple Pay|Google Pay|Ekin Sipahi|Starter Creator|Rising Influencer|Pro Influencer|"
                             r"linksterr\.com|dentaltourism\.tr|@\w+|\{[a-z_]+\}|[\W\d_]+")
NAMES = (*i18n.SECTIONS, "UPDATED")


@dataclass
class Report:
    code: str
    exists: bool = False
    missing: list = field(default_factory=list)    # where: a key, or a whole section, English shows
    problems: list = field(default_factory=list)   # what must be fixed
    same: list = field(default_factory=list)       # texts identical to English (maybe untranslated)

    @property
    def ok(self):
        return self.exists and not self.missing and not self.problems


def has_file(code):
    name = i18n.module_name(code)
    return name in sys.modules or find_spec(name) is not None


def _where(section, keys):
    return section + "".join(f"[{k!r}]" for k in keys)


def _forbidden(text, code):
    try:
        from apps.pages.checks import forbidden_in
    except Exception:  # noqa: BLE001 - the page engine is someone else's; skip the word check without it
        return []
    # Irish "seo" means "this"; only the upper-case acronym is the search-engine word there.
    return [word for rule, word in forbidden_in(text, code) if not (code == "ga" and rule == "SEO" and word == "seo")]


def _compare(report, section, keys, ref, value):
    where = _where(section, keys)
    if isinstance(ref, dict):
        if not isinstance(value, dict):
            report.problems.append(f"{where}: must be a dict like English (keys {sorted(ref)})")
            return
        for key in ref:
            if key not in value:
                report.missing.append(_where(section, (*keys, key)))
            else:
                _compare(report, section, (*keys, key), ref[key], value[key])
        for key in value:
            if key not in ref:
                report.problems.append(f"{_where(section, (*keys, key))}: unknown key (not in English)")
        return
    if i18n.shape(value) != i18n.shape(ref):
        report.problems.append(f"{where}: shape differs from English ({_describe(value)} instead of {_describe(ref)}); English shows")
        return
    for n, (ref_text, text) in enumerate(_pairs(ref, value)):
        at = where if isinstance(ref, str) else f"{where} item {n + 1}"
        wanted, found = set(PLACEHOLDER.findall(ref_text)), set(PLACEHOLDER.findall(text))
        for ph in sorted(wanted - found):
            report.problems.append(f"{at}: lost placeholder {ph}")
        for ph in sorted(found - wanted):
            report.problems.append(f"{at}: unknown placeholder {ph} (English has {sorted(wanted) or 'none'})")
        for word in _forbidden(text, report.code):
            report.problems.append(f"{at}: forbidden word {word!r} (docs/I18N.md, copy rules)")
        if report.code != i18n.DEFAULT and text == ref_text and SAME_EVERYWHERE.sub("", text).strip():
            report.same.append(f"{at}: {text[:70]!r}")


def _pairs(ref, value):
    """(English text, translated text) pairs of one value, matched by position."""
    if isinstance(ref, str):
        return [(ref, value)]
    if isinstance(ref, dict):  # e.g. HOW["flow"] items: compare the texts, not the key names
        if not isinstance(value, dict):
            return []
        return [pair for key, r in ref.items() if key in value for pair in _pairs(r, value[key])]
    return [pair for r, v in zip(ref, value) for pair in _pairs(r, v)]


def _describe(value):
    if isinstance(value, (list, tuple)):
        return f"{type(value).__name__} of {len(value)}"
    return type(value).__name__


def check(code):
    """The Report of one language's core file."""
    report = Report(code)
    if code not in i18n.LANG_BY_CODE:
        report.problems.append(f"{code}: not a site language (apps/core/languages.py)")
        return report
    english = import_module(i18n.module_name(i18n.DEFAULT))
    if not has_file(code):
        report.missing.append(f"apps/core/i18n/{code}.py doesn't exist yet: English chrome, no core pages")
        return report
    try:
        module = import_module(i18n.module_name(code))
    except Exception as error:  # noqa: BLE001 - report syntax and import errors
        report.problems.append(f"apps/core/i18n/{code}.py can't be imported: {error!r}")
        return report
    report.exists = True
    for name in sorted(n for n in vars(module) if n.isupper() and n not in NAMES):
        report.problems.append(f"{name}: unknown name (the file holds {', '.join(NAMES)})")
    updated = getattr(module, "UPDATED", None)
    if updated is not None and not isinstance(updated, date):
        report.problems.append("UPDATED: must be a date, e.g. date(2026, 11, 8)")
    for name in i18n.SECTIONS:
        own = getattr(module, name, None)
        if own is None:
            served = {v[0]: k for k, v in i18n.PAGES.items()}.get(name)
            note = f": {i18n.path(served, code)} isn't served" if served else ": the chrome shows in English"
            report.missing.append(f"{name} (the whole section){note}")
            continue
        _compare(report, name, (), getattr(english, name), own)
    if code != i18n.DEFAULT and any(getattr(module, i18n.PAGES[p][0], None) is not None for p in ("home", "pricing")):
        from apps.growth.validate import has_file as has_growth_file

        if not has_growth_file(code):
            report.problems.append(f"HOME/PRICING show the packages, whose words come from apps/growth/i18n/{code}.py: "
                                   "that file doesn't exist yet, so they'd show in English")
    return report
