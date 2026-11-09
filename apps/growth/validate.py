"""Checks a language's growth UI strings (apps/growth/i18n/<code>.py) against the English
source: the same keys and shapes in UI and PLATFORM_UI, every placeholder kept, and the copy
rules (no search-engine talk, no promises or "free", no competitors, no crypto, no other
brand). Used by the tests and by `manage.py check_growth_ui [codes]`, which only imports the
files it checks, so a half-written translation elsewhere can't break it."""
import json
import re
from importlib import import_module

from .constants import PLATFORMS

# Never on the site, in any language: search-engine talk, promises we can't make, "free",
# competitor brands, selling panels, crypto, star ratings, and the sister site's brand.
FORBIDDEN = re.compile(
    r"\bSEO\b|search engine|keyword|guarantee|garant|garanz|gwaranc|гарант|zəmanət|ضمان|مضمون|"
    r"\bfree\b|gratis|gratuit|kostenlos|darmo|бесплатн|безкоштовн|مجان|pulsuz|ücretsiz|bedava|"
    r"buzzoid|passthevote|stormlikes|goread|socialwick|superviral|famety|bulkoid|megafamous|useviral|media ?mister|"
    r"smm panel|\bpaypal\b|crypto|krypto|bitcoin|5[- ]star|★|\bSterr\b|sterragency", re.I)
# Filled in by ui_for(); every other {placeholder} is filled by the page that uses the string.
UI_PLACEHOLDERS = ("{platform}", "{audience}")
PLACEHOLDER = re.compile(r"\{[a-z_]+\}")


def load(code):
    module = import_module(f"apps.growth.i18n.{code}")
    return module.UI, getattr(module, "PLATFORM_UI", {})


def shape(value):
    if isinstance(value, dict):
        return {k: shape(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [shape(v) for v in value]
    return type(value).__name__


def _texts(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, (list, tuple)):
        for v in value:
            yield from _texts(v)
    elif isinstance(value, dict):
        for v in value.values():
            yield from _texts(v)


def _pairs(ref, value):
    """(English text, translated text) pairs of one key, matched by position."""
    if isinstance(ref, str):
        return [(ref, value if isinstance(value, str) else None)]
    if isinstance(ref, (list, tuple)) and isinstance(value, (list, tuple)):
        return [pair for r, v in zip(ref, value) for pair in _pairs(r, v)]
    if isinstance(ref, dict) and isinstance(value, dict):
        return [pair for k, r in ref.items() for pair in _pairs(r, value.get(k))]
    return []


def _compare(where, ref, data, problems):
    if set(data) != set(ref):
        problems.append(f"{where} keys: missing {sorted(set(ref) - set(data))}, extra {sorted(set(data) - set(ref))}")
    for key, value in ref.items():
        if key not in data:
            continue
        if shape(data[key]) != shape(value):
            problems.append(f"{where}[{key!r}] shape differs from English")
        for ref_text, text in _pairs(value, data[key]):
            for ph in PLACEHOLDER.findall(ref_text):
                if text is not None and ph not in text:
                    problems.append(f"{where}[{key!r}] lost placeholder {ph}")
        for text in _texts(data[key]):
            m = FORBIDDEN.search(text)
            if m:
                problems.append(f"{where}[{key!r}] forbidden word {m.group(0)!r}")


def check(code):
    """List of problems (empty when the language is complete and clean)."""
    problems = []
    ref_ui, ref_platform = load("en")
    try:
        ui, platform_ui = load(code)
    except Exception as exc:  # noqa: BLE001 - report import/syntax errors as a problem
        return [f"{code}: cannot import: {exc!r}"]
    _compare(f"{code} UI", ref_ui, ui, problems)
    if set(platform_ui) != set(ref_platform) or not set(platform_ui) <= set(PLATFORMS):
        problems.append(f"{code} PLATFORM_UI platforms: {sorted(platform_ui)}, English has {sorted(ref_platform)}")
    for platform, ref in ref_platform.items():
        data = platform_ui.get(platform, {})
        _compare(f"{code} PLATFORM_UI[{platform!r}]", ref, data, problems)
        for key in data:
            if key in ui and shape(data[key]) != shape(ui[key]):
                problems.append(f"{code} PLATFORM_UI[{platform!r}][{key!r}] shape differs from UI[{key!r}]")
    if code == "en":  # YouTube speaks of subscribers and a channel, never of followers
        for key, value in ref_platform.get("youtube", {}).items():
            for text in _texts(value):
                if re.search(r"follow", PLACEHOLDER.sub("", text), re.I):
                    problems.append(f"en PLATFORM_UI['youtube'][{key!r}] says follow: {text!r}")
    return problems


def has_file(code):
    """True when apps/growth/i18n/<code>.py exists (without importing it)."""
    from importlib.util import find_spec

    return find_spec(f"apps.growth.i18n.{code}") is not None


def everything():
    """{code: problems} for every site language that has a file (the others are shown in English)."""
    from apps.core.languages import LANGS

    return {lang.code: check(lang.code) for lang in LANGS if has_file(lang.code)}


def as_text(problems):
    return json.dumps(problems, ensure_ascii=False, indent=1)
