"""Estonian TikTok pages: the hub and likes. Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "tiktok",
        "label": "TikTok",
        "title": "TikToki kasvupaketid sisuloojatele | Growsterr",
        "description": "Kasva TikTokis päris inimestega: kuupaketid toovad uusi jälgijaid, meeldimisi ja kommentaare neilt, kes otsustasid sind jälgida. Alates {from_price} kuus.",
        "h1": ("Kasva TikTokis ", "päris inimestega."),
        "intro": "Tahad osta TikToki jälgijaid, meeldimisi või vaatamisi? Bottide asemel pakume hoopis seda: kuupõhised kasvupaketid sisuloojatele ja suunamudijatele. Päris inimesed avastavad sinu profiili, vaatavad sinu videoid ja hakkavad sind jälgima, kui nähtu neile meeldib. Töölaud näitab päev-päevalt, mida me mõõtsime.",
        "hero": {"image": "tiktok-hub", "alt": "TikToki sisulooja profiil, kuhu saabuvad uued jälgijad ja meeldimised"},
        "sections": [
            {
                "h2": "TikTokis on tähelepanu kõik",
                "p": [
                    "TikTok näitab videot rohkematele inimestele, kui selle esimesed vaatajad vaatavad, annavad meeldimisi, kommenteerivad ja hakkavad jälgima. Numbrid, mille taga pole inimesi, ei liiguta sellest midagi.",
                    "Meie paketid toovad iga päev sinu profiilile päris inimesi. Nad vaatavad, otsustavad ja need, kellele sinu videod meeldivad, hakkavad jälgima ja annavad meeldimisi. Just selline tähelepanu aitab videol levida.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Päris vaatajad vaatavad sisulooja TikToki videoid"},
            },
            {
                "h2": "Sisuloojatele, kellel on midagi öelda",
                "p": [
                    "Komöödia, toiduvalmistamine, mood või õpetused: kui postitad regulaarselt, annavad päris vaatajad igale uuele videole parema alguse. Alusta paketiga {starter_name} ja liigu edasi, kui oled valmis.",
                ],
                "ul": [
                    "Sina ütled, millisest linnast, piirkonnast või riigist sinu publik peaks tulema.",
                    "Jälgijad, meeldimised ja kommentaarid tulevad koos, samadelt inimestelt.",
                    "Konto jääb sinu omaks: me ei küsi kunagi sinu parooli.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Sisulooja filmib statiivil oleva telefoniga TikToki videot"},
            },
        ],
        "faqs": [
            ("Kas jälgijad on päris inimesed?", "Jah. Iga jälgija on päris inimene, kes nägi sinu profiili ja otsustas sind jälgida. Me ei kasuta kunagi botte, võltskontosid ega silmapilkset kohaletoimetamist."),
            ("Mitu jälgijat pakett toob?", "Paketiga {starter_name} tavaliselt {starter_audience} uut jälgijat kuus, paketiga {rising_name} {rising_audience} ja paketiga {pro_name} {pro_audience}. Tüüpilised vahemikud, mitte kindel arv: päris inimesed otsustavad ise."),
            ("Kas te vajate minu TikToki parooli?", "Mitte kunagi. Vajame ainult sinu kasutajanime. Hoia konto avalikuna, et inimesed, kes selle avastavad, saaksid sind jälgida."),
            ("Kas vaatamisi või meeldimisi saab osta eraldi?", "Ei. Vaatamised, meeldimised ja kommentaarid tulevad iga paketi sees, samadelt päris inimestelt, kes sind jälgivad."),
            ("Kas saan igal ajal tühistada?", "Jah. Paketid uuenevad kord kuus ja tühistada saad oma kontol. Juba makstud kuu kestab lõpuni."),
        ],
    },
    {
        "service": "likes",
        "slug": "tiktok/meeldimised",
        "label": "TikToki meeldimised",
        "title": "Osta TikToki meeldimisi päris inimestelt | Growsterr",
        "description": "TikToki meeldimised päris inimestelt, kes vaatavad sinu videoid. Need tulevad iga kuupaketi sees koos jälgijate ja kommentaaridega. Alates {from_price} kuus.",
        "h1": ("TikToki meeldimised päris inimestelt. ", "Iga paketi sees."),
        "intro": "Mõtled TikToki meeldimiste ostmisele? Me ei müü neid eraldi. Iga pakett toob päris inimesi, kes avastavad sinu profiili, vaatavad sinu videoid ja annavad meeldimise sellele, mis neile meeldib: paketiga {starter_name} tavaliselt {starter_likes} meeldimist kuus.",
        "hero": {"image": "tiktok-likes", "alt": "Päris vaatajate meeldimised tõusevad TikToki videost"},
        "sections": [
            {
                "h2": "Miks meeldimine loeb ainult siis, kui selle taga on inimene",
                "p": [
                    "TikTok jälgib, mis toimub meeldimise ümber: kas vaataja vaatas edasi, hakkas jälgima, tuli tagasi? Bottide meeldimised vastavad kõigele eitavalt, nii et need lisavad numbri ja võtavad levikut ära.",
                    "Päris inimeste meeldimised tulevad koos kõige muuga: vaatamisaja, jälgimiste ja kommentaaridega. See on signaal, mis aitab videol levida.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Vaatajad vaatavad TikToki video lõpuni ja annavad sellele meeldimise"},
            },
            {
                "h2": "Mitu meeldimist iga pakett toob",
                "ul": [
                    "{starter_name} ({starter_price} kuus): tavaliselt {starter_likes} meeldimist.",
                    "{rising_name} ({rising_price} kuus): tavaliselt {rising_likes} meeldimist, sinu valitud videotele.",
                    "{pro_name} ({pro_price} kuus): tavaliselt {pro_likes} meeldimist, eelisjärjekorras.",
                ],
            },
            {
                "h2": "Miks me ei müü meeldimisi eraldi",
                "p": [
                    "Meeldimised, mis saabuvad ilma vaatamiste, jälgimiste või kommentaarideta, paistavad täpselt sellena, mis need on. Paketi sees tuleb iga meeldimine kelleltki, kes vaatas, nii et sinu numbrid liiguvad koos, nagu päris kasvu puhul.",
                ],
            },
        ],
        "faqs": [
            ("Kas TikToki meeldimisi saab ilma paketita?", "Ei. Meeldimised, vaatamised ja kommentaarid tulevad ainult meie kuupakettide sees, samadelt päris inimestelt. Just see hoiab need loomulikud."),
            ("Millised videod meeldimised saavad?", "Päris inimesed annavad meeldimise sellele, mis neile meeldib, tavaliselt sinu uusimatele videotele. Pakettidega {rising_name} ja {pro_name} saad ise valida, millised videod tähelepanu saavad."),
            ("Kui kiiresti meeldimised tulevad?", "Natuke iga päev, terve kuu jooksul. Mitte kunagi silmapilkselt: silmapilkne meeldimine on bot."),
            ("Kas te vajate minu TikToki parooli?", "Mitte kunagi. Vajame ainult sinu kasutajanime ja konto peaks olema avalik."),
        ],
    },
]
