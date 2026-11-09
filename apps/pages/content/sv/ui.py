"""Swedish UI of the money pages (mirrors en/ui.py key by key).
{profile} profil/kanal and {handle} användarnamn/kanalhandtag share a gender, so "din {profile}"
and "ditt {handle}" read right on every platform; {content} is plural (dina inlägg, dina videor)."""

UI = {
    # Words that change with the platform or the service
    "audience": {"instagram": "följare", "tiktok": "följare", "youtube": "prenumeranter"},
    "follow": {"instagram": "följa", "tiktok": "följa", "youtube": "prenumerera"},
    "profile": {"instagram": "profil", "tiktok": "profil", "youtube": "kanal"},
    "handle": {"instagram": "användarnamn", "tiktok": "användarnamn", "youtube": "kanalhandtag"},
    "content": {"instagram": "inlägg", "tiktok": "videor", "youtube": "videor"},
    "service_names": {"followers": "Följare", "subscribers": "Prenumeranter", "likes": "Likes",
                      "views": "Visningar", "comments": "Kommentarer"},
    "service_words": {"followers": "följare", "subscribers": "prenumeranter", "likes": "likes",
                      "views": "visningar", "comments": "kommentarer"},

    # Page chrome
    "home": "Hem",
    "crumbs_label": "Brödsmulor",
    "eyebrow": "{platform} · {service_name}",
    "eyebrow_hub": "Tillväxt på {platform}",
    "cta": "Börja med {pick_name}",
    "cta_more": "Se alla paket",
    "trust": ["Riktiga människor, aldrig bottar", "Vi ber aldrig om ditt lösenord", "Månadsvis, säg upp när du vill"],
    "product_name": "Tillväxtpaket för {platform}",
    "sticky_cta": "Kom igång",

    # Packages
    "packages_title": "Välj ditt paket",
    "packages_lead": "Tre månadspaket. Nya {audience}, likes, visningar och kommentarer kommer tillsammans, från samma riktiga människor.",
    "packages_note": "Typiska intervall per månad, inget fast antal: var och en av dina nya {audience} är en riktig människa som har valt att {follow}, så varje månad blir lite olika.",

    # What's included: the page's own service comes first, then the rest in this order.
    "included_title": "Det här ingår",
    "included_lead": "Varje paket ger hela bilden, från samma riktiga människor.",
    "included_items": {
        "audience": ("Nya {audience}", "Riktiga människor som har hittat din {profile} och valt att {follow}. Oftast {starter_audience} i månaden med {starter_name}."),
        "likes": ("Likes från samma människor", "Oftast {starter_likes} i månaden med {starter_name}, på de {content} de gillar."),
        "comments": ("Kommentarer med egna ord", "Oftast {starter_comments} i månaden med {starter_name}. Skrivna av människor, aldrig efter manus."),
        "views": ("Visningar som följer med", "Samma människor tittar på dina {content} på eget initiativ. Vi räknar inte visningar i förväg: varje visning är en människa."),
        "days": ("Utspritt över 30 dagar", "Lite varje dag, från platsen du väljer. Aldrig allt på en gång."),
        "dashboard": ("Din översikt", "Det vi har mätt, dag för dag: besök från din kampanj och de nya {audience} de har gett."),
    },

    # How it works: the subscription, step by step
    "steps_title": "Så fungerar det",
    "steps_lead": "En månadsprenumeration: du väljer paketet, vi kör kampanjen, riktiga människor bestämmer.",
    "steps": [
        ("Välj ett paket", "{starter_name}, {rising_name} eller {pro_name}, debiteras månadsvis. Säg upp när du vill från ditt konto."),
        ("Vi startar din kampanj", "Ge oss ditt {handle} på {platform} och berätta var din publik ska komma ifrån. Vi ber aldrig om ditt lösenord."),
        ("Riktiga människor hittar din {profile}", "Varje dag visas din {profile} för riktiga människor. De som gillar det de ser väljer själva att {follow}, gilla och kommentera."),
        ("Din översikt visar vad vi har mätt", "Besök från din kampanj och de nya {audience} de har gett, dag för dag. Uppmätta siffror, aldrig gissningar."),
    ],

    # Real people vs bots / instant
    "compare_title": "Riktiga människor, inte bottar",
    "compare_lead": "Direkt betyder bottar: ingen riktig människa väljer att {follow} sekunder efter en betalning.",
    "compare_cols": ("Vad som skiljer", "Direkttjänster och bottar", "Growsterr"),
    "compare": [
        ("Vilka de är", "Bottar och falska profiler", "Riktiga människor som valt att {follow}"),
        ("Takt", "Tusentals på några minuter", "Lite varje dag, hela månaden"),
        ("Likes och kommentarer", "Säljs separat, från fler bottar", "Från samma människor, i ditt paket"),
        ("Din räckvidd", "Sjunker i tysthet: en publik som aldrig engagerar sig säger till {platform} att dina {content} inte är värda att visa", "Växer med människor som tittar, gillar och kommer tillbaka"),
        ("Ditt lösenord", "Efterfrågas ofta", "Aldrig"),
        ("Vad du ser", "En siffra som kan försvinna vid nästa rensning", "En översikt över det vi har mätt"),
    ],

    # Quantity pages: how a monthly package gets you to the goal
    "quantity_title": "Så når du {quantity} {service}",
    "quantity_lead": "Vi säljer inget fast paket med {quantity}. Riktiga människor bestämmer själva, så ett månadspaket tar dig dit i naturlig takt.",
    "pace_title": "Typisk takt med {pick_name}",
    "pace_month": "Månad {n}",
    "pace_goal": "Mål: {quantity}",
    "pace_note": "Typiska intervall utifrån vad riktiga människor gör, aldrig ett löfte. Vissa månader ger mer, andra mindre.",
    "by_plan_title": "Tid till {quantity}, per paket",
    "a_month": "{range} i månaden",
    "when_first": "oftast inom första månaden",
    "when_about": "oftast cirka {n} månader",
    "when_range": "oftast {low}–{high} månader",
    "views_pace": "Visningar kommer från samma riktiga människor som hittar din {profile}, så vi räknar dem inte i förväg. {pick_name} är paketet som passar det här målet bäst.",

    # FAQ, related pages, closing
    "faq_title": "Frågor och svar",
    "related_title": "Utforska vidare",
    "related": {
        "platform": "Mer om {platform}",
        "platforms": "På andra plattformar",
        "quantities": "Andra mål",
        "modifiers": "Andra sätt att växa",
        "articles": "Läs vidare",
        "hubs": "Väx med riktiga människor på",
    },
    # The tools a page can carry ("tool"): they run in the browser, nothing is sent.
    "tools": {
        "calculate": "Räkna ut",
        "followers": "Följare",
        "avg_likes": "Genomsnittliga likes per inlägg",
        "avg_comments": "Genomsnittliga kommentarer per inlägg",
        "engagement_title": "Din engagemangsgrad",
        "engagement_lead": "Hur många av dina följare reagerar på ett vanligt inlägg? Fyll i siffrorna från dina senaste inlägg.",
        "engagement_result": "Din engagemangsgrad är {rate} %.",
        "engagement_note": "Graden stiger när de som följer dig faktiskt bryr sig om dina inlägg. Följare som aldrig reagerar sänker den, hur många de än är.",
        "growth_title": "Hur lång tid till ditt mål?",
        "growth_lead": "Fyll i var du är och var du vill vara. Vi räknar utifrån varje pakets typiska intervall per månad.",
        "current": "Följare i dag",
        "goal": "Ditt mål",
        "when_first": "oftast inom första månaden",
        "when_range": "oftast {low}–{high} månader",
        "when_about": "cirka {n} månader",
        "reached": "Du är redan där.",
        "growth_note": "Typiska intervall, inget löfte: riktiga människor bestämmer själva om de vill följa.",
    },
    # Eyebrow above the headline of pages outside the platform x service grid (by "kind").
    "article_eyebrows": {
        "guide": "Guide",
        "alternative": "Jämförelse",
        "payment": "Betalning",
        "agency": "Tillväxtbyrå",
        "tool": "Verktyg",
        "intent": "Rakt svar",
    },
    "cta_title": "Redo att växa på {platform}?",
    "cta_text": "Välj ett paket så startar vi din kampanj. Riktiga människor bestämmer resten, och din översikt visar vad vi har mätt.",

    # Platform hubs
    "services_title": "Det här får vi att växa på {platform}",
    "services_lead": "Ett paket ger allt detta, från samma riktiga människor.",
    "teasers": {
        "audience": "Riktiga människor som hittar din {profile} och väljer att {follow}.",
        "likes": "Likes från människor som gillar dina {content}.",
        "views": "Visningar från människor som väljer att titta, aldrig från skript.",
        "comments": "Kommentarer skrivna av riktiga människor, med egna ord.",
    },
    "explore": "Utforska",
    "in_package": "Ingår i varje paket",
    "goals_title": "Fler sätt att växa på {platform}",
    "other_hubs_title": "Vi hjälper dig också att växa på",
}
