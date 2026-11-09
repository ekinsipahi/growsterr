"""Serbian (Latin script) UI of the money pages: section titles and the blocks every page shares.
Mirrors apps/pages/content/en/ui.py key by key.

The per-platform words are single forms, so every sentence is built around the form given here:
{audience} and {service} are genitive plural (they follow a number or "novih"), {follow} is a
third-person plural present that follows "da" (vas zaprate / se pretplate), {profile} is masculine
(profil / kanal), {content} is nominative plural and only ever the subject of its clause.
"""

UI = {
    # Words that change with the platform or the service
    "audience": {"instagram": "pratilaca", "tiktok": "pratilaca", "youtube": "pretplatnika"},
    "follow": {"instagram": "vas zaprate", "tiktok": "vas zaprate", "youtube": "se pretplate"},
    "profile": {"instagram": "profil", "tiktok": "profil", "youtube": "kanal"},
    "handle": {"instagram": "korisničko ime", "tiktok": "korisničko ime", "youtube": "identifikator kanala"},
    "content": {"instagram": "objave", "tiktok": "video snimci", "youtube": "video snimci"},
    "service_names": {"followers": "Pratioci", "subscribers": "Pretplatnici", "likes": "Lajkovi",
                      "views": "Pregledi", "comments": "Komentari"},
    "service_words": {"followers": "pratilaca", "subscribers": "pretplatnika", "likes": "lajkova",
                      "views": "pregleda", "comments": "komentara"},

    # Page chrome
    "home": "Početna",
    "crumbs_label": "Navigaciona putanja",
    "eyebrow": "{platform} · {service_name}",
    "eyebrow_hub": "Rast na mreži {platform}",
    "cta": "Počnite sa paketom {pick_name}",
    "cta_more": "Pogledajte sve pakete",
    "trust": ["Pravi ljudi, nikada botovi", "Nikada ne tražimo vašu lozinku", "Mesečno, otkazivanje bilo kada"],
    "product_name": "Paketi za rast na mreži {platform}",
    "sticky_cta": "Počnite",

    # Packages
    "packages_title": "Izaberite paket",
    "packages_lead": "Tri mesečna paketa. Svaki donosi priliv novih {audience}, a uz njih lajkove, preglede i komentare, od istih pravih ljudi.",
    "packages_note": "Tipični mesečni rasponi, a ne fiksan broj. Broj novih {audience} zavisi od pravih ljudi koji sami odluče da {follow}, pa je svaki mesec malo drugačiji.",

    # What's included: the page's own service comes first, then the rest in this order.
    "included_title": "Šta je uključeno",
    "included_lead": "Svaki paket donosi celu sliku, od istih pravih ljudi.",
    "included_items": {
        "audience": ("Priliv novih {audience}", "Pravi ljudi koji su otkrili vaš {profile} i odlučili da {follow}. Uz {starter_name} obično {starter_audience} mesečno."),
        "likes": ("Lajkovi od istih ljudi", "Uz {starter_name} obično {starter_likes} mesečno, tamo gde se ljudima zaista dopadnu {content}."),
        "comments": ("Komentari njihovim rečima", "Uz {starter_name} obično {starter_comments} mesečno. Pišu ih ljudi, nikada po scenariju."),
        "views": ("Pregledi koji stižu uz to", "Isti ljudi sami biraju šta gledaju, pa {content} dobijaju i preglede. Preglede ne brojimo unapred: svaki je jedna osoba."),
        "days": ("Raspoređeno na 30 dana", "Pomalo svakog dana, sa lokacije koju izaberete. Nikada sve odjednom."),
        "dashboard": ("Vaša kontrolna tabla", "Ono što smo izmerili, dan po dan: posete iz vaše kampanje i priliv novih {audience} koji su one donele."),
    },

    # How it works: the subscription, step by step
    "steps_title": "Kako funkcioniše",
    "steps_lead": "Mesečna pretplata: vi birate paket, mi vodimo kampanju, a pravi ljudi odlučuju.",
    "steps": [
        ("Izaberite paket", "{starter_name}, {rising_name} ili {pro_name}, uz mesečnu naplatu. Otkažite bilo kada iz svog naloga."),
        ("Pokrećemo vašu kampanju", "Javite nam {handle} na mreži {platform} i odakle treba da dolazi vaša publika. Nikada ne tražimo vašu lozinku."),
        ("Pravi ljudi otkrivaju vaš {profile}", "Vaš {profile} se svakog dana prikazuje pravim ljudima. Oni kojima se dopadne ono što vide sami odluče da {follow}, lajkuju i komentarišu."),
        ("Kontrolna tabla pokazuje šta smo izmerili", "Posete iz vaše kampanje i priliv novih {audience} koji su one donele, dan po dan. Izmerene brojke, nikada nagađanja."),
    ],

    # Real people vs bots / instant
    "compare_title": "Pravi ljudi, a ne botovi",
    "compare_lead": "„Odmah” znači botovi: pravi ljudi ne odluče da {follow} nekoliko sekundi posle uplate.",
    "compare_cols": ("Šta se menja", "Servisi za „odmah” i botove", "Growsterr"),
    "compare": [
        ("Ko su oni", "Botovi i lažni profili", "Pravi ljudi koji su odlučili da {follow}"),
        ("Brzina", "Hiljade za nekoliko minuta", "Pomalo svakog dana, ceo mesec"),
        ("Lajkovi i komentari", "Prodaju se zasebno, od još botova", "Od istih ljudi, u okviru vašeg paketa"),
        ("Vaš doseg", "Tiho opada: publika koja nikad ne reaguje govori mreži {platform} da {content} ne zaslužuju prikazivanje", "Raste uz ljude koji gledaju, lajkuju i vraćaju se"),
        ("Vaša lozinka", "Često je traže", "Nikada"),
        ("Šta vidite", "Broj koji može da nestane u sledećem čišćenju", "Kontrolna tabla sa onim što smo izmerili"),
    ],

    # Quantity pages: how a monthly package gets you to the goal
    "quantity_title": "Kako do {quantity} {service}",
    "quantity_lead": "Ne prodajemo fiksan paket od {quantity}. Pravi ljudi sami odlučuju, pa vas mesečni paket do cilja dovodi prirodnim tempom.",
    "pace_title": "Tipičan tempo uz {pick_name}",
    "pace_month": "{n}. mesec",
    "pace_goal": "Cilj: {quantity}",
    "pace_note": "Tipični rasponi prema onome što pravi ljudi rade, nikada obećanje. Neki meseci donesu više, neki manje.",
    "by_plan_title": "Vreme do {quantity}, po paketu",
    "a_month": "{range} mesečno",
    "when_first": "obično već u prvom mesecu",
    "when_about": "obično tokom {n}. meseca",
    "when_range": "obično između {low}. i {high}. meseca",
    "views_pace": "Pregledi stižu od istih pravih ljudi koji otkriju vaš {profile}, pa ih ne brojimo unapred. {pick_name} je paket koji najbolje odgovara ovom cilju.",

    # FAQ, related pages, closing
    "faq_title": "Pitanja i odgovori",
    "related_title": "Istražite dalje",
    "related": {
        "platform": "Još o mreži {platform}",
        "platforms": "Na drugim mrežama",
        "quantities": "Drugi ciljevi",
        "modifiers": "Drugi načini rasta",
        "articles": "Pročitajte i ovo",
        "hubs": "Rastite uz prave ljude na mrežama",
    },
    # The tools a page can carry ("tool"): they run in the browser, nothing is sent.
    "tools": {
        "calculate": "Izračunaj",
        "followers": "Pratioci",
        "avg_likes": "Prosečan broj lajkova po objavi",
        "avg_comments": "Prosečan broj komentara po objavi",
        "engagement_title": "Vaša stopa angažovanja",
        "engagement_lead": "Koliko vaših pratilaca reaguje na tipičnu objavu. Unesite brojke sa nekoliko poslednjih objava.",
        "engagement_result": "Vaša stopa angažovanja je {rate}%.",
        "engagement_note": "Stopa raste kada je ljudima koji vas prate zaista stalo do vaših objava. Pratioci koji nikada ne reaguju je snižavaju, bez obzira na to koliko ih ima.",
        "growth_title": "Koliko vam treba do cilja?",
        "growth_lead": "Unesite gde ste sada i gde želite da stignete. Računamo prema tipičnom mesečnom rasponu svakog paketa.",
        "current": "Pratioci danas",
        "goal": "Vaš cilj",
        "when_first": "obično već u prvom mesecu",
        "when_range": "obično između {low}. i {high}. meseca",
        "when_about": "otprilike tokom {n}. meseca",
        "reached": "Već ste stigli do cilja.",
        "growth_note": "Tipični rasponi, a ne obećanje: pravi ljudi sami odlučuju da li će vas zapratiti.",
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
    "cta_title": "Spremni za rast na mreži {platform}?",
    "cta_text": "Izaberite paket i mi pokrećemo vašu kampanju. Ostalo odlučuju pravi ljudi, a kontrolna tabla pokazuje šta smo izmerili.",

    # Platform hubs
    "services_title": "Šta razvijamo na mreži {platform}",
    "services_lead": "Jedan paket donosi sve to, od istih pravih ljudi.",
    "teasers": {
        "audience": "Pravi ljudi koji otkriju vaš {profile} i odluče da {follow}.",
        "likes": "Lajkovi od ljudi kojima se {content} zaista dopadnu.",
        "views": "Pregledi od ljudi koji sami biraju da gledaju, nikada od skripti.",
        "comments": "Komentari koje pišu pravi ljudi, svojim rečima.",
    },
    "explore": "Istražite",
    "in_package": "U svakom paketu",
    "goals_title": "Još načina za rast na mreži {platform}",
    "other_hubs_title": "Rast i na drugim mrežama",
}
