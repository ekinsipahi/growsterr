"""Maltese YouTube pages: the hub and subscribers (abbonati). Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "youtube",
        "label": "YouTube",
        "title": "Pakketti ta' tkabbir fuq YouTube għall-kreaturi | Growsterr",
        "description": "Ikber fuq YouTube ma' nies veri: pakketti ta' kull xahar iġibu abbonati, likes u kummenti minn spettaturi li għażlu li jabbonaw. Minn {from_price} fix-xahar.",
        "h1": ("Kabbar il-kanal tiegħek fuq YouTube ", "ma' spettaturi veri."),
        "intro": "Qed taħseb biex tixtri abbonati jew veduti fuq YouTube? Hawn il-verżjoni onesta: pakketti ta' tkabbir ta' kull xahar għall-kreaturi. Nies veri jiskopru l-kanal tiegħek, jaraw il-vidjows tiegħek u jabbonaw meta jogħġobhom dak li jaraw. Il-pannell tiegħek juri dak li kejjilna, jum b'jum.",
        "hero": {"image": "youtube-hub", "alt": "Kanal fuq YouTube jikseb abbonati, likes u kummenti minn spettaturi veri"},
        "sections": [
            {
                "h2": "L-abbonati li jaraw huma dawk li jgħoddu",
                "p": [
                    "YouTube jirrakkomanda vidjows li n-nies jaraw, jagħtuhom like u jerġgħu lura għalihom. Abbonat li qatt ma jara huwa agħar milli xejn: ibaxxi s-sehem tal-udjenza tiegħek li tinteraġixxi.",
                    "Kull abbonat li nġibulek huwa persuna li sabet il-kanal tiegħek u għażlet li tabbona fih. Il-likes, il-veduti u l-kummenti jiġu mill-istess nies, ġewwa l-pakkett tiegħek.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Spettaturi jaraw vidjo ta' kreatur fuq YouTube u jiktbu kummenti"},
            },
            {
                "h2": "Għall-kanali li jippubblikaw bil-għaqal",
                "p": [
                    "Tutorials, vlogs, mużika jew gaming: jekk tippubblika regolarment, spettaturi veri jagħtu bidu aħjar lil kull vidjo ġdid. Ibda b'{starter_name} u itla' pakkett meta l-kanal tiegħek ikun lest għal aktar.",
                ],
                "ul": [
                    "Int tgħidilna l-belt, ir-reġjun jew il-pajjiż minn fejn għandha tiġi l-udjenza tiegħek.",
                    "L-abbonati, il-likes u l-kummenti jiġu flimkien, mill-istess nies.",
                    "Il-kanal jibqa' tiegħek: qatt ma nitolbuk il-password.",
                ],
                "image": {"image": "youtube-channel", "alt": "Kreatur jeditja vidjo għal YouTube fi studio fid-dar"},
            },
        ],
        "faqs": [
            ("L-abbonati huma nies veri?", "Iva. Kull abbonat huwa persuna vera li sabet il-kanal tiegħek u għażlet li tabbona fih. L-ebda bot, l-ebda kont falz, xejn istantanju."),
            ("Kemm-il abbonat iġib pakkett?", "Normalment {starter_audience} abbonat ġdid fix-xahar b'{starter_name}, {rising_audience} b'{rising_name} u {pro_audience} b'{pro_name}. Firxiet tipiċi, mhux għadd fiss."),
            ("Għandkom bżonn il-password tiegħi ta' Google jew YouTube?", "Qatt. Għandna bżonn biss il-handle tal-kanal tiegħek, u l-kanal għandu jkun pubbliku."),
            ("Nista' nixtri veduti jew likes weħidhom?", "Le. Il-veduti, il-likes u l-kummenti jiġu ġewwa kull pakkett, mill-istess nies veri li jabbonaw fil-kanal tiegħek."),
            ("Nista' nikkanċella meta rrid?", "Iva. Il-pakketti jiġġeddu kull xahar u tista' tikkanċella mill-kont tiegħek. Ix-xahar li ħallast għalih jibqa' sejjer sal-aħħar."),
        ],
    },
    {
        "service": "subscribers",
        "slug": "youtube/abbonati",
        "label": "Abbonati fuq YouTube",
        "title": "Ixtri abbonati veri fuq YouTube li jaraw | Growsterr",
        "description": "Ixtri abbonati fuq YouTube li huma nies veri: spettaturi li sabu l-kanal tiegħek u għażlu li jabbonaw, b'likes u kummenti. Minn {from_price} fix-xahar.",
        "h1": ("Abbonati fuq YouTube ", "li verament jaraw."),
        "intro": "Ixtri abbonati fuq YouTube bil-mod onest: nies veri jiskopru l-kanal tiegħek, jaraw il-vidjows tiegħek u jabbonaw meta jogħġobhom dak li jaraw. Normalment {starter_audience} abbonat ġdid fix-xahar b'{starter_name}, b'likes u kummenti mill-istess spettaturi.",
        "hero": {"image": "youtube-subscribers", "alt": "Paġna ta' kanal fuq YouTube b'abbonati ġodda minn spettaturi veri"},
        "sections": [
            {
                "h2": "Abbonat għandu jkun spettatur",
                "p": [
                    "Fuq YouTube, abbonat huwa utli biss jekk jara. L-abbonati veri jaraw il-vidjo li jmiss tiegħek, jagħtuh like u xi drabi jikkummentaw, u dak hu li YouTube iħares lejh meta jiddeċiedi x'jirrakkomanda.",
                    "L-abbonati li huma bots qatt ma jaraw. Jagħmlu kanal jidher akbar, filwaqt li l-vidjows tiegħu jaslu għand inqas nies.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Spettaturi veri jabbonaw f'kanal fuq YouTube wara li raw vidjo"},
            },
            {
                "h2": "Kif jidher xahar",
                "ul": [
                    "L-ewwel jiem: il-kampanja tiegħek tibda u jaslu l-ewwel spettaturi.",
                    "Kull ġimgħa: abbonati ġodda, likes u kummenti, ftit kuljum.",
                    "Sa tmiem ix-xahar: normalment {pick_audience} abbonat ġdid b'{pick_name}.",
                ],
            },
            {
                "h2": "Minn fejn jiġu l-ispettaturi tiegħek",
                "p": [
                    "Għidilna l-belt, ir-reġjun jew il-pajjiż minn fejn għandha tiġi l-udjenza tiegħek. L-ewwel nuru l-kanal tiegħek lil nies veri hemmhekk; fejn l-udjenza li l-aktar taqbel tkun akbar fil-qrib, jistgħu jiġu aktar minn hemm.",
                ],
            },
        ],
        "faqs": [
            ("Kemm jaslu malajr l-abbonati?", "Ftit kuljum, matul ix-xahar kollu. Qatt kollha f'daqqa: in-nies veri jabbonaw bir-ritmu tagħhom."),
            ("Se jaraw il-vidjows tiegħi?", "Huma nies veri li għażlu li jabbonaw wara li raw il-kanal tiegħek. X'jaraw wara jiddeċiduh huma, bħal kull udjenza, u eżattament għalhekk jgħodd."),
            ("Nieħu wkoll likes u kummenti?", "Iva, mill-istess spettaturi: normalment {pick_likes} like u {pick_comments} kumment fix-xahar b'{pick_name}."),
            ("Għandkom bżonn il-password tiegħi?", "Qatt. Għandna bżonn biss il-handle tal-kanal tiegħek, u l-kanal għandu jkun pubbliku."),
        ],
    },
]
