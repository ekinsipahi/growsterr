"""Albanian TikTok pages: the hub and likes. Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "tiktok",
        "label": "TikTok",
        "title": "Paketa rritjeje në TikTok për krijues | Growsterr",
        "description": "Rrituni në TikTok me njerëz të vërtetë: paketa mujore me ndjekës të rinj, pëlqime dhe komente nga njerëz që zgjodhën t'ju ndjekin. Nga {from_price} në muaj.",
        "h1": ("Rritni TikTok-un tuaj ", "me njerëz të vërtetë."),
        "intro": "Paketa mujore rritjeje për krijues dhe influencerë. Njerëz të vërtetë zbulojnë profilin tuaj, shikojnë videot tuaja dhe ju ndjekin kur u pëlqen ajo që shohin. Paneli juaj tregon çfarë matëm, ditë pas dite.",
        "hero": {"image": "tiktok-hub", "alt": "Profili i një krijuesi në TikTok, ku vijnë ndjekës dhe pëlqime të reja"},
        "sections": [
            {
                "h2": "Në TikTok, vëmendja është gjithçka",
                "p": [
                    "TikTok-u ia shfaq një video më shumë njerëzve kur shikuesit e parë e shohin, e pëlqejnë, e komentojnë dhe ndjekin krijuesin. Numrat pa njerëz pas tyre nuk lëvizin asgjë nga këto.",
                    "Paketat tona sjellin çdo ditë njerëz të vërtetë në profilin tuaj. Ata shikojnë, vendosin, dhe ata që i shijojnë videot tuaja ju ndjekin dhe i pëlqejnë. Ky është lloji i vëmendjes që e ndihmon një video të shkojë larg.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Shikues të vërtetë që shohin videot e një krijuesi në TikTok"},
            },
            {
                "h2": "Për krijues që kanë diçka për të thënë",
                "p": [
                    "Humor, gatim, modë apo tutoriale: nëse postoni rregullisht, shikuesit e vërtetë i japin çdo videoje të re një nisje më të mirë. Nisni me {starter_name} dhe kaloni më lart kur të jeni gati.",
                ],
                "ul": [
                    "Ju na tregoni qytetin, rajonin ose shtetin nga duhet të vijë publiku juaj.",
                    "Ndjekësit, pëlqimet dhe komentet vijnë bashkë, nga të njëjtët njerëz.",
                    "Llogaria mbetet e juaja: nuk ju kërkojmë kurrë fjalëkalimin.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Një krijues që xhiron një video për TikTok me telefon mbi trekëmbësh"},
            },
        ],
        "faqs": [
            ("A janë ndjekësit njerëz të vërtetë?", "Po. Çdo ndjekës është një njeri i vërtetë që pa profilin tuaj dhe zgjodhi t'ju ndjekë. Nuk përdorim kurrë robotë, llogari të rreme apo dërgim «në çast»."),
            ("Sa ndjekës sjell një paketë?", "Zakonisht {starter_audience} ndjekës të rinj në muaj me {starter_name}, {rising_audience} me {rising_name} dhe {pro_audience} me {pro_name}. Intervale tipike, jo një numër i caktuar: njerëzit e vërtetë vendosin vetë."),
            ("A ju duhet fjalëkalimi im i TikTok-ut?", "Kurrë. Na duhet vetëm emri i përdoruesit. Mbajeni llogarinë publike, që njerëzit që e zbulojnë të mund t'ju ndjekin."),
            ("A mund të blej shikime ose pëlqime më vete?", "Jo. Shikimet, pëlqimet dhe komentet vijnë brenda çdo pakete, nga të njëjtët njerëz të vërtetë që ju ndjekin."),
            ("A mund të anuloj kur të dua?", "Po. Paketat rinovohen çdo muaj dhe mund t'i anuloni nga llogaria juaj. Muaji i paguar vazhdon deri në fund."),
        ],
    },
    {
        "service": "likes",
        "slug": "tiktok/pelqime",
        "label": "Pëlqime në TikTok",
        "title": "Pëlqime në TikTok nga njerëz të vërtetë, në çdo paketë",
        "description": "Pëlqime në TikTok nga njerëz të vërtetë që shikojnë videot tuaja, kurrë nga robotë. Vijnë brenda çdo pakete mujore, me ndjekës dhe komente. Nga {from_price} në muaj.",
        "h1": ("Pëlqime në TikTok nga njerëz të vërtetë. ", "Brenda çdo pakete."),
        "intro": "Nuk shesim pëlqime më vete. Çdo paketë sjell njerëz të vërtetë që zbulojnë profilin tuaj, shikojnë videot tuaja dhe pëlqejnë ato që shijojnë: zakonisht {starter_likes} pëlqime në muaj me {starter_name}.",
        "hero": {"image": "tiktok-likes", "alt": "Pëlqime nga shikues të vërtetë që ngrihen mbi një video në TikTok"},
        "sections": [
            {
                "h2": "Pse një pëlqim vlen vetëm kur pas tij ka një njeri",
                "p": [
                    "TikTok-u shikon çfarë ndodh rreth një pëlqimi: a vazhdoi shikuesi të shikonte, a ndoqi krijuesin, a u rikthye? Pëlqimet nga robotët i përgjigjen «jo» të gjithave, ndaj shtojnë një numër dhe ju heqin shtrirje.",
                    "Pëlqimet nga njerëz të vërtetë vijnë me pjesën tjetër: kohë shikimi, ndjekje dhe komente. Ky është sinjali që e ndihmon një video të shkojë larg.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Shikues që e shohin një video në TikTok deri në fund dhe e pëlqejnë"},
            },
            {
                "h2": "Sa pëlqime sjell secila paketë",
                "ul": [
                    "{starter_name} ({starter_price} në muaj): zakonisht {starter_likes} pëlqime.",
                    "{rising_name} ({rising_price} në muaj): zakonisht {rising_likes} pëlqime, te videot që zgjidhni.",
                    "{pro_name} ({pro_price} në muaj): zakonisht {pro_likes} pëlqime, me përparësi në radhë.",
                ],
            },
            {
                "h2": "Pse nuk shesim pëlqime më vete",
                "p": [
                    "Pëlqimet që vijnë pa shikime, ndjekje apo komente duken pikërisht ashtu siç janë. Brenda një pakete, çdo pëlqim vjen nga dikush që e shikoi videon, ndaj shifrat tuaja lëvizin bashkë, ashtu si në një rritje të vërtetë.",
                ],
            },
        ],
        "faqs": [
            ("A mund të marr pëlqime në TikTok pa paketë?", "Jo. Pëlqimet, shikimet dhe komentet vijnë vetëm brenda paketave tona mujore, nga të njëjtët njerëz të vërtetë. Kjo i mban natyrale."),
            ("Cilat video marrin pëlqimet?", "Njerëzit e vërtetë pëlqejnë atë që shijojnë, zakonisht videot tuaja më të reja. Me {rising_name} dhe {pro_name} mund të zgjidhni vetë cilat video marrin vëmendjen."),
            ("Sa shpejt vijnë pëlqimet?", "Pak çdo ditë, gjatë gjithë muajit. Kurrë «në çast»: një pëlqim që vjen në çast është nga një robot."),
            ("A ju duhet fjalëkalimi im i TikTok-ut?", "Kurrë. Na duhet vetëm emri i përdoruesit, dhe llogaria juaj duhet të jetë publike."),
        ],
    },
]
