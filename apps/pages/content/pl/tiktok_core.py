"""Polish TikTok pages: followers, views and comments, and the ways people ask for them
(prawdziwi, organicznie, stopniowo, co miesiąc, bez spadków, bezpiecznie, konto prywatne, LIVE,
strona Dla Ciebie...). Mirrors en/tiktok_core.py; the hub and likes live in tiktok.py. Keys and
placeholders: docs/CONTENT.md; word forms: pl/ui.py."""

UPDATED = "2026-11-09"

PAGES = [
    # --- Followers ------------------------------------------------------------------------
    {
        "service": "followers",
        "slug": "tiktok/obserwujacy",
        "label": "Obserwujący na TikToku",
        "title": "Kup obserwujących na TikToku: prawdziwi ludzie | Growsterr",
        "description": "Kup obserwujących na TikToku uczciwie: prawdziwi ludzie odkrywają Twoje filmy i sami zaczynają obserwować, codziennie przez miesiąc. Pakiety od {from_price}.",
        "h1": ("Kup obserwujących na TikToku, ", "za każdym stoi prawdziwy człowiek."),
        "intro": "Chcesz kupić obserwujących na TikToku, nie zapełniając konta botami? Nasze miesięczne pakiety codziennie pokazują Twój profil nowym ludziom, a widzowie, którym podoba się Twój styl, klikają „Obserwuj”. W pakiecie {starter_name} to zwykle {starter_audience} nowych obserwujących miesięcznie; większe pakiety dają więcej.",
        "hero": {"image": "tiktok-creator", "alt": "Twórca nagrywa nowy film na TikToka, a prawdziwi ludzie zaczynają go obserwować"},
        "sections": [
            {
                "h2": "Za co naprawdę płacisz",
                "p": [
                    "Gdy kupujesz u nas obserwujących na TikToku, płacisz za kampanię, a nie za licznik. Dzięki promowanym kampaniom w naszej sieci partnerskiej Twój profil codziennie przez cały miesiąc trafia do prawdziwych ludzi. Czy ktoś zacznie obserwować, zależy od niego, i właśnie ten wybór sprawia, że obserwowanie jest coś warte.",
                    "Wartość obserwującego na TikToku leży w tym, co robi dalej: ogląda Twój nowy film, zostaje do końca, lajkuje, wysyła znajomemu. Ludzie robią to wszystko. Konto stworzone do pompowania liczby nie robi nic z tego.",
                ],
            },
            {
                "h2": "Jak wybrać stronę, na której kupisz obserwujących na TikToku",
                "p": ["Niezależnie od strony czy aplikacji, kilka pytań szybko oddziela prawdziwe serwisy od sklepów z botami."],
                "ul": [
                    "Czy chce Twojego hasła albo logowania przez TikToka? Serwis z obserwującymi nigdy nie potrzebuje ani jednego, ani drugiego.",
                    "Czy mówi o tysiącach obserwujących w kilka minut? Tak szybko przychodzą tylko boty.",
                    "Czy pokazuje, co zmierzył, dzień po dniu, czy tylko liczbę na końcu?",
                    "Czy możesz sam zatrzymać subskrypcję, czy musisz pisać maila i czekać?",
                    "Czy polubienia i komentarze są sprzedawane jako dodatki, czy pochodzą od samych obserwujących?",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Nowi obserwujący oglądają na telefonach najnowsze filmy twórcy z TikToka"},
            },
            {
                "h2": "Najpierw obserwujący, potem wszystko, co przynoszą",
                "p": [
                    "Nowi obserwujący widzą Twoje filmy w kanale Obserwowane, a ich oglądanie, lajki i udostępnienia pomagają TikTokowi ustalić, komu jeszcze film może się spodobać. Obserwujący-boty zostawiają tę pierwszą widownię w ciszy, więc każdy nowy film startuje ze słabszej pozycji.",
                ],
            },
        ],
        "faqs": [
            ("Jak zdobyć obserwujących na TikToku z Growsterr?", "Wybierz pakiet, podaj nazwę użytkownika na TikToku, powiedz, gdzie ma mieszkać Twoja nowa publiczność, i zapłać kartą przez Stripe. Kampania rusza, a nowi obserwujący zaczynają przychodzić, po kilku każdego dnia."),
            ("Czy mogę kupić obserwujących na TikToku jednorazowo, bez subskrypcji?", "Nie. Nie sprzedajemy jednorazowych paczek. Prawdziwi ludzie przychodzą przez tygodnie, a nie w jednej dostawie, więc wzrost działa jako miesięczny pakiet. Możesz zrezygnować, kiedy chcesz, a opłacony miesiąc zostaje Twój."),
            ("Czy muszę instalować aplikację?", "Nie. Zamawiasz na tej stronie i śledzisz kampanię na swoim koncie Growsterr, w dowolnej przeglądarce. Uważaj na aplikacje, które dają obserwujących w zamian za obserwowanie obcych: takie obserwowania zwykle znikają, gdy tylko wymiana się kończy."),
            ("Czy kupno obserwujących na TikToku da mi viral?", "Nikt nie może tego obiecać. Prawdziwi obserwujący dają każdemu nowemu filmowi więcej ludzi, którzy mogą obejrzeć go do końca i podać dalej, co zwiększa jego szanse. To, czy wystrzeli, wciąż zależy od filmu."),
            ("Co robią obserwujący, gdy już obserwują?", "To, co zawsze robią prawdziwi ludzie: jedni oglądają każdy film, inni lajkują i komentują, kilku z czasem odpływa. W ciągu miesiąca {pick_name} zwykle daje {pick_likes} polubień i {pick_comments} komentarzy od tych samych ludzi."),
            ("Czy kupowanie obserwujących na TikToku ma sens w 2026 roku?", "Kupowanie botów nie ma: TikTok wciąż usuwa fałszywe konta, więc liczba się kurczy, a szkoda dla zasięgu zostaje. Płacenie za to, żeby prawdziwi ludzie odkryli Twój profil, to co innego, bo zachowują się jak publiczność, którą zdobyłbyś sam."),
        ],
    },
    {
        "service": "followers",
        "modifier": "real",
        "slug": "tiktok/obserwujacy/prawdziwi",
        "label": "Prawdziwi obserwujący na TikToku",
        "title": "Prawdziwi obserwujący na TikToku, którzy reagują | Growsterr",
        "description": "Kup prawdziwych obserwujących na TikToku: aktywnych ludzi, którzy znaleźli Twoje filmy, sami Cię wybrali, lajkują i komentują. Pakiety od {from_price}/mies.",
        "h1": ("Kup prawdziwych obserwujących na TikToku: ", "aktywnych i tu z wyboru."),
        "intro": "Gdy kupujesz u nas prawdziwych obserwujących na TikToku, każdy z nich jest człowiekiem: kimś, kto zobaczył Twój profil dzięki naszej kampanii, obejrzał kilka filmów i zdecydował się obserwować. Są aktywni tak, jak aktywni są ludzie: lajkują i komentują, gdy coś trafi, a milczą, gdy film nie jest dla nich.",
        "hero": {"image": "tiktok-likes", "alt": "Serca i nowe obserwowania od prawdziwych ludzi zbierają się na profilu na TikToku"},
        "sections": [
            {
                "h2": "Co sprawia, że obserwujący na TikToku jest prawdziwy",
                "ul": [
                    "Za kontem stoi człowiek, z własnymi filmami, polubieniami i historią.",
                    "Ma powód, żeby obserwować: najpierw obejrzał Twoje filmy.",
                    "To jego własny wybór: nikt mu nie zapłacił i nikt nie oczekuje obserwowania w zamian.",
                    "Ludzkie tempo: przychodzą po kilku, tak jak ludzie odkrywają wszystko, co warto obserwować.",
                ],
            },
            {
                "h2": "Aktywni obserwujący, uczciwie zdefiniowani",
                "p": [
                    "Nikt nie sprawi, że człowiek będzie aktywny. Gdy serwis sprzedaje aktywnych obserwujących na tysiące, opisuje konta, które lajkują według harmonogramu. Prawdziwi ludzie reagują, gdy coś ich złapie, co jest mniej przewidywalne i warte o wiele więcej.",
                    "W ciągu miesiąca ludzie, których sprowadza {pick_name}, zwykle zostawiają {pick_likes} polubień i {pick_comments} komentarzy. Tak zwykle wygląda prawdziwa aktywność {pick_audience} nowych obserwujących.",
                ],
            },
            {
                "h2": "Wysoka jakość to dobre dopasowanie",
                "p": [
                    "Obserwujący wysokiej jakości to taki, który może obejrzeć Twój kolejny film. Decyduje o tym dopasowanie: gdzie mieszka, jakim językiem mówi, co lubi oglądać. Ty wybierasz miejsce, a resztę selekcji robią Twoje filmy, bo ludzie obserwują tylko to, co do nich przemawia.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Twórca czyta komentarze nowych obserwujących z TikToka między ujęciami"},
            },
        ],
        "faqs": [
            ("Jak sprawdzić, czy obserwujący są prawdziwi?", "Przyjrzyj się im. Przejrzyj kilku nowych obserwujących, a znajdziesz profile z własnymi filmami i polubieniami. Patrz też na wyświetlenia i polubienia, bo prawdziwi obserwujący je ruszają. Panel pokazuje wizyty i obserwowania z naszej kampanii z każdego dnia."),
            ("Czy każdy obserwujący będzie lajkował i komentował?", "Nie, i to normalne. Niektórzy reagują prawie na wszystko, inni głównie oglądają. Nasze typowe miesięczne zakresy polubień i komentarzy wynikają z tego, co robi prawdziwa publiczność, a nie ze scenariusza."),
            ("Czy prawdziwi obserwujący kosztują więcej niż boty?", "Tak, bo dotarcie do prawdziwego człowieka kosztuje. {starter_name} to {starter_price} miesięcznie za zwykle {starter_audience} nowych obserwujących. Boty są tańsze z najprostszego powodu: nikogo tam nie ma."),
            ("Skąd pochodzą prawdziwi obserwujący?", "Stamtąd, gdzie skierujesz kampanię: z jednego miasta, szerszego regionu albo całego kraju. Odkrywają Twój profil dzięki naszym promowanym kampaniom, a potem obserwują na TikToku jak każdy inny."),
            ("Czy mogę kupić prawdziwych obserwujących na zupełnie nowe konto?", "Tak, ale najpierw opublikuj kilka filmów. Ludzie decydują na podstawie tego, co znajdą na profilu, a pusta siatka nie daje im czego obserwować."),
        ],
    },
    {
        "service": "followers",
        "modifier": "organic",
        "slug": "tiktok/obserwujacy/organiczni",
        "label": "Organiczni obserwujący na TikToku",
        "title": "Organiczni obserwujący na TikToku z Twojej okolicy | Growsterr",
        "description": "Kup organicznych obserwujących na TikToku przejrzyście: płacimy za pokazanie Twojego profilu prawdziwym ludziom tam, gdzie chcesz, a obserwują z własnej woli.",
        "h1": ("Organiczni obserwujący na TikToku: ", "płatny zasięg, ich własna decyzja."),
        "intro": "Czy można kupić organicznych obserwujących na TikToku? Oto dokładnie, co robimy. Płacimy za promowane kampanie, które przez naszą sieć partnerską pokazują Twój profil prawdziwym ludziom w wybranym przez Ciebie miejscu. Wszystko, co dzieje się dalej, jest organiczne: ludzie oglądają, wyrabiają sobie zdanie i obserwują, jeśli chcą więcej.",
        "hero": {"image": "tiktok-creator", "alt": "Lokalny twórca nagrywa film na TikToka dla widzów z własnego miasta"},
        "sections": [
            {
                "h2": "Za co się płaci, a za co nie",
                "p": [
                    "Płatna jest ekspozycja. Decyzja już nie. Nikt nie dostaje nagrody za obserwowanie Cię, nikt nie obserwuje w ramach wymiany i żadne konto nie obserwuje według skryptu. Tu przebiega granica między organicznymi a kupionymi obserwującymi.",
                    "W praktyce działa to podobnie jak twórca promujący własny profil, z tą różnicą, że kampanię prowadzi zespół, a panel pokazuje, co zmierzono.",
                ],
            },
            {
                "h2": "Obserwujący na TikToku kierowani według miejsca",
                "p": [
                    "Kierujemy według miejsca. Wskaż jedno miasto, region albo cały kraj, a tam pokażemy Twój profil najpierw. Piekarnia w Gdańsku chce ludzi z Gdańska; nauczyciel języka chce krajów, w których mieszkają uczący się. Gdy najlepiej dopasowani ludzie są rozsiani szerzej, część obserwujących może przyjść z okolicy.",
                ],
            },
            {
                "h2": "Prawdziwi obserwujący na TikToku, każdego dnia",
                "ul": [
                    "Każdego dnia miesiąca kilka nowych osób znajduje Twój profil.",
                    "Każda przychodzi przez Twoje filmy, więc wie, kogo zaczyna obserwować.",
                    "Panel pokazuje wizyty i obserwowania z każdego dnia, więc widzisz, jak to się dzieje.",
                ],
            },
        ],
        "faqs": [
            ("Czy to organiczne, skoro płacicie za kampanię?", "Płacisz za zasięg. Samo obserwowanie jest organiczne: ludzie widzą Twój profil, oglądają to, co ich interesuje, i decydują sami, a nikt nic nie dostaje za obserwowanie. To właśnie czyni obserwowanie organicznym."),
            ("Czym to się różni od follow za follow?", "Follow za follow to wymiana: ludzie obserwują Cię, żeby coś dostać, a wielu przestaje, gdy już to ma. Nasza kampania niczego od nikogo nie wymaga. Ludzie obserwują, bo chcą zobaczyć więcej."),
            ("Na co mogę kierować poza lokalizacją?", "Wybierasz lokalizację, od jednego miasta po cały kraj. W jej obrębie selekcję robią Twoje filmy. Ci, którzy się zatrzymują i obserwują, to ludzie, do których trafiają Twoje treści, a tego żadne ustawienie nie wyłapie równie dobrze."),
            ("Czy organiczni obserwujący będą reagować na moje filmy?", "Wielu tak, na własnych zasadach: w ciągu miesiąca z pakietem {pick_name} ludzie, którzy zaczynają obserwować, zwykle zostawiają razem {pick_likes} polubień i {pick_comments} komentarzy."),
            ("Jak szybko przychodzą organiczni obserwujący?", "Po trochu każdego dnia, od pierwszych dni kampanii do końca miesiąca. Organicznie nigdy nie znaczy wszystko naraz."),
        ],
    },
    {
        "service": "followers",
        "modifier": "monthly",
        "slug": "tiktok/obserwujacy/co-miesiac",
        "label": "Obserwujący na TikToku co miesiąc",
        "title": "Obserwujący na TikToku co miesiąc: subskrypcja wzrostu",
        "description": "Kupuj obserwujących na TikToku co miesiąc w subskrypcji, która codziennie sprowadza prawdziwych ludzi. Płatność kartą przez Stripe, rezygnujesz, kiedy chcesz.",
        "h1": ("Obserwujący na TikToku co miesiąc. ", "Wzrost, który sam się odnawia."),
        "intro": "Kupowanie obserwujących na TikToku co miesiąc to dokładnie nasz model. Wybierasz pakiet, działa przez 30 dni i odnawia się, dopóki go nie zatrzymasz. Każdego dnia każdego miesiąca nowi ludzie trafiają na Twój profil, a ci, którzy chcą więcej Twoich filmów, zaczynają obserwować.",
        "hero": {"image": "tiktok-likes", "alt": "Liczba obserwujących na TikToku rośnie miesiąc po miesiącu dzięki prawdziwym ludziom"},
        "sections": [
            {
                "h2": "Dlaczego wzrost sprzedaje się na miesiące",
                "p": [
                    "Prawdziwi ludzie nie przychodzą na zamówienie. Trafiają na profil, oglądają kilka filmów i decydują, a to trwa dni. Dlatego jednorazowa paczka obserwujących zawsze będzie botami. Miesiąc to naturalna jednostka prawdziwego wzrostu: dość długi, żeby ludzie Cię znaleźli, i dość krótki, żeby zmienić kurs.",
                    "Każdy miesiąc buduje też na poprzednim. Obserwujący z pierwszego miesiąca widzą Twoje nowe filmy, a ci, którzy je udostępniają, mogą przyprowadzić ludzi, którym nigdy nie pokazywaliśmy Twojego profilu.",
                ],
            },
            {
                "h2": "Jak działa płatność miesięczna",
                "ul": [
                    "Płacisz kartą przez Stripe; na urządzeniach, które je oferują, działa też Apple Pay i Google Pay.",
                    "Twoje konto pokazuje datę kolejnego odnowienia.",
                    "Rezygnacja na koncie zatrzymuje kolejną płatność; opłacony miesiąc trwa do końca.",
                    "Płacisz zawsze tylko za wybrany pakiet, bez żadnych dopłat.",
                ],
            },
            {
                "h2": "Drugi miesiąc i kolejne",
                "p": [
                    "Pierwszy miesiąc rozkręca kampanię. W drugim i trzecim Twój panel ma już wzór, który da się czytać: które tygodnie przyniosły więcej wizyt, które filmy zamieniały odwiedzających w obserwujących. Wtedy najłatwiej zdecydować, czy zostać, przejść wyżej, czy przestać.",
                ],
            },
        ],
        "faqs": [
            ("Czy muszę zamawiać ponownie co miesiąc?", "Nie. Pakiet odnawia się w swoim terminie, a kampania trwa bez przerwy. Musisz coś zrobić tylko wtedy, gdy chcesz zmienić pakiet albo zrezygnować."),
            ("Czy jest minimalna liczba miesięcy?", "Nie. Możesz zrezygnować po pierwszym miesiącu albo zostać tak długo, jak to pomaga. Rezygnacja zatrzymuje kolejną płatność, a opłacony już miesiąc trwa do ostatniego dnia."),
            ("Czy co miesiąc dostanę tyle samo obserwujących?", "Nie dokładnie. Każdy pakiet ma typowy zakres, na przykład {pick_audience} miesięcznie z pakietem {pick_name}, a prawdziwi ludzie sprawiają, że każdy miesiąc jest trochę inny."),
            ("Co pokazuje mój panel w każdym miesiącu?", "Wizyty na profilu z Twojej kampanii z każdego dnia, nowych obserwujących, których przyniosły, i aktualną liczbę obserwujących. Miesiąc po miesiącu to Twój zapis tego, co zrobił pakiet."),
            ("Jakie metody płatności działają przy planie miesięcznym?", "Karta przez Stripe oraz Apple Pay i Google Pay na telefonach i w przeglądarkach, które je mają. Subskrypcja potrzebuje metody, którą da się odnawiać co miesiąc, dlatego nie przyjmujemy jednorazowych opcji, takich jak przelew."),
        ],
    },
    {
        "service": "followers",
        "modifier": "gradual",
        "slug": "tiktok/obserwujacy/stopniowo",
        "label": "Obserwujący na TikToku stopniowo",
        "title": "Obserwujący na TikToku stopniowo, codziennie | Growsterr",
        "description": "Kup obserwujących na TikToku stopniowo: prawdziwi ludzie odkrywają Twój profil i obserwują po kilku, każdego dnia przez 30 dni. Bez kroplówki, w ludzkim tempie.",
        "h1": ("Obserwujący na TikToku stopniowo, ", "w tempie, w jakim ludzie naprawdę obserwują."),
        "intro": "Jeśli chcesz kupić obserwujących na TikToku stopniowo, a nie jednym podejrzanym skokiem, miesięczny pakiet działa tak z natury. Każdego dnia prawdziwi ludzie trafiają na Twój profil, a ci, którym się spodoba, obserwują. Nic nie jest wstrzymywane ani wypuszczane według minutnika: powolne, codzienne tempo to po prostu to, jak zachowują się ludzie.",
        "hero": {"image": "tiktok-likes", "alt": "Linia obserwujących na TikToku łagodnie rośnie, kilku prawdziwych ludzi dziennie"},
        "sections": [
            {
                "h2": "Kroplówka kontra prawdziwe codzienne tempo",
                "p": [
                    "Wiele serwisów oferuje „kroplówkę”: te same boty, wypuszczane małymi partiami, żeby skok wyglądał na mniejszy. Obserwujący to nadal konta, które nic nie oglądają. Rozłożenie ich w czasie tylko na chwilę ukrywa dostawę.",
                    "Nasze codzienne tempo nie jest ustawieniem. Wynika z tego, że tego dnia ludzie widzą Twój profil i decydują, jeden po drugim.",
                ],
            },
            {
                "h2": "Jak wygląda stopniowy wzrost na Twoim profilu",
                "ul": [
                    "Liczba obserwujących rośnie odrobinę prawie każdego dnia, z dniami spokojniejszymi i bardziej ruchliwymi.",
                    "Wyświetlenia i polubienia rosną razem z nią, bo oglądają ci sami ludzie.",
                    "Panel pokazuje wizyty na profilu i nowych obserwujących z każdego dnia, więc sam widzisz nachylenie.",
                ],
            },
            {
                "h2": "Dlaczego powolny wzrost jest tym, który zostaje",
                "p": [
                    "Konta, które rosną równo, zwykle zatrzymują zdobytą publiczność. Każdy nowy obserwujący przychodzi dzięki filmowi, który mu się spodobał, więc na Twój kolejny film ktoś już czeka.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Twórca publikuje codzienny film na TikToku, a publiczność rośnie równo"},
            },
        ],
        "faqs": [
            ("Ilu nowych obserwujących daje jeden dzień?", "To się zmienia. W skali całego miesiąca {pick_name} zwykle dodaje {pick_audience} nowych obserwujących; jedne dni przynoszą więcej, inne mniej, zależnie od tego, kto widzi Twój profil i co ostatnio publikowałeś."),
            ("Czy mogę ustawić tempo dostawy?", "Nie, bo nie ma dostawy do dławienia. Ludzie obserwują, gdy sami tak zdecydują. Ty wybierasz pakiet, a z nim to, ilu ludzi co miesiąc widzi Twój profil."),
            ("Czy powolna dostawa jest bezpieczniejsza dla konta?", "Tempo to tylko część sprawy. Powolna strużka botów to wciąż boty. Konto pozostaje zdrowe, gdy każdy obserwujący jest człowiekiem, który sam zdecydował się obserwować, a tylko takich sprowadzamy."),
            ("Kiedy przychodzą pierwsi obserwujący?", "Kampania rusza po zamówieniu, a pierwsze wizyty na profilu zwykle pojawiają się w pierwszych dniach. Obserwujący wyrastają z tych wizyt, osoba po osobie."),
            ("Czy stopniowy wzrost kończy się po 30 dniach?", "Każdy pakiet działa przez 30 dni i odnawia się co miesiąc, więc codzienne tempo trwa dalej w kolejnym miesiącu, dopóki nie zrezygnujesz."),
        ],
    },
    {
        "service": "followers",
        "modifier": "no-drop",
        "slug": "tiktok/obserwujacy/bez-spadkow",
        "label": "Obserwujący na TikToku, którzy zostają",
        "title": "Obserwujący na TikToku bez spadków: kto zostaje | Growsterr",
        "description": "Kup obserwujących na TikToku bez spadków po czystkach botów: prawdziwi ludzie, którzy sami Cię wybrali, nie znikają. Co zostaje, co nie i dlaczego.",
        "h1": ("Obserwujący na TikToku bez spadków. ", "Zacznij od ludzi, którzy tego chcą."),
        "intro": "Ludzie, którzy chcą kupić obserwujących na TikToku bez spadków, zwykle mają dość patrzenia, jak liczba się kurczy. Dzieje się tak, gdy obserwujący to boty, a TikTok je czyści. Nasi obserwujący to prawdziwi ludzie, którzy sami zdecydowali się obserwować, więc czystka nie ma czego usunąć. Kilku może później przestać obserwować, tak jak zmienia się każda prawdziwa publiczność.",
        "hero": {"image": "tiktok-likes", "alt": "Liczba obserwujących na TikToku trzyma się po miesiącu prawdziwego wzrostu"},
        "sections": [
            {
                "h2": "Skąd biorą się spadki",
                "p": [
                    "Nagłe spadki mają jedną typową przyczynę: usuwanie fałszywych kont. TikTok regularnie je kasuje, a każde obserwowanie, które miały, znika razem z nimi. Serwisy oferują wtedy uzupełnienia, czyli kolejne boty czekające na następną czystkę.",
                    "Prawdziwi obserwujący nie odchodzą falami. Niektórzy z czasem odpływają, pojedynczo, z powodów, dla których każdy przestaje obserwować: stracili zainteresowanie albo porządkowali listę obserwowanych.",
                ],
            },
            {
                "h2": "Nikt nie sprzeda Ci obserwujących na zawsze",
                "p": [
                    "Uważaj na każdego, kto sprzedaje obserwujących na TikToku „na zawsze”. Prawdziwy człowiek zawsze może zmienić zdanie, więc obietnica zera odobserwowań ma sens tylko przy kontach, które w ogóle nie myślą. Możemy powiedzieć, że ludzie, którzy sami zdecydowali się obserwować, zwykle zostają, bo zaczęli obserwować dla Twoich filmów.",
                ],
            },
            {
                "h2": "Jak zatrzymać obserwujących, którzy zostają",
                "ul": [
                    "Publikuj dalej takie filmy, dla których zaczęli Cię obserwować.",
                    "Odpowiadaj na komentarze: ludzie zostają tam, gdzie czują się wysłuchani.",
                    "Jeśli zmieniasz niszę, rób to stopniowo, a nie z dnia na dzień.",
                    "Publikuj na tyle często, żeby nie zapomnieli, że jesteś.",
                ],
            },
        ],
        "faqs": [
            ("Czy stracę któregoś z obserwujących od Was?", "Może kilku, tak jak zmienia się każda prawdziwa publiczność. Nie zobaczysz za to nagłej fali strat, bo TikTok nie ma tu żadnych fałszywych kont do wyczyszczenia."),
            ("Czy oferujecie uzupełnienia?", "Nie. Uzupełnienia istnieją po to, by zastąpić usunięte boty, a tu nie ma ich czym zastępować. Nasi obserwujący to ludzie, a Twój pakiet przez każdy dzień działania sprowadza nowych."),
            ("Czy zachowam obserwujących po rezygnacji?", "Zostają Twoi. Rezygnacja kończy kampanię z końcem opłaconego miesiąca; ludzie, którzy zaczęli Cię obserwować, obserwują dalej, dopóki podobają im się Twoje filmy."),
            ("Czy Wasi obserwujący na TikToku są na stałe?", "Żaden prawdziwy obserwujący nie jest na stałe z umowy, nasi też nie. To ludzie, a ludzie mogą przestać obserwować. To także jedyny rodzaj obserwujących, który nie znika w czystce."),
            ("Jak wypatrzyć boty wśród moich obecnych obserwujących?", "Otwórz kilka profili. Prawdziwi obserwujący mają własne filmy, polubienia i historię. Boty zwykle nie mają filmów, mają przypadkową nazwę i tysiące obserwowanych kont. Mówią Ci to też wyświetlenia: prawdziwi obserwujący je ruszają, boty nie."),
        ],
    },
    {
        "service": "followers",
        "modifier": "safe",
        "slug": "tiktok/obserwujacy/bezpiecznie",
        "label": "Bezpieczni obserwujący na TikToku",
        "title": "Bezpieczni obserwujący na TikToku, bez hasła | Growsterr",
        "description": "Bezpieczny i uczciwy sposób na obserwujących na TikToku: bez hasła i logowania, tylko prawdziwi ludzie, płatność kartą przez Stripe i plan, który anulujesz sam.",
        "h1": ("Kup obserwujących na TikToku bezpiecznie, ", "bez oddawania konta."),
        "intro": "Żeby bezpiecznie kupić obserwujących na TikToku, pierwsza zasada jest prosta: konto zostaje w Twoich rękach. Potrzebujemy tylko nazwy użytkownika. Nigdy nie prosimy o hasło, nigdy się nie logujemy i niczego nie uruchamiamy na Twoim koncie. Prawdziwi ludzie odkrywają Twój profil i decydują sami.",
        "hero": {"image": "tiktok-creator", "alt": "Twórca w pełni kontroluje swoje konto na TikToku, które rośnie dzięki prawdziwym obserwującym"},
        "sections": [
            {
                "h2": "Bezpieczne dla Twojego konta",
                "p": [
                    "Ryzyko w większości serwisów z obserwującymi nie leży w przycisku „Obserwuj”. Leży w tym, co przychodzi razem z nim: hasłach oddawanych obcym, aplikacjach logujących się jako Ty, botach, które znikają i zostawiają Twoje zaangażowanie puste. Tu nic z tego się nie dzieje.",
                    "Od strony TikToka każdy nowy obserwujący to człowiek, który odwiedził Twój profil i kliknął „Obserwuj”. Nic nie dzieje się wewnątrz Twojego konta, więc potem nie ma czego sprzątać.",
                ],
            },
            {
                "h2": "Jak rozpoznać uczciwą stronę z obserwującymi na TikToku",
                "ul": [
                    "Nigdy nie prosi o hasło ani o logowanie przez TikToka.",
                    "Nie obiecuje tysięcy obserwujących w kilka minut.",
                    "Podaje nazwę firmy, która za nią stoi.",
                    "Przyjmuje płatności przez znanego operatora i pozwala samemu zrezygnować.",
                    "Mówi o typowych zakresach, a nie dokładnych liczbach, bo prawdziwych ludzi nie da się policzyć z góry.",
                ],
            },
            {
                "h2": "Kto stoi za Growsterr",
                "p": [
                    "Za Growsterr stoi Sterr Agency: spółka Sterr Technologies OÜ, zarejestrowana w Tallinnie w Estonii, z siedzibą główną w Turcji. Płatności idą przez bezpieczną kasę Stripe: kartą, Apple Pay lub Google Pay. Gdy masz pytanie, odpowiada człowiek, na WhatsAppie albo mailem.",
                ],
            },
        ],
        "faqs": [
            ("Czy to może narobić mojemu kontu na TikToku kłopotów?", "Nigdy nie dotykamy Twojego konta: żadnego hasła, logowania ani automatyzacji. Do Twojego profilu trafiają ludzie, którzy go odwiedzają i obserwują, tak samo jak wtedy, gdy ktoś udostępni Twój film. Nie wypowiadamy się za TikToka, ale po Twojej stronie nie dzieje się nic poza większą liczbą prawdziwych odwiedzających."),
            ("Czy Growsterr to uczciwy serwis?", "Jesteśmy zarejestrowaną firmą, Sterr Technologies OÜ w Tallinnie w Estonii, za marką Sterr Agency. Płacisz przez Stripe, śledzisz kampanię w panelu ze zmierzonymi liczbami i rezygnujesz na swoim koncie, kiedy chcesz."),
            ("Czy moja płatność jest bezpieczna?", "Płatność idzie przez bezpieczną kasę Stripe, więc pełny numer Twojej karty nigdy do nas nie trafia. Możesz zapłacić kartą, Apple Pay lub Google Pay."),
            ("O jakie dane prosicie?", "O nazwę użytkownika na TikToku, miejsce, z którego ma pochodzić Twoja publiczność, oraz e-mail, numer telefonu i hasło do konta w Growsterr. Nigdy o hasło do TikToka."),
            ("Co, jeśli nie będę zadowolony?", "Zrezygnuj na swoim koncie, a pakiet się nie odnowi. Opłacony miesiąc trwa do ostatniego dnia i nie jest zwracany, więc zachowujesz wszystko, co przyniesie."),
        ],
    },
    {
        "service": "followers",
        "modifier": "private-account",
        "slug": "tiktok/obserwujacy/konto-prywatne",
        "label": "Obserwujący na prywatne konto na TikToku",
        "title": "Obserwujący na prywatne konto na TikToku? | Growsterr",
        "description": "Chcesz kupić obserwujących na prywatne konto na TikToku? Prawdziwi ludzie mogą tam tylko wysłać prośbę, więc na czas pakietu prosimy o konto publiczne.",
        "h1": ("Obserwujący na prywatnym koncie na TikToku? ", "Tak to działa."),
        "intro": "Myślisz o kupnie obserwujących na prywatne konto na TikToku? Prawdziwi ludzie nie mogą po prostu obserwować prywatnego profilu: mogą tylko wysłać prośbę i nie zobaczą Twoich filmów, dopóki jej nie zaakceptujesz. Dlatego nasze kampanie działają na kontach publicznych i dlatego prosimy, żeby Twoje było publiczne, dopóki działa pakiet.",
        "hero": {"image": "tiktok-creator", "alt": "Twórca przełącza konto na TikToku z prywatnego na publiczne przed kampanią"},
        "sections": [
            {
                "h2": "Dlaczego prywatne konto i prawdziwy wzrost się nie łączą",
                "p": [
                    "Gdy ktoś trafia na prywatne konto na TikToku, widzi nazwę, zdjęcie i kłódkę. Żadnych filmów, nic, na podstawie czego mógłby zdecydować, więc większość odwiedzających odchodzi. Garstka, która wyśle prośbę, czeka, aż ją zaakceptujesz, a rosnący stos próśb łatwo przeoczyć.",
                    "Serwis, który twierdzi, że rozwinie prywatne konto bez Twojego akceptowania każdej prośby, albo loguje się jako Ty, żeby je akceptować, albo nie dodaje nic.",
                ],
            },
            {
                "h2": "Twoje opcje, jeśli zależy Ci na prywatności",
                "ul": [
                    "Przełącz konto na publiczne na miesiące działania pakietu, a potem zdecyduj.",
                    "Prowadź osobne prywatne konto dla znajomych i rodziny, a rozwijaj publiczne.",
                    "Osobiste filmy ustaw jako widoczne dla Znajomych albo Tylko dla Ciebie, a resztę zostaw otwartą dla nowych ludzi.",
                ],
            },
        ],
        "faqs": [
            ("Czy rozwijacie prywatne konta na TikToku?", "Niezbyt dobrze i nie będziemy udawać, że jest inaczej. Prawdziwi ludzie muszą zobaczyć Twoje filmy, zanim zdecydują, a prywatny profil je ukrywa. Utrzymaj go publicznym, dopóki działa pakiet."),
            ("Czy muszę akceptować prośby o obserwowanie?", "Tylko na prywatnym koncie, dlatego prosimy o przełączenie na publiczne. Na publicznym koncie ludzie obserwują od razu i nie musisz nic robić."),
            ("Czy po miesiącu mogę wrócić do prywatnego konta?", "Możesz. Obserwujący, których już masz, zostają. Nowi ludzie znowu będą mogli tylko wysyłać prośby, więc wzrost zwolni do tego, co zaakceptujesz."),
            ("Czy potrzebujecie mojego logowania, żeby akceptować prośby za mnie?", "Nie, i nikt nie powinien. Nigdy nie prosimy o hasło i nie logujemy się na Twoje konto. Każdy, kto proponuje zarządzanie prośbami z wnętrza Twojego konta, chce więcej dostępu, niż potrzebuje serwis wzrostu."),
            ("Czy część moich filmów może zostać prywatna?", "Tak. TikTok pozwala ustawić, kto może oglądać każdy film. Zostaw profil publiczny, żeby dało się Cię odkryć, i ogranicz tylko kilka osobistych."),
        ],
    },
    {
        "service": "followers",
        "modifier": "live",
        "plan": "starter",
        "slug": "tiktok/obserwujacy/live",
        "label": "Obserwujący na TikToku, żeby odpalić LIVE",
        "title": "Obserwujący na TikToku do LIVE, prawdziwi ludzie | Growsterr",
        "description": "LIVE na TikToku wymaga 1000 obserwujących. Zdobądź ich wśród ludzi, którzy mogą wpaść na Twoje transmisje: {starter_name} daje zwykle {starter_audience} miesięcznie.",
        "h1": ("Obserwujący na TikToku, żeby odpalić LIVE, ", "i ktoś, dla kogo nadawać."),
        "intro": "Kupno obserwujących na TikToku, żeby odblokować LIVE, ma sens tylko wtedy, gdy ci obserwujący mogą się pojawić. TikTok wymaga 1000 obserwujących, zanim odblokuje LIVE, a nasze pakiety doprowadzą Cię tam z prawdziwymi ludźmi, którzy znaleźli Twoje filmy i zdecydowali się obserwować. Miesiąc w pakiecie {starter_name} zwykle dodaje {starter_audience} takich osób.",
        "hero": {"image": "tiktok-creator", "alt": "Twórca ustawia telefon i lampę pierścieniową przed pierwszym LIVE na TikToku"},
        "sections": [
            {
                "h2": "Próg 1000 obserwujących i dlaczego boty go tak naprawdę nie odblokują",
                "p": [
                    "Obserwujący-boty mogą przepchnąć liczbę ponad 1000, ale LIVE to pokój, a boty do niego nie wchodzą. Nadawałbyś do licznika, który pokazuje, że nikt nie ogląda. TikTok usuwa też fałszywe konta falami, więc liczba może spaść z powrotem pod próg.",
                    "Prawdziwi obserwujący to co innego. Zaczęli obserwować, bo spodobały im się Twoje filmy, a gdy odpalasz LIVE, to oni najczęściej to zauważają i wpadają.",
                ],
            },
            {
                "h2": "Przygotuj się do LIVE, gdy rośniesz",
                "ul": [
                    "Sprawdź opcję LIVE w aplikacji: TikTok ma też wymóg wieku i własne zasady dla transmisji.",
                    "Publikuj dalej w trakcie pakietu, żeby nowi obserwujący mieli powód zostać.",
                    "Wspomnij w filmach, że szykuje się pierwszy LIVE.",
                    "Zaplanuj pierwszą transmisję wokół czegoś konkretnego: pytań i odpowiedzi, poradnika, zajrzenia za kulisy.",
                ],
            },
            {
                "h2": "Gdy przekroczysz 1000",
                "p": [
                    "Pakiet działa z miesiąca na miesiąc, dopóki nie zrezygnujesz, więc publiczność rośnie dalej po odblokowaniu LIVE. Nie wysyłamy widzów na transmisję o konkretnej godzinie; kto dołączy, zależy od ludzi. Rośnie liczba osób, które mogą to zrobić.",
                ],
            },
        ],
        "faqs": [
            ("Ile czasu, zanim będę mógł odpalić LIVE?", "To zależy, od czego zaczynasz. {starter_name} zwykle daje {starter_audience} nowych obserwujących miesięcznie, więc przy małym koncie próg to zwykle kwestia tygodni. Ludzie decydują, kiedy obserwować, więc nie podamy daty."),
            ("Czy 1000 obserwujących to wciąż wymóg do LIVE?", "To od dawna obowiązujący próg TikToka, ale TikTok ustala zasady i może je zmieniać albo testować. Opcja LIVE w aplikacji pokazuje, co dotyczy Twojego konta."),
            ("Czy nowi obserwujący będą oglądać mój LIVE?", "Niektórzy mogą. To prawdziwi ludzie, którzy zaczęli obserwować dla Twoich filmów, a to, czy dołączą, zależy od ich dnia, jak przy każdej publiczności. Boty nie dołączyłyby nigdy."),
            ("Czy możecie wysłać widzów na mój pierwszy LIVE?", "Nie. Nikt nie wsadzi prawdziwych ludzi na transmisję o wybranej przez Ciebie godzinie, a konta, które dołączają na polecenie, siedzą w milczeniu. Możemy rozwijać publiczność, która może przyjść."),
            ("Który pakiet pasuje do odpalenia LIVE?", "{starter_name} zwykle wystarcza, żeby dojść do progu. Jeśli planujesz nadawać regularnie, {rising_name} szybciej rozwija publiczność i pozwala wybrać filmy, które dostają uwagę."),
        ],
    },
    # --- Comments -------------------------------------------------------------------------
    {
        "service": "comments",
        "slug": "tiktok/komentarze",
        "label": "Komentarze na TikToku",
        "title": "Kup komentarze na TikToku: prawdziwe, w pakiecie | Growsterr",
        "description": "Kup komentarze na TikToku uczciwie: prawdziwi ludzie mówią, co myślą o Twoich filmach, zwykle {starter_comments} miesięcznie, plus obserwujący i polubienia.",
        "h1": ("Kup komentarze na TikToku? ", "Zdobądź ludzi, którzy mają coś do powiedzenia."),
        "intro": "Jeśli przyszedłeś kupić komentarze na TikToku, oto uczciwa wersja: nie sprzedajemy samych komentarzy. Każdy pakiet sprowadza do Ciebie prawdziwych ludzi, a część z nich komentuje filmy, które im się podobają, własnymi słowami. {starter_name} zwykle daje {starter_comments} komentarzy miesięcznie, a większe pakiety więcej.",
        "hero": {"image": "tiktok-watch-time", "alt": "Widzowie wpisują komentarze pod filmem na TikToku, który właśnie obejrzeli"},
        "sections": [
            {
                "h2": "Dlaczego komentarzy nie zamawia się jak towaru",
                "p": [
                    "Komentarz to ktoś, kto mówi Ci, co pomyślał. Gdy pisze się go na zamówienie, przestaje tym być: ta sama garść zwrotów, te same emoji, publikowane z kont bez własnych filmów. Widzowie je wypatrują i przewijają dalej.",
                    "Prawdziwe komentarze są bardziej chaotyczne i o wiele bardziej przydatne. Zadają pytania, nie zgadzają się, cytują Twoją puentę i oznaczają znajomego, który musi to zobaczyć.",
                ],
            },
            {
                "h2": "Ile komentarzy daje każdy pakiet",
                "ul": [
                    "{starter_name}: zwykle {starter_comments} komentarzy miesięcznie, razem z {starter_audience} nowych obserwujących.",
                    "{rising_name}: zwykle {rising_comments}, a Ty decydujesz, które filmy dostają uwagę.",
                    "{pro_name}: zwykle {pro_comments}, do tego priorytetowe miejsce i linia na WhatsAppie prosto do nas.",
                ],
            },
            {
                "h2": "Zamień prawdziwe komentarze w kolejny film",
                "p": [
                    "TikTok pozwala odpowiedzieć na komentarz filmem, a szczere pytanie od widza to jeden z najłatwiejszych pomysłów, jakie kiedykolwiek dostaniesz. Komentarze ze scenariusza nigdy nie pytają o nic, na co warto odpowiedzieć.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Twórca nagrywa filmową odpowiedź na pytanie widza na TikToku"},
            },
        ],
        "faqs": [
            ("Czy mogę dostać komentarze na TikToku bez obserwujących?", "Nie. Komentarze są częścią każdego miesięcznego pakietu i piszą je ludzie, którzy także Cię obserwują i lajkują. Nie są sprzedawane osobno."),
            ("Czy mogę decydować, co ludzie napiszą?", "Nie, i o to chodzi: ludzie piszą to, co naprawdę myślą. Żeby zacząć rozmowę, zadaj pytanie w opisie albo na końcu filmu. Prawdziwi widzowie odpowiadają na pytania."),
            ("Które filmy dostają komentarze?", "Głównie najnowsze, bo to je ludzie widzą najpierw na Twoim profilu. Jeśli chcesz, żeby rozmowa toczyła się pod jednym filmem, {rising_name} i {pro_name} pozwalają skierować na niego kampanię."),
            ("Czy komentarze będą w moim języku?", "Ludzie komentują w języku, którym mówią. Skieruj kampanię tam, gdzie mówi się Twoim językiem, a zwykle w nim będziesz czytać komentarze."),
            ("Czy komentarze przychodzą wszystkie naraz?", "Nie. Przychodzą przez cały miesiąc, gdy ludzie odkrywają Twoje filmy. Wysyp komentarzy w pierwszej minucie pod filmem, którego prawie nikt nie obejrzał, wygląda źle dla każdego, kto to widzi."),
        ],
    },
    # --- Views ----------------------------------------------------------------------------
    {
        "service": "views",
        "slug": "tiktok/wyswietlenia",
        "label": "Wyświetlenia na TikToku",
        "title": "Kup wyświetlenia na TikToku od ludzi, którzy oglądają | Growsterr",
        "description": "Kup wyświetlenia na TikToku, za którymi stoi prawdziwe oglądanie: ludzie odkrywają Twój profil i oglądają filmy, w pakiecie z obserwującymi i polubieniami.",
        "h1": ("Kup wyświetlenia na TikToku ", "od ludzi, którzy naprawdę oglądają."),
        "intro": "Szukasz sposobu, żeby kupić wyświetlenia na TikToku? Nie sprzedajemy odtworzeń na tysiące. Każdy pakiet sprowadza na Twój profil nowych widzów, którzy oglądają filmy, które ich złapią, lajkują to, co im się podoba, i obserwują, gdy chcą więcej. Ich wyświetlenia są częścią pakietu, nigdy osobną liczbą.",
        "hero": {"image": "tiktok-watch-time", "alt": "Prawdziwi ludzie oglądają filmy na TikToku na telefonach, wyświetlenie po wyświetleniu"},
        "sections": [
            {
                "h2": "Wyświetlenie jest warte tyle, ile oglądanie",
                "p": [
                    "TikTok liczy wyświetlenie, gdy tylko film zacznie się odtwarzać. Liczy się to, co dzieje się dalej: czy widz został, obejrzał jeszcze raz, udostępnił, otworzył Twój profil? Tysiące odtworzeń, które kończą się po sekundzie, mówią TikTokowi coś odwrotnego, niż chciałeś.",
                    "Wyświetlenia od prawdziwych ludzi niosą resztę tej historii, bo osoba, która obejrzała, może też polubić, zacząć obserwować albo podać film dalej.",
                ],
            },
            {
                "h2": "Dlaczego nie podajemy liczby wyświetleń",
                "p": [
                    "Obserwujący, polubienia i komentarze mają typowe miesięczne zakresy. Wyświetlenia nie, bo zależą od filmu tak samo jak od widza: jedna osoba obejrzy klip raz i pójdzie dalej, inna puści go w pętli i otworzy trzy kolejne. Dlatego nie sprzedajemy liczby wyświetleń. Sprowadzamy ludzi, a resztę robią Twoje filmy.",
                ],
            },
            {
                "h2": "Jak wybrać, gdzie kupić wyświetlenia na TikToku",
                "ul": [
                    "Prawdziwe wyświetlenie przychodzi z widzem: szukaj polubień, obserwowań i komentarzy, które rosną razem z nim.",
                    "Tanie wyświetlenia na tysiące to odtworzenia, a nie ludzie.",
                    "Strona, która do dostarczenia wyświetleń potrzebuje Twojego logowania do TikToka, to strona do opuszczenia.",
                    "Jeśli serwis pokazuje panel, sprawdź, co faktycznie mierzy.",
                ],
            },
        ],
        "faqs": [
            ("Ile wyświetleń dostaną moje filmy?", "Nie liczymy wyświetleń z góry. Dają je prawdziwi ludzie, którzy każdego dnia odkrywają Twój profil, a to, ile obejrzą, zależy od Twoich filmów. Mierzymy i pokazujemy wizyty na profilu z Twojej kampanii i nowych obserwujących, których przyniosły."),
            ("Czy mogę kupić wyświetlenia pod jeden konkretny film na TikToku?", "Nie osobno. Z pakietem {rising_name} i {pro_name} wybierasz filmy, które dostają uwagę, więc film, na którym Ci zależy, zobaczy więcej sprowadzanych przez nas ludzi."),
            ("Czy tanie wyświetlenia filmów na TikToku szkodzą?", "Mogą. Wyświetlenia od botów to odtworzenia, których nikt nie ogląda, więc obniżają średni czas oglądania Twojego filmu, a to jedna z rzeczy, które TikTok bierze pod uwagę, decydując, kto zobaczy film następny."),
            ("Czy potrzebuję aplikacji, żeby kupić wyświetlenia na TikToku?", "Nie. Wszystko działa z Twojego konta Growsterr w przeglądarce: zamawiasz, płacisz kartą albo portfelem w telefonie, takim jak Apple Pay, i sprawdzasz panel. Omijaj aplikacje, które każą logować się przez TikToka, żeby odblokować wyświetlenia."),
            ("Czy wyświetlenia przychodzą z obserwującymi i polubieniami?", "Tak. Ludzie, którzy oglądają Twoje filmy, to ci sami, którzy obserwują i lajkują: zwykle {pick_audience} nowych obserwujących i {pick_likes} polubień miesięcznie z pakietem {pick_name}."),
        ],
    },
    # --- Likes (the likes page itself is in tiktok.py) ----------------------------------------
    {
        "service": "likes",
        "modifier": "real",
        "slug": "tiktok/polubienia/prawdziwe",
        "label": "Prawdziwe polubienia na TikToku",
        "title": "Prawdziwe polubienia na TikToku, bez botów | Growsterr",
        "description": "Kup prawdziwe polubienia na TikToku, bez botów: od widzów, którzy obejrzeli Twój film i go polubili, w miesięcznym pakiecie z obserwującymi i komentarzami.",
        "h1": ("Prawdziwe polubienia na TikToku. ", "Każde od kogoś, kto obejrzał."),
        "intro": "Gdy kupujesz prawdziwe polubienia na TikToku przez Growsterr, każde pochodzi od człowieka, nigdy od bota: od kogoś, kto znalazł Twój profil dzięki naszej kampanii, odtworzył film i go polubił. Polubienia są w każdym pakiecie, razem z obserwującymi i komentarzami, zwykle {starter_likes} miesięcznie w pakiecie {starter_name}.",
        "hero": {"image": "tiktok-likes", "alt": "Serce stuknięte przez prawdziwego widza na końcu filmu na TikToku"},
        "sections": [
            {
                "h2": "Jak odróżnić prawdziwe polubienia od polubień botów",
                "ul": [
                    "Sprawdź, kto polubił: aktywność pokazuje konta, a prawdziwe mają własne zdjęcia, filmy i obserwujących.",
                    "Porównaj polubienia z wyświetleniami: prawdziwe polubienia to wycinek osób, które obejrzały, nigdy więcej niż wszyscy.",
                    "Spójrz na czas: prawdziwe polubienia spływają przez dni, polubienia botów lądują jednym blokiem.",
                    "Zobacz, co przychodzi razem z nimi: prawdziwi lajkujący czasem komentują, obserwują albo udostępniają.",
                ],
            },
            {
                "h2": "Polubienia wysokiej jakości, czyli jakie",
                "p": [
                    "Polubienie wysokiej jakości to takie, za którym stoi prawdziwe obejrzenie, od kogoś, kto może obejrzeć znowu. Nie ma znaczenia, jak dopracowane jest konto. Liczy się to, że człowiek wybrał Twój film i został przy nim na tyle długo, żeby stuknąć w serce.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Widz zatrzymuje się przy klipie na TikToku, który mu się spodobał, z kciukiem nad sercem"},
            },
            {
                "h2": "Prawdziwe polubienia przychodzą z resztą pakietu",
                "p": [
                    "Polubienia to jedna z rzeczy, które robią ci sami ludzie: także obserwują i komentują. Miesiąc z pakietem {pick_name} to zwykle {pick_likes} polubień, {pick_audience} nowych obserwujących i {pick_comments} komentarzy, wszystko od prawdziwych ludzi.",
                ],
            },
        ],
        "faqs": [
            ("Czy polubienia są od prawdziwych ludzi, zupełnie bez botów?", "Tak. Nigdzie nie używamy botów, fałszywych kont ani automatyzacji. Każde polubienie zostawia ktoś, kto dotarł do Twojego filmu dzięki naszej kampanii i zdecydował się stuknąć w serce."),
            ("Czy mogę kupić prawdziwe polubienia bez obserwujących?", "Nie. Prawdziwe polubienia dają tylko prawdziwi widzowie, a prawdziwi widzowie także obserwują, komentują i udostępniają, gdy mają ochotę. Dlatego wszystko jest w jednym pakiecie."),
            ("Dlaczego nie możecie podać dokładnej liczby polubień?", "Bo decydują ludzie. Wiemy, co zwykle robi prawdziwa publiczność, więc podajemy zakresy, na przykład {pick_likes} miesięcznie z pakietem {pick_name}. Stała liczba oznaczałaby, że komuś kazano lajkować."),
            ("Czy prawdziwe polubienia pomagają filmom docierać do większej liczby osób?", "Przychodzą z tym, czego polubienia od botów nigdy nie mają: prawdziwym czasem oglądania, a czasem udostępnieniem lub obserwowaniem. To pełniejszy obraz pomaga filmowi iść dalej; sama liczba nie pomaga."),
            ("Skąd są ludzie, którzy lajkują moje filmy?", "Z lokalizacji, którą podajesz przy zamówieniu: jednego miasta, szerszego regionu albo całego kraju. Jeśli najlepsze dopasowanie do Twojej publiczności jest nieco szersze, część polubień przychodzi z okolicy."),
        ],
    },
    {
        "service": "likes",
        "modifier": "organic",
        "slug": "tiktok/polubienia/organiczne",
        "label": "Organiczne polubienia na TikToku",
        "title": "Organiczne polubienia na TikToku, zasłużone filmem | Growsterr",
        "description": "Kup organiczne polubienia na TikToku: prawdziwi ludzie trafiają na Twój profil i lajkują filmy, które na to zasłużą. Najwięcej zbierają najlepsze.",
        "h1": ("Organiczne polubienia na TikToku, ", "zdobywane film po filmie."),
        "intro": "Czy można kupić organiczne polubienia na TikToku? Możesz zapłacić za to, żeby ludzie zobaczyli Twoje filmy, i to właśnie robią nasze pakiety. Polubienia pozostają organiczne, bo każde to reakcja prawdziwego człowieka na film, który obejrzał. Nikt nie dostaje polecenia, co polubić, i nic nie jest rozkładane równo, żeby wyglądało naturalnie.",
        "hero": {"image": "tiktok-likes", "alt": "Polubienia zbierają się nierówno pod filmami twórcy, najwięcej pod najlepszym"},
        "sections": [
            {
                "h2": "Jak wyglądają organiczne polubienia",
                "p": [
                    "Organiczne polubienia są nierówne. Najlepszy film zbiera ich dużo więcej niż najsłabszy, polubienia wciąż przychodzą pod starsze filmy, a jeden hit potrafi ściągnąć polubienia na wszystko inne na profilu. Kupione wyglądają płasko: ta sama liczba pod każdym postem, wszystkie naraz.",
                ],
            },
            {
                "h2": "Twoje filmy decydują, gdzie trafiają polubienia",
                "ul": [
                    "Pierwsze sekundy decydują, czy ktoś zostanie na tyle długo, żeby polubić.",
                    "Dźwięk, który ludzie rozpoznają, może sprawić, że przestaną przewijać.",
                    "Napisy i tekst na ekranie pomagają widzom oglądającym bez dźwięku.",
                    "Wyraźne zakończenie albo płynna pętla sprawiają, że ludzie oglądają jeszcze raz.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Twórca wybiera dźwięk do filmu na TikToku przed publikacją"},
            },
            {
                "h2": "Co dodaje pakiet",
                "p": [
                    "Dodajemy ludzi: stały dopływ prawdziwych widzów z wybranego przez Ciebie miejsca, każdego dnia miesiąca. Z pakietem {pick_name} zostawiają zwykle {pick_likes} polubień, razem z nowymi obserwującymi i komentarzami.",
                ],
            },
        ],
        "faqs": [
            ("Czy polubienia są naprawdę organiczne, skoro płacę?", "Twoje pieniądze kupują szansę, żeby Cię zobaczono. Każde polubienie to wciąż decyzja kogoś, kto ogląda Twój film, i to właśnie znaczy organiczne. Jeśli film nie trafi, dostanie mniej, a to też warto wiedzieć."),
            ("Czy wszystkie moje filmy dostaną tyle samo polubień?", "Nie. Organiczne polubienia idą za jakością, momentem i odrobiną szczęścia. Ta nierówność to część tego, co czyni je wiarygodnymi."),
            ("Czy organiczne polubienia mogą pochodzić z konkretnego kraju?", "Tak. Wybierz miasto, region lub kraj, a ludzie, którzy zobaczą Twój profil, będą najpierw stamtąd. Ich polubienia pochodzą z tego samego miejsca."),
            ("Czy organiczne polubienia pomagają, żeby film był częściej pokazywany?", "TikTok patrzy na polubienia razem z czasem oglądania, udostępnieniami i obserwowaniami. Polubienia od ludzi, którzy obejrzeli, niosą ze sobą te inne sygnały; polubienia od botów nie niosą żadnych."),
            ("Czym to się różni od grup zaangażowania?", "Grupy zaangażowania wymieniają się polubieniami: Ty lajkujesz ich, oni Twoje. Konta są prawdziwe, ale zainteresowanie nie. Nasi widzowie nic Ci nie są winni, więc gdy lajkują film, robią to szczerze."),
        ],
    },
    {
        "service": "likes",
        "modifier": "monthly",
        "slug": "tiktok/polubienia/co-miesiac",
        "label": "Polubienia na TikToku co miesiąc",
        "title": "Polubienia na TikToku co miesiąc, nie autolajki | Growsterr",
        "description": "Kupuj polubienia na TikToku co miesiąc od prawdziwych ludzi: pakiet odnawia się sam i sprowadza widzów pod każdy nowy film. Inaczej niż autolajki: bez skryptu.",
        "h1": ("Polubienia na TikToku co miesiąc. ", "Prawdziwi ludzie, a nie autolajker."),
        "intro": "Chcesz kupować polubienia na TikToku co miesiąc, żeby każdy nowy film miał start? To robią nasze pakiety, z jedną różnicą wobec autolajków: nie ma skryptu. Pakiet sam odnawia się co miesiąc, a każdego dnia prawdziwi ludzie odkrywają Twój profil, oglądają i lajkują filmy, które im się podobają.",
        "hero": {"image": "tiktok-likes", "alt": "Polubienia od prawdziwych widzów przychodzą pod najnowsze filmy twórcy na TikToku"},
        "sections": [
            {
                "h2": "Autolajki kontra miesięczny pakiet",
                "p": [
                    "Autolajki na TikToku obserwują Twoje konto i w kilka minut wystrzeliwują ustaloną liczbę polubień w każdy nowy film. Każdy film dostaje tyle samo, od kont, które go nigdy nie obejrzały. Wygląda to na automat, bo nim jest.",
                    "Miesięczny pakiet jest automatyczny w jedynym miejscu, w którym powinien: w płatności. Nie zamawiasz ponownie, a kampania nie robi przerwy między miesiącami. Same polubienia zostają ludzkie, więc świetny film dostaje więcej, a cichy mniej.",
                ],
            },
            {
                "h2": "Jak wygląda miesiąc polubień",
                "ul": [
                    "Polubienia rozkładają się na 30 dni i na filmy, które ludzie sami wybierają do oglądania.",
                    "Najmocniejsze filmy zbierają najwięcej, tak jak powinny.",
                    "Nowe filmy trafiają na świeżą publiczność, bo nowi ludzie znajdują Twój profil każdego dnia.",
                    "{rising_name} i {pro_name} pozwalają wybrać filmy, które w tym miesiącu są najważniejsze.",
                ],
            },
            {
                "h2": "Dlaczego miesięczny rytm pasuje do TikToka",
                "p": [
                    "Twórcy na TikToku pracują w rytmach: seria, cotygodniowy format, premiera. Miesięczny pakiet do tego pasuje. Co miesiąc widzisz, co zmierzył Twój panel, sprawdzasz, które filmy ludzie lajkowali, i decydujesz, na czym skupić się w kolejnym.",
                ],
            },
        ],
        "faqs": [
            ("Czy każdy nowy film dostanie polubienia automatycznie?", "Nie według harmonogramu. Nowe filmy widzą ludzie, którzy tego dnia odkrywają Twój profil, i lajkują to, co im się podoba. Jedne filmy zbierają dużo, inne mniej, tak jak przy prawdziwej publiczności."),
            ("Ile polubień dostaję co miesiąc?", "{starter_name} zwykle daje {starter_likes} miesięcznie, {rising_name} {rising_likes}, a {pro_name} {pro_likes}, wszystko od ludzi, którzy Cię obserwują."),
            ("Czy muszę Wam mówić, kiedy publikuję?", "Nie. Kampania pokazuje Twój profil, a ludzie widzą to, co najnowsze. Jeśli jeden film jest ważniejszy od reszty, {rising_name} i {pro_name} pozwalają skierować tam uwagę."),
            ("Co jest złego w autolajkach?", "Lądują kilka minut po publikacji, za każdym razem w tej samej liczbie, z kont, które nigdy nie oglądały. Polubienia bez czasu oglądania i identyczna liczba pod każdym filmem tworzą wzór, który każdy odczyta."),
            ("Czy mogę zatrzymać miesięczne polubienia?", "Tak. Rezygnacja na koncie kończy odnawianie; bieżący miesiąc i tak trwa do ostatniego dnia."),
        ],
    },
    {
        "service": "likes",
        "modifier": "gradual",
        "slug": "tiktok/polubienia/stopniowo",
        "label": "Polubienia na TikToku stopniowo",
        "title": "Polubienia na TikToku powoli, od prawdziwych widzów | Growsterr",
        "description": "Kup polubienia na TikToku powoli i naturalnie: prawdziwi ludzie lajkują Twoje filmy po trochu, dzień po dniu, w pakiecie z obserwującymi i komentarzami.",
        "h1": ("Polubienia na TikToku powoli, ", "tak jak dają je prawdziwi widzowie."),
        "intro": "Ludzie, którzy kupują polubienia na TikToku powoli, chcą, żeby wyglądały naturalnie. Najprostszy sposób: niech będą naturalne. Każdego dnia miesiąca nasza kampania sprowadza na Twój profil nowych widzów; oglądają i lajkują to, co im się podoba, po kilka naraz. {pick_name} zwykle daje w miesiąc {pick_likes} polubień.",
        "hero": {"image": "tiktok-likes", "alt": "Pod filmem na TikToku pojawia się po kilka polubień dziennie przez kilka dni"},
        "sections": [
            {
                "h2": "Jak prawdziwe polubienia rozkładają się w życiu filmu",
                "p": [
                    "Prawdziwy film nie dostaje wszystkich polubień w pierwszej godzinie. Ludzie znajdują go przez Twój profil kilka dni później, przewijają starsze filmy i lajkują te, które przegapili. Ten długi ogon to obraz prawdziwej uwagi i właśnie tego brakuje nagłej paczce polubień.",
                ],
            },
            {
                "h2": "Dlaczego stopniowa dostawa to nie sedno",
                "p": [
                    "Niektóre serwisy sprzedają stopniową dostawę: te same polubienia od botów, wypuszczane przez kilka godzin. Zmienia się tempo, a polubienia nie. Polubienie bez wyświetlenia za nim jest puste, choćby przychodziło najwolniej.",
                    "U nas nie ma czego wypuszczać. Polubienia dają ludzie, którzy obejrzeli, tego dnia, w którym obejrzeli.",
                ],
            },
            {
                "h2": "Czego się spodziewać, tydzień po tygodniu",
                "ul": [
                    "Pierwszy tydzień: pierwsi odwiedzający i ich pierwsze polubienia, zwykle pod najnowszymi filmami.",
                    "Drugi i trzeci tydzień: równy strumień, gdy kolejni ludzie znajdują Twój profil i przewijają wstecz.",
                    "Czwarty tydzień: miesiąc polubień rozłożony na wiele filmów, a nie spiętrzony pod jednym.",
                ],
            },
        ],
        "faqs": [
            ("Ile polubień dziennie dostanę?", "To zmienia się z dnia na dzień. W skali miesiąca {starter_name} zwykle daje {starter_likes} polubień, a {rising_name} {rising_likes}, rozłożonych na 30 dni i na filmy, które ludzie sami wybierają."),
            ("Czy mogę wybrać, jak wolno przychodzą polubienia?", "Nie ma ustawienia tempa, bo nikt nie wypuszcza polubień według minutnika. Przychodzą, gdy ludzie oglądają. Jeśli chcesz więcej uwagi przy konkretnych filmach, {rising_name} i {pro_name} pozwalają je wybrać."),
            ("Dlaczego niektóre starsze filmy też dostają polubienia?", "Bo prawdziwi ludzie przeglądają. Ktoś, komu spodoba się jeden film, często otwiera Twój profil i ogląda kilka kolejnych. Takie polubienia to dobry znak: znaczą, że ludzie chcą Cię więcej."),
            ("Czy polubienia przychodzą z wyświetleniami?", "Zawsze. Polubienie oznacza tu, że człowiek najpierw obejrzał film, więc wyświetlenia rosną razem z nim. Polubienia, których jest więcej niż wyświetleń filmu, zdradzają, że w grę wchodziły boty."),
            ("Czy polubienia przychodzą też po pierwszym miesiącu?", "Tak, dopóki pakiet się odnawia. Każdy miesiąc przynosi świeży strumień widzów, a ludzie, którzy zaczęli obserwować wcześniej, często dalej lajkują Twoje nowe filmy."),
        ],
    },
    {
        "service": "likes",
        "modifier": "no-drop",
        "slug": "tiktok/polubienia/bez-spadkow",
        "label": "Polubienia na TikToku, które zostają",
        "title": "Polubienia na TikToku, które zostają, bez spadków | Growsterr",
        "description": "Kup polubienia na TikToku, które zostają pod filmami: polubienia od prawdziwych ludzi nie znikają, gdy TikTok czyści fałszywe konta. W każdym pakiecie.",
        "h1": ("Polubienia na TikToku, które zostają, ", "bo dał je człowiek."),
        "intro": "Żeby kupić polubienia na TikToku, które zostają, potrzebujesz polubień, których nie ruszy żadna czystka. Gdy fałszywe konto zostaje usunięte, znika każde polubienie, które zostawiło. Nasze polubienia dają prawdziwi ludzie, którzy obejrzeli Twoje filmy, w miesięcznym pakiecie, a ludzie rzadko cofają polubienie, które już dali.",
        "hero": {"image": "tiktok-likes", "alt": "Liczba polubień na TikToku utrzymuje się tydzień po tygodniu"},
        "sections": [
            {
                "h2": "Dlaczego kupione polubienia znikają",
                "p": [
                    "Liczba polubień spada głównie z jednego powodu: konta za nimi zniknęły. TikTok usuwa fałszywe konta i fałszywe zaangażowanie, a wtedy ich polubienia też odchodzą. Film może pokazywać dużą liczbę jednego tygodnia i znacznie mniejszą następnego, choć w międzyczasie nic nie zrobiłeś.",
                ],
            },
            {
                "h2": "Polubienia, które zostają, i dlaczego",
                "ul": [
                    "Pochodzą z prawdziwych kont z własną historią, których czystka nie ma powodu usuwać.",
                    "Pochodzą od ludzi, którzy obejrzeli, więc wyświetlenia za nimi też są prawdziwe.",
                    "Rozkładają się na dni i filmy, nigdy nie piętrzą się pod jednym postem.",
                    "Należą do ludzi, którzy często też obserwują, więc są związane z prawdziwą publicznością.",
                ],
            },
            {
                "h2": "Jeśli kupowałeś już polubienia",
                "p": [
                    "Nie możesz sam usunąć polubień i nie musisz. Polubienia od botów znikają, gdy TikTok czyści konta, które za nimi stoją. Najlepsze, co możesz zrobić, to sprowadzić prawdziwych widzów pod kolejne filmy, żeby to nowsze liczby mówiły za Twoje konto.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Twórca zaczyna od nowa z nowym filmem na TikToku dla prawdziwych widzów"},
            },
        ],
        "faqs": [
            ("Czy polubienia kiedyś znikną?", "Tylko jeśli osoba, która je dała, je usunie albo skasuje konto, a to rzadkie. Nie czeka żadna fala usunięć, bo nie stoją za nimi fałszywe konta."),
            ("Czy mogę dostać trwałe polubienia bez obserwujących?", "Nie. Polubienia są częścią każdego pakietu i przychodzą razem z obserwowaniami i komentarzami od tych samych widzów. Nie sprzedajemy ich osobno i to jeden z powodów, dla których zostają: są związane z ludźmi, którzy sami zaczęli obserwować."),
            ("Dlaczego polubienia kupione gdzie indziej spadły?", "Najpewniej konta za nimi zostały usunięte. Tak prędzej czy później dzieje się z fałszywym zaangażowaniem na TikToku, cokolwiek obiecywał sprzedawca."),
            ("Ile polubień zostaje co miesiąc?", "Wszystkie nasze polubienia zostawiają prawdziwi ludzie, więc właściwe pytanie brzmi, ilu ludzi lajkuje Twoje filmy: zwykle {pick_likes} miesięcznie z pakietem {pick_name}."),
            ("Czy mniej prawdziwych polubień jest lepsze niż dużo kupionych?", "Tak. Polubienie, które przychodzi z pełnym obejrzeniem, obserwowaniem albo komentarzem, jest częścią wzoru, który czyta się jako prawdziwe zainteresowanie. Duża liczba bez niczego wokół czyta się dokładnie jako to, czym jest."),
        ],
    },
    {
        "service": "likes",
        "modifier": "safe",
        "slug": "tiktok/polubienia/bezpiecznie",
        "label": "Bezpieczne polubienia na TikToku",
        "title": "Czy kupno polubień na TikToku jest bezpieczne? | Growsterr",
        "description": "Uczciwy sposób na polubienia na TikToku: prawdziwi widzowie, bez logowania, płatność kartą przez Stripe, panel z pomiarami i plan, który anulujesz sam.",
        "h1": ("Uczciwy sposób na polubienia na TikToku: ", "prawdziwi ludzie, bez dróg na skróty."),
        "intro": "Pytanie, czy kupowanie polubień na TikToku jest w porządku, to dobry odruch. Większość sprzedawców polubień dostarcza boty, a niektórzy chcą też Twojego logowania. My robimy coś innego: prawdziwi ludzie odkrywają Twój profil i lajkują filmy, które im się podobają, w miesięcznym pakiecie, za który płacisz przez Stripe i który anulujesz na swoim koncie.",
        "hero": {"image": "tiktok-likes", "alt": "Polubienia od prawdziwych widzów pod filmem na TikToku, bez żadnych skrótów"},
        "sections": [
            {
                "h2": "Sygnały ostrzegawcze u sprzedawcy polubień na TikToku",
                "ul": [
                    "Tysiące polubień obiecane w ciągu godziny.",
                    "Cena za tysiąc polubień niższa niż kawa.",
                    "Prośba o hasło do TikToka albo o logowanie przez TikToka.",
                    "Brak nazwy firmy, adresu i regulaminu.",
                    "Polubienia sprzedawane pod dowolny link, bez słowa o tym, kto miałby oglądać.",
                ],
            },
            {
                "h2": "Co czyni nas uczciwym serwisem",
                "p": [
                    "Jesteśmy Growsterr, stworzeni przez zespół Sterr Agency (Sterr Technologies OÜ z Tallinna w Estonii). Rozwijamy konta promowanymi kampaniami w naszej sieci partnerskiej, które pokazują je prawdziwym ludziom, i mówimy wprost, czego nie możemy: nie obiecujemy liczb, a polubienia nigdy nie są sprzedawane osobno.",
                    "Twój panel pokazuje, co zmierzyliśmy: wizyty na profilu z każdego dnia i to, ile z nich zamieniło się w obserwowania.",
                ],
            },
            {
                "h2": "Bezpieczne także dla Twoich filmów",
                "p": [
                    "Polubienia od botów nie tylko później znikają. Dopóki są, zniekształcają obraz: mnóstwo serc, mało czasu oglądania, zero komentarzy. Prawdziwe polubienia zostawiają ludzie, którzy obejrzeli, więc liczby pod Twoim filmem do siebie pasują.",
                ],
            },
        ],
        "faqs": [
            ("Skąd mam wiedzieć, że Growsterr to nie oszustwo?", "Spójrz, o co prosimy i co obiecujemy. Prosimy o nazwę użytkownika, nigdy o hasło. Podajemy typowe zakresy, nigdy dokładne liczby. Płatność idzie przez Stripe, a rezygnujesz na swoim koncie, bez pytania kogokolwiek."),
            ("Czy mogę dostać zwrot za polubienia?", "Pakiety to miesięczne subskrypcje. Jeśli zrezygnujesz, opłacony miesiąc trwa dalej i nie jest zwracany, a po nim nic więcej nie jest pobierane."),
            ("Czy uczciwe polubienia będą wyglądać inaczej niż te, które kupowałem wcześniej?", "Zwykle tak. Przychodzą przez kilka dni, rozkładają się na Twoje filmy i idą w parze z wyświetleniami, obserwowaniami i komentarzami od tych samych ludzi. Polubienia od botów zwykle lądują jednym blokiem pod jednym filmem."),
            ("Z kim mogę porozmawiać, jeśli coś wygląda źle?", "Z człowiekiem z naszego zespołu, mailem lub na WhatsAppie. {pro_name} ma też bezpośrednią linię na WhatsAppie."),
            ("Czy płacenie za polubienia na TikToku w ogóle jest w porządku?", "Płacenie za boty nie jest: dostajesz liczbę, za którą nikt nie stoi. Płacenie za to, żeby prawdziwi ludzie zobaczyli Twoje filmy, to co innego, tak jak firma płaci, żeby ją zauważono. Taki wzrost sprzedajemy."),
        ],
    },
    {
        "service": "likes",
        "modifier": "comment-likes",
        "slug": "tiktok/polubienia/pod-komentarzami",
        "label": "Polubienia komentarzy na TikToku",
        "title": "Polubienia komentarzy na TikToku? Co robią widzowie | Growsterr",
        "description": "Chcesz kupić polubienia komentarzy na TikToku? Nie sprzedajemy ich. Prawdziwi widzowie czytają sekcję komentarzy i lajkują odpowiedzi, które do nich trafiają.",
        "h1": ("Polubienia komentarzy na TikToku? ", "Niech prawdziwi widzowie zdecydują, co warto."),
        "intro": "Jeśli chciałeś kupić polubienia komentarzy na TikToku, żeby wynieść na górę przypięty komentarz albo odpowiedź, oto prosta odpowiedź: nie sprzedajemy polubień pod pojedyncze komentarze. Nasze kampanie prowadzą prawdziwych ludzi na Twój profil, a ci, którzy czytają sekcję komentarzy, lajkują komentarze, z którymi się zgadzają, także Twoje.",
        "hero": {"image": "tiktok-watch-time", "alt": "Widz czyta sekcję komentarzy na TikToku i lajkuje odpowiedź"},
        "sections": [
            {
                "h2": "Dlaczego nie sprzedajemy polubień komentarzy",
                "p": [
                    "Komentarz z setkami polubień i bez odpowiedzi wygląda dziwnie dla każdego, kto przewija obok. Polubienia komentarzy od botów też nie wskazują niczego przydatnego: lądują, wiszą i nic nie mówią o tym, czy komentarz był dobry.",
                    "Nie możemy też wypchnąć komentarza wyżej pod cudzym filmem. Nasze kampanie pokazują ludziom Twój profil; to, co dzieje się w sekcjach komentarzy innych twórców, zależy od ich widzów.",
                ],
            },
            {
                "h2": "Komentarze, które ludzie naprawdę lajkują",
                "ul": [
                    "Przypnij komentarz, który coś dodaje: link do drugiej części, odpowiedź na pytanie, które wszyscy zadają.",
                    "Odpowiadaj, póki film jest świeży, gdy w komentarzach dzieje się najwięcej.",
                    "Zadaj pytanie w opisie, żeby widzowie mieli o czym rozmawiać.",
                    "Pisz krótko i swoim głosem; ludzie lajkują komentarze, które brzmią jak Ty.",
                ],
            },
            {
                "h2": "Skąd biorą się polubienia komentarzy w pakiecie",
                "p": [
                    "Każdy pakiet przynosi polubienia i komentarze pod Twoimi filmami od tych samych ludzi; w ciągu miesiąca {pick_name} oznacza zwykle {pick_likes} polubień i {pick_comments} komentarzy. Ci ludzie często lajkują przy czytaniu inne komentarze, ale tego nie liczymy ani nie sterujemy.",
                ],
            },
        ],
        "faqs": [
            ("Czy możecie dać polubienia mojemu komentarzowi pod filmem dużego twórcy?", "Nie. Nasze kampanie zawsze rozwijają wyłącznie Twój własny profil. Wypchnięcie komentarza w cudzej sekcji komentarzy oznaczałoby wysłanie tam kont, żeby go polubiły, a to dokładnie zadanie, do którego robi się boty."),
            ("Czy Wasze pakiety obejmują polubienia komentarzy?", "Nie jako liczbę. Pakiety obejmują polubienia pod Twoimi filmami i komentarze pisane przez prawdziwych ludzi. Ci sami ludzie czasem lajkują komentarze, które czytają, ale to ich wybór i nie mierzymy go."),
            ("Jak sprawić, żeby mój przypięty komentarz zbierał polubienia?", "Przypięty komentarz już jest na górze. Polubienia zdobywa, gdy jest wart przeczytania: dopowiedzenie, odpowiedź, puenta. Prawdziwi widzowie lajkują go, gdy coś dodaje do filmu."),
            ("Czy kupione polubienia komentarzy pomogłyby mojemu filmowi?", "Nie w żaden sposób, który się liczy. Polubienie komentarza z konta, które nigdy nie obejrzało filmu, nic nie zmienia w wynikach filmu, a wysyp takich polubień pod jednym komentarzem łatwo wypatrzyć."),
            ("Który pakiet przynosi najwięcej ruchu w komentarzach?", "{pro_name}, zwykle {pro_comments} komentarzy miesięcznie, potem {rising_name} z {rising_comments}. Więcej komentarzy to bardziej ruchliwa sekcja komentarzy, a ruchliwe sekcje komentarzy ludzie czytają."),
        ],
    },
    {
        "service": "likes",
        "modifier": "private-account",
        "slug": "tiktok/polubienia/konto-prywatne",
        "label": "Polubienia na prywatnym koncie na TikToku",
        "title": "Polubienia na prywatne konto na TikToku? | Growsterr",
        "description": "Czy można kupić polubienia na prywatne konto na TikToku? Filmy widzą tylko zatwierdzeni obserwujący, więc nowi ludzie ich nie polubią. Oto co działa.",
        "h1": ("Polubienia na prywatnym koncie na TikToku? ", "Najpierw ludzie muszą zobaczyć filmy."),
        "intro": "Jeśli chcesz kupić polubienia na prywatne konto na TikToku, najpierw poznaj haczyk: na prywatnym koncie Twoje filmy mogą oglądać tylko zaakceptowani obserwujący. Nowi ludzie ich nie widzą, więc nie mogą ich polubić. Nasze pakiety sprowadzają prawdziwych widzów, dlatego na czas działania potrzebują publicznego profilu.",
        "hero": {"image": "tiktok-watch-time", "alt": "Film na TikToku ustawiony jako publiczny, żeby nowi widzowie mogli go obejrzeć i polubić"},
        "sections": [
            {
                "h2": "Kto może polubić prywatny film",
                "p": [
                    "Na prywatnym koncie na TikToku Twoje filmy trafiają tylko do zaakceptowanych obserwujących. Wszyscy inni widzą zablokowany profil. Polubienie wymaga wyświetlenia, a wyświetlenie wymaga dostępu, więc polubienia mogą przyjść tylko od osób, które już wpuściłeś.",
                    "To odwrotność tego, do czego służy pakiet wzrostu. Nasze kampanie istnieją po to, by docierać do ludzi, którzy jeszcze Cię nie znają, a oni mogą polubić tylko to, co wolno im obejrzeć.",
                ],
            },
            {
                "h2": "Publiczne konto z prywatnymi chwilami",
                "ul": [
                    "Ustaw konto jako publiczne, żeby nowi ludzie mogli Cię znaleźć i polubić to, co zobaczą.",
                    "Osobiste filmy ogranicz do Znajomych albo Tylko dla Ciebie; ludzie z kampanii ich nie zobaczą.",
                    "Wyłącz duety, stitche albo pobieranie przy wybranych filmach, jeśli chcesz mieć większą kontrolę.",
                    "Używaj filtrów komentarzy na TikToku, żeby rozmowa wyglądała tak, jak chcesz.",
                ],
            },
            {
                "h2": "Co przynosi publiczny miesiąc",
                "p": [
                    "Gdy konto jest publiczne, ludzie z naszej kampanii mogą obejrzeć wszystko, co udostępniłeś wszystkim. Z pakietem {pick_name} to zwykle {pick_likes} polubień miesięcznie, razem z {pick_audience} nowych obserwujących.",
                ],
            },
        ],
        "faqs": [
            ("Czy polubienia trafią pod filmy ustawione jako prywatne?", "Nie. Filmy ustawione dla Znajomych albo Tylko dla Ciebie widzą tylko te osoby, więc ludzie z kampanii nie mogą ich obejrzeć ani polubić. Polubienia od nowych widzów dostają tylko filmy, które widzą wszyscy."),
            ("Czy po skończonym miesiącu mogę wrócić do konta prywatnego?", "Tak. Po zakończeniu pakietu możesz znowu przejść na prywatne. Polubienia, które już są pod filmami, zostają, ale nowi ludzie nie będą mogli ich obejrzeć."),
            ("Czy mogę zostać na prywatnym koncie i dostawać polubienia tylko od obserwujących?", "Twoi obecni obserwujący mogą lajkować, co chcą; nie możemy ich do tego zmusić. Nasze kampanie działają przez pokazywanie Twojego profilu nowym ludziom, a to pomaga tylko wtedy, gdy mogą zobaczyć Twoje filmy."),
            ("Czy przejście z prywatnego na publiczne jest ryzykowne?", "To ustawienie, które kontrolujesz i możesz cofnąć. Przed przełączeniem sprawdź, które filmy są ustawione dla wszystkich, i przenieś osobiste do Znajomych albo Tylko dla Ciebie."),
            ("Czy ktoś potrzebuje dostępu do mojego konta, żeby wysłać polubienia?", "Nikt nie powinien. Pracujemy wyłącznie na podstawie nazwy użytkownika i nigdy nie logujemy się na Twoje konto. Jeśli serwis potrzebuje Twojego logowania, żeby wrzucić polubienia na prywatne konto, zachowaj logowanie dla siebie."),
        ],
    },
    {
        "service": "likes",
        "modifier": "live",
        "slug": "tiktok/polubienia/live",
        "label": "Polubienia na LIVE na TikToku",
        "title": "Polubienia na LIVE na TikToku? Potrzebni widzowie | Growsterr",
        "description": "Chcesz kupić polubienia na LIVE na TikToku? Stuknięcia dają ludzie w pokoju. Rozwijamy obserwujących, którzy mogą wpaść, a polubień na LIVE nie wysyłamy.",
        "h1": ("Polubienia na LIVE na TikToku? ", "Zapełnij pokój, a stuknięcia przyjdą."),
        "intro": "Jeśli chcesz kupić polubienia na LIVE na TikToku, warto wiedzieć, czym są: stuknięciami w ekran od ludzi, którzy właśnie oglądają Twoją transmisję. Nie wysyłamy stuknięć na LIVE i nikt nie wyśle prawdziwych. Rozwijamy publiczność, która może dołączyć: prawdziwych obserwujących, którzy trafili na Twoje filmy i spodobały im się na tyle, żeby zostać.",
        "hero": {"image": "tiktok-likes", "alt": "Serca unoszą się na ekranie podczas LIVE na TikToku z prawdziwymi widzami"},
        "sections": [
            {
                "h2": "Co naprawdę mierzą polubienia na LIVE",
                "p": [
                    "Polubienia na LIVE to puls pokoju. Widz może stukać, ile chce, więc transmisja z kilkoma zaangażowanymi osobami potrafi ich zebrać sporo. Stuknięcia pokazują Tobie i każdemu, kto wpada, że ludziom, którzy oglądają, się podoba.",
                    "Stuknięcia wysłane z kont, które nie oglądają, nie pokazują niczego takiego. Czat milczy, serca nie pasują do tego, co dzieje się na ekranie, a każdy, kto dołącza, to czuje.",
                ],
            },
            {
                "h2": "Jak pakiet pomaga Twoim transmisjom",
                "p": [
                    "Pokoju nie kupisz, ale możesz powiększyć grono ludzi, którzy mogą do niego wejść. Każdy obserwujący z naszych kampanii to ktoś, kto wybrał Twoje filmy, a Twoi obserwujący to publiczność, od której zaczyna się każdy LIVE.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Twórca rozmawia z widzami podczas LIVE na TikToku z domowego studia"},
            },
            {
                "h2": "Więcej stuknięć od ludzi, którzy dołączają",
                "ul": [
                    "Ustaw cel na ekranie albo zrób głosowanie stuknięciami, żeby widzowie mieli powód stukać.",
                    "Reaguj na głos, gdy serca rosną; ludzie stukają więcej, gdy widzą, że to trafia.",
                    "Zadbaj o żywe pierwsze minuty, bo wtedy nowi decydują, czy zostać.",
                    "Dziękuj stałym widzom po imieniu: pokój, który czuje się jak społeczność, tak też stuka.",
                ],
            },
        ],
        "faqs": [
            ("Czy mogę kupić polubienia na LIVE na TikToku, który trwa teraz?", "Nie. Nie wysyłamy na transmisje polubień, widzów ani komentarzy. Prawdziwi ludzie dołączają do LIVE, gdy go zobaczą i mają ochotę, a tego nikt nie zaplanuje."),
            ("Czy Wasze pakiety dają polubienia na transmisjach LIVE?", "Nie bezpośrednio. Pakiety przynoszą obserwujących oraz polubienia i komentarze pod Twoimi filmami. Część tych obserwujących może dołączać do Twoich LIVE i stukać; to zależy od nich i tego nie liczymy."),
            ("Czy potrzebuję 1000 obserwujących, zanim polubienia na LIVE zaczną mieć znaczenie?", "Sam LIVE jest zablokowany, dopóki konto nie ma 1000 obserwujących. Jeśli jeszcze tam nie jesteś, najpierw rozwijaj obserwujących; polubienia na LIVE przyjdą później, od ludzi, którzy zostaną."),
            ("Dlaczego mam mało polubień na LIVE mimo wielu obserwujących?", "Obserwujący, którzy nigdy nie oglądają, nie dołączają do transmisji. Jeśli liczbę zbudowano na botach, LIVE będzie pusty. Stuknięcia przynoszą prawdziwi obserwujący, regularne transmisje i żywy początek."),
            ("Czy polubienia na LIVE wpływają na to, kto zobaczy moją transmisję?", "TikTok nie publikuje dokładnie, jak wybiera LIVE do pokazania, ale pokój, w którym ludzie zostają, piszą na czacie i stukają, daje mu z czym pracować. Pokój pełen milczących kont nie daje nic."),
        ],
    },
    # --- Views: the ways people ask for them --------------------------------------------------
    {
        "service": "views",
        "modifier": "real",
        "slug": "tiktok/wyswietlenia/prawdziwe",
        "label": "Prawdziwe wyświetlenia na TikToku",
        "title": "Prawdziwe wyświetlenia na TikToku, jakość mierzalna | Growsterr",
        "description": "Kup prawdziwe wyświetlenia na TikToku od ludzi, a nie skryptów: widzów, którzy oglądają, otwierają Twój profil i obserwują, gdy chcą więcej.",
        "h1": ("Prawdziwe wyświetlenia na TikToku, ", "od ludzi, którzy sami klikają play."),
        "intro": "Gdy kupujesz prawdziwe wyświetlenia na TikToku w pakiecie Growsterr, płacisz za ludzi: prawdziwych widzów, którzy odkrywają Twój profil, sami klikają play i oglądają tak długo, jak film ich trzyma. Jakość to nie poziom, który wybierasz. To to, co dostajesz, gdy za każdym wyświetleniem stoi człowiek.",
        "hero": {"image": "tiktok-watch-time", "alt": "Prawdziwy widz włącza film twórcy na TikToku"},
        "sections": [
            {
                "h2": "Jak ocenić jakość wyświetleń na TikToku",
                "ul": [
                    "Czas oglądania: prawdziwi widzowie zostają, gdy film jest dobry, i odchodzą, gdy nie jest.",
                    "Wizyty na profilu: ludzie, którym film się podoba, otwierają Twój profil, żeby zobaczyć więcej.",
                    "Obserwowania i polubienia: część widzów chce więcej i to pokazuje.",
                    "Komentarze: prawdziwa publiczność odpowiada, własnymi słowami.",
                    "Udostępnienia: najwyraźniejszy znak ze wszystkich, a robią to tylko ludzie.",
                ],
            },
            {
                "h2": "Prawdziwe wyświetlenia zaczynają się na Twoim profilu",
                "p": [
                    "Nasze kampanie przedstawiają Twój profil prawdziwym widzom w całej naszej sieci partnerskiej. Ciekawi otwierają go na TikToku i zaczynają oglądać, i stąd biorą się Twoje wyświetlenia. Dlatego też mierzymy wizyty na profilu: wizyta to przybywający człowiek, a wyświetlenia idą za nim.",
                    "Masowe wyświetlenia pomijają ten krok. Są kierowane na pojedynczy link do filmu, odtwarzane przez program i znikają po sekundzie.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Nowi widzowie otwierają profil twórcy na TikToku i przeglądają jego filmy"},
            },
        ],
        "faqs": [
            ("Jaka jest różnica między prawdziwymi a wysokiej jakości wyświetleniami?", "Dla nas żadna. Prawdziwe wyświetlenie pochodzi od człowieka, który zdecydował się obejrzeć, a to jedyna jakość, która się liczy. Etykiety jakości na paczkach wyświetleń zwykle znaczą tylko tyle, że konta mają zdjęcie profilowe."),
            ("Czy możecie pokazać mi wyświetlenia, które przynieśliście?", "Pokazujemy to, co mierzymy: dzienne wizyty na Twoim profilu z kampanii i część z nich, która zamieniła się w obserwowania. Twoje wyświetlenia widać we własnych statystykach TikToka, razem z czasem oglądania."),
            ("Czy prawdziwe wyświetlenia liczą się tak samo jak inne?", "W liczniku wyświetlenie to wyświetlenie. Różnica to wszystko wokół: prawdziwi widzowie oglądają, reagują i czasem obserwują, a to pomaga filmowi dotrzeć do większej liczby ludzi."),
            ("Dlaczego nie sprzedajecie wyświetleń bez obserwujących?", "Bo prawdziwi widzowie nie przychodzą w osobnych kawałkach. Ta sama osoba, która ogląda, może polubić, skomentować albo zacząć obserwować, więc sprowadzamy ludzi, a nie liczbę odtworzeń, i wszystko jest w jednym pakiecie."),
            ("Czy prawdziwe wyświetlenia przychodzą wolniej niż kupione?", "Tak. Ludzie przychodzą przez cały dzień, każdego dnia miesiąca. Wszystko, co ląduje szybciej, niż ludzie mogą znaleźć film, to nie ludzie."),
        ],
    },
    {
        "service": "views",
        "modifier": "organic",
        "slug": "tiktok/wyswietlenia/organiczne",
        "label": "Organiczne wyświetlenia na TikToku",
        "title": "Organiczne wyświetlenia na TikToku z Twojej okolicy | Growsterr",
        "description": "Kup organiczne wyświetlenia na TikToku od ludzi tam, gdzie mieszka Twoja publiczność, w mieście, regionie lub kraju. Prawdziwi widzowie oglądają, bo chcą.",
        "h1": ("Organiczne wyświetlenia na TikToku ", "od ludzi tam, gdzie mieszka Twoja publiczność."),
        "intro": "Żeby kupić organiczne wyświetlenia na TikToku, które coś znaczą, liczą się dwie rzeczy: prawdziwy człowiek zdecydował się obejrzeć i jest to właściwy człowiek. Nasze pakiety dbają o obie. Kierujemy Twój profil do prawdziwych ludzi w wybranym przez Ciebie miejscu, a wyświetlenia dają ci, którzy się zatrzymują i oglądają.",
        "hero": {"image": "tiktok-watch-time", "alt": "Ludzie z jednego miasta oglądają filmy lokalnego twórcy na TikToku"},
        "sections": [
            {
                "h2": "Wyświetlenia na TikToku kierowane według miejsca",
                "p": [
                    "Restauracja w Łodzi potrzebuje wyświetleń z Łodzi. Twórca nagrywający po polsku chce widzów, którzy rozumieją polski. Sklep, który wysyła tylko w Polsce, niewiele zyska na wyświetleniach z innego kontynentu. Wybór miejsca to najprostszy sposób, żeby wyświetlenia się liczyły.",
                    "Podaj w zamówieniu miasto, region lub kraj, a kampania zacznie właśnie tam.",
                ],
            },
            {
                "h2": "Co sprawia, że wyświetlenie jest organiczne",
                "ul": [
                    "Nikt nie zapłacił widzowi, nie poprosił go ani nie kazał mu oglądać według skryptu.",
                    "Dotarł do Twojego filmu z Twojego profilu i sam kliknął play.",
                    "Mógł przewinąć dalej, ale tego nie zrobił.",
                    "To, co zrobi potem, polubienie, obserwowanie, udostępnienie albo nic, zależy od niego.",
                ],
            },
            {
                "h2": "Dlaczego wyświetlenia z właściwego miejsca idą dalej",
                "p": [
                    "Wyświetlenia z właściwego miejsca przychodzą z resztą: komentarzami w języku, w którym możesz odpowiedzieć, obserwowaniami od ludzi, którzy mogą naprawdę przyjść do Twojego lokalu, udostępnieniami znajomym z okolicy. Wyświetlenie z drugiego końca świata, od kogoś, kogo to nie obchodzi, nie daje nic z tego.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Właściciel małej firmy nagrywa film na TikToka dla klientów ze swojego miasta"},
            },
        ],
        "faqs": [
            ("Czy mogę kierować wyświetlenia na TikToku według kraju?", "Tak, albo według miasta lub regionu. Podaj miejsce przy zamówieniu; ludzie stamtąd zobaczą Twój profil najpierw, a gdy najlepsze dopasowanie jest nieco szersze, część widzów może przyjść z okolicy."),
            ("Czy kierowane wyświetlenia są wciąż organiczne?", "Tak. Wybór, kto zobaczy Twój profil, nie wybiera, kto obejrzy. Każda osoba w tym miejscu sama decyduje, czy Twój film jest wart jej czasu."),
            ("Co, jeśli moja publiczność jest w kilku krajach?", "Wskaż region, który je obejmuje, albo kraj, który liczy się najbardziej. Jeśli potrzebujesz czegoś bardziej szczegółowego, napisz do nas przed zamówieniem."),
            ("Czy wyświetlenia będą się zgadzać ze strefą czasową mojej publiczności?", "Prawdziwi ludzie przeglądają, gdy nie śpią, więc wyświetlenia z wybranego miejsca zwykle idą za tamtejszym dniem. Wyświetleniom od botów jest obojętne, która jest u Ciebie godzina."),
            ("Czy organiczne wyświetlenia przychodzą z obserwującymi?", "Tak. Widzowie, którzy oglądają, to ci sami ludzie, którzy obserwują: z pakietem {pick_name} to zwykle {pick_audience} nowych obserwujących miesięcznie, z ich polubieniami i komentarzami."),
        ],
    },
    {
        "service": "views",
        "modifier": "monthly",
        "slug": "tiktok/wyswietlenia/co-miesiac",
        "label": "Wyświetlenia na TikToku pod każdy film",
        "title": "Wyświetlenia na TikToku pod wiele filmów, co miesiąc | Growsterr",
        "description": "Kup wyświetlenia na TikToku pod wiele filmów w jednym pakiecie: prawdziwi ludzie przeglądają Twój profil i oglądają to, co ich złapie, przez cały miesiąc.",
        "h1": ("Wyświetlenia na TikToku pod wiele filmów, ", "przez cały miesiąc, od prawdziwych ludzi."),
        "intro": "Chcesz kupić wyświetlenia na TikToku pod wiele filmów bez zamawiania pod każdy osobno? Miesięczny pakiet obejmuje cały Twój profil. Prawdziwi ludzie odkrywają Cię każdego dnia, a gdy już są na profilu, oglądają więcej niż jeden film: najnowszy, przypięte, cokolwiek ich złapie. Wyświetlenia rosną z czasem, pod wszystkim, co publikujesz.",
        "hero": {"image": "tiktok-watch-time", "alt": "Widz przewija kilka filmów na profilu twórcy na TikToku"},
        "sections": [
            {
                "h2": "Jeden pakiet, każdy film",
                "p": [
                    "Paczki wyświetleń pod pojedyncze filmy zmuszają do wyboru: ten dostaje pomoc, tamten nie, a za tydzień zamawiasz znowu. Miesięczny pakiet działa na poziomie profilu. Każdy film, który opublikujesz w tym miesiącu, czeka na ludzi, których sprowadzamy, tak samo jak wszystko, co opublikowałeś wcześniej.",
                    "{rising_name} i {pro_name} pozwalają też wskazać filmy, które mają dostać najwięcej uwagi.",
                ],
            },
            {
                "h2": "Autowyświetlenia na TikToku i dlaczego ich nie robimy",
                "p": [
                    "Autowyświetlenia wysyłają ustaloną liczbę odtworzeń pod każdy nowy film w chwili publikacji. Każdy film dostaje ten sam skok, czy to najlepszy, czy najsłabszy, a za żadnym z tych odtworzeń nie stoi widz. Ten wzór łatwo wypatrzyć.",
                ],
            },
            {
                "h2": "Więcej wyświetleń z czasem",
                "ul": [
                    "Przypnij trzy najmocniejsze filmy, bo przypięte są na profilu na samej górze.",
                    "Zrób serię, żeby ludzie mieli powód obejrzeć następną i poprzednią część.",
                    "Dbaj o porządny profil i jasne bio, żeby odwiedzający wiedzieli, czego się spodziewać.",
                    "Starsze filmy zbierają wyświetlenia tak długo, jak przychodzą nowi ludzie.",
                ],
            },
        ],
        "faqs": [
            ("Czy pakiet obejmuje każdy film, który publikuję?", "Tak. Kampania sprowadza ludzi na Twój profil, a nie pod pojedynczy link, więc można obejrzeć wszystko, co jest na nim publiczne. Najwięcej zwykle dostają nowe filmy, bo są blisko góry tego, co widzą odwiedzający."),
            ("Jak wyświetlenia dzielą się między moje filmy?", "Według widzów. Oglądają to, co ich interesuje, więc najmocniejsze filmy zbierają więcej. Nie dzielimy żadnej liczby między nie, bo takiej liczby nie ma."),
            ("Czy starsze filmy będą dalej zbierać wyświetlenia?", "Tak, dopóki nowi ludzie odkrywają Twój profil. Każdy miesiąc przynosi świeżą publiczność, która może przewinąć wstecz to, co opublikowałeś wcześniej."),
            ("Czy to to samo co autowyświetlenia na TikToku?", "Nie. Autowyświetlenia same wystrzeliwują odtworzenia pod każdy nowy post. Nasz pakiet sam się odnawia, ale wyświetlenia dają ludzie, którzy zdecydowali się obejrzeć."),
            ("Czy mogę dostać wyświetlenia na więcej niż jedno konto na TikToku?", "Każdy pakiet rozwija jedno konto. Jeśli prowadzisz kilka, uruchom pakiet dla każdego; wszystkie są na tym samym koncie Growsterr."),
        ],
    },
    {
        "service": "views",
        "modifier": "gradual",
        "slug": "tiktok/wyswietlenia/stopniowo",
        "label": "Wyświetlenia na TikToku stopniowo",
        "title": "Wyświetlenia na TikToku powoli, naturalny rytm | Growsterr",
        "description": "Kup wyświetlenia na TikToku powoli, bez kroplówki: prawdziwi ludzie codziennie trafiają na Twój profil i oglądają we własnym tempie, w miesięcznym pakiecie.",
        "h1": ("Wyświetlenia na TikToku powoli, ", "jeden prawdziwy widz po drugim."),
        "intro": "Chcesz kupić wyświetlenia na TikToku powoli, żeby wyglądały naturalnie? Odpuść kroplówkę. Naturalnie wyglądają wyświetlenia od ludzi. Nasze pakiety sprowadzają prawdziwych widzów na Twój profil każdego dnia miesiąca, a oni oglądają Twoje filmy, gdy na nie trafią, w tempie, w jakim ludzie naprawdę przeglądają.",
        "hero": {"image": "tiktok-watch-time", "alt": "Wyświetlenia na TikToku rosną dzień po dniu, gdy prawdziwi ludzie znajdują filmy twórcy"},
        "sections": [
            {
                "h2": "Kształt prawdziwych wyświetleń",
                "p": [
                    "Prawdziwe wyświetlenia nie przychodzą w linii prostej. Film dostaje pierwszą falę od ludzi, którzy widzą go wcześnie, potem długi ogon od widzów, którzy znajdują go na Twoim profilu dni albo tygodnie później. Każdy nowy obserwujący to nowy widz całego Twojego archiwum.",
                    "Wyświetlenia z kroplówki spłaszczają ten kształt w równą rampę: ustalona liczba na godzinę, z kont, które odchodzą po sekundzie. Wygląda to wolno, ale nie wygląda prawdziwie.",
                ],
            },
            {
                "h2": "Wyświetlenia, które idą w parze z resztą",
                "ul": [
                    "Gdy rosną wyświetlenia, rosną z nimi polubienia i obserwowania, bo wszystkie trzy robią ci sami ludzie.",
                    "Starsze filmy wciąż są oglądane, gdy nowi ludzie przeglądają Twój profil.",
                    "Ruchliwe i spokojne dni się przeplatają, jak u każdego twórcy.",
                ],
            },
            {
                "h2": "Co mierzymy my, a co TikTok",
                "p": [
                    "Nie liczymy wyświetleń z góry i nie udajemy, że to robimy. Twój panel pokazuje, co zmierzył nasz system: wizyty na profilu z kampanii i obserwujących, w których się zamieniły, dzień po dniu. Statystyki TikToka pokazują Twoje wyświetlenia, a gdy stoją za nimi prawdziwi ludzie, jedno i drugie opowiada tę samą historię.",
                ],
            },
        ],
        "faqs": [
            ("Ile wyświetleń dziennie dostaną moje filmy?", "To zależy bardziej od Twoich filmów niż od nas. Sprowadzamy na Twój profil równy strumień prawdziwych ludzi; ile filmów obejrzą i jak często, to ich wybór."),
            ("Dlaczego wyświetlenia przychodzą falami, a nie równo?", "Bo ludzie nie przeglądają równo. Wieczory, weekendy i nowy film robią dni bardziej ruchliwymi. Równy strumień wyświetleń co godzinę to wytwór maszyny."),
            ("Czy starsze filmy też dostają wyświetlenia?", "Często. Ludzie, którym spodoba się jeden film, zwykle otwierają Twój profil i oglądają więcej. To jeden z najlepszych śladów, jakie zostawia prawdziwa publiczność."),
            ("Czy mogę rozłożyć wyświetlenia na konkretne filmy?", "Z pakietem {rising_name} lub {pro_name} decydujesz, które filmy kampania faworyzuje; ludzie, których sprowadzamy, i tak oglądają we własnym tempie."),
            ("Czy tempo będzie się zmieniać z miesiąca na miesiąc?", "Trochę. Każdy miesiąc przynosi nowych ludzi, a to, co publikujesz, wpływa na to, ile oglądają. Miesiąc mocnych filmów zwykle jest bardziej ruchliwy."),
        ],
    },
    {
        "service": "views",
        "modifier": "no-drop",
        "slug": "tiktok/wyswietlenia/bez-spadkow",
        "label": "Wyświetlenia na TikToku bez spadków",
        "title": "Wyświetlenia na TikToku bez spadków, od ludzi | Growsterr",
        "description": "Kup wyświetlenia na TikToku bez spadków: wyświetlenia od prawdziwych ludzi to zwykłe odtworzenia, które zostają policzone. Bez obietnic uzupełnień.",
        "h1": ("Wyświetlenia na TikToku, które nie spadają: ", "zacznij od ludzi, którzy obejrzeli."),
        "intro": "Jeśli chcesz kupić wyświetlenia na TikToku bez spadków, zobacz najpierw, dlaczego wyświetlenia w ogóle spadają: nigdy nie były prawdziwymi odtworzeniami, a TikTok je odebrał. Nasze pakiety sprowadzają prawdziwych ludzi, którzy oglądają Twoje filmy, a ich wyświetlenia to zwykłe wyświetlenia od zwykłych widzów. Nie ma czego odbierać.",
        "hero": {"image": "tiktok-watch-time", "alt": "Licznik wyświetleń na TikToku trzyma się, bo oglądali prawdziwi ludzie"},
        "sections": [
            {
                "h2": "Dlaczego niektóre liczniki wyświetleń spadają",
                "p": [
                    "TikTok pracuje nad tym, żeby fałszywe zaangażowanie nie zostawało na platformie, a gdy usuwa nieautentyczne odtworzenia albo konta, które za nimi stoją, licznik się koryguje. Dlatego film może jednego dnia pokazywać więcej wyświetleń niż następnego. Etykieta „bez spadków” na paczce odtworzeń nie zmienia tego, czym te odtworzenia są.",
                ],
            },
            {
                "h2": "Co sprawia, że wyświetlenie zostaje",
                "ul": [
                    "Prawdziwy człowiek kliknął play, na własnym telefonie, z własnego wyboru.",
                    "Znalazł Twój film przez Twój profil, a nie przez link wrzucony do skryptu.",
                    "Jego wyświetlenie przychodzi z polubieniami, obserwowaniami i komentarzami, które razem mają sens.",
                ],
            },
            {
                "h2": "Prawdziwe wyświetlenia bez spadków, w uczciwej wersji",
                "p": [
                    "Nie obiecamy, że liczba nigdy się nie ruszy, bo TikTok prowadzi własne liczniki. Możemy powiedzieć, że każde wyświetlenie od nas to czyjaś własna decyzja o obejrzeniu, czyli jedyny rodzaj wyświetlenia, którego czystka nie ma powodu ruszać.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Twórca sprawdza statystyki TikToka po miesiącu wyświetleń od prawdziwych ludzi"},
            },
        ],
        "faqs": [
            ("Czy moje wyświetlenia spadną po kampanii?", "Wyświetlenia od prawdziwych ludzi liczą się jak każde inne, więc nie ma powodu, żeby znikały, gdy pakiet się kończy. Po prostu rosną wolniej, gdy nowi ludzie przestają przychodzić."),
            ("Dlaczego wyświetlenia „bez spadków” z innych stron i tak spadają?", "Bo „bez spadków” opisuje nadzieję, a nie wyświetlenia. Jeśli odtworzenia pochodziły od botów albo skryptów, mogą zostać usunięte, cokolwiek mówi etykieta."),
            ("Ile moich wyświetleń zostanie?", "Wszystkie, które dadzą Ci prawdziwi ludzie. Nie liczymy wyświetleń z góry, bo zależą od tego, ile filmów obejrzy każda osoba, ale każde pochodzi od prawdziwego człowieka."),
            ("Czy wyświetlenia zostają, jeśli usunę film i opublikuję go ponownie?", "Nie. Usunięty film zabiera swoje wyświetlenia, kto by ich nie dał. Ponowna publikacja startuje od zera, więc zwykle lepiej zostawić film i pozwolić ludziom go dalej znajdować."),
            ("Czy prawdziwe wyświetlenia przychodzą też z polubieniami?", "Tak. Ci sami widzowie lajkują, komentują i obserwują, gdy chcą, co z pakietem {pick_name} zwykle daje {pick_likes} polubień i {pick_comments} komentarzy miesięcznie."),
        ],
    },
    {
        "service": "views",
        "modifier": "safe",
        "slug": "tiktok/wyswietlenia/bezpiecznie",
        "label": "Bezpieczne wyświetlenia na TikToku",
        "title": "Bezpieczne wyświetlenia na TikToku, bez botów | Growsterr",
        "description": "Czy kupno wyświetleń na TikToku jest bezpieczne? Wyświetlenia od botów psują statystyki i znikają. Prawdziwi widzowie, bez logowania, płatność przez Stripe.",
        "h1": ("Kup wyświetlenia na TikToku bezpiecznie: ", "czyste konto i czyste statystyki."),
        "intro": "Żeby bezpiecznie kupić wyświetlenia na TikToku, pomyśl o czymś więcej niż hasło. Wyświetlenia od botów wykrzywiają też Twoje statystyki, więc przestajesz wiedzieć, które filmy działają. Nasze pakiety sprowadzają prawdziwych ludzi, którzy odkrywają Twój profil i oglądają sami. Bez logowania, bez skryptów, bez niczego, co dotyka Twojego konta, a liczby w statystykach zostają uczciwe.",
        "hero": {"image": "tiktok-watch-time", "alt": "Czyste statystyki TikToka z wyświetleniami i czasem oglądania od prawdziwych ludzi"},
        "sections": [
            {
                "h2": "Ukryty koszt niebezpiecznych wyświetleń",
                "p": [
                    "Statystyki TikToka to sposób, w jaki się uczysz: które haczyki trzymają ludzi, które dźwięki działają, które tematy przynoszą obserwujących. Wyświetlenia od botów zalewają to wszystko szumem. Średni czas oglądania się sypie, źródła ruchu przestają mieć sens, a Ty kopiujesz film, który tylko wyglądał, jakby zadziałał.",
                ],
            },
            {
                "h2": "Czy to uczciwy sposób na wyświetlenia na TikToku?",
                "p": [
                    "Nie sprzedajemy wyświetleń jako produktu. Sprzedajemy miesięczny pakiet wzrostu, prowadzony jako promowane kampanie, w których prawdziwi ludzie trafiają na Twój profil. Wyświetlenia to to, co ci ludzie robią, gdy podobają im się Twoje filmy. To uczciwa wersja: płacisz za to, żeby Cię zobaczono, a resztę decydują ludzie.",
                ],
            },
            {
                "h2": "Co pozostaje bezpieczne",
                "ul": [
                    "Twoje logowanie: nigdy nie wychodzi z Twoich rąk, bo wystarcza nazwa użytkownika.",
                    "Twoja płatność: bezpieczna kasa Stripe, z kartą, Apple Pay lub Google Pay.",
                    "Twoje wyjście: rezygnujesz na koncie, kiedy chcesz, a reszta opłaconego miesiąca zostaje Twoja.",
                    "Twoje dane: wyświetlenia i czas oglądania od ludzi, więc to, czego się z nich uczysz, jest prawdą.",
                ],
            },
        ],
        "faqs": [
            ("Czy kupno wyświetleń może narazić moje filmy?", "Sprowadzamy ludzi, którzy oglądają sami, i nigdy nie działamy wewnątrz Twojego konta ani nie wysyłamy odtworzeń ze skryptu. TikTok podejmuje własne decyzje, ale prawdziwi widzowie oglądający publiczne filmy to dokładnie to, do czego służy aplikacja."),
            ("Czy potrzebujecie dostępu do mojego TikToka, żeby wysłać wyświetlenia?", "Nie. Wyświetlenia przychodzą od ludzi, którzy otwierają Twój profil i klikają play, a to nie wymaga od Ciebie niczego poza publicznym kontem i nazwą użytkownika."),
            ("Dlaczego tanie paczki wyświetleń są ryzykowne?", "Są tanie, bo nikt nie ogląda. Takie odtworzenia mogą zostać usunięte, obniżają średni czas oglądania i sprawiają, że statystyki stają się bezużyteczne przy decydowaniu, co publikować dalej."),
            ("Skąd mam wiedzieć, że wyświetlenia są prawdziwe?", "Patrz, co przychodzi razem z nimi. Prawdziwe wyświetlenia przynoszą wizyty na profilu, polubienia, obserwowania i od czasu do czasu komentarz, a statystyki pokazują widzów zostających różnie długo, a nie wszystkich odchodzących w tej samej sekundzie."),
            ("Czy mogę przestać, jeśli nie czuję się z tym dobrze?", "Tak, kiedy chcesz, na swoim koncie. Kolejna płatność nie zostanie pobrana, a bieżący miesiąc trwa do ostatniego dnia."),
        ],
    },
    {
        "service": "views",
        "modifier": "fyp",
        "slug": "tiktok/wyswietlenia/dla-ciebie",
        "label": "Wyświetlenia na TikToku a strona Dla Ciebie",
        "title": "Wyświetlenia a strona Dla Ciebie na TikToku | Growsterr",
        "description": "Czy wyświetlenia na TikToku wprowadzą Cię na stronę Dla Ciebie? Nikt nie sprzeda ani nie obieca tam miejsca. Film niesie to, co robią z nim prawdziwi widzowie.",
        "h1": ("Wyświetlenia na TikToku a strona Dla Ciebie: ", "co naprawdę niesie film."),
        "intro": "Chęć kupienia wyświetleń na TikToku pod FYP zwykle oznacza jedno: chcesz, żeby film trafił na stronę Dla Ciebie. Nikt nie sprzeda Ci tego miejsca, my też nie. Możemy dzień po dniu sprowadzać prawdziwych ludzi na Twój profil, a to, co robią z Twoimi filmami, oglądanie, udostępnianie i obserwowanie, to rodzaj sygnału, z którego według TikToka korzysta.",
        "hero": {"image": "tiktok-watch-time", "alt": "Widzowie oglądają film na TikToku do końca i go udostępniają"},
        "sections": [
            {
                "h2": "Dlaczego nikt nie sprzeda Ci strony Dla Ciebie",
                "p": [
                    "Strona Dla Ciebie to nie miejsce, w które wkłada się film. Jest inna dla każdej osoby, zbudowana z tego, co dany widz oglądał, lajkował, udostępniał i pomijał. TikTok wybiera dla niego, film po filmie, i nie ma tam miejsca do kupienia.",
                    "Gdy więc serwis sprzedaje wyświetlenia „na FYP”, sprzedaje odtworzenia, zwykle od botów. Odtworzenia, których nikt nie ogląda, nie przekonają TikToka, że ktoś chce zobaczyć więcej.",
                ],
            },
            {
                "h2": "Na co według TikToka patrzy algorytm",
                "p": [
                    "TikTok opisał, co zasila jego rekomendacje, i nic z tego nie jest liczbą, którą da się kupić:",
                ],
                "ul": [
                    "Interakcje ludzi: co oglądają, lajkują, udostępniają, komentują i obserwują.",
                    "Szczegóły samego filmu: opisy, dźwięki i hashtagi.",
                    "Ustawienia, takie jak język i lokalizacja.",
                ],
            },
            {
                "h2": "Viral na TikToku, uczciwie",
                "p": [
                    "Nikt nie obieca viralowego filmu. Udostępnienia i zapisania zdarzają się, gdy widz chce, żeby znajomy coś zobaczył, albo chce obejrzeć to jeszcze raz, a tego nikt nie zamówi u prawdziwych ludzi. Stały wzrost daje Ci więcej szans: więcej prawdziwych ludzi widzi każdy film i więcej może go udostępnić we właściwym momencie. Film wciąż musi na to zasłużyć. Mocny haczyk, pasujący dźwięk i zakończenie warte powtórki zrobią więcej niż jakakolwiek kupiona liczba.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Twórca testuje różne dźwięki do filmu na TikToku przed publikacją"},
            },
        ],
        "faqs": [
            ("Czy Wasz pakiet wprowadzi mój film na stronę Dla Ciebie?", "Nie możemy tego obiecać i nikt uczciwie nie może. Sprowadzamy prawdziwych widzów na Twój profil; jeśli oglądają, udostępniają i obserwują, TikTok ma powody, żeby pokazać Twój film kolejnym podobnym ludziom."),
            ("Czy wyświetlenia pomagają filmowi trafić na FYP?", "Same wyświetlenia nie. Odtworzenie, które kończy się po sekundzie, mówi TikTokowi, że film nie utrzymał uwagi. Oglądanie do końca, powtórki, udostępnienia i zapisania znaczą o wiele więcej, a robią to tylko ludzie."),
            ("Czy mogę kupić udostępnienia albo zapisania?", "Nie. Udostępnienia i zapisania dają prawdziwi widzowie, którym film spodobał się na tyle, żeby komuś go wysłać albo go zachować. Przychodzą z pakietem, gdy Twoje filmy na nie zasłużą, a my nigdy nie liczymy ich ani nie sprzedajemy osobno."),
            ("Jak zrobić viral na TikToku?", "Nie ma przełącznika. Publikuj często, łap widzów w pierwszych sekundach, używaj dźwięków pasujących do filmu i rób rzeczy, które ludzie chcą wysłać znajomym. Prawdziwi widzowie dają każdemu filmowi więcej szans; reszta to film i trochę szczęścia."),
            ("Czy hashtag #fyp pomaga?", "TikTok czyta hashtagi, ale #fyp nic nie mówi o tym, o czym jest Twój film. Hashtag opisujący temat pomaga właściwym ludziom go znaleźć."),
            ("Który pakiet zrobi najwięcej dla jednego filmu?", "Z pakietem {rising_name} lub {pro_name} możesz wyróżnić filmy, które się liczą, więc ten, w który wierzysz, trafi do większej liczby naszych odwiedzających. Jak daleko pójdzie potem, zależy od oglądających."),
        ],
    },
    {
        "service": "views",
        "modifier": "high-retention",
        "slug": "tiktok/wyswietlenia/wysoka-retencja",
        "label": "Wyświetlenia na TikToku z wysoką retencją",
        "title": "Wyświetlenia na TikToku z wysoką retencją, uczciwie | Growsterr",
        "description": "Kupić wyświetlenia na TikToku z wysoką retencją? Retencję dają ludzie, którzy oglądają dalej. My sprowadzamy widzów; haczyk, dźwięk i tempo filmu ich trzymają.",
        "h1": ("Wyświetlenia na TikToku z wysoką retencją? ", "Widzów dajemy my, zatrzymać ich musi film."),
        "intro": "Skoro chcesz kupić wyświetlenia na TikToku z wysoką retencją, znasz już sekret: na TikToku liczy się, jak długo ludzie oglądają, a nie tylko ilu zaczyna. Retencji nie da się jednak sprzedać. To człowiek, który decyduje się oglądać dalej. Naszym zadaniem jest sprowadzenie prawdziwych ludzi na Twój profil; utrzymanie ich do końca to zadanie Twojego filmu.",
        "hero": {"image": "tiktok-watch-time", "alt": "Widz wciąż ogląda film na TikToku, gdy dochodzi on do ostatnich sekund"},
        "sections": [
            {
                "h2": "Czym zwykle są wyświetlenia z wysoką retencją",
                "p": [
                    "Gdy ktoś sprzedaje wyświetlenia z wysoką retencją, ma na myśli odtworzenia zaprogramowane tak, by trwały ustaloną liczbę sekund, zanim przejdą dalej. Czas oglądania jest prawdziwy tylko w tym sensie, że ekran go odtworzył. Nikt go nie widział, nikt się nie zaśmiał, nikt nie udostępnił, a reszta Twoich liczb to pokazuje.",
                ],
            },
            {
                "h2": "Retencja, którą naprawdę możesz podnieść",
                "ul": [
                    "Przejdź do rzeczy w pierwszej sekundzie lub dwóch, gdy większość widzów decyduje.",
                    "Dopasuj długość do pomysłu: szybki żart nie powinien trwać minuty.",
                    "Wybierz dźwięk, który pasuje do nastroju, i nie pozwól mu zagłuszyć Twojego głosu.",
                    "Dodaj napisy dla osób oglądających bez dźwięku.",
                    "Zakończ tak, żeby powtórka wydawała się naturalna.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Twórca przycina pierwsze sekundy filmu na TikToku, żeby zatrzymać widzów"},
            },
            {
                "h2": "Czytaj własną retencję",
                "p": [
                    "Statystyki TikToka pokazują średni czas oglądania i to, ilu widzów obejrzało cały film. Sprawdzaj je po każdej publikacji. Gdy prawdziwi ludzie znajdują Twoje filmy dzięki naszej kampanii, te liczby są uczciwe i widzisz, które filmy trzymają obcych, a które nie.",
                ],
            },
        ],
        "faqs": [
            ("Czy możecie dostarczyć wyświetlenia z ustalonym czasem oglądania?", "Nie. Każde wyświetlenie pochodzi od prawdziwego człowieka, a ten ogląda tak długo, jak film go trzyma. Ustalony czas oglądania oznaczałby, że nikt naprawdę nie oglądał."),
            ("Czy prawdziwi widzowie obejrzą cały mój film?", "Jedni tak, inni nie, zależnie od filmu. Właśnie dlatego ich retencja jest coś warta: mówi Tobie i TikTokowi, co działa."),
            ("Czy dłuższe filmy mają gorszą retencję?", "Niekoniecznie. Długi film, który uzasadnia swoją długość, potrafi dobrze trzymać ludzi. Szkodzi długość, której pomysł nie udźwignie."),
            ("Czy retencja jest ważniejsza niż polubienia?", "Są ze sobą połączone. Ludzie, którzy oglądają do końca, najczęściej lajkują, komentują i udostępniają, więc prawdziwi widzowie dają Ci to wszystko naraz."),
            ("Który pakiet sprowadza najwięcej widzów pod moje filmy?", "{pro_name} sprowadza na Twój profil najwięcej ludzi, zwykle {pro_audience} nowych obserwujących miesięcznie, i dodaje priorytetowe miejsce oraz wybór filmów, które dostają uwagę."),
        ],
    },
    {
        "service": "views",
        "modifier": "live",
        "slug": "tiktok/wyswietlenia/live",
        "label": "Widzowie na LIVE na TikToku",
        "title": "Widzowie na LIVE na TikToku: pokoju się nie kupi | Growsterr",
        "description": "Szukasz widzów na LIVE na TikToku? Prawdziwych ludzi nie da się zarezerwować na transmisję. Budujemy obserwujących, którzy przychodzą na LIVE, nigdy boty.",
        "h1": ("Widzowie na LIVE na TikToku ", "to obserwujący, którym zależy."),
        "intro": "Widzowie na LIVE na TikToku to ludzie, którzy są w pokoju teraz, a prawdziwych nikt nie dostarczy według harmonogramu. Dlatego nie sprzedajemy wyświetleń ani widzów na LIVE. Rozwijamy publiczność, która może dołączyć: prawdziwych ludzi, którzy odkryli Twoje filmy i zaczęli obserwować, każdego dnia miesiąca. Gdy odpalasz LIVE, to oni mogą się pojawić.",
        "hero": {"image": "tiktok-creator", "alt": "Twórca prowadzi LIVE na TikToku, a prawdziwi widzowie dołączają i piszą na czacie"},
        "sections": [
            {
                "h2": "Dlaczego kupieni widzowie psują transmisję",
                "p": [
                    "Wysoka liczba widzów przy pustym czacie mówi każdemu, kto wpada, że coś jest nie tak. Kupieni widzowie siedzą w pokoju, nie odzywając się, nie wysyłając prezentów i nie udostępniając transmisji. Pompują jedną liczbę, którą wszyscy widzą, i głodzą te, które napędzają LIVE.",
                ],
            },
            {
                "h2": "Jak zamienić obserwujących w widzów LIVE",
                "ul": [
                    "Zaplanuj transmisję z wyprzedzeniem jako wydarzenie LIVE, żeby obserwujący mogli ustawić przypomnienie.",
                    "Wspomnij godzinę w filmach dzień wcześniej.",
                    "Nadawaj co tydzień o tej samej porze, żeby stało się to nawykiem Twoich obserwujących.",
                    "Odpal LIVE wkrótce po filmie, który dobrze poszedł, póki jego widzowie są Cię ciekawi.",
                ],
            },
            {
                "h2": "Co możemy, a czego nie możemy zrobić dla LIVE",
                "p": [
                    "Nie zapełnimy Twojej transmisji w piątek o ósmej wieczorem i nie obiecamy liczby widzów. Możemy dopilnować, żeby co miesiąc więcej prawdziwych ludzi znało Twoje filmy i Cię obserwowało, więc każdy LIVE zaczyna się z większą grupą, która może przyjść.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Obserwujący otwierają LIVE twórcy na TikToku na swoich telefonach"},
            },
        ],
        "faqs": [
            ("Czy mogę kupić prawdziwych widzów na LIVE na TikToku?", "Nikt nie może. Prawdziwi ludzie dołączają do transmisji, bo ją zobaczyli i w tej chwili mieli ochotę. Widzowie dostarczani na żądanie to konta, które nie oglądają, a przez nie LIVE wydaje się bardziej pusty, a nie pełniejszy."),
            ("Jak Wasze pakiety pomagają moim wyświetleniom na LIVE?", "Rozwijają Twoich obserwujących z prawdziwymi ludźmi. Obserwujący to Twoja przyszła publiczność LIVE: jedni dołączą, gdy nadajesz, inni nie, jak przy każdej publiczności."),
            ("Czy liczycie wyświetlenia LIVE w panelu?", "Nie. Panel pokazuje, co zmierzyła nasza kampania, czyli wizyty na profilu i obserwowania, do których doprowadziły, z każdego dnia. Statystyki LIVE w TikToku pokazują, kto dołączał do Twoich transmisji."),
            ("Czy mogę odpalić LIVE bez 1000 obserwujących?", "Zwykle nie: TikTok najpierw wymaga 1000 obserwujących, a aplikacja mówi, czy LIVE jest dla Ciebie dostępny. Dojście do progu z prawdziwymi obserwującymi oznacza, że na pierwszą transmisję mogą przyjść ludzie."),
            ("Czy kupieni widzowie sprawią, że moja transmisja będzie polecana?", "Nie ma powodu się tego spodziewać. Pokój pełen kont, które nigdy nie piszą, nie wysyłają prezentów i nie zostają, nie daje TikTokowi nic wartego polecania."),
        ],
    },
    {
        "service": "views",
        "modifier": "promote",
        "slug": "tiktok/wyswietlenia/promowanie",
        "label": "Promowanie filmów na TikToku",
        "title": "Wyświetlenia z Promuj na TikToku czy kampania? | Growsterr",
        "description": "Myślisz o funkcji Promuj na TikToku dla wyświetleń lub obserwujących? Prowadzimy promowane kampanie Twojego profilu przez cały miesiąc, z zespołem.",
        "h1": ("Wyświetlenia z Promuj na TikToku ", "czy kampania wzrostu prowadzona za Ciebie."),
        "intro": "Jeśli zastanawiasz się, czy kupić wyświetlenia przez Promuj na TikToku, czy spróbować czegoś innego, oto gdzie jesteśmy my. Nie prowadzimy za Ciebie reklam na TikToku. Prowadzimy własne promowane kampanie w naszej sieci partnerskiej, codziennie pokazując Twój profil prawdziwym ludziom przez cały miesiąc, w wybranym przez Ciebie miejscu. Ci, którym spodoba się to, co zobaczą, oglądają, obserwują i wracają.",
        "hero": {"image": "tiktok-creator", "alt": "Twórca planuje, jak wypromować film na TikToku wśród większej liczby prawdziwych ludzi"},
        "sections": [
            {
                "h2": "Dwa sposoby na promowanie filmu na TikToku",
                "p": [
                    "Własne narzędzie TikToka, Promuj, pozwala zapłacić TikTokowi za pokazanie filmu większej liczbie osób, dopóki starczy budżetu: wybierasz film, cel i kwotę, a zarządzasz tym sam.",
                    "Pakiet Growsterr promuje Twój profil, a nie pojedynczy post, przez cały miesiąc, a kampanię prowadzi zespół. Ludzie trafiają na Twój profil, oglądają to, co przyciągnie ich wzrok, i decydują, czy obserwować.",
                ],
            },
            {
                "h2": "Co przynosi miesiąc promocji",
                "ul": [
                    "Nowi obserwujący: zwykle {pick_audience} z pakietem {pick_name}.",
                    "Polubienia i komentarze od tych samych obserwujących: zwykle {pick_likes} i {pick_comments}.",
                    "Wyświetlenia na całym profilu, których nie liczymy z góry.",
                    "Panel z wizytami na profilu i nowymi obserwującymi, dzień po dniu.",
                ],
            },
            {
                "h2": "Czy można korzystać z obu?",
                "p": [
                    "Można. Narzędzia TikToka pasują do jednorazowego pchnięcia jednego filmu; miesięczny pakiet sprawia, że ludzie trafiają na Twój profil także między takimi pchnięciami. Jedno nie przeszkadza drugiemu.",
                ],
            },
        ],
        "faqs": [
            ("Czy korzystacie z Promuj albo reklam na TikToku?", "Nie. Nasze kampanie działają w naszej sieci partnerskiej, poza narzędziami reklamowymi TikToka. Nigdy nie potrzebujemy dostępu do Twojego konta ani budżetu reklamowego, tylko nazwy użytkownika."),
            ("Czym różni się cena od samodzielnych reklam?", "Pakiet to stała miesięczna cena: {starter_price} za {starter_name}, {rising_price} za {rising_name}, {pro_price} za {pro_name}. Przy reklamach sam ustalasz i pilnujesz budżetu. Nie powiemy Ci, co wyjdzie taniej dla Twojego konta, ale powiemy dokładnie, ile kosztuje każdy pakiet."),
            ("Czy mogę promować konkretny film na TikToku?", "Z pakietem {rising_name} i {pro_name} tak: wybierasz filmy, które dostają uwagę. {starter_name} promuje Twój profil jako całość."),
            ("Czy promowanie przyniesie mi też obserwujących na TikToku?", "Tak, w dużej mierze o to chodzi. Ludzie, którym podoba się to, co oglądają, zaczynają obserwować, zwykle {pick_audience} miesięcznie z pakietem {pick_name}, a ich polubienia i komentarze przychodzą razem z nimi."),
            ("Czy potrzebuję konta firmowego?", "Nie. Działają konta osobiste i firmowe, o ile konto jest publiczne, a prosimy tylko o nazwę użytkownika."),
        ],
    },
]
