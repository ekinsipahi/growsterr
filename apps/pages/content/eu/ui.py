"""Basque UI of the money pages ("zu"). Mirrors en/ui.py key by key.

Basque attaches case endings to the noun, so these placeholders are bare stems and the ending
follows the placeholder: {audience} jarraitzaile/harpidedun ("{audience} berriak"),
{profile} profil/kanal ("zure {profile}a", "zure {profile}era"), {content} argitalpen/bideo
("zure {content}ak", "{content}etan"); both stems of each take the same endings.
{follow} is the verbal noun ("{follow} erabaki dute": jarraitzea / harpidetzea).
Never attach an ending to {platform}, {quantity} or a price: write "{platform} sarean",
"{platform} plataformari", "{starter_name} paketearekin", "{from_price} hilean".
"""

UI = {
    # Words that change with the platform or the service
    "audience": {"instagram": "jarraitzaile", "tiktok": "jarraitzaile", "youtube": "harpidedun"},
    "follow": {"instagram": "jarraitzea", "tiktok": "jarraitzea", "youtube": "harpidetzea"},
    "profile": {"instagram": "profil", "tiktok": "profil", "youtube": "kanal"},
    "handle": {"instagram": "erabiltzaile-izena", "tiktok": "erabiltzaile-izena", "youtube": "kanalaren identifikatzailea"},
    "content": {"instagram": "argitalpen", "tiktok": "bideo", "youtube": "bideo"},
    "service_names": {"followers": "Jarraitzaileak", "subscribers": "Harpidedunak", "likes": "Atsegiteak",
                      "views": "Ikustaldiak", "comments": "Iruzkinak"},
    "service_words": {"followers": "jarraitzaile", "subscribers": "harpidedun", "likes": "atsegite",
                      "views": "ikustaldi", "comments": "iruzkin"},

    # Page chrome
    "home": "Hasiera",
    "crumbs_label": "Nabigazio-bidea",
    "eyebrow": "{platform} · {service_name}",
    "eyebrow_hub": "{platform} hazkundea",
    "cta": "Hasi {pick_name} paketearekin",
    "cta_more": "Ikusi pakete guztiak",
    "trust": ["Pertsona errealak, inoiz ez botak", "Ez dizugu inoiz pasahitza eskatzen", "Hilekoa, nahi duzunean utz dezakezu"],
    "product_name": "{platform} hazteko paketeak",
    "sticky_cta": "Hasi",

    # Packages
    "packages_title": "Aukeratu zure paketea",
    "packages_lead": "Hiru hileko pakete. {audience} berriak, atsegiteak, ikustaldiak eta iruzkinak batera datoz, pertsona erreal berengandik.",
    "packages_note": "Hileko tarte ohikoak, ez kopuru finko bat: zure {audience} berri bakoitza {follow} erabaki duen pertsona erreal bat da, eta horregatik hilabete bakoitza apur bat desberdina da.",

    # What's included: the page's own service comes first, then the rest in this order.
    "included_title": "Zer dago barne",
    "included_lead": "Pakete bakoitzak irudi osoa dakar, pertsona erreal berengandik.",
    "included_items": {
        "audience": ("{audience} berriak", "Zure {profile}a ezagutu eta {follow} erabaki duten pertsona errealak. Normalean {starter_audience} hilean {starter_name} paketearekin."),
        "likes": ("Pertsona berengandik datozen atsegiteak", "Normalean {starter_likes} hilean {starter_name} paketearekin, gustuko dituzten {content}etan."),
        "comments": ("Iruzkinak, beren hitzekin", "Normalean {starter_comments} hilean {starter_name} paketearekin. Pertsonek idatziak, inoiz ez gidoi batetik."),
        "views": ("Ikustaldiak ere bai", "Pertsona berberek beren kabuz ikusten dituzte zure {content}ak. Ez ditugu ikustaldiak aldez aurretik zenbatzen: bakoitzaren atzean pertsona bat dago."),
        "days": ("30 egunetan banatuta", "Egunero pixka bat, zuk aukeratutako tokitik. Inoiz ez dena batera."),
        "dashboard": ("Zure panela", "Neurtu duguna, egunez egun: zure kanpainatik etorritako bisitak eta haiek ekarritako {audience} berriak."),
    },

    # How it works: the subscription, step by step
    "steps_title": "Nola funtzionatzen du",
    "steps_lead": "Hileko harpidetza bat: zuk paketea aukeratzen duzu, guk kanpaina kudeatzen dugu, pertsona errealek erabakitzen dute.",
    "steps": [
        ("Aukeratu pakete bat", "{starter_name}, {rising_name} edo {pro_name}, hilero kobratuta. Nahi duzunean utz dezakezu zure kontutik."),
        ("Zure kanpaina martxan jartzen dugu", "Esaguzu zure {platform} {handle} eta nondik etorri behar den zure publikoa. Ez dizugu inoiz pasahitza eskatzen."),
        ("Pertsona errealek zure {profile}a ezagutzen dute", "Egunero zure {profile}a pertsona errealei erakusten diegu. Ikusten dutena gustuko dutenek beren kabuz erabakitzen dute {follow}, eta atsegiteak eta iruzkinak uzten dituzte."),
        ("Zure panelak neurtu duguna erakusten du", "Zure kanpainatik etorritako bisitak eta haiek ekarritako {audience} berriak, egunez egun. Neurtutako zenbakiak, inoiz ez asmakizunak."),
    ],

    # Real people vs bots / instant
    "compare_title": "Pertsona errealak, ez botak",
    "compare_lead": "Berehalakoa botak esan nahi du: pertsona erreal batek ere ez du {follow} erabakitzen ordainketa baten ondorengo segundoetan.",
    "compare_cols": ("Zer aldatzen da", "Berehalako zerbitzuak eta botak", "Growsterr"),
    "compare": [
        ("Nor diren", "Botak eta profil faltsuak", "Pertsona errealak, {follow} erabaki dutenak"),
        ("Abiadura", "Milaka minutu gutxitan", "Egunero pixka bat, hilabete osoan"),
        ("Atsegiteak eta iruzkinak", "Bereiz saltzen dira, bot gehiagorengandik", "Pertsona berengandik, zure paketearen barruan"),
        ("Zure irismena", "Isilean jaisten da: inoiz parte hartzen ez duen publikoak {platform} plataformari esaten dio zure {content}ak ez direla erakusteko modukoak", "Ikusi, atsegin eta itzultzen diren pertsonekin hazten da"),
        ("Zure pasahitza", "Askotan eskatzen dute", "Inoiz ez"),
        ("Zer ikusten duzun", "Hurrengo garbiketan desager daitekeen zenbaki bat", "Neurtu dugunaren panel bat"),
    ],

    # Quantity pages: how a monthly package gets you to the goal
    "quantity_title": "Nola lortu {quantity} {service}",
    "quantity_lead": "Ez dugu {quantity} {service} dituen sorta finkorik saltzen. Pertsona errealek beren kabuz erabakitzen dute; beraz, hileko pakete batek erritmo naturalean eramango zaitu helburura.",
    "pace_title": "Ohiko erritmoa {pick_name} paketearekin",
    "pace_month": "{n}. hilabetea",
    "pace_goal": "Helburua: {quantity}",
    "pace_note": "Pertsona errealek egiten dutenetik ateratako ohiko tarteak, inoiz ez promesak. Hilabete batzuek gehiago ekartzen dute, beste batzuek gutxiago.",
    "by_plan_title": "{quantity} lortzeko denbora, paketearen arabera",
    "a_month": "{range} hilean",
    "when_first": "normalean lehen hilabetean",
    "when_about": "normalean {n} hilabete inguru",
    "when_range": "normalean {low}–{high} hilabete",
    "views_pace": "Ikustaldiak zure {profile}a ezagutzen duten pertsona erreal berengandik datoz; horregatik ez ditugu aldez aurretik zenbatzen. {pick_name} da helburu honetarako pakete egokiena.",

    # FAQ, related pages, closing
    "faq_title": "Galderak eta erantzunak",
    "related_title": "Jarraitu arakatzen",
    "related": {
        "platform": "{platform} sareari buruz gehiago",
        "platforms": "Beste plataforma batzuetan",
        "quantities": "Beste helburu batzuk",
        "modifiers": "Hazteko beste modu batzuk",
        "articles": "Irakurri hau ere",
        "hubs": "Hazi pertsona errealekin hemen:",
    },
    # The tools a page can carry ("tool"): they run in the browser, nothing is sent.
    "tools": {
        "calculate": "Kalkulatu",
        "followers": "Jarraitzaileak",
        "avg_likes": "Batez besteko atsegiteak argitalpeneko",
        "avg_comments": "Batez besteko iruzkinak argitalpeneko",
        "engagement_title": "Zure interakzio-tasa",
        "engagement_lead": "Zure jarraitzaileetatik zenbatek erreakzionatzen duten ohiko argitalpen batean. Idatzi zure azken argitalpenetako zenbakiak.",
        "engagement_result": "Zure interakzio-tasa: %{rate}.",
        "engagement_note": "Tasa igo egiten da zuri jarraitzen dizuten pertsonei zure argitalpenak benetan axola zaizkienean. Inoiz erreakzionatzen ez duten jarraitzaileek jaitsi egiten dute, zenbat diren gorabehera.",
        "growth_title": "Zenbat falta da zure helbururako?",
        "growth_lead": "Idatzi non zauden eta nora iritsi nahi duzun. Pakete bakoitzaren hileko ohiko tartearekin kalkulatzen dugu.",
        "current": "Jarraitzaileak gaur",
        "goal": "Zure helburua",
        "when_first": "normalean lehen hilabetean",
        "when_range": "normalean {low}–{high} hilabete",
        "when_about": "{n} hilabete inguru",
        "reached": "Iritsi zara jada.",
        "growth_note": "Ohiko tarteak, ez promesa bat: pertsona errealek erabakitzen dute zuri jarraitu ala ez.",
    },
    # Eyebrow above the headline of pages outside the platform x service grid (by "kind").
    "article_eyebrows": {
        "guide": "Gida",
        "alternative": "Konparazioa",
        "payment": "Ordainketak",
        "agency": "Hazkunde-agentzia",
        "tool": "Tresna",
        "intent": "Erantzun argia",
    },
    "cta_title": "Prest {platform} sarean hazteko?",
    "cta_text": "Aukeratu pakete bat eta zure kanpaina martxan jarriko dugu. Gainerakoa pertsona errealek erabakitzen dute, eta zure panelak neurtu duguna erakusten du.",

    # Platform hubs
    "services_title": "Zer hazten dugu {platform} sarean",
    "services_lead": "Pakete bakar batek dena dakar, pertsona erreal berengandik.",
    "teasers": {
        "audience": "Zure {profile}a ezagutu eta {follow} erabakitzen duten pertsona errealak.",
        "likes": "Zure {content}ak gustuko dituzten pertsonen atsegiteak.",
        "views": "Ikustea aukeratzen duten pertsonen ikustaldiak, inoiz ez scriptenak.",
        "comments": "Pertsona errealek beren hitzekin idatzitako iruzkinak.",
    },
    "explore": "Arakatu",
    "in_package": "Pakete guztietan barne",
    "goals_title": "{platform} sarean hazteko modu gehiago",
    "other_hubs_title": "Hemen ere hazten zaitugu",
}
