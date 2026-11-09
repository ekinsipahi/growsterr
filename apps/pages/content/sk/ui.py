"""Slovak UI of the money pages: section titles and the blocks every page shares (mirrors en/ui.py).

Word forms, chosen so every sentence below stays grammatical:
    {audience} nominative plural (sledovatelia / odberatelia) · {follow} infinitive with its object
    (vás sledovať / vás odoberať) · {profile} nominative = accusative (profil / kanál)
    {content} nominative = accusative plural (príspevky / videá) · {service} genitive plural,
    because it follows {quantity} ("1 000 sledovateľov").
"""

UI = {
    # Words that change with the platform or the service
    "audience": {"instagram": "sledovatelia", "tiktok": "sledovatelia", "youtube": "odberatelia"},
    "follow": {"instagram": "vás sledovať", "tiktok": "vás sledovať", "youtube": "vás odoberať"},
    "profile": {"instagram": "profil", "tiktok": "profil", "youtube": "kanál"},
    "handle": {"instagram": "používateľské meno", "tiktok": "používateľské meno", "youtube": "identifikátor kanála"},
    "content": {"instagram": "príspevky", "tiktok": "videá", "youtube": "videá"},
    "service_names": {"followers": "Sledovatelia", "subscribers": "Odberatelia", "likes": "Lajky",
                      "views": "Zhliadnutia", "comments": "Komentáre"},
    "service_words": {"followers": "sledovateľov", "subscribers": "odberateľov", "likes": "lajkov",
                      "views": "zhliadnutí", "comments": "komentárov"},

    # Page chrome
    "home": "Domov",
    "crumbs_label": "Navigačná cesta",
    "eyebrow": "{platform} · {service_name}",
    "eyebrow_hub": "{platform}: rast",
    "cta": "Začnite s balíkom {pick_name}",
    "cta_more": "Zobraziť všetky balíky",
    "trust": ["Skutoční ľudia, nikdy boty", "Nikdy nežiadame vaše heslo", "Mesačne, zrušiť môžete kedykoľvek"],
    "product_name": "Balíky rastu pre {platform}",
    "sticky_cta": "Začať",

    # Packages
    "packages_title": "Vyberte si balík",
    "packages_lead": "Tri mesačné balíky. Noví {audience}, lajky, zhliadnutia a komentáre prichádzajú spolu, od tých istých skutočných ľudí.",
    "packages_note": "Typické mesačné rozpätia, nie pevný počet: vaši noví {audience} sú skutoční ľudia, ktorí sa sami rozhodli {follow}, takže každý mesiac je trochu iný.",

    # What's included: the page's own service comes first, then the rest in this order.
    "included_title": "Čo je v balíku",
    "included_lead": "Každý balík prináša celý obraz, od tých istých skutočných ľudí.",
    "included_items": {
        "audience": ("Noví {audience}", "Skutoční ľudia, ktorí objavili váš {profile} a rozhodli sa {follow}. S balíkom {starter_name} typicky {starter_audience} mesačne."),
        "likes": ("Lajky od tých istých ľudí", "Ľudia lajkujú {content}, ktoré ich bavia: s balíkom {starter_name} typicky {starter_likes} mesačne."),
        "comments": ("Komentáre vlastnými slovami", "S balíkom {starter_name} typicky {starter_comments} mesačne. Píšu ich ľudia, nikdy nie podľa scenára."),
        "views": ("Zhliadnutia prichádzajú s nimi", "Tí istí ľudia si sami pozerajú vaše {content}. Zhliadnutia vopred nepočítame: za každým je človek."),
        "days": ("Rozložené na 30 dní", "Každý deň trochu, z lokality, ktorú si vyberiete. Nikdy nie všetko naraz."),
        "dashboard": ("Váš prehľad", "Čo sme namerali, deň po dni: návštevy z vašej kampane a noví {audience}, ktorých priniesli."),
    },

    # How it works: the subscription, step by step
    "steps_title": "Ako to funguje",
    "steps_lead": "Mesačné predplatné: vy si vyberiete balík, my spustíme kampaň, skutoční ľudia rozhodnú.",
    "steps": [
        ("Vyberte si balík", "{starter_name}, {rising_name} alebo {pro_name}, účtované mesačne. Zrušiť môžete kedykoľvek vo svojom účte."),
        ("Spustíme vašu kampaň", "Pošlite nám {handle} na platforme {platform} a napíšte, odkiaľ má pochádzať vaše publikum. Vaše heslo nikdy nežiadame."),
        ("Skutoční ľudia objavia váš {profile}", "Váš {profile} sa každý deň zobrazuje skutočným ľuďom. Komu sa páči, čo vidí, začne {follow}, dávať lajky a komentovať, celkom sám od seba."),
        ("Váš prehľad ukazuje, čo sme namerali", "Návštevy z vašej kampane a noví {audience}, ktorých priniesli, deň po dni. Namerané čísla, nikdy nie odhady."),
    ],

    # Real people vs bots / instant
    "compare_title": "Skutoční ľudia, nie boty",
    "compare_lead": "Okamžite znamená boty: žiadny skutočný človek sa nerozhodne {follow} pár sekúnd po platbe.",
    "compare_cols": ("Čo sa mení", "Okamžité a botové služby", "Growsterr"),
    "compare": [
        ("Kto to je", "Boty a falošné profily", "Skutoční ľudia, ktorí sa rozhodli {follow}"),
        ("Rýchlosť", "Tisíce za pár minút", "Každý deň trochu, celý mesiac"),
        ("Lajky a komentáre", "Predávané zvlášť, od ďalších botov", "Od tých istých ľudí, v rámci vášho balíka"),
        ("Váš dosah", "Potichu klesá: publikum, ktoré nereaguje, hovorí platforme {platform}, že vaše {content} nestoja za zobrazenie", "Rastie s ľuďmi, ktorí pozerajú, lajkujú a vracajú sa"),
        ("Vaše heslo", "Často ho žiadajú", "Nikdy"),
        ("Čo vidíte", "Číslo, ktoré môže zmiznúť pri ďalšom čistení", "Prehľad toho, čo sme namerali"),
    ],

    # Quantity pages: how a monthly package gets you to the goal
    "quantity_title": "Ako dosiahnete {quantity} {service}",
    "quantity_lead": "Nepredávame pevný balík {quantity} {service}. Skutoční ľudia sa rozhodujú sami, takže mesačný balík vás k cieľu dovedie prirodzeným tempom.",
    "pace_title": "Typické tempo s balíkom {pick_name}",
    "pace_month": "{n}. mesiac",
    "pace_goal": "Cieľ: {quantity}",
    "pace_note": "Typické rozpätia podľa toho, čo robia skutoční ľudia, nikdy nie sľub. Niektoré mesiace prinesú viac, iné menej.",
    "by_plan_title": "Čas do {quantity} podľa balíka",
    "a_month": "{range} mesačne",
    "when_first": "zvyčajne už v prvom mesiaci",
    "when_about": "zvyčajne okolo {n}. mesiaca",
    "when_range": "zvyčajne medzi {low}. a {high}. mesiacom",
    "views_pace": "Zhliadnutia prichádzajú od tých istých skutočných ľudí, ktorí objavia váš {profile}, preto ich vopred nepočítame. {pick_name} je balík, ktorý k tomuto cieľu sedí najlepšie.",

    # FAQ, related pages, closing
    "faq_title": "Otázky a odpovede",
    "related_title": "Pozrite si aj",
    "related": {
        "platform": "Ďalšie na platforme {platform}",
        "platforms": "Na iných platformách",
        "quantities": "Iné ciele",
        "modifiers": "Ďalšie spôsoby rastu",
        "articles": "Čítajte ďalej",
        "hubs": "Rastite so skutočnými ľuďmi aj tu",
    },
    # The tools a page can carry ("tool"): they run in the browser, nothing is sent.
    "tools": {
        "calculate": "Vypočítať",
        "followers": "Sledovatelia",
        "avg_likes": "Priemerný počet lajkov na príspevok",
        "avg_comments": "Priemerný počet komentárov na príspevok",
        "engagement_title": "Vaša miera angažovanosti",
        "engagement_lead": "Koľko vašich sledovateľov reaguje na bežný príspevok. Zadajte čísla z niekoľkých posledných príspevkov.",
        "engagement_result": "Vaša miera angažovanosti je {rate} %.",
        "engagement_note": "Miera rastie, keď ľuďom, ktorí vás sledujú, na vašich príspevkoch naozaj záleží. Sledovatelia, ktorí nikdy nereagujú, ju znižujú, nech ich je koľkokoľvek.",
        "growth_title": "Za ako dlho dosiahnete svoj cieľ?",
        "growth_lead": "Zadajte, kde ste teraz a kam sa chcete dostať. Vypočítame to z typického mesačného rozpätia každého balíka.",
        "current": "Sledovatelia dnes",
        "goal": "Váš cieľ",
        "when_first": "zvyčajne už v prvom mesiaci",
        "when_range": "zvyčajne medzi {low}. a {high}. mesiacom",
        "when_about": "približne okolo {n}. mesiaca",
        "reached": "Svoj cieľ ste už dosiahli.",
        "growth_note": "Typické rozpätia, nie sľub: skutoční ľudia sa sami rozhodujú, či vás budú sledovať.",
    },
    # Eyebrow above the headline of pages outside the platform x service grid (by "kind").
    "article_eyebrows": {
        "guide": "Návod",
        "alternative": "Porovnanie",
        "payment": "Platby",
        "agency": "Rastová agentúra",
        "tool": "Nástroj",
        "intent": "Priama odpoveď",
    },
    "cta_title": "Pripravení rásť na platforme {platform}?",
    "cta_text": "Vyberte si balík a my spustíme vašu kampaň. Zvyšok rozhodnú skutoční ľudia a váš prehľad ukáže, čo sme namerali.",

    # Platform hubs
    "services_title": "Čo rozvíjame na platforme {platform}",
    "services_lead": "Jeden balík prinesie všetko, od tých istých skutočných ľudí.",
    "teasers": {
        "audience": "Skutoční ľudia, ktorí objavia váš {profile} a rozhodnú sa {follow}.",
        "likes": "Lajky od ľudí, ktorých bavia vaše {content}.",
        "views": "Zhliadnutia od ľudí, ktorí sa sami rozhodnú pozerať, nikdy nie od skriptov.",
        "comments": "Komentáre od skutočných ľudí, ich vlastnými slovami.",
    },
    "explore": "Preskúmať",
    "in_package": "V každom balíku",
    "goals_title": "Ďalšie spôsoby rastu na platforme {platform}",
    "other_hubs_title": "Rozvíjame aj",
}
