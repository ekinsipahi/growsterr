"""Dutch YouTube pages: the hub and subscribers. Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "youtube",
        "label": "YouTube",
        "title": "YouTube-groeipakketten voor creators | Growsterr",
        "description": "Laat uw YouTube-kanaal groeien met echte mensen: maandpakketten brengen abonnees, likes en reacties van echte kijkers. Vanaf {from_price} per maand.",
        "h1": ("Laat uw YouTube-kanaal groeien ", "met echte kijkers."),
        "intro": "Maandelijkse groeipakketten voor creators. Echte mensen ontdekken uw kanaal, bekijken uw video's en abonneren zich als ze leuk vinden wat ze zien. Uw dashboard laat dag voor dag zien wat we hebben gemeten.",
        "hero": {"image": "youtube-hub", "alt": "Een YouTube-kanaal krijgt abonnees, likes en reacties van echte kijkers"},
        "sections": [
            {
                "h2": "Abonnees die kijken, daar gaat het om",
                "p": [
                    "YouTube raadt video's aan die mensen bekijken, liken en waar ze naar terugkeren. Een abonnee die nooit kijkt, is erger dan geen abonnee: hij verlaagt het deel van uw publiek dat betrokken is.",
                    "Elke abonnee die wij brengen, is een mens die uw kanaal vond en ervoor koos zich te abonneren. Likes, views en reacties komen van dezelfde mensen, in uw pakket.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Kijkers bekijken de YouTubevideo van een creator en schrijven reacties"},
            },
            {
                "h2": "Voor kanalen die met zorg publiceren",
                "p": [
                    "Tutorials, vlogs, muziek of gaming: als u regelmatig publiceert, geven echte kijkers elke nieuwe video een betere start. Begin met {starter_name} en stap over wanneer uw kanaal klaar is voor meer.",
                ],
                "ul": [
                    "U vertelt ons uit welke stad, regio of welk land uw publiek moet komen.",
                    "Abonnees, likes en reacties komen samen, van dezelfde mensen.",
                    "Uw kanaal blijft van u: we vragen nooit om uw wachtwoord.",
                ],
                "image": {"image": "youtube-channel", "alt": "Een creator monteert een YouTubevideo in een thuisstudio"},
            },
        ],
        "faqs": [
            ("Zijn de abonnees echte mensen?", "Ja. Elke abonnee is een echt mens die uw kanaal vond en ervoor koos zich te abonneren. Geen bots, geen nepaccounts, niets direct."),
            ("Hoeveel abonnees brengt een pakket?", "Doorgaans {starter_audience} nieuwe abonnees per maand met {starter_name}, {rising_audience} met {rising_name} en {pro_audience} met {pro_name}. Typische bereiken, geen vast aantal."),
            ("Hebt u mijn Google- of YouTube-wachtwoord nodig?", "Nooit. We hebben alleen uw kanaalhandle nodig, en uw kanaal moet openbaar zijn."),
            ("Kan ik views of likes los kopen?", "Nee. Views, likes en reacties zitten in elk pakket, van dezelfde echte mensen die zich abonneren."),
            ("Kan ik altijd opzeggen?", "Ja. Pakketten worden maandelijks verlengd en u kunt opzeggen vanuit uw account. De maand die u hebt betaald, loopt door tot het einde."),
        ],
    },
    {
        "service": "subscribers",
        "slug": "youtube/abonnees",
        "label": "YouTube-abonnees",
        "title": "Echte YouTube-abonnees die kijken | Growsterr",
        "description": "YouTube-abonnees die echte mensen zijn: kijkers die uw kanaal vonden en zich bewust abonneerden, met likes en reacties. Vanaf {from_price} per maand.",
        "h1": ("YouTube-abonnees ", "die echt kijken."),
        "intro": "Echte mensen ontdekken uw kanaal, bekijken uw video's en abonneren zich als ze leuk vinden wat ze zien. Doorgaans {starter_audience} nieuwe abonnees per maand met {starter_name}, met likes en reacties van dezelfde kijkers.",
        "hero": {"image": "youtube-subscribers", "alt": "Een YouTube-kanaalpagina met nieuwe abonnees van echte kijkers"},
        "sections": [
            {
                "h2": "Een abonnee hoort een kijker te zijn",
                "p": [
                    "Op YouTube heeft een abonnee alleen zin als hij kijkt. Echte abonnees zien uw volgende upload, bekijken hem, liken hem en reageren soms, en daar kijkt YouTube naar wanneer het beslist wat het aanraadt.",
                    "Botabonnees kijken nooit. Ze laten een kanaal groter lijken terwijl de video's minder mensen bereiken.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Echte kijkers abonneren zich op een YouTube-kanaal na het bekijken van een video"},
            },
            {
                "h2": "Hoe een maand eruitziet",
                "ul": [
                    "De eerste dagen: uw campagne start en de eerste kijkers komen binnen.",
                    "Elke week: nieuwe abonnees, likes en reacties, elke dag een paar.",
                    "Aan het eind van de maand: doorgaans {pick_audience} nieuwe abonnees met {pick_name}.",
                ],
            },
            {
                "h2": "Waar uw kijkers vandaan komen",
                "p": [
                    "Vertel ons uit welke stad, regio of welk land uw publiek moet komen. We tonen uw kanaal eerst aan echte mensen daar; waar het best passende publiek in de buurt groter is, kunnen er meer vandaan komen.",
                ],
            },
        ],
        "faqs": [
            ("Hoe snel komen de abonnees?", "Elke dag een beetje, verspreid over de hele maand. Nooit alles tegelijk: echte mensen abonneren zich in hun eigen tempo."),
            ("Gaan ze mijn video's bekijken?", "Het zijn echte mensen die zich abonneerden nadat ze uw kanaal zagen. Wat ze daarna bekijken, bepalen ze zelf, zoals elk publiek, en juist daarom telt het."),
            ("Krijg ik ook likes en reacties?", "Ja, van dezelfde kijkers: doorgaans {pick_likes} likes en {pick_comments} reacties per maand met {pick_name}."),
            ("Hebt u mijn wachtwoord nodig?", "Nooit. We hebben alleen uw kanaalhandle nodig, en uw kanaal moet openbaar zijn."),
        ],
    },
]
