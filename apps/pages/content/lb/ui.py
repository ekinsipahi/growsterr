"""Luxembourgish UI of the money pages (formal "Dir"). Mirrors en/ui.py key by key.

Grammar notes for the placeholders (the Eifel n-rule decides most of them):
    {platform} never follows a word that can drop its final n ("op {platform}", "{platform}-…").
    {audience} plural ("Follower", "Abonnenten"); it is always followed by punctuation, the end
        of the string or a word starting with a vowel or n, d, t, z, h, so "Abonnenten" keeps its n.
    {follow} zu-infinitive clause, set off by commas ("decidéiert hunn, {follow}").
    {profile}, {handle} masculine with "Äre" ("Äre Profil", "Äre Kanal-Handle"), nominative or accusative.
    {content} plural with "Är" ("Är Posts", "Är Videoen"), followed by punctuation or a vowel.
    {service} plural at the end of the string ("op {quantity} {service}").
"""

UI = {
    # Words that change with the platform or the service
    "audience": {"instagram": "Follower", "tiktok": "Follower", "youtube": "Abonnenten"},
    "follow": {"instagram": "Iech ze follegen", "tiktok": "Iech ze follegen", "youtube": "Äre Kanal z'abonnéieren"},
    "profile": {"instagram": "Äre Profil", "tiktok": "Äre Profil", "youtube": "Äre Kanal"},
    "handle": {"instagram": "Äre Benotzernumm", "tiktok": "Äre Benotzernumm", "youtube": "Äre Kanal-Handle"},
    "content": {"instagram": "Är Posts", "tiktok": "Är Videoen", "youtube": "Är Videoen"},
    "service_names": {"followers": "Follower", "subscribers": "Abonnenten", "likes": "Likes",
                      "views": "Views", "comments": "Kommentaren"},
    "service_words": {"followers": "Follower", "subscribers": "Abonnenten", "likes": "Likes",
                      "views": "Views", "comments": "Kommentaren"},

    # Page chrome
    "home": "Startsäit",
    "crumbs_label": "Navigatiounswee",
    "eyebrow": "{platform} · {service_name}",
    "eyebrow_hub": "{platform}-Wuesstem",
    "cta": "Mat {pick_name} starten",
    "cta_more": "All Paketen ukucken",
    "trust": ["Echt Mënschen, ni Bots", "Mir froen Iech ni no Ärem Passwuert", "Monatlech, all Moment kënnegbar"],
    "product_name": "{platform}-Wuesstemspaketen",
    "sticky_cta": "Starten",

    # Packages
    "packages_title": "Wielt Äert Paket",
    "packages_lead": "Dräi Monatspaketen. Nei {audience}, Likes, Views a Kommentare kommen zesummen, vun deene selwechten echte Mënschen.",
    "packages_note": "Typesch Wäerter pro Mount, keng fix Zuel: Är nei {audience} hu sech all selwer decidéiert, {follow}, dofir ass all Mount e bësse anescht.",

    # What's included: the page's own service comes first, then the rest in this order.
    "included_title": "Wat dran ass",
    "included_lead": "All Paket bréngt dat ganzt Bild, vun deene selwechten echte Mënschen.",
    "included_items": {
        "audience": ("Nei {audience}", "Echt Mënschen, déi {profile} entdeckt an decidéiert hunn, {follow}. Typescherweis {starter_audience} pro Mount mat {starter_name}."),
        "likes": ("Likes vun deene selwechte Mënschen", "Typescherweis {starter_likes} pro Mount mat {starter_name}, op {content}, déi hinne gefalen."),
        "comments": ("Kommentaren an hiren eegene Wierder", "Typescherweis {starter_comments} pro Mount mat {starter_name}. Vu Mënsche geschriwwen, ni vu Skripter."),
        "views": ("Views kommen dobäi", "Déi selwecht Mënsche kucken {content}, ganz vun eleng. Mir zielen d'Views net am Viraus: Hannert jidderengem stécht e Mënsch."),
        "days": ("Verdeelt iwwer 30 Deeg", "All Dag e bëssen, vun der Plaz, déi Dir wielt. Ni alles op eemol."),
        "dashboard": ("Äert Dashboard", "Wat mir gemooss hunn, Dag fir Dag: d'Besich vun Ärer Campagne an déi nei {audience}, déi se bruecht hunn."),
    },

    # How it works: the subscription, step by step
    "steps_title": "Sou fonctionéiert et",
    "steps_lead": "E Monatsabonnement: Dir wielt d'Paket, mir féieren d'Campagne, echt Mënschen decidéieren.",
    "steps": [
        ("Wielt e Paket", "{starter_name}, {rising_name} oder {pro_name}, monatlech ofgerechent. All Moment an Ärem Kont kënnegbar."),
        ("Mir starten Är Campagne", "Gitt eis {handle} op {platform} un a sot eis, vu wou Äert Publikum soll kommen. Mir froen Iech ni no Ärem Passwuert."),
        ("Echt Mënschen entdecken {profile}", "All Dag gëtt {profile} echte Mënsche gewisen. Déi, deenen et gefält, wat se gesinn, decidéiere selwer, {follow}, ze liken an ze kommentéieren."),
        ("Äert Dashboard weist, wat mir gemooss hunn", "D'Besich vun Ärer Campagne an déi nei {audience}, déi se bruecht hunn, Dag fir Dag. Gemoossen Zuelen, ni Vermutungen."),
    ],

    # Real people vs bots / instant
    "compare_title": "Echt Mënschen, keng Bots",
    "compare_lead": "Sofort heescht Bots: Keen echte Mënsch decidéiert sech, {follow}, e puer Sekonnen no enger Bezuelung.",
    "compare_cols": ("Wat sech ännert", "Sofort- a Bot-Servicer", "Growsterr"),
    "compare": [
        ("Wien et ass", "Bots a falsch Profiller", "Echt Mënschen, déi decidéiert hunn, {follow}"),
        ("Tempo", "Dausende bannent Minutten", "All Dag e bëssen, de ganze Mount"),
        ("Likes a Kommentaren", "Separat verkaaft, vu nach méi Bots", "Vun deene selwechte Mënschen, an Ärem Paket"),
        ("Är Reechwäit", "Fält roueg: E Publikum, dat ni interagéiert, weist {platform}, datt {content} et net wäert sinn, gewisen ze ginn", "Wiisst mat Mënschen, déi kucken, liken an erëmkommen"),
        ("Äert Passwuert", "Gëtt dacks gefrot", "Ni"),
        ("Wat Dir gesitt", "Eng Zuel, déi bei der nächster Botzaktioun verschwanne kann", "En Dashboard mat deem, wat mir gemooss hunn"),
    ],

    # Quantity pages: how a monthly package gets you to the goal
    "quantity_title": "Sou kommt Dir op {quantity} {service}",
    "quantity_lead": "Mir verkafe kee fixt Paket mat {quantity}. Echt Mënschen decidéiere selwer, dofir bréngt e Monatspaket Iech an engem natierlechen Tempo dohinner.",
    "pace_title": "Typeschen Tempo mat {pick_name}",
    "pace_month": "Mount {n}",
    "pace_goal": "Zil: {quantity}",
    "pace_note": "Typesch Spannen aus deem, wat echt Mënsche maachen, ni e Verspriechen. Verschidde Méint bréngen der méi, anerer manner.",
    "by_plan_title": "Zäit bis {quantity}, no Paket",
    "a_month": "{range} pro Mount",
    "when_first": "meeschtens am éischte Mount",
    "when_about": "meeschtens ongeféier {n} Méint",
    "when_range": "meeschtens {low}–{high} Méint",
    "views_pace": "Views komme vun deene selwechten echte Mënschen, déi {profile} entdecken, dofir ziele mir se net am Viraus. {pick_name} ass d'Paket, dat am beschten zu dësem Zil passt.",

    # FAQ, related pages, closing
    "faq_title": "Froen an Äntwerten",
    "related_title": "Weider entdecken",
    "related": {
        "platform": "Méi iwwer {platform}",
        "platforms": "Op anere Plattformen",
        "quantities": "Aner Ziler",
        "modifiers": "Aner Weeër ze wuessen",
        "articles": "Weider liesen",
        "hubs": "Mat echte Mënsche wuessen op",
    },
    # The tools a page can carry ("tool"): they run in the browser, nothing is sent.
    "tools": {
        "calculate": "Berechnen",
        "followers": "Follower",
        "avg_likes": "Duerchschnëttlech Likes pro Post",
        "avg_comments": "Duerchschnëttlech Kommentare pro Post",
        "engagement_title": "Är Engagement-Rate",
        "engagement_lead": "Wéi vill vun Äre Follower op en typesche Post reagéieren. Gitt d'Zuele vun Äre leschte Posts an.",
        "engagement_result": "Är Engagement-Rate ass {rate}%.",
        "engagement_note": "D'Rate klëmmt, wann d'Leit, déi Iech follegen, sech wierklech fir Är Posts interesséieren. Follower, déi ni reagéieren, drécke se, egal wéi vill der sinn.",
        "growth_title": "Wéi laang bis zu Ärem Zil?",
        "growth_lead": "Gitt an, wou Dir elo sidd a wou Dir hiwëllt. Mir rechnen et aus der typescher Monatsspann vun all Paket aus.",
        "current": "Follower haut",
        "goal": "Äert Zil",
        "when_first": "meeschtens am éischte Mount",
        "when_range": "meeschtens {low}–{high} Méint",
        "when_about": "ongeféier {n} Méint",
        "reached": "Dir sidd schonn do.",
        "growth_note": "Typesch Spannen, kee Verspriechen: Echt Mënschen decidéiere selwer, ob se Iech follegen.",
    },
    # Eyebrow above the headline of pages outside the platform x service grid (by "kind").
    "article_eyebrows": {
        "guide": "Guide",
        "alternative": "Vergläich",
        "payment": "Bezuelen",
        "agency": "Wuesstemsagence",
        "tool": "Tool",
        "intent": "Kloer Äntwert",
    },
    "cta_title": "Prett fir op {platform} ze wuessen?",
    "cta_text": "Wielt e Paket a mir starten Är Campagne. De Rescht decidéieren echt Mënschen, an Äert Dashboard weist, wat mir gemooss hunn.",

    # Platform hubs
    "services_title": "Wat mir op {platform} wuesse loossen",
    "services_lead": "Ee Paket bréngt dat alles, vun deene selwechten echte Mënschen.",
    "teasers": {
        "audience": "Echt Mënschen, déi {profile} entdecken an decidéieren, {follow}.",
        "likes": "Likes vu Leit, déi sech fir {content} interesséieren.",
        "views": "Views vu Leit, déi selwer decidéieren ze kucken, ni vu Skripter.",
        "comments": "Kommentaren, déi echt Mënschen an hiren eegene Wierder schreiwen.",
    },
    "explore": "Entdecken",
    "in_package": "An all Paket",
    "goals_title": "Méi Weeër, fir op {platform} ze wuessen",
    "other_hubs_title": "Mir loossen Iech och wuessen op",
}
