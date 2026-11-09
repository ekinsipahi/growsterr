"""Norwegian (Bokmål) TikTok pages: the hub and likes (mirrors en/tiktok.py)."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "tiktok",
        "label": "TikTok",
        "title": "TikTok-vekstpakker for innholdsskapere | Growsterr",
        "description": "Voks på TikTok med ekte mennesker: månedlige pakker gir nye følgere, likes og kommentarer fra folk som selv valgte å følge. Fra {from_price} i måneden.",
        "h1": ("Få TikTok-kontoen din til å vokse ", "med ekte mennesker."),
        "intro": "Månedlige vekstpakker for innholdsskapere og influencere. Ekte mennesker finner profilen din, ser videoene dine og følger deg når de liker det de ser. Dashbordet viser hva vi har målt, dag for dag.",
        "hero": {"image": "tiktok-hub", "alt": "Profilen til en TikTok-skaper der nye følgere og likes kommer inn"},
        "sections": [
            {
                "h2": "På TikTok er oppmerksomhet alt",
                "p": [
                    "TikTok viser en video til flere når de første seerne ser den, liker, kommenterer og følger. Tall uten mennesker bak flytter ingenting av dette.",
                    "Pakkene våre bringer ekte mennesker til profilen din hver dag. De ser, de bestemmer seg, og de som liker videoene dine, følger og liker. Det er den typen oppmerksomhet som hjelper en video å spre seg.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Ekte seere som ser TikTok-videoene til en skaper"},
            },
            {
                "h2": "For innholdsskapere som har noe på hjertet",
                "p": [
                    "Humor, matlaging, mote eller tutorials: hvis du publiserer jevnlig, gir ekte seere hver nye video en bedre start. Start med {starter_name}, og gå opp et trinn når du er klar.",
                ],
                "ul": [
                    "Du forteller hvilken by, region eller hvilket land publikummet ditt skal komme fra.",
                    "Følgere, likes og kommentarer kommer sammen, fra de samme menneskene.",
                    "Kontoen din forblir din: vi ber aldri om passordet ditt.",
                ],
                "image": {"image": "tiktok-creator", "alt": "En innholdsskaper som filmer en TikTok-video med mobilen på et stativ"},
            },
        ],
        "faqs": [
            ("Er følgerne ekte mennesker?", "Ja. Hver følger er et ekte menneske som har sett profilen din og valgt å følge deg. Vi bruker aldri bots, falske kontoer eller umiddelbar levering."),
            ("Hvor mange følgere gir en pakke?", "Vanligvis {starter_audience} nye følgere i måneden med {starter_name}, {rising_audience} med {rising_name} og {pro_audience} med {pro_name}. Typiske intervaller, ikke et fast antall: ekte mennesker bestemmer selv."),
            ("Trenger dere TikTok-passordet mitt?", "Aldri. Vi trenger bare brukernavnet ditt. Hold kontoen offentlig, så de som finner den, kan følge deg."),
            ("Kan jeg kjøpe visninger eller likes alene?", "Nei. Visninger, likes og kommentarer følger med i hver pakke, fra de samme ekte menneskene som følger deg."),
            ("Kan jeg si opp når jeg vil?", "Ja. Pakkene fornyes hver måned, og du kan si dem opp fra kontoen din. Måneden du har betalt for, løper ut."),
        ],
    },
    {
        "service": "likes",
        "slug": "tiktok/likes",
        "label": "TikTok-likes",
        "title": "TikTok-likes fra ekte mennesker, i hver pakke",
        "description": "TikTok-likes fra ekte mennesker som ser videoene dine, aldri bots. Likes følger med i hver månedlige pakke, sammen med følgere og kommentarer. Fra {from_price}/mnd.",
        "h1": ("TikTok-likes fra ekte mennesker. ", "I hver pakke."),
        "intro": "Vi selger ikke likes alene. Hver pakke gir ekte mennesker som finner profilen din, ser videoene dine og liker det de setter pris på: vanligvis {starter_likes} likes i måneden med {starter_name}.",
        "hero": {"image": "tiktok-likes", "alt": "Likes fra ekte seere som stiger fra en TikTok-video"},
        "sections": [
            {
                "h2": "En like teller bare med et menneske bak",
                "p": [
                    "TikTok følger med på hva som skjer rundt en like: så seeren videre, fulgte personen, kom den tilbake? Likes fra bots svarer nei på alt, så de legger til et tall og tar bort rekkevidde.",
                    "Likes fra ekte mennesker kommer med resten: seertid, nye følgere og kommentarer. Det er signalet som hjelper en video å spre seg.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Seere som ser en TikTok-video til slutten og liker den"},
            },
            {
                "h2": "Så mange likes gir hver pakke",
                "ul": [
                    "{starter_name} ({starter_price} i måneden): vanligvis {starter_likes} likes.",
                    "{rising_name} ({rising_price} i måneden): vanligvis {rising_likes} likes, på videoene du velger.",
                    "{pro_name} ({pro_price} i måneden): vanligvis {pro_likes} likes, med prioritert plassering.",
                ],
            },
            {
                "h2": "Derfor selger vi ikke likes alene",
                "p": [
                    "Likes som kommer uten visninger, følgere eller kommentarer, ser ut akkurat som det de er. I en pakke kommer hver like fra noen som har sett videoen, så tallene dine beveger seg sammen, slik ekte vekst gjør.",
                ],
            },
        ],
        "faqs": [
            ("Kan jeg få TikTok-likes uten en pakke?", "Nei. Likes, visninger og kommentarer kommer bare i de månedlige pakkene våre, fra de samme ekte menneskene. Det er det som holder dem naturlige."),
            ("Hvilke videoer får likes?", "Ekte mennesker liker det de setter pris på, som regel de nyeste videoene dine. Med {rising_name} og {pro_name} kan du velge hvilke videoer som får oppmerksomheten."),
            ("Hvor raskt kommer likene?", "Litt hver dag, gjennom måneden. Aldri umiddelbart: en like som kommer umiddelbart, er en bot."),
            ("Trenger dere TikTok-passordet mitt?", "Aldri. Vi trenger bare brukernavnet ditt, og kontoen må være offentlig."),
        ],
    },
]
