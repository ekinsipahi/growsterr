"""Czech UI of the money pages (mirrors en/ui.py key by key).

Word forms the sentences are built around: {audience} nominative plural (sledující / odběratelé),
{follow} infinitive (sledovat / odebírat), {profile} nominative = accusative (profil / kanál),
{content} nominative = accusative plural (příspěvky / videa), {service} the counting form after a
number (genitive plural: 1 000 sledujících).
"""

UI = {
    # Words that change with the platform or the service
    "audience": {"instagram": "sledující", "tiktok": "sledující", "youtube": "odběratelé"},
    "follow": {"instagram": "sledovat", "tiktok": "sledovat", "youtube": "odebírat"},
    "profile": {"instagram": "profil", "tiktok": "profil", "youtube": "kanál"},
    "handle": {"instagram": "uživatelské jméno", "tiktok": "uživatelské jméno", "youtube": "identifikátor kanálu"},
    "content": {"instagram": "příspěvky", "tiktok": "videa", "youtube": "videa"},
    "service_names": {"followers": "Sledující", "subscribers": "Odběratelé", "likes": "Lajky",
                      "views": "Zhlédnutí", "comments": "Komentáře"},
    "service_words": {"followers": "sledujících", "subscribers": "odběratelů", "likes": "lajků",
                      "views": "zhlédnutí", "comments": "komentářů"},

    # Page chrome
    "home": "Domů",
    "crumbs_label": "Drobečková navigace",
    "eyebrow": "{platform} · {service_name}",
    "eyebrow_hub": "{platform} · růst",
    "cta": "Začněte s balíčkem {pick_name}",
    "cta_more": "Zobrazit všechny balíčky",
    "trust": ["Skuteční lidé, nikdy boti", "Heslo po vás nikdy nechceme", "Měsíčně, zrušit můžete kdykoli"],
    "product_name": "Balíčky růstu pro {platform}",
    "sticky_cta": "Začít",

    # Packages
    "packages_title": "Vyberte si balíček",
    "packages_lead": "Tři měsíční balíčky. Noví {audience}, lajky, zhlédnutí a komentáře přicházejí společně, od stejných skutečných lidí.",
    "packages_note": "Typická měsíční rozpětí, ne pevný počet: noví {audience} jsou skuteční lidé, kteří se sami rozhodli {follow} váš {profile}, takže každý měsíc vypadá trochu jinak.",

    # What's included: the page's own service comes first, then the rest in this order.
    "included_title": "Co balíček obsahuje",
    "included_lead": "Každý balíček přináší všechno najednou, od stejných skutečných lidí.",
    "included_items": {
        "audience": ("Noví {audience}", "Skuteční lidé, kteří objevili váš {profile} a rozhodli se ho {follow}. S balíčkem {starter_name} obvykle {starter_audience} měsíčně."),
        "likes": ("Lajky od stejných lidí", "S balíčkem {starter_name} obvykle {starter_likes} měsíčně, na vaše {content}, které je baví."),
        "comments": ("Komentáře jejich vlastními slovy", "S balíčkem {starter_name} obvykle {starter_comments} měsíčně. Píšou je lidé, nikdy podle scénáře."),
        "views": ("Zhlédnutí k tomu", "Stejní lidé se na vaše {content} dívají sami od sebe. Zhlédnutí dopředu nepočítáme: každé z nich je člověk."),
        "days": ("Rozloženo do 30 dnů", "Každý den kousek, z lokality, kterou si zvolíte. Nikdy všechno najednou."),
        "dashboard": ("Váš přehled", "Co jsme naměřili, den po dni: návštěvy z vaší kampaně a noví {audience}, které přivedly."),
    },

    # How it works: the subscription, step by step
    "steps_title": "Jak to funguje",
    "steps_lead": "Měsíční předplatné: vy si vyberete balíček, my vedeme kampaň, rozhodují skuteční lidé.",
    "steps": [
        ("Vyberte si balíček", "{starter_name}, {rising_name} nebo {pro_name}, účtováno měsíčně. Zrušit můžete kdykoli ve svém účtu."),
        ("Spustíme vaši kampaň", "Napište nám {handle} na platformě {platform} a odkud má vaše publikum přicházet. Heslo po vás nikdy nechceme."),
        ("Skuteční lidé objevují váš {profile}", "Váš {profile} se každý den ukazuje skutečným lidem. Ti, které zaujme, co vidí, se sami rozhodnou ho {follow}, dát lajk a napsat komentář."),
        ("Přehled ukazuje, co jsme naměřili", "Návštěvy z vaší kampaně a noví {audience}, které přivedly, den po dni. Naměřená čísla, nikdy odhady."),
    ],

    # Real people vs bots / instant
    "compare_title": "Skuteční lidé, ne boti",
    "compare_lead": "Okamžitě znamená boti: žádný skutečný člověk se nerozhodne {follow} váš {profile} pár sekund po zaplacení.",
    "compare_cols": ("Co se mění", "Okamžité služby a boti", "Growsterr"),
    "compare": [
        ("Kdo to je", "Boti a falešné profily", "Skuteční lidé, kteří se rozhodli {follow} váš {profile}"),
        ("Rychlost", "Tisíce během pár minut", "Každý den kousek, celý měsíc"),
        ("Lajky a komentáře", "Prodávané zvlášť, od dalších botů", "Od stejných lidí, v rámci balíčku"),
        ("Váš dosah", "Potichu klesá: publikum, které nikdy nereaguje, dává platformě {platform} najevo, že vaše {content} nestojí za zobrazení", "Roste s lidmi, kteří se dívají, dávají lajky a vracejí se"),
        ("Vaše heslo", "Často ho chtějí", "Nikdy"),
        ("Co vidíte", "Číslo, které může při příští čistce zmizet", "Přehled toho, co jsme naměřili"),
    ],

    # Quantity pages: how a monthly package gets you to the goal
    "quantity_title": "Jak se dostanete na {quantity} {service}",
    "quantity_lead": "Neprodáváme jednorázově {quantity} {service}. Skuteční lidé se rozhodují sami, takže měsíční balíček vás k cíli dovede přirozeným tempem.",
    "pace_title": "Typické tempo s balíčkem {pick_name}",
    "pace_month": "{n}. měsíc",
    "pace_goal": "Cíl: {quantity}",
    "pace_note": "Typická rozpětí podle toho, co skuteční lidé dělají, nikdy slib. Některé měsíce přinesou víc, jiné méně.",
    "by_plan_title": "Doba do cíle {quantity} podle balíčku",
    "a_month": "{range} měsíčně",
    "when_first": "obvykle už během prvního měsíce",
    "when_about": "obvykle kolem {n}. měsíce",
    "when_range": "obvykle mezi {low}. a {high}. měsícem",
    "views_pace": "Zhlédnutí přicházejí od stejných skutečných lidí, kteří objevují váš {profile}, proto je dopředu nepočítáme. Pro tento cíl se nejlépe hodí balíček {pick_name}.",

    # FAQ, related pages, closing
    "faq_title": "Otázky a odpovědi",
    "related_title": "Mohlo by vás zajímat",
    "related": {
        "platform": "Další o platformě {platform}",
        "platforms": "Na dalších platformách",
        "quantities": "Další cíle",
        "modifiers": "Další cesty k růstu",
        "articles": "Čtěte dál",
        "hubs": "Rosťte se skutečnými lidmi na",
    },
    # The tools a page can carry ("tool"): they run in the browser, nothing is sent.
    "tools": {
        "calculate": "Spočítat",
        "followers": "Sledující",
        "avg_likes": "Průměrný počet lajků na příspěvek",
        "avg_comments": "Průměrný počet komentářů na příspěvek",
        "engagement_title": "Vaše míra zapojení",
        "engagement_lead": "Kolik vašich sledujících reaguje na běžný příspěvek. Zadejte čísla z několika posledních příspěvků.",
        "engagement_result": "Vaše míra zapojení je {rate} %.",
        "engagement_note": "Míra roste, když lidem, kteří vás sledují, na vašich příspěvcích opravdu záleží. Sledující, kteří nikdy nereagují, ji snižují, ať je jich kolik chce.",
        "growth_title": "Za jak dlouho dosáhnete cíle?",
        "growth_lead": "Zadejte, kde jste teď a kam se chcete dostat. Spočítáme to z typického měsíčního rozpětí každého balíčku.",
        "current": "Sledující dnes",
        "goal": "Váš cíl",
        "when_first": "obvykle už během prvního měsíce",
        "when_range": "obvykle mezi {low}. a {high}. měsícem",
        "when_about": "zhruba kolem {n}. měsíce",
        "reached": "Svého cíle už jste dosáhli.",
        "growth_note": "Typická rozpětí, ne slib: skuteční lidé se sami rozhodují, jestli vás budou sledovat.",
    },
    # Eyebrow above the headline of pages outside the platform x service grid (by "kind").
    "article_eyebrows": {
        "guide": "Návod",
        "alternative": "Srovnání",
        "payment": "Platby",
        "agency": "Agentura pro růst",
        "tool": "Nástroj",
        "intent": "Na rovinu",
    },
    "cta_title": "Chcete růst na platformě {platform}?",
    "cta_text": "Vyberte si balíček a my spustíme vaši kampaň. O zbytku rozhodnou skuteční lidé a v přehledu uvidíte, co jsme naměřili.",

    # Platform hubs
    "services_title": "Co vám na platformě {platform} přineseme",
    "services_lead": "Jeden balíček přináší všechno, od stejných skutečných lidí.",
    "teasers": {
        "audience": "Skuteční lidé, kteří objeví váš {profile} a rozhodnou se ho {follow}.",
        "likes": "Lajky od lidí, které baví vaše {content}.",
        "views": "Zhlédnutí od lidí, kteří se sami rozhodnou dívat, nikdy od skriptů.",
        "comments": "Komentáře od skutečných lidí, jejich vlastními slovy.",
    },
    "explore": "Prozkoumat",
    "in_package": "V každém balíčku",
    "goals_title": "Další cesty k růstu na platformě {platform}",
    "other_hubs_title": "Pomáháme růst i jinde",
}
