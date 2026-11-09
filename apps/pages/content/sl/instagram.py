"""Slovenian Instagram pages: the hub, followers, and the 1,000-followers goal.
Keys and placeholders: docs/CONTENT.md. Numbers come from the packages ({starter_audience}...),
so they follow apps/growth/plan.py when prices or ranges change."""

UPDATED = "2026-11-08"

PAGES = [
    {
        # The hub: no service.
        "slug": "instagram",
        "label": "Instagram",
        "title": "Paketi za rast na Instagramu za ustvarjalce | Growsterr",
        "description": "Rastite na Instagramu z resničnimi ljudmi: mesečni paketi prinesejo nove sledilce, všečke in komentarje ljudi, ki so se odločili slediti. Od {from_price}/mesec.",
        "h1": ("Rastite na Instagramu ", "z resničnimi ljudmi."),
        "intro": "Mesečni paketi za rast za ustvarjalce in vplivneže. Vaš profil pokažemo resničnim ljudem, tisti, ki jim je všeč, kar vidijo, pa vam sledijo, všečkajo in komentirajo. Nadzorna plošča dan za dnem pokaže, kaj smo izmerili.",
        "hero": {"image": "instagram-hub", "alt": "Profil ustvarjalca na Instagramu, na katerega prihajajo novi sledilci, všečki in komentarji"},
        "sections": [
            {
                "h2": "Rast, ki je videti zaslužena",
                "p": [
                    "Instagram nagrajuje račune, s katerimi se ljudje res ukvarjajo. Boti naredijo ravno nasprotno: sedijo med vašimi sledilci, nikoli ne všečkajo, nikoli ne gledajo in algoritem naučijo, da vaših objav ni vredno prikazovati.",
                    "Mi delamo obratno. Vaš profil vsak dan pokažemo resničnim ljudem in vsako sledenje je nečija odločitev. Zato všečki, ogledi in komentarji pridejo skupaj s sledilci, ne kot ločen nakup.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Resnični ljudje odkrivajo objave ustvarjalca na Instagramu in puščajo komentarje"},
            },
            {
                "h2": "Za ustvarjalce, ki objavljajo z namenom",
                "p": [
                    "Osebna blagovna znamka, nišna stran ali manjše podjetje: paketi rastejo z vami. Začnite s paketom {starter_name} in preidite višje, ko je vaša vsebina pripravljena na več.",
                ],
                "ul": [
                    "Koristi imajo vse objave: Reels, vrtiljaki in fotografije.",
                    "Poveste nam mesto, regijo ali državo, iz katere naj prihaja vaše občinstvo.",
                    "Vaš račun ostane vaš: nikoli ne zahtevamo vašega gesla.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "Ustvarjalec za mizo načrtuje vsebino za Instagram"},
            },
        ],
        "faqs": [
            ("So sledilci resnični ljudje?", "Da. Vsak sledilec je resnična oseba, ki je videla vaš profil in se odločila, da vam bo sledila. Nikoli ne uporabljamo botov, lažnih profilov ali takojšnje dostave."),
            ("Koliko sledilcev prinese paket?", "Običajno {starter_audience} novih sledilcev na mesec s paketom {starter_name}, {rising_audience} s paketom {rising_name} in {pro_audience} s paketom {pro_name}. To so tipični razponi, ne fiksno število: resnični ljudje se odločajo sami."),
            ("Potrebujete moje geslo za Instagram?", "Nikoli. Potrebujemo le vaše uporabniško ime. Račun naj bo javen, da mu ljudje, ki ga odkrijejo, lahko sledijo."),
            ("Lahko kupim samo všečke ali komentarje?", "Ne. Všečki, ogledi in komentarji so vključeni v vsak paket in prihajajo od istih resničnih ljudi, ki vam sledijo. Tako vaše številke ostanejo naravne."),
            ("Lahko kadar koli prekličem?", "Da. Paketi se podaljšujejo mesečno, prekličete pa jih lahko v svojem računu. Plačani mesec teče do konca."),
        ],
    },
    {
        "service": "followers",
        "slug": "instagram/sledilci",
        "label": "Sledilci na Instagramu",
        "title": "Resnični sledilci na Instagramu, vsak mesec | Growsterr",
        "description": "Sledilci na Instagramu, ki so resnični ljudje in so se vam sami odločili slediti, z všečki in komentarji istih ljudi. Mesečni paketi od {from_price}.",
        "h1": ("Sledilci na Instagramu, ", "ki so se vam odločili slediti."),
        "intro": "Resnični ljudje vsak dan odkrivajo vaš profil, tisti, ki jim je všeč, kar vidijo, pa vam začnejo slediti. Običajno {starter_audience} novih sledilcev na mesec s paketom {starter_name}, z všečki in komentarji istih ljudi.",
        "hero": {"image": "instagram-followers", "alt": "Profil na Instagramu, ki pridobiva nove sledilce od resničnih ljudi"},
        "sections": [
            {
                "h2": "Zakaj so resnični sledilci vredni več",
                "p": [
                    "Sledilec šteje le, če je za njim človek. Resnični sledilci vidijo vašo naslednjo objavo, jo všečkajo, komentirajo in delijo, prav ta odziv pa Instagram upošteva, ko se odloča, komu še pokazati vašo vsebino.",
                    "Boti ne zmorejo ničesar od tega. Nekaj dni dvigujejo številko, izginejo ob naslednjem čiščenju, tisti, ki ostanejo, pa vam tiho znižujejo doseg.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Resnični ljudje všečkajo in komentirajo objavo ustvarjalca na Instagramu"},
            },
            {
                "h2": "Od kod pridejo vaši novi sledilci",
                "p": [
                    "Povejte nam mesto, regijo ali državo, iz katere naj prihaja vaše občinstvo. Vaš profil najprej pokažemo resničnim ljudem tam; kjer je najbolj ujemajoče se občinstvo večje, jih lahko več pride iz bližine.",
                ],
            },
            {
                "h2": "Kako je videti en mesec",
                "ul": [
                    "Prvi dnevi: kampanja se začne in pridejo prvi obiski.",
                    "Vsak teden: novi sledilci, všečki in komentarji, vsak dan nekaj.",
                    "Do konca meseca: običajno {pick_audience} novih sledilcev s paketom {pick_name}.",
                ],
            },
        ],
        "faqs": [
            ("Kako hitro pridejo sledilci?", "Vsak dan malo, skozi ves mesec. Nikoli vse naenkrat: resnični ljudje sledijo v svojem tempu, vse, kar pride takoj, pa je bot."),
            ("Mi bodo novi sledilci nehali slediti?", "Nekateri morda, tako kot se spreminja vsako resnično občinstvo. Resnični sledilci ostanejo veliko pogosteje kot boti, ki izginjajo v valovih."),
            ("Dobim tudi všečke in komentarje?", "Da, od istih ljudi: običajno {pick_likes} všečkov in {pick_comments} komentarjev na mesec s paketom {pick_name}."),
            ("Je to varno za moj račun?", "Nikoli ne zahtevamo vašega gesla in se nikoli ne prijavimo v vaš račun. Ljudje najdejo vaš profil in se odločijo sami, tako kot vas najde vsak sledilec."),
            ("Lahko izberem, od kod so moji sledilci?", "Da. Ob naročilu nam povejte mesto, regijo ali državo. Najprej ciljamo tja; kadar je v bližini večje, zelo podobno občinstvo, lahko nekaj sledilcev pride od tam."),
        ],
    },
    {
        "service": "followers",
        "quantity": 1000,
        "slug": "instagram/sledilci/1000",
        "label": "{quantity} sledilcev na Instagramu",
        "title": "{quantity} sledilcev na Instagramu od resničnih ljudi | Growsterr",
        "description": "Do {quantity} sledilcev na Instagramu z resničnimi ljudmi, ne z boti. {pick_name} običajno prinese {pick_audience} na mesec, skupaj z všečki in komentarji.",
        "h1": ("{quantity} sledilcev na Instagramu, ", "vsak od njih resničen."),
        "intro": "Ne prodajamo paketa {quantity} botov. Vaš račun gradimo z resničnimi ljudmi: {pick_name} običajno prinese {pick_audience} novih sledilcev na mesec, zato je cilj {quantity} običajno dosegljiv že v prvem mesecu.",
        "hero": {"image": "instagram-followers-1000", "alt": "Naraščajoča črta novih sledilcev na Instagramu, ki doseže prvi mejnik"},
        "sections": [
            {
                "h2": "Zakaj ne {quantity} sledilcev v eni uri?",
                "p": [
                    "Ker nobena resnična oseba ne začne slediti računu nekaj sekund po plačilu. Storitve, ki dostavijo {quantity} sledilcev v eni uri, dostavijo bote: ti ne všečkajo, ne komentirajo in izginjajo v valovih.",
                    "Tisti, ki ostanejo, naredijo še več škode. Vsak sledilec, ki se nikoli ne odzove, zniža delež vašega občinstva, ki se odziva, in vaše objave tiho dosežejo manj ljudi.",
                ],
            },
            {
                "h2": "Vaših prvih tisoč, kot je prav",
                "p": [
                    "Prvih tisoč resničnih sledilcev spremeni, kako vas vidijo novi obiskovalci. To so ljudje, ki si morda ogledajo vaše Reels, všečkajo vaše objave in se vračajo, prav to pa pomaga, da vas najde naslednjih tisoč.",
                ],
                "ul": [
                    "Resnični ljudje, ki so se odločili slediti, z lokacije, ki jo izberete.",
                    "Všečki in komentarji istih ljudi, vključeni v paket.",
                    "Nadzorna plošča, ki dan za dnem pokaže, kaj smo izmerili.",
                ],
            },
        ],
        "faqs": [
            ("V kolikšnem času pridem do {quantity} resničnih sledilcev?", "Ob tipičnem tempu {pick_name} prinese {pick_audience} novih sledilcev na mesec, zato je cilj {quantity} običajno dosegljiv že v prvem mesecu. Resnični ljudje sledijo v svojem tempu, zato je vsak mesec malo drugačen."),
            ("Je to enkratni paket {quantity} sledilcev?", "Ne. Rast prodajamo kot mesečne pakete. {pick_name} stane {pick_price} na mesec, prekličete pa ga lahko kadar koli v svojem računu."),
            ("Dobim z njimi tudi všečke in komentarje?", "Da, od istih resničnih ljudi: običajno {pick_likes} všečkov in {pick_comments} komentarjev na mesec s paketom {pick_name}."),
            ("Kaj sledi, ko dosežem {quantity}?", "Vaš paket teče, dokler ga ne prekličete, zato se rast nadaljuje iz meseca v mesec. Ko je vaša vsebina pripravljena na več, lahko preidete na večji paket."),
        ],
    },
]
