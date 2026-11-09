"""Basque TikTok pages: the hub and likes ("atsegiteak"). Keys and placeholders: docs/CONTENT.md;
Basque placeholder grammar: eu/ui.py."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "tiktok",
        "label": "TikTok",
        "title": "TikTok hazteko paketeak sortzaileentzat | Growsterr",
        "description": "Hazi TikTok sarean pertsona errealekin: hileko paketeek jarraitzaile berriak, atsegiteak eta iruzkinak dakartzate. Pakete merkeena: {from_price} hilean.",
        "h1": ("Hazi zure TikTok kontua ", "pertsona errealekin."),
        "intro": "Sortzaile eta influencerrentzako hileko hazkunde-paketeak. Pertsona errealek zure profila ezagutzen dute, zure bideoak ikusten dituzte eta jarraitu egiten dizute ikusten dutena gustuko dutenean. Zure panelak egunez egun erakusten du neurtu duguna.",
        "hero": {"image": "tiktok-hub", "alt": "Sortzaile baten TikTok profila, jarraitzaile berriak eta atsegiteak jasotzen ari dena"},
        "sections": [
            {
                "h2": "TikTok sarean, arreta da dena",
                "p": [
                    "TikTokek pertsona gehiagori erakusten die bideo bat lehen ikusleek ikusi, atsegin eta iruzkindu egiten dutenean, eta kontuari jarraitzen hasten direnean. Atzean pertsonarik ez duten zenbakiek ez dute horretatik ezer mugitzen.",
                    "Gure paketeek egunero pertsona errealak eramaten dituzte zure profilera. Ikusi egiten dute, erabaki egiten dute, eta zure bideoak gustuko dituztenek jarraitu egiten dizute eta atsegiteak uzten dituzte. Horrelako arretak eramaten du bideo bat urrun.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Ikusle errealak sortzaile baten TikTok bideoak ikusten"},
            },
            {
                "h2": "Zerbait esateko duten sortzaileentzat",
                "p": [
                    "Umorea, sukaldaritza, moda edo tutorialak: aldizka argitaratzen baduzu, ikusle errealek abiapuntu hobea ematen diote bideo berri bakoitzari. Hasi {starter_name} paketearekin, eta igo hurrengo paketera prest zaudenean.",
                ],
                "ul": [
                    "Zuk esaten diguzu zein hiri, eskualde edo herrialdetatik etorri behar den zure publikoa.",
                    "Jarraitzaileak, atsegiteak eta iruzkinak batera datoz, pertsona berengandik.",
                    "Zure kontua zurea da: ez dizugu inoiz pasahitza eskatzen.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Sortzaile bat TikTok bideo bat grabatzen, mugikorra tripode batean jarrita"},
            },
        ],
        "faqs": [
            ("Jarraitzaileak pertsona errealak dira?", "Bai. Jarraitzaile bakoitza zure profila ikusi eta zuri jarraitzea erabaki duen pertsona erreal bat da. Ez dugu inoiz botik, kontu faltsurik edo berehalako entregarik erabiltzen."),
            ("Zenbat jarraitzaile dakartza pakete batek?", "Normalean {starter_audience} jarraitzaile berri hilean {starter_name} paketearekin, {rising_audience} {rising_name} paketearekin eta {pro_audience} {pro_name} paketearekin. Ohiko tarteak, ez kopuru finko bat: pertsona errealek beren kabuz erabakitzen dute."),
            ("Nire TikTok pasahitza behar duzue?", "Inoiz ez. Zure erabiltzaile-izena besterik ez dugu behar. Mantendu zure kontua publiko, ezagutzen dutenek jarraitu ahal izan diezazuten."),
            ("Ikustaldiak edo atsegiteak bereiz eros ditzaket?", "Ez. Ikustaldiak, atsegiteak eta iruzkinak pakete guztietan daude barne, eta zuri jarraitzen dizuten pertsona erreal berengandik datoz."),
            ("Nahi dudanean utz dezaket?", "Bai. Paketeak hilero berritzen dira, eta zure kontutik utz dezakezu. Ordaindutako hilabeteak amaierara arte jarraitzen du."),
        ],
    },
    {
        "service": "likes",
        "slug": "tiktok/atsegiteak",
        "label": "TikTok atsegiteak",
        "title": "TikTok atsegiteak pertsona errealengandik, pakete bakoitzean",
        "description": "Pertsona errealen TikTok atsegiteak, inoiz ez botenak: hileko pakete guztietan daude, jarraitzaile eta iruzkinekin. Pakete merkeena: {from_price} hilean.",
        "h1": ("TikTok atsegiteak pertsona errealengandik. ", "Pakete bakoitzean."),
        "intro": "Ez dugu atsegiterik bereiz saltzen. Pakete bakoitzak zure profila ezagutu, zure bideoak ikusi eta gustuko dutena atsegin duten pertsona errealak dakartza: normalean {starter_likes} atsegite hilean {starter_name} paketearekin.",
        "hero": {"image": "tiktok-likes", "alt": "Ikusle errealen atsegiteak TikTok bideo batetik gora igotzen"},
        "sections": [
            {
                "h2": "Atsegite batek atzean pertsona bat badu bakarrik balio du",
                "p": [
                    "TikTokek begiratzen du zer gertatzen den atsegite baten inguruan: ikusleak ikusten jarraitu du, kontuari jarraitzen hasi da, itzuli da? Boten atsegiteek ezetz erantzuten diote guztiari; beraz, zenbaki bat gehitzen dute eta irismena kentzen.",
                    "Pertsona errealen atsegiteak gainerako guztiarekin batera datoz: ikusteko denbora, jarraitzaile berriak eta iruzkinak. Seinale horrek eramaten du bideo bat urrun.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Ikusleek TikTok bideo bat amaierara arte ikusten dute eta atsegin dute"},
            },
            {
                "h2": "Zenbat atsegite dakartzan pakete bakoitzak",
                "ul": [
                    "{starter_name} ({starter_price} hilean): normalean {starter_likes} atsegite.",
                    "{rising_name} ({rising_price} hilean): normalean {rising_likes} atsegite, zuk aukeratutako bideoetan.",
                    "{pro_name} ({pro_price} hilean): normalean {pro_likes} atsegite, lehentasunezko ikusgarritasunarekin.",
                ],
            },
            {
                "h2": "Zergatik ez ditugun atsegiteak bereiz saltzen",
                "p": [
                    "Ikustaldirik, jarraitzailerik edo iruzkinik gabe iristen diren atsegiteek direna dirudite, hain zuzen ere. Pakete batean, atsegite bakoitza bideoa ikusi duen norbaitengandik dator; beraz, zure zenbakiak batera mugitzen dira, benetako hazkunde batean bezala.",
                ],
            },
        ],
        "faqs": [
            ("TikTok atsegiteak lor ditzaket paketerik gabe?", "Ez. Atsegiteak, ikustaldiak eta iruzkinak gure hileko paketeen barruan bakarrik datoz, pertsona erreal berengandik. Horrek mantentzen ditu natural."),
            ("Zein bideok jasotzen dituzte atsegiteak?", "Pertsona errealek gustuko dutena atsegin dute, normalean zure bideo berrienak. {rising_name} eta {pro_name} paketeekin zuk aukera dezakezu zein bideok jasotzen duten arreta."),
            ("Zein azkar iristen dira atsegiteak?", "Egunero pixka bat, hilabetean zehar. Inoiz ez berehala: berehalako atsegite bat bot bat da."),
            ("Nire TikTok pasahitza behar duzue?", "Inoiz ez. Zure erabiltzaile-izena besterik ez dugu behar, eta zure kontuak publikoa izan behar du."),
        ],
    },
]
