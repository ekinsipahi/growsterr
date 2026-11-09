"""Slovenian YouTube pages: the hub and subscribers. Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "youtube",
        "label": "YouTube",
        "title": "Paketi za rast na YouTubu za ustvarjalce | Growsterr",
        "description": "Rastite na YouTubu z resničnimi ljudmi: mesečni paketi prinesejo naročnike, všečke in komentarje gledalcev, ki so se odločili za naročnino. Od {from_price}/mesec.",
        "h1": ("Rastite na YouTubu ", "z resničnimi gledalci."),
        "intro": "Mesečni paketi za rast za ustvarjalce. Resnični ljudje odkrijejo vaš kanal, si ogledajo vaše videe in se naročijo, ko jim je všeč, kar vidijo. Nadzorna plošča dan za dnem pokaže, kaj smo izmerili.",
        "hero": {"image": "youtube-hub", "alt": "Kanal na YouTubu, ki pridobiva naročnike, všečke in komentarje od resničnih gledalcev"},
        "sections": [
            {
                "h2": "Štejejo naročniki, ki gledajo",
                "p": [
                    "YouTube priporoča videe, ki jih ljudje gledajo, všečkajo in se k njim vračajo. Naročnik, ki nikoli ne gleda, je slabši od nobenega: zniža delež vašega občinstva, ki se odziva.",
                    "Vsak naročnik, ki ga pripeljemo, je oseba, ki je našla vaš kanal in se odločila za naročnino. Všečki, ogledi in komentarji prihajajo od istih ljudi, v vašem paketu.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Gledalci gledajo video ustvarjalca na YouTubu in pišejo komentarje"},
            },
            {
                "h2": "Za kanale, ki objavljajo skrbno",
                "p": [
                    "Vodiči, vlogi, glasba ali igre: če redno objavljate, resnični gledalci vsakemu novemu videu dajo boljši začetek. Začnite s paketom {starter_name} in preidite višje, ko je vaš kanal pripravljen na več.",
                ],
                "ul": [
                    "Poveste nam mesto, regijo ali državo, iz katere naj prihaja vaše občinstvo.",
                    "Naročniki, všečki in komentarji pridejo skupaj, od istih ljudi.",
                    "Vaš kanal ostane vaš: nikoli ne zahtevamo vašega gesla.",
                ],
                "image": {"image": "youtube-channel", "alt": "Ustvarjalec v domačem studiu ureja video za YouTube"},
            },
        ],
        "faqs": [
            ("So naročniki resnični ljudje?", "Da. Vsak naročnik je resnična oseba, ki je našla vaš kanal in se odločila za naročnino. Brez botov, brez lažnih računov, nič takojšnjega."),
            ("Koliko naročnikov prinese paket?", "Običajno {starter_audience} novih naročnikov na mesec s paketom {starter_name}, {rising_audience} s paketom {rising_name} in {pro_audience} s paketom {pro_name}. Tipični razponi, ne fiksno število."),
            ("Potrebujete moje geslo za Google ali YouTube?", "Nikoli. Potrebujemo le identifikator vašega kanala, kanal pa naj bo javen."),
            ("Lahko kupim samo oglede ali všečke?", "Ne. Ogledi, všečki in komentarji so vključeni v vsak paket, od istih resničnih ljudi, ki se naročijo."),
            ("Lahko kadar koli prekličem?", "Da. Paketi se podaljšujejo mesečno, prekličete pa jih lahko v svojem računu. Plačani mesec teče do konca."),
        ],
    },
    {
        "service": "subscribers",
        "slug": "youtube/narocniki",
        "label": "Naročniki na YouTubu",
        "title": "Resnični naročniki na YouTubu, ki gledajo | Growsterr",
        "description": "Naročniki na YouTubu, ki so resnični ljudje: gledalci, ki so našli vaš kanal in se odločili za naročnino, z všečki in komentarji. Od {from_price} na mesec.",
        "h1": ("Naročniki na YouTubu, ", "ki res gledajo."),
        "intro": "Resnični ljudje odkrijejo vaš kanal, si ogledajo vaše videe in se naročijo, ko jim je všeč, kar vidijo. Običajno {starter_audience} novih naročnikov na mesec s paketom {starter_name}, z všečki in komentarji istih gledalcev.",
        "hero": {"image": "youtube-subscribers", "alt": "Stran kanala na YouTubu z novimi naročniki od resničnih gledalcev"},
        "sections": [
            {
                "h2": "Naročnik naj bo gledalec",
                "p": [
                    "Na YouTubu je naročnik koristen le, če gleda. Resnični naročniki vidijo vaš naslednji video, si ga ogledajo, ga všečkajo in včasih komentirajo, prav to pa YouTube upošteva, ko se odloča, kaj bo priporočil.",
                    "Botovski naročniki nikoli ne gledajo. Kanal je zaradi njih videti večji, njegovi videi pa dosežejo manj ljudi.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Resnični gledalci se po ogledu videa naročijo na kanal na YouTubu"},
            },
            {
                "h2": "Kako je videti en mesec",
                "ul": [
                    "Prvi dnevi: kampanja se začne in pridejo prvi gledalci.",
                    "Vsak teden: novi naročniki, všečki in komentarji, vsak dan nekaj.",
                    "Do konca meseca: običajno {pick_audience} novih naročnikov s paketom {pick_name}.",
                ],
            },
            {
                "h2": "Od kod pridejo vaši gledalci",
                "p": [
                    "Povejte nam mesto, regijo ali državo, iz katere naj prihaja vaše občinstvo. Vaš kanal najprej pokažemo resničnim ljudem tam; kjer je najbolj ujemajoče se občinstvo večje, jih lahko več pride iz bližine.",
                ],
            },
        ],
        "faqs": [
            ("Kako hitro pridejo naročniki?", "Vsak dan malo, skozi ves mesec. Nikoli vse naenkrat: resnični ljudje se naročajo v svojem tempu."),
            ("Ali bodo gledali moje videe?", "So resnični ljudje, ki so se naročili, potem ko so videli vaš kanal. Kaj bodo gledali naprej, je odvisno od njih, kot pri vsakem občinstvu, in prav zato šteje."),
            ("Dobim tudi všečke in komentarje?", "Da, od istih gledalcev: običajno {pick_likes} všečkov in {pick_comments} komentarjev na mesec s paketom {pick_name}."),
            ("Potrebujete moje geslo?", "Nikoli. Potrebujemo le identifikator vašega kanala, kanal pa naj bo javen."),
        ],
    },
]
