"""Polish Instagram pages: the hub, followers, and the 1,000-followers goal (mirrors en/instagram.py).
Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-08"

PAGES = [
    {
        # The hub: no service.
        "slug": "instagram",
        "label": "Instagram",
        "title": "Pakiety wzrostu na Instagramie dla twórców | Growsterr",
        "description": "Rozwijaj Instagram z prawdziwymi ludźmi: miesięczne pakiety to nowi obserwujący, polubienia i komentarze od osób, które same Cię wybrały. Od {from_price}/mies.",
        "h1": ("Rozwijaj swój Instagram ", "z prawdziwymi ludźmi."),
        "intro": "Miesięczne pakiety wzrostu dla twórców i influencerów. Pokazujemy Twój profil prawdziwym ludziom, a ci, którym spodoba się to, co zobaczą, obserwują, lajkują i komentują. Twój panel pokazuje dzień po dniu, co zmierzyliśmy.",
        "hero": {"image": "instagram-hub", "alt": "Profil twórcy na Instagramie, na który przychodzą nowi obserwujący, polubienia i komentarze"},
        "sections": [
            {
                "h2": "Wzrost, który wygląda naturalnie, bo taki jest",
                "p": [
                    "Instagram nagradza konta, z którymi ludzie naprawdę wchodzą w interakcje. Boty działają odwrotnie: siedzą w liczbie obserwujących, nigdy nie lajkują, nic nie oglądają i uczą algorytm, że Twoich postów nie warto pokazywać.",
                    "My działamy na odwrót. Codziennie pokazujemy Twój profil prawdziwym ludziom, a każde obserwowanie to czyjś wybór. Dlatego polubienia, wyświetlenia i komentarze przychodzą razem z obserwującymi, a nie jako osobny zakup.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Prawdziwi ludzie odkrywają posty twórcy na Instagramie i zostawiają komentarze"},
            },
            {
                "h2": "Dla twórców, którzy publikują z pomysłem",
                "p": [
                    "Marka osobista, profil tematyczny czy mała firma: pakiety rosną razem z Tobą. Zacznij od {starter_name} i przejdź wyżej, gdy Twoje treści będą gotowe na więcej.",
                ],
                "ul": [
                    "Korzystają na tym rolki, karuzele i zdjęcia.",
                    "Ty wskazujesz miasto, region lub kraj, z którego mają pochodzić Twoi odbiorcy.",
                    "Konto zostaje Twoje: nigdy nie prosimy o hasło.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "Twórca planuje treści na Instagram przy biurku"},
            },
        ],
        "faqs": [
            ("Czy obserwujący to prawdziwi ludzie?", "Tak. Każdy obserwujący to prawdziwa osoba, która zobaczyła Twój profil i sama zdecydowała się Cię obserwować. Nigdy nie używamy botów, fałszywych profili ani dostarczania „natychmiast”."),
            ("Ilu obserwujących daje pakiet?", "Zwykle {starter_audience} nowych obserwujących miesięcznie w pakiecie {starter_name}, {rising_audience} w {rising_name} i {pro_audience} w {pro_name}. To typowe zakresy, a nie stała liczba: prawdziwi ludzie decydują sami."),
            ("Czy potrzebujecie mojego hasła do Instagrama?", "Nigdy. Potrzebujemy tylko nazwy użytkownika. Konto powinno być publiczne, żeby osoby, które je odkryją, mogły Cię obserwować."),
            ("Czy mogę kupić same polubienia albo komentarze?", "Nie. Polubienia, wyświetlenia i komentarze są w każdym pakiecie i pochodzą od tych samych prawdziwych ludzi, którzy Cię obserwują. Dzięki temu Twoje liczby pozostają naturalne."),
            ("Czy mogę zrezygnować w dowolnym momencie?", "Tak. Pakiety odnawiają się co miesiąc, a anulujesz je na swoim koncie. Opłacony miesiąc trwa do końca."),
        ],
    },
    {
        "service": "followers",
        "slug": "instagram/obserwujacy",
        "label": "Obserwujący na Instagramie",
        "title": "Prawdziwi obserwujący na Instagramie co miesiąc | Growsterr",
        "description": "Obserwujący na Instagramie, którzy są prawdziwymi ludźmi i sami Cię wybrali, plus polubienia i komentarze od tych samych osób. Pakiety od {from_price}/mies.",
        "h1": ("Obserwujący na Instagramie, ", "którzy sami Cię wybrali."),
        "intro": "Prawdziwi ludzie codziennie odkrywają Twój profil, a ci, którym spodoba się to, co zobaczą, zaczynają Cię obserwować. Zwykle {starter_audience} nowych obserwujących miesięcznie w pakiecie {starter_name}, razem z polubieniami i komentarzami od tych samych osób.",
        "hero": {"image": "instagram-followers", "alt": "Profil na Instagramie zyskuje nowych obserwujących: prawdziwych ludzi"},
        "sections": [
            {
                "h2": "Dlaczego prawdziwi obserwujący są więcej warci",
                "p": [
                    "Obserwujący liczy się tylko wtedy, gdy stoi za nim człowiek. Prawdziwi obserwujący widzą Twój kolejny post, lajkują go, komentują i udostępniają, a właśnie na to zaangażowanie patrzy Instagram, gdy decyduje, komu jeszcze pokazać Twoje treści.",
                    "Boty nie potrafią nic z tych rzeczy. Podbijają liczbę na kilka dni, znikają przy kolejnej czystce, a te, które zostają, po cichu obniżają Twój zasięg.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Prawdziwi ludzie lajkują i komentują post twórcy na Instagramie"},
            },
            {
                "h2": "Skąd przychodzą nowi obserwujący",
                "p": [
                    "Podaj miasto, region lub kraj, z którego mają pochodzić Twoi odbiorcy. Najpierw pokazujemy Twój profil prawdziwym ludziom właśnie tam; jeśli najlepiej dopasowana publiczność jest większa w pobliżu, więcej osób może przyjść stamtąd.",
                ],
            },
            {
                "h2": "Jak wygląda miesiąc",
                "ul": [
                    "Pierwsze dni: kampania rusza i pojawiają się pierwsze wizyty.",
                    "Każdy tydzień: nowi obserwujący, polubienia i komentarze, po trochu każdego dnia.",
                    "Koniec miesiąca: zwykle {pick_audience} nowych obserwujących w pakiecie {pick_name}.",
                ],
            },
        ],
        "faqs": [
            ("Jak szybko przybywa obserwujących?", "Po trochu każdego dnia, przez cały miesiąc. Nigdy wszystko naraz: prawdziwi ludzie obserwują we własnym tempie, a wszystko, co pojawia się natychmiast, to boty."),
            ("Czy nowi obserwujący przestaną mnie obserwować?", "Niektórzy mogą, tak jak zmienia się każda prawdziwa publiczność. Prawdziwi obserwujący zostają jednak znacznie częściej niż boty, które znikają falami."),
            ("Czy dostanę też polubienia i komentarze?", "Tak, od tych samych ludzi: zwykle {pick_likes} polubień i {pick_comments} komentarzy miesięcznie w pakiecie {pick_name}."),
            ("Czy to bezpieczne dla mojego konta?", "Nigdy nie prosimy o hasło i nigdy nie logujemy się na Twoje konto. Ludzie sami znajdują Twój profil i sami decydują, tak jak każdy obserwujący, który na Ciebie trafia."),
            ("Czy mogę wybrać, skąd będą obserwujący?", "Tak. Podaj miasto, region lub kraj przy zamówieniu. Celujemy najpierw tam; jeśli w pobliżu jest większa, dobrze dopasowana publiczność, część obserwujących może przyjść stamtąd."),
        ],
    },
    {
        "service": "followers",
        "quantity": 1000,
        "slug": "instagram/obserwujacy/1000",
        "label": "{quantity} obserwujących na Instagramie",
        "title": "{quantity} prawdziwych obserwujących na Instagramie | Growsterr",
        "description": "Zdobądź {quantity} obserwujących na Instagramie: prawdziwych ludzi, nie boty. {pick_name} zwykle daje {pick_audience} miesięcznie, z polubieniami i komentarzami.",
        "h1": ("{quantity} obserwujących na Instagramie, ", "każdy z nich prawdziwy."),
        "intro": "Nie sprzedajemy paczki {quantity} botów. Rozwijamy Twoje konto z prawdziwymi ludźmi: {pick_name} zwykle daje {pick_audience} nowych obserwujących miesięcznie, więc {quantity} jest zazwyczaj w zasięgu już w pierwszym miesiącu.",
        "hero": {"image": "instagram-followers-1000", "alt": "Rosnąca linia nowych obserwujących na Instagramie dochodzi do pierwszego progu"},
        "sections": [
            {
                "h2": "Dlaczego nie {quantity} obserwujących w godzinę?",
                "p": [
                    "Bo żadna prawdziwa osoba nie zaczyna obserwować konta kilka sekund po płatności. Usługi, które dostarczają {quantity} obserwujących w godzinę, dostarczają boty: nie lajkują, nie komentują i znikają falami.",
                    "Te, które zostają, szkodzą jeszcze bardziej. Każdy obserwujący, który nigdy nie reaguje, obniża odsetek odbiorców, którzy reagują, a Twoje posty po cichu docierają do mniejszej liczby osób.",
                ],
            },
            {
                "h2": "Pierwszy tysiąc zdobyty porządnie",
                "p": [
                    "Pierwszy tysiąc prawdziwych obserwujących zmienia to, jak widzą Cię nowi odwiedzający. To ludzie, którzy mogą oglądać Twoje rolki, lajkować posty i wracać, a właśnie to pomaga kolejnemu tysiącowi Cię znaleźć.",
                ],
                "ul": [
                    "Prawdziwi ludzie, którzy sami zdecydowali się Cię obserwować, z wybranej przez Ciebie lokalizacji.",
                    "Polubienia i komentarze od tych samych ludzi, w ramach pakietu.",
                    "Panel, który dzień po dniu pokazuje, co zmierzyliśmy.",
                ],
            },
        ],
        "faqs": [
            ("Ile trwa zdobycie {quantity} prawdziwych obserwujących?", "W typowym tempie {pick_name} daje {pick_audience} nowych obserwujących miesięcznie, więc {quantity} jest zazwyczaj w zasięgu w pierwszym miesiącu. Prawdziwi ludzie obserwują we własnym tempie, więc każdy miesiąc wygląda trochę inaczej."),
            ("Czy to jednorazowa paczka {quantity}?", "Nie. Sprzedajemy wzrost w miesięcznych pakietach. {pick_name} kosztuje {pick_price} miesięcznie, a zrezygnować możesz w dowolnym momencie na swoim koncie."),
            ("Czy dostanę z nimi polubienia i komentarze?", "Tak, od tych samych prawdziwych ludzi: zwykle {pick_likes} polubień i {pick_comments} komentarzy miesięcznie w pakiecie {pick_name}."),
            ("Co dalej po {quantity}?", "Pakiet działa, dopóki go nie anulujesz, więc Twój wzrost trwa miesiąc po miesiącu. Gdy Twoje treści będą gotowe na więcej, możesz przejść na wyższy pakiet."),
        ],
    },
]
