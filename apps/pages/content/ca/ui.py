"""Catalan UI of the money pages ("tu"). Mirrors en/ui.py key by key.

{follow} reads after "ha decidit": "seguir-te" / "subscriure-s'hi". {content} is masculine on
every platform ("els teus continguts", "els teus vídeos"). {platform} never follows a bare "de"
(Instagram would need "d'"): write "a {platform}". Likes are "m'agrades" (singular "m'agrada").
"""

UI = {
    # Words that change with the platform or the service
    "audience": {"instagram": "seguidors", "tiktok": "seguidors", "youtube": "subscriptors"},
    "follow": {"instagram": "seguir-te", "tiktok": "seguir-te", "youtube": "subscriure-s'hi"},
    "profile": {"instagram": "perfil", "tiktok": "perfil", "youtube": "canal"},
    "handle": {"instagram": "nom d'usuari", "tiktok": "nom d'usuari", "youtube": "identificador del canal"},
    "content": {"instagram": "continguts", "tiktok": "vídeos", "youtube": "vídeos"},
    "service_names": {"followers": "Seguidors", "subscribers": "Subscriptors", "likes": "M'agrades",
                      "views": "Visualitzacions", "comments": "Comentaris"},
    "service_words": {"followers": "seguidors", "subscribers": "subscriptors", "likes": "m'agrades",
                      "views": "visualitzacions", "comments": "comentaris"},

    # Page chrome
    "home": "Inici",
    "crumbs_label": "Camí de navegació",
    "eyebrow": "{platform} · {service_name}",
    "eyebrow_hub": "Creixement a {platform}",
    "cta": "Comença amb {pick_name}",
    "cta_more": "Mira tots els paquets",
    "trust": ["Persones reals, mai bots", "Mai et demanem la contrasenya", "Mensual, cancel·la quan vulguis"],
    "product_name": "Paquets de creixement per a {platform}",
    "sticky_cta": "Comença",

    # Packages
    "packages_title": "Tria el teu paquet",
    "packages_lead": "Tres paquets mensuals. Nous {audience}, m'agrades, visualitzacions i comentaris arriben junts, de les mateixes persones reals.",
    "packages_note": "Intervals mensuals habituals, no una xifra fixa: cadascun dels teus nous {audience} és una persona real que ha decidit {follow}, així que cada mes és una mica diferent.",

    # What's included: the page's own service comes first, then the rest in this order.
    "included_title": "Què inclou",
    "included_lead": "Cada paquet porta el conjunt complet, de les mateixes persones reals.",
    "included_items": {
        "audience": ("Nous {audience}", "Persones reals que han descobert el teu {profile} i han decidit {follow}. Normalment {starter_audience} al mes amb {starter_name}."),
        "likes": ("M'agrades de les mateixes persones", "Normalment {starter_likes} al mes amb {starter_name}, en els {content} que més els agraden."),
        "comments": ("Comentaris amb les seves paraules", "Normalment {starter_comments} al mes amb {starter_name}. Escrits per persones, mai amb guió."),
        "views": ("Visualitzacions incloses", "Les mateixes persones miren els teus {content} pel seu compte. No comptem les visualitzacions per avançat: darrere de cadascuna hi ha una persona."),
        "days": ("Repartit en 30 dies", "Una mica cada dia, des de la ubicació que triïs. Mai tot de cop."),
        "dashboard": ("El teu tauler", "El que hem mesurat, dia a dia: les visites de la teva campanya i els nous {audience} que han portat."),
    },

    # How it works: the subscription, step by step
    "steps_title": "Com funciona",
    "steps_lead": "Una subscripció mensual: tu tries el paquet, nosaltres portem la campanya, les persones reals decideixen.",
    "steps": [
        ("Tria un paquet", "{starter_name}, {rising_name} o {pro_name}, amb cobrament mensual. Cancel·la quan vulguis des del teu compte."),
        ("Engeguem la teva campanya", "Digues-nos el teu {handle} a {platform} i d'on ha de venir el teu públic. Mai et demanem la contrasenya."),
        ("Persones reals descobreixen el teu {profile}", "Cada dia mostrem el teu {profile} a persones reals. Qui gaudeix del que veu decideix pel seu compte {follow}, fer m'agrada i comentar."),
        ("El teu tauler mostra el que hem mesurat", "Les visites de la teva campanya i els nous {audience} que han portat, dia a dia. Xifres mesurades, mai suposicions."),
    ],

    # Real people vs bots / instant
    "compare_title": "Persones reals, no bots",
    "compare_lead": "Instantani vol dir bots: cap persona real no decideix {follow} uns segons després d'un pagament.",
    "compare_cols": ("Què canvia", "Serveis instantanis i bots", "Growsterr"),
    "compare": [
        ("Qui són", "Bots i perfils falsos", "Persones reals que han decidit {follow}"),
        ("Velocitat", "Milers en minuts", "Una mica cada dia, tot el mes"),
        ("M'agrades i comentaris", "Es venen a part, de més bots", "De les mateixes persones, dins del teu paquet"),
        ("El teu abast", "Cau en silenci: un públic que no interactua mai diu a {platform} que no val la pena mostrar els teus {content}", "Creix amb persones que miren, fan m'agrada i tornen"),
        ("La teva contrasenya", "Te la demanen sovint", "Mai"),
        ("El que veus", "Un número que pot desaparèixer en la propera neteja", "Un tauler amb el que hem mesurat"),
    ],

    # Quantity pages: how a monthly package gets you to the goal
    "quantity_title": "Com arribar a {quantity} {service}",
    "quantity_lead": "No venem un lot fix de {quantity}. Les persones reals decideixen per si mateixes, així que un paquet mensual t'hi porta a un ritme natural.",
    "pace_title": "Ritme habitual amb {pick_name}",
    "pace_month": "Mes {n}",
    "pace_goal": "Objectiu: {quantity}",
    "pace_note": "Intervals habituals basats en el que fan persones reals, mai una promesa. Alguns mesos en porten més, i d'altres, menys.",
    "by_plan_title": "Temps fins a {quantity}, per paquet",
    "a_month": "{range} al mes",
    "when_first": "normalment ja el primer mes",
    "when_about": "normalment uns {n} mesos",
    "when_range": "normalment {low}–{high} mesos",
    "views_pace": "Les visualitzacions provenen de les mateixes persones reals que descobreixen el teu {profile}, així que no les comptem per avançat. {pick_name} és el paquet que encaixa millor amb aquest objectiu.",

    # FAQ, related pages, closing
    "faq_title": "Preguntes i respostes",
    "related_title": "Continua explorant",
    "related": {
        "platform": "Més sobre {platform}",
        "platforms": "En altres plataformes",
        "quantities": "Altres objectius",
        "modifiers": "Altres maneres de créixer",
        "articles": "Continua llegint",
        "hubs": "Creix amb persones reals a",
    },
    # The tools a page can carry ("tool"): they run in the browser, nothing is sent.
    "tools": {
        "calculate": "Calcula",
        "followers": "Seguidors",
        "avg_likes": "M'agrades de mitjana per publicació",
        "avg_comments": "Comentaris de mitjana per publicació",
        "engagement_title": "La teva taxa d'interacció",
        "engagement_lead": "Quants dels teus seguidors reaccionen a una publicació típica. Escriu les xifres de les teves últimes publicacions.",
        "engagement_result": "La teva taxa d'interacció és del {rate} %.",
        "engagement_note": "La taxa puja quan a les persones que et segueixen els importen de debò les teves publicacions. Els seguidors que no reaccionen mai la fan baixar, siguin quants siguin.",
        "growth_title": "Quant falta per al teu objectiu?",
        "growth_lead": "Escriu on ets i on vols arribar. Ho calculem amb l'interval mensual habitual de cada paquet.",
        "current": "Seguidors avui",
        "goal": "El teu objectiu",
        "when_first": "normalment ja el primer mes",
        "when_range": "normalment {low}–{high} mesos",
        "when_about": "uns {n} mesos",
        "reached": "Ja hi has arribat.",
        "growth_note": "Intervals habituals, no una promesa: les persones reals decideixen per si mateixes si et segueixen.",
    },
    # Eyebrow above the headline of pages outside the platform x service grid (by "kind").
    "article_eyebrows": {
        "guide": "Guia",
        "alternative": "Comparativa",
        "payment": "Pagaments",
        "agency": "Agència de creixement",
        "tool": "Eina",
        "intent": "Resposta clara",
    },
    "cta_title": "A punt per créixer a {platform}?",
    "cta_text": "Tria un paquet i engeguem la teva campanya. Les persones reals decideixen la resta, i el teu tauler mostra el que hem mesurat.",

    # Platform hubs
    "services_title": "Què fem créixer a {platform}",
    "services_lead": "Un sol paquet ho porta tot, de les mateixes persones reals.",
    "teasers": {
        "audience": "Persones reals que descobreixen el teu {profile} i decideixen {follow}.",
        "likes": "M'agrades de persones que gaudeixen dels teus {content}.",
        "views": "Visualitzacions de persones que trien mirar, mai de scripts.",
        "comments": "Comentaris escrits per persones reals, amb les seves paraules.",
    },
    "explore": "Explora",
    "in_package": "Inclòs en cada paquet",
    "goals_title": "Més maneres de créixer a {platform}",
    "other_hubs_title": "També et fem créixer a",
}
