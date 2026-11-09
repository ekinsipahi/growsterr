"""Latvian TikTok pages: the hub and likes (patīk atzīmes). Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "tiktok",
        "label": "TikTok",
        "title": "TikTok izaugsmes paketes satura veidotājiem | Growsterr",
        "description": "Augiet TikTokā ar īstiem cilvēkiem: mēneša paketes atnes sekotājus, patīk atzīmes un komentārus no tiem, kas izvēlējās jums sekot. No {from_price} mēnesī.",
        "h1": ("Augiet TikTokā ", "ar īstiem cilvēkiem."),
        "intro": "Vēlaties pirkt TikTok sekotājus, patīk atzīmes vai skatījumus? Lūk, ko mēs piedāvājam botu vietā: ikmēneša izaugsmes paketes satura veidotājiem un influenceriem. Īsti cilvēki atklāj jūsu profilu, skatās jūsu video un seko jums, ja redzētais viņiem patīk. Jūsu pārskats dienu pa dienai rāda, ko mēs izmērījām.",
        "hero": {"image": "tiktok-hub", "alt": "TikTok satura veidotāja profils, kurā ienāk jauni sekotāji un patīk atzīmes"},
        "sections": [
            {
                "h2": "TikTokā uzmanība ir viss",
                "p": [
                    "TikTok rāda video vairāk cilvēkiem, ja tā pirmie skatītāji to noskatās, atzīmē ar „patīk”, komentē un sāk sekot. Skaitļi bez cilvēkiem aiz tiem neko no tā neietekmē.",
                    "Mūsu paketes katru dienu atved uz jūsu profilu īstus cilvēkus. Viņi skatās, izlemj, un tie, kam jūsu video patīk, seko un atzīmē „patīk”. Tieši šāda uzmanība palīdz video izplatīties.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Īsti skatītāji skatās satura veidotāja TikTok video"},
            },
            {
                "h2": "Satura veidotājiem, kam ir ko teikt",
                "p": [
                    "Komēdija, ēdiena gatavošana, mode vai pamācības: ja publicējat regulāri, īsti skatītāji katram jaunam video dod labāku sākumu. Sāciet ar {starter_name} un pārejiet uz lielāku paketi, kad būsiet gatavi.",
                ],
                "ul": [
                    "Jūs norādāt pilsētu, reģionu vai valsti, no kuras jānāk jūsu auditorijai.",
                    "Sekotāji, patīk atzīmes un komentāri nāk kopā, no tiem pašiem cilvēkiem.",
                    "Jūsu konts paliek jūsu: mēs nekad neprasām jūsu paroli.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Satura veidotājs filmē TikTok video ar telefonu uz statīva"},
            },
        ],
        "faqs": [
            ("Vai sekotāji ir īsti cilvēki?", "Jā. Katrs sekotājs ir īsts cilvēks, kurš redzēja jūsu profilu un izvēlējās jums sekot. Mēs nekad neizmantojam botus, viltus kontus vai tūlītēju piegādi."),
            ("Cik sekotāju atnes viena pakete?", "Parasti {starter_audience} jaunu sekotāju mēnesī ar {starter_name}, {rising_audience} ar {rising_name} un {pro_audience} ar {pro_name}. Tipiski diapazoni, nevis fiksēts skaits: īsti cilvēki izlemj paši."),
            ("Vai jums vajag manu TikTok paroli?", "Nekad. Mums vajag tikai jūsu lietotājvārdu. Turiet kontu publisku, lai cilvēki, kuri to atklāj, varētu jums sekot."),
            ("Vai varu nopirkt skatījumus vai patīk atzīmes atsevišķi?", "Nē. Skatījumi, patīk atzīmes un komentāri ir iekļauti katrā paketē, no tiem pašiem īstajiem cilvēkiem, kas jums seko."),
            ("Vai varu atcelt jebkurā laikā?", "Jā. Paketes atjaunojas katru mēnesi, un atcelt varat savā kontā. Apmaksātais mēnesis turpinās līdz beigām."),
        ],
    },
    {
        "service": "likes",
        "slug": "tiktok/patik-atzimes",
        "label": "TikTok patīk atzīmes",
        "title": "Pērciet TikTok patīk atzīmes no īstiem cilvēkiem | Growsterr",
        "description": "TikTok patīk atzīmes no īstiem cilvēkiem, kas skatās jūsu video. Tās ir katrā mēneša paketē kopā ar sekotājiem un komentāriem. No {from_price} mēnesī.",
        "h1": ("TikTok patīk atzīmes no īstiem cilvēkiem. ", "Katrā paketē."),
        "intro": "Domājat pirkt TikTok patīk atzīmes? Mēs tās nepārdodam atsevišķi. Katra pakete atved īstus cilvēkus, kas atklāj jūsu profilu, skatās jūsu video un novērtē to, kas viņiem iepatīkas: ar {starter_name} parasti {starter_likes} patīk atzīmju mēnesī.",
        "hero": {"image": "tiktok-likes", "alt": "Īstu skatītāju patīk atzīmes paceļas no TikTok video"},
        "sections": [
            {
                "h2": "Kāpēc patīk atzīme ir vērtīga tikai tad, ja aiz tās ir cilvēks",
                "p": [
                    "TikTok vēro, kas notiek ap patīk atzīmi: vai skatītājs turpināja skatīties, sāka sekot, atgriezās? Botu patīk atzīmes uz visu atbild ar „nē”, tāpēc tās pievieno skaitli un atņem sasniedzamību.",
                    "Īstu cilvēku patīk atzīmes nāk kopā ar visu pārējo: skatīšanās laiku, sekojumiem un komentāriem. Tas ir signāls, kas palīdz video izplatīties.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Skatītāji noskatās TikTok video līdz galam un atzīmē to ar „patīk”"},
            },
            {
                "h2": "Cik patīk atzīmju atnes katra pakete",
                "ul": [
                    "{starter_name} ({starter_price} mēnesī): parasti {starter_likes} patīk atzīmju.",
                    "{rising_name} ({rising_price} mēnesī): parasti {rising_likes} patīk atzīmju, jūsu izvēlētajiem video.",
                    "{pro_name} ({pro_price} mēnesī): parasti {pro_likes} patīk atzīmju, ar prioritāru izvietošanu.",
                ],
            },
            {
                "h2": "Kāpēc mēs nepārdodam patīk atzīmes atsevišķi",
                "p": [
                    "Patīk atzīmes, kas ienāk bez skatījumiem, sekojumiem vai komentāriem, izskatās tieši tādas, kādas tās ir. Paketē katra patīk atzīme nāk no kāda, kurš skatījās, tāpēc jūsu skaitļi kustas kopā, kā tas notiek īstā izaugsmē.",
                ],
            },
        ],
        "faqs": [
            ("Vai TikTok patīk atzīmes var saņemt bez paketes?", "Nē. Patīk atzīmes, skatījumi un komentāri nāk tikai mūsu mēneša paketēs, no tiem pašiem īstajiem cilvēkiem. Tieši tas tos saglabā dabiskus."),
            ("Kuri video saņem patīk atzīmes?", "Īsti cilvēki novērtē to, kas viņiem patīk, parasti jūsu jaunākos video. Ar {rising_name} un {pro_name} jūs varat izvēlēties, kuri video saņem uzmanību."),
            ("Cik ātri nāk patīk atzīmes?", "Mazliet katru dienu, visa mēneša garumā. Nekad acumirklī: tūlītēja patīk atzīme ir bots."),
            ("Vai jums vajag manu TikTok paroli?", "Nekad. Mums vajag tikai jūsu lietotājvārdu, un kontam jābūt publiskam."),
        ],
    },
]
