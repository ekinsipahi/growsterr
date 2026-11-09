"""Croatian YouTube pages: the hub and subscribers. Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "youtube",
        "label": "YouTube",
        "title": "Paketi rasta za YouTube kanale kreatora | Growsterr",
        "description": "Razvijte YouTube kanal uz stvarne ljude: mjesečni paketi donose pretplatnike, lajkove i komentare gledatelja koji su se sami pretplatili. Od {from_price}.",
        "h1": ("Razvijte svoj YouTube kanal ", "uz stvarne gledatelje."),
        "intro": "Mjesečni paketi rasta za kreatore. Stvarni ljudi otkrivaju vaš kanal, gledaju vaše videozapise i pretplate se kad im se svidi ono što vide. Nadzorna ploča pokazuje što smo izmjerili, dan po dan.",
        "hero": {"image": "youtube-hub", "alt": "YouTube kanal dobiva pretplatnike, lajkove i komentare od stvarnih gledatelja"},
        "sections": [
            {
                "h2": "Važni su pretplatnici koji gledaju",
                "p": [
                    "YouTube preporučuje videozapise koje ljudi gledaju, lajkaju i kojima se vraćaju. Pretplatnik koji nikad ne gleda gori je nego nijedan: smanjuje udio publike koja reagira.",
                    "Svaki pretplatnik kojeg dovedemo osoba je koja je pronašla vaš kanal i odlučila se pretplatiti. Lajkovi, pregledi i komentari dolaze od istih ljudi, unutar vašeg paketa.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Gledatelji gledaju YouTube videozapis kreatora i pišu komentare"},
            },
            {
                "h2": "Za kanale koji objavljuju s pažnjom",
                "p": [
                    "Tutorijali, vlogovi, glazba ili gaming: ako redovito objavljujete, stvarni gledatelji svakom novom videozapisu daju bolji početak. Počnite s paketom {starter_name} i prijeđite na veći kad vaš kanal bude spreman za više.",
                ],
                "ul": [
                    "Vi nam kažete iz kojeg grada, regije ili države bi trebala dolaziti vaša publika.",
                    "Pretplatnici, lajkovi i komentari stižu zajedno, od istih ljudi.",
                    "Kanal ostaje vaš: nikad ne tražimo vašu lozinku.",
                ],
                "image": {"image": "youtube-channel", "alt": "Kreator montira YouTube videozapis u kućnom studiju"},
            },
        ],
        "faqs": [
            ("Jesu li pretplatnici stvarni ljudi?", "Da. Svaki pretplatnik stvarna je osoba koja je pronašla vaš kanal i odlučila se pretplatiti. Bez botova, bez lažnih profila, ništa instant."),
            ("Koliko pretplatnika donosi paket?", "Obično {starter_audience} novih pretplatnika mjesečno uz {starter_name}, {rising_audience} uz {rising_name} i {pro_audience} uz {pro_name}. Tipični rasponi, a ne fiksan broj."),
            ("Trebate li moju lozinku za Google ili YouTube?", "Nikad. Treba nam samo identifikator vašeg kanala, a kanal bi trebao biti javan."),
            ("Mogu li kupiti samo preglede ili lajkove?", "Ne. Pregledi, lajkovi i komentari dolaze unutar svakog paketa, od istih stvarnih ljudi koji se pretplate."),
            ("Mogu li otkazati bilo kada?", "Da. Paketi se obnavljaju svaki mjesec, a otkazati ih možete u svom računu. Plaćeni mjesec traje do kraja."),
        ],
    },
    {
        "service": "subscribers",
        "slug": "youtube/pretplatnici",
        "label": "YouTube pretplatnici",
        "title": "Stvarni YouTube pretplatnici koji gledaju | Growsterr",
        "description": "YouTube pretplatnici koji su stvarni ljudi: gledatelji koji su pronašli vaš kanal i odlučili se pretplatiti, uz lajkove i komentare. Od {from_price} mjesečno.",
        "h1": ("YouTube pretplatnici ", "koji stvarno gledaju."),
        "intro": "Stvarni ljudi otkrivaju vaš kanal, gledaju vaše videozapise i pretplate se kad im se svidi ono što vide. Obično {starter_audience} novih pretplatnika mjesečno uz {starter_name}, s lajkovima i komentarima istih gledatelja.",
        "hero": {"image": "youtube-subscribers", "alt": "Stranica YouTube kanala s novim pretplatnicima, stvarnim gledateljima"},
        "sections": [
            {
                "h2": "Pretplatnik bi trebao biti gledatelj",
                "p": [
                    "Na YouTubeu pretplatnik koristi samo ako gleda. Stvarni pretplatnici vide vaš sljedeći videozapis, pogledaju ga, lajkaju i ponekad komentiraju, a upravo to YouTube gleda kad odlučuje što preporučiti.",
                    "Pretplatnici botovi nikad ne gledaju. Kanal zbog njih izgleda veći, a njegovi videozapisi dopiru do manje ljudi.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Stvarni gledatelji pretplaćuju se na YouTube kanal nakon što pogledaju videozapis"},
            },
            {
                "h2": "Kako izgleda jedan mjesec",
                "ul": [
                    "Prvi dani: kampanja kreće i stižu prvi gledatelji.",
                    "Svaki tjedan: novi pretplatnici, lajkovi i komentari, pomalo svaki dan.",
                    "Do kraja mjeseca: obično {pick_audience} novih pretplatnika uz {pick_name}.",
                ],
            },
            {
                "h2": "Odakle dolaze vaši gledatelji",
                "p": [
                    "Recite nam iz kojeg grada, regije ili države bi trebala dolaziti vaša publika. Vaš kanal najprije prikazujemo stvarnim ljudima ondje; gdje je publika koja vam najbolje odgovara veća, više ih može doći iz okolice.",
                ],
            },
        ],
        "faqs": [
            ("Koliko brzo stižu pretplatnici?", "Pomalo svaki dan, kroz cijeli mjesec. Nikad sve odjednom: stvarni ljudi pretplaćuju se vlastitim tempom."),
            ("Hoće li gledati moje videozapise?", "To su stvarni ljudi koji su se pretplatili nakon što su vidjeli vaš kanal. Što će gledati dalje, odlučuju sami, kao i svaka publika, i upravo zato se to računa."),
            ("Dobivam li i lajkove i komentare?", "Da, od istih gledatelja: obično {pick_likes} lajkova i {pick_comments} komentara mjesečno uz {pick_name}."),
            ("Trebate li moju lozinku?", "Nikad. Treba nam samo identifikator vašeg kanala, a kanal bi trebao biti javan."),
        ],
    },
]
