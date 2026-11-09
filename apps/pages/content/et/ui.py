"""Estonian UI of the money pages (informal "sa"). Mirrors en/ui.py key by key.

Grammar notes for the placeholders (one case each, every template below uses that case):
    {platform} can't take a case ending (YouTube needs "YouTube'is"), so it stays nominative
        after a generic noun: "platvormil {platform}", "platvormile {platform}".
    {audience} nominative plural ("Uued {audience}", "kõik sinu uued {audience} on...").
    {follow} da-infinitive phrase after "otsustama" ("otsustasid {follow}").
    {profile} genitive, the total object ("avastasid sinu {profile}").
    {handle} nominative, object of an imperative ("Anna meile oma {handle}").
    {content} nominative plural, always the subject ("sinu {content} meeldivad").
    {service} partitive singular, the form after a number ("{quantity} {service}").
"""

UI = {
    # Words that change with the platform or the service
    "audience": {"instagram": "jälgijad", "tiktok": "jälgijad", "youtube": "tellijad"},
    "follow": {"instagram": "sind jälgida", "tiktok": "sind jälgida", "youtube": "tellida"},
    "profile": {"instagram": "profiili", "tiktok": "profiili", "youtube": "kanali"},
    "handle": {"instagram": "kasutajanimi", "tiktok": "kasutajanimi", "youtube": "kanali käepide"},
    "content": {"instagram": "postitused", "tiktok": "videod", "youtube": "videod"},
    "service_names": {"followers": "Jälgijad", "subscribers": "Tellijad", "likes": "Meeldimised",
                      "views": "Vaatamised", "comments": "Kommentaarid"},
    "service_words": {"followers": "jälgijat", "subscribers": "tellijat", "likes": "meeldimist",
                      "views": "vaatamist", "comments": "kommentaari"},

    # Page chrome
    "home": "Avaleht",
    "crumbs_label": "Navigeerimisrada",
    "eyebrow": "{platform} · {service_name}",
    "eyebrow_hub": "{platform} · kasv",
    "cta": "Alusta paketiga {pick_name}",
    "cta_more": "Vaata kõiki pakette",
    "trust": ["Päris inimesed, mitte botid", "Me ei küsi kunagi sinu parooli", "Kuupõhine, tühistad igal ajal"],
    "product_name": "Kasvupaketid platvormile {platform}",
    "sticky_cta": "Alusta",

    # Packages
    "packages_title": "Vali oma pakett",
    "packages_lead": "Kolm kuupaketti. Uued {audience}, meeldimised, vaatamised ja kommentaarid tulevad koos, samadelt päris inimestelt.",
    "packages_note": "Tüüpilised kuuvahemikud, mitte kindel arv: kõik sinu uued {audience} on päris inimesed, kes otsustasid ise {follow}, nii et iga kuu on veidi erinev.",

    # What's included: the page's own service comes first, then the rest in this order.
    "included_title": "Mis on hinna sees",
    "included_lead": "Iga pakett toob kogu pildi, samadelt päris inimestelt.",
    "included_items": {
        "audience": ("Uued {audience}", "Päris inimesed, kes avastasid sinu {profile} ja otsustasid {follow}. Paketiga {starter_name} tavaliselt {starter_audience} kuus."),
        "likes": ("Meeldimised samadelt inimestelt", "Paketiga {starter_name} tavaliselt {starter_likes} kuus. Meeldimise saavad need {content}, mis inimestele päriselt meeldivad."),
        "comments": ("Kommentaarid nende endi sõnadega", "Paketiga {starter_name} tavaliselt {starter_comments} kuus. Kirjutavad inimesed, mitte kunagi skriptid."),
        "views": ("Vaatamised tulevad kaasa", "Sinu {content} jõuavad samade inimesteni, kes vaatavad neid omal soovil. Vaatamisi me ette ei loe: igaüks neist on inimene."),
        "days": ("Jaotatud 30 päevale", "Natuke iga päev, sinu valitud asukohast. Mitte kunagi kõik korraga."),
        "dashboard": ("Sinu töölaud", "Mida me mõõtsime, päev-päevalt: sinu kampaania külastused ja uued {audience}, kelle need tõid."),
    },

    # How it works: the subscription, step by step
    "steps_title": "Kuidas see töötab",
    "steps_lead": "Kuutellimus: sina valid paketi, meie viime läbi kampaania, päris inimesed otsustavad.",
    "steps": [
        ("Vali pakett", "{starter_name}, {rising_name} või {pro_name}, arveldus kord kuus. Tühistada saad igal ajal oma kontol."),
        ("Me käivitame sinu kampaania", "Anna meile oma {handle} platvormil {platform} ja ütle, kust sinu publik peaks pärit olema. Me ei küsi kunagi sinu parooli."),
        ("Päris inimesed avastavad sinu {profile}", "Iga päev viime sinu {profile} päris inimeste ette. Need, kellele nähtu meeldib, otsustavad ise {follow}, annavad meeldimisi ja kommenteerivad."),
        ("Töölaud näitab, mida me mõõtsime", "Sinu kampaania külastused ja uued {audience}, kelle need tõid, päev-päevalt. Mõõdetud numbrid, mitte kunagi oletused."),
    ],

    # Real people vs bots / instant
    "compare_title": "Päris inimesed, mitte botid",
    "compare_lead": "Silmapilkne tähendab botte: ükski päris inimene ei otsusta {follow} paar sekundit pärast makset.",
    "compare_cols": ("Mis muutub", "Silmapilksed ja botiteenused", "Growsterr"),
    "compare": [
        ("Kes nad on", "Botid ja võltsprofiilid", "Päris inimesed, kes otsustasid {follow}"),
        ("Kiirus", "Tuhandeid minutitega", "Natuke iga päev, terve kuu"),
        ("Meeldimised ja kommentaarid", "Müüakse eraldi, veel rohkematelt bottidelt", "Samadelt inimestelt, sinu paketi sees"),
        ("Sinu levik", "Langeb vaikselt: publik, kes kunagi ei reageeri, annab platvormile {platform} märku, et sinu {content} ei vääri näitamist", "Kasvab koos inimestega, kes vaatavad, annavad meeldimisi ja tulevad tagasi"),
        ("Sinu parool", "Küsitakse sageli", "Mitte kunagi"),
        ("Mida sa näed", "Number, mis võib järgmise puhastusega kaduda", "Töölaud sellega, mida me mõõtsime"),
    ],

    # Quantity pages: how a monthly package gets you to the goal
    "quantity_title": "Kuidas koguda {quantity} {service}",
    "quantity_lead": "Me ei müü valmis pakki, kus on täpselt {quantity}. Päris inimesed otsustavad ise, seega jõuad sinna kuupaketiga loomulikus tempos.",
    "pace_title": "Tüüpiline tempo paketiga {pick_name}",
    "pace_month": "{n}. kuu",
    "pace_goal": "Eesmärk: {quantity}",
    "pace_note": "Tüüpilised vahemikud selle põhjal, mida päris inimesed teevad, mitte lubadus. Mõni kuu toob rohkem, mõni vähem.",
    "by_plan_title": "Aeg eesmärgini {quantity} paketi kaupa",
    "a_month": "{range} kuus",
    "when_first": "tavaliselt juba esimesel kuul",
    "when_about": "tavaliselt umbes {n} kuud",
    "when_range": "tavaliselt {low}–{high} kuud",
    "views_pace": "Vaatamised tulevad samadelt päris inimestelt, kes avastavad sinu {profile}, seega me ei loe neid ette. Sellele eesmärgile sobib kõige paremini pakett {pick_name}.",

    # FAQ, related pages, closing
    "faq_title": "Küsimused ja vastused",
    "related_title": "Uuri edasi",
    "related": {
        "platform": "Veel teemal {platform}",
        "platforms": "Teistel platvormidel",
        "quantities": "Teised eesmärgid",
        "modifiers": "Teised viisid kasvada",
        "articles": "Loe edasi",
        "hubs": "Kasva päris inimestega platvormidel",
    },
    # The tools a page can carry ("tool"): they run in the browser, nothing is sent.
    "tools": {
        "calculate": "Arvuta",
        "followers": "Jälgijad",
        "avg_likes": "Keskmiselt meeldimisi postituse kohta",
        "avg_comments": "Keskmiselt kommentaare postituse kohta",
        "engagement_title": "Sinu kaasatuse määr",
        "engagement_lead": "Kui suur osa sinu jälgijatest reageerib tavalisele postitusele. Sisesta numbrid oma viimastest postitustest.",
        "engagement_result": "Sinu kaasatuse määr on {rate}%.",
        "engagement_note": "Määr tõuseb, kui sinu postitused lähevad jälgijatele päriselt korda. Jälgijad, kes kunagi ei reageeri, langetavad seda, olgu neid kui palju tahes.",
        "growth_title": "Kui kaua läheb eesmärgini?",
        "growth_lead": "Sisesta, kus sa praegu oled ja kuhu tahad jõuda. Arvutame selle iga paketi tüüpilise kuuvahemiku põhjal.",
        "current": "Jälgijaid täna",
        "goal": "Sinu eesmärk",
        "when_first": "tavaliselt juba esimesel kuul",
        "when_range": "tavaliselt {low}–{high} kuud",
        "when_about": "umbes {n} kuud",
        "reached": "Oled juba kohal.",
        "growth_note": "Tüüpilised vahemikud, mitte lubadus: päris inimesed otsustavad ise, kas sind jälgida.",
    },
    # Eyebrow above the headline of pages outside the platform x service grid (by "kind").
    "article_eyebrows": {
        "guide": "Juhend",
        "alternative": "Võrdlus",
        "payment": "Maksed",
        "agency": "Kasvuagentuur",
        "tool": "Tööriist",
        "intent": "Otsene vastus",
    },
    "cta_title": "Valmis kasvama platvormil {platform}?",
    "cta_text": "Vali pakett ja me käivitame sinu kampaania. Ülejäänu otsustavad päris inimesed ja töölaud näitab, mida me mõõtsime.",

    # Platform hubs
    "services_title": "Mida me platvormil {platform} kasvatame",
    "services_lead": "Üks pakett toob kõik selle, samadelt päris inimestelt.",
    "teasers": {
        "audience": "Päris inimesed, kes avastavad sinu {profile} ja otsustavad {follow}.",
        "likes": "Meeldimised inimestelt, kellele sinu {content} meeldivad.",
        "views": "Vaatamised inimestelt, kes otsustavad ise vaadata, mitte kunagi skriptidelt.",
        "comments": "Kommentaarid, mille päris inimesed kirjutavad oma sõnadega.",
    },
    "explore": "Vaata lähemalt",
    "in_package": "Iga paketi sees",
    "goals_title": "Veel võimalusi kasvada platvormil {platform}",
    "other_hubs_title": "Kasvatame ka",
}
