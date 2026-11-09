"""Croatian UI of the money pages: section titles and the blocks every page shares (mirrors en/ui.py).

Forms of the per-platform words, chosen so every sentence below stays grammatical:
    {audience} nominative plural (pratitelji / pretplatnici)
    {follow}   infinitive with its clitic, after "odlučiti" (vas pratiti / se pretplatiti)
    {profile}  masculine, nominative = accusative (profil / kanal), after "vaš"
    {handle}   the bare noun phrase (korisničko ime / identifikator kanala)
    {content}  accusative plural (objave / videozapise)
    {service}  genitive plural, after a number (pratitelja, lajkova...)
"""

UI = {
    # Words that change with the platform or the service
    "audience": {"instagram": "pratitelji", "tiktok": "pratitelji", "youtube": "pretplatnici"},
    "follow": {"instagram": "vas pratiti", "tiktok": "vas pratiti", "youtube": "se pretplatiti"},
    "profile": {"instagram": "profil", "tiktok": "profil", "youtube": "kanal"},
    "handle": {"instagram": "korisničko ime", "tiktok": "korisničko ime", "youtube": "identifikator kanala"},
    "content": {"instagram": "objave", "tiktok": "videozapise", "youtube": "videozapise"},
    "service_names": {"followers": "Pratitelji", "subscribers": "Pretplatnici", "likes": "Lajkovi",
                      "views": "Pregledi", "comments": "Komentari"},
    "service_words": {"followers": "pratitelja", "subscribers": "pretplatnika", "likes": "lajkova",
                      "views": "pregleda", "comments": "komentara"},

    # Page chrome
    "home": "Početna",
    "crumbs_label": "Putanja stranice",
    "eyebrow": "{platform} · {service_name}",
    "eyebrow_hub": "{platform} · rast",
    "cta": "Počnite s paketom {pick_name}",
    "cta_more": "Pogledajte sve pakete",
    "trust": ["Stvarni ljudi, nikad botovi", "Nikad ne tražimo vašu lozinku", "Mjesečno, otkazivanje bilo kada"],
    "product_name": "Paketi rasta za {platform}",
    "sticky_cta": "Počnite",

    # Packages
    "packages_title": "Odaberite svoj paket",
    "packages_lead": "Tri mjesečna paketa. Novi {audience}, lajkovi, pregledi i komentari stižu zajedno, od istih stvarnih ljudi.",
    "packages_note": "Tipični mjesečni rasponi, a ne fiksan broj: vaši novi {audience} stvarni su ljudi koji su sami odlučili {follow}, pa je svaki mjesec malo drukčiji.",

    # What's included: the page's own service comes first, then the rest in this order.
    "included_title": "Što je uključeno",
    "included_lead": "Svaki paket donosi cijelu sliku, od istih stvarnih ljudi.",
    "included_items": {
        "audience": ("Novi {audience}", "Stvarni ljudi koji su otkrili vaš {profile} i odlučili {follow}. Obično {starter_audience} mjesečno uz {starter_name}."),
        "likes": ("Lajkovi od istih ljudi", "Obično {starter_likes} mjesečno uz {starter_name}, za {content} koje im se sviđaju."),
        "comments": ("Komentari njihovim riječima", "Obično {starter_comments} mjesečno uz {starter_name}. Pišu ih ljudi, nikad po scenariju."),
        "views": ("Pregledi koji dolaze s time", "Isti ljudi sami gledaju vaše {content}. Preglede ne brojimo unaprijed: iza svakog stoji osoba."),
        "days": ("Raspoređeno na 30 dana", "Pomalo svaki dan, s lokacije koju odaberete. Nikad sve odjednom."),
        "dashboard": ("Vaša nadzorna ploča", "Ono što smo izmjerili, dan po dan: posjeti iz vaše kampanje i novi {audience} koje su doveli."),
    },

    # How it works: the subscription, step by step
    "steps_title": "Kako funkcionira",
    "steps_lead": "Mjesečna pretplata: vi birate paket, mi vodimo kampanju, a stvarni ljudi odlučuju.",
    "steps": [
        ("Odaberite paket", "{starter_name}, {rising_name} ili {pro_name}, uz mjesečnu naplatu. Otkazati možete bilo kada u svom računu."),
        ("Pokrećemo vašu kampanju", "Javite nam {handle} na platformi {platform} i odakle bi trebala dolaziti vaša publika. Nikad ne tražimo vašu lozinku."),
        ("Stvarni ljudi otkrivaju vaš {profile}", "Vaš {profile} svaki dan prikazujemo stvarnim ljudima. Oni kojima se svidi ono što vide sami odluče {follow}, lajkati i komentirati."),
        ("Nadzorna ploča pokazuje što smo izmjerili", "Posjeti iz vaše kampanje i novi {audience} koje su doveli, dan po dan. Izmjerene brojke, nikad nagađanja."),
    ],

    # Real people vs bots / instant
    "compare_title": "Stvarni ljudi, a ne botovi",
    "compare_lead": "Instant znači botove: nijedna stvarna osoba ne odluči {follow} nekoliko sekundi nakon plaćanja.",
    "compare_cols": ("Što se mijenja", "Instant usluge i botovi", "Growsterr"),
    "compare": [
        ("Tko su oni", "Botovi i lažni profili", "Stvarni ljudi koji su odlučili {follow}"),
        ("Brzina", "Tisuće u nekoliko minuta", "Pomalo svaki dan, cijeli mjesec"),
        ("Lajkovi i komentari", "Prodaju se zasebno, od još botova", "Od istih ljudi, unutar vašeg paketa"),
        ("Vaš doseg", "Tiho pada: publika koja nikad ne reagira govori platformi {platform} da vaše {content} ne vrijedi prikazivati", "Raste s ljudima koji gledaju, lajkaju i vraćaju se"),
        ("Vaša lozinka", "Često je traže", "Nikad"),
        ("Što vidite", "Broj koji može nestati u sljedećem čišćenju", "Nadzorna ploča s onim što smo izmjerili"),
    ],

    # Quantity pages: how a monthly package gets you to the goal
    "quantity_title": "Kako doći do {quantity} {service}",
    "quantity_lead": "Ne prodajemo fiksni paket od {quantity}. Stvarni ljudi odlučuju sami, pa vas mjesečni paket onamo dovodi prirodnim tempom.",
    "pace_title": "Tipičan tempo uz {pick_name}",
    "pace_month": "{n}. mjesec",
    "pace_goal": "Cilj: {quantity}",
    "pace_note": "Tipični rasponi prema onome što stvarni ljudi rade, nikad obećanje. Neki mjeseci donesu više, neki manje.",
    "by_plan_title": "Vrijeme do {quantity}, po paketu",
    "a_month": "{range} mjesečno",
    "when_first": "obično već u prvom mjesecu",
    "when_about": "obično oko {n}. mjeseca",
    "when_range": "obično između {low}. i {high}. mjeseca",
    "views_pace": "Pregledi dolaze od istih stvarnih ljudi koji otkriju vaš {profile}, pa ih ne brojimo unaprijed. {pick_name} je paket koji najbolje odgovara ovom cilju.",

    # FAQ, related pages, closing
    "faq_title": "Pitanja i odgovori",
    "related_title": "Istražite dalje",
    "related": {
        "platform": "Više o platformi {platform}",
        "platforms": "Na drugim platformama",
        "quantities": "Drugi ciljevi",
        "modifiers": "Drugi načini rasta",
        "articles": "Pročitajte i ovo",
        "hubs": "Rastite uz stvarne ljude na",
    },
    # The tools a page can carry ("tool"): they run in the browser, nothing is sent.
    "tools": {
        "calculate": "Izračunaj",
        "followers": "Pratitelji",
        "avg_likes": "Prosječno lajkova po objavi",
        "avg_comments": "Prosječno komentara po objavi",
        "engagement_title": "Vaša stopa angažiranosti",
        "engagement_lead": "Koliko vaših pratitelja reagira na tipičnu objavu. Upišite brojke iz nekoliko svojih zadnjih objava.",
        "engagement_result": "Vaša stopa angažiranosti je {rate} %.",
        "engagement_note": "Stopa raste kad ljudima koji vas prate stvarno nije svejedno što objavljujete. Pratitelji koji nikad ne reagiraju snižavaju je, ma koliko ih bilo.",
        "growth_title": "Koliko do vašeg cilja?",
        "growth_lead": "Upišite gdje ste sada i gdje želite biti. Izračunavamo to iz tipičnog mjesečnog raspona svakog paketa.",
        "current": "Pratitelji danas",
        "goal": "Vaš cilj",
        "when_first": "obično već u prvom mjesecu",
        "when_range": "obično između {low}. i {high}. mjeseca",
        "when_about": "oko {n}. mjeseca",
        "reached": "Već ste ondje.",
        "growth_note": "Tipični rasponi, a ne obećanje: stvarni ljudi sami odlučuju hoće li vas pratiti.",
    },
    # Eyebrow above the headline of pages outside the platform x service grid (by "kind").
    "article_eyebrows": {
        "guide": "Vodič",
        "alternative": "Usporedba",
        "payment": "Plaćanje",
        "agency": "Agencija za rast",
        "tool": "Alat",
        "intent": "Izravan odgovor",
    },
    "cta_title": "Spremni za rast na platformi {platform}?",
    "cta_text": "Odaberite paket i mi pokrećemo vašu kampanju. Ostalo odlučuju stvarni ljudi, a nadzorna ploča pokazuje što smo izmjerili.",

    # Platform hubs
    "services_title": "Što vam donosimo na platformi {platform}",
    "services_lead": "Jedan paket donosi sve to, od istih stvarnih ljudi.",
    "teasers": {
        "audience": "Stvarni ljudi koji otkriju vaš {profile} i odluče {follow}.",
        "likes": "Lajkovi ljudi koji rado gledaju vaše {content}.",
        "views": "Pregledi ljudi koji sami odluče gledati, nikad iz skripti.",
        "comments": "Komentari koje pišu stvarni ljudi, svojim riječima.",
    },
    "explore": "Istražite",
    "in_package": "U svakom paketu",
    "goals_title": "Još načina za rast na platformi {platform}",
    "other_hubs_title": "Rast nudimo i na",
}
