"""Irish UI of the money pages ("tú"). Mirrors en/ui.py key by key.

Grammar notes for the placeholders (one form each, every template below uses that form):
    {platform} is never mutated: only after "ar", as a subject, or in "Pacáistí fáis {platform}".
    {audience} radical plural ("leantóirí", "síntiúsóirí"): after a verb, after the plural
        article "na" (l and s don't change) or before "nua"; never after "do".
    {follow} verbal-noun phrase after "socraigh" ("a shocraigh {follow}").
    {profile}, {handle}, {content} carry the possessive inside ("do phróifíl", "d'fhíseáin"),
        so a template never puts "do" before them.
    {service} singular, the form after a number ("{quantity} {service}": 1,000 leantóir).
    Month counts use ordinals ("faoin {n}ú mí") so no noun follows a bare number.
"""

UI = {
    # Words that change with the platform or the service
    "audience": {"instagram": "leantóirí", "tiktok": "leantóirí", "youtube": "síntiúsóirí"},
    "follow": {"instagram": "thú a leanúint", "tiktok": "thú a leanúint", "youtube": "liostáil"},
    "profile": {"instagram": "do phróifíl", "tiktok": "do phróifíl", "youtube": "do chainéal"},
    "handle": {"instagram": "d'ainm úsáideora", "tiktok": "d'ainm úsáideora", "youtube": "ainm @ do chainéil"},
    "content": {"instagram": "do phostálacha", "tiktok": "d'fhíseáin", "youtube": "d'fhíseáin"},
    "service_names": {"followers": "Leantóirí", "subscribers": "Síntiúsóirí", "likes": "‘Is maith liom’",
                      "views": "Féachaintí", "comments": "Tráchtanna"},
    "service_words": {"followers": "leantóir", "subscribers": "síntiúsóir", "likes": "‘is maith liom’",
                      "views": "féachaint", "comments": "trácht"},

    # Page chrome
    "home": "Baile",
    "crumbs_label": "Rian nascleanúna",
    "eyebrow": "{platform} · {service_name}",
    "eyebrow_hub": "Fás ar {platform}",
    "cta": "Tosaigh le {pick_name}",
    "cta_more": "Féach gach pacáiste",
    "trust": ["Daoine fíora, ní róbait choíche", "Ní iarraimid do phasfhocal riamh", "Míosúil, cealaigh am ar bith"],
    "product_name": "Pacáistí fáis {platform}",
    "sticky_cta": "Tosaigh",

    # Packages
    "packages_title": "Roghnaigh do phacáiste",
    "packages_lead": "Trí phacáiste mhíosúla. Tagann {audience} nua, ‘is maith liom’, féachaintí agus tráchtanna le chéile, ó na daoine fíora céanna.",
    "packages_note": "Raonta tipiciúla míosúla, ní líon seasta: is daoine fíora iad na {audience} nua go léir, a shocraigh féin {follow}, mar sin bíonn gach mí beagán difriúil.",

    # What's included: the page's own service comes first, then the rest in this order.
    "included_title": "Cad atá san áireamh",
    "included_lead": "Tugann gach pacáiste an pictiúr iomlán, ó na daoine fíora céanna.",
    "included_items": {
        "audience": ("Na {audience} nua", "Daoine fíora a d'aimsigh {profile} agus a shocraigh {follow}. {starter_audience} sa mhí de ghnáth le {starter_name}."),
        "likes": ("‘Is maith liom’ ó na daoine céanna", "{starter_likes} sa mhí de ghnáth le {starter_name}, ar {content} a thaitníonn leo."),
        "comments": ("Tráchtanna ina bhfocail féin", "{starter_comments} sa mhí de ghnáth le {starter_name}. Scríofa ag daoine, ní ag scripteanna."),
        "views": ("Féachaintí a thagann leis", "Féachann na daoine céanna ar {content} as a stuaim féin. Ní chomhairímid féachaintí roimh ré: duine is ea gach ceann acu."),
        "days": ("Scaipthe thar 30 lá", "Beagán gach lá, ón áit a roghnaíonn tú. Ní thagann sé ar fad in aon iarraidh amháin."),
        "dashboard": ("Do dheais", "Cad a thomhaiseamar, lá ar lá: cuairteanna ó d'fheachtas agus na {audience} nua a thug siad leo."),
    },

    # How it works: the subscription, step by step
    "steps_title": "Conas a oibríonn sé",
    "steps_lead": "Síntiús míosúil: roghnaíonn tusa an pacáiste, reáchtálaimidne an feachtas, socraíonn daoine fíora.",
    "steps": [
        ("Roghnaigh pacáiste", "{starter_name}, {rising_name} nó {pro_name}, billeáilte go míosúil. Cealaigh am ar bith ó do chuntas."),
        ("Tosaímid d'fheachtas", "Inis dúinn {handle} ar {platform} agus cárb as ar cheart do do lucht féachana teacht. Ní iarraimid do phasfhocal riamh."),
        ("Aimsíonn daoine fíora {profile}", "Gach lá taispeántar {profile} do dhaoine fíora. Iad siúd ar maith leo an rud a fheiceann siad, socraíonn siad féin {follow}, ‘is maith liom’ a thabhairt agus trácht a dhéanamh."),
        ("Taispeánann do dheais cad a thomhaiseamar", "Cuairteanna ó d'fheachtas agus na {audience} nua a thug siad leo, lá ar lá. Uimhreacha tomhaiste, ní buillí faoi thuairim."),
    ],

    # Real people vs bots / instant
    "compare_title": "Daoine fíora, ní róbait",
    "compare_lead": "Ciallaíonn ar an toirt róbait: ní shocraíonn aon duine fíor {follow} cúpla soicind tar éis íocaíochta.",
    "compare_cols": ("Cad a athraíonn", "Seirbhísí ar an toirt agus róbait", "Growsterr"),
    "compare": [
        ("Cé hiad", "Róbait agus próifílí bréige", "Daoine fíora a shocraigh {follow}"),
        ("Luas", "Na mílte i gceann nóiméad", "Beagán gach lá, ar feadh na míosa"),
        ("‘Is maith liom’ agus tráchtanna", "Díolta ar leith, ó thuilleadh róbat", "Ó na daoine céanna, laistigh de do phacáiste"),
        ("Cé mhéad duine a fheiceann thú", "Titeann sé go ciúin: nuair nach nglacann do lucht féachana páirt riamh, ceapann {platform} nach fiú {content} a thaispeáint", "Fásann sé le daoine a fhéachann, a thugann ‘is maith liom’ agus a fhilleann"),
        ("Do phasfhocal", "Iarrtar go minic é", "Ní iarrtar riamh"),
        ("Cad a fheiceann tú", "Uimhir a d'fhéadfadh imeacht sa chéad ghlanadh eile", "Deais de na rudaí a thomhaiseamar"),
    ],

    # Quantity pages: how a monthly package gets you to the goal
    "quantity_title": "Conas {quantity} {service} a bhaint amach",
    "quantity_lead": "Ní dhíolaimid pacáiste seasta de {quantity}. Socraíonn daoine fíora dóibh féin, mar sin tugann pacáiste míosúil ann thú ar luas nádúrtha.",
    "pace_title": "Luas tipiciúil le {pick_name}",
    "pace_month": "Mí {n}",
    "pace_goal": "Sprioc: {quantity}",
    "pace_note": "Raonta tipiciúla bunaithe ar a ndéanann daoine fíora, ní gealltanas. Tugann míonna áirithe níos mó, cinn eile níos lú.",
    "by_plan_title": "Am go dtí {quantity}, de réir pacáiste",
    "a_month": "{range} sa mhí",
    "when_first": "sa chéad mhí de ghnáth",
    "when_about": "faoin {n}ú mí de ghnáth",
    "when_range": "idir an {low}ú agus an {high}ú mí de ghnáth",
    "views_pace": "Tagann féachaintí ó na daoine fíora céanna a aimsíonn {profile}, mar sin ní chomhairímid roimh ré iad. Is é {pick_name} an pacáiste is fearr a oireann don sprioc sin.",

    # FAQ, related pages, closing
    "faq_title": "Ceisteanna agus freagraí",
    "related_title": "Tuilleadh le fiosrú",
    "related": {
        "platform": "Tuilleadh faoi {platform}",
        "platforms": "Ar ardáin eile",
        "quantities": "Spriocanna eile",
        "modifiers": "Bealaí eile le fás",
        "articles": "Le léamh freisin",
        "hubs": "Fás le daoine fíora ar",
    },
    # The tools a page can carry ("tool"): they run in the browser, nothing is sent.
    "tools": {
        "calculate": "Ríomh",
        "followers": "Leantóirí",
        "avg_likes": "Meán ‘is maith liom’ in aghaidh postála",
        "avg_comments": "Meán tráchtanna in aghaidh postála",
        "engagement_title": "Do ráta rannpháirtíochta",
        "engagement_lead": "An sciar de do leantóirí a fhreagraíonn do ghnáthphostáil. Cuir isteach na huimhreacha ó do chúpla postáil is déanaí.",
        "engagement_result": "Is é {rate}% do ráta rannpháirtíochta.",
        "engagement_note": "Ardaíonn an ráta nuair is cás leis na daoine a leanann thú do phostálacha i ndáiríre. Íslíonn leantóirí nach bhfreagraíonn riamh é, is cuma cé mhéad acu atá ann.",
        "growth_title": "Cá fhad go dtí do sprioc?",
        "growth_lead": "Cuir isteach cá bhfuil tú anois agus cá háit ar mhaith leat a bheith. Oibrímid amach é ó raon míosúil tipiciúil gach pacáiste.",
        "current": "Leantóirí inniu",
        "goal": "Do sprioc",
        "when_first": "sa chéad mhí de ghnáth",
        "when_range": "idir an {low}ú agus an {high}ú mí de ghnáth",
        "when_about": "faoin {n}ú mí",
        "reached": "Tá tú ann cheana féin.",
        "growth_note": "Raonta tipiciúla, ní gealltanas: socraíonn daoine fíora dóibh féin an leanfaidh siad thú.",
    },
    # Eyebrow above the headline of pages outside the platform x service grid (by "kind").
    "article_eyebrows": {
        "guide": "Treoir",
        "alternative": "Comparáid",
        "payment": "Íocaíochtaí",
        "agency": "Gníomhaireacht fáis",
        "tool": "Uirlis",
        "intent": "Freagra díreach",
    },
    "cta_title": "Réidh le fás ar {platform}?",
    "cta_text": "Roghnaigh pacáiste agus tosóimid d'fheachtas. Socraíonn daoine fíora an chuid eile, agus taispeánann do dheais cad a thomhaiseamar.",

    # Platform hubs
    "services_title": "Cad a fhásaimid ar {platform}",
    "services_lead": "Tugann pacáiste amháin iad uile, ó na daoine fíora céanna.",
    "teasers": {
        "audience": "Daoine fíora a aimsíonn {profile} agus a shocraíonn {follow}.",
        "likes": "‘Is maith liom’ ó dhaoine a dtaitníonn {content} leo.",
        "views": "Féachaintí ó dhaoine a roghnaíonn féachaint, ní ó scripteanna choíche.",
        "comments": "Tráchtanna scríofa ag daoine fíora, ina bhfocail féin.",
    },
    "explore": "Fiosraigh",
    "in_package": "I ngach pacáiste",
    "goals_title": "Tuilleadh bealaí le fás ar {platform}",
    "other_hubs_title": "Cabhraímid leat fás freisin ar",
}
