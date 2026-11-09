"""Basque Instagram pages: the hub, followers ("jarraitzaileak"), and the 1,000-followers goal.
Keys and placeholders: docs/CONTENT.md; Basque placeholder grammar: eu/ui.py."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "instagram",
        "label": "Instagram",
        "title": "Instagram hazteko paketeak sortzaileentzat | Growsterr",
        "description": "Hazi Instagram sarean pertsona errealekin: hileko paketeek jarraitzaile berriak, atsegiteak eta iruzkinak dakartzate. Pakete merkeena: {from_price} hilean.",
        "h1": ("Hazi zure Instagram kontua ", "pertsona errealekin."),
        "intro": "Sortzaile eta influencerrentzako hileko hazkunde-paketeak. Zure profila pertsona errealei erakusten diegu, eta ikusten dutena gustuko dutenek jarraitu egiten dizute, atsegiteak uzten dituzte eta iruzkinak idazten dituzte. Zure panelak egunez egun erakusten du neurtu duguna.",
        "hero": {"image": "instagram-hub", "alt": "Sortzaile baten Instagram profila, jarraitzaile berriak, atsegiteak eta iruzkinak jasotzen ari dena"},
        "sections": [
            {
                "h2": "Merezitakoa dirudien hazkundea, merezitakoa delako",
                "p": [
                    "Instagramek jendeak benetan parte hartzen duen kontuak saritzen ditu. Botek kontrakoa egiten dute: zure jarraitzaile-kopuruan geratzen dira, ez dute inoiz atsegiterik uzten, ez dute ezer ikusten, eta algoritmoari erakusten diote zure argitalpenak ez direla erakusteko modukoak.",
                    "Guk alderantziz egiten dugu. Egunero zure profila pertsona errealei erakusten diegu, eta jarraitzaile berri bakoitza norbaiten erabakia da. Horregatik datoz atsegiteak, ikustaldiak eta iruzkinak zure jarraitzaileekin batera, eta ez aparteko erosketa gisa.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Pertsona errealak sortzaile baten Instagram argitalpenak ezagutzen eta iruzkinak uzten"},
            },
            {
                "h2": "Asmo argiz argitaratzen duten sortzaileentzat",
                "p": [
                    "Marka pertsonala, nitxo-orria edo negozio txikia: paketeak zurekin hazten dira. Hasi {starter_name} paketearekin, eta igo hurrengo paketera zure edukia gehiagorako prest dagoenean.",
                ],
                "ul": [
                    "Reelsek, karruselek eta argazkiek denek ateratzen dute onura.",
                    "Zuk esaten diguzu zein hiri, eskualde edo herrialdetatik etorri behar den zure publikoa.",
                    "Zure kontua zurea da: ez dizugu inoiz pasahitza eskatzen.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "Sortzaile bat Instagram edukia planifikatzen bere mahaian"},
            },
        ],
        "faqs": [
            ("Jarraitzaileak pertsona errealak dira?", "Bai. Jarraitzaile bakoitza zure profila ikusi eta zuri jarraitzea erabaki duen pertsona erreal bat da. Ez dugu inoiz botik, profil faltsurik edo berehalako entregarik erabiltzen."),
            ("Zenbat jarraitzaile dakartza pakete batek?", "Normalean {starter_audience} jarraitzaile berri hilean {starter_name} paketearekin, {rising_audience} {rising_name} paketearekin eta {pro_audience} {pro_name} paketearekin. Ohiko tarteak dira, ez kopuru finko bat: pertsona errealek beren kabuz erabakitzen dute."),
            ("Nire Instagram pasahitza behar duzue?", "Inoiz ez. Zure erabiltzaile-izena besterik ez dugu behar. Mantendu zure kontua publiko, ezagutzen dutenek jarraitu ahal izan diezazuten."),
            ("Atsegiteak edo iruzkinak bereiz eros ditzaket?", "Ez. Atsegiteak, ikustaldiak eta iruzkinak pakete guztietan daude barne, eta zuri jarraitzen dizuten pertsona erreal berengandik datoz. Horrek mantentzen ditu zure zenbakiak natural."),
            ("Nahi dudanean utz dezaket?", "Bai. Paketeak hilero berritzen dira, eta zure kontutik utz dezakezu. Ordaindutako hilabeteak amaierara arte jarraitzen du."),
        ],
    },
    {
        "service": "followers",
        "slug": "instagram/jarraitzaileak",
        "label": "Instagram jarraitzaileak",
        "title": "Benetako Instagram jarraitzaileak, hilero | Growsterr",
        "description": "Instagram jarraitzaileak: zuri jarraitzea erabaki duten pertsona errealak, atsegite eta iruzkinekin. Pakete merkeenak {from_price} balio du hilean.",
        "h1": ("Instagram jarraitzaileak, ", "zuri jarraitzea erabaki dutenak."),
        "intro": "Pertsona errealek egunero ezagutzen dute zure profila, eta ikusten dutena gustuko dutenek jarraitu egiten dizute. Normalean {starter_audience} jarraitzaile berri hilean {starter_name} paketearekin, pertsona berengandik datozen atsegite eta iruzkinekin.",
        "hero": {"image": "instagram-followers", "alt": "Instagram profil batek pertsona errealen jarraitzaile berriak irabazten ditu"},
        "sections": [
            {
                "h2": "Zergatik balio duten gehiago benetako jarraitzaileek",
                "p": [
                    "Jarraitzaile batek atzean pertsona bat dagoenean bakarrik balio du. Benetako jarraitzaileek zure hurrengo argitalpena ikusten dute, atsegin dute, iruzkintzen dute eta partekatzen dute, eta interakzio hori begiratzen du Instagramek zure edukia nori gehiago erakutsi erabakitzeko.",
                    "Botek ez dute horrelakorik egiten. Zenbaki bat puzten dute egun batzuetan, hurrengo garbiketan desagertzen dira, eta geratzen direnek isilean jaisten dute zure irismena.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Pertsona errealek sortzaile baten Instagram argitalpena atsegin eta iruzkintzen dute"},
            },
            {
                "h2": "Nondik datozen zure jarraitzaile berriak",
                "p": [
                    "Esaguzu zein hiri, eskualde edo herrialdetatik etorri behar den zure publikoa. Zure profila hango pertsona errealei erakusten diegu lehenik; publiko egokiena inguruan handiagoa bada, gehiago etor daitezke handik.",
                ],
            },
            {
                "h2": "Nolakoa den hilabete bat",
                "ul": [
                    "Lehen egunak: kanpaina abian jartzen da eta lehen bisitak iristen dira.",
                    "Astero: jarraitzaile berriak, atsegiteak eta iruzkinak, egunero batzuk.",
                    "Hilabetearen amaieran: normalean {pick_audience} jarraitzaile berri {pick_name} paketearekin.",
                ],
            },
        ],
        "faqs": [
            ("Zein azkar iristen dira jarraitzaileak?", "Egunero pixka bat, hilabete osoan zehar. Inoiz ez dena batera: pertsona errealek beren erritmoan jarraitzen dute, eta berehala iristen den guztia bot bat da."),
            ("Nire jarraitzaile berriek jarraitzeari utziko diote?", "Batzuek agian bai, edozein publiko errealetan gertatzen den bezala. Benetako jarraitzaileak askoz gehiagotan geratzen dira botak baino, eta botak olatuka desagertzen dira."),
            ("Atsegiteak eta iruzkinak ere jasotzen ditut?", "Bai, pertsona berengandik: normalean {pick_likes} atsegite eta {pick_comments} iruzkin hilean {pick_name} paketearekin."),
            ("Segurua da nire kontuarentzat?", "Ez dizugu inoiz pasahitza eskatzen eta ez gara inoiz zure kontuan sartzen. Jendeak zure profila aurkitzen du eta beren kabuz erabakitzen dute, edozein jarraitzailek aurkitzen zaituen bezala."),
            ("Aukera dezaket nondik datozen nire jarraitzaileak?", "Bai. Esan hiria, eskualdea edo herrialdea eskaera egitean. Hara jotzen dugu lehenik; inguruan oso antzeko publiko handiagoa badago, jarraitzaile batzuk handik etor daitezke."),
        ],
    },
    {
        "service": "followers",
        "quantity": 1000,
        "slug": "instagram/jarraitzaileak/1000",
        "label": "{quantity} Instagram jarraitzaile",
        "title": "{quantity} Instagram jarraitzaile, pertsona errealak | Growsterr",
        "description": "Lortu {quantity} Instagram jarraitzaile pertsona errealekin, ez botekin. {pick_name} paketeak normalean {pick_audience} dakartza hilean, atsegiteekin.",
        "h1": ("{quantity} Instagram jarraitzaile, ", "denak errealak."),
        "intro": "Ez dugu {quantity} botez osatutako sortarik saltzen. Zure kontua pertsona errealekin hazten dugu: {pick_name} paketeak normalean {pick_audience} jarraitzaile berri dakartza hilean; beraz, {quantity} lehen hilabetean bertan lor daiteke askotan.",
        "hero": {"image": "instagram-followers-1000", "alt": "Instagram jarraitzaile berrien lerro gorakorra, lehen mugarri batera iristen"},
        "sections": [
            {
                "h2": "Zergatik ez {quantity} jarraitzaile ordubetean?",
                "p": [
                    "Pertsona erreal batek ere ez diolako kontu bati jarraitzen ordainketa baten ondorengo segundoetan. Ordubetean {quantity} jarraitzaile ematen dituzten zerbitzuek botak ematen dituzte: ez dute atsegiterik uzten, ez dute iruzkinik idazten, eta olatuka desagertzen dira.",
                    "Geratzen direnek kalte handiagoa egiten dute. Inoiz parte hartzen ez duen jarraitzaile bakoitzak txikitu egiten du parte hartzen duen publikoaren zatia, eta zure argitalpenak isilean iristen dira pertsona gutxiagorengana.",
                ],
            },
            {
                "h2": "Zure lehen milak, ondo eginda",
                "p": [
                    "Lehen mila jarraitzaile errealek aldatu egiten dute bisitari berriek zu ikusteko modua. Zure Reelsak ikusi, zure argitalpenak atsegin eta itzul daitezkeen pertsonak dira, eta horixe bera da hurrengo milei zu aurkitzen laguntzen diena.",
                ],
                "ul": [
                    "Zuri jarraitzea erabaki duten pertsona errealak, zuk aukeratutako tokitik.",
                    "Pertsona berengandik datozen atsegiteak eta iruzkinak, paketean barne.",
                    "Neurtu duguna egunez egun erakusten duen panel bat.",
                ],
            },
        ],
        "faqs": [
            ("Zenbat denbora behar da {quantity} jarraitzaile erreal lortzeko?", "Ohiko erritmoan, {pick_name} paketeak {pick_audience} jarraitzaile berri dakartza hilean; beraz, {quantity} lehen hilabetean bertan lortzen da askotan. Pertsona errealek beren erritmoan jarraitzen dute, eta horregatik hilabete bakoitza apur bat desberdina da."),
            ("Behin bakarrik ordaintzen den {quantity} jarraitzaileko sorta bat da?", "Ez. Hazkundea hileko paketetan saltzen dugu. {pick_name} paketeak {pick_price} balio du hilean, eta nahi duzunean utz dezakezu zure kontutik."),
            ("Atsegiteak eta iruzkinak ere jasotzen ditut haiekin?", "Bai, pertsona erreal berengandik: normalean {pick_likes} atsegite eta {pick_comments} iruzkin hilean {pick_name} paketearekin."),
            ("Zer gertatzen da {quantity} jarraitzaile lortu ondoren?", "Zure paketeak aurrera jarraitzen du zuk utzi arte; beraz, zure hazkundeak hilabetez hilabete jarraitzen du. Zure edukia gehiagorako prest dagoenean, pakete handiago batera igo zaitezke."),
        ],
    },
]
