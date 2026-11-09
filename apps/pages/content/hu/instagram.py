"""Hungarian Instagram pages: the hub, followers, and the 1,000-followers goal.
Keys and placeholders: docs/CONTENT.md. Numbers come from the packages ({starter_audience}...)."""

UPDATED = "2026-11-08"

PAGES = [
    {
        # The hub: no service.
        "slug": "instagram",
        "label": "Instagram",
        "title": "Instagram-növekedési csomagok alkotóknak | Growsterr",
        "description": "Növekedj az Instagramon valódi emberekkel: havi csomagok új követőkkel, lájkokkal és kommentekkel olyanoktól, akik maguk döntöttek. Már havi {from_price}.",
        "h1": ("Instagram-növekedés ", "valódi emberekkel."),
        "intro": "Havi növekedési csomagok alkotóknak és influencereknek. Valódi emberek elé tesszük a profilodat, és akiknek tetszik, amit látnak, követnek, lájkolnak és kommentelnek. Az irányítópultod napról napra mutatja, mit mértünk.",
        "hero": {"image": "instagram-hub", "alt": "Egy Instagram-alkotó profilja, ahová új követők, lájkok és kommentek érkeznek"},
        "sections": [
            {
                "h2": "Növekedés, amit tényleg kiérdemeltél",
                "p": [
                    "Az Instagram azokat a fiókokat jutalmazza, amelyekkel az emberek tényleg foglalkoznak. A botok ennek az ellenkezőjét teszik: ott ülnek a követőid között, soha nem lájkolnak, soha nem néznek, és azt tanítják az algoritmusnak, hogy a posztjaidat nem érdemes megmutatni.",
                    "Mi fordítva dolgozunk. A profilodat minden nap valódi emberek látják, és minden követés valakinek a saját döntése. Ezért érkeznek a lájkok, megtekintések és kommentek a követőiddel együtt, nem külön vásárlásként.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Valódi emberek fedezik fel egy alkotó Instagram-posztjait, és kommentet írnak"},
            },
            {
                "h2": "Alkotóknak, akik céllal posztolnak",
                "p": [
                    "Személyes márka, niche oldal vagy kisvállalkozás: a csomagok veled együtt nőnek. Kezdd a {starter_name} csomaggal, és lépj feljebb, amikor a tartalmad készen áll többre.",
                ],
                "ul": [
                    "A Reels-videók, a karusszelek és a fotóposztok egyaránt profitálnak belőle.",
                    "Te mondod meg, melyik városból, régióból vagy országból érkezzen a közönséged.",
                    "A fiókod a tiéd marad: a jelszavadat soha nem kérjük el.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "Egy alkotó az íróasztalánál tervezi az Instagram-tartalmait"},
            },
        ],
        "faqs": [
            ("Valódi emberek a követők?", "Igen. Minden követő valódi ember, aki látta a profilodat, és úgy döntött, hogy követ. Soha nem használunk botokat, hamis profilokat vagy azonnali kiszállítást."),
            ("Hány követőt hoz egy csomag?", "A {starter_name} csomaggal jellemzően havi {starter_audience} új követőt, a {rising_name} csomaggal {rising_audience}, a {pro_name} csomaggal {pro_audience} követőt. Ezek jellemző tartományok, nem fix mennyiség: valódi emberek döntenek maguktól."),
            ("Kell az Instagram-jelszavam?", "Soha. Csak a felhasználónevedre van szükségünk. A fiókod legyen nyilvános, hogy aki rátalál, követni tudja."),
            ("Vehetek külön lájkokat vagy kommenteket?", "Nem. A lájkok, megtekintések és kommentek minden csomagban benne vannak, ugyanazoktól a valódi emberektől, akik követnek. Ettől maradnak természetesek a számaid."),
            ("Bármikor lemondhatom?", "Igen. A csomagok havonta megújulnak, és a fiókodból bármikor lemondhatod őket. A kifizetett hónap a végéig tart."),
        ],
    },
    {
        "service": "followers",
        "slug": "instagram/kovetok",
        "label": "Instagram-követők",
        "title": "Valódi Instagram-követők, minden hónapban | Growsterr",
        "description": "Instagram-követők, akik valódi emberek és maguk döntöttek melletted, lájkokkal és kommentekkel ugyanazoktól. Havi csomagok, már {from_price}.",
        "h1": ("Instagram-követők, ", "akik maguk döntöttek melletted."),
        "intro": "Valódi emberek minden nap felfedezik a profilodat, és akiknek tetszik, amit látnak, bekövetnek. A {starter_name} csomaggal havonta jellemzően {starter_audience} új követő, lájkokkal és kommentekkel ugyanazoktól az emberektől.",
        "hero": {"image": "instagram-followers", "alt": "Egy Instagram-profil, amely valódi emberektől kap új követőket"},
        "sections": [
            {
                "h2": "Miért ér többet a valódi követő?",
                "p": [
                    "Egy követő csak akkor számít, ha ember áll mögötte. A valódi követők látják a következő posztodat, lájkolják, kommentelnek és megosztják, és az Instagram éppen ezt az aktivitást figyeli, amikor eldönti, kinek mutassa még meg a tartalmadat.",
                    "A botok egyikre sem képesek. Néhány napra megemelnek egy számot, eltűnnek a következő tisztításnál, a maradók pedig csendben lehúzzák az elérésedet.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Valódi emberek lájkolnak és kommentelnek egy alkotó Instagram-posztja alatt"},
            },
            {
                "h2": "Honnan érkeznek az új követőid?",
                "p": [
                    "Mondd meg, melyik városból, régióból vagy országból érkezzen a közönséged. Először az ottani valódi embereknek mutatjuk a profilodat; ahol a legjobban illő közönség nagyobb, a közelből többen is érkezhetnek.",
                ],
            },
            {
                "h2": "Így néz ki egy hónap",
                "ul": [
                    "Az első napok: elindul a kampányod, és megérkeznek az első látogatások.",
                    "Minden héten: új követők, lájkok és kommentek, naponta néhány.",
                    "A hónap végére: a {pick_name} csomaggal jellemzően {pick_audience} új követő.",
                ],
            },
        ],
        "faqs": [
            ("Milyen gyorsan érkeznek a követők?", "Minden nap egy kicsit, az egész hónap során. Soha nem egyszerre: valódi emberek a saját tempójukban követnek, és ami azonnali, az bot."),
            ("Kikövetnek majd az új követőim?", "Néhányan igen, ahogy minden valódi közönség változik. A valódi követők sokkal gyakrabban maradnak, mint a botok, amelyek hullámokban tűnnek el."),
            ("Lájkokat és kommenteket is kapok?", "Igen, ugyanazoktól az emberektől: a {pick_name} csomaggal havonta jellemzően {pick_likes} lájkot és {pick_comments} kommentet."),
            ("Biztonságos ez a fiókomra nézve?", "A jelszavadat soha nem kérjük el, és soha nem lépünk be a fiókodba. Az emberek maguk találják meg a profilodat és maguk döntenek, ahogy bármelyik követőd rád talál."),
            ("Megválaszthatom, honnan legyenek a követőim?", "Igen. Rendeléskor add meg a várost, régiót vagy országot. Először oda célzunk; ha a közelben nagyobb, jól illő közönség van, a követőid egy része onnan is érkezhet."),
        ],
    },
    {
        "service": "followers",
        "quantity": 1000,
        "slug": "instagram/kovetok/1000",
        "label": "{quantity} Instagram-követő",
        "title": "{quantity} Instagram-követő valódi emberektől | Growsterr",
        "description": "{quantity} Instagram-követő valódi emberektől, nem botoktól. A {pick_name} csomag havonta jellemzően {pick_audience} követőt hoz, lájkokkal és kommentekkel.",
        "h1": ("{quantity} Instagram-követő, ", "és mindegyikük valódi."),
        "intro": "Nem árulunk {quantity} botból álló csomagot. Valódi emberekkel növeljük a fiókodat: a {pick_name} csomag havonta jellemzően {pick_audience} új követőt hoz, így {quantity} követő általában már az első hónapban összejön.",
        "hero": {"image": "instagram-followers-1000", "alt": "Emelkedő vonal, ahogy az új Instagram-követők elérik az első mérföldkövet"},
        "sections": [
            {
                "h2": "Miért nem {quantity} követő egy óra alatt?",
                "p": [
                    "Mert egyetlen valódi ember sem követ be egy fiókot másodpercekkel a fizetés után. Azok a szolgáltatások, amelyek egy óra alatt adnak {quantity} követőt, botokat adnak: nem lájkolnak, nem kommentelnek, és hullámokban tűnnek el.",
                    "A maradók még nagyobb kárt okoznak. Minden követő, aki soha nem reagál, csökkenti a közönséged aktív részének arányát, a posztjaid pedig csendben kevesebb emberhez jutnak el.",
                ],
            },
            {
                "h2": "Az első ezer, ahogy kell",
                "p": [
                    "Az első ezer valódi követő megváltoztatja, hogyan látnak az új látogatók. Olyan emberek ők, akik megnézhetik a Reels-videóidat, lájkolhatják a posztjaidat és visszatérhetnek, és pont ez segít abban, hogy a következő ezer is rád találjon.",
                ],
                "ul": [
                    "Valódi emberek, akik maguk döntöttek a követés mellett, az általad választott helyről.",
                    "Lájkok és kommentek ugyanazoktól az emberektől, a csomag részeként.",
                    "Irányítópult, amely napról napra mutatja, mit mértünk.",
                ],
            },
        ],
        "faqs": [
            ("Mennyi idő alatt lesz {quantity} valódi követőm?", "Jellemző tempóval a {pick_name} csomag havonta {pick_audience} új követőt hoz, így {quantity} követő általában már az első hónapban összejön. Valódi emberek a saját tempójukban követnek, ezért minden hónap kicsit más."),
            ("Ez egy egyszeri, {quantity} darabos csomag?", "Nem. A növekedést havi csomagokban kínáljuk. A {pick_name} díja havi {pick_price}, és a fiókodból bármikor lemondhatod."),
            ("Lájkokat és kommenteket is kapok mellé?", "Igen, ugyanazoktól a valódi emberektől: a {pick_name} csomaggal havonta jellemzően {pick_likes} lájkot és {pick_comments} kommentet."),
            ("Mi történik {quantity} követő után?", "A csomagod a lemondásig fut, így a növekedésed hónapról hónapra folytatódik. Ha a tartalmad készen áll többre, nagyobb csomagra válthatsz."),
        ],
    },
]
