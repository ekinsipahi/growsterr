"""Latvian YouTube pages: the hub and subscribers (abonenti). Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "youtube",
        "label": "YouTube",
        "title": "YouTube izaugsmes paketes satura veidotājiem | Growsterr",
        "description": "Audziniet YouTube kanālu ar īstiem cilvēkiem: mēneša paketes atnes abonentus, patīk atzīmes un komentārus no skatītājiem, kas izvēlējās abonēt. No {from_price}.",
        "h1": ("Audziniet savu YouTube kanālu ", "ar īstiem skatītājiem."),
        "intro": "Vēlaties pirkt YouTube abonentus vai skatījumus? Lūk, godīgais variants: ikmēneša izaugsmes paketes satura veidotājiem. Īsti cilvēki atklāj jūsu kanālu, skatās jūsu video un abonē, ja redzētais viņiem patīk. Jūsu pārskats dienu pa dienai rāda, ko mēs izmērījām.",
        "hero": {"image": "youtube-hub", "alt": "YouTube kanāls iegūst abonentus, patīk atzīmes un komentārus no īstiem skatītājiem"},
        "sections": [
            {
                "h2": "Svarīgi ir abonenti, kas skatās",
                "p": [
                    "YouTube iesaka video, kurus cilvēki skatās, atzīmē ar „patīk” un pie kuriem atgriežas. Abonents, kurš nekad neskatās, ir sliktāks par nevienu: viņš samazina to jūsu auditorijas daļu, kas iesaistās.",
                    "Katrs abonents, ko mēs atvedam, ir cilvēks, kurš atrada jūsu kanālu un izvēlējās to abonēt. Patīk atzīmes, skatījumi un komentāri nāk no tiem pašiem cilvēkiem, jūsu paketes ietvaros.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Skatītāji skatās satura veidotāja YouTube video un raksta komentārus"},
            },
            {
                "h2": "Kanāliem, kas publicē rūpīgi",
                "p": [
                    "Pamācības, vlogi, mūzika vai spēles: ja publicējat regulāri, īsti skatītāji katram jaunam video dod labāku sākumu. Sāciet ar {starter_name} un pārejiet uz lielāku paketi, kad jūsu kanāls būs gatavs vairāk.",
                ],
                "ul": [
                    "Jūs norādāt pilsētu, reģionu vai valsti, no kuras jānāk jūsu auditorijai.",
                    "Abonenti, patīk atzīmes un komentāri nāk kopā, no tiem pašiem cilvēkiem.",
                    "Jūsu kanāls paliek jūsu: mēs nekad neprasām jūsu paroli.",
                ],
                "image": {"image": "youtube-channel", "alt": "Satura veidotājs mājas studijā montē YouTube video"},
            },
        ],
        "faqs": [
            ("Vai abonenti ir īsti cilvēki?", "Jā. Katrs abonents ir īsts cilvēks, kurš atrada jūsu kanālu un izvēlējās to abonēt. Nekādu botu, nekādu viltus kontu, nekā tūlītēja."),
            ("Cik abonentu atnes viena pakete?", "Parasti {starter_audience} jaunu abonentu mēnesī ar {starter_name}, {rising_audience} ar {rising_name} un {pro_audience} ar {pro_name}. Tipiski diapazoni, nevis fiksēts skaits."),
            ("Vai jums vajag manu Google vai YouTube paroli?", "Nekad. Mums vajag tikai jūsu kanāla identifikatoru, un kanālam jābūt publiskam."),
            ("Vai varu nopirkt skatījumus vai patīk atzīmes atsevišķi?", "Nē. Skatījumi, patīk atzīmes un komentāri ir iekļauti katrā paketē, no tiem pašiem īstajiem cilvēkiem, kas abonē jūsu kanālu."),
            ("Vai varu atcelt jebkurā laikā?", "Jā. Paketes atjaunojas katru mēnesi, un atcelt varat savā kontā. Apmaksātais mēnesis turpinās līdz beigām."),
        ],
    },
    {
        "service": "subscribers",
        "slug": "youtube/abonenti",
        "label": "YouTube abonenti",
        "title": "Pērciet īstus YouTube abonentus, kas skatās | Growsterr",
        "description": "Pērciet YouTube abonentus, kas ir īsti cilvēki: skatītāji, kuri atrada jūsu kanālu un to abonēja, ar patīk atzīmēm un komentāriem. No {from_price} mēnesī.",
        "h1": ("YouTube abonenti, ", "kas tiešām skatās."),
        "intro": "Pērciet YouTube abonentus godīgā veidā: īsti cilvēki atklāj jūsu kanālu, skatās jūsu video un abonē, ja redzētais viņiem patīk. Ar {starter_name} parasti {starter_audience} jaunu abonentu mēnesī, kā arī patīk atzīmes un komentāri no tiem pašiem skatītājiem.",
        "hero": {"image": "youtube-subscribers", "alt": "YouTube kanāla lapa ar jauniem abonentiem no īstiem skatītājiem"},
        "sections": [
            {
                "h2": "Abonentam jābūt skatītājam",
                "p": [
                    "YouTube abonents ir noderīgs tikai tad, ja viņš skatās. Īsti abonenti redz jūsu nākamo video, noskatās to, atzīmē ar „patīk” un dažreiz komentē, un tieši uz to YouTube skatās, kad izlemj, ko ieteikt.",
                    "Botu abonenti nekad neskatās. Tie liek kanālam izskatīties lielākam, kamēr tā video sasniedz mazāk cilvēku.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Īsti skatītāji abonē YouTube kanālu pēc video noskatīšanās"},
            },
            {
                "h2": "Kā izskatās viens mēnesis",
                "ul": [
                    "Pirmās dienas: jūsu kampaņa sākas, un ierodas pirmie skatītāji.",
                    "Katru nedēļu: jauni abonenti, patīk atzīmes un komentāri, mazliet katru dienu.",
                    "Līdz mēneša beigām: ar {pick_name} parasti {pick_audience} jaunu abonentu.",
                ],
            },
            {
                "h2": "No kurienes nāk jūsu skatītāji",
                "p": [
                    "Norādiet pilsētu, reģionu vai valsti, no kuras jānāk jūsu auditorijai. Vispirms mēs parādām jūsu kanālu īstiem cilvēkiem tur; ja vispiemērotākā auditorija tuvumā ir lielāka, vairāk skatītāju var nākt no turienes.",
                ],
            },
        ],
        "faqs": [
            ("Cik ātri nāk abonenti?", "Mazliet katru dienu, visa mēneša garumā. Nekad visi uzreiz: īsti cilvēki abonē savā tempā."),
            ("Vai viņi skatīsies manus video?", "Tie ir īsti cilvēki, kuri izvēlējās abonēt pēc tam, kad bija redzējuši jūsu kanālu. Ko viņi skatīsies tālāk, izlemj viņi paši, kā jebkura auditorija, un tieši tāpēc tas ir vērtīgi."),
            ("Vai saņemšu arī patīk atzīmes un komentārus?", "Jā, no tiem pašiem skatītājiem: ar {pick_name} parasti {pick_likes} patīk atzīmju un {pick_comments} komentāru mēnesī."),
            ("Vai jums vajag manu paroli?", "Nekad. Mums vajag tikai jūsu kanāla identifikatoru, un kanālam jābūt publiskam."),
        ],
    },
]
