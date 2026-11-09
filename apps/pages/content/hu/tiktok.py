"""Hungarian TikTok pages: the hub and likes. Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "tiktok",
        "label": "TikTok",
        "title": "TikTok-növekedési csomagok alkotóknak | Growsterr",
        "description": "Növekedj a TikTokon valódi emberekkel: havi csomagok új követőkkel, lájkokkal és kommentekkel azoktól, akik maguk választanak téged. Már havi {from_price}.",
        "h1": ("TikTok-növekedés ", "valódi emberekkel."),
        "intro": "Havi növekedési csomagok alkotóknak és influencereknek. Valódi emberek fedezik fel a profilodat, megnézik a videóidat, és ha tetszik, amit látnak, bekövetnek. Az irányítópultod napról napra mutatja, mit mértünk.",
        "hero": {"image": "tiktok-hub", "alt": "Egy TikTok-alkotó profilja, ahová új követők és lájkok érkeznek"},
        "sections": [
            {
                "h2": "A TikTokon a figyelem minden",
                "p": [
                    "A TikTok annál több embernek mutat meg egy videót, minél inkább végignézik, lájkolják, kommentelik az első nézők, és minél többen követnek be. Az ember nélküli számok ebből semmit nem mozdítanak meg.",
                    "A csomagjaink minden nap valódi embereket hoznak a profilodra. Ők néznek, döntenek, és akiknek tetszenek a videóid, követnek és lájkolnak. Ez az a fajta figyelem, amelytől egy videó messzire jut.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Valódi nézők nézik egy alkotó TikTok-videóit"},
            },
            {
                "h2": "Alkotóknak, akiknek van mondanivalójuk",
                "p": [
                    "Humor, főzés, divat vagy oktatóvideók: ha rendszeresen posztolsz, a valódi nézők minden új videódnak jobb indulást adnak. Kezdd a {starter_name} csomaggal, és lépj feljebb, amikor készen állsz.",
                ],
                "ul": [
                    "Te mondod meg, melyik városból, régióból vagy országból érkezzen a közönséged.",
                    "Követők, lájkok és kommentek együtt érkeznek, ugyanazoktól az emberektől.",
                    "A fiókod a tiéd marad: a jelszavadat soha nem kérjük el.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Egy alkotó állványra tett telefonnal TikTok-videót forgat"},
            },
        ],
        "faqs": [
            ("Valódi emberek a követők?", "Igen. Minden követő valódi ember, aki látta a profilodat, és úgy döntött, hogy követ. Soha nem használunk botokat, hamis fiókokat vagy azonnali kiszállítást."),
            ("Hány követőt hoz egy csomag?", "A {starter_name} csomaggal jellemzően havi {starter_audience} új követőt, a {rising_name} csomaggal {rising_audience}, a {pro_name} csomaggal {pro_audience} követőt. Jellemző tartományok, nem fix mennyiség: valódi emberek döntenek maguktól."),
            ("Kell a TikTok-jelszavam?", "Soha. Csak a felhasználónevedre van szükségünk. A fiókod legyen nyilvános, hogy aki rátalál, követni tudja."),
            ("Vehetek külön megtekintéseket vagy lájkokat?", "Nem. A megtekintések, lájkok és kommentek minden csomagban benne vannak, ugyanazoktól a valódi emberektől, akik követnek."),
            ("Bármikor lemondhatom?", "Igen. A csomagok havonta megújulnak, és a fiókodból bármikor lemondhatod őket. A kifizetett hónap a végéig tart."),
        ],
    },
    {
        "service": "likes",
        "slug": "tiktok/lajkok",
        "label": "TikTok-lájkok",
        "title": "TikTok-lájkok valódi emberektől, minden csomagban",
        "description": "TikTok-lájkok valódi emberektől, akik nézik a videóidat, soha nem botoktól. Minden havi csomag része, követőkkel és kommentekkel. Már havi {from_price}.",
        "h1": ("TikTok-lájkok valódi emberektől. ", "Minden csomagban."),
        "intro": "Lájkot nem árulunk külön. Minden csomag valódi embereket hoz, akik felfedezik a profilodat, megnézik a videóidat, és lájkolják, ami tetszik nekik: a {starter_name} csomaggal havonta jellemzően {starter_likes} lájkot kapsz.",
        "hero": {"image": "tiktok-likes", "alt": "Valódi nézők lájkjai szállnak fel egy TikTok-videóból"},
        "sections": [
            {
                "h2": "Miért csak akkor számít egy lájk, ha ember áll mögötte?",
                "p": [
                    "A TikTok azt figyeli, mi történik egy lájk körül: tovább nézte a néző a videót, bekövetett, visszajött? A botok lájkjai mindenre nemmel felelnek, így hozzáadnak egy számot, de elvesznek az elérésből.",
                    "A valódi emberek lájkjai a többivel együtt jönnek: nézési idővel, követésekkel és kommentekkel. Ez az a jelzés, amelytől egy videó messzire jut.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Nézők végignéznek egy TikTok-videót, és lájkolják"},
            },
            {
                "h2": "Hány lájkot hoznak a csomagok?",
                "ul": [
                    "{starter_name} (havi {starter_price}): jellemzően {starter_likes} lájk.",
                    "{rising_name} (havi {rising_price}): jellemzően {rising_likes} lájk, az általad választott videókon.",
                    "{pro_name} (havi {pro_price}): jellemzően {pro_likes} lájk, elsőbbséggel.",
                ],
            },
            {
                "h2": "Miért nem árulunk külön lájkot?",
                "p": [
                    "A megtekintések, követések és kommentek nélkül érkező lájkok pontosan annak látszanak, amik. A csomagon belül minden lájk olyasvalakitől jön, aki megnézte a videót, így a számaid együtt mozognak, ahogy a valódi növekedésnél.",
                ],
            },
        ],
        "faqs": [
            ("Kaphatok TikTok-lájkokat csomag nélkül?", "Nem. Lájkok, megtekintések és kommentek csak a havi csomagjainkban érkeznek, ugyanazoktól a valódi emberektől. Ettől maradnak természetesek."),
            ("Melyik videóim kapják a lájkokat?", "Valódi emberek azt lájkolják, ami tetszik nekik, általában a legújabb videóidat. A {rising_name} és a {pro_name} csomaggal te választhatod ki, mely videók kapják a figyelmet."),
            ("Milyen gyorsan érkeznek a lájkok?", "Minden nap egy kicsit, a hónap során. Soha nem azonnal: az azonnali lájk mögött bot áll."),
            ("Kell a TikTok-jelszavam?", "Soha. Csak a felhasználónevedre van szükségünk, és a fiókodnak nyilvánosnak kell lennie."),
        ],
    },
]
