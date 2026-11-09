"""UI strings of the growth system: apps/growth/i18n/<code>.py, one file per language that has them.

Each file has UI (the strings, worded for Instagram and TikTok, where the audience is
"followers") and PLATFORM_UI = {"youtube": {...}}: the keys whose wording differs on YouTube
(subscribers, a channel, subscribing), written out per language so the grammar stays right.
ui_for() merges them and fills the placeholders {platform} (Instagram, TikTok, YouTube) and
{audience} (the language's word for the platform's audience: the "audience" key).
English fills any key a language doesn't have yet (`manage.py check_growth_ui` reports it), and a site
language without a file (apps/core/languages.py lists 41) is shown in English: UI only holds the
languages that have one, so `code in UI` tells whether the growth pages speak it."""
from importlib import import_module

from apps.core.languages import LANGS

from .constants import AUDIENCE, PLATFORM_NAMES, PLATFORMS  # noqa: F401

UI = {}
PLATFORM_UI = {}
for _lang in LANGS:
    try:
        _module = import_module(f"apps.growth.i18n.{_lang.code}")
    except ModuleNotFoundError:
        continue
    UI[_lang.code] = _module.UI
    PLATFORM_UI[_lang.code] = getattr(_module, "PLATFORM_UI", {})


def _fill(value, values):
    if isinstance(value, str):
        for key, text in values.items():
            value = value.replace("{" + key + "}", text)
        return value
    if isinstance(value, (list, tuple)):
        return type(value)(_fill(v, values) for v in value)
    if isinstance(value, dict):
        return {k: _fill(v, values) for k, v in value.items()}
    return value


def ui_for(code, platform):
    """The UI strings of one language for one platform, placeholders filled."""
    code = code if code in UI else "en"
    merged = {**UI["en"], **PLATFORM_UI["en"].get(platform, {}), **UI[code], **PLATFORM_UI[code].get(platform, {})}
    values = {"platform": PLATFORM_NAMES[platform], "audience": merged.get("audience", "")}
    return {k: _fill(v, values) for k, v in merged.items()}


def platform_keys(code):
    """The keys whose text differs between the platforms in this language (the order page swaps them)."""
    variants = [ui_for(code, p) for p in PLATFORMS]
    return sorted(k for k in variants[0] if any(v.get(k) != variants[0][k] for v in variants[1:]))
