"""Serbian (Latin script) YouTube pages: the hub and subscribers. Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "youtube",
        "label": "YouTube",
        "title": "Paketi za rast YouTube kanala za kreatore | Growsterr",
        "description": "Razvijajte YouTube kanal uz prave ljude: mesečni paketi donose pretplatnike, lajkove i komentare od gledalaca koji su se sami pretplatili. Od {from_price} mesečno.",
        "h1": ("Razvijajte svoj YouTube kanal ", "uz prave gledaoce."),
        "intro": "Mesečni paketi za rast, namenjeni kreatorima. Pravi ljudi otkrivaju vaš kanal, gledaju vaše video snimke i pretplaćuju se kada im se dopadne ono što vide. Kontrolna tabla pokazuje šta smo izmerili, dan po dan.",
        "hero": {"image": "youtube-hub", "alt": "YouTube kanal koji dobija pretplatnike, lajkove i komentare od pravih gledalaca"},
        "sections": [
            {
                "h2": "Važni su pretplatnici koji gledaju",
                "p": [
                    "YouTube preporučuje video snimke koje ljudi gledaju, lajkuju i kojima se vraćaju. Pretplatnik koji nikada ne gleda gori je nego nijedan: smanjuje udeo vaše publike koja reaguje.",
                    "Svaki pretplatnik kog dovedemo je osoba koja je pronašla vaš kanal i odlučila da se pretplati. Lajkovi, pregledi i komentari stižu od istih ljudi, u okviru vašeg paketa.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Gledaoci gledaju YouTube video kreatora i pišu komentare"},
            },
            {
                "h2": "Za kanale koji objavljuju sa pažnjom",
                "p": [
                    "Tutorijali, vlogovi, muzika ili gejming: ako redovno objavljujete, pravi gledaoci daju svakom novom videu bolji početak. Počnite sa paketom {starter_name} i pređite na veći kada vaš kanal bude spreman za više.",
                ],
                "ul": [
                    "Vi nam kažete grad, region ili zemlju iz koje treba da dolazi vaša publika.",
                    "Pretplatnici, lajkovi i komentari stižu zajedno, od istih ljudi.",
                    "Kanal ostaje vaš: nikada ne tražimo vašu lozinku.",
                ],
                "image": {"image": "youtube-channel", "alt": "Kreator montira YouTube video u kućnom studiju"},
            },
        ],
        "faqs": [
            ("Da li su pretplatnici pravi ljudi?", "Da. Svaki pretplatnik je prava osoba koja je pronašla vaš kanal i odlučila da se pretplati. Bez botova, bez lažnih naloga, ništa „odmah”."),
            ("Koliko pretplatnika donosi jedan paket?", "Obično {starter_audience} novih pretplatnika mesečno uz {starter_name}, {rising_audience} uz {rising_name} i {pro_audience} uz {pro_name}. Tipični rasponi, a ne fiksan broj."),
            ("Da li vam treba moja lozinka za Google ili YouTube?", "Nikada. Potreban nam je samo identifikator vašeg kanala, a kanal treba da bude javan."),
            ("Mogu li da kupim samo preglede ili lajkove?", "Ne. Pregledi, lajkovi i komentari dolaze u okviru svakog paketa, od istih pravih ljudi koji se pretplate."),
            ("Mogu li da otkažem bilo kada?", "Da. Paketi se obnavljaju mesečno, a otkazati možete iz svog naloga. Plaćeni mesec traje do kraja."),
        ],
    },
    {
        "service": "subscribers",
        "slug": "youtube/pretplatnici",
        "label": "YouTube pretplatnici",
        "title": "Pravi YouTube pretplatnici koji gledaju | Growsterr",
        "description": "YouTube pretplatnici koji su pravi ljudi: gledaoci koji su pronašli vaš kanal i sami se pretplatili, uz lajkove i komentare. Od {from_price} mesečno.",
        "h1": ("YouTube pretplatnici ", "koji zaista gledaju."),
        "intro": "Pravi ljudi otkrivaju vaš kanal, gledaju vaše video snimke i pretplaćuju se kada im se dopadne ono što vide. Uz {starter_name} obično {starter_audience} novih pretplatnika mesečno, uz lajkove i komentare od istih gledalaca.",
        "hero": {"image": "youtube-subscribers", "alt": "Stranica YouTube kanala sa novim pretplatnicima, pravim gledaocima"},
        "sections": [
            {
                "h2": "Pretplatnik treba da bude gledalac",
                "p": [
                    "Na YouTube-u pretplatnik ima smisla samo ako gleda. Pravi pretplatnici vide vaš sledeći video, gledaju ga, lajkuju i ponekad komentarišu, a upravo na to YouTube gleda kada odlučuje šta da preporuči.",
                    "Bot pretplatnici nikada ne gledaju. Kanal zbog njih izgleda veći, dok njegovi video snimci stižu do manje ljudi.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Pravi gledaoci se pretplaćuju na YouTube kanal posle gledanja videa"},
            },
            {
                "h2": "Kako izgleda jedan mesec",
                "ul": [
                    "Prvi dani: kampanja počinje i stižu prvi gledaoci.",
                    "Svake nedelje: novi pretplatnici, lajkovi i komentari, pomalo svakog dana.",
                    "Do kraja meseca: uz {pick_name} obično {pick_audience} novih pretplatnika.",
                ],
            },
            {
                "h2": "Odakle dolaze vaši gledaoci",
                "p": [
                    "Recite nam grad, region ili zemlju iz koje treba da dolazi vaša publika. Vaš kanal prvo prikazujemo pravim ljudima tamo; gde je publika koja vam najviše odgovara veća, više njih može doći iz okoline.",
                ],
            },
        ],
        "faqs": [
            ("Koliko brzo stižu pretplatnici?", "Pomalo svakog dana, tokom celog meseca. Nikada sve odjednom: pravi ljudi se pretplaćuju svojim tempom."),
            ("Hoće li gledati moje video snimke?", "To su pravi ljudi koji su odlučili da se pretplate pošto su videli vaš kanal. Šta će sledeće gledati zavisi od njih, kao kod svake publike, i upravo zato se to računa."),
            ("Da li dobijam i lajkove i komentare?", "Da, od istih gledalaca: uz {pick_name} obično {pick_likes} lajkova i {pick_comments} komentara mesečno."),
            ("Da li vam treba moja lozinka?", "Nikada. Potreban nam je samo identifikator vašeg kanala, a kanal treba da bude javan."),
        ],
    },
]
