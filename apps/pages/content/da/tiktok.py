"""Danish TikTok pages: the hub and likes (mirrors en/tiktok.py)."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "tiktok",
        "label": "TikTok",
        "title": "TikTok-vækstpakker til skabere | Growsterr",
        "description": "Voks på TikTok med rigtige mennesker: månedlige pakker giver nye følgere, likes og kommentarer fra folk, der selv valgte at følge. Fra {from_price} om måneden.",
        "h1": ("Få din TikTok til at vokse ", "med rigtige mennesker."),
        "intro": "Månedlige vækstpakker til skabere og influencere. Rigtige mennesker finder din profil, ser dine videoer og følger dig, når de kan lide det, de ser. Dit dashboard viser, hvad vi har målt, dag for dag.",
        "hero": {"image": "tiktok-hub", "alt": "En TikTok-skabers profil, hvor nye følgere og likes kommer ind"},
        "sections": [
            {
                "h2": "På TikTok er opmærksomhed alt",
                "p": [
                    "TikTok viser en video til flere, når de første seere ser den, liker, kommenterer og følger. Tal uden mennesker bag flytter intet af det.",
                    "Vores pakker bringer rigtige mennesker til din profil hver dag. De ser, de beslutter, og de, der kan lide dine videoer, følger og liker. Det er den slags opmærksomhed, der hjælper en video med at sprede sig.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Rigtige seere, der ser en skabers TikTok-videoer"},
            },
            {
                "h2": "Til skabere, der har noget på hjerte",
                "p": [
                    "Comedy, madlavning, mode eller tutorials: hvis du poster regelmæssigt, giver rigtige seere hver ny video en bedre start. Start med {starter_name}, og gå et trin op, når du er klar.",
                ],
                "ul": [
                    "Du fortæller, hvilken by, region eller hvilket land dit publikum skal komme fra.",
                    "Følgere, likes og kommentarer kommer sammen, fra de samme mennesker.",
                    "Din konto forbliver din: vi beder aldrig om din adgangskode.",
                ],
                "image": {"image": "tiktok-creator", "alt": "En skaber, der filmer en TikTok-video med telefonen på et stativ"},
            },
        ],
        "faqs": [
            ("Er følgerne rigtige mennesker?", "Ja. Hver følger er et rigtigt menneske, der har set din profil og valgt at følge dig. Vi bruger aldrig bots, falske konti eller øjeblikkelig levering."),
            ("Hvor mange følgere giver en pakke?", "Typisk {starter_audience} nye følgere om måneden med {starter_name}, {rising_audience} med {rising_name} og {pro_audience} med {pro_name}. Typiske intervaller, ikke et fast antal: rigtige mennesker bestemmer selv."),
            ("Skal I bruge min TikTok-adgangskode?", "Aldrig. Vi skal kun bruge dit brugernavn. Hold din konto offentlig, så de, der finder den, kan følge dig."),
            ("Kan jeg købe visninger eller likes for sig?", "Nej. Visninger, likes og kommentarer følger med i hver pakke, fra de samme rigtige mennesker, der følger dig."),
            ("Kan jeg opsige når som helst?", "Ja. Pakkerne fornyes hver måned, og du kan opsige dem fra din konto. Den måned, du har betalt for, kører til ende."),
        ],
    },
    {
        "service": "likes",
        "slug": "tiktok/likes",
        "label": "TikTok-likes",
        "title": "TikTok-likes fra rigtige mennesker, i hver pakke",
        "description": "TikTok-likes fra rigtige mennesker, der ser dine videoer, aldrig bots. Likes følger med i hver månedlig pakke med følgere og kommentarer. Fra {from_price}/md.",
        "h1": ("TikTok-likes fra rigtige mennesker. ", "I hver pakke."),
        "intro": "Vi sælger ikke likes for sig. Hver pakke giver rigtige mennesker, der finder din profil, ser dine videoer og liker det, de kan lide: typisk {starter_likes} likes om måneden med {starter_name}.",
        "hero": {"image": "tiktok-likes", "alt": "Likes fra rigtige seere, der stiger op fra en TikTok-video"},
        "sections": [
            {
                "h2": "Et like tæller kun med et menneske bag",
                "p": [
                    "TikTok holder øje med, hvad der sker omkring et like: blev seeren ved med at se, fulgte vedkommende, kom vedkommende igen? Likes fra bots svarer nej til det hele, så de lægger et tal til og trækker rækkevidde fra.",
                    "Likes fra rigtige mennesker kommer med resten: seertid, nye følgere og kommentarer. Det er det signal, der hjælper en video med at sprede sig.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Seere, der ser en TikTok-video til ende og liker den"},
            },
            {
                "h2": "Så mange likes giver hver pakke",
                "ul": [
                    "{starter_name} ({starter_price} om måneden): typisk {starter_likes} likes.",
                    "{rising_name} ({rising_price} om måneden): typisk {rising_likes} likes, på de videoer, du vælger.",
                    "{pro_name} ({pro_price} om måneden): typisk {pro_likes} likes, med prioriteret placering.",
                ],
            },
            {
                "h2": "Derfor sælger vi ikke likes for sig",
                "p": [
                    "Likes, der kommer uden visninger, følgere eller kommentarer, ser ud præcis som det, de er. I en pakke kommer hvert like fra en, der har set videoen, så dine tal bevæger sig sammen, sådan som ægte vækst gør.",
                ],
            },
        ],
        "faqs": [
            ("Kan jeg få TikTok-likes uden en pakke?", "Nej. Likes, visninger og kommentarer kommer kun i vores månedlige pakker, fra de samme rigtige mennesker. Det er det, der holder dem naturlige."),
            ("Hvilke videoer får likes?", "Rigtige mennesker liker det, de kan lide, som regel dine nyeste videoer. Med {rising_name} og {pro_name} kan du vælge, hvilke videoer der får opmærksomheden."),
            ("Hvor hurtigt kommer likes?", "Lidt hver dag, hen over måneden. Aldrig øjeblikkeligt: et øjeblikkeligt like er en bot."),
            ("Skal I bruge min TikTok-adgangskode?", "Aldrig. Vi skal kun bruge dit brugernavn, og din konto skal være offentlig."),
        ],
    },
]
