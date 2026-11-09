"""Hungarian YouTube pages: the hub and subscribers. Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "youtube",
        "label": "YouTube",
        "title": "YouTube-növekedési csomagok alkotóknak | Growsterr",
        "description": "Növeld a YouTube-csatornádat valódi emberekkel: havi csomagok feliratkozókkal, lájkokkal és kommentekkel önként feliratkozó nézőktől. Már havi {from_price}.",
        "h1": ("Növeld a YouTube-csatornádat ", "valódi nézőkkel."),
        "intro": "Havi növekedési csomagok alkotóknak. Valódi emberek fedezik fel a csatornádat, megnézik a videóidat, és ha tetszik, amit látnak, feliratkoznak. Az irányítópultod napról napra mutatja, mit mértünk.",
        "hero": {"image": "youtube-hub", "alt": "Egy YouTube-csatorna, amely valódi nézőktől kap feliratkozókat, lájkokat és kommenteket"},
        "sections": [
            {
                "h2": "Azok a feliratkozók számítanak, akik néznek is",
                "p": [
                    "A YouTube azokat a videókat ajánlja, amelyeket az emberek megnéznek, lájkolnak, és amelyekhez visszatérnek. Egy feliratkozó, aki soha nem néz, rosszabb, mintha nem is lenne: csökkenti a közönséged aktív részének arányát.",
                    "Minden feliratkozó, akit hozunk, olyan ember, aki rátalált a csatornádra, és úgy döntött, hogy feliratkozik. A lájkok, megtekintések és kommentek ugyanezektől az emberektől jönnek, a csomagod részeként.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Nézők egy alkotó YouTube-videóját nézik, és kommentet írnak"},
            },
            {
                "h2": "Csatornáknak, amelyek gondosan publikálnak",
                "p": [
                    "Oktatóvideók, vlogok, zene vagy gaming: ha rendszeresen publikálsz, a valódi nézők minden új videódnak jobb indulást adnak. Kezdd a {starter_name} csomaggal, és lépj feljebb, amikor a csatornád készen áll többre.",
                ],
                "ul": [
                    "Te mondod meg, melyik városból, régióból vagy országból érkezzen a közönséged.",
                    "Feliratkozók, lájkok és kommentek együtt érkeznek, ugyanazoktól az emberektől.",
                    "A csatornád a tiéd marad: a jelszavadat soha nem kérjük el.",
                ],
                "image": {"image": "youtube-channel", "alt": "Egy alkotó YouTube-videót vág az otthoni stúdiójában"},
            },
        ],
        "faqs": [
            ("Valódi emberek a feliratkozók?", "Igen. Minden feliratkozó valódi ember, aki rátalált a csatornádra, és úgy döntött, hogy feliratkozik. Nincsenek botok, hamis fiókok, és semmi sem azonnali."),
            ("Hány feliratkozót hoz egy csomag?", "A {starter_name} csomaggal jellemzően havi {starter_audience} új feliratkozót, a {rising_name} csomaggal {rising_audience}, a {pro_name} csomaggal {pro_audience} feliratkozót. Jellemző tartományok, nem fix mennyiség."),
            ("Kell a Google- vagy YouTube-jelszavam?", "Soha. Csak a csatornád azonosítójára van szükségünk, és a csatornádnak nyilvánosnak kell lennie."),
            ("Vehetek külön megtekintéseket vagy lájkokat?", "Nem. A megtekintések, lájkok és kommentek minden csomagban benne vannak, ugyanazoktól a valódi emberektől, akik feliratkoznak."),
            ("Bármikor lemondhatom?", "Igen. A csomagok havonta megújulnak, és a fiókodból bármikor lemondhatod őket. A kifizetett hónap a végéig tart."),
        ],
    },
    {
        "service": "subscribers",
        "slug": "youtube/feliratkozok",
        "label": "YouTube-feliratkozók",
        "title": "Valódi YouTube-feliratkozók, akik néznek is | Growsterr",
        "description": "YouTube-feliratkozók, akik valódi emberek: nézők, akik rátaláltak a csatornádra és feliratkoztak, lájkokkal és kommentekkel. Már havi {from_price}.",
        "h1": ("YouTube-feliratkozók, ", "akik tényleg néznek."),
        "intro": "Valódi emberek fedezik fel a csatornádat, megnézik a videóidat, és ha tetszik, amit látnak, feliratkoznak. A {starter_name} csomaggal havonta jellemzően {starter_audience} új feliratkozó, lájkokkal és kommentekkel ugyanezektől a nézőktől.",
        "hero": {"image": "youtube-subscribers", "alt": "Egy YouTube-csatornaoldal új feliratkozókkal, valódi nézőktől"},
        "sections": [
            {
                "h2": "A feliratkozó legyen néző is",
                "p": [
                    "A YouTube-on egy feliratkozó csak akkor hasznos, ha néz. A valódi feliratkozók látják a következő feltöltésedet, megnézik, lájkolják, és néha kommentelnek is, a YouTube pedig éppen ezt figyeli, amikor eldönti, mit ajánljon.",
                    "A bot feliratkozók soha nem néznek. Nagyobbnak mutatják a csatornát, miközben a videói kevesebb emberhez jutnak el.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Valódi nézők feliratkoznak egy YouTube-csatornára, miután megnéztek egy videót"},
            },
            {
                "h2": "Így néz ki egy hónap",
                "ul": [
                    "Az első napok: elindul a kampányod, és megérkeznek az első nézők.",
                    "Minden héten: új feliratkozók, lájkok és kommentek, naponta néhány.",
                    "A hónap végére: a {pick_name} csomaggal jellemzően {pick_audience} új feliratkozó.",
                ],
            },
            {
                "h2": "Honnan érkeznek a nézőid?",
                "p": [
                    "Mondd meg, melyik városból, régióból vagy országból érkezzen a közönséged. Először az ottani valódi embereknek mutatjuk a csatornádat; ahol a legjobban illő közönség nagyobb, a közelből többen is érkezhetnek.",
                ],
            },
        ],
        "faqs": [
            ("Milyen gyorsan érkeznek a feliratkozók?", "Minden nap egy kicsit, az egész hónap során. Soha nem egyszerre: valódi emberek a saját tempójukban iratkoznak fel."),
            ("Megnézik majd a videóimat?", "Valódi emberek, akik a csatornád láttán döntöttek a feliratkozás mellett. Hogy mit néznek meg ezután, az rajtuk múlik, mint bármely közönségnél, és pont ezért számít."),
            ("Lájkokat és kommenteket is kapok?", "Igen, ugyanazoktól a nézőktől: a {pick_name} csomaggal havonta jellemzően {pick_likes} lájkot és {pick_comments} kommentet."),
            ("Kell a jelszavam?", "Soha. Csak a csatornád azonosítójára van szükségünk, és a csatornádnak nyilvánosnak kell lennie."),
        ],
    },
]
