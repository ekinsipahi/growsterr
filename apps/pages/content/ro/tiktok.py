"""Romanian TikTok pages: the hub and likes (mirrors en/tiktok.py). Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "tiktok",
        "label": "TikTok",
        "title": "Pachete de creștere pe TikTok pentru creatori | Growsterr",
        "description": "Crește pe TikTok cu oameni reali: pachete lunare cu urmăritori noi, like-uri și comentarii de la oameni care au ales să te urmărească. De la {from_price} pe lună.",
        "h1": ("Crește-ți contul de TikTok ", "cu oameni reali."),
        "intro": "Pachete lunare de creștere pentru creatori și influenceri. Oameni reali îți descoperă profilul, se uită la videoclipurile tale și te urmăresc când le place ce văd. Panoul tău îți arată ce am măsurat, zi de zi.",
        "hero": {"image": "tiktok-hub", "alt": "Profilul de TikTok al unui creator, cu urmăritori noi și like-uri care sosesc"},
        "sections": [
            {
                "h2": "Pe TikTok, atenția este totul",
                "p": [
                    "TikTok arată un videoclip mai multor oameni atunci când primii spectatori se uită, dau like, comentează și urmăresc contul. Cifrele fără oameni în spate nu mișcă nimic din toate astea.",
                    "Pachetele noastre aduc zilnic oameni reali pe profilul tău. Se uită, decid, iar cei cărora le plac videoclipurile tale te urmăresc și dau like. Este genul de atenție care ajută un videoclip să ajungă departe.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Spectatori reali care se uită la videoclipurile de TikTok ale unui creator"},
            },
            {
                "h2": "Pentru creatorii care au ceva de spus",
                "p": [
                    "Comedie, gătit, modă sau tutoriale: dacă postezi constant, spectatorii reali îi dau fiecărui videoclip nou un start mai bun. Începe cu {starter_name} și treci mai sus când ești pregătit.",
                ],
                "ul": [
                    "Ne spui orașul, regiunea sau țara din care să vină publicul tău.",
                    "Urmăritorii, like-urile și comentariile vin împreună, de la aceiași oameni.",
                    "Contul rămâne al tău: nu îți cerem niciodată parola.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Un creator care filmează un videoclip de TikTok cu telefonul pe un trepied"},
            },
        ],
        "faqs": [
            ("Urmăritorii sunt oameni reali?", "Da. Fiecare urmăritor este un om real care ți-a văzut profilul și a ales să te urmărească. Nu folosim niciodată boți, conturi false sau livrare instant."),
            ("Câți urmăritori aduce un pachet?", "De obicei {starter_audience} de urmăritori noi pe lună cu {starter_name}, {rising_audience} cu {rising_name} și {pro_audience} cu {pro_name}. Intervale obișnuite, nu un număr fix: oamenii reali decid singuri."),
            ("Aveți nevoie de parola mea de TikTok?", "Niciodată. Avem nevoie doar de numele tău de utilizator. Păstrează contul public, ca oamenii care îl descoperă să te poată urmări."),
            ("Pot cumpăra separat vizualizări sau like-uri?", "Nu. Vizualizările, like-urile și comentariile vin în fiecare pachet, de la aceiași oameni reali care te urmăresc."),
            ("Pot anula oricând?", "Da. Pachetele se reînnoiesc lunar și poți anula din contul tău. Luna pe care ai plătit-o continuă până la capăt."),
        ],
    },
    {
        "service": "likes",
        "slug": "tiktok/like-uri",
        "label": "Like-uri TikTok",
        "title": "Like-uri TikTok de la oameni reali, în fiecare pachet",
        "description": "Like-uri pe TikTok de la oameni reali care se uită la videoclipurile tale, niciodată boți. Vin în fiecare pachet lunar, cu urmăritori și comentarii.",
        "h1": ("Like-uri pe TikTok de la oameni reali. ", "În fiecare pachet."),
        "intro": "Nu vindem like-uri separat. Fiecare pachet aduce oameni reali care îți descoperă profilul, se uită la videoclipurile tale și dau like la ce le place: de obicei {starter_likes} de like-uri pe lună cu {starter_name}.",
        "hero": {"image": "tiktok-likes", "alt": "Like-uri de la spectatori reali care se ridică deasupra unui videoclip de TikTok"},
        "sections": [
            {
                "h2": "De ce un like contează doar cu un om în spate",
                "p": [
                    "TikTok observă ce se întâmplă în jurul unui like: spectatorul a continuat să se uite, a urmărit contul, a revenit? Like-urile de la boți răspund „nu” la toate, așa că adaugă un număr și iau din acoperire.",
                    "Like-urile de la oameni reali vin cu tot restul: timp de vizionare, urmăriri și comentarii. Acesta este semnalul care ajută un videoclip să ajungă departe.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Spectatori care se uită la un videoclip de TikTok până la capăt și îi dau like"},
            },
            {
                "h2": "Câte like-uri aduce fiecare pachet",
                "ul": [
                    "{starter_name} ({starter_price} pe lună): de obicei {starter_likes} de like-uri.",
                    "{rising_name} ({rising_price} pe lună): de obicei {rising_likes} de like-uri, la videoclipurile pe care le alegi.",
                    "{pro_name} ({pro_price} pe lună): de obicei {pro_likes} de like-uri, cu prioritate la afișare.",
                ],
            },
            {
                "h2": "De ce nu vindem like-uri separat",
                "p": [
                    "Like-urile care vin fără vizualizări, urmăriri sau comentarii arată exact a ceea ce sunt. Într-un pachet, fiecare like vine de la cineva care s-a uitat, așa că cifrele tale cresc împreună, cum se întâmplă la o creștere reală.",
                ],
            },
        ],
        "faqs": [
            ("Pot primi like-uri pe TikTok fără un pachet?", "Nu. Like-urile, vizualizările și comentariile vin doar în pachetele noastre lunare, de la aceiași oameni reali. Așa rămân naturale."),
            ("Ce videoclipuri primesc like-urile?", "Oamenii reali dau like la ce le place, de obicei la cele mai noi videoclipuri ale tale. Cu {rising_name} și {pro_name} poți alege ce videoclipuri primesc atenția."),
            ("Cât de repede vin like-urile?", "Câte puțin în fiecare zi, pe parcursul lunii. Niciodată instant: un like instant vine de la un bot."),
            ("Aveți nevoie de parola mea de TikTok?", "Niciodată. Avem nevoie doar de numele tău de utilizator, iar contul tău trebuie să fie public."),
        ],
    },
]
