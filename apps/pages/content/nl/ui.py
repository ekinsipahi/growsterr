"""Dutch UI of the money pages (formal "u"). Mirrors en/ui.py key by key.

{follow} reads after "ervoor kiezen": "u te volgen" / "zich te abonneren".
"""

UI = {
    # Words that change with the platform or the service
    "audience": {"instagram": "volgers", "tiktok": "volgers", "youtube": "abonnees"},
    "follow": {"instagram": "u te volgen", "tiktok": "u te volgen", "youtube": "zich te abonneren"},
    "profile": {"instagram": "profiel", "tiktok": "profiel", "youtube": "kanaal"},
    "handle": {"instagram": "gebruikersnaam", "tiktok": "gebruikersnaam", "youtube": "kanaalhandle"},
    "content": {"instagram": "berichten", "tiktok": "video's", "youtube": "video's"},
    "service_names": {"followers": "Volgers", "subscribers": "Abonnees", "likes": "Likes",
                      "views": "Views", "comments": "Reacties"},
    "service_words": {"followers": "volgers", "subscribers": "abonnees", "likes": "likes",
                      "views": "views", "comments": "reacties"},

    # Page chrome
    "home": "Home",
    "crumbs_label": "Kruimelpad",
    "eyebrow": "{platform} · {service_name}",
    "eyebrow_hub": "{platform}-groei",
    "cta": "Begin met {pick_name}",
    "cta_more": "Bekijk alle pakketten",
    "trust": ["Echte mensen, nooit bots", "We vragen nooit om uw wachtwoord", "Maandelijks, altijd opzegbaar"],
    "product_name": "{platform}-groeipakketten",
    "sticky_cta": "Starten",

    # Packages
    "packages_title": "Kies uw pakket",
    "packages_lead": "Drie maandpakketten. Nieuwe {audience}, likes, views en reacties komen samen, van dezelfde echte mensen.",
    "packages_note": "Typische maandbereiken, geen vast aantal: elk van uw nieuwe {audience} is een echt mens die ervoor koos {follow}, dus elke maand is net iets anders.",

    # What's included: the page's own service comes first, then the rest in this order.
    "included_title": "Wat er inbegrepen is",
    "included_lead": "Elk pakket brengt het hele plaatje, van dezelfde echte mensen.",
    "included_items": {
        "audience": ("Nieuwe {audience}", "Echte mensen die uw {profile} ontdekten en ervoor kozen {follow}. Met {starter_name} doorgaans {starter_audience} per maand."),
        "likes": ("Likes van dezelfde mensen", "Met {starter_name} doorgaans {starter_likes} per maand, op de {content} die ze leuk vinden."),
        "comments": ("Reacties in hun eigen woorden", "Met {starter_name} doorgaans {starter_comments} per maand. Geschreven door mensen, nooit volgens een script."),
        "views": ("Views die erbij horen", "Dezelfde mensen bekijken uw {content} uit zichzelf. Views tellen we niet vooraf: achter elke view zit een mens."),
        "days": ("Verspreid over 30 dagen", "Elke dag een beetje, vanuit de locatie die u kiest. Nooit alles tegelijk."),
        "dashboard": ("Uw dashboard", "Wat we hebben gemeten, dag voor dag: bezoeken vanuit uw campagne en de nieuwe {audience} die ze opleverden."),
    },

    # How it works: the subscription, step by step
    "steps_title": "Zo werkt het",
    "steps_lead": "Een maandabonnement: u kiest het pakket, wij voeren de campagne, echte mensen beslissen.",
    "steps": [
        ("Kies een pakket", "{starter_name}, {rising_name} of {pro_name}, maandelijks gefactureerd. Altijd opzegbaar vanuit uw account."),
        ("Wij starten uw campagne", "Geef ons uw {platform}-{handle} en vertel waar uw publiek vandaan moet komen. We vragen nooit om uw wachtwoord."),
        ("Echte mensen ontdekken uw {profile}", "Elke dag wordt uw {profile} aan echte mensen getoond. Wie leuk vindt wat hij ziet, kiest er zelf voor {follow}, te liken en te reageren."),
        ("Uw dashboard toont wat we hebben gemeten", "Bezoeken vanuit uw campagne en de nieuwe {audience} die ze opleverden, dag voor dag. Gemeten cijfers, nooit schattingen."),
    ],

    # Real people vs bots / instant
    "compare_title": "Echte mensen, geen bots",
    "compare_lead": "Direct betekent bots: geen echt mens besluit seconden na een betaling {follow}.",
    "compare_cols": ("Wat er verandert", "Directe diensten en bots", "Growsterr"),
    "compare": [
        ("Wie het zijn", "Bots en nepprofielen", "Echte mensen die ervoor kozen {follow}"),
        ("Tempo", "Duizenden in minuten", "Elke dag een beetje, de hele maand"),
        ("Likes en reacties", "Apart verkocht, van nog meer bots", "Van dezelfde mensen, in uw pakket"),
        ("Uw bereik", "Daalt ongemerkt: een publiek dat nooit reageert, vertelt {platform} dat uw {content} het tonen niet waard zijn", "Groeit met mensen die kijken, liken en terugkomen"),
        ("Uw wachtwoord", "Wordt vaak gevraagd", "Nooit"),
        ("Wat u ziet", "Een getal dat bij de volgende opschoning kan verdwijnen", "Een dashboard met wat we hebben gemeten"),
    ],

    # Quantity pages: how a monthly package gets you to the goal
    "quantity_title": "Zo bereikt u {quantity} {service}",
    "quantity_lead": "We verkopen geen vast pakket van {quantity}. Echte mensen beslissen zelf, dus een maandpakket brengt u er in een natuurlijk tempo.",
    "pace_title": "Typisch tempo met {pick_name}",
    "pace_month": "Maand {n}",
    "pace_goal": "Doel: {quantity}",
    "pace_note": "Typische bereiken op basis van wat echte mensen doen, nooit een belofte. Sommige maanden brengen meer, andere minder.",
    "by_plan_title": "Tijd tot {quantity}, per pakket",
    "a_month": "{range} per maand",
    "when_first": "meestal binnen de eerste maand",
    "when_about": "meestal ongeveer {n} maanden",
    "when_range": "meestal {low}–{high} maanden",
    "views_pace": "Views komen van dezelfde echte mensen die uw {profile} ontdekken, dus we tellen ze niet vooraf. {pick_name} is het pakket dat het best bij dit doel past.",

    # FAQ, related pages, closing
    "faq_title": "Vragen en antwoorden",
    "related_title": "Verder ontdekken",
    "related": {
        "platform": "Meer over {platform}",
        "platforms": "Op andere platforms",
        "quantities": "Andere doelen",
        "modifiers": "Andere manieren om te groeien",
        "articles": "Lees verder",
        "hubs": "Groei met echte mensen op",
    },
    # The tools a page can carry ("tool"): they run in the browser, nothing is sent.
    "tools": {
        "calculate": "Berekenen",
        "followers": "Volgers",
        "avg_likes": "Gemiddeld aantal likes per bericht",
        "avg_comments": "Gemiddeld aantal reacties per bericht",
        "engagement_title": "Uw engagementratio",
        "engagement_lead": "Hoeveel van uw volgers reageren op een gemiddeld bericht. Vul de cijfers van uw laatste berichten in.",
        "engagement_result": "Uw engagementratio is {rate}%.",
        "engagement_note": "De ratio stijgt als de mensen die u volgen echt om uw berichten geven. Volgers die nooit reageren, trekken hem omlaag, hoeveel het er ook zijn.",
        "growth_title": "Hoe lang tot uw doel?",
        "growth_lead": "Vul in waar u nu staat en waar u naartoe wilt. We rekenen het uit met het typische maandbereik van elk pakket.",
        "current": "Volgers vandaag",
        "goal": "Uw doel",
        "when_first": "meestal binnen de eerste maand",
        "when_range": "meestal {low}–{high} maanden",
        "when_about": "ongeveer {n} maanden",
        "reached": "U bent er al.",
        "growth_note": "Typische bereiken, geen belofte: echte mensen beslissen zelf of ze volgen.",
    },
    # Eyebrow above the headline of pages outside the platform x service grid (by "kind").
    "article_eyebrows": {
        "guide": "Gids",
        "alternative": "Vergelijking",
        "payment": "Betalen",
        "agency": "Groeibureau",
        "tool": "Tool",
        "intent": "Eerlijk antwoord",
    },
    "cta_title": "Klaar om te groeien op {platform}?",
    "cta_text": "Kies een pakket en we starten uw campagne. Echte mensen beslissen de rest, en uw dashboard toont wat we hebben gemeten.",

    # Platform hubs
    "services_title": "Wat we laten groeien op {platform}",
    "services_lead": "Eén pakket brengt het allemaal, van dezelfde echte mensen.",
    "teasers": {
        "audience": "Echte mensen die uw {profile} ontdekken en ervoor kiezen {follow}.",
        "likes": "Likes van mensen die uw {content} leuk vinden.",
        "views": "Views van mensen die zelf kiezen om te kijken, nooit van scripts.",
        "comments": "Reacties van echte mensen, in hun eigen woorden.",
    },
    "explore": "Ontdekken",
    "in_package": "In elk pakket",
    "goals_title": "Meer manieren om te groeien op {platform}",
    "other_hubs_title": "We laten u ook groeien op",
}
