"""Latvian UI of the money pages (polite "jūs"). Mirrors en/ui.py key by key.

Grammar notes for the placeholders (one case each, every template below uses that case):
    {platform} stays indeclinable, as Latvian treats these brand names ("{platform} izaugsme",
        "platformā {platform}").
    {audience} nominative plural ("Jauni {audience}", "visi jūsu jaunie {audience} ir...").
    {follow} infinitive after "izvēlēties" ("izvēlējās {follow}").
    {profile} accusative ("atklāj jūsu {profile}").
    {handle} accusative ("Norādiet savu {platform} {handle}").
    {content} accusative plural, always an object ("skatās jūsu {content}").
    {service} genitive plural, the form after a round number ("{quantity} {service}").
"""

UI = {
    # Words that change with the platform or the service
    "audience": {"instagram": "sekotāji", "tiktok": "sekotāji", "youtube": "abonenti"},
    "follow": {"instagram": "jums sekot", "tiktok": "jums sekot", "youtube": "abonēt"},
    "profile": {"instagram": "profilu", "tiktok": "profilu", "youtube": "kanālu"},
    "handle": {"instagram": "lietotājvārdu", "tiktok": "lietotājvārdu", "youtube": "kanāla identifikatoru"},
    "content": {"instagram": "ierakstus", "tiktok": "video", "youtube": "video"},
    "service_names": {"followers": "Sekotāji", "subscribers": "Abonenti", "likes": "Patīk atzīmes",
                      "views": "Skatījumi", "comments": "Komentāri"},
    "service_words": {"followers": "sekotāju", "subscribers": "abonentu", "likes": "patīk atzīmju",
                      "views": "skatījumu", "comments": "komentāru"},

    # Page chrome
    "home": "Sākums",
    "crumbs_label": "Navigācijas ceļš",
    "eyebrow": "{platform} · {service_name}",
    "eyebrow_hub": "{platform} izaugsme",
    "cta": "Sākt ar {pick_name}",
    "cta_more": "Skatīt visas paketes",
    "trust": ["Īsti cilvēki, nekad boti", "Mēs nekad neprasām jūsu paroli", "Katru mēnesi, atcelt var jebkurā laikā"],
    "product_name": "{platform} izaugsmes paketes",
    "sticky_cta": "Sākt",

    # Packages
    "packages_title": "Izvēlieties paketi",
    "packages_lead": "Trīs mēneša paketes. Jauni {audience}, patīk atzīmes, skatījumi un komentāri nāk kopā, no tiem pašiem īstajiem cilvēkiem.",
    "packages_note": "Tipiski mēneša diapazoni, nevis fiksēts skaits: visi jūsu jaunie {audience} ir īsti cilvēki, kuri paši izvēlējās {follow}, tāpēc katrs mēnesis ir mazliet citāds.",

    # What's included: the page's own service comes first, then the rest in this order.
    "included_title": "Kas ir iekļauts",
    "included_lead": "Katra pakete dod pilnu ainu, no tiem pašiem īstajiem cilvēkiem.",
    "included_items": {
        "audience": ("Jauni {audience}", "Īsti cilvēki, kas atklāja jūsu {profile} un izvēlējās {follow}. Ar {starter_name} parasti {starter_audience} mēnesī."),
        "likes": ("Patīk atzīmes no tiem pašiem cilvēkiem", "Ar {starter_name} parasti {starter_likes} mēnesī, no cilvēkiem, kuri ar prieku skatās jūsu {content}."),
        "comments": ("Komentāri pašu vārdiem", "Ar {starter_name} parasti {starter_comments} mēnesī. Tos raksta cilvēki, nekad skripti."),
        "views": ("Skatījumi nāk līdzi", "Tie paši cilvēki paši skatās jūsu {content}. Skatījumus mēs iepriekš neskaitām: katrs no tiem ir cilvēks."),
        "days": ("Sadalīts 30 dienās", "Mazliet katru dienu, no jūsu izvēlētās vietas. Nekad visu uzreiz."),
        "dashboard": ("Jūsu pārskats", "Ko mēs izmērījām, dienu pa dienai: jūsu kampaņas apmeklējumi un jaunie {audience}, kurus tie atveda."),
    },

    # How it works: the subscription, step by step
    "steps_title": "Kā tas darbojas",
    "steps_lead": "Ikmēneša abonements: jūs izvēlaties paketi, mēs vadām kampaņu, īsti cilvēki izlemj.",
    "steps": [
        ("Izvēlieties paketi", "{starter_name}, {rising_name} vai {pro_name}, ar maksājumu reizi mēnesī. Atcelt varat jebkurā laikā savā kontā."),
        ("Mēs sākam jūsu kampaņu", "Norādiet savu {platform} {handle} un to, no kurienes jānāk jūsu auditorijai. Mēs nekad neprasām jūsu paroli."),
        ("Īsti cilvēki atklāj jūsu {profile}", "Katru dienu mēs parādām jūsu {profile} īstiem cilvēkiem. Tie, kam redzētais patīk, paši izvēlas {follow}, atzīmēt „patīk” un komentēt."),
        ("Jūsu pārskats rāda, ko mēs izmērījām", "Jūsu kampaņas apmeklējumi un jaunie {audience}, kurus tie atveda, dienu pa dienai. Izmērīti skaitļi, nekad minējumi."),
    ],

    # Real people vs bots / instant
    "compare_title": "Īsti cilvēki, nevis boti",
    "compare_lead": "Tūlītējs nozīmē botus: neviens īsts cilvēks neizvēlas {follow} dažas sekundes pēc maksājuma.",
    "compare_cols": ("Kas mainās", "Tūlītējie un botu pakalpojumi", "Growsterr"),
    "compare": [
        ("Kas viņi ir", "Boti un viltus profili", "Īsti cilvēki, kas izvēlējās {follow}"),
        ("Ātrums", "Tūkstoši dažās minūtēs", "Mazliet katru dienu, visu mēnesi"),
        ("Patīk atzīmes un komentāri", "Pārdod atsevišķi, no vēl citiem botiem", "No tiem pašiem cilvēkiem, paketes ietvaros"),
        ("Jūsu sasniedzamība", "Klusi krītas: auditorija, kas nekad neiesaistās, signalizē platformai {platform}, ka jūsu {content} nav vērts rādīt", "Aug kopā ar cilvēkiem, kas skatās, atzīmē „patīk” un atgriežas"),
        ("Jūsu parole", "Bieži tiek prasīta", "Nekad"),
        ("Ko jūs redzat", "Skaitli, kas var pazust nākamajā tīrīšanā", "Pārskatu ar to, ko mēs izmērījām"),
    ],

    # Quantity pages: how a monthly package gets you to the goal
    "quantity_title": "Kā sasniegt {quantity} {service}",
    "quantity_lead": "Mēs nepārdodam fiksētu paku ar {quantity}. Īsti cilvēki izlemj paši, tāpēc mēneša pakete jūs tur aizved dabiskā tempā.",
    "pace_title": "Tipisks temps ar {pick_name}",
    "pace_month": "{n}. mēnesis",
    "pace_goal": "Mērķis: {quantity}",
    "pace_note": "Tipiski diapazoni pēc tā, ko dara īsti cilvēki, nekad ne solījums. Daži mēneši atnes vairāk, daži mazāk.",
    "by_plan_title": "Laiks līdz {quantity} pa paketēm",
    "a_month": "{range} mēnesī",
    "when_first": "parasti jau pirmajā mēnesī",
    "when_about": "parasti apmēram {n} mēneši",
    "when_range": "parasti {low}–{high} mēneši",
    "views_pace": "Skatījumi nāk no tiem pašiem īstajiem cilvēkiem, kas atklāj jūsu {profile}, tāpēc mēs tos iepriekš neskaitām. Šim mērķim vislabāk der {pick_name}.",

    # FAQ, related pages, closing
    "faq_title": "Jautājumi un atbildes",
    "related_title": "Uzziniet vairāk",
    "related": {
        "platform": "Vairāk par {platform}",
        "platforms": "Citās platformās",
        "quantities": "Citi mērķi",
        "modifiers": "Citi veidi, kā augt",
        "articles": "Lasiet tālāk",
        "hubs": "Augiet ar īstiem cilvēkiem platformās",
    },
    # The tools a page can carry ("tool"): they run in the browser, nothing is sent.
    "tools": {
        "calculate": "Aprēķināt",
        "followers": "Sekotāji",
        "avg_likes": "Vidēji patīk atzīmju uz ierakstu",
        "avg_comments": "Vidēji komentāru uz ierakstu",
        "engagement_title": "Jūsu iesaistes rādītājs",
        "engagement_lead": "Cik liela daļa jūsu sekotāju reaģē uz tipisku ierakstu. Ievadiet skaitļus no saviem pēdējiem ierakstiem.",
        "engagement_result": "Jūsu iesaistes rādītājs ir {rate}%.",
        "engagement_note": "Rādītājs aug, kad cilvēkiem, kas jums seko, jūsu ieraksti patiešām rūp. Sekotāji, kas nekad nereaģē, to samazina, lai cik viņu būtu.",
        "growth_title": "Cik ilgi līdz jūsu mērķim?",
        "growth_lead": "Ievadiet, kur esat tagad un kur vēlaties nonākt. Mēs to aprēķinām pēc katras paketes tipiskā mēneša diapazona.",
        "current": "Sekotāji šodien",
        "goal": "Jūsu mērķis",
        "when_first": "parasti jau pirmajā mēnesī",
        "when_range": "parasti {low}–{high} mēneši",
        "when_about": "apmēram {n} mēneši",
        "reached": "Mērķis jau ir sasniegts.",
        "growth_note": "Tipiski diapazoni, nevis solījums: īsti cilvēki paši izlemj, vai jums sekot.",
    },
    # Eyebrow above the headline of pages outside the platform x service grid (by "kind").
    "article_eyebrows": {
        "guide": "Ceļvedis",
        "alternative": "Salīdzinājums",
        "payment": "Maksājumi",
        "agency": "Izaugsmes aģentūra",
        "tool": "Rīks",
        "intent": "Tieša atbilde",
    },
    "cta_title": "Gatavi augt platformā {platform}?",
    "cta_text": "Izvēlieties paketi, un mēs sāksim jūsu kampaņu. Pārējo izlemj īsti cilvēki, un jūsu pārskats rāda, ko mēs izmērījām.",

    # Platform hubs
    "services_title": "Ko mēs audzējam platformā {platform}",
    "services_lead": "Viena pakete atnes to visu, no tiem pašiem īstajiem cilvēkiem.",
    "teasers": {
        "audience": "Īsti cilvēki, kas atklāj jūsu {profile} un izvēlas {follow}.",
        "likes": "Patīk atzīmes no cilvēkiem, kuri ar prieku skatās jūsu {content}.",
        "views": "Skatījumi no cilvēkiem, kas paši izvēlas skatīties, nekad no skriptiem.",
        "comments": "Komentāri, ko īsti cilvēki raksta saviem vārdiem.",
    },
    "explore": "Apskatīt",
    "in_package": "Katrā paketē",
    "goals_title": "Vairāk veidu, kā augt platformā {platform}",
    "other_hubs_title": "Mēs palīdzam augt arī",
}
