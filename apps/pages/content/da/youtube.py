"""Danish YouTube pages: the hub and subscribers (mirrors en/youtube.py)."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "youtube",
        "label": "YouTube",
        "title": "YouTube-vækstpakker til skabere | Growsterr",
        "description": "Voks på YouTube med rigtige mennesker: månedlige pakker giver abonnenter, likes og kommentarer fra seere, der valgte at abonnere. Fra {from_price} om måneden.",
        "h1": ("Få din YouTube-kanal til at vokse ", "med rigtige seere."),
        "intro": "Månedlige vækstpakker til skabere. Rigtige mennesker finder din kanal, ser dine videoer og abonnerer, når de kan lide det, de ser. Dit dashboard viser, hvad vi har målt, dag for dag.",
        "hero": {"image": "youtube-hub", "alt": "En YouTube-kanal, der får abonnenter, likes og kommentarer fra rigtige seere"},
        "sections": [
            {
                "h2": "Det er abonnenterne, der ser med, der tæller",
                "p": [
                    "YouTube anbefaler videoer, som folk ser, liker og vender tilbage til. En abonnent, der aldrig ser med, er værre end ingen: vedkommende sænker andelen af dit publikum, der engagerer sig.",
                    "Hver abonnent, vi bringer, er et menneske, der har fundet din kanal og valgt at abonnere. Likes, visninger og kommentarer kommer fra de samme mennesker, med i din pakke.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Seere, der ser en skabers YouTube-video og skriver kommentarer"},
            },
            {
                "h2": "Til kanaler, der udgiver med omhu",
                "p": [
                    "Tutorials, vlogs, musik eller gaming: hvis du udgiver regelmæssigt, giver rigtige seere hver ny video en bedre start. Start med {starter_name}, og gå et trin op, når din kanal er klar til mere.",
                ],
                "ul": [
                    "Du fortæller, hvilken by, region eller hvilket land dit publikum skal komme fra.",
                    "Abonnenter, likes og kommentarer kommer sammen, fra de samme mennesker.",
                    "Din kanal forbliver din: vi beder aldrig om din adgangskode.",
                ],
                "image": {"image": "youtube-channel", "alt": "En skaber, der redigerer en YouTube-video i et hjemmestudie"},
            },
        ],
        "faqs": [
            ("Er abonnenterne rigtige mennesker?", "Ja. Hver abonnent er et rigtigt menneske, der har fundet din kanal og valgt at abonnere. Ingen bots, ingen falske konti, intet øjeblikkeligt."),
            ("Hvor mange abonnenter giver en pakke?", "Typisk {starter_audience} nye abonnenter om måneden med {starter_name}, {rising_audience} med {rising_name} og {pro_audience} med {pro_name}. Typiske intervaller, ikke et fast antal."),
            ("Skal I bruge min Google- eller YouTube-adgangskode?", "Aldrig. Vi skal kun bruge dit kanalhandle (@handle), og din kanal skal være offentlig."),
            ("Kan jeg købe visninger eller likes for sig?", "Nej. Visninger, likes og kommentarer følger med i hver pakke, fra de samme rigtige mennesker, der abonnerer."),
            ("Kan jeg opsige når som helst?", "Ja. Pakkerne fornyes hver måned, og du kan opsige dem fra din konto. Den måned, du har betalt for, kører til ende."),
        ],
    },
    {
        "service": "subscribers",
        "slug": "youtube/abonnenter",
        "label": "YouTube-abonnenter",
        "title": "Ægte YouTube-abonnenter, der ser med | Growsterr",
        "description": "YouTube-abonnenter, der er rigtige mennesker: seere, der fandt din kanal og valgte at abonnere, med likes og kommentarer. Fra {from_price} om måneden.",
        "h1": ("YouTube-abonnenter, ", "der rent faktisk ser med."),
        "intro": "Rigtige mennesker finder din kanal, ser dine videoer og abonnerer, når de kan lide det, de ser. Typisk {starter_audience} nye abonnenter om måneden med {starter_name}, med likes og kommentarer fra de samme seere.",
        "hero": {"image": "youtube-subscribers", "alt": "En YouTube-kanalside med nye abonnenter fra rigtige seere"},
        "sections": [
            {
                "h2": "En abonnent bør være en seer",
                "p": [
                    "På YouTube er en abonnent kun nyttig, hvis vedkommende ser med. Ægte abonnenter opdager din næste upload, ser den, liker den og kommenterer nogle gange, og det er det, YouTube ser på, når den afgør, hvad der skal anbefales.",
                    "Bot-abonnenter ser aldrig med. De får en kanal til at se større ud, mens dens videoer når færre mennesker.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Rigtige seere, der abonnerer på en YouTube-kanal efter at have set en video"},
            },
            {
                "h2": "Sådan ser en måned ud",
                "ul": [
                    "De første dage: kampagnen starter, og de første seere kommer.",
                    "Hver uge: nye abonnenter, likes og kommentarer, et par stykker hver dag.",
                    "Ved månedens slutning: typisk {pick_audience} nye abonnenter med {pick_name}.",
                ],
            },
            {
                "h2": "Hvor dine seere kommer fra",
                "p": [
                    "Fortæl os, hvilken by, region eller hvilket land dit publikum skal komme fra. Vi viser din kanal for rigtige mennesker der først; hvor det bedst matchende publikum er større, kan flere komme fra områderne i nærheden.",
                ],
            },
        ],
        "faqs": [
            ("Hvor hurtigt kommer abonnenterne?", "Lidt hver dag, hen over hele måneden. Aldrig det hele på én gang: rigtige mennesker abonnerer i deres eget tempo."),
            ("Vil de se mine videoer?", "Det er rigtige mennesker, der valgte at abonnere efter at have set din kanal. Hvad de ser bagefter, er op til dem, som med ethvert publikum, og det er netop derfor, det tæller."),
            ("Får jeg også likes og kommentarer?", "Ja, fra de samme seere: typisk {pick_likes} likes og {pick_comments} kommentarer om måneden med {pick_name}."),
            ("Skal I bruge min adgangskode?", "Aldrig. Vi skal kun bruge dit kanalhandle, og din kanal skal være offentlig."),
        ],
    },
]
