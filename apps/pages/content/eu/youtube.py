"""Basque YouTube pages: the hub and subscribers ("harpidedunak"). Keys and placeholders: docs/CONTENT.md;
Basque placeholder grammar: eu/ui.py."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "youtube",
        "label": "YouTube",
        "title": "YouTube hazteko paketeak sortzaileentzat | Growsterr",
        "description": "Hazi zure YouTube kanala pertsona errealekin: hileko paketeek harpidedunak, atsegiteak eta iruzkinak dakartzate. Pakete merkeena: {from_price} hilean.",
        "h1": ("Hazi zure YouTube kanala ", "ikusle errealekin."),
        "intro": "Sortzaileentzako hileko hazkunde-paketeak. Pertsona errealek zure kanala ezagutzen dute, zure bideoak ikusten dituzte eta harpidetu egiten dira ikusten dutena gustuko dutenean. Zure panelak egunez egun erakusten du neurtu duguna.",
        "hero": {"image": "youtube-hub", "alt": "YouTube kanal batek ikusle errealen harpidedunak, atsegiteak eta iruzkinak irabazten ditu"},
        "sections": [
            {
                "h2": "Ikusten duten harpidedunak dira kontatzen dutenak",
                "p": [
                    "YouTubek jendeak ikusi, atsegin eta berriz bisitatzen dituen bideoak gomendatzen ditu. Inoiz ikusten ez duen harpidedun bat izatea bat ere ez izatea baino okerragoa da: parte hartzen duen publikoaren zatia txikitzen du.",
                    "Ekartzen dugun harpidedun bakoitza zure kanala aurkitu eta harpidetzea erabaki duen pertsona bat da. Atsegiteak, ikustaldiak eta iruzkinak pertsona berengandik datoz, zure paketearen barruan.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Ikusleak sortzaile baten YouTube bideoa ikusten eta iruzkinak idazten"},
            },
            {
                "h2": "Arretaz argitaratzen duten kanalentzat",
                "p": [
                    "Tutorialak, vlogak, musika edo gaming: aldizka argitaratzen baduzu, ikusle errealek abiapuntu hobea ematen diote bideo berri bakoitzari. Hasi {starter_name} paketearekin, eta igo hurrengo paketera zure kanala gehiagorako prest dagoenean.",
                ],
                "ul": [
                    "Zuk esaten diguzu zein hiri, eskualde edo herrialdetatik etorri behar den zure publikoa.",
                    "Harpidedunak, atsegiteak eta iruzkinak batera datoz, pertsona berengandik.",
                    "Zure kanala zurea da: ez dizugu inoiz pasahitza eskatzen.",
                ],
                "image": {"image": "youtube-channel", "alt": "Sortzaile bat YouTube bideo bat editatzen etxeko estudioan"},
            },
        ],
        "faqs": [
            ("Harpidedunak pertsona errealak dira?", "Bai. Harpidedun bakoitza zure kanala aurkitu eta harpidetzea erabaki duen pertsona erreal bat da. Botik gabe, kontu faltsurik gabe, berehalako ezer gabe."),
            ("Zenbat harpidedun dakartza pakete batek?", "Normalean {starter_audience} harpidedun berri hilean {starter_name} paketearekin, {rising_audience} {rising_name} paketearekin eta {pro_audience} {pro_name} paketearekin. Ohiko tarteak, ez kopuru finko bat."),
            ("Nire Google edo YouTube pasahitza behar duzue?", "Inoiz ez. Zure kanalaren identifikatzailea besterik ez dugu behar, eta zure kanalak publikoa izan behar du."),
            ("Ikustaldiak edo atsegiteak bereiz eros ditzaket?", "Ez. Ikustaldiak, atsegiteak eta iruzkinak pakete guztietan daude barne, eta harpidetzen diren pertsona erreal berengandik datoz."),
            ("Nahi dudanean utz dezaket?", "Bai. Paketeak hilero berritzen dira, eta zure kontutik utz dezakezu. Ordaindutako hilabeteak amaierara arte jarraitzen du."),
        ],
    },
    {
        "service": "subscribers",
        "slug": "youtube/harpidedunak",
        "label": "YouTube harpidedunak",
        "title": "Ikusten duten YouTube harpidedun errealak | Growsterr",
        "description": "YouTube harpidedunak, pertsona errealak: zure kanala aurkitu eta harpidetzea erabaki duten ikusleak, atsegite eta iruzkinekin. Pakete merkeena: {from_price} hilean.",
        "h1": ("YouTube harpidedunak, ", "benetan ikusten dutenak."),
        "intro": "Pertsona errealek zure kanala ezagutzen dute, zure bideoak ikusten dituzte eta harpidetu egiten dira ikusten dutena gustuko dutenean. Normalean {starter_audience} harpidedun berri hilean {starter_name} paketearekin, ikusle berengandik datozen atsegite eta iruzkinekin.",
        "hero": {"image": "youtube-subscribers", "alt": "YouTube kanal baten orria, ikusle errealen harpidedun berriekin"},
        "sections": [
            {
                "h2": "Harpidedun batek ikusle izan beharko luke",
                "p": [
                    "YouTuben, harpidedun bat ikusten badu bakarrik da baliagarria. Benetako harpidedunek zure hurrengo bideoa ikusten dute, atsegin dute eta batzuetan iruzkintzen dute, eta hori begiratzen du YouTubek zer gomendatu erabakitzeko.",
                    "Bot-harpidedunek ez dute inoiz ezer ikusten. Kanal bat handiagoa dela dirudi haiei esker, baina haren bideoak pertsona gutxiagorengana iristen dira.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Ikusle errealak YouTube kanal batera harpidetzen, bideo bat ikusi ondoren"},
            },
            {
                "h2": "Nolakoa den hilabete bat",
                "ul": [
                    "Lehen egunak: kanpaina abian jartzen da eta lehen ikusleak iristen dira.",
                    "Astero: harpidedun berriak, atsegiteak eta iruzkinak, egunero batzuk.",
                    "Hilabetearen amaieran: normalean {pick_audience} harpidedun berri {pick_name} paketearekin.",
                ],
            },
            {
                "h2": "Nondik datozen zure ikusleak",
                "p": [
                    "Esaguzu zein hiri, eskualde edo herrialdetatik etorri behar den zure publikoa. Zure kanala hango pertsona errealei erakusten diegu lehenik; publiko egokiena inguruan handiagoa bada, gehiago etor daitezke handik.",
                ],
            },
        ],
        "faqs": [
            ("Zein azkar iristen dira harpidedunak?", "Egunero pixka bat, hilabete osoan zehar. Inoiz ez dena batera: pertsona errealak beren erritmoan harpidetzen dira."),
            ("Nire bideoak ikusiko dituzte?", "Zure kanala ikusi ondoren harpidetzea erabaki duten pertsona errealak dira. Gero zer ikusi beraiek erabakitzen dute, edozein publikok bezala, eta horregatik du balioa."),
            ("Atsegiteak eta iruzkinak ere jasotzen ditut?", "Bai, ikusle berengandik: normalean {pick_likes} atsegite eta {pick_comments} iruzkin hilean {pick_name} paketearekin."),
            ("Nire pasahitza behar duzue?", "Inoiz ez. Zure kanalaren identifikatzailea besterik ez dugu behar, eta zure kanalak publikoa izan behar du."),
        ],
    },
]
