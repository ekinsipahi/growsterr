"""Swedish Instagram pages: the hub, followers, and the 1,000-followers goal (mirrors en/instagram.py)."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "instagram",
        "label": "Instagram",
        "title": "Instagram-tillväxtpaket för kreatörer | Growsterr",
        "description": "Väx på Instagram med riktiga människor: månadspaket ger nya följare, likes och kommentarer från människor som själva valt att följa. Från {from_price} i månaden.",
        "h1": ("Få ditt Instagram att växa ", "med riktiga människor."),
        "intro": "Tillväxtpaket per månad för kreatörer och influencers. Vi visar din profil för riktiga människor, och de som gillar det de ser följer, gillar och kommenterar. Din översikt visar vad vi har mätt, dag för dag.",
        "hero": {"image": "instagram-hub", "alt": "En Instagramkreatörs profil där nya följare, likes och kommentarer kommer in"},
        "sections": [
            {
                "h2": "Tillväxt som ser förtjänad ut",
                "p": [
                    "Instagram belönar konton som människor faktiskt engagerar sig i. Bottar gör tvärtom: de sitter i ditt följarantal, gillar aldrig, tittar aldrig och lär algoritmen att dina inlägg inte är värda att visa.",
                    "Vi arbetar åt andra hållet. Din profil visas för riktiga människor varje dag, och varje följning är ett val som någon har gjort. Därför kommer likes, visningar och kommentarer tillsammans med dina följare, inte som ett separat köp.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Riktiga människor som upptäcker en kreatörs Instagraminlägg och lämnar kommentarer"},
            },
            {
                "h2": "För kreatörer som publicerar med en tanke",
                "p": [
                    "Personligt varumärke, nischsida eller litet företag: paketen växer med dig. Börja med {starter_name} och gå upp ett steg när ditt innehåll är redo för mer.",
                ],
                "ul": [
                    "Reels, karuseller och bildinlägg gynnas allihop.",
                    "Du berättar vilken stad, region eller vilket land din publik ska komma ifrån.",
                    "Ditt konto förblir ditt: vi ber aldrig om ditt lösenord.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "En kreatör som planerar Instagraminnehåll vid ett skrivbord"},
            },
        ],
        "faqs": [
            ("Är följarna riktiga människor?", "Ja. Varje följare är en riktig människa som har sett din profil och valt att följa dig. Vi använder aldrig bottar, falska profiler eller direktleverans."),
            ("Hur många följare ger ett paket?", "Oftast {starter_audience} nya följare i månaden med {starter_name}, {rising_audience} med {rising_name} och {pro_audience} med {pro_name}. Det är typiska intervall, inget fast antal: riktiga människor bestämmer själva."),
            ("Behöver ni mitt Instagramlösenord?", "Aldrig. Vi behöver bara ditt användarnamn. Håll kontot offentligt så att de som hittar det kan följa dig."),
            ("Kan jag köpa likes eller kommentarer separat?", "Nej. Likes, visningar och kommentarer ingår i varje paket, från samma riktiga människor som följer dig. Det är det som håller dina siffror naturliga."),
            ("Kan jag säga upp när jag vill?", "Ja. Paketen förnyas varje månad och du kan säga upp dem från ditt konto. Månaden du har betalat för löper till sitt slut."),
        ],
    },
    {
        "service": "followers",
        "slug": "instagram/foljare",
        "label": "Instagramföljare",
        "title": "Äkta Instagramföljare, varje månad | Growsterr",
        "description": "Instagramföljare som är riktiga människor och själva valt att följa dig, med likes och kommentarer från samma människor. Månadspaket från {from_price}.",
        "h1": ("Instagramföljare ", "som själva valt att följa dig."),
        "intro": "Riktiga människor hittar din profil varje dag, och de som gillar det de ser följer dig. Oftast {starter_audience} nya följare i månaden med {starter_name}, med likes och kommentarer från samma människor.",
        "hero": {"image": "instagram-followers", "alt": "En Instagramprofil som får nya följare från riktiga människor"},
        "sections": [
            {
                "h2": "Därför är äkta följare värda mer",
                "p": [
                    "En följare räknas bara om det finns en människa bakom. Äkta följare ser ditt nästa inlägg, gillar det, kommenterar och delar det, och det är just det engagemanget Instagram tittar på när den avgör vilka fler som ska få se ditt innehåll.",
                    "Bottar kan inget av det. De höjer en siffra i några dagar, försvinner vid nästa rensning, och de som blir kvar drar i tysthet ner din räckvidd.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Riktiga människor som gillar och kommenterar en kreatörs Instagraminlägg"},
            },
            {
                "h2": "Var dina nya följare kommer ifrån",
                "p": [
                    "Berätta vilken stad, region eller vilket land din publik ska komma ifrån. Vi visar din profil för riktiga människor där först; där den bäst matchande publiken är större kan fler komma från närliggande områden.",
                ],
            },
            {
                "h2": "Så ser en månad ut",
                "ul": [
                    "De första dagarna: kampanjen startar och de första besöken kommer.",
                    "Varje vecka: nya följare, likes och kommentarer, några varje dag.",
                    "I slutet av månaden: oftast {pick_audience} nya följare med {pick_name}.",
                ],
            },
        ],
        "faqs": [
            ("Hur snabbt kommer följarna?", "Lite varje dag, under hela månaden. Aldrig allt på en gång: riktiga människor följer i sin egen takt, och allt som kommer direkt är bottar."),
            ("Kommer mina nya följare att sluta följa?", "Några kan göra det, precis som i all riktig publik. Men äkta följare stannar betydligt oftare än bottar, som försvinner i vågor."),
            ("Får jag likes och kommentarer också?", "Ja, från samma människor: oftast {pick_likes} likes och {pick_comments} kommentarer i månaden med {pick_name}."),
            ("Är det säkert för mitt konto?", "Vi ber aldrig om ditt lösenord och loggar aldrig in på ditt konto. Människor hittar din profil och bestämmer själva, precis som alla andra följare hittar dig."),
            ("Kan jag välja var mina följare kommer ifrån?", "Ja. Ange stad, region eller land när du beställer. Vi siktar dit först; om en nära matchande publik är större i närheten kan en del av dina följare komma därifrån."),
        ],
    },
    {
        "service": "followers",
        "quantity": 1000,
        "slug": "instagram/foljare/1000",
        "label": "{quantity} Instagramföljare",
        "title": "{quantity} Instagramföljare från riktiga människor | Growsterr",
        "description": "Nå {quantity} Instagramföljare med riktiga människor, inte bottar. {pick_name} ger oftast {pick_audience} i månaden, med likes och kommentarer också.",
        "h1": ("{quantity} Instagramföljare, ", "var och en en riktig människa."),
        "intro": "Vi säljer inget paket med {quantity} bottar. Vi får ditt konto att växa med riktiga människor: {pick_name} ger oftast {pick_audience} nya följare i månaden, så {quantity} är oftast inom räckhåll redan första månaden.",
        "hero": {"image": "instagram-followers-1000", "alt": "En stigande kurva av nya Instagramföljare som når en första milstolpe"},
        "sections": [
            {
                "h2": "Varför inte {quantity} följare på en timme?",
                "p": [
                    "För att ingen riktig människa följer ett konto sekunder efter en betalning. Tjänster som levererar {quantity} följare på en timme levererar bottar: de gillar inte, kommenterar inte och försvinner i vågor.",
                    "De som blir kvar gör ännu mer skada. Varje följare som aldrig engagerar sig sänker andelen av din publik som gör det, och dina inlägg når i tysthet färre människor.",
                ],
            },
            {
                "h2": "Dina första tusen, på rätt sätt",
                "p": [
                    "De första tusen äkta följarna ändrar hur nya besökare ser dig. Det är människor som kan titta på dina Reels, gilla dina inlägg och komma tillbaka, och det är precis det som hjälper nästa tusen att hitta dig.",
                ],
                "ul": [
                    "Riktiga människor som valt att följa, från platsen du väljer.",
                    "Likes och kommentarer från samma människor, i paketet.",
                    "En översikt som visar vad vi har mätt, dag för dag.",
                ],
            },
        ],
        "faqs": [
            ("Hur lång tid tar {quantity} äkta följare?", "I typisk takt ger {pick_name} {pick_audience} nya följare i månaden, så {quantity} är oftast inom räckhåll första månaden. Riktiga människor följer i sin egen takt, så varje månad blir lite olika."),
            ("Är det ett engångspaket med {quantity}?", "Nej. Vi säljer tillväxt som månadspaket. {pick_name} kostar {pick_price} i månaden, och du kan säga upp när du vill från ditt konto."),
            ("Får jag likes och kommentarer med dem?", "Ja, från samma riktiga människor: oftast {pick_likes} likes och {pick_comments} kommentarer i månaden med {pick_name}."),
            ("Vad händer efter {quantity}?", "Ditt paket fortsätter tills du säger upp det, så tillväxten fortsätter månad efter månad. När ditt innehåll är redo för mer kan du gå upp ett paket."),
        ],
    },
]
