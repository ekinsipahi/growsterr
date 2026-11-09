"""Norwegian (Bokmål) YouTube pages: the hub and subscribers (mirrors en/youtube.py)."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "youtube",
        "label": "YouTube",
        "title": "YouTube-vekstpakker for innholdsskapere | Growsterr",
        "description": "Voks på YouTube med ekte mennesker: månedlige pakker gir abonnenter, likes og kommentarer fra seere som valgte å abonnere. Fra {from_price} i måneden.",
        "h1": ("Få YouTube-kanalen din til å vokse ", "med ekte seere."),
        "intro": "Månedlige vekstpakker for innholdsskapere. Ekte mennesker finner kanalen din, ser videoene dine og abonnerer når de liker det de ser. Dashbordet viser hva vi har målt, dag for dag.",
        "hero": {"image": "youtube-hub", "alt": "En YouTube-kanal som får abonnenter, likes og kommentarer fra ekte seere"},
        "sections": [
            {
                "h2": "Det er abonnentene som ser på, som teller",
                "p": [
                    "YouTube anbefaler videoer som folk ser, liker og kommer tilbake til. En abonnent som aldri ser på, er verre enn ingen: den senker andelen av publikummet ditt som engasjerer seg.",
                    "Hver abonnent vi gir deg, er et menneske som har funnet kanalen din og valgt å abonnere. Likes, visninger og kommentarer kommer fra de samme menneskene, med i pakken din.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Seere som ser YouTube-videoen til en skaper og skriver kommentarer"},
            },
            {
                "h2": "For kanaler som publiserer med omhu",
                "p": [
                    "Tutorials, vlogger, musikk eller gaming: hvis du publiserer jevnlig, gir ekte seere hver nye video en bedre start. Start med {starter_name}, og gå opp et trinn når kanalen din er klar for mer.",
                ],
                "ul": [
                    "Du forteller hvilken by, region eller hvilket land publikummet ditt skal komme fra.",
                    "Abonnenter, likes og kommentarer kommer sammen, fra de samme menneskene.",
                    "Kanalen din forblir din: vi ber aldri om passordet ditt.",
                ],
                "image": {"image": "youtube-channel", "alt": "En innholdsskaper som redigerer en YouTube-video i et hjemmestudio"},
            },
        ],
        "faqs": [
            ("Er abonnentene ekte mennesker?", "Ja. Hver abonnent er et ekte menneske som har funnet kanalen din og valgt å abonnere. Ingen bots, ingen falske kontoer, ingenting umiddelbart."),
            ("Hvor mange abonnenter gir en pakke?", "Vanligvis {starter_audience} nye abonnenter i måneden med {starter_name}, {rising_audience} med {rising_name} og {pro_audience} med {pro_name}. Typiske intervaller, ikke et fast antall."),
            ("Trenger dere Google- eller YouTube-passordet mitt?", "Aldri. Vi trenger bare kanalens @-navn (@handle), og kanalen må være offentlig."),
            ("Kan jeg kjøpe visninger eller likes alene?", "Nei. Visninger, likes og kommentarer følger med i hver pakke, fra de samme ekte menneskene som abonnerer."),
            ("Kan jeg si opp når jeg vil?", "Ja. Pakkene fornyes hver måned, og du kan si dem opp fra kontoen din. Måneden du har betalt for, løper ut."),
        ],
    },
    {
        "service": "subscribers",
        "slug": "youtube/abonnenter",
        "label": "YouTube-abonnenter",
        "title": "Ekte YouTube-abonnenter som ser på | Growsterr",
        "description": "YouTube-abonnenter som er ekte mennesker: seere som fant kanalen din og valgte å abonnere, med likes og kommentarer. Fra {from_price} i måneden.",
        "h1": ("YouTube-abonnenter ", "som faktisk ser på."),
        "intro": "Ekte mennesker finner kanalen din, ser videoene dine og abonnerer når de liker det de ser. Vanligvis {starter_audience} nye abonnenter i måneden med {starter_name}, med likes og kommentarer fra de samme seerne.",
        "hero": {"image": "youtube-subscribers", "alt": "En YouTube-kanalside med nye abonnenter fra ekte seere"},
        "sections": [
            {
                "h2": "En abonnent bør være en seer",
                "p": [
                    "På YouTube er en abonnent bare nyttig hvis den ser på. Ekte abonnenter oppdager den neste opplastingen din, ser den, liker den og kommenterer av og til, og det er dette YouTube ser på når den avgjør hva som skal anbefales.",
                    "Bot-abonnenter ser aldri på. De får en kanal til å se større ut mens videoene når færre mennesker.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Ekte seere som abonnerer på en YouTube-kanal etter å ha sett en video"},
            },
            {
                "h2": "Slik ser en måned ut",
                "ul": [
                    "De første dagene: kampanjen starter, og de første seerne kommer.",
                    "Hver uke: nye abonnenter, likes og kommentarer, noen hver dag.",
                    "Ved slutten av måneden: vanligvis {pick_audience} nye abonnenter med {pick_name}.",
                ],
            },
            {
                "h2": "Hvor seerne dine kommer fra",
                "p": [
                    "Fortell oss hvilken by, region eller hvilket land publikummet ditt skal komme fra. Vi viser kanalen din for ekte mennesker der først; der det best matchende publikummet er større, kan flere komme fra områdene rundt.",
                ],
            },
        ],
        "faqs": [
            ("Hvor raskt kommer abonnentene?", "Litt hver dag, gjennom hele måneden. Aldri alt på én gang: ekte mennesker abonnerer i sitt eget tempo."),
            ("Kommer de til å se videoene mine?", "De er ekte mennesker som valgte å abonnere etter å ha sett kanalen din. Hva de ser etterpå, er opp til dem, som med ethvert publikum, og det er nettopp derfor det teller."),
            ("Får jeg likes og kommentarer også?", "Ja, fra de samme seerne: vanligvis {pick_likes} likes og {pick_comments} kommentarer i måneden med {pick_name}."),
            ("Trenger dere passordet mitt?", "Aldri. Vi trenger bare kanalens @-navn, og kanalen må være offentlig."),
        ],
    },
]
