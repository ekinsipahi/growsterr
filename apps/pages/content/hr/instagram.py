"""Croatian Instagram pages: the hub, followers, and the 1,000-followers goal.
Keys and placeholders: docs/CONTENT.md. Numbers come from the packages ({starter_audience}...),
so they follow apps/growth/plan.py when prices or ranges change."""

UPDATED = "2026-11-08"

PAGES = [
    {
        # The hub: no service.
        "slug": "instagram",
        "label": "Instagram",
        "title": "Paketi rasta na Instagramu za kreatore | Growsterr",
        "description": "Rastite na Instagramu uz stvarne ljude: mjesečni paketi donose nove pratitelje, lajkove i komentare ljudi koji su vas odlučili pratiti. Od {from_price}.",
        "h1": ("Rastite na Instagramu ", "uz stvarne ljude."),
        "intro": "Mjesečni paketi rasta za kreatore i influencere. Vaš profil prikazujemo stvarnim ljudima, a oni kojima se svidi ono što vide zaprate vas, lajkaju i komentiraju. Nadzorna ploča pokazuje što smo izmjerili, dan po dan.",
        "hero": {"image": "instagram-hub", "alt": "Instagram profil kreatora na koji stižu novi pratitelji, lajkovi i komentari"},
        "sections": [
            {
                "h2": "Rast koji izgleda zasluženo",
                "p": [
                    "Instagram nagrađuje profile s kojima ljudi stvarno komuniciraju. Botovi rade suprotno: sjede u broju vaših pratitelja, nikad ne lajkaju, nikad ne gledaju i uče algoritam da vaše objave ne vrijedi prikazivati.",
                    "Mi radimo obrnuto. Vaš profil svaki dan prikazujemo stvarnim ljudima i svako je praćenje nečija odluka. Zato lajkovi, pregledi i komentari stižu zajedno s pratiteljima, a ne kao zasebna kupnja.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Stvarni ljudi otkrivaju objave kreatora na Instagramu i ostavljaju komentare"},
            },
            {
                "h2": "Za kreatore koji objavljuju s namjerom",
                "p": [
                    "Osobni brend, nišni profil ili mali obrt: paketi rastu s vama. Počnite s paketom {starter_name} i prijeđite na veći kad vaš sadržaj bude spreman za više.",
                ],
                "ul": [
                    "Koristi imaju i Reels videozapisi, i karuseli, i fotografije.",
                    "Vi nam kažete iz kojeg grada, regije ili države bi trebala dolaziti vaša publika.",
                    "Profil ostaje vaš: nikad ne tražimo vašu lozinku.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "Planiranje sadržaja za Instagram za radnim stolom"},
            },
        ],
        "faqs": [
            ("Jesu li pratitelji stvarni ljudi?", "Da. Svaki pratitelj stvarna je osoba koja je vidjela vaš profil i odlučila vas pratiti. Nikad ne koristimo botove, lažne profile ni instant isporuku."),
            ("Koliko pratitelja donosi paket?", "Obično {starter_audience} novih pratitelja mjesečno uz {starter_name}, {rising_audience} uz {rising_name} i {pro_audience} uz {pro_name}. To su tipični rasponi, a ne fiksan broj: stvarni ljudi odlučuju sami."),
            ("Trebate li moju lozinku za Instagram?", "Nikad. Treba nam samo vaše korisničko ime. Neka profil bude javan kako bi vas ljudi koji ga otkriju mogli zapratiti."),
            ("Mogu li kupiti samo lajkove ili komentare?", "Ne. Lajkovi, pregledi i komentari dolaze unutar svakog paketa, od istih stvarnih ljudi koji vas prate. Upravo zato vaše brojke ostaju prirodne."),
            ("Mogu li otkazati bilo kada?", "Da. Paketi se obnavljaju svaki mjesec, a otkazati ih možete u svom računu. Plaćeni mjesec traje do kraja."),
        ],
    },
    {
        "service": "followers",
        "slug": "instagram/pratitelji",
        "label": "Instagram pratitelji",
        "title": "Stvarni pratitelji na Instagramu, svaki mjesec | Growsterr",
        "description": "Pratitelji na Instagramu koji su stvarni ljudi i sami su vas odlučili pratiti, uz lajkove i komentare istih ljudi. Mjesečni paketi od {from_price}.",
        "h1": ("Pratitelji na Instagramu ", "koji su vas odlučili pratiti."),
        "intro": "Stvarni ljudi svaki dan otkrivaju vaš profil, a oni kojima se svidi ono što vide zaprate vas. Obično {starter_audience} novih pratitelja mjesečno uz {starter_name}, s lajkovima i komentarima istih ljudi.",
        "hero": {"image": "instagram-followers", "alt": "Instagram profil koji dobiva nove pratitelje, stvarne ljude"},
        "sections": [
            {
                "h2": "Zašto stvarni pratitelji vrijede više",
                "p": [
                    "Pratitelj se računa samo ako iza njega stoji osoba. Stvarni pratitelji vide vašu sljedeću objavu, lajkaju je, komentiraju i dijele, a upravo tu angažiranost Instagram gleda kad odlučuje kome još prikazati vaš sadržaj.",
                    "Botovi ništa od toga ne mogu. Nekoliko dana podižu broj, nestanu u sljedećem čišćenju, a oni koji ostanu tiho vam smanjuju doseg.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Stvarni ljudi lajkaju i komentiraju objavu kreatora na Instagramu"},
            },
            {
                "h2": "Odakle dolaze vaši novi pratitelji",
                "p": [
                    "Recite nam iz kojeg grada, regije ili države bi trebala dolaziti vaša publika. Vaš profil najprije prikazujemo stvarnim ljudima ondje; gdje je publika koja vam najbolje odgovara veća, više ih može doći iz okolice.",
                ],
            },
            {
                "h2": "Kako izgleda jedan mjesec",
                "ul": [
                    "Prvi dani: kampanja kreće i stižu prvi posjeti.",
                    "Svaki tjedan: novi pratitelji, lajkovi i komentari, pomalo svaki dan.",
                    "Do kraja mjeseca: obično {pick_audience} novih pratitelja uz {pick_name}.",
                ],
            },
        ],
        "faqs": [
            ("Koliko brzo stižu pratitelji?", "Pomalo svaki dan, kroz cijeli mjesec. Nikad sve odjednom: stvarni ljudi prate vlastitim tempom, a sve što stigne instant je bot."),
            ("Hoće li me novi pratitelji otpratiti?", "Neki možda hoće, kao što se mijenja svaka stvarna publika. Stvarni pratitelji ostaju mnogo češće od botova, koji nestaju u valovima."),
            ("Dobivam li i lajkove i komentare?", "Da, od istih ljudi: obično {pick_likes} lajkova i {pick_comments} komentara mjesečno uz {pick_name}."),
            ("Je li to sigurno za moj profil?", "Nikad ne tražimo vašu lozinku i nikad se ne prijavljujemo u vaš profil. Ljudi sami pronalaze vaš profil i sami odlučuju, kao i svaki drugi pratitelj."),
            ("Mogu li odabrati odakle su moji pratitelji?", "Da. Pri narudžbi navedite grad, regiju ili državu. Najprije ciljamo ondje; kad je vrlo slična publika u blizini veća, dio pratitelja može doći i odande."),
        ],
    },
    {
        "service": "followers",
        "quantity": 1000,
        "slug": "instagram/pratitelji/1000",
        "label": "{quantity} Instagram pratitelja",
        "title": "{quantity} pratitelja na Instagramu, samo stvarni ljudi | Growsterr",
        "description": "Dođite do {quantity} pratitelja na Instagramu uz stvarne ljude, a ne botove. {pick_name} obično donosi {pick_audience} mjesečno, uz lajkove i komentare.",
        "h1": ("{quantity} pratitelja na Instagramu, ", "i svaki je stvarna osoba."),
        "intro": "Ne prodajemo paket od {quantity} botova. Vaš profil razvijamo uz stvarne ljude: {pick_name} obično donosi {pick_audience} novih pratitelja mjesečno, pa je {quantity} obično nadohvat ruke već u prvom mjesecu.",
        "hero": {"image": "instagram-followers-1000", "alt": "Rastuća linija novih pratitelja na Instagramu dostiže prvu prekretnicu"},
        "sections": [
            {
                "h2": "Zašto ne {quantity} pratitelja u jednom satu?",
                "p": [
                    "Zato što nijedna stvarna osoba ne zaprati profil nekoliko sekundi nakon plaćanja. Usluge koje isporuče {quantity} pratitelja u jednom satu isporučuju botove: ne lajkaju, ne komentiraju i nestaju u valovima.",
                    "Oni koji ostanu čine još veću štetu. Svaki pratitelj koji nikad ne reagira smanjuje udio publike koja reagira, a vaše objave tiho dopiru do manje ljudi.",
                ],
            },
            {
                "h2": "Vaših prvih tisuću, kako treba",
                "p": [
                    "Prvih tisuću stvarnih pratitelja mijenja način na koji vas vide novi posjetitelji. To su ljudi koji bi mogli gledati vaše Reels videozapise, lajkati objave i vraćati se, a upravo to pomaže da vas pronađe sljedećih tisuću.",
                ],
                "ul": [
                    "Stvarni ljudi koji su vas odlučili pratiti, s lokacije koju odaberete.",
                    "Lajkovi i komentari istih ljudi, unutar paketa.",
                    "Nadzorna ploča koja pokazuje što smo izmjerili, dan po dan.",
                ],
            },
        ],
        "faqs": [
            ("Koliko treba do {quantity} stvarnih pratitelja?", "Uobičajenim tempom {pick_name} donosi {pick_audience} novih pratitelja mjesečno, pa je {quantity} obično nadohvat već u prvom mjesecu. Stvarni ljudi prate vlastitim tempom, pa je svaki mjesec malo drukčiji."),
            ("Je li to jednokratni paket od {quantity}?", "Ne. Rast prodajemo kao mjesečne pakete. {pick_name} stoji {pick_price} mjesečno, a otkazati ga možete bilo kada u svom računu."),
            ("Dobivam li uz njih i lajkove i komentare?", "Da, od istih stvarnih ljudi: obično {pick_likes} lajkova i {pick_comments} komentara mjesečno uz {pick_name}."),
            ("Što nakon {quantity}?", "Paket traje dok ga ne otkažete, pa se vaš rast nastavlja iz mjeseca u mjesec. Kad vaš sadržaj bude spreman za više, možete prijeći na veći paket."),
        ],
    },
]
