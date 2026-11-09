"""Polish YouTube pages: the hub and subscribers (mirrors en/youtube.py). Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "youtube",
        "label": "YouTube",
        "title": "Pakiety wzrostu na YouTube dla twórców | Growsterr",
        "description": "Rozwijaj kanał na YouTube z prawdziwymi ludźmi: miesięczne pakiety to subskrybenci, polubienia i komentarze od widzów, którzy sami Cię wybrali. Od {from_price}/mies.",
        "h1": ("Rozwijaj kanał na YouTube ", "z prawdziwymi widzami."),
        "intro": "Miesięczne pakiety wzrostu dla twórców. Prawdziwi ludzie odkrywają Twój kanał, oglądają Twoje filmy i subskrybują, gdy spodoba im się to, co widzą. Twój panel pokazuje dzień po dniu, co zmierzyliśmy.",
        "hero": {"image": "youtube-hub", "alt": "Kanał na YouTube zyskuje subskrybentów, polubienia i komentarze od prawdziwych widzów"},
        "sections": [
            {
                "h2": "Liczą się subskrybenci, którzy oglądają",
                "p": [
                    "YouTube poleca filmy, które ludzie oglądają, lajkują i do których wracają. Subskrybent, który nigdy nie ogląda, jest gorszy niż żaden: obniża odsetek widzów, którzy reagują.",
                    "Każdy subskrybent, którego sprowadzamy, to osoba, która znalazła Twój kanał i sama zdecydowała się go subskrybować. Polubienia, wyświetlenia i komentarze pochodzą od tych samych ludzi, w ramach Twojego pakietu.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Widzowie oglądają film twórcy na YouTube i piszą komentarze"},
            },
            {
                "h2": "Dla kanałów, które dbają o każdy film",
                "p": [
                    "Poradniki, vlogi, muzyka czy gry: jeśli publikujesz regularnie, prawdziwi widzowie dają każdemu nowemu filmowi lepszy start. Zacznij od {starter_name} i przejdź wyżej, gdy Twój kanał będzie gotowy na więcej.",
                ],
                "ul": [
                    "Ty wskazujesz miasto, region lub kraj, z którego mają pochodzić Twoi widzowie.",
                    "Subskrybenci, polubienia i komentarze przychodzą razem, od tych samych ludzi.",
                    "Kanał zostaje Twój: nigdy nie prosimy o hasło.",
                ],
                "image": {"image": "youtube-channel", "alt": "Twórca montuje film na YouTube w domowym studiu"},
            },
        ],
        "faqs": [
            ("Czy subskrybenci to prawdziwi ludzie?", "Tak. Każdy subskrybent to prawdziwa osoba, która znalazła Twój kanał i sama zdecydowała się go subskrybować. Żadnych botów, żadnych fałszywych kont, nic „natychmiast”."),
            ("Ilu subskrybentów daje pakiet?", "Zwykle {starter_audience} nowych subskrybentów miesięcznie w pakiecie {starter_name}, {rising_audience} w {rising_name} i {pro_audience} w {pro_name}. Typowe zakresy, a nie stała liczba."),
            ("Czy potrzebujecie mojego hasła do Google lub YouTube?", "Nigdy. Potrzebujemy tylko identyfikatora kanału (@handle), a kanał powinien być publiczny."),
            ("Czy mogę kupić same wyświetlenia albo polubienia?", "Nie. Wyświetlenia, polubienia i komentarze są w każdym pakiecie i pochodzą od tych samych prawdziwych ludzi, którzy subskrybują Twój kanał."),
            ("Czy mogę zrezygnować w dowolnym momencie?", "Tak. Pakiety odnawiają się co miesiąc, a anulujesz je na swoim koncie. Opłacony miesiąc trwa do końca."),
        ],
    },
    {
        "service": "subscribers",
        "slug": "youtube/subskrybenci",
        "label": "Subskrybenci na YouTube",
        "title": "Prawdziwi subskrybenci YouTube, którzy oglądają | Growsterr",
        "description": "Subskrybenci na YouTube, czyli prawdziwi widzowie, którzy znaleźli Twój kanał i sami go subskrybowali, plus polubienia i komentarze. Od {from_price}/mies.",
        "h1": ("Subskrybenci na YouTube, ", "którzy naprawdę oglądają."),
        "intro": "Prawdziwi ludzie odkrywają Twój kanał, oglądają Twoje filmy i subskrybują, gdy spodoba im się to, co widzą. Zwykle {starter_audience} nowych subskrybentów miesięcznie w pakiecie {starter_name}, z polubieniami i komentarzami od tych samych widzów.",
        "hero": {"image": "youtube-subscribers", "alt": "Strona kanału na YouTube z nowymi subskrybentami: prawdziwymi widzami"},
        "sections": [
            {
                "h2": "Subskrybent powinien być widzem",
                "p": [
                    "Na YouTube subskrybent ma sens tylko wtedy, gdy ogląda. Prawdziwi subskrybenci widzą Twój kolejny film, oglądają go, lajkują i czasem komentują, a właśnie na to patrzy YouTube, gdy decyduje, co polecić.",
                    "Subskrybenci-boty nigdy nie oglądają. Sprawiają, że kanał wygląda na większy, a jego filmy docierają do mniejszej liczby osób.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Prawdziwi widzowie subskrybują kanał na YouTube po obejrzeniu filmu"},
            },
            {
                "h2": "Jak wygląda miesiąc",
                "ul": [
                    "Pierwsze dni: kampania rusza i pojawiają się pierwsi widzowie.",
                    "Każdy tydzień: nowi subskrybenci, polubienia i komentarze, po trochu każdego dnia.",
                    "Koniec miesiąca: zwykle {pick_audience} nowych subskrybentów w pakiecie {pick_name}.",
                ],
            },
            {
                "h2": "Skąd przychodzą Twoi widzowie",
                "p": [
                    "Podaj miasto, region lub kraj, z którego mają pochodzić Twoi odbiorcy. Najpierw pokazujemy Twój kanał prawdziwym ludziom właśnie tam; jeśli najlepiej dopasowana publiczność jest większa w pobliżu, więcej osób może przyjść stamtąd.",
                ],
            },
        ],
        "faqs": [
            ("Jak szybko przybywa subskrybentów?", "Po trochu każdego dnia, przez cały miesiąc. Nigdy wszystko naraz: prawdziwi ludzie subskrybują we własnym tempie."),
            ("Czy będą oglądać moje filmy?", "To prawdziwi ludzie, którzy zdecydowali się subskrybować po obejrzeniu Twojego kanału. Co obejrzą dalej, zależy od nich, jak w przypadku każdej publiczności, i właśnie dlatego to się liczy."),
            ("Czy dostanę też polubienia i komentarze?", "Tak, od tych samych widzów: zwykle {pick_likes} polubień i {pick_comments} komentarzy miesięcznie w pakiecie {pick_name}."),
            ("Czy potrzebujecie mojego hasła?", "Nigdy. Potrzebujemy tylko identyfikatora kanału (@handle), a kanał powinien być publiczny."),
        ],
    },
]
