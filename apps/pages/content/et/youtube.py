"""Estonian YouTube pages: the hub and subscribers (tellijad). Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "youtube",
        "label": "YouTube",
        "title": "YouTube'i kasvupaketid sisuloojatele | Growsterr",
        "description": "Kasvata YouTube'i kanalit päris inimestega: kuupaketid toovad tellijaid, meeldimisi ja kommentaare vaatajatelt, kes otsustasid tellida. Alates {from_price} kuus.",
        "h1": ("Kasvata oma YouTube'i kanalit ", "päris vaatajatega."),
        "intro": "Tahad osta YouTube'i tellijaid või vaatamisi? Siin on aus variant: kuupõhised kasvupaketid sisuloojatele. Päris inimesed avastavad sinu kanali, vaatavad sinu videoid ja tellivad selle, kui nähtu neile meeldib. Töölaud näitab päev-päevalt, mida me mõõtsime.",
        "hero": {"image": "youtube-hub", "alt": "YouTube'i kanal saab päris vaatajatelt tellijaid, meeldimisi ja kommentaare"},
        "sections": [
            {
                "h2": "Loevad tellijad, kes vaatavad",
                "p": [
                    "YouTube soovitab videoid, mida inimesed vaatavad, millele annavad meeldimise ja mille juurde tagasi tulevad. Tellija, kes kunagi ei vaata, on halvem kui mitte ühtegi: ta vähendab sinu publiku aktiivset osa.",
                    "Iga tellija, kelle me toome, on inimene, kes leidis sinu kanali ja otsustas selle tellida. Meeldimised, vaatamised ja kommentaarid tulevad samadelt inimestelt, sinu paketi sees.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Vaatajad vaatavad sisulooja YouTube'i videot ja kirjutavad kommentaare"},
            },
            {
                "h2": "Kanalitele, mis avaldavad hoolega",
                "p": [
                    "Õpetused, vlogid, muusika või mängud: kui avaldad regulaarselt, annavad päris vaatajad igale uuele videole parema alguse. Alusta paketiga {starter_name} ja liigu edasi, kui sinu kanal on valmis rohkemaks.",
                ],
                "ul": [
                    "Sina ütled, millisest linnast, piirkonnast või riigist sinu publik peaks tulema.",
                    "Tellijad, meeldimised ja kommentaarid tulevad koos, samadelt inimestelt.",
                    "Kanal jääb sinu omaks: me ei küsi kunagi sinu parooli.",
                ],
                "image": {"image": "youtube-channel", "alt": "Sisulooja monteerib kodustuudios YouTube'i videot"},
            },
        ],
        "faqs": [
            ("Kas tellijad on päris inimesed?", "Jah. Iga tellija on päris inimene, kes leidis sinu kanali ja otsustas selle tellida. Ei mingeid botte, võltskontosid ega midagi silmapilkset."),
            ("Mitu tellijat pakett toob?", "Paketiga {starter_name} tavaliselt {starter_audience} uut tellijat kuus, paketiga {rising_name} {rising_audience} ja paketiga {pro_name} {pro_audience}. Tüüpilised vahemikud, mitte kindel arv."),
            ("Kas te vajate minu Google'i või YouTube'i parooli?", "Mitte kunagi. Vajame ainult sinu kanali käepidet ja kanal peaks olema avalik."),
            ("Kas vaatamisi või meeldimisi saab osta eraldi?", "Ei. Vaatamised, meeldimised ja kommentaarid tulevad iga paketi sees, samadelt päris inimestelt, kes sinu kanali tellivad."),
            ("Kas saan igal ajal tühistada?", "Jah. Paketid uuenevad kord kuus ja tühistada saad oma kontol. Juba makstud kuu kestab lõpuni."),
        ],
    },
    {
        "service": "subscribers",
        "slug": "youtube/tellijad",
        "label": "YouTube'i tellijad",
        "title": "Osta päris YouTube'i tellijaid, kes vaatavad | Growsterr",
        "description": "Osta YouTube'i tellijaid, kes on päris inimesed: vaatajad, kes leidsid su kanali ja otsustasid tellida, koos meeldimiste ja kommentaaridega. Alates {from_price}.",
        "h1": ("YouTube'i tellijad, ", "kes päriselt vaatavad."),
        "intro": "Osta YouTube'i tellijaid ausal viisil: päris inimesed avastavad sinu kanali, vaatavad sinu videoid ja tellivad selle, kui nähtu neile meeldib. Paketiga {starter_name} tavaliselt {starter_audience} uut tellijat kuus, koos meeldimiste ja kommentaaridega samadelt vaatajatelt.",
        "hero": {"image": "youtube-subscribers", "alt": "YouTube'i kanali leht päris vaatajatelt saabunud uute tellijatega"},
        "sections": [
            {
                "h2": "Tellija peaks olema vaataja",
                "p": [
                    "YouTube'is on tellijast kasu ainult siis, kui ta vaatab. Päris tellijad näevad sinu järgmist videot, vaatavad seda, annavad meeldimise ja vahel kommenteerivad, ja just seda vaatab YouTube, kui otsustab, mida soovitada.",
                    "Botitellijad ei vaata kunagi. Need muudavad kanali suuremaks, samal ajal kui selle videod jõuavad vähemate inimesteni.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Päris vaatajad tellivad YouTube'i kanali pärast video vaatamist"},
            },
            {
                "h2": "Milline näeb välja üks kuu",
                "ul": [
                    "Esimesed päevad: kampaania algab ja saabuvad esimesed vaatajad.",
                    "Iga nädal: uued tellijad, meeldimised ja kommentaarid, iga päev natuke.",
                    "Kuu lõpuks: paketiga {pick_name} tavaliselt {pick_audience} uut tellijat.",
                ],
            },
            {
                "h2": "Kust sinu vaatajad tulevad",
                "p": [
                    "Ütle meile linn, piirkond või riik, kust sinu publik peaks tulema. Näitame sinu kanalit kõigepealt sealsetele päris inimestele; kui kõige paremini sobiv publik on lähedal suurem, võib osa neist tulla sealt.",
                ],
            },
        ],
        "faqs": [
            ("Kui kiiresti tellijad tulevad?", "Natuke iga päev, terve kuu jooksul. Mitte kunagi kõik korraga: päris inimesed tellivad omas tempos."),
            ("Kas nad vaatavad minu videoid?", "Nad on päris inimesed, kes otsustasid sinu kanali tellida pärast seda, kui olid seda näinud. Mida nad edasi vaatavad, on nende enda otsus, nagu iga publiku puhul, ja just seepärast see loebki."),
            ("Kas saan ka meeldimisi ja kommentaare?", "Jah, samadelt vaatajatelt: paketiga {pick_name} tavaliselt {pick_likes} meeldimist ja {pick_comments} kommentaari kuus."),
            ("Kas te vajate minu parooli?", "Mitte kunagi. Vajame ainult sinu kanali käepidet ja kanal peaks olema avalik."),
        ],
    },
]
