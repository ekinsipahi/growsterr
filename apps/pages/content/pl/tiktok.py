"""Polish TikTok pages: the hub and likes (mirrors en/tiktok.py). Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "tiktok",
        "label": "TikTok",
        "title": "Pakiety wzrostu na TikToku dla twórców | Growsterr",
        "description": "Rozwijaj TikToka z prawdziwymi ludźmi: miesięczne pakiety to nowi obserwujący, polubienia i komentarze od osób, które same Cię wybrały. Od {from_price}/mies.",
        "h1": ("Rozwijaj swojego TikToka ", "z prawdziwymi ludźmi."),
        "intro": "Miesięczne pakiety wzrostu dla twórców i influencerów. Prawdziwi ludzie odkrywają Twój profil, oglądają Twoje filmy i zaczynają Cię obserwować, gdy spodoba im się to, co widzą. Twój panel pokazuje dzień po dniu, co zmierzyliśmy.",
        "hero": {"image": "tiktok-hub", "alt": "Profil twórcy na TikToku, na który przychodzą nowi obserwujący i polubienia"},
        "sections": [
            {
                "h2": "Na TikToku liczy się uwaga",
                "p": [
                    "TikTok pokazuje film większej liczbie osób, gdy pierwsi widzowie go oglądają, lajkują, komentują i zaczynają obserwować autora. Liczby, za którymi nie stoją ludzie, niczego tu nie ruszają.",
                    "Nasze pakiety codziennie sprowadzają na Twój profil prawdziwych ludzi. Oglądają, decydują, a ci, którym podobają się Twoje filmy, obserwują i lajkują. Właśnie taka uwaga pomaga filmowi pójść dalej.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Prawdziwi widzowie oglądają filmy twórcy na TikToku"},
            },
            {
                "h2": "Dla twórców, którzy mają coś do powiedzenia",
                "p": [
                    "Komedia, gotowanie, moda czy poradniki: jeśli publikujesz regularnie, prawdziwi widzowie dają każdemu nowemu filmowi lepszy start. Zacznij od {starter_name} i przejdź wyżej, gdy przyjdzie na to pora.",
                ],
                "ul": [
                    "Ty wskazujesz miasto, region lub kraj, z którego mają pochodzić Twoi odbiorcy.",
                    "Obserwujący, polubienia i komentarze przychodzą razem, od tych samych ludzi.",
                    "Konto zostaje Twoje: nigdy nie prosimy o hasło.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Twórca nagrywa film na TikToka telefonem na statywie"},
            },
        ],
        "faqs": [
            ("Czy obserwujący to prawdziwi ludzie?", "Tak. Każdy obserwujący to prawdziwa osoba, która zobaczyła Twój profil i sama zdecydowała się Cię obserwować. Nigdy nie używamy botów, fałszywych kont ani dostarczania „natychmiast”."),
            ("Ilu obserwujących daje pakiet?", "Zwykle {starter_audience} nowych obserwujących miesięcznie w pakiecie {starter_name}, {rising_audience} w {rising_name} i {pro_audience} w {pro_name}. Typowe zakresy, a nie stała liczba: prawdziwi ludzie decydują sami."),
            ("Czy potrzebujecie mojego hasła do TikToka?", "Nigdy. Potrzebujemy tylko nazwy użytkownika. Konto powinno być publiczne, żeby osoby, które je odkryją, mogły Cię obserwować."),
            ("Czy mogę kupić same wyświetlenia albo polubienia?", "Nie. Wyświetlenia, polubienia i komentarze są w każdym pakiecie i pochodzą od tych samych prawdziwych ludzi, którzy Cię obserwują."),
            ("Czy mogę zrezygnować w dowolnym momencie?", "Tak. Pakiety odnawiają się co miesiąc, a anulujesz je na swoim koncie. Opłacony miesiąc trwa do końca."),
        ],
    },
    {
        "service": "likes",
        "slug": "tiktok/polubienia",
        "label": "Polubienia na TikToku",
        "title": "Polubienia na TikToku od prawdziwych ludzi, w każdym pakiecie",
        "description": "Polubienia na TikToku od prawdziwych ludzi, którzy oglądają Twoje filmy, nigdy od botów. Są w każdym pakiecie miesięcznym, z obserwującymi i komentarzami.",
        "h1": ("Polubienia na TikToku od prawdziwych ludzi. ", "W każdym pakiecie."),
        "intro": "Nie sprzedajemy samych polubień. Każdy pakiet sprowadza prawdziwych ludzi, którzy odkrywają Twój profil, oglądają Twoje filmy i lajkują to, co im się podoba: zwykle {starter_likes} polubień miesięcznie w pakiecie {starter_name}.",
        "hero": {"image": "tiktok-likes", "alt": "Polubienia od prawdziwych widzów pod filmem na TikToku"},
        "sections": [
            {
                "h2": "Polubienie liczy się tylko wtedy, gdy stoi za nim człowiek",
                "p": [
                    "TikTok patrzy na to, co dzieje się wokół polubienia: czy widz oglądał dalej, zaczął obserwować, wrócił? Polubienia od botów na wszystko odpowiadają „nie”, więc dodają liczbę, a odbierają zasięg.",
                    "Polubienia od prawdziwych ludzi przychodzą z resztą: czasem oglądania, obserwowaniem i komentarzami. To właśnie ten sygnał pomaga filmowi pójść dalej.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Widzowie oglądają film na TikToku do końca i go lajkują"},
            },
            {
                "h2": "Ile polubień daje każdy pakiet",
                "ul": [
                    "{starter_name} ({starter_price} miesięcznie): zwykle {starter_likes} polubień.",
                    "{rising_name} ({rising_price} miesięcznie): zwykle {rising_likes} polubień, pod wybranymi przez Ciebie filmami.",
                    "{pro_name} ({pro_price} miesięcznie): zwykle {pro_likes} polubień, z priorytetowym miejscem w kolejce.",
                ],
            },
            {
                "h2": "Dlaczego nie sprzedajemy samych polubień",
                "p": [
                    "Polubienia, które przychodzą bez wyświetleń, obserwujących i komentarzy, wyglądają dokładnie na to, czym są. W pakiecie każde polubienie pochodzi od kogoś, kto obejrzał film, więc Twoje liczby rosną razem, tak jak przy prawdziwym wzroście.",
                ],
            },
        ],
        "faqs": [
            ("Czy mogę dostać polubienia na TikToku bez pakietu?", "Nie. Polubienia, wyświetlenia i komentarze są tylko w naszych miesięcznych pakietach i pochodzą od tych samych prawdziwych ludzi. Dzięki temu pozostają naturalne."),
            ("Które filmy dostają polubienia?", "Prawdziwi ludzie lajkują to, co im się podoba, zwykle Twoje najnowsze filmy. W pakietach {rising_name} i {pro_name} możesz wybrać, które filmy dostają uwagę."),
            ("Jak szybko przychodzą polubienia?", "Po trochu każdego dnia, przez cały miesiąc. Nigdy natychmiast: natychmiastowe polubienie to bot."),
            ("Czy potrzebujecie mojego hasła do TikToka?", "Nigdy. Potrzebujemy tylko nazwy użytkownika, a konto powinno być publiczne."),
        ],
    },
]
