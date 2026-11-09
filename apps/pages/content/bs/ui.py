"""Bosnian UI of the money pages (formal "vi", ijekavian): section titles and the blocks every
page shares. Mirrors apps/pages/content/en/ui.py key by key.

The platform words are fixed forms the sentences are written around: {audience} nominative
plural (pratioci / pretplatnici), {follow} the third person plural after "da" (vas zaprate /
se pretplate), {profile} and {content} accusative (profil / kanal, objave / videe),
{service} genitive plural ("do 1000 pratilaca").
"""

UI = {
    # Words that change with the platform or the service
    "audience": {"instagram": "pratioci", "tiktok": "pratioci", "youtube": "pretplatnici"},
    "follow": {"instagram": "vas zaprate", "tiktok": "vas zaprate", "youtube": "se pretplate"},
    "profile": {"instagram": "profil", "tiktok": "profil", "youtube": "kanal"},
    "handle": {"instagram": "korisničko ime", "tiktok": "korisničko ime", "youtube": "handle kanala"},
    "content": {"instagram": "objave", "tiktok": "videe", "youtube": "videe"},
    "service_names": {"followers": "Pratioci", "subscribers": "Pretplatnici", "likes": "Lajkovi",
                      "views": "Pregledi", "comments": "Komentari"},
    "service_words": {"followers": "pratilaca", "subscribers": "pretplatnika", "likes": "lajkova",
                      "views": "pregleda", "comments": "komentara"},

    # Page chrome
    "home": "Početna",
    "crumbs_label": "Putanja stranice",
    "eyebrow": "{platform} · {service_name}",
    "eyebrow_hub": "Rast na platformi {platform}",
    "cta": "Počnite s paketom {pick_name}",
    "cta_more": "Pogledajte sve pakete",
    "trust": ["Stvarni ljudi, nikada botovi", "Nikada ne tražimo vašu lozinku", "Mjesečno, otkažite kad god želite"],
    "product_name": "Paketi za rast na platformi {platform}",
    "sticky_cta": "Počnite",

    # Packages
    "packages_title": "Odaberite svoj paket",
    "packages_lead": "Tri mjesečna paketa. Novi {audience}, lajkovi, pregledi i komentari dolaze zajedno, od istih stvarnih ljudi.",
    "packages_note": "Tipični mjesečni rasponi, a ne fiksna količina: svi vaši novi {audience} su stvarni ljudi koji su odlučili da {follow}, pa je svaki mjesec malo drugačiji.",

    # What's included: the page's own service comes first, then the rest in this order.
    "included_title": "Šta je uključeno",
    "included_lead": "Svaki paket donosi cijelu sliku, od istih stvarnih ljudi.",
    "included_items": {
        "audience": ("Novi {audience}", "Stvarni ljudi koji su otkrili vaš {profile} i odlučili da {follow}. Obično {starter_audience} mjesečno uz {starter_name}."),
        "likes": ("Lajkovi od istih ljudi", "Obično {starter_likes} mjesečno uz {starter_name}, na vaše {content} koje vole."),
        "comments": ("Komentari njihovim riječima", "Obično {starter_comments} mjesečno uz {starter_name}. Pišu ih ljudi, nikada unaprijed pripremljeni tekstovi."),
        "views": ("Pregledi koji dolaze uz to", "Isti ljudi sami gledaju vaše {content}. Preglede ne brojimo unaprijed: svaki je jedna osoba."),
        "days": ("Raspoređeno na 30 dana", "Pomalo svaki dan, s lokacije koju odaberete. Nikada sve odjednom."),
        "dashboard": ("Vaša kontrolna ploča", "Ono što smo izmjerili, dan po dan: posjete iz vaše kampanje i novi {audience} koji su iz njih došli."),
    },

    # How it works: the subscription, step by step
    "steps_title": "Kako to funkcioniše",
    "steps_lead": "Mjesečna pretplata: vi birate paket, mi vodimo kampanju, a stvarni ljudi odlučuju.",
    "steps": [
        ("Odaberite paket", "{starter_name}, {rising_name} ili {pro_name}, uz mjesečnu naplatu. Otkažite kad god želite na svom računu."),
        ("Pokrećemo vašu kampanju", "Pošaljite nam {handle} za {platform} i recite nam odakle treba doći vaša publika. Nikada ne tražimo vašu lozinku."),
        ("Stvarni ljudi otkrivaju vaš {profile}", "Svaki dan se vaš {profile} prikazuje stvarnim ljudima. Oni kojima se svidi ono što vide sami odluče da {follow}, lajkuju i komentarišu."),
        ("Kontrolna ploča pokazuje šta smo izmjerili", "Posjete iz vaše kampanje i novi {audience} koji su iz njih došli, dan po dan. Izmjereni brojevi, nikada nagađanja."),
    ],

    # Real people vs bots / instant
    "compare_title": "Stvarni ljudi, ne botovi",
    "compare_lead": "Instant znači botovi: stvarni ljudi ne odluče da {follow} nekoliko sekundi nakon uplate.",
    "compare_cols": ("Šta se mijenja", "Instant i bot usluge", "Growsterr"),
    "compare": [
        ("Ko su oni", "Botovi i lažni profili", "Stvarni ljudi koji su odlučili da {follow}"),
        ("Brzina", "Hiljade za nekoliko minuta", "Pomalo svaki dan, cijeli mjesec"),
        ("Lajkovi i komentari", "Prodaju se zasebno, od još botova", "Od istih ljudi, u okviru vašeg paketa"),
        ("Vaš doseg", "Tiho pada: publika koja nikad ne reaguje govori platformi {platform} da ne vrijedi prikazivati vaše {content}", "Raste s ljudima koji gledaju, lajkuju i vraćaju se"),
        ("Vaša lozinka", "Često je traže", "Nikada"),
        ("Šta vidite", "Broj koji može nestati pri sljedećem čišćenju", "Kontrolna ploča s onim što smo izmjerili"),
    ],

    # Quantity pages: how a monthly package gets you to the goal
    "quantity_title": "Kako doći do {quantity} {service}",
    "quantity_lead": "Ne prodajemo fiksni paket od {quantity}. Stvarni ljudi odlučuju sami, pa vas mjesečni paket do cilja dovodi prirodnim tempom.",
    "pace_title": "Tipičan tempo uz {pick_name}",
    "pace_month": "Mjesec {n}",
    "pace_goal": "Cilj: {quantity}",
    "pace_note": "Tipični rasponi na osnovu onoga što stvarni ljudi rade, nikada obećanje. Neki mjeseci donesu više, neki manje.",
    "by_plan_title": "Vrijeme do {quantity}, po paketu",
    "a_month": "{range} mjesečno",
    "when_first": "obično već u prvom mjesecu",
    "when_about": "obično oko {n} mj.",
    "when_range": "obično {low}–{high} mj.",
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
        "followers": "Pratioci",
        "avg_likes": "Prosječan broj lajkova po objavi",
        "avg_comments": "Prosječan broj komentara po objavi",
        "engagement_title": "Vaša stopa angažmana",
        "engagement_lead": "Koliko vaših pratilaca reaguje na tipičnu objavu. Unesite brojeve s nekoliko posljednjih objava.",
        "engagement_result": "Vaša stopa angažmana je {rate}%.",
        "engagement_note": "Stopa raste kada je ljudima koji vas prate zaista stalo do vaših objava. Pratioci koji nikad ne reaguju je snižavaju, koliko god ih bilo.",
        "growth_title": "Koliko vam treba do cilja?",
        "growth_lead": "Unesite gdje ste sada i gdje želite biti. Računamo na osnovu tipičnog mjesečnog raspona svakog paketa.",
        "current": "Pratioci danas",
        "goal": "Vaš cilj",
        "when_first": "obično već u prvom mjesecu",
        "when_range": "obično {low}–{high} mj.",
        "when_about": "oko {n} mj.",
        "reached": "Već ste stigli do cilja.",
        "growth_note": "Tipični rasponi, a ne obećanje: stvarni ljudi sami odlučuju da li će vas pratiti.",
    },
    # Eyebrow above the headline of pages outside the platform x service grid (by "kind").
    "article_eyebrows": {
        "guide": "Vodič",
        "alternative": "Poređenje",
        "payment": "Plaćanje",
        "agency": "Agencija za rast",
        "tool": "Alat",
        "intent": "Direktan odgovor",
    },
    "cta_title": "Spremni za rast na platformi {platform}?",
    "cta_text": "Odaberite paket i mi pokrećemo vašu kampanju. Ostalo odlučuju stvarni ljudi, a kontrolna ploča pokazuje šta smo izmjerili.",

    # Platform hubs
    "services_title": "Šta razvijamo na platformi {platform}",
    "services_lead": "Jedan paket donosi sve to, od istih stvarnih ljudi.",
    "teasers": {
        "audience": "Stvarni ljudi koji otkriju vaš {profile} i odluče da {follow}.",
        "likes": "Lajkovi od ljudi koji rado gledaju vaše {content}.",
        "views": "Pregledi od ljudi koji sami odluče gledati, nikada od skripti.",
        "comments": "Komentari koje pišu stvarni ljudi, svojim riječima.",
    },
    "explore": "Istražite",
    "in_package": "U svakom paketu",
    "goals_title": "Više načina za rast na platformi {platform}",
    "other_hubs_title": "Također razvijamo",
}
