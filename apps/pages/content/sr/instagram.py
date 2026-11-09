"""Serbian (Latin script) Instagram pages: the hub, followers, and the 1,000-followers goal.
Keys and placeholders: docs/CONTENT.md. Numbers come from the packages ({starter_audience}...),
so they follow apps/growth/plan.py when prices or ranges change."""

UPDATED = "2026-11-08"

PAGES = [
    {
        # The hub: no service.
        "slug": "instagram",
        "label": "Instagram",
        "title": "Paketi za rast na Instagramu za kreatore | Growsterr",
        "description": "Rastite na Instagramu uz prave ljude: mesečni paketi donose nove pratioce, lajkove i komentare od ljudi koji su vas sami zapratili. Od {from_price} mesečno.",
        "h1": ("Rastite na Instagramu ", "uz prave ljude."),
        "intro": "Mesečni paketi za rast, namenjeni kreatorima i influenserima. Vaš profil prikazujemo pravim ljudima, a oni kojima se dopadne ono što vide zaprate vas, lajkuju i komentarišu. Kontrolna tabla pokazuje šta smo izmerili, dan po dan.",
        "hero": {"image": "instagram-hub", "alt": "Instagram profil kreatora na koji stižu novi pratioci, lajkovi i komentari"},
        "sections": [
            {
                "h2": "Rast koji izgleda kao da ste ga zaslužili",
                "p": [
                    "Instagram nagrađuje naloge sa kojima ljudi zaista komuniciraju. Botovi rade suprotno: samo stoje u broju pratilaca, nikada ne lajkuju, nikada ne gledaju i uče algoritam da vaše objave ne vredi prikazivati.",
                    "Mi radimo obrnuto. Vaš profil se svakog dana prikazuje pravim ljudima i svako praćenje je nečija odluka. Zato lajkovi, pregledi i komentari stižu zajedno sa pratiocima, a ne kao zasebna kupovina.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Pravi ljudi otkrivaju Instagram objave kreatora i ostavljaju komentare"},
            },
            {
                "h2": "Za kreatore koji objavljuju sa namerom",
                "p": [
                    "Lični brend, nišna stranica ili mali biznis: paketi rastu zajedno sa vama. Počnite sa paketom {starter_name} i pređite na veći kada vaš sadržaj bude spreman za više.",
                ],
                "ul": [
                    "Koristi imaju i Reels snimci, i karuseli, i fotografije.",
                    "Vi nam kažete grad, region ili zemlju iz koje treba da dolazi vaša publika.",
                    "Nalog ostaje vaš: nikada ne tražimo vašu lozinku.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "Kreator za stolom planira sadržaj za Instagram"},
            },
        ],
        "faqs": [
            ("Da li su pratioci pravi ljudi?", "Da. Svaki pratilac je prava osoba koja je videla vaš profil i odlučila da vas prati. Nikada ne koristimo botove, lažne profile niti isporuku „odmah”."),
            ("Koliko pratilaca donosi jedan paket?", "Obično {starter_audience} novih pratilaca mesečno uz {starter_name}, {rising_audience} uz {rising_name} i {pro_audience} uz {pro_name}. To su tipični rasponi, a ne fiksan broj: pravi ljudi odlučuju sami."),
            ("Da li vam treba moja lozinka za Instagram?", "Nikada. Potrebno nam je samo vaše korisničko ime. Neka nalog bude javan, kako bi ljudi koji ga otkriju mogli da vas zaprate."),
            ("Mogu li da kupim samo lajkove ili komentare?", "Ne. Lajkovi, pregledi i komentari dolaze u okviru svakog paketa, od istih pravih ljudi koji vas prate. Upravo zato vaše brojke ostaju prirodne."),
            ("Mogu li da otkažem bilo kada?", "Da. Paketi se obnavljaju mesečno, a otkazati možete iz svog naloga. Plaćeni mesec traje do kraja."),
        ],
    },
    {
        "service": "followers",
        "slug": "instagram/pratioci",
        "label": "Instagram pratioci",
        "title": "Pravi pratioci na Instagramu, svakog meseca | Growsterr",
        "description": "Pratioci na Instagramu koji su pravi ljudi i sami su odlučili da vas prate, uz lajkove i komentare od istih ljudi. Mesečni paketi od {from_price}.",
        "h1": ("Pratioci na Instagramu ", "koji su sami izabrali vas."),
        "intro": "Pravi ljudi svakog dana otkrivaju vaš profil, a oni kojima se dopadne ono što vide zaprate vas. Uz {starter_name} obično {starter_audience} novih pratilaca mesečno, uz lajkove i komentare od istih ljudi.",
        "hero": {"image": "instagram-followers", "alt": "Instagram profil na koji stižu novi pratioci, pravi ljudi"},
        "sections": [
            {
                "h2": "Zašto pravi pratioci vrede više",
                "p": [
                    "Pratilac se računa samo ako iza njega stoji osoba. Pravi pratioci vide vašu sledeću objavu, lajkuju je, komentarišu i dele, a upravo na to angažovanje Instagram gleda kada odlučuje kome još da prikaže vaš sadržaj.",
                    "Botovi ne mogu ništa od toga. Podignu broj na nekoliko dana, nestanu u sledećem čišćenju, a oni koji ostanu tiho smanjuju vaš doseg.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Pravi ljudi lajkuju i komentarišu objavu kreatora na Instagramu"},
            },
            {
                "h2": "Odakle dolaze vaši novi pratioci",
                "p": [
                    "Recite nam grad, region ili zemlju iz koje treba da dolazi vaša publika. Vaš profil prvo prikazujemo pravim ljudima tamo; gde je publika koja vam najviše odgovara veća, više njih može doći iz okoline.",
                ],
            },
            {
                "h2": "Kako izgleda jedan mesec",
                "ul": [
                    "Prvi dani: kampanja počinje i stižu prve posete.",
                    "Svake nedelje: novi pratioci, lajkovi i komentari, pomalo svakog dana.",
                    "Do kraja meseca: uz {pick_name} obično {pick_audience} novih pratilaca.",
                ],
            },
        ],
        "faqs": [
            ("Koliko brzo stižu pratioci?", "Pomalo svakog dana, tokom celog meseca. Nikada sve odjednom: pravi ljudi prate svojim tempom, a sve što stigne „odmah” su botovi."),
            ("Hoće li novi pratioci prestati da me prate?", "Neki možda hoće, kao što se menja svaka prava publika. Pravi pratioci ostaju mnogo češće od botova, koji nestaju u talasima."),
            ("Da li dobijam i lajkove i komentare?", "Da, od istih ljudi: uz {pick_name} obično {pick_likes} lajkova i {pick_comments} komentara mesečno."),
            ("Da li je to bezbedno za moj nalog?", "Nikada ne tražimo vašu lozinku i nikada se ne prijavljujemo na vaš nalog. Ljudi pronalaze vaš profil i sami odlučuju, kao što vas pronalazi svaki pratilac."),
            ("Mogu li da izaberem odakle su moji pratioci?", "Da. Prilikom naručivanja navedite grad, region ili zemlju. Ciljamo prvo tamo; kada je slična publika u okolini veća, deo pratilaca može doći i odande."),
        ],
    },
    {
        "service": "followers",
        "quantity": 1000,
        "slug": "instagram/pratioci/1000",
        "label": "{quantity} Instagram pratilaca",
        "title": "{quantity} pratilaca na Instagramu, pravi ljudi | Growsterr",
        "description": "Stignite do {quantity} pratilaca na Instagramu uz prave ljude, a ne botove. {pick_name} obično donosi {pick_audience} mesečno, uz lajkove i komentare.",
        "h1": ("{quantity} pratilaca na Instagramu, ", "svaki od njih pravi."),
        "intro": "Ne prodajemo paket od {quantity} botova. Vaš nalog razvijamo uz prave ljude: {pick_name} obično donosi {pick_audience} novih pratilaca mesečno, pa je {quantity} najčešće na dohvat ruke već u prvom mesecu.",
        "hero": {"image": "instagram-followers-1000", "alt": "Rastuća linija novih Instagram pratilaca koja stiže do prvog cilja"},
        "sections": [
            {
                "h2": "Zašto ne {quantity} pratilaca za sat vremena?",
                "p": [
                    "Zato što nijedna prava osoba ne zaprati nalog nekoliko sekundi posle uplate. Servisi koji isporuče {quantity} pratilaca za sat vremena isporučuju botove: ne lajkuju, ne komentarišu i nestaju u talasima.",
                    "Oni koji ostanu prave još veću štetu. Svaki pratilac koji nikada ne reaguje smanjuje udeo publike koja reaguje, a vaše objave tiho stižu do manje ljudi.",
                ],
            },
            {
                "h2": "Vaših prvih hiljadu, kako treba",
                "p": [
                    "Prvih hiljadu pravih pratilaca menja to kako vas vide novi posetioci. To su ljudi koji mogu da gledaju vaše Reels snimke, lajkuju objave i vraćaju se, a upravo to pomaže da vas pronađe sledećih hiljadu.",
                ],
                "ul": [
                    "Pravi ljudi koji su sami odlučili da vas prate, sa lokacije koju izaberete.",
                    "Lajkovi i komentari od istih ljudi, u okviru paketa.",
                    "Kontrolna tabla koja pokazuje šta smo izmerili, dan po dan.",
                ],
            },
        ],
        "faqs": [
            ("Koliko vremena treba za {quantity} pravih pratilaca?", "Uobičajenim tempom {pick_name} donosi {pick_audience} novih pratilaca mesečno, pa je {quantity} obično dostižno već u prvom mesecu. Pravi ljudi prate svojim tempom, pa je svaki mesec malo drugačiji."),
            ("Da li je to jednokratni paket od {quantity}?", "Ne. Rast prodajemo kao mesečne pakete. {pick_name} košta {pick_price} mesečno, a otkazati možete bilo kada iz svog naloga."),
            ("Da li uz njih dobijam lajkove i komentare?", "Da, od istih pravih ljudi: uz {pick_name} obično {pick_likes} lajkova i {pick_comments} komentara mesečno."),
            ("Šta se dešava posle {quantity}?", "Vaš paket radi dok ga ne otkažete, pa se rast nastavlja iz meseca u mesec. Kada vaš sadržaj bude spreman za više, možete preći na veći paket."),
        ],
    },
]
