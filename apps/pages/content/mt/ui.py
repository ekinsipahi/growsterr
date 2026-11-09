"""Maltese UI of the money pages (informal "int"). Mirrors en/ui.py key by key.

Grammar notes for the placeholders (one form each, every template below uses that form):
    {platform} stays plain after "fuq" / "għal" or as a subject; never after "ta'".
    {audience} plural without the article ("{audience} ġodda"), because the article would
        assimilate differently (is-segwaċi, l-abbonati).
    {follow} third person plural ("jsegwuk", "jabbonaw"): every template gives it a plural
        subject ("nies veri li għażlu li {follow}").
    {profile}, {handle}, {content} carry the article and "tiegħek" ("il-profil tiegħek").
    {service} singular, the form after a number from 11 up ("{quantity} {service}": 1000 segwaċ).
"""

UI = {
    # Words that change with the platform or the service
    "audience": {"instagram": "segwaċi", "tiktok": "segwaċi", "youtube": "abbonati"},
    "follow": {"instagram": "jsegwuk", "tiktok": "jsegwuk", "youtube": "jabbonaw"},
    "profile": {"instagram": "il-profil tiegħek", "tiktok": "il-profil tiegħek", "youtube": "il-kanal tiegħek"},
    "handle": {"instagram": "l-isem tal-utent tiegħek", "tiktok": "l-isem tal-utent tiegħek", "youtube": "il-handle tal-kanal tiegħek"},
    "content": {"instagram": "il-posts tiegħek", "tiktok": "il-vidjows tiegħek", "youtube": "il-vidjows tiegħek"},
    "service_names": {"followers": "Segwaċi", "subscribers": "Abbonati", "likes": "Likes",
                      "views": "Veduti", "comments": "Kummenti"},
    "service_words": {"followers": "segwaċ", "subscribers": "abbonat", "likes": "like",
                      "views": "veduta", "comments": "kumment"},

    # Page chrome
    "home": "Paġna ewlenija",
    "crumbs_label": "Fejn tinsab",
    "eyebrow": "{platform} · {service_name}",
    "eyebrow_hub": "Tkabbir fuq {platform}",
    "cta": "Ibda bil-pakkett {pick_name}",
    "cta_more": "Ara l-pakketti kollha",
    "trust": ["Nies veri, qatt bots", "Qatt ma nitolbuk il-password", "Kull xahar, ikkanċella meta trid"],
    "product_name": "Pakketti ta' tkabbir għal {platform}",
    "sticky_cta": "Ibda",

    # Packages
    "packages_title": "Agħżel il-pakkett tiegħek",
    "packages_lead": "Tliet pakketti ta' kull xahar: {audience} ġodda, likes, veduti u kummenti jiġu flimkien, mill-istess nies veri.",
    "packages_note": "Firxiet tipiċi ta' kull xahar, mhux għadd fiss: {audience} ġodda jiġu biss minn nies veri li għażlu huma stess li {follow}, għalhekk kull xahar ikun xi ftit differenti.",

    # What's included: the page's own service comes first, then the rest in this order.
    "included_title": "X'jinkludi",
    "included_lead": "Kull pakkett iġib l-istampa sħiħa, mill-istess nies veri.",
    "included_items": {
        "audience": ("Aktar {audience}", "Nies veri li skoprew {profile} u għażlu li {follow}. Normalment {starter_audience} fix-xahar b'{starter_name}."),
        "likes": ("Likes mill-istess nies", "Normalment {starter_likes} fix-xahar b'{starter_name}, fuq {content} li jogħġbuhom."),
        "comments": ("Kummenti bi kliemhom stess", "Normalment {starter_comments} fix-xahar b'{starter_name}. Miktuba minn nies, qatt minn skripts."),
        "views": ("Veduti li jiġu miegħu", "L-istess nies jaraw {content} minn jeddhom. Ma ngħoddux il-veduti minn qabel: kull waħda hija persuna."),
        "days": ("Mifruxa fuq 30 jum", "Ftit kuljum, mill-post li tagħżel int. Qatt kollox f'daqqa."),
        "dashboard": ("Il-pannell tiegħek", "Dak li kejjilna, jum b'jum: iż-żjarat mill-kampanja tiegħek u kemm ġabu {audience} ġodda."),
    },

    # How it works: the subscription, step by step
    "steps_title": "Kif taħdem",
    "steps_lead": "Abbonament ta' kull xahar: int tagħżel il-pakkett, aħna nmexxu l-kampanja, in-nies veri jiddeċiedu.",
    "steps": [
        ("Agħżel pakkett", "{starter_name}, {rising_name} jew {pro_name}, imħallas kull xahar. Tista' tikkanċella meta trid mill-kont tiegħek."),
        ("Nibdew il-kampanja tiegħek", "Għidilna {handle} fuq {platform} u minn fejn għandha tiġi l-udjenza tiegħek. Qatt ma nitolbuk il-password."),
        ("Nies veri jiskopru {profile}", "Kuljum {profile} jintwera lil nies veri. Dawk li jogħġobhom dak li jaraw, {follow}, jagħtu like u jikkummentaw minn jeddhom."),
        ("Il-pannell juri dak li kejjilna", "Iż-żjarat mill-kampanja tiegħek u kemm ġabu {audience} ġodda, jum b'jum. Numri mkejla, qatt supożizzjonijiet."),
    ],

    # Real people vs bots / instant
    "compare_title": "Nies veri, mhux bots",
    "compare_lead": "Istantanju jfisser bots: nies veri ma jagħżlux li {follow} ftit sekondi wara ħlas.",
    "compare_cols": ("X'jinbidel", "Servizzi istantanji u bots", "Growsterr"),
    "compare": [
        ("Min huma", "Bots u profili foloz", "Nies veri li għażlu li {follow}"),
        ("Veloċità", "Eluf f'minuti", "Ftit kuljum, għax-xahar kollu"),
        ("Likes u kummenti", "Jinbiegħu separatament, minn aktar bots", "Mill-istess nies, ġewwa l-pakkett tiegħek"),
        ("Kemm-il persuna jaraw", "Jonqos bil-kwiet: meta l-udjenza qatt ma tinteraġixxi, {platform} jikkonkludi li {content} ma jistħoqqilhomx jintwerew", "Jikber ma' nies li jaraw, jagħtu like u jerġgħu jiġu"),
        ("Il-password tiegħek", "Spiss jitolbuha", "Qatt"),
        ("X'tara int", "Numru li jista' jisparixxi fit-tindif li jmiss", "Pannell b'dak li kejjilna"),
    ],

    # Quantity pages: how a monthly package gets you to the goal
    "quantity_title": "Kif tasal għal {quantity} {service}",
    "quantity_lead": "Ma nbigħux pakkett fiss ta' {quantity}. In-nies veri jiddeċiedu huma stess, għalhekk pakkett ta' kull xahar iwasslek hemm b'ritmu naturali.",
    "pace_title": "Ritmu tipiku b'{pick_name}",
    "pace_month": "Xahar {n}",
    "pace_goal": "Għan: {quantity}",
    "pace_note": "Firxiet tipiċi minn dak li jagħmlu nies veri, qatt wegħda. Xi xhur iġibu aktar, oħrajn inqas.",
    "by_plan_title": "Żmien biex tasal għal {quantity}, skont il-pakkett",
    "a_month": "{range} fix-xahar",
    "when_first": "normalment fl-ewwel xahar",
    "when_about": "normalment madwar {n} xhur",
    "when_range": "normalment {low}–{high} xhur",
    "views_pace": "Il-veduti jiġu mill-istess nies veri li jiskopru {profile}, għalhekk ma ngħoddhomx minn qabel. {pick_name} huwa l-pakkett li l-aħjar jaqbel ma' dan l-għan.",

    # FAQ, related pages, closing
    "faq_title": "Mistoqsijiet u tweġibiet",
    "related_title": "Kompli esplora",
    "related": {
        "platform": "Aktar dwar {platform}",
        "platforms": "Fuq pjattaformi oħra",
        "quantities": "Għanijiet oħra",
        "modifiers": "Modi oħra kif tikber",
        "articles": "Aqra wkoll",
        "hubs": "Ikber ma' nies veri fuq",
    },
    # The tools a page can carry ("tool"): they run in the browser, nothing is sent.
    "tools": {
        "calculate": "Ikkalkula",
        "followers": "Segwaċi",
        "avg_likes": "Medja ta' likes għal kull post",
        "avg_comments": "Medja ta' kummenti għal kull post",
        "engagement_title": "Ir-rata ta' interazzjoni tiegħek",
        "engagement_lead": "Kemm mis-segwaċi tiegħek jirreaġixxu għal post tipiku. Daħħal in-numri mill-aħħar ftit posts tiegħek.",
        "engagement_result": "Ir-rata ta' interazzjoni tiegħek hija {rate}%.",
        "engagement_note": "Ir-rata togħla meta n-nies li jsegwuk verament jieħdu interess fil-posts tiegħek. Segwaċi li qatt ma jirreaġixxu jbaxxuha, ikun x'ikun l-għadd tagħhom.",
        "growth_title": "Kemm iddum biex tasal għall-għan tiegħek?",
        "growth_lead": "Daħħal fejn int issa u fejn trid tasal. Nikkalkulawh mill-firxa tipika ta' kull xahar ta' kull pakkett.",
        "current": "Segwaċi llum",
        "goal": "L-għan tiegħek",
        "when_first": "normalment fl-ewwel xahar",
        "when_range": "normalment {low}–{high} xhur",
        "when_about": "madwar {n} xhur",
        "reached": "Diġà wasalt.",
        "growth_note": "Firxiet tipiċi, mhux wegħda: in-nies veri jiddeċiedu huma stess jekk isegwukx jew le.",
    },
    # Eyebrow above the headline of pages outside the platform x service grid (by "kind").
    "article_eyebrows": {
        "guide": "Gwida",
        "alternative": "Paragun",
        "payment": "Ħlasijiet",
        "agency": "Aġenzija tat-tkabbir",
        "tool": "Għodda",
        "intent": "Tweġiba diretta",
    },
    "cta_title": "Lest biex tikber fuq {platform}?",
    "cta_text": "Agħżel pakkett u nibdew il-kampanja tiegħek. Il-bqija jiddeċiduh nies veri, u l-pannell tiegħek juri dak li kejjilna.",

    # Platform hubs
    "services_title": "X'inkabbru fuq {platform}",
    "services_lead": "Pakkett wieħed iġib dan kollu, mill-istess nies veri.",
    "teasers": {
        "audience": "Nies veri li jiskopru {profile} u jagħżlu li {follow}.",
        "likes": "Likes min-nies li jħobbu {content}.",
        "views": "Veduti minn nies li jagħżlu li jaraw, qatt minn skripts.",
        "comments": "Kummenti miktuba minn nies veri, bi kliemhom stess.",
    },
    "explore": "Esplora",
    "in_package": "F'kull pakkett",
    "goals_title": "Aktar modi kif tikber fuq {platform}",
    "other_hubs_title": "Inkabbruk ukoll fuq",
}
