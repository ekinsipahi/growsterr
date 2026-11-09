"""The 41 site languages. English is the main site at /, the others live under /<code>/.

A language here doesn't need any translation to exist: whatever it has no file for falls back
to English (the chrome, the growth pages) or isn't served at all (the core pages, the money
pages). The files a language can have are listed in docs/I18N.md."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Lang:
    code: str           # URL prefix + hreflang
    name: str           # native name shown in the menu
    og_locale: str
    django: str         # Django locale used for form error messages, dates and numbers ("en" when Django has none)
    rtl: bool = False

    @property
    def flag(self):
        return f"img/flags/{self.code}.png"

    @property
    def flag_2x(self):
        return f"img/flags/{self.code}@2x.png"


LANGS = [
    Lang("en", "English", "en_GB", "en"),
    Lang("de", "Deutsch", "de_DE", "de"),
    Lang("nl", "Nederlands", "nl_NL", "nl"),
    Lang("fr", "Français", "fr_FR", "fr"),
    Lang("it", "Italiano", "it_IT", "it"),
    Lang("es", "Español", "es_ES", "es"),
    Lang("pl", "Polski", "pl_PL", "pl"),
    Lang("ru", "Русский", "ru_RU", "ru"),
    Lang("uk", "Українська", "uk_UA", "uk"),
    Lang("ar", "العربية", "ar_AR", "ar", rtl=True),
    Lang("sv", "Svenska", "sv_SE", "sv"),
    Lang("da", "Dansk", "da_DK", "da"),
    Lang("no", "Norsk", "nb_NO", "nb"),
    Lang("ro", "Română", "ro_RO", "ro"),
    Lang("az", "Azərbaycanca", "az_AZ", "az"),
    Lang("tr", "Türkçe", "tr_TR", "tr"),
    Lang("pt", "Português", "pt_PT", "pt"),
    Lang("cs", "Čeština", "cs_CZ", "cs"),
    Lang("sk", "Slovenčina", "sk_SK", "sk"),
    Lang("hu", "Magyar", "hu_HU", "hu"),
    Lang("bg", "Български", "bg_BG", "bg"),
    Lang("hr", "Hrvatski", "hr_HR", "hr"),
    Lang("sl", "Slovenščina", "sl_SI", "sl"),
    Lang("sr", "Srpski", "sr_RS", "sr_Latn"),  # Latin script
    Lang("bs", "Bosanski", "bs_BA", "bs"),
    Lang("mk", "Македонски", "mk_MK", "mk"),
    Lang("sq", "Shqip", "sq_AL", "sq"),
    Lang("el", "Ελληνικά", "el_GR", "el"),
    Lang("fi", "Suomi", "fi_FI", "fi"),
    Lang("et", "Eesti", "et_EE", "et"),
    Lang("lv", "Latviešu", "lv_LV", "lv"),
    Lang("lt", "Lietuvių", "lt_LT", "lt"),
    Lang("ga", "Gaeilge", "ga_IE", "ga"),
    Lang("mt", "Malti", "mt_MT", "en"),  # Django has no Maltese
    Lang("is", "Íslenska", "is_IS", "is"),
    Lang("ca", "Català", "ca_ES", "ca"),
    Lang("eu", "Euskara", "eu_ES", "eu"),
    Lang("gl", "Galego", "gl_ES", "gl"),
    Lang("lb", "Lëtzebuergesch", "lb_LU", "lb"),
    Lang("cy", "Cymraeg", "cy_GB", "cy"),
    Lang("be", "Беларуская", "be_BY", "be"),
]
DEFAULT = "en"  # x-default
LANG_BY_CODE = {lang.code: lang for lang in LANGS}
INTL_CODES = [lang.code for lang in LANGS if lang.code != "tr"]


def django_locale(code):
    """The Django language to format dates and numbers in for a site language (English for an unknown code)."""
    lang = LANG_BY_CODE.get(code)
    return lang.django if lang else "en"
