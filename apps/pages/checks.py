"""Everything a content file can get wrong, checked on what visitors actually see (placeholders
filled from the packages). manage.py check_pages prints these; the tests run them on every
content file, so a broken page can't ship.

Errors fail the check. Warnings are worth fixing but don't block (--strict makes them fail)."""
import re
from datetime import date

from django.contrib.staticfiles import finders
from django.urls import Resolver404, resolve

from apps.core.languages import DEFAULT

from . import context as page_context
from . import dimensions as dims
from . import sitemaps
from .images import ARTS, IMAGES
from .registry import LANG_ORDER, Problem, Variant

TITLE = (20, 65)           # characters, after placeholders are filled
DESCRIPTION = (70, 160)
LABEL_MAX = 60
H1_MAX = 90
INTRO = (60, 420)
ALT_MAX = 160
FAQ_MIN = 3
REQUIRED = ("slug", "label", "title", "description", "h1", "intro", "hero", "faqs")
OPTIONAL = ("service", "quantity", "modifier", "country", "updated", "plan", "sections", "included", "steps",
            "compare", "quantity_text", "article", "kind", "platform", "tool")
TOOLS = ("engagement-calculator", "growth-calculator")
SECTION_KEYS = {"h2", "p", "ul", "image"}

# The copy rules as patterns (case-insensitive). ALL is checked in every language, because English
# words turn up in any language's copy; LANG adds each language's own words. Extend freely.
FORBIDDEN_ALL = (
    (r"\bseo\b", "SEO"),
    (r"search engine|search result|\bkeywords?\b|\brankings?\b", "search engines, keywords or rankings"),
    (r"guarant", "guarantee"),
    (r"\bfree\b", "free"),
    (r"crypto|bitcoin|ethereum|\busdt\b", "crypto"),
    (r"celebrit|\bverified\b", "celebrity or verified"),
    (r"\b(?:fe)?male\b|\bgender\b", "gender targeting"),
    (r"testimonial|trustpilot|\b\d(?:[.,]\d)?\s*/\s*5\b|★", "reviews, ratings or testimonials"),
)
FORBIDDEN_LANG = {
    "de": r"kostenlos|gratis|umsonst|garantie|garantiert|suchmaschin|schlüsselw|promi\b|verifiziert|weiblich|männlich|geschlecht",
    "nl": r"gratis|garantie|gegarandeerd|zoekmachine|zoekwoord|geverifieerd|vrouwelijk|mannelijk|geslacht",
    "fr": r"gratuit|garanti|référencement|moteurs? de recherche|mots?-clés?|célébrit|vérifié|féminin|masculin",
    "it": r"gratis|gratuit|garanzi|garantit|motor[ei] di ricerca|posizionamento|parol[ae] chiave|celebrit|verificat|femminil|maschil",
    "es": r"gratis|gratuit|garantí|garantiza|motor(?:es)? de búsqueda|posicionamiento|palabras? clave|celebridad|verificad|femenin|masculin",
    "pl": r"darmow|za darmo|gratis|gwarancj|gwarantowan|wyszukiwar|pozycjonowan|słow[ao] kluczow|celebryt|zweryfikowan|kobiec|męsk",
    "ru": r"бесплатн|даром|гарант|поисков|ключев\w* слов|знаменит|верифицир|женск|мужск",
    "uk": r"безкоштовн|задарма|гарант|пошуков|ключов\w* слів|знаменит|верифік|жіноч|чоловіч",
    "ar": r"مجان|ضمان|مضمون|محركات البحث|محرك البحث|كلمات مفتاحية|الكلمات المفتاحية|مشاهير|موثق|إناث|ذكور",
    "sv": r"gratis|kostnadsfri|garanti|sökmotor|sökord|nyckelord|kändis|verifierad|kvinnlig|manlig",
    "da": r"gratis|garanti|søgemaskine|søgeord|nøgleord|kendis|berømthed|verificeret|kvindelig|mandlig",
    "no": r"gratis|garanti|søkemotor|søkeord|nøkkelord|kjendis|verifisert|kvinnelig|mannlig",
    "ro": r"gratuit|gratis|garan|motor(?:ul)? de căutare|motoare de căutare|cuvinte cheie|cuvânt cheie|celebrit|verificat|feminin|masculin",
    "az": r"pulsuz|zəmanət|axtarış sistem|axtarış motor|açar söz|məşhur|təsdiqlənmiş|qadın",
    "tr": r"ücretsiz|bedava|garanti|arama motor|anahtar kelime|ünlü yorum|onaylı yorum|mavi tik|kadın|erkek|cinsiyet",
    "hr": r"besplatn|gratis|džab|garanc|garantir|zajamč|jamč|jamstv|tražilic|pretraživač|ključn\w* riječ|rangiranj|pozicioniranj|slavn|poznat\w* osob|celebrit|verificiran|potvrđen\w* komentar|žensk|mušk|\bspol\b|spola\b|po spolu",
    "sl": r"brezplačn|zastonj|gratis|garancij|garantir|zajamč|jamstv|jamčimo|iskalnik|ključn\w* besed|zvezdnik|slavn|celebrit|verificiran|preverjen|overjen|žensk|mošk|\bspol\b|\bspola\b|po spolu",
    "sr": r"besplatn|gratis|džab|garanc|garantov|garantuj|zagarantovan|jemč|jemstv|pretraživač|ključn\w* reč|rangiranj|slavn|poznat\w* ličnost|verifikovan|žensk|mušk|\bpol\b|po polu",
    "bs": r"besplatn|gratis|džab|garanc|garantuj|garantir|garantovan|jamč|jamstv|tražilic|pretraživač|ključn\w* riječ|rangiranj|pozicioniranj|slavn|poznat\w* ličnost|celebrit|verificiran|verifikovan|potvrđen\w* komentar|žensk|mušk|\bspol\b|spola\b|po spolu",
    "mk": r"бесплатн|гратис|бадева|гаранц|гарантир|загарантир|пребарувач|клучн\w* збор|рангирањ|позиционирањ|славн\w* личност|познат\w* личност|целебрит|верификуван|потврден\w* коментар|сина ознака|женск|машк|\bпол(?:от|ови)?\b",
    "sq": r"falas|gratis|pa pages|pa kosto|garanc|garant|motor\w* (?:e |i |të )?kërkim|fjal\w* kyç|renditj|famsh|celebrit|personazh\w* të njohur|verifikua|femr|femër|meshk|mashkull|gjini",
    "cs": r"zdarma|zadarmo|bezplatn|gratis|garanc|garantov|zaruč|vyhledávač|klíčov\w* slov|celebrit|slavn\w* osobnost|ověřen|žensk|mužsk|pohlaví",
    "sk": r"zadarmo|zdarma|bezplatn|gratis|garanc|garantov|záruk|zaruč|vyhľadávač|kľúčov\w* slov|celebrit|slávn\w* osobnost|overen|žensk|mužsk|pohlavi",
    "hu": r"ingyen|díjmentes|garanci|garantál|keresőmotor|keresőoptimaliz|kulcssz|rangsor|celeb|hírességek?|hitelesített|ellenőrzött fiók|\bnői\b|férfi|nemek szerint",
    "bg": r"безплатн|даром|гаранц|гарантир|търсачк|търсещ\w* машин|ключов\w* дум|знаменитост|известни личности|верифицир|потвърден\w* (?:профил|акаунт)|женск|мъжк",
    "be": r"бясплатн|дарма|гарант|пошукав|ключав\w* сло|знакаміт|верыфік|жаноч|мужчынск",
    "fi": r"ilmai|takuu|taattu|taataan|takaam|\btakaa\b|hakukone|avainsan|hakutulo|julkkis|julkimo|kuuluisuu|vahvistet\w* (?:tili|tile|komment)|varmennet|sininen merkki|naisseuraaj|miesseuraaj|naispuol|miespuol|sukupuol",
    "is": r"ókeypis|frítt|ábyrgð|ábyrgj|tryggjum|tryggt|leitarvél|leitarorð|leitarniðurst|frægt fólk|frægra|frægu fólki|stjörnur|vottað|vottuð|staðfest\w* (?:reikning|aðgang|athugasemd|ummæl)|blátt hak|kvenkyns|karlkyns|eftir kyni|kynjamið|\bkonur\b|\bkarlar\b",
    "pt": r"gr[aá]tis|gratuit|de borla|garant|motor(?:es)? de (?:busca|pesquisa)|posicionamento|palavras?[- ]chave|celebridade|verificad|feminin|masculin",
    "ca": r"gr[aà]tis|gratu[iï]t|\bde franc\b|garant|cercador|motors? de cerca|posicionament|paraul(?:a|es) clau|celebritat|verificad|verificat|femen[ií]|mascul[ií]",
    "eu": r"\bdoan\b|doako|dohain|bermat|berme(?!o)|bilatzaile|bilaketa[- ]motor|gako[- ]hitz|ospetsu|famatu|egiaztatu(?:tako|riko|ak\b|a\b)|emakumezko|gizonezko",
    "gl": r"gr[aá]tis|gratu[ií]t|de balde|garant|motor(?:es)? de busca|buscador|posicionamento|palabras?[- ]clave|celebridade|verificad|feminin|masculin",
    "et": r"tasuta|garantii|garanteeri|otsingumootor|märksõn|võtmesõn|kuulsus|verifitseeri|kinnitatud (?:konto|kommentaar)|naissoost|meessoost|\bsugu\b|soolise",
    "lv": r"bezmaksas|par brīvu|garantij|garantē|meklētājprogramm|meklēšanas sistēm|atslēgvārd|slavenīb|verificēt|sieviet|vīriet|dzimum",
    "lt": r"nemokam|garantuo|garantij|paieškos sistem|raktažod|įžymyb|verifikuot|patvirtint\w* (?:paskyr|komentar)|moter|vyrišk|\blyt(?:is|ies|ims)\b",
    "ga": r"in aisce|ráthaíocht|ráthaigh|inneall cuardaigh|innill chuardaigh|eochairfhocal|cáiliúl|fíoraithe|baineannach|fireannach|inscne",
    "mt": r"b'xejn|bla ħlas|garanzij|garantit|magni tat-tfittxija|magna tat-tfittxija|kliem ewlieni|kelma ewlenija|ċelebrit|famuż|verifikat|\bnisa\b|irġiel|\bsess\b|ġeneru",
    "lb": r"gratis|\bfräi\b|ëmsoss|garanti|sichmaschinn|sichmotor|schlësselwier|promi\b|celebrit|verifizéier|weiblech|männlech|geschlecht",
    "cy": r"am ddim|gwarant|peiriant chwilio|peiriannau chwilio|allweddair|allweddeiriau|enwog|wedi'i ddilysu|wedi'u dilysu|dilysedig|benywaidd|gwrywaidd|rhywedd",
    "el": r"δωρε[άα]ν|τζ[άα]μπα|εγγυ|εγγύ|μηχαν\w* αναζ[ήη]τησ|λ[έε]ξ\w* κλειδ|κατ[άα]ταξ|δι[άα]σημ|σελεμπρ[ίι]τι|επαληθευμ[έε]ν|πιστοποιημ[έε]ν|γυνα[ίι]κ|[άα]νδρ|[άα]ντρ|θηλυκ|αρσενικ|φ[ύυ]λο\b|φ[ύυ]λου|κρυπτονομ",
}


# The words of each copy rule across languages, for intent pages: a page that may use "free" may say
# "ücretsiz" or "kostenlos", but the rest of its language's forbidden list still applies.
LOCAL_FAMILIES = {
    "free": (r"free|kostenlos|gratis|umsonst|gratuit|gratu[iïí]t|darmow|za darmo|бесплатн|даром|безкоштовн|задарма|مجان|"
             r"kostnadsfri|pulsuz|ücretsiz|bedava|zdarma|zadarmo|bezplatn|ingyen|díjmentes|безплатн|бясплатн|дарма|"
             r"besplatn|džab|brezplačn|zastonj|гратис|бадева|falas|pa pages|pa kosto|δωρε[άα]ν|τζ[άα]μπα|ilmai|ókeypis|"
             r"frítt|gr[aáà]tis|de borla|de franc|doan|doako|dohain|de balde|tasuta|bezmaksas|par brīvu|nemokam|in aisce|"
             r"b'xejn|bla ħlas|fräi|ëmsoss|am ddim"),
    "celebrity or verified": (r"verif|vérif|celeb|célèb|célébr|promi|ünlü|onaylı|mavi tik|знаменит|верифи|верыфік|знакаміт|مشاهير|موثق|kändis|"
                              r"kendis|berømthed|kjendis|məşhur|təsdiqlənmiş|ověřen|overen|slavn|slávn|hírességek?|hitelesített|"
                              r"ellenőrzött fiók|известни личности|потвърден|poznat|potvrđen|zvezdnik|preverjen|overjen|"
                              r"целебрит|верификуван|потврден|сина ознака|famsh|personazh|δι[άα]σημ|σελεμπρ|επαληθευμ|πιστοποιημ|"
                              r"julkkis|julkimo|kuuluisuu|vahvistet|varmennet|sininen merkki|fræg|stjörnur|vottað|vottuð|staðfest|"
                              r"blátt hak|ospetsu|famatu|egiaztatu|kuulsus|kinnitatud|slavenīb|įžymyb|patvirtint|cáiliúl|"
                              r"fíoraithe|ċelebrit|famuż|enwog|dilys|zweryfikowan|celebryt"),
    "gender targeting": (r"female|male|gender|weiblich|männlich|geschlecht|vrouwelijk|mannelijk|geslacht|féminin|femen|feminin|"
                         r"mascul|maschil|femminil|kobiec|męsk|женск|мужск|жіноч|чоловіч|إناث|ذكور|kvinnlig|manlig|kvindelig|"
                         r"mandlig|kvinnelig|mannlig|qadın|kadın|erkek|cinsiyet|žensk|mužsk|pohlav|\bnői\b|férfi|nemek szerint|"
                         r"мъжк|жаноч|мужчынск|mušk|mošk|spol|\bpol\b|po polu|машк|\bпол|femr|femër|meshk|mashkull|gjini|"
                         r"γυνα|[άα]νδρ|[άα]ντρ|θηλυκ|αρσενικ|φ[ύυ]λο|naisseuraaj|miesseuraaj|naispuol|miespuol|sukupuol|"
                         r"kvenkyns|karlkyns|kyni|kynjamið|konur|karlar|emakumezko|gizonezko|naissoost|meessoost|sugu|soolise|"
                         r"sieviet|vīriet|dzimum|moter|vyrišk|lyt|baineannach|fireannach|inscne|nisa|irġiel|sess|ġeneru|"
                         r"weiblech|männlech|benywaidd|gwrywaidd|rhywedd"),
}


def forbidden_in(text, lang, allow=()):
    """The copy rules a string breaks: [(rule, matched text)]. allow: rule names this page may break
    (dimensions.allowed_rules: an intent page's own word)."""
    found = []
    for pattern, rule in FORBIDDEN_ALL:
        if rule in allow:
            continue
        if rule == "SEO" and lang == "ga":  # Irish "seo" means "this": only the capitalised acronym counts
            match = re.search(r"\bSEO\b", text)
        else:
            match = re.search(pattern, text, re.IGNORECASE)
        if match:
            found.append((rule, match.group(0)))
    local = FORBIDDEN_LANG.get(lang)
    if local:
        exempt = [re.compile(LOCAL_FAMILIES[rule], re.IGNORECASE) for rule in allow if rule in LOCAL_FAMILIES]
        for match in re.finditer(local, text, re.IGNORECASE):
            if any(e.search(match.group(0)) for e in exempt):
                continue  # the page's own word, in this language
            found.append(("forbidden word in this language", match.group(0)))
            break
    return found


class Report:
    def __init__(self):
        self.problems = []

    def error(self, where, message):
        self.problems.append(Problem("error", where, message))

    def warning(self, where, message):
        self.problems.append(Problem("warning", where, message))


def _is_text(value):
    return isinstance(value, str) and value.strip() != ""


def _pairs(value, size):
    return isinstance(value, (list, tuple)) and all(
        isinstance(item, (list, tuple)) and len(item) == size and all(_is_text(x) for x in item) for item in value)


def _check_strings(report, where, lang, value, known=None, allow=()):
    """Placeholders left unfilled and copy-rule words, in every string of a value."""
    seen = set()
    for text in page_context.strings(value):
        for name in page_context.PLACEHOLDER.findall(text):
            if (known is None or name not in known) and name not in seen:
                seen.add(name)
                report.error(where, f"placeholder {{{name}}} has no value here")
        for rule, word in forbidden_in(text, lang, allow):
            report.error(where, f"copy rule ({rule}): '{word}' in \"{text[:90]}\"")


def check_ui(report, registry, plan_keys):
    english = registry.ui.get(DEFAULT)
    if not english:
        report.error("apps/pages/content/en/ui.py", "the English UI is missing: every language falls back to it")
        return
    known = page_context.known_names(plan_keys)
    for lang in registry.languages():
        where = f"{lang} UI (apps/pages/content/{lang}/ui.py)"
        ui = registry.ui.get(lang)
        if ui is None:
            report.error(where, "this language has pages but no ui.py")
            continue
        if lang != DEFAULT:
            missing = sorted(set(english) - set(ui))
            if missing:
                report.error(where, f"missing keys (English shows instead): {', '.join(missing)}")
            for key, value in english.items():
                if isinstance(value, dict) and isinstance(ui.get(key), dict):
                    gaps = sorted(set(value) - set(ui[key]))
                    if gaps:
                        report.error(where, f"'{key}' misses {', '.join(gaps)}")
        merged = registry.ui_for(lang)
        shapes = {"steps": 2, "compare": 3}
        for key, size in shapes.items():
            if not _pairs(merged.get(key), size):
                report.error(where, f"'{key}' must be a list of {size}-part entries")
        if not (isinstance(merged.get("compare_cols"), (list, tuple)) and len(merged["compare_cols"]) == 3):
            report.error(where, "'compare_cols' must have 3 parts: the row label column, the bot column, ours")
        items = merged.get("included_items")
        if not (isinstance(items, dict) and all(_pairs([v], 2) for v in items.values())):
            report.error(where, "'included_items' must map each item to (title, text)")
        _check_strings(report, where, lang, ui, known)


def check_image(report, where, ref, used):
    if not isinstance(ref, dict):
        report.error(where, 'an image must be {"image": "<id from apps/pages/images.py>", "alt": "..."}')
        return
    image_id = ref.get("image")
    if image_id not in IMAGES:
        report.error(where, f"image '{image_id}' isn't declared in apps/pages/images.py")
    else:
        used.add(image_id)
    alt = ref.get("alt")
    if not _is_text(alt):
        report.error(where, f"image '{image_id}' needs alt text")
    elif len(alt) > ALT_MAX:
        report.warning(where, f"alt text of '{image_id}' is {len(alt)} characters; keep it under {ALT_MAX}")


def check_images(report, used):
    for image_id, spec in IMAGES.items():
        where = f"image '{image_id}' (apps/pages/images.py)"
        src = spec.get("src", "")
        if not (isinstance(src, str) and src.startswith("img/pages/")):
            report.error(where, "src must be a path under static/img/pages/")
            continue
        for side in ("width", "height"):
            if not (isinstance(spec.get(side), int) and spec[side] > 0):
                report.error(where, f"{side} must be the file's size in pixels")
        if spec.get("art", "growth") not in ARTS:
            report.error(where, f"art must be one of {', '.join(ARTS)}")
        exists = finders.find(src) is not None
        if not exists and not spec.get("pending"):
            report.error(where, f"static/{src} doesn't exist (add the file, or mark the image pending)")
        elif exists and spec.get("pending"):
            report.warning(where, f"static/{src} exists now: remove \"pending\"")
        if image_id not in used:
            report.warning(where, "no page uses this image")


def check_page(report, page, registry, live, used, plan_keys):
    where = f"{page.name} ({page.source})"
    data, v = page.data, page.variant
    for key in REQUIRED:
        if key not in data:
            report.error(where, f"'{key}' is missing")
    unknown = sorted(set(data) - set(REQUIRED) - set(OPTIONAL))
    if unknown:
        report.warning(where, f"unknown keys are ignored: {', '.join(unknown)}")
    if "plan" in data and data["plan"] not in plan_keys:
        report.error(where, f"plan must be one of {', '.join(plan_keys)}")
    try:
        r = page_context.resolve_page(page, registry)
    except Exception as error:  # noqa: BLE001 (report anything that stops the page from building)
        report.error(where, f"the page can't be built: {error!r}")
        return
    p = r.p
    empty = sorted(name for name, value in r.values.items() if value in ("", None))
    if empty:
        report.error(where, f"no value from the packages for {', '.join('{' + n + '}' for n in empty)} "
                            "(apps/growth/plan.py changed?)")

    for key, (low, high) in (("title", TITLE), ("description", DESCRIPTION)):
        text = p.get(key)
        if not _is_text(text):
            report.error(where, f"'{key}' must be text")
        elif not low <= len(text) <= high:
            report.error(where, f"{key} is {len(text)} characters; keep it {low}–{high}: \"{text}\"")
    label = page_context.label(page, registry)
    if not _is_text(data.get("label")):
        report.error(where, "'label' must be text (the link text other pages use)")
    elif len(label) > LABEL_MAX:
        report.error(where, f"label is {len(label)} characters; keep it under {LABEL_MAX}")
    elif page_context.PLACEHOLDER.search(label):
        report.error(where, "a label can only use {platform}, {audience}, {service}, {quantity} and the other page words")
    h1 = p.get("h1")
    if not (_is_text(h1) or (isinstance(h1, (list, tuple)) and 1 <= len(h1) <= 2 and all(isinstance(x, str) for x in h1)
                             and _is_text("".join(h1)))):
        report.error(where, "'h1' must be text, or (text, highlighted text)")
    elif len("".join(page_context.headline(h1))) > H1_MAX:
        report.warning(where, f"h1 is longer than {H1_MAX} characters")
    intro = p.get("intro")
    if not _is_text(intro):
        report.error(where, "'intro' must be text")
    elif not INTRO[0] <= len(intro) <= INTRO[1]:
        report.warning(where, f"intro is {len(intro)} characters; {INTRO[0]}–{INTRO[1]} reads best")
    faqs = p.get("faqs")
    if not _pairs(faqs, 2):
        report.error(where, "'faqs' must be a list of (question, answer)")
    elif len(faqs) < FAQ_MIN:
        report.error(where, f"at least {FAQ_MIN} questions, please (there are {len(faqs)})")
    if "hero" in data:
        check_image(report, where, data["hero"], used)
    sections = data.get("sections", [])
    if not isinstance(sections, (list, tuple)):
        report.error(where, "'sections' must be a list")
        sections = []
    for number, section in enumerate(sections, 1):
        spot = f"{where} section {number}"
        if not isinstance(section, dict) or not _is_text(section.get("h2")):
            report.error(spot, "a section needs an 'h2'")
            continue
        extra = sorted(set(section) - SECTION_KEYS)
        if extra:
            report.warning(spot, f"unknown keys are ignored: {', '.join(extra)}")
        paragraphs = section.get("p", [])
        paragraphs = [paragraphs] if isinstance(paragraphs, str) else paragraphs
        if not (isinstance(paragraphs, (list, tuple)) and all(_is_text(x) for x in paragraphs)):
            report.error(spot, "'p' must be text or a list of texts")
        if not (isinstance(section.get("ul", []), (list, tuple)) and all(_is_text(x) for x in section.get("ul", []))):
            report.error(spot, "'ul' must be a list of texts")
        if not paragraphs and not section.get("ul"):
            report.error(spot, "a section needs 'p' or 'ul'")
        if "image" in section:
            check_image(report, spot, section["image"], used)
    for key, size in (("included", 2), ("steps", 2), ("compare", 3)):
        if key in data and not _pairs(data[key], size):
            report.error(where, f"'{key}' must be a list of {size}-part entries")
    if "updated" in data:
        try:
            date.fromisoformat(str(data["updated"]))
        except ValueError:
            report.error(where, "'updated' must be a date: YYYY-MM-DD")
    allow = dims.allowed_rules(v, data.get("kind", ""))
    _check_strings(report, where, page.lang, p, known=None, allow=allow)
    for rule, word in forbidden_in(page.slug.replace("-", " ").replace("/", " "), page.lang, allow):
        report.error(where, f"copy rule ({rule}) in the slug: '{word}'")
    if "tool" in data and data["tool"] not in TOOLS:
        report.error(where, f"tool must be one of {', '.join(TOOLS)}")

    if v.quantity and page_context.metric_for(v.service, r.plans_raw) is None and "plan" not in data:
        report.warning(where, "a quantity of views has no typical ratio: name the package with \"plan\"")
    if page.lang == DEFAULT and v.is_hub and page.slug != v.platform:
        report.error(where, f"the English hub's slug must be '{v.platform}' (other pages link to /{v.platform}/)")
    if v.article:
        pass
    elif not v.is_hub and registry.get(page.lang, Variant(v.platform)) is None:
        report.warning(where, f"this language has no {v.platform} hub yet")
    if not v.is_hub and not v.is_base and registry.get(page.lang, Variant(v.platform, v.service)) is None:
        report.warning(where, f"this language has no {v.platform} {v.service} page above this one")

    for code, path in registry.alternates(page):
        target = registry.at(path)
        if target is None or target.variant != v:
            report.error(where, f"hreflang {code} points to {path}, which isn't this page in {code}")
    if live:
        check_route(report, where, page)


def check_route(report, where, page):
    """The page's path must reach this page: another app's URL can shadow it (pages come last)."""
    from . import views

    try:
        match = resolve(page.path)
    except Resolver404:
        report.error(where, f"{page.path} has no route (restart the server after changing content)")
        return
    if match.func is not views.page or match.kwargs.get("page") is not page:
        report.error(where, f"{page.path} is taken by another URL ({match.view_name or match.func.__name__}): change the slug")


def check_duplicates(report, registry):
    for lang in registry.languages():
        for key in ("title", "description"):
            seen = {}
            for page in registry.pages_in(lang):
                value = page.data.get(key)
                if not isinstance(value, str):
                    continue
                value = page_context.fill(value, page_context.basic_values(page, registry.ui_for(lang)))
                if value in seen:
                    report.error(f"{page.name} ({page.source})", f"same {key} as {seen[value].name}: every page needs its own")
                else:
                    seen[value] = page


def check_sitemaps(report, live):
    """Other apps' sitemap entries (warnings: those files belong to their apps)."""
    for name, entries in sitemaps.app_sections().items():
        where = f"sitemap section '{name}' (apps/{name}/sitemap.py)"
        try:
            raw = list(entries() or [])
        except Exception as error:  # noqa: BLE001
            report.warning(where, f"entries() fails: {error!r}")
            continue
        kept = sitemaps.clean(raw, name)
        if len(kept) != len(raw):
            report.warning(where, f"{len(raw) - len(kept)} entries are dropped (private or not a /path/)")
        if not live:
            continue
        for entry in kept:
            for path in [entry["path"]] + [alt for _, alt in entry.get("alternates") or []]:
                try:
                    resolve(path)
                except Resolver404:
                    report.warning(where, f"{path} doesn't resolve")


def validate(registry, langs=None, live=None):
    """[Problem], errors first. live: the registry the site's URLs are built from (routing is checked)."""
    from apps.growth import plan as growth_plan

    from . import registry as registry_module

    if live is None:
        live = registry is registry_module.REGISTRY
    plan_keys = [p["key"] for p in growth_plan.PLANS]
    report = Report()
    report.problems.extend(registry.problems)
    check_ui(report, registry, plan_keys)
    used = set()
    for page in registry.pages:
        if langs and page.lang not in langs:
            continue
        check_page(report, page, registry, live, used, plan_keys)
    check_duplicates(report, registry)
    if not langs:
        check_images(report, used)
        check_sitemaps(report, live)
    for lang in langs or []:
        if lang not in LANG_ORDER:
            report.error(lang, "unknown language code")
    return sorted(report.problems, key=lambda problem: problem.level != "error")


def summary(registry):
    langs = registry.languages()
    counts = ", ".join(f"{lang} {len(registry.pages_in(lang))}" for lang in langs) or "none"
    pending = sum(1 for spec in IMAGES.values() if finders.find(spec["src"]) is None)
    return (f"{len(registry.pages)} pages in {len(langs)} language{'' if len(langs) == 1 else 's'} ({counts}); "
            f"{len(IMAGES)} images, {pending} still pending.")
