"""Latvian Instagram pages: the hub, followers, and the 1,000-followers goal.
Keys and placeholders: docs/CONTENT.md. Numbers come from the packages ({starter_audience}...)."""

UPDATED = "2026-11-08"

PAGES = [
    {
        # The hub: no service.
        "slug": "instagram",
        "label": "Instagram",
        "title": "Instagram izaugsmes paketes satura veidotājiem | Growsterr",
        "description": "Augiet Instagramā ar īstiem cilvēkiem: mēneša paketes atnes sekotājus, patīk atzīmes un komentārus no tiem, kas izvēlējās jums sekot. No {from_price} mēnesī.",
        "h1": ("Augiet Instagramā ", "ar īstiem cilvēkiem."),
        "intro": "Vēlaties pirkt Instagram sekotājus, patīk atzīmes vai komentārus? Lūk, godīgais variants: ikmēneša izaugsmes paketes satura veidotājiem un influenceriem. Mēs parādām jūsu profilu īstiem cilvēkiem, un tie, kam redzētais patīk, jums seko, atzīmē „patīk” un komentē. Jūsu pārskats dienu pa dienai rāda, ko mēs izmērījām.",
        "hero": {"image": "instagram-hub", "alt": "Instagram satura veidotāja profils, kurā ienāk jauni sekotāji, patīk atzīmes un komentāri"},
        "sections": [
            {
                "h2": "Izaugsme, kas izskatās godīgi nopelnīta",
                "p": [
                    "Instagram atalgo kontus, ar kuriem cilvēki patiešām mijiedarbojas. Boti dara pretējo: tie sēž jūsu sekotāju skaitā, nekad neatzīmē „patīk”, neko neskatās un iemāca algoritmam, ka jūsu ierakstus nav vērts rādīt.",
                    "Mēs strādājam otrādi. Jūsu profils katru dienu tiek parādīts īstiem cilvēkiem, un katrs sekojums ir kāda cilvēka izvēle. Tāpēc patīk atzīmes, skatījumi un komentāri nāk kopā ar sekotājiem, nevis kā atsevišķs pirkums.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Īsti cilvēki atklāj satura veidotāja Instagram ierakstus un atstāj komentārus"},
            },
            {
                "h2": "Satura veidotājiem, kas publicē ar mērķi",
                "p": [
                    "Personīgais zīmols, nišas lapa vai mazs uzņēmums: paketes aug kopā ar jums. Sāciet ar {starter_name} un pārejiet uz lielāku paketi, kad jūsu saturs būs gatavs vairāk.",
                ],
                "ul": [
                    "Ieguvums ir gan Reels, gan karuselēm, gan foto ierakstiem.",
                    "Jūs norādāt pilsētu, reģionu vai valsti, no kuras jānāk jūsu auditorijai.",
                    "Jūsu konts paliek jūsu: mēs nekad neprasām jūsu paroli.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "Satura veidotājs pie galda plāno Instagram saturu"},
            },
        ],
        "faqs": [
            ("Vai sekotāji ir īsti cilvēki?", "Jā. Katrs sekotājs ir īsts cilvēks, kurš redzēja jūsu profilu un izvēlējās jums sekot. Mēs nekad neizmantojam botus, viltus profilus vai tūlītēju piegādi."),
            ("Cik sekotāju atnes viena pakete?", "Parasti {starter_audience} jaunu sekotāju mēnesī ar {starter_name}, {rising_audience} ar {rising_name} un {pro_audience} ar {pro_name}. Tie ir tipiski diapazoni, nevis fiksēts skaits: īsti cilvēki izlemj paši."),
            ("Vai jums vajag manu Instagram paroli?", "Nekad. Mums vajag tikai jūsu lietotājvārdu. Turiet kontu publisku, lai cilvēki, kuri to atklāj, varētu jums sekot."),
            ("Vai varu nopirkt patīk atzīmes vai komentārus atsevišķi?", "Nē. Patīk atzīmes, skatījumi un komentāri ir iekļauti katrā paketē, no tiem pašiem īstajiem cilvēkiem, kas jums seko. Tieši tas saglabā jūsu skaitļus dabiskus."),
            ("Vai varu atcelt jebkurā laikā?", "Jā. Paketes atjaunojas katru mēnesi, un atcelt varat savā kontā. Apmaksātais mēnesis turpinās līdz beigām."),
        ],
    },
    {
        "service": "followers",
        "slug": "instagram/sekotaji",
        "label": "Instagram sekotāji",
        "title": "Pērciet īstus Instagram sekotājus katru mēnesi | Growsterr",
        "description": "Pērciet Instagram sekotājus, kas ir īsti cilvēki un paši izvēlējās jums sekot, ar patīk atzīmēm un komentāriem no tiem pašiem cilvēkiem. Mēnesī no {from_price}.",
        "h1": ("Instagram sekotāji, ", "kas izvēlējās jums sekot."),
        "intro": "Pērciet Instagram sekotājus godīgā veidā: īsti cilvēki katru dienu atklāj jūsu profilu, un tie, kam redzētais patīk, sāk jums sekot. Ar {starter_name} parasti {starter_audience} jaunu sekotāju mēnesī, kā arī patīk atzīmes un komentāri no tiem pašiem cilvēkiem.",
        "hero": {"image": "instagram-followers", "alt": "Instagram profils, kas iegūst jaunus sekotājus no īstiem cilvēkiem"},
        "sections": [
            {
                "h2": "Kāpēc īsti sekotāji ir vērtīgāki",
                "p": [
                    "Sekotājs ir vērtīgs tikai tad, ja aiz viņa ir cilvēks. Īsti sekotāji redz jūsu nākamo ierakstu, atzīmē to ar „patīk”, komentē un dalās ar to, un tieši uz šo iesaisti Instagram skatās, kad izlemj, kam vēl rādīt jūsu saturu.",
                    "Boti neko no tā nespēj. Tie uz pāris dienām palielina skaitli, pazūd nākamajā tīrīšanā, un tie, kas paliek, klusi samazina jūsu sasniedzamību.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Īsti cilvēki atzīmē „patīk” un komentē satura veidotāja Instagram ierakstu"},
            },
            {
                "h2": "No kurienes nāk jūsu jaunie sekotāji",
                "p": [
                    "Norādiet pilsētu, reģionu vai valsti, no kuras jānāk jūsu auditorijai. Vispirms mēs parādām jūsu profilu īstiem cilvēkiem tur; ja vispiemērotākā auditorija tuvumā ir lielāka, vairāk sekotāju var nākt no turienes.",
                ],
            },
            {
                "h2": "Kā izskatās viens mēnesis",
                "ul": [
                    "Pirmās dienas: jūsu kampaņa sākas, un ierodas pirmie apmeklējumi.",
                    "Katru nedēļu: jauni sekotāji, patīk atzīmes un komentāri, mazliet katru dienu.",
                    "Līdz mēneša beigām: ar {pick_name} parasti {pick_audience} jaunu sekotāju.",
                ],
            },
        ],
        "faqs": [
            ("Cik ātri nāk sekotāji?", "Mazliet katru dienu, visa mēneša garumā. Nekad visi uzreiz: īsti cilvēki seko savā tempā, un viss, kas ienāk acumirklī, ir boti."),
            ("Vai jaunie sekotāji pārstās sekot?", "Daži var, tāpat kā mainās jebkura īsta auditorija. Īsti sekotāji paliek daudz biežāk nekā boti, kas pazūd viļņveidīgi."),
            ("Vai saņemšu arī patīk atzīmes un komentārus?", "Jā, no tiem pašiem cilvēkiem: ar {pick_name} parasti {pick_likes} patīk atzīmju un {pick_comments} komentāru mēnesī."),
            ("Vai tas ir droši manam kontam?", "Mēs nekad neprasām jūsu paroli un nekad nepierakstāmies jūsu kontā. Cilvēki atrod jūsu profilu un izlemj paši, tāpat kā jūs atrod jebkurš cits sekotājs."),
            ("Vai varu izvēlēties, no kurienes būs mani sekotāji?", "Jā. Pasūtot norādiet pilsētu, reģionu vai valsti. Vispirms mērķējam turp; ja tuvumā ir lielāka līdzīga auditorija, daļa sekotāju var nākt no turienes."),
        ],
    },
    {
        "service": "followers",
        "quantity": 1000,
        "slug": "instagram/sekotaji/1000",
        "label": "{quantity} Instagram sekotāju",
        "title": "{quantity} Instagram sekotāju no īstiem cilvēkiem | Growsterr",
        "description": "Sasniedziet {quantity} Instagram sekotāju ar īstiem cilvēkiem, ne botiem. {pick_name} parasti dod {pick_audience} mēnesī, kopā ar patīk atzīmēm un komentāriem.",
        "h1": ("{quantity} Instagram sekotāju, ", "katrs no viņiem īsts."),
        "intro": "Mēs nepārdodam {quantity} botu paku. Mēs audzējam jūsu kontu ar īstiem cilvēkiem: {pick_name} parasti atnes {pick_audience} jaunu sekotāju mēnesī, tāpēc {quantity} sekotāju robeža parasti ir sasniedzama jau pirmajā mēnesī.",
        "hero": {"image": "instagram-followers-1000", "alt": "Augoša jaunu Instagram sekotāju līkne, kas sasniedz pirmo nozīmīgo robežu"},
        "sections": [
            {
                "h2": "Kāpēc ne {quantity} sekotāju stundas laikā?",
                "p": [
                    "Tāpēc, ka neviens īsts cilvēks nesāk sekot kontam dažas sekundes pēc maksājuma. Pakalpojumi, kas piegādā {quantity} sekotāju stundā, piegādā botus: tie neatzīmē „patīk”, nekomentē un pazūd viļņveidīgi.",
                    "Tie, kas paliek, nodara vēl lielāku kaitējumu. Katrs sekotājs, kurš nekad neiesaistās, samazina to jūsu auditorijas daļu, kas iesaistās, un jūsu ieraksti klusi sasniedz mazāk cilvēku.",
                ],
            },
            {
                "h2": "Jūsu pirmais tūkstotis, izdarīts pareizi",
                "p": [
                    "Pirmais tūkstotis īstu sekotāju maina to, kā jūs redz jauni apmeklētāji. Tie ir cilvēki, kas var skatīties jūsu Reels, atzīmēt jūsu ierakstus ar „patīk” un atgriezties, un tieši tas palīdz nākamajam tūkstotim jūs atrast.",
                ],
                "ul": [
                    "Īsti cilvēki, kas izvēlējās jums sekot, no jūsu izvēlētās vietas.",
                    "Patīk atzīmes un komentāri no tiem pašiem cilvēkiem, paketes ietvaros.",
                    "Pārskats, kas dienu pa dienai rāda, ko mēs izmērījām.",
                ],
            },
        ],
        "faqs": [
            ("Cik ilgā laikā var iegūt {quantity} īstu sekotāju?", "Tipiskā tempā {pick_name} atnes {pick_audience} jaunu sekotāju mēnesī, tāpēc {quantity} sekotāju robeža parasti ir sasniedzama jau pirmajā mēnesī. Īsti cilvēki seko savā tempā, tāpēc katrs mēnesis ir mazliet citāds."),
            ("Vai tā ir vienreizēja {quantity} sekotāju paka?", "Nē. Mēs pārdodam izaugsmi ikmēneša paketēs. {pick_name} maksā {pick_price} mēnesī, un atcelt varat jebkurā laikā savā kontā."),
            ("Vai kopā ar tiem saņemšu patīk atzīmes un komentārus?", "Jā, no tiem pašiem īstajiem cilvēkiem: ar {pick_name} parasti {pick_likes} patīk atzīmju un {pick_comments} komentāru mēnesī."),
            ("Kas notiek, kad {quantity} sekotāju robeža ir sasniegta?", "Jūsu pakete turpina darboties, līdz to atceļat, tāpēc izaugsme turpinās mēnesi pēc mēneša. Kad jūsu saturs būs gatavs vairāk, varat pāriet uz lielāku paketi."),
        ],
    },
]
