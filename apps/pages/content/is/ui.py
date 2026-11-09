"""Icelandic UI of the money pages (mirrors en/ui.py key by key).

The word placeholders are chosen so every sentence stays grammatical on every platform:
{audience} nominative plural after "nýir" (fylgjendur/áskrifendur), {follow} an infinitive
phrase with no agreement (fylgja þér / skrá sig í áskrift), {profile}, {content} and {handle}
accusative with the possessive (prófílinn þinn, færslurnar þínar), {service} a plural that is
the same in nominative and accusative (fylgjendur, læk, áhorf). {platform} stays uninflected.
"""

UI = {
    # Words that change with the platform or the service
    "audience": {"instagram": "fylgjendur", "tiktok": "fylgjendur", "youtube": "áskrifendur"},
    "follow": {"instagram": "fylgja þér", "tiktok": "fylgja þér", "youtube": "skrá sig í áskrift"},
    "profile": {"instagram": "prófílinn þinn", "tiktok": "prófílinn þinn", "youtube": "rásina þína"},
    "handle": {"instagram": "notandanafnið þitt", "tiktok": "notandanafnið þitt", "youtube": "auðkenni rásarinnar"},
    "content": {"instagram": "færslurnar þínar", "tiktok": "myndböndin þín", "youtube": "myndböndin þín"},
    "service_names": {"followers": "Fylgjendur", "subscribers": "Áskrifendur", "likes": "Læk",
                      "views": "Áhorf", "comments": "Athugasemdir"},
    "service_words": {"followers": "fylgjendur", "subscribers": "áskrifendur", "likes": "læk",
                      "views": "áhorf", "comments": "athugasemdir"},

    # Page chrome
    "home": "Forsíða",
    "crumbs_label": "Brauðmolar",
    "eyebrow": "{platform} · {service_name}",
    "eyebrow_hub": "Vöxtur á {platform}",
    "cta": "Byrjaðu með {pick_name}",
    "cta_more": "Sjá alla pakka",
    "trust": ["Raunverulegt fólk, aldrei bottar", "Við biðjum aldrei um lykilorðið þitt", "Mánaðarlega, segðu upp hvenær sem er"],
    "product_name": "Vaxtarpakkar fyrir {platform}",
    "sticky_cta": "Byrja",

    # Packages
    "packages_title": "Veldu pakkann þinn",
    "packages_lead": "Þrír mánaðarpakkar. Nýir {audience}, læk, áhorf og athugasemdir koma saman, frá sama raunverulega fólkinu.",
    "packages_note": "Dæmigerð bil á mánuði, ekki föst tala: allir nýir {audience} eru raunverulegt fólk sem hefur valið að {follow}, svo hver mánuður er aðeins ólíkur.",

    # What's included: the page's own service comes first, then the rest in this order.
    "included_title": "Þetta er innifalið",
    "included_lead": "Hver pakki færir þér heildarmyndina, frá sama raunverulega fólkinu.",
    "included_items": {
        "audience": ("Nýir {audience}", "Raunverulegt fólk sem fann {profile} og valdi að {follow}. Yfirleitt {starter_audience} á mánuði með {starter_name}."),
        "likes": ("Læk frá sama fólkinu", "Yfirleitt {starter_likes} á mánuði með {starter_name}, þegar sama fólkið sér {content} og kann að meta það sem það sér."),
        "comments": ("Athugasemdir með eigin orðum", "Yfirleitt {starter_comments} á mánuði með {starter_name}. Skrifaðar af fólki, aldrei eftir handriti."),
        "views": ("Áhorf fylgir með", "Sama fólkið horfir á {content} af eigin frumkvæði. Við teljum ekki áhorf fyrir fram: hvert áhorf er manneskja."),
        "days": ("Dreift á 30 daga", "Svolítið á hverjum degi, frá staðnum sem þú velur. Aldrei allt í einu."),
        "dashboard": ("Stjórnborðið þitt", "Það sem við mældum, dag frá degi: heimsóknir úr herferðinni þinni og nýir {audience} sem þær skiluðu."),
    },

    # How it works: the subscription, step by step
    "steps_title": "Svona virkar þetta",
    "steps_lead": "Mánaðarleg áskrift: þú velur pakkann, við keyrum herferðina, raunverulegt fólk ákveður.",
    "steps": [
        ("Veldu pakka", "{starter_name}, {rising_name} eða {pro_name}, greitt mánaðarlega. Segðu upp hvenær sem er á reikningnum þínum."),
        ("Við hefjum herferðina þína", "Sendu okkur {handle} á {platform} og segðu okkur hvaðan markhópurinn þinn á að koma. Við biðjum aldrei um lykilorðið þitt."),
        ("Raunverulegt fólk finnur {profile}", "Á hverjum degi sýnum við {profile} raunverulegu fólki. Þau sem kunna að meta það sem þau sjá velja sjálf að {follow}, læka og skrifa athugasemdir."),
        ("Stjórnborðið sýnir það sem við mældum", "Heimsóknir úr herferðinni þinni og nýir {audience} sem þær skiluðu, dag frá degi. Mældar tölur, aldrei ágiskanir."),
    ],

    # Real people vs bots / instant
    "compare_title": "Raunverulegt fólk, ekki bottar",
    "compare_lead": "Samstundis þýðir bottar: engin raunveruleg manneskja velur að {follow} sekúndum eftir greiðslu.",
    "compare_cols": ("Hvað breytist", "Skyndiþjónustur og bottar", "Growsterr"),
    "compare": [
        ("Hver þau eru", "Bottar og falskir prófílar", "Raunverulegt fólk sem valdi að {follow}"),
        ("Hraði", "Þúsundir á mínútum", "Svolítið á hverjum degi, allan mánuðinn"),
        ("Læk og athugasemdir", "Seld sér, frá fleiri bottum", "Frá sama fólkinu, innifalið í pakkanum"),
        ("Útbreiðslan þín", "Minnkar í kyrrþey: markhópur sem tekur aldrei þátt segir {platform} að {content} séu ekki þess virði að sýna", "Vex með fólki sem horfir, lækar og kemur aftur"),
        ("Lykilorðið þitt", "Oft beðið um það", "Aldrei"),
        ("Það sem þú sérð", "Tala sem getur horfið í næstu hreinsun", "Stjórnborð með því sem við mældum"),
    ],

    # Quantity pages: how a monthly package gets you to the goal
    "quantity_title": "Svona kemstu í {quantity} {service}",
    "quantity_lead": "Við seljum ekki fastan pakka upp á {quantity} {service}. Raunverulegt fólk ákveður sjálft, svo mánaðarpakki kemur þér þangað á eðlilegum hraða.",
    "pace_title": "Dæmigerður hraði með {pick_name}",
    "pace_month": "Mánuður {n}",
    "pace_goal": "Markmið: {quantity}",
    "pace_note": "Dæmigerð bil út frá því sem raunverulegt fólk gerir, aldrei loforð. Sumir mánuðir skila meiru, aðrir minna.",
    "by_plan_title": "Tími að {quantity}, eftir pakka",
    "a_month": "{range} á mánuði",
    "when_first": "yfirleitt innan fyrsta mánaðarins",
    "when_about": "yfirleitt um {n} mánuðir",
    "when_range": "yfirleitt {low}–{high} mánuðir",
    "views_pace": "Áhorf kemur frá sama raunverulega fólkinu og finnur {profile}, svo við teljum það ekki fyrir fram. {pick_name} er pakkinn sem hentar þessu markmiði best.",

    # FAQ, related pages, closing
    "faq_title": "Spurningar og svör",
    "related_title": "Skoðaðu meira",
    "related": {
        "platform": "Meira um {platform}",
        "platforms": "Á öðrum miðlum",
        "quantities": "Önnur markmið",
        "modifiers": "Aðrar leiðir til að vaxa",
        "articles": "Lestu næst",
        "hubs": "Vaxtu með raunverulegu fólki á",
    },
    # The tools a page can carry ("tool"): they run in the browser, nothing is sent.
    "tools": {
        "calculate": "Reikna",
        "followers": "Fylgjendur",
        "avg_likes": "Meðalfjöldi læka á færslu",
        "avg_comments": "Meðalfjöldi athugasemda á færslu",
        "engagement_title": "Þátttökuhlutfallið þitt",
        "engagement_lead": "Hve margir fylgjenda þinna bregðast við venjulegri færslu? Sláðu inn tölurnar úr síðustu færslunum þínum.",
        "engagement_result": "Þátttökuhlutfallið þitt er {rate}%.",
        "engagement_note": "Hlutfallið hækkar þegar fólkið sem fylgir þér hefur raunverulegan áhuga á færslunum þínum. Fylgjendur sem bregðast aldrei við lækka það, sama hve margir þeir eru.",
        "growth_title": "Hve langt er í markmiðið?",
        "growth_lead": "Sláðu inn hvar þú ert og hvert þú vilt komast. Við reiknum það út frá dæmigerðu mánaðarbili hvers pakka.",
        "current": "Fylgjendur í dag",
        "goal": "Markmiðið þitt",
        "when_first": "yfirleitt innan fyrsta mánaðarins",
        "when_range": "yfirleitt {low}–{high} mánuðir",
        "when_about": "um {n} mánuðir",
        "reached": "Markmiðinu er þegar náð.",
        "growth_note": "Dæmigerð bil, ekki loforð: raunverulegt fólk ákveður sjálft hvort það fylgir þér.",
    },
    # Eyebrow above the headline of pages outside the platform x service grid (by "kind").
    "article_eyebrows": {
        "guide": "Leiðarvísir",
        "alternative": "Samanburður",
        "payment": "Greiðslur",
        "agency": "Vaxtarstofa",
        "tool": "Verkfæri",
        "intent": "Hreinskilið svar",
    },
    "cta_title": "Viltu vaxa á {platform}?",
    "cta_text": "Veldu pakka og við hefjum herferðina þína. Raunverulegt fólk ákveður restina og stjórnborðið sýnir það sem við mældum.",

    # Platform hubs
    "services_title": "Það sem við látum vaxa á {platform}",
    "services_lead": "Einn pakki færir þér þetta allt, frá sama raunverulega fólkinu.",
    "teasers": {
        "audience": "Raunverulegt fólk sem finnur {profile} og velur að {follow}.",
        "likes": "Læk frá fólki sem kann að meta {content}.",
        "views": "Áhorf frá fólki sem velur að horfa, aldrei frá forskriftum.",
        "comments": "Athugasemdir skrifaðar af raunverulegu fólki, með eigin orðum.",
    },
    "explore": "Skoða",
    "in_package": "Innifalið í hverjum pakka",
    "goals_title": "Fleiri leiðir til að vaxa á {platform}",
    "other_hubs_title": "Við hjálpum þér líka að vaxa á",
}
