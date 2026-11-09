"""Swedish YouTube pages: the hub and subscribers (mirrors en/youtube.py)."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "youtube",
        "label": "YouTube",
        "title": "YouTube-tillväxtpaket för kreatörer | Growsterr",
        "description": "Väx på YouTube med riktiga människor: månadspaket ger prenumeranter, likes och kommentarer från tittare som valt att prenumerera. Från {from_price} i månaden.",
        "h1": ("Få din YouTube-kanal att växa ", "med riktiga tittare."),
        "intro": "Tillväxtpaket per månad för kreatörer. Riktiga människor hittar din kanal, tittar på dina videor och prenumererar när de gillar det de ser. Din översikt visar vad vi har mätt, dag för dag.",
        "hero": {"image": "youtube-hub", "alt": "En YouTube-kanal som får prenumeranter, likes och kommentarer från riktiga tittare"},
        "sections": [
            {
                "h2": "Det är prenumeranterna som tittar som räknas",
                "p": [
                    "YouTube rekommenderar videor som människor tittar på, gillar och kommer tillbaka till. En prenumerant som aldrig tittar är sämre än ingen alls: den sänker andelen av din publik som engagerar sig.",
                    "Varje prenumerant vi ger dig är en människa som har hittat din kanal och valt att prenumerera. Likes, visningar och kommentarer kommer från samma människor, i ditt paket.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Tittare som ser en kreatörs YouTube-video och skriver kommentarer"},
            },
            {
                "h2": "För kanaler som publicerar med omsorg",
                "p": [
                    "Tutorials, vloggar, musik eller gaming: om du publicerar regelbundet ger riktiga tittare varje ny video en bättre start. Börja med {starter_name} och gå upp ett steg när din kanal är redo för mer.",
                ],
                "ul": [
                    "Du berättar vilken stad, region eller vilket land din publik ska komma ifrån.",
                    "Prenumeranter, likes och kommentarer kommer tillsammans, från samma människor.",
                    "Din kanal förblir din: vi ber aldrig om ditt lösenord.",
                ],
                "image": {"image": "youtube-channel", "alt": "En kreatör som redigerar en YouTube-video i en hemmastudio"},
            },
        ],
        "faqs": [
            ("Är prenumeranterna riktiga människor?", "Ja. Varje prenumerant är en riktig människa som har hittat din kanal och valt att prenumerera. Inga bottar, inga falska konton, inget direkt."),
            ("Hur många prenumeranter ger ett paket?", "Oftast {starter_audience} nya prenumeranter i månaden med {starter_name}, {rising_audience} med {rising_name} och {pro_audience} med {pro_name}. Typiska intervall, inget fast antal."),
            ("Behöver ni mitt Google- eller YouTube-lösenord?", "Aldrig. Vi behöver bara ditt kanalhandtag (@handle), och kanalen ska vara offentlig."),
            ("Kan jag köpa visningar eller likes separat?", "Nej. Visningar, likes och kommentarer ingår i varje paket, från samma riktiga människor som prenumererar."),
            ("Kan jag säga upp när jag vill?", "Ja. Paketen förnyas varje månad och du kan säga upp dem från ditt konto. Månaden du har betalat för löper till sitt slut."),
        ],
    },
    {
        "service": "subscribers",
        "slug": "youtube/prenumeranter",
        "label": "YouTube-prenumeranter",
        "title": "Äkta YouTube-prenumeranter som tittar | Growsterr",
        "description": "YouTube-prenumeranter som är riktiga människor: tittare som hittat din kanal och valt att prenumerera, med likes och kommentarer. Från {from_price} i månaden.",
        "h1": ("YouTube-prenumeranter ", "som faktiskt tittar."),
        "intro": "Riktiga människor hittar din kanal, tittar på dina videor och prenumererar när de gillar det de ser. Oftast {starter_audience} nya prenumeranter i månaden med {starter_name}, med likes och kommentarer från samma tittare.",
        "hero": {"image": "youtube-subscribers", "alt": "En YouTube-kanalsida med nya prenumeranter från riktiga tittare"},
        "sections": [
            {
                "h2": "En prenumerant ska vara en tittare",
                "p": [
                    "På YouTube är en prenumerant bara till nytta om den tittar. Äkta prenumeranter ser din nästa uppladdning, tittar på den, gillar den och kommenterar ibland, och det är det YouTube utgår från när den avgör vad som ska rekommenderas.",
                    "Bottprenumeranter tittar aldrig. De får en kanal att se större ut medan dess videor når färre människor.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Riktiga tittare som prenumererar på en YouTube-kanal efter att ha sett en video"},
            },
            {
                "h2": "Så ser en månad ut",
                "ul": [
                    "De första dagarna: kampanjen startar och de första tittarna kommer.",
                    "Varje vecka: nya prenumeranter, likes och kommentarer, några varje dag.",
                    "I slutet av månaden: oftast {pick_audience} nya prenumeranter med {pick_name}.",
                ],
            },
            {
                "h2": "Var dina tittare kommer ifrån",
                "p": [
                    "Berätta vilken stad, region eller vilket land din publik ska komma ifrån. Vi visar din kanal för riktiga människor där först; där den bäst matchande publiken är större kan fler komma från närliggande områden.",
                ],
            },
        ],
        "faqs": [
            ("Hur snabbt kommer prenumeranterna?", "Lite varje dag, under hela månaden. Aldrig allt på en gång: riktiga människor prenumererar i sin egen takt."),
            ("Kommer de att titta på mina videor?", "De är riktiga människor som valt att prenumerera efter att ha sett din kanal. Vad de tittar på sedan är upp till dem, som för all publik, och det är precis därför det räknas."),
            ("Får jag likes och kommentarer också?", "Ja, från samma tittare: oftast {pick_likes} likes och {pick_comments} kommentarer i månaden med {pick_name}."),
            ("Behöver ni mitt lösenord?", "Aldrig. Vi behöver bara ditt kanalhandtag, och kanalen ska vara offentlig."),
        ],
    },
]
