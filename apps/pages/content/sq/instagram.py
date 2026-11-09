"""Albanian Instagram pages: the hub, followers, and the 1,000-followers goal.
Keys and placeholders: docs/CONTENT.md. Numbers come from the packages ({starter_audience}...),
so they follow apps/growth/plan.py when prices or ranges change."""

UPDATED = "2026-11-08"

PAGES = [
    {
        # The hub: no service.
        "slug": "instagram",
        "label": "Instagram",
        "title": "Paketa rritjeje në Instagram për krijues | Growsterr",
        "description": "Rrituni në Instagram me njerëz të vërtetë: paketa mujore me ndjekës të rinj, pëlqime dhe komente nga njerëz që zgjodhën t'ju ndjekin. Nga {from_price} në muaj.",
        "h1": ("Rritni Instagram-in tuaj ", "me njerëz të vërtetë."),
        "intro": "Paketa mujore rritjeje për krijues dhe influencerë. Ua shfaqim profilin tuaj njerëzve të vërtetë, dhe ata që pëlqejnë atë që shohin ju ndjekin, pëlqejnë dhe komentojnë. Paneli juaj tregon çfarë matëm, ditë pas dite.",
        "hero": {"image": "instagram-hub", "alt": "Profili i një krijuesi në Instagram, ku vijnë ndjekës, pëlqime dhe komente të reja"},
        "sections": [
            {
                "h2": "Rritje që duket se e keni fituar vetë",
                "p": [
                    "Instagram-i shpërblen llogaritë me të cilat njerëzit angazhohen vërtet. Robotët bëjnë të kundërtën: rrinë në numrin e ndjekësve, nuk pëlqejnë kurrë, nuk shikojnë kurrë dhe i mësojnë algoritmit se postimet tuaja nuk ia vlen të shfaqen.",
                    "Ne punojmë anasjelltas. Profili juaj u shfaqet çdo ditë njerëzve të vërtetë, dhe çdo ndjekje është një zgjedhje që dikush bëri. Prandaj pëlqimet, shikimet dhe komentet vijnë bashkë me ndjekësit, jo si blerje më vete.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Njerëz të vërtetë që zbulojnë postimet e një krijuesi në Instagram dhe lënë komente"},
            },
            {
                "h2": "Për krijues që postojnë me qëllim",
                "p": [
                    "Markë personale, faqe me temë të veçantë apo biznes i vogël: paketat rriten bashkë me ju. Nisni me {starter_name} dhe kaloni më lart kur përmbajtja juaj të jetë gati për më shumë.",
                ],
                "ul": [
                    "Përfitojnë të gjitha: Reels, karuselet dhe postimet me foto.",
                    "Ju na tregoni qytetin, rajonin ose shtetin nga duhet të vijë publiku juaj.",
                    "Llogaria mbetet e juaja: nuk ju kërkojmë kurrë fjalëkalimin.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "Një krijues që planifikon përmbajtje për Instagram në tavolinën e punës"},
            },
        ],
        "faqs": [
            ("A janë ndjekësit njerëz të vërtetë?", "Po. Çdo ndjekës është një njeri i vërtetë që pa profilin tuaj dhe zgjodhi t'ju ndjekë. Nuk përdorim kurrë robotë, profile të rreme apo dërgim «në çast»."),
            ("Sa ndjekës sjell një paketë?", "Zakonisht {starter_audience} ndjekës të rinj në muaj me {starter_name}, {rising_audience} me {rising_name} dhe {pro_audience} me {pro_name}. Këto janë intervale tipike, jo një numër i caktuar: njerëzit e vërtetë vendosin vetë."),
            ("A ju duhet fjalëkalimi im i Instagram-it?", "Kurrë. Na duhet vetëm emri i përdoruesit. Mbajeni llogarinë publike, që njerëzit që e zbulojnë të mund t'ju ndjekin."),
            ("A mund të blej pëlqime ose komente më vete?", "Jo. Pëlqimet, shikimet dhe komentet vijnë brenda çdo pakete, nga të njëjtët njerëz të vërtetë që ju ndjekin. Kjo i mban shifrat tuaja natyrale."),
            ("A mund të anuloj kur të dua?", "Po. Paketat rinovohen çdo muaj dhe mund t'i anuloni nga llogaria juaj. Muaji i paguar vazhdon deri në fund."),
        ],
    },
    {
        "service": "followers",
        "slug": "instagram/ndjekes",
        "label": "Ndjekës në Instagram",
        "title": "Ndjekës të vërtetë në Instagram, çdo muaj | Growsterr",
        "description": "Ndjekës në Instagram që janë njerëz të vërtetë dhe zgjodhën t'ju ndjekin, me pëlqime dhe komente nga të njëjtët njerëz. Paketa mujore nga {from_price}.",
        "h1": ("Ndjekës në Instagram ", "që zgjodhën t'ju ndjekin."),
        "intro": "Njerëz të vërtetë e zbulojnë profilin tuaj çdo ditë, dhe ata që pëlqejnë atë që shohin ju ndjekin. Zakonisht {starter_audience} ndjekës të rinj në muaj me {starter_name}, me pëlqime dhe komente nga të njëjtët njerëz.",
        "hero": {"image": "instagram-followers", "alt": "Një profil në Instagram që fiton ndjekës të rinj nga njerëz të vërtetë"},
        "sections": [
            {
                "h2": "Pse ndjekësit e vërtetë vlejnë më shumë",
                "p": [
                    "Një ndjekës ka vlerë vetëm nëse pas tij ka një njeri. Ndjekësit e vërtetë e shohin postimin tuaj të radhës, e pëlqejnë, e komentojnë dhe e ndajnë, dhe pikërisht këtë angazhim shikon Instagram-i kur vendos kujt t'ia shfaqë përmbajtjen tuaj.",
                    "Robotët nuk bëjnë asgjë nga këto. E ngrenë numrin për disa ditë, zhduken në pastrimin e radhës, dhe ata që mbeten e ulin në heshtje shtrirjen tuaj.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Njerëz të vërtetë që pëlqejnë dhe komentojnë postimin e një krijuesi në Instagram"},
            },
            {
                "h2": "Nga vijnë ndjekësit tuaj të rinj",
                "p": [
                    "Na tregoni qytetin, rajonin ose shtetin nga duhet të vijë publiku juaj. Ua shfaqim profilin tuaj fillimisht njerëzve të vërtetë atje; aty ku publiku më i përshtatshëm është më i madh, më shumë prej tyre mund të vijnë nga zonat përreth.",
                ],
            },
            {
                "h2": "Si duket një muaj",
                "ul": [
                    "Ditët e para: fushata juaj nis dhe mbërrijnë vizitat e para.",
                    "Çdo javë: ndjekës të rinj, pëlqime dhe komente, pak nga pak çdo ditë.",
                    "Në fund të muajit: zakonisht {pick_audience} ndjekës të rinj me {pick_name}.",
                ],
            },
        ],
        "faqs": [
            ("Sa shpejt vijnë ndjekësit?", "Pak çdo ditë, gjatë gjithë muajit. Kurrë të gjithë njëherësh: njerëzit e vërtetë ndjekin me ritmin e tyre, dhe çdo gjë «në çast» është robot."),
            ("A do të më ndalojnë së ndjekuri ndjekësit e rinj?", "Disa mund ta bëjnë, ashtu siç ndryshon çdo publik i vërtetë. Ndjekësit e vërtetë mbeten shumë më shpesh se robotët, që zhduken me valë."),
            ("A marr edhe pëlqime dhe komente?", "Po, nga të njëjtët njerëz: zakonisht {pick_likes} pëlqime dhe {pick_comments} komente në muaj me {pick_name}."),
            ("A është e sigurt për llogarinë time?", "Nuk ju kërkojmë kurrë fjalëkalimin dhe nuk hyjmë kurrë në llogarinë tuaj. Njerëzit e gjejnë profilin tuaj dhe vendosin vetë, ashtu si ju gjen çdo ndjekës."),
            ("A mund të zgjedh nga janë ndjekësit?", "Po. Na tregoni qytetin, rajonin ose shtetin kur porositni. Synojmë fillimisht atje; kur një publik shumë i ngjashëm është më i madh aty pranë, disa nga ndjekësit tuaj mund të vijnë prej andej."),
        ],
    },
    {
        "service": "followers",
        "quantity": 1000,
        "slug": "instagram/ndjekes/1000",
        "label": "{quantity} ndjekës në Instagram",
        "title": "{quantity} ndjekës në Instagram nga njerëz të vërtetë | Growsterr",
        "description": "Arrini {quantity} ndjekës në Instagram me njerëz të vërtetë, jo robotë. {pick_name} sjell zakonisht {pick_audience} në muaj, bashkë me pëlqime dhe komente.",
        "h1": ("{quantity} ndjekës në Instagram, ", "secili prej tyre i vërtetë."),
        "intro": "Nuk shesim një paketë me {quantity} robotë. E rritim llogarinë tuaj me njerëz të vërtetë: {pick_name} sjell zakonisht {pick_audience} ndjekës të rinj në muaj, ndaj {quantity} zakonisht arrihen që në muajin e parë.",
        "hero": {"image": "instagram-followers-1000", "alt": "Një vijë në ngjitje me ndjekës të rinj në Instagram që arrin synimin e parë"},
        "sections": [
            {
                "h2": "Pse jo {quantity} ndjekës brenda një ore?",
                "p": [
                    "Sepse asnjë njeri i vërtetë nuk ndjek një llogari pak sekonda pas një pagese. Shërbimet që japin {quantity} ndjekës brenda një ore japin robotë: nuk pëlqejnë, nuk komentojnë dhe zhduken me valë.",
                    "Ata që mbeten bëjnë edhe më shumë dëm. Çdo ndjekës që nuk angazhohet kurrë ul pjesën e publikut tuaj që angazhohet, dhe postimet tuaja arrijnë në heshtje te më pak njerëz.",
                ],
            },
            {
                "h2": "Mijëshja juaj e parë, e bërë si duhet",
                "p": [
                    "Një mijë ndjekësit e parë të vërtetë ndryshojnë mënyrën si ju shohin vizitorët e rinj. Janë njerëz që mund të shohin Reels-at tuaja, të pëlqejnë postimet tuaja dhe të rikthehen, dhe pikërisht kjo e ndihmon mijëshen e radhës t'ju gjejë.",
                ],
                "ul": [
                    "Njerëz të vërtetë që zgjodhën t'ju ndjekin, nga vendndodhja që zgjidhni.",
                    "Pëlqime dhe komente nga të njëjtët njerëz, brenda paketës.",
                    "Një panel që tregon çfarë matëm, ditë pas dite.",
                ],
            },
        ],
        "faqs": [
            ("Sa kohë duhet për {quantity} ndjekës të vërtetë?", "Me ritmin tipik, {pick_name} sjell {pick_audience} ndjekës të rinj në muaj, ndaj {quantity} zakonisht arrihen që në muajin e parë. Njerëzit e vërtetë ndjekin me ritmin e tyre, ndaj çdo muaj është pak ndryshe."),
            ("A është një paketë e njëhershme prej {quantity}?", "Jo. Rritjen e shesim si paketa mujore. {pick_name} kushton {pick_price} në muaj dhe mund ta anuloni kur të doni nga llogaria juaj."),
            ("A marr pëlqime dhe komente bashkë me ta?", "Po, nga të njëjtët njerëz të vërtetë: zakonisht {pick_likes} pëlqime dhe {pick_comments} komente në muaj me {pick_name}."),
            ("Çfarë ndodh pas {quantity}?", "Paketa juaj vazhdon derisa ta anuloni, ndaj rritja juaj vazhdon muaj pas muaji. Kur përmbajtja juaj të jetë gati për më shumë, mund të kaloni në një paketë më të madhe."),
        ],
    },
]
