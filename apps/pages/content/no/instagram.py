"""Norwegian (Bokmål) Instagram pages: the hub, followers, and the 1,000-followers goal (mirrors en/instagram.py)."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "instagram",
        "label": "Instagram",
        "title": "Instagram-vekstpakker for innholdsskapere | Growsterr",
        "description": "Voks på Instagram med ekte mennesker: månedlige pakker gir nye følgere, likes og kommentarer fra folk som selv valgte å følge. Fra {from_price} i måneden.",
        "h1": ("Få Instagram-kontoen din til å vokse ", "med ekte mennesker."),
        "intro": "Månedlige vekstpakker for innholdsskapere og influencere. Vi viser profilen din til ekte mennesker, og de som liker det de ser, følger, liker og kommenterer. Dashbordet viser hva vi har målt, dag for dag.",
        "hero": {"image": "instagram-hub", "alt": "Profilen til en Instagram-skaper der nye følgere, likes og kommentarer kommer inn"},
        "sections": [
            {
                "h2": "Vekst som ser fortjent ut",
                "p": [
                    "Instagram belønner kontoer som folk faktisk engasjerer seg i. Bots gjør det motsatte: de sitter i følgertallet ditt, liker aldri, ser aldri og lærer algoritmen at innleggene dine ikke er verdt å vise.",
                    "Vi jobber andre veien. Profilen din vises for ekte mennesker hver dag, og hver nye følger er et valg noen har tatt. Derfor kommer likes, visninger og kommentarer sammen med følgerne dine, ikke som et eget kjøp.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Ekte mennesker som oppdager Instagram-innleggene til en skaper og legger igjen kommentarer"},
            },
            {
                "h2": "For innholdsskapere som publiserer med en hensikt",
                "p": [
                    "Personlig merkevare, nisjeside eller liten bedrift: pakkene vokser med deg. Start med {starter_name}, og gå opp et trinn når innholdet ditt er klart for mer.",
                ],
                "ul": [
                    "Reels, karuseller og bildeinnlegg har alle nytte av det.",
                    "Du forteller hvilken by, region eller hvilket land publikummet ditt skal komme fra.",
                    "Kontoen din forblir din: vi ber aldri om passordet ditt.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "En innholdsskaper som planlegger Instagram-innhold ved en pult"},
            },
        ],
        "faqs": [
            ("Er følgerne ekte mennesker?", "Ja. Hver følger er et ekte menneske som har sett profilen din og valgt å følge deg. Vi bruker aldri bots, falske profiler eller umiddelbar levering."),
            ("Hvor mange følgere gir en pakke?", "Vanligvis {starter_audience} nye følgere i måneden med {starter_name}, {rising_audience} med {rising_name} og {pro_audience} med {pro_name}. Dette er typiske intervaller, ikke et fast antall: ekte mennesker bestemmer selv."),
            ("Trenger dere Instagram-passordet mitt?", "Aldri. Vi trenger bare brukernavnet ditt. Hold kontoen offentlig, så de som finner den, kan følge deg."),
            ("Kan jeg kjøpe likes eller kommentarer alene?", "Nei. Likes, visninger og kommentarer følger med i hver pakke, fra de samme ekte menneskene som følger deg. Det er det som holder tallene dine naturlige."),
            ("Kan jeg si opp når jeg vil?", "Ja. Pakkene fornyes hver måned, og du kan si dem opp fra kontoen din. Måneden du har betalt for, løper ut."),
        ],
    },
    {
        "service": "followers",
        "slug": "instagram/folgere",
        "label": "Instagram-følgere",
        "title": "Ekte Instagram-følgere hver måned | Growsterr",
        "description": "Instagram-følgere som er ekte mennesker og selv valgte å følge deg, med likes og kommentarer fra de samme menneskene. Månedlige pakker fra {from_price}.",
        "h1": ("Instagram-følgere ", "som selv valgte å følge deg."),
        "intro": "Ekte mennesker finner profilen din hver dag, og de som liker det de ser, følger deg. Vanligvis {starter_audience} nye følgere i måneden med {starter_name}, med likes og kommentarer fra de samme menneskene.",
        "hero": {"image": "instagram-followers", "alt": "En Instagram-profil som får nye følgere fra ekte mennesker"},
        "sections": [
            {
                "h2": "Derfor er ekte følgere verdt mer",
                "p": [
                    "En følger teller bare hvis det står et menneske bak. Ekte følgere ser det neste innlegget ditt, liker det, kommenterer og deler det, og det er nettopp det engasjementet Instagram ser på når den avgjør hvem andre som skal se innholdet ditt.",
                    "Bots klarer ikke noe av dette. De løfter et tall i noen dager, forsvinner ved neste opprydding, og de som blir igjen, trekker rekkevidden din ned i det stille.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Ekte mennesker som liker og kommenterer et Instagram-innlegg fra en skaper"},
            },
            {
                "h2": "Hvor de nye følgerne dine kommer fra",
                "p": [
                    "Fortell oss hvilken by, region eller hvilket land publikummet ditt skal komme fra. Vi viser profilen din for ekte mennesker der først; der det best matchende publikummet er større, kan flere komme fra områdene rundt.",
                ],
            },
            {
                "h2": "Slik ser en måned ut",
                "ul": [
                    "De første dagene: kampanjen starter, og de første besøkene kommer.",
                    "Hver uke: nye følgere, likes og kommentarer, noen hver dag.",
                    "Ved slutten av måneden: vanligvis {pick_audience} nye følgere med {pick_name}.",
                ],
            },
        ],
        "faqs": [
            ("Hvor raskt kommer følgerne?", "Litt hver dag, gjennom hele måneden. Aldri alt på én gang: ekte mennesker følger i sitt eget tempo, og alt som kommer umiddelbart, er bots."),
            ("Kommer de nye følgerne mine til å slutte å følge?", "Noen kan gjøre det, slik ethvert ekte publikum endrer seg. Men ekte følgere blir mye oftere enn bots, som forsvinner i bølger."),
            ("Får jeg likes og kommentarer også?", "Ja, fra de samme menneskene: vanligvis {pick_likes} likes og {pick_comments} kommentarer i måneden med {pick_name}."),
            ("Er det trygt for kontoen min?", "Vi ber aldri om passordet ditt og logger aldri inn på kontoen din. Folk finner profilen din og bestemmer selv, slik enhver følger finner deg."),
            ("Kan jeg velge hvor følgerne mine kommer fra?", "Ja. Oppgi by, region eller land når du bestiller. Vi sikter dit først; hvis et publikum som passer nesten like godt, er større i nærheten, kan noen av følgerne dine komme derfra."),
        ],
    },
    {
        "service": "followers",
        "quantity": 1000,
        "slug": "instagram/folgere/1000",
        "label": "{quantity} Instagram-følgere",
        "title": "{quantity} Instagram-følgere fra ekte mennesker | Growsterr",
        "description": "Nå {quantity} Instagram-følgere med ekte mennesker, ikke bots. {pick_name} gir vanligvis {pick_audience} i måneden, med likes og kommentarer i tillegg.",
        "h1": ("{quantity} Instagram-følgere, ", "hver eneste en et ekte menneske."),
        "intro": "Vi selger ikke en pakke med {quantity} bots. Vi får kontoen din til å vokse med ekte mennesker: {pick_name} gir vanligvis {pick_audience} nye følgere i måneden, så {quantity} er som regel innen rekkevidde allerede den første måneden.",
        "hero": {"image": "instagram-followers-1000", "alt": "En stigende kurve av nye Instagram-følgere som når en første milepæl"},
        "sections": [
            {
                "h2": "Hvorfor ikke {quantity} følgere på en time?",
                "p": [
                    "Fordi ingen ekte mennesker følger en konto sekunder etter en betaling. Tjenester som leverer {quantity} følgere på en time, leverer bots: de liker ikke, kommenterer ikke og forsvinner i bølger.",
                    "De som blir igjen, gjør enda mer skade. Hver følger som aldri engasjerer seg, senker andelen av publikummet ditt som gjør det, og innleggene dine når færre mennesker i det stille.",
                ],
            },
            {
                "h2": "De første tusen, gjort skikkelig",
                "p": [
                    "De første tusen ekte følgerne endrer hvordan nye besøkende ser deg. Det er mennesker som kan se Reels-videoene dine, like innleggene dine og komme tilbake, og det er akkurat det som hjelper de neste tusen å finne deg.",
                ],
                "ul": [
                    "Ekte mennesker som valgte å følge, fra stedet du velger.",
                    "Likes og kommentarer fra de samme menneskene, med i pakken.",
                    "Et dashbord som viser hva vi har målt, dag for dag.",
                ],
            },
        ],
        "faqs": [
            ("Hvor lang tid tar {quantity} ekte følgere?", "I et typisk tempo gir {pick_name} {pick_audience} nye følgere i måneden, så {quantity} er som regel innen rekkevidde den første måneden. Ekte mennesker følger i sitt eget tempo, så hver måned blir litt forskjellig."),
            ("Er det en engangspakke med {quantity}?", "Nei. Vi selger vekst som månedlige pakker. {pick_name} koster {pick_price} i måneden, og du kan si opp når du vil fra kontoen din."),
            ("Får jeg likes og kommentarer med dem?", "Ja, fra de samme ekte menneskene: vanligvis {pick_likes} likes og {pick_comments} kommentarer i måneden med {pick_name}."),
            ("Hva skjer etter {quantity}?", "Pakken din fortsetter til du sier den opp, så veksten fortsetter måned etter måned. Når innholdet ditt er klart for mer, kan du gå opp en pakke."),
        ],
    },
]
