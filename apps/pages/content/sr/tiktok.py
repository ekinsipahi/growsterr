"""Serbian (Latin script) TikTok pages: the hub and likes. Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "tiktok",
        "label": "TikTok",
        "title": "Paketi za rast na TikToku za kreatore | Growsterr",
        "description": "Rastite na TikToku uz prave ljude: mesečni paketi donose nove pratioce, lajkove i komentare od ljudi koji su vas sami zapratili. Od {from_price} mesečno.",
        "h1": ("Rastite na TikToku ", "uz prave ljude."),
        "intro": "Mesečni paketi za rast, namenjeni kreatorima i influenserima. Pravi ljudi otkrivaju vaš profil, gledaju vaše video snimke i zaprate vas kada im se dopadne ono što vide. Kontrolna tabla pokazuje šta smo izmerili, dan po dan.",
        "hero": {"image": "tiktok-hub", "alt": "TikTok profil kreatora na koji stižu novi pratioci i lajkovi"},
        "sections": [
            {
                "h2": "Na TikToku je pažnja sve",
                "p": [
                    "TikTok prikazuje video većem broju ljudi kada ga prvi gledaoci odgledaju, lajkuju, komentarišu i zaprate autora. Brojke iza kojih nema ljudi ništa od toga ne pokreću.",
                    "Naši paketi svakog dana dovode prave ljude na vaš profil. Oni gledaju i odlučuju, a oni kojima se vaši video snimci dopadnu zaprate vas i lajkuju. Upravo takva pažnja pomaže da se video proširi.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Pravi gledaoci gledaju TikTok video snimke kreatora"},
            },
            {
                "h2": "Za kreatore koji imaju šta da kažu",
                "p": [
                    "Komedija, kuvanje, moda ili tutorijali: ako redovno objavljujete, pravi gledaoci daju svakom novom videu bolji početak. Počnite sa paketom {starter_name} i pređite na veći kada budete spremni.",
                ],
                "ul": [
                    "Vi nam kažete grad, region ili zemlju iz koje treba da dolazi vaša publika.",
                    "Pratioci, lajkovi i komentari stižu zajedno, od istih ljudi.",
                    "Nalog ostaje vaš: nikada ne tražimo vašu lozinku.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Kreator snima TikTok video telefonom na stativu"},
            },
        ],
        "faqs": [
            ("Da li su pratioci pravi ljudi?", "Da. Svaki pratilac je prava osoba koja je videla vaš profil i odlučila da vas prati. Nikada ne koristimo botove, lažne naloge niti isporuku „odmah”."),
            ("Koliko pratilaca donosi jedan paket?", "Obično {starter_audience} novih pratilaca mesečno uz {starter_name}, {rising_audience} uz {rising_name} i {pro_audience} uz {pro_name}. Tipični rasponi, a ne fiksan broj: pravi ljudi odlučuju sami."),
            ("Da li vam treba moja lozinka za TikTok?", "Nikada. Potrebno nam je samo vaše korisničko ime. Neka nalog bude javan, kako bi ljudi koji ga otkriju mogli da vas zaprate."),
            ("Mogu li da kupim samo preglede ili lajkove?", "Ne. Pregledi, lajkovi i komentari dolaze u okviru svakog paketa, od istih pravih ljudi koji vas prate."),
            ("Mogu li da otkažem bilo kada?", "Da. Paketi se obnavljaju mesečno, a otkazati možete iz svog naloga. Plaćeni mesec traje do kraja."),
        ],
    },
    {
        "service": "likes",
        "slug": "tiktok/lajkovi",
        "label": "TikTok lajkovi",
        "title": "TikTok lajkovi od pravih ljudi, u svakom paketu",
        "description": "TikTok lajkovi od pravih ljudi koji gledaju vaše video snimke, nikada od botova. Stižu u svakom mesečnom paketu, uz pratioce i komentare. Od {from_price}.",
        "h1": ("TikTok lajkovi od pravih ljudi. ", "U svakom paketu."),
        "intro": "Lajkove ne prodajemo zasebno. Svaki paket dovodi prave ljude koji otkriju vaš profil, gledaju vaše video snimke i lajkuju ono što im se dopadne: uz {starter_name} obično {starter_likes} lajkova mesečno.",
        "hero": {"image": "tiktok-likes", "alt": "Lajkovi pravih gledalaca koji se nižu iznad TikTok videa"},
        "sections": [
            {
                "h2": "Zašto se lajk računa samo kada iza njega stoji osoba",
                "p": [
                    "TikTok prati šta se dešava oko lajka: da li je gledalac nastavio da gleda, zapratio autora, vratio se? Lajkovi od botova na sve to odgovaraju sa „ne”, pa dodaju broj, a oduzimaju doseg.",
                    "Lajkovi od pravih ljudi dolaze sa svim ostalim: vremenom gledanja, praćenjem i komentarima. To je signal koji pomaže da se video proširi.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Gledaoci odgledaju TikTok video do kraja i lajkuju ga"},
            },
            {
                "h2": "Koliko lajkova donosi svaki paket",
                "ul": [
                    "{starter_name} ({starter_price} mesečno): obično {starter_likes} lajkova.",
                    "{rising_name} ({rising_price} mesečno): obično {rising_likes} lajkova, na video snimcima koje izaberete.",
                    "{pro_name} ({pro_price} mesečno): obično {pro_likes} lajkova, uz prioritetno mesto.",
                ],
            },
            {
                "h2": "Zašto lajkove ne prodajemo zasebno",
                "p": [
                    "Lajkovi koji stignu bez pregleda, praćenja i komentara izgledaju tačno onako kakvi jesu. U okviru paketa svaki lajk dolazi od nekoga ko je gledao, pa se vaše brojke kreću zajedno, kao kod pravog rasta.",
                ],
            },
        ],
        "faqs": [
            ("Mogu li da dobijem TikTok lajkove bez paketa?", "Ne. Lajkovi, pregledi i komentari dolaze samo u okviru naših mesečnih paketa, od istih pravih ljudi. Upravo zato ostaju prirodni."),
            ("Koji video snimci dobijaju lajkove?", "Pravi ljudi lajkuju ono što im se dopadne, najčešće vaše najnovije video snimke. Uz {rising_name} i {pro_name} možete sami izabrati koji video snimci dobijaju pažnju."),
            ("Koliko brzo stižu lajkovi?", "Pomalo svakog dana, tokom celog meseca. Nikada odmah: lajk koji stigne odmah dolazi od bota."),
            ("Da li vam treba moja lozinka za TikTok?", "Nikada. Potrebno nam je samo vaše korisničko ime, a nalog treba da bude javan."),
        ],
    },
]
