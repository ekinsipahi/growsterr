"""Romanian Instagram pages: the hub, followers, and the 1,000-followers goal (mirrors en/instagram.py).
Keys and placeholders: docs/CONTENT.md. Romanian puts "de" between a number of 20 or more and its noun."""

UPDATED = "2026-11-08"

PAGES = [
    {
        # The hub: no service.
        "slug": "instagram",
        "label": "Instagram",
        "title": "Pachete de creștere pe Instagram pentru creatori | Growsterr",
        "description": "Crește pe Instagram cu oameni reali: pachete lunare cu urmăritori noi, like-uri și comentarii de la oameni care te-au ales. De la {from_price} pe lună.",
        "h1": ("Crește-ți contul de Instagram ", "cu oameni reali."),
        "intro": "Pachete lunare de creștere pentru creatori și influenceri. Îți arătăm profilul unor oameni reali, iar cei cărora le place ce văd te urmăresc, dau like și comentează. Panoul tău îți arată ce am măsurat, zi de zi.",
        "hero": {"image": "instagram-hub", "alt": "Profilul de Instagram al unui creator, cu urmăritori noi, like-uri și comentarii care sosesc"},
        "sections": [
            {
                "h2": "Creștere care arată că ai muncit pentru ea",
                "p": [
                    "Instagram răsplătește conturile cu care oamenii chiar interacționează. Boții fac exact opusul: stau în numărul tău de urmăritori, nu dau niciodată like, nu se uită niciodată și învață algoritmul că postările tale nu merită arătate.",
                    "Noi lucrăm invers. Profilul tău le este arătat zilnic unor oameni reali, iar fiecare urmărire este alegerea cuiva. De aceea like-urile, vizualizările și comentariile vin odată cu urmăritorii, nu ca o achiziție separată.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Oameni reali care descoperă postările de Instagram ale unui creator și lasă comentarii"},
            },
            {
                "h2": "Pentru creatorii care postează cu un scop",
                "p": [
                    "Brand personal, pagină de nișă sau afacere mică: pachetele cresc odată cu tine. Începe cu {starter_name} și treci la un pachet mai mare când conținutul tău e pregătit pentru mai mult.",
                ],
                "ul": [
                    "Reels, caruseluri și postări foto: toate au de câștigat.",
                    "Ne spui orașul, regiunea sau țara din care să vină publicul tău.",
                    "Contul rămâne al tău: nu îți cerem niciodată parola.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "Un creator care își plănuiește conținutul de Instagram la birou"},
            },
        ],
        "faqs": [
            ("Urmăritorii sunt oameni reali?", "Da. Fiecare urmăritor este un om real care ți-a văzut profilul și a ales să te urmărească. Nu folosim niciodată boți, profiluri false sau livrare instant."),
            ("Câți urmăritori aduce un pachet?", "De obicei {starter_audience} de urmăritori noi pe lună cu {starter_name}, {rising_audience} cu {rising_name} și {pro_audience} cu {pro_name}. Sunt intervale obișnuite, nu un număr fix: oamenii reali decid singuri."),
            ("Aveți nevoie de parola mea de Instagram?", "Niciodată. Avem nevoie doar de numele tău de utilizator. Păstrează contul public, ca oamenii care îl descoperă să te poată urmări."),
            ("Pot cumpăra separat like-uri sau comentarii?", "Nu. Like-urile, vizualizările și comentariile vin în fiecare pachet, de la aceiași oameni reali care te urmăresc. Așa cifrele tale rămân naturale."),
            ("Pot anula oricând?", "Da. Pachetele se reînnoiesc lunar și poți anula din contul tău. Luna pe care ai plătit-o continuă până la capăt."),
        ],
    },
    {
        "service": "followers",
        "slug": "instagram/urmaritori",
        "label": "Urmăritori Instagram",
        "title": "Urmăritori reali pe Instagram, în fiecare lună | Growsterr",
        "description": "Urmăritori pe Instagram care sunt oameni reali și au ales să te urmărească, cu like-uri și comentarii de la aceiași oameni. Pachete lunare de la {from_price}.",
        "h1": ("Urmăritori pe Instagram ", "care au ales să te urmărească."),
        "intro": "Oameni reali îți descoperă profilul în fiecare zi, iar cei cărora le place ce văd te urmăresc. De obicei {starter_audience} de urmăritori noi pe lună cu {starter_name}, cu like-uri și comentarii de la aceiași oameni.",
        "hero": {"image": "instagram-followers", "alt": "Un profil de Instagram care primește urmăritori noi de la oameni reali"},
        "sections": [
            {
                "h2": "De ce valorează mai mult urmăritorii reali",
                "p": [
                    "Un urmăritor contează doar dacă în spatele lui e un om. Urmăritorii reali îți văd următoarea postare, îi dau like, o comentează și o distribuie, iar la interacțiunea asta se uită Instagram când decide cui să-ți mai arate conținutul.",
                    "Boții nu pot face nimic din toate astea. Umflă un număr câteva zile, dispar la următoarea curățenie, iar cei care rămân îți trag acoperirea în jos, pe tăcute.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Oameni reali care dau like și comentează la postarea de Instagram a unui creator"},
            },
            {
                "h2": "De unde vin noii tăi urmăritori",
                "p": [
                    "Spune-ne orașul, regiunea sau țara din care să vină publicul tău. Îți arătăm profilul mai întâi oamenilor reali de acolo; unde publicul cel mai potrivit e mai mare, mai mulți pot veni din zonele apropiate.",
                ],
            },
            {
                "h2": "Cum arată o lună",
                "ul": [
                    "Primele zile: campania pornește și sosesc primele vizite.",
                    "În fiecare săptămână: urmăritori noi, like-uri și comentarii, câteva în fiecare zi.",
                    "La final de lună: de obicei {pick_audience} de urmăritori noi cu {pick_name}.",
                ],
            },
        ],
        "faqs": [
            ("Cât de repede vin urmăritorii?", "Câte puțin în fiecare zi, pe parcursul întregii luni. Niciodată toți deodată: oamenii reali urmăresc în ritmul lor, iar orice vine instant e un bot."),
            ("Pot noii urmăritori să renunțe să mă urmărească?", "Unii pot, așa cum se schimbă orice public real. Urmăritorii reali rămân mult mai des decât boții, care dispar în valuri."),
            ("Primesc și like-uri și comentarii?", "Da, de la aceiași oameni: de obicei {pick_likes} de like-uri și {pick_comments} de comentarii pe lună cu {pick_name}."),
            ("Este sigur pentru contul meu?", "Nu îți cerem niciodată parola și nu intrăm niciodată în contul tău. Oamenii îți găsesc profilul și decid singuri, exact cum te găsește orice urmăritor."),
            ("Pot alege de unde sunt urmăritorii?", "Da. Spune-ne orașul, regiunea sau țara când comanzi. Țintim mai întâi acolo; când în apropiere există un public foarte potrivit și mai mare, unii urmăritori pot veni de acolo."),
        ],
    },
    {
        "service": "followers",
        "quantity": 1000,
        "slug": "instagram/urmaritori/1000",
        "label": "{quantity} de urmăritori Instagram",
        "title": "{quantity} de urmăritori Instagram, oameni reali | Growsterr",
        "description": "Ajungi la {quantity} de urmăritori pe Instagram cu oameni reali, nu boți. {pick_name} aduce de obicei {pick_audience} pe lună, plus like-uri și comentarii.",
        "h1": ("{quantity} de urmăritori pe Instagram, ", "fiecare dintre ei, un om real."),
        "intro": "Nu vindem un pachet de {quantity} de boți. Îți creștem contul cu oameni reali: {pick_name} aduce de obicei {pick_audience} de urmăritori noi pe lună, așa că pragul de {quantity} e de obicei la îndemână încă din prima lună.",
        "hero": {"image": "instagram-followers-1000", "alt": "O linie ascendentă de urmăritori noi pe Instagram care atinge un prim prag"},
        "sections": [
            {
                "h2": "De ce nu {quantity} de urmăritori într-o oră?",
                "p": [
                    "Pentru că niciun om real nu urmărește un cont la câteva secunde după o plată. Serviciile care livrează {quantity} de urmăritori într-o oră livrează boți: nu dau like, nu comentează și dispar în valuri.",
                    "Cei care rămân fac și mai mult rău. Fiecare urmăritor care nu interacționează niciodată scade procentul publicului tău care o face, iar postările tale ajung, pe tăcute, la mai puțini oameni.",
                ],
            },
            {
                "h2": "Prima ta mie, făcută cum trebuie",
                "p": [
                    "O primă mie de urmăritori reali schimbă felul în care te văd vizitatorii noi. Sunt oameni care s-ar putea uita la Reels-urile tale, ar putea da like postărilor și ar putea reveni, exact ce ajută următoarea mie să te găsească.",
                ],
                "ul": [
                    "Oameni reali care au ales să te urmărească, din locația pe care o alegi.",
                    "Like-uri și comentarii de la aceiași oameni, incluse în pachet.",
                    "Un panou care îți arată ce am măsurat, zi de zi.",
                ],
            },
        ],
        "faqs": [
            ("Cât durează până la {quantity} de urmăritori reali?", "Într-un ritm obișnuit, {pick_name} aduce {pick_audience} de urmăritori noi pe lună, așa că pragul de {quantity} e de obicei la îndemână în prima lună. Oamenii reali urmăresc în ritmul lor, deci fiecare lună e puțin diferită."),
            ("E un pachet unic de {quantity} de urmăritori?", "Nu. Vindem creșterea sub formă de pachete lunare. {pick_name} costă {pick_price} pe lună și poți anula oricând din contul tău."),
            ("Primesc și like-uri și comentarii odată cu ei?", "Da, de la aceiași oameni reali: de obicei {pick_likes} de like-uri și {pick_comments} de comentarii pe lună cu {pick_name}."),
            ("Ce se întâmplă după {quantity}?", "Pachetul tău continuă până când îl anulezi, așa că creșterea merge mai departe lună de lună. Când conținutul tău e pregătit pentru mai mult, poți trece la un pachet mai mare."),
        ],
    },
]
