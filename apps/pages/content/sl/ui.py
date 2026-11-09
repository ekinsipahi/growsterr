"""Slovenian UI of the money pages (formal "vi"): section titles and the blocks every page shares.
Mirrors apps/pages/content/en/ui.py key by key.

The platform words are single forms, so every sentence is built around them:
    {audience} genitive plural (sledilcev, naročnikov): "novih {audience}", "vsak od vaših novih {audience}"
    {follow} accusative noun after "odločiti se za" (sledenje, naročnino)
    {profile} nominative = accusative (profil, kanal) · {handle} accusative (uporabniško ime, identifikator kanala)
    {content} accusative plural (objave, videe) · {service} genitive plural: "do {quantity} {service}"
"""

UI = {
    # Words that change with the platform or the service
    "audience": {"instagram": "sledilcev", "tiktok": "sledilcev", "youtube": "naročnikov"},
    "follow": {"instagram": "sledenje", "tiktok": "sledenje", "youtube": "naročnino"},
    "profile": {"instagram": "profil", "tiktok": "profil", "youtube": "kanal"},
    "handle": {"instagram": "uporabniško ime", "tiktok": "uporabniško ime", "youtube": "identifikator kanala"},
    "content": {"instagram": "objave", "tiktok": "videe", "youtube": "videe"},
    "service_names": {"followers": "Sledilci", "subscribers": "Naročniki", "likes": "Všečki",
                      "views": "Ogledi", "comments": "Komentarji"},
    "service_words": {"followers": "sledilcev", "subscribers": "naročnikov", "likes": "všečkov",
                      "views": "ogledov", "comments": "komentarjev"},

    # Page chrome
    "home": "Domov",
    "crumbs_label": "Pot do strani",
    "eyebrow": "{platform} · {service_name}",
    "eyebrow_hub": "{platform} · rast",
    "cta": "Začnite s paketom {pick_name}",
    "cta_more": "Oglejte si vse pakete",
    "trust": ["Resnični ljudje, nikoli boti", "Nikoli ne zahtevamo vašega gesla", "Mesečno, preklic kadar koli"],
    "product_name": "Paketi za rast na platformi {platform}",
    "sticky_cta": "Začnite",

    # Packages
    "packages_title": "Izberite svoj paket",
    "packages_lead": "Trije mesečni paketi. Vsak prinaša pritok novih {audience}, všečkov, ogledov in komentarjev, vse od istih resničnih ljudi.",
    "packages_note": "Tipični mesečni razponi, ne fiksno število: vsak od vaših novih {audience} je resnična oseba, ki se je sama odločila za {follow}, zato je vsak mesec malo drugačen.",

    # What's included: the page's own service comes first, then the rest in this order.
    "included_title": "Kaj je vključeno",
    "included_lead": "Vsak paket prinese celotno sliko, od istih resničnih ljudi.",
    "included_items": {
        "audience": ("Pritok novih {audience}", "Resnični ljudje, ki so odkrili vaš {profile} in se odločili za {follow}. Običajno {starter_audience} na mesec s paketom {starter_name}."),
        "likes": ("Všečki istih ljudi", "Običajno {starter_likes} na mesec s paketom {starter_name}, za {content}, ki so jim všeč."),
        "comments": ("Komentarji, napisani po svoje", "Običajno {starter_comments} na mesec s paketom {starter_name}. Pišejo jih ljudje, nikoli po scenariju."),
        "views": ("Ogledi, ki pridejo zraven", "Isti ljudje si sami ogledajo vaše {content}. Ogledov ne štejemo vnaprej: vsak je človek."),
        "days": ("Razporejeno čez 30 dni", "Vsak dan malo, z lokacije, ki jo izberete. Nikoli vse naenkrat."),
        "dashboard": ("Vaša nadzorna plošča", "Kar smo izmerili, dan za dnem: obiski iz vaše kampanje in število novih {audience}, ki so jih prinesli."),
    },

    # How it works: the subscription, step by step
    "steps_title": "Kako deluje",
    "steps_lead": "Mesečna naročnina: vi izberete paket, mi vodimo kampanjo, odločajo resnični ljudje.",
    "steps": [
        ("Izberite paket", "{starter_name}, {rising_name} ali {pro_name}, z mesečnim obračunom. Prekličete lahko kadar koli v svojem računu."),
        ("Začnemo vašo kampanjo", "Sporočite nam {handle} za {platform} in od kod naj prihaja vaše občinstvo. Nikoli ne zahtevamo vašega gesla."),
        ("Resnični ljudje odkrijejo vaš {profile}", "Vsak dan vaš {profile} pokažemo resničnim ljudem. Kdor ga vidi in mu je všeč, se sam odloči za {follow}, všečke in komentarje."),
        ("Nadzorna plošča pokaže, kaj smo izmerili", "Obiski iz vaše kampanje in število novih {audience}, ki so jih prinesli, dan za dnem. Izmerjene številke, nikoli ugibanja."),
    ],

    # Real people vs bots / instant
    "compare_title": "Resnični ljudje, ne boti",
    "compare_lead": "»Takoj« pomeni bote: nobena resnična oseba se ne odloči za {follow} nekaj sekund po plačilu.",
    "compare_cols": ("Kaj se spremeni", "Takojšnje in botovske storitve", "Growsterr"),
    "compare": [
        ("Kdo so", "Boti in lažni profili", "Resnični ljudje, ki so se odločili za {follow}"),
        ("Hitrost", "Tisoče v nekaj minutah", "Vsak dan malo, ves mesec"),
        ("Všečki in komentarji", "Prodani posebej, od še več botov", "Od istih ljudi, v vašem paketu"),
        ("Vaš doseg", "Tiho pada: občinstvo, ki se nikoli ne odzove, platformi {platform} sporoča, naj vaše {content} kaže manj ljudem", "Raste z ljudmi, ki gledajo, všečkajo in se vračajo"),
        ("Vaše geslo", "Pogosto ga zahtevajo", "Nikoli"),
        ("Kaj vidite", "Število, ki lahko izgine ob naslednjem čiščenju", "Nadzorno ploščo z izmerjenimi podatki"),
    ],

    # Quantity pages: how a monthly package gets you to the goal
    "quantity_title": "Kako pridete do {quantity} {service}",
    "quantity_lead": "Številke {quantity} ne prodajamo kot fiksnega paketa. Resnični ljudje se odločajo sami, zato vas mesečni paket tja pripelje v naravnem tempu.",
    "pace_title": "Tipičen tempo s paketom {pick_name}",
    "pace_month": "{n}. mesec",
    "pace_goal": "Cilj: {quantity}",
    "pace_note": "Tipični razponi glede na to, kar počnejo resnični ljudje, nikoli obljuba. Nekateri meseci prinesejo več, drugi manj.",
    "by_plan_title": "Čas do {quantity}, po paketih",
    "a_month": "{range} na mesec",
    "when_first": "običajno že v prvem mesecu",
    "when_about": "običajno okoli {n}. meseca",
    "when_range": "običajno med {low}. in {high}. mesecem",
    "views_pace": "Ogledi prihajajo od istih resničnih ljudi, ki odkrijejo vaš {profile}, zato jih vnaprej ne štejemo. {pick_name} je paket, ki temu cilju najbolj ustreza.",

    # FAQ, related pages, closing
    "faq_title": "Vprašanja in odgovori",
    "related_title": "Raziščite še",
    "related": {
        "platform": "Več o platformi {platform}",
        "platforms": "Na drugih platformah",
        "quantities": "Drugi cilji",
        "modifiers": "Drugi načini rasti",
        "articles": "Preberite še",
        "hubs": "Rastite z resničnimi ljudmi na platformah",
    },
    # The tools a page can carry ("tool"): they run in the browser, nothing is sent.
    "tools": {
        "calculate": "Izračunaj",
        "followers": "Sledilci",
        "avg_likes": "Povprečno število všečkov na objavo",
        "avg_comments": "Povprečno število komentarjev na objavo",
        "engagement_title": "Vaša stopnja zavzetosti",
        "engagement_lead": "Koliko vaših sledilcev se odzove na tipično objavo. Vpišite številke svojih zadnjih nekaj objav.",
        "engagement_result": "Vaša stopnja zavzetosti je {rate} %.",
        "engagement_note": "Stopnja raste, ko je ljudem, ki vam sledijo, res mar za vaše objave. Sledilci, ki se nikoli ne odzovejo, jo znižujejo, ne glede na to, koliko jih je.",
        "growth_title": "Koliko časa do vašega cilja?",
        "growth_lead": "Vpišite, kje ste zdaj in kam želite priti. Izračunamo iz tipičnega mesečnega razpona vsakega paketa.",
        "current": "Sledilci danes",
        "goal": "Vaš cilj",
        "when_first": "običajno že v prvem mesecu",
        "when_range": "običajno med {low}. in {high}. mesecem",
        "when_about": "okoli {n}. meseca",
        "reached": "Tam ste že.",
        "growth_note": "Tipični razponi, ne obljuba: resnični ljudje se sami odločijo, ali vam bodo sledili.",
    },
    # Eyebrow above the headline of pages outside the platform x service grid (by "kind").
    "article_eyebrows": {
        "guide": "Vodnik",
        "alternative": "Primerjava",
        "payment": "Plačila",
        "agency": "Agencija za rast",
        "tool": "Orodje",
        "intent": "Jasen odgovor",
    },
    "cta_title": "Ste pripravljeni na rast na platformi {platform}?",
    "cta_text": "Izberite paket in začnemo vašo kampanjo. O ostalem odločajo resnični ljudje, vaša nadzorna plošča pa pokaže, kaj smo izmerili.",

    # Platform hubs
    "services_title": "Kaj vse raste z nami na platformi {platform}",
    "services_lead": "En paket prinese vse to, od istih resničnih ljudi.",
    "teasers": {
        "audience": "Resnični ljudje, ki odkrijejo vaš {profile} in se odločijo za {follow}.",
        "likes": "Všečki ljudi, ki radi gledajo vaše {content}.",
        "views": "Ogledi ljudi, ki se sami odločijo za ogled, nikoli od skript.",
        "comments": "Komentarji, ki jih resnični ljudje napišejo po svoje.",
    },
    "explore": "Raziščite",
    "in_package": "V vsakem paketu",
    "goals_title": "Več načinov za rast na platformi {platform}",
    "other_hubs_title": "Pomagamo rasti tudi na platformah",
}
