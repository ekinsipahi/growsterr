"""Bosnian YouTube pages: the hub and subscribers. Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "youtube",
        "label": "YouTube",
        "title": "Paketi za rast na YouTubeu za kreatore | Growsterr",
        "description": "Razvijte YouTube kanal uz stvarne ljude: mjesečni paketi donose pretplatnike, lajkove i komentare od gledalaca koji su se sami pretplatili. Od {from_price} mjesečno.",
        "h1": ("Razvijte svoj YouTube kanal ", "uz stvarne gledaoce."),
        "intro": "Mjesečni paketi rasta za kreatore. Stvarni ljudi otkrivaju vaš kanal, gledaju vaše videe i pretplate se kada im se svidi ono što vide. Kontrolna ploča pokazuje šta smo izmjerili, dan po dan.",
        "hero": {"image": "youtube-hub", "alt": "YouTube kanal koji dobija pretplatnike, lajkove i komentare od stvarnih gledalaca"},
        "sections": [
            {
                "h2": "Važni su pretplatnici koji gledaju",
                "p": [
                    "YouTube preporučuje videe koje ljudi gledaju, lajkuju i kojima se vraćaju. Pretplatnik koji nikad ne gleda gori je nego nikakav: smanjuje udio publike koja reaguje.",
                    "Svaki pretplatnik kojeg dovedemo je osoba koja je pronašla vaš kanal i odlučila da se pretplati. Lajkovi, pregledi i komentari dolaze od istih ljudi, u okviru vašeg paketa.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Gledaoci gledaju YouTube video kreatora i pišu komentare"},
            },
            {
                "h2": "Za kanale koji objavljuju s pažnjom",
                "p": [
                    "Tutorijali, vlogovi, muzika ili gaming: ako redovno objavljujete, stvarni gledaoci daju svakom novom videu bolji početak. Počnite s paketom {starter_name} i pređite na veći kada vaš kanal bude spreman za više.",
                ],
                "ul": [
                    "Vi nam kažete grad, regiju ili državu iz koje treba doći vaša publika.",
                    "Pretplatnici, lajkovi i komentari dolaze zajedno, od istih ljudi.",
                    "Vaš kanal ostaje vaš: nikada ne tražimo vašu lozinku.",
                ],
                "image": {"image": "youtube-channel", "alt": "Kreator montira YouTube video u kućnom studiju"},
            },
        ],
        "faqs": [
            ("Da li su pretplatnici stvarni ljudi?", "Da. Svaki pretplatnik je stvarna osoba koja je pronašla vaš kanal i odlučila da se pretplati. Bez botova, bez lažnih računa, ništa instant."),
            ("Koliko pretplatnika donosi jedan paket?", "Obično {starter_audience} novih pretplatnika mjesečno uz {starter_name}, {rising_audience} uz {rising_name} i {pro_audience} uz {pro_name}. Tipični rasponi, a ne fiksna količina."),
            ("Da li vam treba moja lozinka za Google ili YouTube?", "Nikada. Treba nam samo handle vašeg kanala, a kanal treba biti javan."),
            ("Mogu li kupiti samo preglede ili lajkove?", "Ne. Pregledi, lajkovi i komentari dolaze u svakom paketu, od istih stvarnih ljudi koji se pretplate."),
            ("Mogu li otkazati u bilo kojem trenutku?", "Da. Paketi se obnavljaju mjesečno i možete ih otkazati na svom računu. Mjesec koji ste platili traje do kraja."),
        ],
    },
    {
        "service": "subscribers",
        "slug": "youtube/pretplatnici",
        "label": "YouTube pretplatnici",
        "title": "Stvarni YouTube pretplatnici koji gledaju | Growsterr",
        "description": "YouTube pretplatnici koji su stvarni ljudi: gledaoci koji su pronašli vaš kanal i sami se pretplatili, uz lajkove i komentare. Od {from_price} mjesečno.",
        "h1": ("YouTube pretplatnici ", "koji zaista gledaju."),
        "intro": "Stvarni ljudi otkrivaju vaš kanal, gledaju vaše videe i pretplate se kada im se svidi ono što vide. Obično {starter_audience} novih pretplatnika mjesečno uz {starter_name}, uz lajkove i komentare od istih gledalaca.",
        "hero": {"image": "youtube-subscribers", "alt": "Stranica YouTube kanala s novim pretplatnicima od stvarnih gledalaca"},
        "sections": [
            {
                "h2": "Pretplatnik treba biti gledalac",
                "p": [
                    "Na YouTubeu je pretplatnik koristan samo ako gleda. Stvarni pretplatnici vide vaš sljedeći video, pogledaju ga, lajkuju i ponekad komentarišu, a upravo to YouTube gleda kada odlučuje šta će preporučiti.",
                    "Bot pretplatnici nikad ne gledaju. Zbog njih kanal izgleda veći, dok njegovi videi dopiru do manje ljudi.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Stvarni gledaoci se pretplaćuju na YouTube kanal nakon što pogledaju video"},
            },
            {
                "h2": "Kako izgleda jedan mjesec",
                "ul": [
                    "Prvi dani: vaša kampanja počinje i stižu prvi gledaoci.",
                    "Svake sedmice: novi pretplatnici, lajkovi i komentari, po nekoliko svaki dan.",
                    "Do kraja mjeseca: obično {pick_audience} novih pretplatnika uz {pick_name}.",
                ],
            },
            {
                "h2": "Odakle dolaze vaši gledaoci",
                "p": [
                    "Recite nam grad, regiju ili državu iz koje treba doći vaša publika. Vaš kanal prvo prikazujemo stvarnim ljudima odatle; tamo gdje je publika koja vam najbolje odgovara veća, više njih može doći iz okoline.",
                ],
            },
        ],
        "faqs": [
            ("Koliko brzo stižu pretplatnici?", "Pomalo svaki dan, tokom cijelog mjeseca. Nikada sve odjednom: stvarni ljudi se pretplaćuju svojim tempom."),
            ("Hoće li gledati moje videe?", "To su stvarni ljudi koji su se pretplatili nakon što su vidjeli vaš kanal. Šta će sljedeće gledati odlučuju oni, kao i svaka publika, i upravo zato se to računa."),
            ("Dobijam li i lajkove i komentare?", "Da, od istih gledalaca: obično {pick_likes} lajkova i {pick_comments} komentara mjesečno uz {pick_name}."),
            ("Da li vam treba moja lozinka?", "Nikada. Treba nam samo handle vašeg kanala, a kanal treba biti javan."),
        ],
    },
]
