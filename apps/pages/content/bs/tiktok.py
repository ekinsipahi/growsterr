"""Bosnian TikTok pages: the hub and likes. Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "tiktok",
        "label": "TikTok",
        "title": "Paketi za rast na TikToku za kreatore | Growsterr",
        "description": "Rastite na TikToku uz stvarne ljude: mjesečni paketi donose nove pratioce, lajkove i komentare od ljudi koji su vas sami zapratili. Od {from_price} mjesečno.",
        "h1": ("Razvijte svoj TikTok ", "uz stvarne ljude."),
        "intro": "Mjesečni paketi rasta za kreatore i influencere. Stvarni ljudi otkrivaju vaš profil, gledaju vaše videe i zaprate vas kada im se svidi ono što vide. Kontrolna ploča pokazuje šta smo izmjerili, dan po dan.",
        "hero": {"image": "tiktok-hub", "alt": "TikTok profil kreatora na koji stižu novi pratioci i lajkovi"},
        "sections": [
            {
                "h2": "Na TikToku je pažnja sve",
                "p": [
                    "TikTok prikazuje video većem broju ljudi kada ga prvi gledaoci pogledaju, lajkuju, komentarišu i zaprate autora. Brojevi iza kojih ne stoje ljudi ništa od toga ne pokreću.",
                    "Naši paketi svaki dan dovode stvarne ljude na vaš profil. Oni gledaju i odlučuju, a oni kojima se vaši videi dopadnu zaprate vas i lajkuju. Upravo takva pažnja pomaže videu da stigne dalje.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Stvarni gledaoci gledaju TikTok videe kreatora"},
            },
            {
                "h2": "Za kreatore koji imaju šta reći",
                "p": [
                    "Komedija, kuhanje, moda ili tutorijali: ako redovno objavljujete, stvarni gledaoci daju svakom novom videu bolji početak. Počnite s paketom {starter_name} i pređite na veći kada budete spremni.",
                ],
                "ul": [
                    "Vi nam kažete grad, regiju ili državu iz koje treba doći vaša publika.",
                    "Pratioci, lajkovi i komentari dolaze zajedno, od istih ljudi.",
                    "Vaš profil ostaje vaš: nikada ne tražimo vašu lozinku.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Kreator snima TikTok video telefonom na stativu"},
            },
        ],
        "faqs": [
            ("Da li su pratioci stvarni ljudi?", "Da. Svaki pratilac je stvarna osoba koja je vidjela vaš profil i odlučila da vas prati. Nikada ne koristimo botove, lažne račune ni instant isporuku."),
            ("Koliko pratilaca donosi jedan paket?", "Obično {starter_audience} novih pratilaca mjesečno uz {starter_name}, {rising_audience} uz {rising_name} i {pro_audience} uz {pro_name}. Tipični rasponi, a ne fiksna količina: stvarni ljudi odlučuju sami."),
            ("Da li vam treba moja lozinka za TikTok?", "Nikada. Treba nam samo vaše korisničko ime. Neka vaš profil bude javan kako bi vas ljudi koji ga otkriju mogli zapratiti."),
            ("Mogu li kupiti samo preglede ili lajkove?", "Ne. Pregledi, lajkovi i komentari dolaze u svakom paketu, od istih stvarnih ljudi koji vas prate."),
            ("Mogu li otkazati u bilo kojem trenutku?", "Da. Paketi se obnavljaju mjesečno i možete ih otkazati na svom računu. Mjesec koji ste platili traje do kraja."),
        ],
    },
    {
        "service": "likes",
        "slug": "tiktok/lajkovi",
        "label": "TikTok lajkovi",
        "title": "TikTok lajkovi od stvarnih ljudi, u svakom paketu",
        "description": "TikTok lajkovi od stvarnih ljudi koji gledaju vaše videe, nikad od botova. Dolaze u svakom mjesečnom paketu, uz pratioce i komentare. Od {from_price} mjesečno.",
        "h1": ("TikTok lajkovi od stvarnih ljudi. ", "U svakom paketu."),
        "intro": "Lajkove ne prodajemo zasebno. Svaki paket dovodi stvarne ljude koji otkriju vaš profil, gledaju vaše videe i lajkuju ono što im se dopadne: obično {starter_likes} lajkova mjesečno uz {starter_name}.",
        "hero": {"image": "tiktok-likes", "alt": "Lajkovi stvarnih gledalaca koji se dižu iznad TikTok videa"},
        "sections": [
            {
                "h2": "Zašto se lajk računa samo kad iza njega stoji osoba",
                "p": [
                    "TikTok prati šta se dešava oko lajka: da li je gledalac nastavio gledati, zapratio vas, vratio se? Lajkovi od botova na sve to odgovaraju s „ne”, pa dodaju broj, a oduzimaju doseg.",
                    "Lajkovi od stvarnih ljudi dolaze s ostalim: vremenom gledanja, praćenjima i komentarima. To je signal koji pomaže videu da stigne dalje.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Gledaoci gledaju TikTok video do kraja i lajkuju ga"},
            },
            {
                "h2": "Koliko lajkova donosi svaki paket",
                "ul": [
                    "{starter_name} ({starter_price} mjesečno): obično {starter_likes} lajkova.",
                    "{rising_name} ({rising_price} mjesečno): obično {rising_likes} lajkova, na videima koje vi odaberete.",
                    "{pro_name} ({pro_price} mjesečno): obično {pro_likes} lajkova, uz prioritetno mjesto.",
                ],
            },
            {
                "h2": "Zašto lajkove ne prodajemo zasebno",
                "p": [
                    "Lajkovi koji stignu bez pregleda, praćenja i komentara izgledaju upravo onako kakvi jesu. U paketu svaki lajk dolazi od nekoga ko je gledao, pa se vaši brojevi kreću zajedno, kao kod stvarnog rasta.",
                ],
            },
        ],
        "faqs": [
            ("Mogu li dobiti TikTok lajkove bez paketa?", "Ne. Lajkovi, pregledi i komentari dolaze samo u našim mjesečnim paketima, od istih stvarnih ljudi. Upravo zato ostaju prirodni."),
            ("Koji videi dobijaju lajkove?", "Stvarni ljudi lajkuju ono što im se dopada, najčešće vaše najnovije videe. Uz {rising_name} i {pro_name} možete odabrati koji videi dobijaju pažnju."),
            ("Koliko brzo stižu lajkovi?", "Pomalo svaki dan, tokom cijelog mjeseca. Nikada odmah: instant lajk je bot."),
            ("Da li vam treba moja lozinka za TikTok?", "Nikada. Treba nam samo vaše korisničko ime, a vaš profil treba biti javan."),
        ],
    },
]
