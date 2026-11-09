"""Welsh UI of the money pages (formal "chi"). Mirrors en/ui.py key by key.

Grammar notes for the placeholders (one form each, every template below uses that form):
    {platform} is never mutated ("ar {platform}", "Pecynnau twf {platform}").
    {audience} radical plural ("dilynwyr", "tanysgrifwyr"): only after "mae", "eich"/"'ch",
        the plural article "'r" or at a point where nothing mutates it; never after "a", "i", "o".
    {follow} verb-noun phrase after another verb-noun ("wedi dewis {follow}",
        "yn penderfynu {follow}"), where its object isn't mutated.
    {profile}, {handle}, {content} carry "eich" ("eich proffil", "eich fideos"), which never mutates.
    {service} soft-mutated plural for after "o" ("{quantity} o {service}": 1,000 o ddilynwyr).
"""

UI = {
    # Words that change with the platform or the service
    "audience": {"instagram": "dilynwyr", "tiktok": "dilynwyr", "youtube": "tanysgrifwyr"},
    "follow": {"instagram": "eich dilyn", "tiktok": "eich dilyn", "youtube": "tanysgrifio"},
    "profile": {"instagram": "eich proffil", "tiktok": "eich proffil", "youtube": "eich sianel"},
    "handle": {"instagram": "eich enw defnyddiwr", "tiktok": "eich enw defnyddiwr", "youtube": "enw @ eich sianel"},
    "content": {"instagram": "eich postiadau", "tiktok": "eich fideos", "youtube": "eich fideos"},
    "service_names": {"followers": "Dilynwyr", "subscribers": "Tanysgrifwyr", "likes": "Hoffiadau",
                      "views": "Gwyliadau", "comments": "Sylwadau"},
    "service_words": {"followers": "ddilynwyr", "subscribers": "danysgrifwyr", "likes": "hoffiadau",
                      "views": "wyliadau", "comments": "sylwadau"},

    # Page chrome
    "home": "Hafan",
    "crumbs_label": "Briwsion bara",
    "eyebrow": "{platform} · {service_name}",
    "eyebrow_hub": "Twf ar {platform}",
    "cta": "Dechrau gyda {pick_name}",
    "cta_more": "Gweld pob pecyn",
    "trust": ["Pobl go iawn, byth bots", "Dydyn ni byth yn gofyn am eich cyfrinair", "Misol, canslo unrhyw bryd"],
    "product_name": "Pecynnau twf {platform}",
    "sticky_cta": "Dechrau",

    # Packages
    "packages_title": "Dewiswch eich pecyn",
    "packages_lead": "Tri phecyn misol. Mae {audience} newydd, hoffiadau, gwyliadau a sylwadau'n dod gyda'i gilydd, gan yr un bobl go iawn.",
    "packages_note": "Ystodau misol nodweddiadol, nid nifer sefydlog: mae pob un o'ch {audience} newydd yn berson go iawn sydd wedi dewis {follow}, felly mae pob mis ychydig yn wahanol.",

    # What's included: the page's own service comes first, then the rest in this order.
    "included_title": "Beth sydd wedi'i gynnwys",
    "included_lead": "Mae pob pecyn yn dod â'r darlun cyfan, gan yr un bobl go iawn.",
    "included_items": {
        "audience": ("Eich {audience} newydd", "Pobl go iawn a ddarganfu {profile} ac sydd wedi dewis {follow}. Fel arfer {starter_audience} y mis gyda {starter_name}."),
        "likes": ("Hoffiadau gan yr un bobl", "Fel arfer {starter_likes} y mis gyda {starter_name}, ar {content} maen nhw'n eu mwynhau."),
        "comments": ("Sylwadau yn eu geiriau eu hunain", "Fel arfer {starter_comments} y mis gyda {starter_name}. Wedi'u hysgrifennu gan bobl, byth gan sgriptiau."),
        "views": ("Gwyliadau sy'n dod gydag ef", "Mae'r un bobl yn gwylio {content} ohonyn nhw'u hunain. Dydyn ni ddim yn cyfrif gwyliadau ymlaen llaw: person yw pob un."),
        "days": ("Wedi'u gwasgaru dros 30 diwrnod", "Ychydig bob dydd, o'r lleoliad a ddewiswch. Byth i gyd ar yr un pryd."),
        "dashboard": ("Eich dangosfwrdd", "Beth wnaethon ni ei fesur, dydd wrth ddydd: ymweliadau o'ch ymgyrch a'r {audience} newydd a ddaeth yn eu sgil."),
    },

    # How it works: the subscription, step by step
    "steps_title": "Sut mae'n gweithio",
    "steps_lead": "Tanysgrifiad misol: chi sy'n dewis y pecyn, ni sy'n rhedeg yr ymgyrch, pobl go iawn sy'n penderfynu.",
    "steps": [
        ("Dewiswch becyn", "{starter_name}, {rising_name} neu {pro_name}, wedi'i filio'n fisol. Canslo unrhyw bryd o'ch cyfrif."),
        ("Rydyn ni'n dechrau eich ymgyrch", "Rhowch {handle} ar {platform} i ni, a dywedwch o ble dylai eich cynulleidfa ddod. Dydyn ni byth yn gofyn am eich cyfrinair."),
        ("Mae pobl go iawn yn darganfod {profile}", "Bob dydd rydyn ni'n dangos {profile} i bobl go iawn. Mae'r rhai sy'n hoffi'r hyn maen nhw'n ei weld yn penderfynu {follow}, hoffi a rhoi sylwadau, ohonyn nhw'u hunain."),
        ("Mae eich dangosfwrdd yn dangos beth wnaethon ni ei fesur", "Ymweliadau o'ch ymgyrch a'r {audience} newydd a ddaeth yn eu sgil, dydd wrth ddydd. Niferoedd wedi'u mesur, byth dyfaliadau."),
    ],

    # Real people vs bots / instant
    "compare_title": "Pobl go iawn, nid bots",
    "compare_lead": "Mae ar unwaith yn golygu bots: does dim person go iawn yn penderfynu {follow} eiliadau ar ôl taliad.",
    "compare_cols": ("Beth sy'n newid", "Gwasanaethau ar unwaith a bots", "Growsterr"),
    "compare": [
        ("Pwy ydyn nhw", "Bots a phroffiliau ffug", "Pobl go iawn sydd wedi dewis {follow}"),
        ("Cyflymder", "Miloedd mewn munudau", "Ychydig bob dydd, drwy'r mis"),
        ("Hoffiadau a sylwadau", "Yn cael eu gwerthu ar wahân, gan ragor o fots", "Gan yr un bobl, y tu mewn i'ch pecyn"),
        ("Eich cyrhaeddiad", "Yn gostwng yn dawel: mae cynulleidfa sydd byth yn ymgysylltu yn dweud wrth {platform} nad yw {content} yn werth eu dangos", "Yn tyfu gyda phobl sy'n gwylio, yn hoffi ac yn dod yn ôl"),
        ("Eich cyfrinair", "Yn aml yn cael ei ofyn", "Byth"),
        ("Beth rydych chi'n ei weld", "Nifer a all ddiflannu yn y glanhau nesaf", "Dangosfwrdd o'r hyn wnaethon ni ei fesur"),
    ],

    # Quantity pages: how a monthly package gets you to the goal
    "quantity_title": "Sut i gyrraedd {quantity} o {service}",
    "quantity_lead": "Dydyn ni ddim yn gwerthu pecyn sefydlog o {quantity}. Mae pobl go iawn yn penderfynu drostyn nhw'u hunain, felly mae pecyn misol yn mynd â chi yno ar gyflymder naturiol.",
    "pace_title": "Cyflymder nodweddiadol gyda {pick_name}",
    "pace_month": "Mis {n}",
    "pace_goal": "Nod: {quantity}",
    "pace_note": "Ystodau nodweddiadol yn ôl yr hyn mae pobl go iawn yn ei wneud, byth addewid. Mae rhai misoedd yn dod â mwy, eraill â llai.",
    "by_plan_title": "Amser i gyrraedd {quantity}, fesul pecyn",
    "a_month": "{range} y mis",
    "when_first": "fel arfer o fewn y mis cyntaf",
    "when_about": "fel arfer tua {n} mis",
    "when_range": "fel arfer {low}–{high} mis",
    "views_pace": "Daw gwyliadau gan yr un bobl go iawn sy'n darganfod {profile}, felly dydyn ni ddim yn eu cyfrif ymlaen llaw. {pick_name} yw'r pecyn sy'n gweddu orau i'r nod hwn.",

    # FAQ, related pages, closing
    "faq_title": "Cwestiynau ac atebion",
    "related_title": "Archwilio ymhellach",
    "related": {
        "platform": "Mwy am {platform}",
        "platforms": "Ar blatfformau eraill",
        "quantities": "Nodau eraill",
        "modifiers": "Ffyrdd eraill o dyfu",
        "articles": "Darllen nesaf",
        "hubs": "Tyfu gyda phobl go iawn ar",
    },
    # The tools a page can carry ("tool"): they run in the browser, nothing is sent.
    "tools": {
        "calculate": "Cyfrifo",
        "followers": "Dilynwyr",
        "avg_likes": "Cyfartaledd hoffiadau fesul postiad",
        "avg_comments": "Cyfartaledd sylwadau fesul postiad",
        "engagement_title": "Eich cyfradd ymgysylltu",
        "engagement_lead": "Faint o'ch dilynwyr sy'n ymateb i bostiad nodweddiadol. Rhowch y niferoedd o'ch ychydig bostiadau diwethaf.",
        "engagement_result": "Eich cyfradd ymgysylltu yw {rate}%.",
        "engagement_note": "Mae'r gyfradd yn codi pan fydd y bobl sy'n eich dilyn yn poeni go iawn am eich postiadau. Mae dilynwyr sydd byth yn ymateb yn ei gostwng, waeth faint ohonyn nhw sydd.",
        "growth_title": "Faint o amser tan eich nod?",
        "growth_lead": "Rhowch ble rydych chi nawr a ble rydych chi eisiau bod. Rydyn ni'n ei gyfrifo o ystod fisol nodweddiadol pob pecyn.",
        "current": "Dilynwyr heddiw",
        "goal": "Eich nod",
        "when_first": "fel arfer o fewn y mis cyntaf",
        "when_range": "fel arfer {low}–{high} mis",
        "when_about": "tua {n} mis",
        "reached": "Rydych chi yno'n barod.",
        "growth_note": "Ystodau nodweddiadol, nid addewid: pobl go iawn sy'n penderfynu drostyn nhw'u hunain a fyddan nhw'n eich dilyn.",
    },
    # Eyebrow above the headline of pages outside the platform x service grid (by "kind").
    "article_eyebrows": {
        "guide": "Canllaw",
        "alternative": "Cymharu",
        "payment": "Taliadau",
        "agency": "Asiantaeth dwf",
        "tool": "Teclyn",
        "intent": "Ateb plaen",
    },
    "cta_title": "Yn barod i dyfu ar {platform}?",
    "cta_text": "Dewiswch becyn ac fe ddechreuwn ni eich ymgyrch. Pobl go iawn sy'n penderfynu'r gweddill, ac mae eich dangosfwrdd yn dangos beth wnaethon ni ei fesur.",

    # Platform hubs
    "services_title": "Beth rydyn ni'n ei dyfu ar {platform}",
    "services_lead": "Mae un pecyn yn dod â'r cyfan, gan yr un bobl go iawn.",
    "teasers": {
        "audience": "Pobl go iawn sy'n darganfod {profile} ac yn dewis {follow}.",
        "likes": "Hoffiadau gan bobl sy'n mwynhau {content}.",
        "views": "Gwyliadau gan bobl sy'n dewis gwylio, byth gan sgriptiau.",
        "comments": "Sylwadau wedi'u hysgrifennu gan bobl go iawn, yn eu geiriau eu hunain.",
    },
    "explore": "Archwilio",
    "in_package": "Ym mhob pecyn",
    "goals_title": "Mwy o ffyrdd o dyfu ar {platform}",
    "other_hubs_title": "Rydyn ni hefyd yn tyfu",
}
