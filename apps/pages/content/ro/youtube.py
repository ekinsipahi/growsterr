"""Romanian YouTube pages: the hub and subscribers (mirrors en/youtube.py). Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "youtube",
        "label": "YouTube",
        "title": "Pachete de creștere pe YouTube pentru creatori | Growsterr",
        "description": "Crește-ți canalul de YouTube cu oameni reali: pachete lunare cu abonați, like-uri și comentarii de la spectatori care au ales să se aboneze. De la {from_price}/lună.",
        "h1": ("Crește-ți canalul de YouTube ", "cu spectatori reali."),
        "intro": "Pachete lunare de creștere pentru creatori. Oameni reali îți descoperă canalul, se uită la videoclipurile tale și se abonează când le place ce văd. Panoul tău îți arată ce am măsurat, zi de zi.",
        "hero": {"image": "youtube-hub", "alt": "Un canal de YouTube care primește abonați, like-uri și comentarii de la spectatori reali"},
        "sections": [
            {
                "h2": "Contează abonații care se uită",
                "p": [
                    "YouTube recomandă videoclipurile la care oamenii se uită, dau like și revin. Un abonat care nu se uită niciodată e mai rău decât niciunul: scade procentul publicului tău care interacționează.",
                    "Fiecare abonat pe care îl aducem este un om care ți-a găsit canalul și a ales să se aboneze. Like-urile, vizualizările și comentariile vin de la aceiași oameni, în pachetul tău.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Spectatori care se uită la videoclipul de YouTube al unui creator și scriu comentarii"},
            },
            {
                "h2": "Pentru canalele care publică cu grijă",
                "p": [
                    "Tutoriale, vloguri, muzică sau gaming: dacă publici constant, spectatorii reali îi dau fiecărui videoclip nou un start mai bun. Începe cu {starter_name} și treci mai sus când canalul tău e pregătit pentru mai mult.",
                ],
                "ul": [
                    "Ne spui orașul, regiunea sau țara din care să vină publicul tău.",
                    "Abonații, like-urile și comentariile vin împreună, de la aceiași oameni.",
                    "Canalul rămâne al tău: nu îți cerem niciodată parola.",
                ],
                "image": {"image": "youtube-channel", "alt": "Un creator care editează un videoclip de YouTube într-un studio de acasă"},
            },
        ],
        "faqs": [
            ("Abonații sunt oameni reali?", "Da. Fiecare abonat este un om real care ți-a găsit canalul și a ales să se aboneze. Fără boți, fără conturi false, nimic instant."),
            ("Câți abonați aduce un pachet?", "De obicei {starter_audience} de abonați noi pe lună cu {starter_name}, {rising_audience} cu {rising_name} și {pro_audience} cu {pro_name}. Intervale obișnuite, nu un număr fix."),
            ("Aveți nevoie de parola mea de Google sau YouTube?", "Niciodată. Avem nevoie doar de handle-ul canalului, iar canalul tău trebuie să fie public."),
            ("Pot cumpăra separat vizualizări sau like-uri?", "Nu. Vizualizările, like-urile și comentariile vin în fiecare pachet, de la aceiași oameni reali care se abonează."),
            ("Pot anula oricând?", "Da. Pachetele se reînnoiesc lunar și poți anula din contul tău. Luna pe care ai plătit-o continuă până la capăt."),
        ],
    },
    {
        "service": "subscribers",
        "slug": "youtube/abonati",
        "label": "Abonați YouTube",
        "title": "Abonați reali pe YouTube, care se uită | Growsterr",
        "description": "Abonați pe YouTube care sunt oameni reali: spectatori care ți-au găsit canalul și au ales să se aboneze, cu like-uri și comentarii. De la {from_price} pe lună.",
        "h1": ("Abonați pe YouTube ", "care chiar se uită."),
        "intro": "Oameni reali îți descoperă canalul, se uită la videoclipurile tale și se abonează când le place ce văd. De obicei {starter_audience} de abonați noi pe lună cu {starter_name}, cu like-uri și comentarii de la aceiași spectatori.",
        "hero": {"image": "youtube-subscribers", "alt": "Pagina unui canal de YouTube cu abonați noi de la spectatori reali"},
        "sections": [
            {
                "h2": "Un abonat ar trebui să fie un spectator",
                "p": [
                    "Pe YouTube, un abonat e util doar dacă se uită. Abonații reali îți văd următorul videoclip, se uită la el, îi dau like și uneori comentează, iar la asta se uită YouTube când decide ce să recomande.",
                    "Abonații boți nu se uită niciodată. Fac un canal să pară mai mare, în timp ce videoclipurile lui ajung la mai puțini oameni.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Spectatori reali care se abonează la un canal de YouTube după ce au văzut un videoclip"},
            },
            {
                "h2": "Cum arată o lună",
                "ul": [
                    "Primele zile: campania pornește și sosesc primii spectatori.",
                    "În fiecare săptămână: abonați noi, like-uri și comentarii, câteva în fiecare zi.",
                    "La final de lună: de obicei {pick_audience} de abonați noi cu {pick_name}.",
                ],
            },
            {
                "h2": "De unde vin spectatorii tăi",
                "p": [
                    "Spune-ne orașul, regiunea sau țara din care să vină publicul tău. Îți arătăm canalul mai întâi oamenilor reali de acolo; unde publicul cel mai potrivit e mai mare, mai mulți pot veni din zonele apropiate.",
                ],
            },
        ],
        "faqs": [
            ("Cât de repede vin abonații?", "Câte puțin în fiecare zi, pe parcursul întregii luni. Niciodată toți deodată: oamenii reali se abonează în ritmul lor."),
            ("Se vor uita la videoclipurile mele?", "Sunt oameni reali care au ales să se aboneze după ce ți-au văzut canalul. La ce se uită mai departe depinde de ei, ca la orice public, și tocmai de aceea contează."),
            ("Primesc și like-uri și comentarii?", "Da, de la aceiași spectatori: de obicei {pick_likes} de like-uri și {pick_comments} de comentarii pe lună cu {pick_name}."),
            ("Aveți nevoie de parola mea?", "Niciodată. Avem nevoie doar de handle-ul canalului, iar canalul tău trebuie să fie public."),
        ],
    },
]
