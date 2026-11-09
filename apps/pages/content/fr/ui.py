"""French UI of the money pages ("vous"). Mirrors en/ui.py key by key.

{audience} is "abonnés" on every platform, as in apps/growth/i18n/fr.py. {follow} reads after
"choisi de": "vous suivre" / "s'abonner". {profile} is profil (m) or chaîne (f): write "votre
{profile}" and never an article or adjective that agrees with it.
"""

UI = {
    # Words that change with the platform or the service
    "audience": {"instagram": "abonnés", "tiktok": "abonnés", "youtube": "abonnés"},
    "follow": {"instagram": "vous suivre", "tiktok": "vous suivre", "youtube": "s'abonner"},
    "profile": {"instagram": "profil", "tiktok": "profil", "youtube": "chaîne"},
    "handle": {"instagram": "nom d'utilisateur", "tiktok": "nom d'utilisateur", "youtube": "identifiant de chaîne"},
    "content": {"instagram": "publications", "tiktok": "vidéos", "youtube": "vidéos"},
    "service_names": {"followers": "Abonnés", "subscribers": "Abonnés", "likes": "Likes",
                      "views": "Vues", "comments": "Commentaires"},
    "service_words": {"followers": "abonnés", "subscribers": "abonnés", "likes": "likes",
                      "views": "vues", "comments": "commentaires"},

    # Page chrome
    "home": "Accueil",
    "crumbs_label": "Fil d'Ariane",
    "eyebrow": "{platform} · {service_name}",
    "eyebrow_hub": "Croissance {platform}",
    "cta": "Commencer avec {pick_name}",
    "cta_more": "Voir tous les packs",
    "trust": ["De vraies personnes, jamais de bots", "Nous ne demandons jamais votre mot de passe", "Mensuel, résiliable à tout moment"],
    "product_name": "Packs de croissance {platform}",
    "sticky_cta": "Commencer",

    # Packages
    "packages_title": "Choisissez votre pack",
    "packages_lead": "Trois packs mensuels. Nouveaux {audience}, likes, vues et commentaires arrivent ensemble, des mêmes vraies personnes.",
    "packages_note": "Des fourchettes mensuelles habituelles, pas un nombre fixe : chacun de vos nouveaux {audience} est une vraie personne qui a choisi de {follow}, donc chaque mois est un peu différent.",

    # What's included: the page's own service comes first, then the rest in this order.
    "included_title": "Ce qui est inclus",
    "included_lead": "Chaque pack apporte l'ensemble, venant des mêmes vraies personnes.",
    "included_items": {
        "audience": ("Nouveaux {audience}", "De vraies personnes qui ont découvert votre {profile} et choisi de {follow}. En général {starter_audience} par mois avec {starter_name}."),
        "likes": ("Des likes des mêmes personnes", "En général {starter_likes} par mois avec {starter_name}, sur les {content} qu'elles aiment."),
        "comments": ("Des commentaires avec leurs mots", "En général {starter_comments} par mois avec {starter_name}. Écrits par des personnes, jamais scriptés."),
        "views": ("Des vues en prime", "Les mêmes personnes regardent vos {content} d'elles-mêmes. Nous ne comptons pas les vues à l'avance : chacune est une personne."),
        "days": ("Réparti sur 30 jours", "Un peu chaque jour, depuis le lieu de votre choix. Jamais tout d'un coup."),
        "dashboard": ("Votre tableau de bord", "Ce que nous avons mesuré, jour après jour : les visites venues de votre campagne et les nouveaux {audience} qu'elles ont apportés."),
    },

    # How it works: the subscription, step by step
    "steps_title": "Comment ça marche",
    "steps_lead": "Un abonnement mensuel : vous choisissez le pack, nous menons la campagne, de vraies personnes décident.",
    "steps": [
        ("Choisissez un pack", "{starter_name}, {rising_name} ou {pro_name}, facturé chaque mois. Résiliable à tout moment depuis votre compte."),
        ("Nous lançons votre campagne", "Indiquez-nous votre {handle} {platform} et d'où doit venir votre audience. Nous ne demandons jamais votre mot de passe."),
        ("De vraies personnes découvrent votre {profile}", "Chaque jour, nous présentons votre {profile} à de vraies personnes. Celles qui aiment ce qu'elles voient choisissent de {follow}, d'aimer et de commenter, d'elles-mêmes."),
        ("Votre tableau de bord montre ce que nous avons mesuré", "Les visites venues de votre campagne et les nouveaux {audience} qu'elles ont apportés, jour après jour. Des chiffres mesurés, jamais des suppositions."),
    ],

    # Real people vs bots / instant
    "compare_title": "De vraies personnes, pas des bots",
    "compare_lead": "Instantané veut dire bots : aucune vraie personne ne choisit de {follow} quelques secondes après un paiement.",
    "compare_cols": ("Ce qui change", "Services instantanés et bots", "Growsterr"),
    "compare": [
        ("Qui ils sont", "Des bots et de faux profils", "De vraies personnes qui ont choisi de {follow}"),
        ("Vitesse", "Des milliers en quelques minutes", "Un peu chaque jour, tout le mois"),
        ("Likes et commentaires", "Vendus à part, par encore plus de bots", "Des mêmes personnes, inclus dans votre pack"),
        ("Votre portée", "Baisse en silence : une audience qui n'interagit jamais dit à {platform} que vos {content} ne valent pas la peine d'être montrées", "Grandit avec des personnes qui regardent, aiment et reviennent"),
        ("Votre mot de passe", "Souvent demandé", "Jamais"),
        ("Ce que vous voyez", "Un chiffre qui peut disparaître au prochain nettoyage", "Un tableau de bord de ce que nous avons mesuré"),
    ],

    # Quantity pages: how a monthly package gets you to the goal
    "quantity_title": "Comment atteindre {quantity} {service}",
    "quantity_lead": "Nous ne vendons pas un lot fixe de {quantity}. De vraies personnes décident par elles-mêmes, alors un pack mensuel vous y amène à un rythme naturel.",
    "pace_title": "Rythme habituel avec {pick_name}",
    "pace_month": "Mois {n}",
    "pace_goal": "Objectif : {quantity}",
    "pace_note": "Des fourchettes habituelles, tirées de ce que font de vraies personnes, jamais une promesse. Certains mois apportent plus, d'autres moins.",
    "by_plan_title": "Délai pour {quantity}, par pack",
    "a_month": "{range} par mois",
    "when_first": "généralement dès le premier mois",
    "when_about": "généralement environ {n} mois",
    "when_range": "généralement {low} à {high} mois",
    "views_pace": "Les vues viennent des mêmes vraies personnes qui découvrent votre {profile}, donc nous ne les comptons pas à l'avance. {pick_name} est le pack le mieux adapté à cet objectif.",

    # FAQ, related pages, closing
    "faq_title": "Vos questions, nos réponses",
    "related_title": "À explorer aussi",
    "related": {
        "platform": "Plus sur {platform}",
        "platforms": "Sur les autres plateformes",
        "quantities": "Autres objectifs",
        "modifiers": "D'autres façons de grandir",
        "articles": "À lire ensuite",
        "hubs": "Grandir avec de vraies personnes sur",
    },
    # The tools a page can carry ("tool"): they run in the browser, nothing is sent.
    "tools": {
        "calculate": "Calculer",
        "followers": "Abonnés",
        "avg_likes": "Likes moyens par publication",
        "avg_comments": "Commentaires moyens par publication",
        "engagement_title": "Votre taux d'engagement",
        "engagement_lead": "Combien de vos abonnés réagissent à une publication typique. Saisissez les chiffres de vos dernières publications.",
        "engagement_result": "Votre taux d'engagement est de {rate} %.",
        "engagement_note": "Le taux monte quand les personnes qui vous suivent s'intéressent vraiment à vos publications. Les abonnés qui ne réagissent jamais le font baisser, quel que soit leur nombre.",
        "growth_title": "Combien de temps jusqu'à votre objectif ?",
        "growth_lead": "Indiquez où vous en êtes et où vous voulez aller. Nous le calculons à partir de la fourchette mensuelle habituelle de chaque pack.",
        "current": "Abonnés aujourd'hui",
        "goal": "Votre objectif",
        "when_first": "généralement dès le premier mois",
        "when_range": "généralement {low} à {high} mois",
        "when_about": "environ {n} mois",
        "reached": "Vous y êtes déjà.",
        "growth_note": "Des fourchettes habituelles, pas une promesse : de vraies personnes décident elles-mêmes de vous suivre ou non.",
    },
    # Eyebrow above the headline of pages outside the platform x service grid (by "kind").
    "article_eyebrows": {
        "guide": "Guide",
        "alternative": "Comparatif",
        "payment": "Paiement",
        "agency": "Agence de croissance",
        "tool": "Outil",
        "intent": "Réponse franche",
    },
    "cta_title": "Prêt à grandir sur {platform} ?",
    "cta_text": "Choisissez un pack et nous lançons votre campagne. De vraies personnes décident du reste, et votre tableau de bord montre ce que nous avons mesuré.",

    # Platform hubs
    "services_title": "Ce que nous faisons grandir sur {platform}",
    "services_lead": "Un seul pack apporte tout cela, des mêmes vraies personnes.",
    "teasers": {
        "audience": "De vraies personnes qui découvrent votre {profile} et choisissent de {follow}.",
        "likes": "Des likes de personnes qui aiment vos {content}.",
        "views": "Des vues de personnes qui choisissent de regarder, jamais de scripts.",
        "comments": "Des commentaires écrits par de vraies personnes, avec leurs propres mots.",
    },
    "explore": "Découvrir",
    "in_package": "Inclus dans chaque pack",
    "goals_title": "D'autres façons de grandir sur {platform}",
    "other_hubs_title": "Nous vous faisons aussi grandir sur",
}
