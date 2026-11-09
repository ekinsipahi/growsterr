"""Bosnian Instagram pages: the hub, followers, and the 1,000-followers goal.
Keys and placeholders: docs/CONTENT.md. Numbers come from the packages ({starter_audience}...),
so they follow apps/growth/plan.py when prices or ranges change."""

UPDATED = "2026-11-08"

PAGES = [
    {
        # The hub: no service.
        "slug": "instagram",
        "label": "Instagram",
        "title": "Paketi za rast na Instagramu za kreatore | Growsterr",
        "description": "Rastite na Instagramu uz stvarne ljude: mjesečni paketi donose nove pratioce, lajkove i komentare od ljudi koji su vas sami zapratili. Od {from_price} mjesečno.",
        "h1": ("Razvijte svoj Instagram ", "uz stvarne ljude."),
        "intro": "Mjesečni paketi rasta za kreatore i influencere. Vaš profil prikazujemo stvarnim ljudima, a oni kojima se svidi ono što vide zaprate vas, lajkuju i komentarišu. Kontrolna ploča pokazuje šta smo izmjerili, dan po dan.",
        "hero": {"image": "instagram-hub", "alt": "Instagram profil kreatora na koji stižu novi pratioci, lajkovi i komentari"},
        "sections": [
            {
                "h2": "Rast koji izgleda zasluženo",
                "p": [
                    "Instagram nagrađuje profile s kojima ljudi zaista komuniciraju. Botovi rade suprotno: sjede u broju vaših pratilaca, nikad ne lajkuju, nikad ne gledaju i uče algoritam da vaše objave ne vrijedi prikazivati.",
                    "Mi radimo obrnuto. Vaš profil se svaki dan prikazuje stvarnim ljudima, a svako praćenje je nečija odluka. Zato lajkovi, pregledi i komentari stižu zajedno s pratiocima, a ne kao posebna kupovina.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Stvarni ljudi otkrivaju Instagram objave kreatora i ostavljaju komentare"},
            },
            {
                "h2": "Za kreatore koji objavljuju s namjerom",
                "p": [
                    "Lični brend, nišna stranica ili mali biznis: paketi rastu s vama. Počnite s paketom {starter_name} i pređite na veći kada vaš sadržaj bude spreman za više.",
                ],
                "ul": [
                    "Korist imaju i Reels videi, i karuseli, i fotografije.",
                    "Vi nam kažete grad, regiju ili državu iz koje treba doći vaša publika.",
                    "Vaš profil ostaje vaš: nikada ne tražimo vašu lozinku.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "Kreator za radnim stolom planira sadržaj za Instagram"},
            },
        ],
        "faqs": [
            ("Da li su pratioci stvarni ljudi?", "Da. Svaki pratilac je stvarna osoba koja je vidjela vaš profil i odlučila da vas prati. Nikada ne koristimo botove, lažne profile ni instant isporuku."),
            ("Koliko pratilaca donosi jedan paket?", "Obično {starter_audience} novih pratilaca mjesečno uz {starter_name}, {rising_audience} uz {rising_name} i {pro_audience} uz {pro_name}. To su tipični rasponi, a ne fiksna količina: stvarni ljudi odlučuju sami."),
            ("Da li vam treba moja lozinka za Instagram?", "Nikada. Treba nam samo vaše korisničko ime. Neka vaš profil bude javan kako bi vas ljudi koji ga otkriju mogli zapratiti."),
            ("Mogu li kupiti samo lajkove ili komentare?", "Ne. Lajkovi, pregledi i komentari dolaze u svakom paketu, od istih stvarnih ljudi koji vas prate. Upravo zato vaši brojevi ostaju prirodni."),
            ("Mogu li otkazati u bilo kojem trenutku?", "Da. Paketi se obnavljaju mjesečno i možete ih otkazati na svom računu. Mjesec koji ste platili traje do kraja."),
        ],
    },
    {
        "service": "followers",
        "slug": "instagram/pratioci",
        "label": "Instagram pratioci",
        "title": "Stvarni Instagram pratioci, svakog mjeseca | Growsterr",
        "description": "Instagram pratioci koji su stvarni ljudi i koji su vas sami odlučili pratiti, uz lajkove i komentare od istih ljudi. Mjesečni paketi od {from_price}.",
        "h1": ("Instagram pratioci ", "koji su vas odlučili pratiti."),
        "intro": "Stvarni ljudi svaki dan otkrivaju vaš profil, a oni kojima se svidi ono što vide zaprate vas. Obično {starter_audience} novih pratilaca mjesečno uz {starter_name}, uz lajkove i komentare od istih ljudi.",
        "hero": {"image": "instagram-followers", "alt": "Instagram profil koji dobija nove pratioce od stvarnih ljudi"},
        "sections": [
            {
                "h2": "Zašto stvarni pratioci vrijede više",
                "p": [
                    "Pratilac se računa samo ako iza njega stoji osoba. Stvarni pratioci vide vašu sljedeću objavu, lajkuju je, komentarišu i dijele, a upravo taj angažman Instagram gleda kada odlučuje kome još da prikaže vaš sadržaj.",
                    "Botovi ništa od toga ne mogu. Podignu broj na nekoliko dana, nestanu pri sljedećem čišćenju, a oni koji ostanu tiho smanjuju vaš doseg.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Stvarni ljudi lajkuju i komentarišu Instagram objavu kreatora"},
            },
            {
                "h2": "Odakle dolaze vaši novi pratioci",
                "p": [
                    "Recite nam grad, regiju ili državu iz koje treba doći vaša publika. Vaš profil prvo prikazujemo stvarnim ljudima odatle; tamo gdje je publika koja vam najbolje odgovara veća, više njih može doći iz okoline.",
                ],
            },
            {
                "h2": "Kako izgleda jedan mjesec",
                "ul": [
                    "Prvi dani: vaša kampanja počinje i stižu prve posjete.",
                    "Svake sedmice: novi pratioci, lajkovi i komentari, po nekoliko svaki dan.",
                    "Do kraja mjeseca: obično {pick_audience} novih pratilaca uz {pick_name}.",
                ],
            },
        ],
        "faqs": [
            ("Koliko brzo stižu pratioci?", "Pomalo svaki dan, tokom cijelog mjeseca. Nikada sve odjednom: stvarni ljudi prate svojim tempom, a sve što stigne instant je bot."),
            ("Hoće li me novi pratioci otpratiti?", "Neki možda hoće, kao što se mijenja svaka stvarna publika. Stvarni pratioci ostaju mnogo češće od botova, koji nestaju u talasima."),
            ("Dobijam li i lajkove i komentare?", "Da, od istih ljudi: obično {pick_likes} lajkova i {pick_comments} komentara mjesečno uz {pick_name}."),
            ("Da li je to sigurno za moj profil?", "Nikada ne tražimo vašu lozinku i nikada se ne prijavljujemo na vaš profil. Ljudi sami pronađu vaš profil i sami odluče, kao što vas pronađe bilo koji pratilac."),
            ("Mogu li odabrati odakle su moji pratioci?", "Da. Pri narudžbi nam navedite grad, regiju ili državu. Prvo ciljamo tamo; kada je u blizini veća publika koja vam dobro odgovara, dio pratilaca može doći i odatle."),
        ],
    },
    {
        "service": "followers",
        "quantity": 1000,
        "slug": "instagram/pratioci/1000",
        "label": "{quantity} Instagram pratilaca",
        "title": "{quantity} Instagram pratilaca od stvarnih ljudi | Growsterr",
        "description": "Dođite do {quantity} pratilaca na Instagramu uz stvarne ljude, ne botove. {pick_name} obično donosi {pick_audience} mjesečno, uz lajkove i komentare.",
        "h1": ("{quantity} Instagram pratilaca, ", "i svaki je stvaran."),
        "intro": "Ne prodajemo paket od {quantity} botova. Vaš profil razvijamo uz stvarne ljude: {pick_name} obično donosi {pick_audience} novih pratilaca mjesečno, pa je {quantity} najčešće dostižno već u prvom mjesecu.",
        "hero": {"image": "instagram-followers-1000", "alt": "Rastuća linija novih Instagram pratilaca koja dostiže prvi cilj"},
        "sections": [
            {
                "h2": "Zašto ne {quantity} pratilaca za sat vremena?",
                "p": [
                    "Zato što nijedna stvarna osoba ne zaprati profil nekoliko sekundi nakon uplate. Usluge koje isporuče {quantity} pratilaca za sat vremena isporučuju botove: ne lajkuju, ne komentarišu i nestaju u talasima.",
                    "Oni koji ostanu prave još veću štetu. Svaki pratilac koji nikad ne reaguje smanjuje udio publike koja reaguje, pa vaše objave tiho dopiru do manje ljudi.",
                ],
            },
            {
                "h2": "Vaših prvih hiljadu, kako treba",
                "p": [
                    "Prvih hiljadu stvarnih pratilaca mijenja to kako vas novi posjetioci vide. To su ljudi koji bi mogli gledati vaše Reels videe, lajkovati objave i vraćati se, a upravo to pomaže da vas pronađe sljedećih hiljadu.",
                ],
                "ul": [
                    "Stvarni ljudi koji su vas odlučili pratiti, s lokacije koju odaberete.",
                    "Lajkovi i komentari od istih ljudi, u okviru paketa.",
                    "Kontrolna ploča koja dan po dan pokazuje šta smo izmjerili.",
                ],
            },
        ],
        "faqs": [
            ("Koliko traje put do {quantity} stvarnih pratilaca?", "Uobičajenim tempom {pick_name} donosi {pick_audience} novih pratilaca mjesečno, pa je {quantity} najčešće dostižno već u prvom mjesecu. Stvarni ljudi prate svojim tempom, pa je svaki mjesec malo drugačiji."),
            ("Da li je to jednokratni paket od {quantity}?", "Ne. Rast prodajemo kao mjesečne pakete. {pick_name} košta {pick_price} mjesečno, a otkazati možete u bilo kojem trenutku na svom računu."),
            ("Dobijam li uz njih lajkove i komentare?", "Da, od istih stvarnih ljudi: obično {pick_likes} lajkova i {pick_comments} komentara mjesečno uz {pick_name}."),
            ("Šta se dešava nakon {quantity}?", "Vaš paket traje dok ga ne otkažete, pa se rast nastavlja iz mjeseca u mjesec. Kada vaš sadržaj bude spreman za više, možete preći na veći paket."),
        ],
    },
]
