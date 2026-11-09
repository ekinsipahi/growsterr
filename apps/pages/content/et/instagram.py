"""Estonian Instagram pages: the hub, followers, and the 1,000-followers goal.
Keys and placeholders: docs/CONTENT.md. Numbers come from the packages ({starter_audience}...)."""

UPDATED = "2026-11-08"

PAGES = [
    {
        # The hub: no service.
        "slug": "instagram",
        "label": "Instagram",
        "title": "Instagrami kasvupaketid sisuloojatele | Growsterr",
        "description": "Kasva Instagramis päris inimestega: kuupaketid toovad uusi jälgijaid, meeldimisi ja kommentaare neilt, kes otsustasid sind jälgida. Alates {from_price} kuus.",
        "h1": ("Kasva Instagramis ", "päris inimestega."),
        "intro": "Tahad osta Instagrami jälgijaid, meeldimisi või kommentaare? Siin on aus variant: kuupõhised kasvupaketid sisuloojatele ja suunamudijatele. Viime sinu profiili päris inimeste ette ja need, kellele nähtu meeldib, hakkavad sind jälgima, annavad meeldimisi ja kommenteerivad. Töölaud näitab päev-päevalt, mida me mõõtsime.",
        "hero": {"image": "instagram-hub", "alt": "Instagrami sisulooja profiil, kuhu saabuvad uued jälgijad, meeldimised ja kommentaarid"},
        "sections": [
            {
                "h2": "Kasv, mis näeb välja ausalt teenitud",
                "p": [
                    "Instagram eelistab kontosid, millega inimesed päriselt suhtlevad. Botid teevad vastupidist: nad istuvad sinu jälgijate arvus, ei anna kunagi meeldimist ega vaata midagi ning õpetavad algoritmile, et sinu postitusi pole mõtet näidata.",
                    "Meie teeme vastupidi. Sinu profiili näidatakse iga päev päris inimestele ja iga jälgimine on kellegi enda valik. Seepärast saabuvad meeldimised, vaatamised ja kommentaarid koos jälgijatega, mitte eraldi ostuna.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Päris inimesed avastavad sisulooja Instagrami postitusi ja jätavad kommentaare"},
            },
            {
                "h2": "Sisuloojatele, kes postitavad sihikindlalt",
                "p": [
                    "Isiklik bränd, nišileht või väikeettevõte: paketid kasvavad koos sinuga. Alusta paketiga {starter_name} ja liigu edasi, kui sinu sisu on valmis rohkemaks.",
                ],
                "ul": [
                    "Kasu saavad nii Reelsid, karussellid kui ka fotopostitused.",
                    "Sina ütled, millisest linnast, piirkonnast või riigist sinu publik peaks tulema.",
                    "Konto jääb sinu omaks: me ei küsi kunagi sinu parooli.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "Sisulooja planeerib laua taga Instagrami sisu"},
            },
        ],
        "faqs": [
            ("Kas jälgijad on päris inimesed?", "Jah. Iga jälgija on päris inimene, kes nägi sinu profiili ja otsustas sind jälgida. Me ei kasuta kunagi botte, võltsprofiile ega silmapilkset kohaletoimetamist."),
            ("Mitu jälgijat pakett toob?", "Paketiga {starter_name} tavaliselt {starter_audience} uut jälgijat kuus, paketiga {rising_name} {rising_audience} ja paketiga {pro_name} {pro_audience}. Need on tüüpilised vahemikud, mitte kindel arv: päris inimesed otsustavad ise."),
            ("Kas te vajate minu Instagrami parooli?", "Mitte kunagi. Vajame ainult sinu kasutajanime. Hoia konto avalikuna, et inimesed, kes selle avastavad, saaksid sind jälgida."),
            ("Kas meeldimisi või kommentaare saab osta eraldi?", "Ei. Meeldimised, vaatamised ja kommentaarid tulevad iga paketi sees, samadelt päris inimestelt, kes sind jälgivad. Just see hoiab sinu numbrid loomulikud."),
            ("Kas saan igal ajal tühistada?", "Jah. Paketid uuenevad kord kuus ja tühistada saad oma kontol. Juba makstud kuu kestab lõpuni."),
        ],
    },
    {
        "service": "followers",
        "slug": "instagram/jalgijad",
        "label": "Instagrami jälgijad",
        "title": "Osta päris Instagrami jälgijaid, iga kuu | Growsterr",
        "description": "Osta Instagrami jälgijaid, kes on päris inimesed ja otsustasid ise sind jälgida, koos meeldimiste ja kommentaaridega. Kuupaketid alates {from_price}.",
        "h1": ("Instagrami jälgijad, ", "kes otsustasid sind jälgida."),
        "intro": "Osta Instagrami jälgijaid ausal viisil: päris inimesed avastavad iga päev sinu profiili ja need, kellele nähtu meeldib, hakkavad sind jälgima. Paketiga {starter_name} tavaliselt {starter_audience} uut jälgijat kuus, koos meeldimiste ja kommentaaridega samadelt inimestelt.",
        "hero": {"image": "instagram-followers", "alt": "Instagrami profiil, mis saab päris inimestelt uusi jälgijaid"},
        "sections": [
            {
                "h2": "Miks päris jälgijad on rohkem väärt",
                "p": [
                    "Jälgija loeb ainult siis, kui tema taga on inimene. Päris jälgijad näevad sinu järgmist postitust, annavad sellele meeldimise, kommenteerivad ja jagavad seda, ja just seda kaasatust vaatab Instagram, kui otsustab, kellele veel sinu sisu näidata.",
                    "Botid ei suuda midagi sellest. Nad tõstavad numbrit paariks päevaks, kaovad järgmise puhastusega ja need, kes jäävad, vähendavad vaikselt sinu postituste levikut.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Päris inimesed annavad sisulooja Instagrami postitusele meeldimisi ja kommentaare"},
            },
            {
                "h2": "Kust sinu uued jälgijad tulevad",
                "p": [
                    "Ütle meile linn, piirkond või riik, kust sinu publik peaks tulema. Näitame sinu profiili kõigepealt sealsetele päris inimestele; kui kõige paremini sobiv publik on lähedal suurem, võib osa jälgijaid tulla sealt.",
                ],
            },
            {
                "h2": "Milline näeb välja üks kuu",
                "ul": [
                    "Esimesed päevad: kampaania algab ja saabuvad esimesed külastused.",
                    "Iga nädal: uued jälgijad, meeldimised ja kommentaarid, iga päev natuke.",
                    "Kuu lõpuks: paketiga {pick_name} tavaliselt {pick_audience} uut jälgijat.",
                ],
            },
        ],
        "faqs": [
            ("Kui kiiresti jälgijad tulevad?", "Natuke iga päev, terve kuu jooksul. Mitte kunagi kõik korraga: päris inimesed hakkavad jälgima omas tempos ja kõik, mis saabub silmapilkselt, on bot."),
            ("Kas uued jälgijad võivad jälgimise lõpetada?", "Mõned võivad, nii nagu iga päris publik aja jooksul muutub. Päris jälgijad jäävad palju sagedamini kui botid, kes kaovad lainetena."),
            ("Kas saan ka meeldimisi ja kommentaare?", "Jah, samadelt inimestelt: paketiga {pick_name} tavaliselt {pick_likes} meeldimist ja {pick_comments} kommentaari kuus."),
            ("Kas see on minu kontole ohutu?", "Me ei küsi kunagi sinu parooli ega logi sinu kontole sisse. Inimesed leiavad sinu profiili ja otsustavad ise, täpselt nagu iga teinegi jälgija sinuni jõuab."),
            ("Kas saan valida, kust mu jälgijad pärit on?", "Jah. Tellimisel ütle linn, piirkond või riik. Sihime kõigepealt sinna; kui sarnane publik on lähedal suurem, võib osa jälgijaid tulla sealt."),
        ],
    },
    {
        "service": "followers",
        "quantity": 1000,
        "slug": "instagram/jalgijad/1000",
        "label": "{quantity} Instagrami jälgijat",
        "title": "{quantity} Instagrami jälgijat päris inimestelt | Growsterr",
        "description": "Jõua {quantity} Instagrami jälgijani päris inimestega, mitte bottidega. {pick_name} toob tavaliselt {pick_audience} jälgijat kuus, lisaks meeldimisi ja kommentaare.",
        "h1": ("{quantity} Instagrami jälgijat, ", "igaüks neist päris."),
        "intro": "Me ei müü pakki, milles on {quantity} botti. Kasvatame sinu kontot päris inimestega: pakett {pick_name} toob tavaliselt {pick_audience} uut jälgijat kuus, nii et {quantity} on enamasti käeulatuses juba esimesel kuul.",
        "hero": {"image": "instagram-followers-1000", "alt": "Tõusev joon uutest Instagrami jälgijatest, mis jõuab esimese verstapostini"},
        "sections": [
            {
                "h2": "Miks mitte {quantity} jälgijat tunniga?",
                "p": [
                    "Sest ükski päris inimene ei hakka kontot jälgima paar sekundit pärast makset. Teenused, mis toovad {quantity} jälgijat tunniga, toovad botte: need ei anna meeldimisi, ei kommenteeri ja kaovad lainetena.",
                    "Need, kes jäävad, teevad veel rohkem kahju. Iga jälgija, kes kunagi ei reageeri, vähendab sinu publiku aktiivset osa ja sinu postitused jõuavad vaikselt vähemate inimesteni.",
                ],
            },
            {
                "h2": "Sinu esimene tuhat, korralikult tehtud",
                "p": [
                    "Esimene tuhat päris jälgijat muudab seda, kuidas uued külastajad sind näevad. Need on inimesed, kes võivad vaadata sinu Reelse, anda postitustele meeldimisi ja tagasi tulla, ja just see aitab järgmisel tuhandel sind leida.",
                ],
                "ul": [
                    "Päris inimesed, kes otsustasid sind jälgida, sinu valitud asukohast.",
                    "Meeldimised ja kommentaarid samadelt inimestelt, paketi sees.",
                    "Töölaud, mis näitab päev-päevalt, mida me mõõtsime.",
                ],
            },
        ],
        "faqs": [
            ("Kui kaua kulub {quantity} päris jälgija kogumiseks?", "Tüüpilises tempos toob pakett {pick_name} {pick_audience} uut jälgijat kuus, nii et {quantity} on enamasti käeulatuses juba esimesel kuul. Päris inimesed hakkavad jälgima omas tempos, seega on iga kuu veidi erinev."),
            ("Kas see on ühekordne pakk, kus on {quantity} jälgijat?", "Ei. Müüme kasvu kuupakettidena. {pick_name} maksab {pick_price} kuus ja tühistada saad igal ajal oma kontol."),
            ("Kas saan nendega koos ka meeldimisi ja kommentaare?", "Jah, samadelt päris inimestelt: paketiga {pick_name} tavaliselt {pick_likes} meeldimist ja {pick_comments} kommentaari kuus."),
            ("Mis saab siis, kui {quantity} on täis?", "Pakett jätkub, kuni sa selle tühistad, nii et kasv jätkub kuust kuusse. Kui sinu sisu on valmis rohkemaks, saad minna üle suuremale paketile."),
        ],
    },
]
