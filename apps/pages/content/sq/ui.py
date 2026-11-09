"""Albanian UI of the money pages: section titles and the blocks every page shares (mirrors en/ui.py).

The platform words are single forms, and every sentence is written around them:
    {audience} ndjekës/abonentë (indefinite plural: "{audience} të rinj")
    {follow} t'ju ndjekin/të abonohen (with its particle: "zgjodhën {follow}")
    {profile} profilin/kanalin (accusative: "{profile} tuaj") · {handle} emrin e përdoruesit/identifikuesin e kanalit
    {content} postimet/videot (definite plural: "{content} tuaja")
"""

UI = {
    # Words that change with the platform or the service
    "audience": {"instagram": "ndjekës", "tiktok": "ndjekës", "youtube": "abonentë"},
    "follow": {"instagram": "t'ju ndjekin", "tiktok": "t'ju ndjekin", "youtube": "të abonohen"},
    "profile": {"instagram": "profilin", "tiktok": "profilin", "youtube": "kanalin"},
    "handle": {"instagram": "emrin e përdoruesit", "tiktok": "emrin e përdoruesit", "youtube": "identifikuesin e kanalit"},
    "content": {"instagram": "postimet", "tiktok": "videot", "youtube": "videot"},
    "service_names": {"followers": "Ndjekës", "subscribers": "Abonentë", "likes": "Pëlqime",
                      "views": "Shikime", "comments": "Komente"},
    "service_words": {"followers": "ndjekës", "subscribers": "abonentë", "likes": "pëlqime",
                      "views": "shikime", "comments": "komente"},

    # Page chrome
    "home": "Kreu",
    "crumbs_label": "Shtegu i navigimit",
    "eyebrow": "{platform} · {service_name}",
    "eyebrow_hub": "Rritje në {platform}",
    "cta": "Nisni me {pick_name}",
    "cta_more": "Shihni të gjitha paketat",
    "trust": ["Njerëz të vërtetë, kurrë robotë", "Nuk ju kërkojmë kurrë fjalëkalimin", "Mujore, anuloni kur të doni"],
    "product_name": "Paketa rritjeje për {platform}",
    "sticky_cta": "Nisni",

    # Packages
    "packages_title": "Zgjidhni paketën tuaj",
    "packages_lead": "Tri paketa mujore. Bashkë vijnë {audience} të rinj, pëlqime, shikime dhe komente, nga të njëjtët njerëz të vërtetë.",
    "packages_note": "Intervale tipike mujore, jo një numër i caktuar: si {audience} vijnë vetëm njerëz të vërtetë që zgjodhën {follow}, ndaj çdo muaj është pak ndryshe.",

    # What's included: the page's own service comes first, then the rest in this order.
    "included_title": "Çfarë përfshihet",
    "included_lead": "Çdo paketë sjell të gjithë tablonë, nga të njëjtët njerëz të vërtetë.",
    "included_items": {
        "audience": ("Çdo muaj {audience} të rinj", "Njerëz të vërtetë që zbuluan {profile} tuaj dhe zgjodhën {follow}. Zakonisht {starter_audience} në muaj me {starter_name}."),
        "likes": ("Pëlqime nga të njëjtët njerëz", "Zakonisht {starter_likes} në muaj me {starter_name}, te {content} që u pëlqejnë."),
        "comments": ("Komente me fjalët e tyre", "Zakonisht {starter_comments} në muaj me {starter_name}. Të shkruara nga njerëz, kurrë sipas një skenari."),
        "views": ("Shikime që vijnë vetë", "Të njëjtët njerëz shikojnë vetë {content} tuaja. Shikimet nuk i numërojmë paraprakisht: secili prej tyre është një njeri."),
        "days": ("Të shpërndara gjatë 30 ditëve", "Pak çdo ditë, nga vendndodhja që zgjidhni. Kurrë të gjitha njëherësh."),
        "dashboard": ("Paneli juaj", "Çfarë matëm, ditë pas dite: vizitat nga fushata juaj dhe sa {audience} të rinj sollën ato."),
    },

    # How it works: the subscription, step by step
    "steps_title": "Si funksionon",
    "steps_lead": "Një abonim mujor: ju zgjidhni paketën, ne drejtojmë fushatën, njerëzit e vërtetë vendosin.",
    "steps": [
        ("Zgjidhni një paketë", "{starter_name}, {rising_name} ose {pro_name}, me faturim mujor. Anuloni kur të doni nga llogaria juaj."),
        ("Ne nisim fushatën tuaj", "Na tregoni {handle} në {platform} dhe nga duhet të vijë publiku juaj. Nuk ju kërkojmë kurrë fjalëkalimin."),
        ("Njerëz të vërtetë zbulojnë {profile} tuaj", "Çdo ditë ua shfaqim {profile} tuaj njerëzve të vërtetë. Ata që pëlqejnë atë që shohin vendosin vetë {follow}, të pëlqejnë dhe të komentojnë."),
        ("Paneli juaj tregon çfarë matëm", "Vizitat nga fushata juaj dhe sa {audience} të rinj sollën ato, ditë pas dite. Shifra të matura, kurrë hamendje."),
    ],

    # Real people vs bots / instant
    "compare_title": "Njerëz të vërtetë, jo robotë",
    "compare_lead": "«Në çast» do të thotë robotë: njerëzit e vërtetë nuk zgjedhin {follow} pak sekonda pas një pagese.",
    "compare_cols": ("Çfarë ndryshon", "Shërbimet «në çast» dhe me robotë", "Growsterr"),
    "compare": [
        ("Kush janë", "Robotë dhe profile të rreme", "Njerëz të vërtetë që zgjodhën {follow}"),
        ("Shpejtësia", "Mijëra brenda pak minutash", "Pak çdo ditë, gjatë gjithë muajit"),
        ("Pëlqimet dhe komentet", "Shiten veçmas, nga robotë të tjerë", "Nga të njëjtët njerëz, brenda paketës suaj"),
        ("Shtrirja juaj", "Bie në heshtje: një publik që nuk angazhohet kurrë i thotë algoritmit të {platform} se {content} tuaja nuk ia vlen të shfaqen", "Rritet me njerëz që shikojnë, pëlqejnë dhe rikthehen"),
        ("Fjalëkalimi juaj", "Shpesh e kërkojnë", "Kurrë"),
        ("Çfarë shihni", "Një numër që mund të zhduket në pastrimin e radhës", "Një panel me atë që matëm"),
    ],

    # Quantity pages: how a monthly package gets you to the goal
    "quantity_title": "Si arrini në {quantity} {service}",
    "quantity_lead": "Nuk shesim një paketë fikse prej {quantity}. Njerëzit e vërtetë vendosin vetë, ndaj një paketë mujore ju çon atje me ritëm natyral.",
    "pace_title": "Ritmi tipik me {pick_name}",
    "pace_month": "Muaji {n}",
    "pace_goal": "Synimi: {quantity}",
    "pace_note": "Intervale tipike nga ajo që bëjnë njerëzit e vërtetë, kurrë një premtim. Disa muaj sjellin më shumë, disa më pak.",
    "by_plan_title": "Koha deri në {quantity}, sipas paketës",
    "a_month": "{range} në muaj",
    "when_first": "zakonisht brenda muajit të parë",
    "when_about": "zakonisht rreth {n} muaj",
    "when_range": "zakonisht {low}–{high} muaj",
    "views_pace": "Shikimet vijnë nga të njëjtët njerëz të vërtetë që zbulojnë {profile} tuaj, ndaj nuk i numërojmë paraprakisht. {pick_name} është paketa që i përshtatet më mirë këtij synimi.",

    # FAQ, related pages, closing
    "faq_title": "Pyetje dhe përgjigje",
    "related_title": "Vazhdoni të eksploroni",
    "related": {
        "platform": "Më shumë për {platform}",
        "platforms": "Në platforma të tjera",
        "quantities": "Synime të tjera",
        "modifiers": "Mënyra të tjera për t'u rritur",
        "articles": "Lexoni më tej",
        "hubs": "Rrituni me njerëz të vërtetë në",
    },
    # The tools a page can carry ("tool"): they run in the browser, nothing is sent.
    "tools": {
        "calculate": "Llogarit",
        "followers": "Ndjekës",
        "avg_likes": "Pëlqime mesatare për postim",
        "avg_comments": "Komente mesatare për postim",
        "engagement_title": "Shkalla juaj e angazhimit",
        "engagement_lead": "Sa nga ndjekësit tuaj reagojnë ndaj një postimi tipik. Shkruani shifrat nga postimet tuaja të fundit.",
        "engagement_result": "Shkalla juaj e angazhimit është {rate}%.",
        "engagement_note": "Shkalla rritet kur njerëzit që ju ndjekin interesohen vërtet për postimet tuaja. Ndjekësit që nuk reagojnë kurrë e ulin atë, sido që të jetë numri i tyre.",
        "growth_title": "Sa kohë deri te synimi juaj?",
        "growth_lead": "Shkruani ku jeni dhe ku doni të arrini. E llogarisim nga intervali tipik mujor i secilës paketë.",
        "current": "Ndjekës sot",
        "goal": "Synimi juaj",
        "when_first": "zakonisht brenda muajit të parë",
        "when_range": "zakonisht {low}–{high} muaj",
        "when_about": "rreth {n} muaj",
        "reached": "E keni arritur tashmë.",
        "growth_note": "Intervale tipike, jo një premtim: njerëzit e vërtetë vendosin vetë nëse do t'ju ndjekin.",
    },
    # Eyebrow above the headline of pages outside the platform x service grid (by "kind").
    "article_eyebrows": {
        "guide": "Udhëzues",
        "alternative": "Krahasim",
        "payment": "Pagesa",
        "agency": "Agjenci rritjeje",
        "tool": "Mjet",
        "intent": "Përgjigje e drejtpërdrejtë",
    },
    "cta_title": "Gati për t'u rritur në {platform}?",
    "cta_text": "Zgjidhni një paketë dhe ne nisim fushatën tuaj. Pjesën tjetër e vendosin njerëzit e vërtetë, dhe paneli juaj tregon çfarë matëm.",

    # Platform hubs
    "services_title": "Çfarë rritim në {platform}",
    "services_lead": "Një paketë i sjell të gjitha, nga të njëjtët njerëz të vërtetë.",
    "teasers": {
        "audience": "Njerëz të vërtetë që zbulojnë {profile} tuaj dhe zgjedhin {follow}.",
        "likes": "Pëlqime nga njerëzit që shijojnë {content} tuaja.",
        "views": "Shikime nga njerëz që zgjedhin vetë t'i shohin, kurrë nga skripte.",
        "comments": "Komente të shkruara nga njerëz të vërtetë, me fjalët e tyre.",
    },
    "explore": "Eksploroni",
    "in_package": "Brenda çdo pakete",
    "goals_title": "Më shumë mënyra për t'u rritur në {platform}",
    "other_hubs_title": "Rritim edhe në",
}
