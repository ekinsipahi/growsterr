"""UI strings of the growth system in 16 languages: apps/growth/i18n/<code>.py ({platform}
placeholders are filled per platform). English fills any key a language doesn't have yet."""
from importlib import import_module

from apps.core.languages import LANGS

from .constants import PLATFORM_NAMES

UI = {}
for _lang in LANGS:
    try:
        UI[_lang.code] = import_module(f"apps.growth.i18n.{_lang.code}").UI
    except ModuleNotFoundError:
        continue


def ui_for(code, platform):
    """UI strings with {platform} filled in."""
    name = PLATFORM_NAMES[platform]

    def fill(value):
        if isinstance(value, str):
            return value.replace("{platform}", name)
        if isinstance(value, (list, tuple)):
            return type(value)(fill(v) for v in value)
        return value

    return {k: fill(v) for k, v in {**UI["en"], **UI.get(code, {})}.items()}
