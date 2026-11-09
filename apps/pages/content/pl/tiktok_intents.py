"""Polish TikTok intent pages (mirrors en/tiktok_intents.py): what people ask for that we don't
sell (tanio, natychmiast, za darmo, okres próbny, panele, obserwujące kobiety, komentarze z AI
albo z własną treścią). Each answers honestly and shows what works instead. Keys and
placeholders: docs/CONTENT.md; angles: docs/keywords/WRITING.md; word forms: pl/ui.py."""

UPDATED = "2026-11-09"

PAGES = [
    # --- Followers ------------------------------------------------------------------------
    {
        "service": "followers",
        "modifier": "cheap",
        "plan": "starter",
        "slug": "tiktok/obserwujacy/tanio",
        "label": "Tani obserwujący na TikToku: ile kosztują",
        "title": "Tani obserwujący na TikToku: prawdziwa cena | Growsterr",
        "description": "Chcesz tanio kupić obserwujących na TikToku? Ile kosztuje prawdziwy obserwujący, co dają oferty za grosze i dlaczego najniższa cena to nie najniższy koszt.",
        "h1": ("Tani obserwujący na TikToku? ", "Oto ile kosztuje każdy prawdziwy."),
        "intro": "Jeśli chcesz tanio kupić obserwujących na TikToku, porównaj właściwą liczbę. {starter_name} kosztuje {starter_price} miesięcznie i zwykle daje {starter_audience} nowych obserwujących, a każdy z nich to prawdziwy człowiek, który obejrzał Twoje filmy i sam zdecydował się obserwować. Wychodzi kilka centów za obserwującego, bez spadków, martwego zaangażowania i prośby o logowanie, które idą w parze z okazyjnymi paczkami.",
        "hero": {"image": "tiktok-creator", "alt": "Twórca liczy miesięczny koszt rozwijania konta na TikToku z prawdziwymi obserwującymi"},
        "sections": [
            {
                "h2": "Ile kosztuje kupno obserwujących na TikToku?",
                "p": [
                    "Ceny obserwujących na TikToku bardzo się różnią, a ta rozpiętość mówi, co jest sprzedawane. Na samym dole płacisz za konta: profile tworzone hurtem i kierowane na Twoją nazwę użytkownika. Wyżej płacisz za uwagę, bo ktoś musi pokazać Twój profil ludziom, a ludzie potrzebują czasu, żeby zdecydować.",
                    "Nasza cena jest tego drugiego rodzaju. Miesięczna opłata pokrywa promowane kampanie, które codziennie pokazują Twój profil prawdziwym użytkownikom TikToka, zespół, który je prowadzi, i panel, który je mierzy. Podziel ją przez liczbę obserwujących, których zwykle przynosi, a każdy prawdziwy człowiek kosztuje bardzo mało.",
                ],
            },
            {
                "h2": "Co naprawdę kupują obserwujący za dolara",
                "ul": [
                    "Konta bez filmów, bez własnych obserwujących i bez nikogo za nimi.",
                    "Liczbę, którą TikTok może odebrać: regularnie usuwa fałszywe konta i fałszywe obserwowania.",
                    "Obserwujących, którzy nigdy nie oglądają, więc każdy nowy film startuje z publicznością, która go ignoruje.",
                    "Czasem prośbę o Twoje logowanie, której żadna niska cena nie usprawiedliwi.",
                ],
            },
            {
                "h2": "Najtańsza prawdziwa opcja, jaką mamy",
                "p": [
                    "{starter_name} to nasz najmniejszy pakiet i od niego zaczyna większość kont. Poza zwykle {starter_audience} nowymi obserwującymi ci sami ludzie zostawiają w ciągu miesiąca zwykle {starter_likes} polubień i {starter_comments} komentarzy. Przejdź wyżej, gdy Twoje filmy będą gotowe na więcej widzów, albo zrezygnuj, kiedy chcesz.",
                ],
                "image": {"image": "tiktok-likes", "alt": "Nowi obserwujący na małym koncie na TikToku lajkują jego najnowsze filmy"},
            },
        ],
        "faqs": [
            ("Jaki jest najtańszy sposób na prawdziwych obserwujących na TikToku?", "Częste i dobre publikowanie kosztuje tylko czas i wciąż jest podstawą wszystkiego. Jeśli chcesz do tego zasięgu, {starter_name} za {starter_price} miesięcznie to nasza najniższa cena za prawdziwych ludzi, codziennie, z wybranego przez Ciebie miejsca."),
            ("Dlaczego bardzo tani obserwujący na TikToku są tacy tani?", "Bo nikt za nimi nie stoi. Konta tworzone hurtem prawie nic nie kosztują, więc można je sprzedawać prawie za nic. Uwagi prawdziwego człowieka nie da się tak wyprodukować."),
            ("Ile kosztuje obserwujący na TikToku w Growsterr?", "Weź {starter_price} i podziel przez {starter_audience} nowych obserwujących, których {starter_name} zwykle daje w miesiąc: wychodzi kilka centów za osobę. Ludzie decydują sami, więc dokładna liczba zmienia się z miesiąca na miesiąc."),
            ("Czy jest zniżka za płatność za kilka miesięcy z góry?", "Nie. Pakiety są rozliczane co miesiąc w jednej cenie, bez długiej umowy. Płacisz miesiąc po miesiącu i przestajesz, kiedy chcesz."),
            ("Czy niska cena jest warta ryzyka dla konta?", "Obserwujący, którzy nigdy nie oglądają, obniżają wyniki Twoich filmów u publiczności, którą masz. Nie przewidzimy, jak TikTok potraktuje konkretne konto, ale nigdy nie dodalibyśmy takich kont do Twojego."),
        ],
    },
    {
        "service": "followers",
        "modifier": "fast",
        "slug": "tiktok/obserwujacy/szybko",
        "label": "Szybcy obserwujący na TikToku, uczciwie",
        "title": "Szybcy obserwujący na TikToku, bez botów | Growsterr",
        "description": "Chcesz szybko kupić obserwujących na TikToku? Kampania rusza w ciągu kilku dni, a prawdziwi ludzie obserwują codziennie. Tylko „natychmiast” odpada: to boty.",
        "h1": ("Szybcy obserwujący na TikToku: ", "szybki start, a potem codziennie."),
        "intro": "Żeby szybko zdobyć obserwujących na TikToku i ich zatrzymać, potrzebujesz szybkiego startu, a nie licznika „natychmiast”. Uruchamiamy kampanię wkrótce po zamówieniu, prawdziwi ludzie zaczynają odkrywać Twój profil w pierwszych dniach, a nowi obserwujący przychodzą każdego dnia miesiąca. Nigdy nie oferujemy dostawy „natychmiast”, bo obserwujący „natychmiast” to konto, którym nikt nie zarządza.",
        "hero": {"image": "tiktok-hub", "alt": "Liczba obserwujących na TikToku rośnie dzień po dniu od pierwszego tygodnia kampanii"},
        "sections": [
            {
                "h2": "Prawdziwi, „natychmiast” i aktywni: to się nie łączy",
                "p": [
                    "Wiele ofert obiecuje obserwujących na TikToku, którzy są jednocześnie prawdziwi, „natychmiast” i aktywni. Prawdziwy człowiek musi trafić na Twój profil, obejrzeć film czy dwa i wyrobić sobie zdanie. Jednej osobie zajmuje to minuty, a całej publiczności dni. Wszystko, co ląduje szybciej, niż ludzie mogą zdecydować, nigdy nie decydowało.",
                ],
            },
            {
                "h2": "Szybko, po naszemu",
                "ul": [
                    "Zamówienie zajmuje kilka minut: wybierz pakiet, podaj nazwę użytkownika, wskaż miasto lub kraj.",
                    "Uruchomienie jest szybkie, a pierwsi odwiedzający zwykle trafiają na Twój profil w ciągu kilku dni.",
                    "Panel pokazuje pierwsze liczby po kilku dniach, a potem nowy wiersz każdego dnia.",
                    "Obserwujący przychodzą przez cały miesiąc, a nie jednym wysypem pierwszego dnia.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Twórca sprawdza na telefonie pierwsze dni nowych obserwujących na TikToku"},
            },
            {
                "h2": "Dlaczego dostawa „natychmiast” obraca się przeciwko Tobie na TikToku",
                "p": [
                    "Tysiąc obserwujących w godzinę nie obejrzy Twojego kolejnego filmu. TikTok ocenia film częściowo po tym, jak reagują ludzie, którzy go widzą, a publiczność, która nigdy nie reaguje, daje każdemu postowi słabszy start. Szybki wzrost od ludzi, którzy naprawdę oglądają, to jedyny rodzaj, który pomaga filmom publikowanym później.",
                ],
            },
        ],
        "faqs": [
            ("Kiedy pojawia się pierwsze obserwowanie?", "Większość kont widzi pierwsze po kilku dniach. Ludzie muszą zobaczyć Twój profil i polubić to, co znajdą, więc pierwsze obserwowania przychodzą wkrótce po pierwszych wizytach."),
            ("Czy możecie dostarczyć obserwujących na TikToku natychmiast?", "Nie. Obserwujący „natychmiast” to konta wypuszczane według harmonogramu, a nie ludzie, którzy wybierają. Wolimy ruszyć szybko i pozwolić, żeby każde obserwowanie było prawdziwe."),
            ("Który pakiet rośnie najszybciej?", "{pro_name} dociera do największej liczby ludzi każdego dnia, zwykle {pro_audience} nowych obserwujących miesięcznie, z priorytetowym miejscem. {rising_name} zwykle daje {rising_audience}. Wszystkie trzy startują równie szybko; różnią się tym, ilu ludzi Cię zobaczy."),
            ("Potrzebuję obserwujących przed premierą w przyszłym tygodniu. Pomożecie?", "Możemy od razu uruchomić kampanię, a ludzie zaczną przychodzić w ciągu kilku dni. Nie obiecamy liczby na konkretny dzień, bo ludzie decydują sami. Start kilka tygodni przed premierą daje lepszą bazę."),
            ("Czy szybko zdobyci obserwujący potem odpadają?", "Nie, gdy są ludźmi. Nagłe straty po zamówieniu „natychmiast” zdarzają się, bo TikTok usuwa konta; człowiek odchodzi tylko wtedy, gdy sam przestanie obserwować, pojedynczo."),
        ],
    },
    {
        "service": "followers",
        "modifier": "free",
        "plan": "starter",
        "tool": "growth-calculator",
        "slug": "tiktok/obserwujacy/za-darmo",
        "label": "Darmowi obserwujący na TikToku: prawda",
        "title": "Darmowi obserwujący na TikToku: co dostajesz | Growsterr",
        "description": "Szukasz darmowych obserwujących na TikToku? Nie dajemy ich, a oto ile naprawdę kosztują darmowe aplikacje. Do tego darmowy kalkulator czasu prawdziwego wzrostu.",
        "h1": ("Darmowi obserwujący na TikToku? ", "Oto ile naprawdę kosztuje „za darmo”."),
        "intro": "Szukasz obserwujących na TikToku za darmo? Nie rozdajemy ich i uważalibyśmy na każdego, kto to robi. Darmowi obserwujący skądś się biorą: z kont botów, wymian follow za follow albo z aplikacji, która chce Twojego logowania. Za darmo możemy dać kalkulator na tej stronie, który pokazuje, ile potrwa dojście do Twojego celu z prawdziwymi ludźmi, i miesięczny pakiet, z którego zrezygnujesz w każdej chwili.",
        "hero": {"image": "tiktok-likes", "alt": "Telefon z profilem na TikToku obok aplikacji oferującej darmowych obserwujących"},
        "sections": [
            {
                "h2": "Skąd biorą się darmowi obserwujący na TikToku",
                "ul": [
                    "Z generatorów obiecujących 1000 obserwujących na TikToku za darmo, które przeprowadzają Cię przez ankiety albo instalacje aplikacji, zanim cokolwiek się pojawi.",
                    "Z aplikacji z monetami, w których obserwujesz obcych, żeby zarabiać monety i wydawać je na obserwowania w zamian, więc Twój feed zapełnia się kontami, które Cię nie obchodzą.",
                    "Z narzędzi, które każą logować się kontem TikToka, czyli oddać komuś kontrolę nad nim.",
                    "Z kont botów rozdawanych jako próbka, żeby sprzedać Ci więcej tego samego.",
                ],
            },
            {
                "h2": "Darmowi obserwujący na TikToku bez logowania: wciąż nie za darmo",
                "p": [
                    "Oferty darmowych obserwujących bez logowania brzmią bezpieczniej i dla Twojego hasła takie są. Ale ktoś i tak płaci za tych obserwujących, a jeśli nie Ty, to dlatego, że ich zrobienie nic nie kosztuje. Konta, których zrobienie nic nie kosztuje, nie oglądają filmów.",
                ],
            },
            {
                "h2": "Jak zdobyć obserwujących, nikomu nie płacąc",
                "p": [
                    "Prawdziwy wzrost na TikToku bez wydawania pieniędzy istnieje, tylko jest powolny. Publikuj często, łap widzów w pierwszej sekundzie, odpowiadaj na komentarze filmami i dołączaj do trendów, póki rosną. Kalkulator na tej stronie pokazuje, o ile pakiet skróciłby tę drogę, od miejsca, w którym jesteś dziś, do celu, który sobie wyznaczysz.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Twórca nagrywa w domu krótki film, żeby rozwijać publiczność na TikToku"},
            },
        ],
        "faqs": [
            ("Czy Growsterr rozdaje darmowych obserwujących na TikToku?", "Nie. Nie oferujemy darmowych obserwujących, próbek ani okresu próbnego. Każdy obserwujący od nas to człowiek, do którego dotarła nasza kampania, a docieranie do ludzi kosztuje. Pakiet możesz anulować w każdej chwili, a opłacony miesiąc trwa do końca."),
            ("Czy da się kupić 1000 obserwujących na TikToku za kilka złotych?", "Nie prawdziwych. Kilka złotych za tysiąc to ułamek grosza za obserwującego, o wiele za mało, żeby pokazać profil tylu ludziom, by tysiąc z nich go wybrał. Za taką cenę sprzedaje się konta. Prawdziwi kosztują {starter_price} miesięcznie w pakiecie {starter_name}, który zwykle daje {starter_audience}."),
            ("Czy aplikacje z darmowymi obserwującymi są bezpieczne?", "Wszystko, co może logować się jako Ty, może też publikować, obserwować i pisać wiadomości jako Ty, a wiele takich aplikacji prosi właśnie o to. Reszta jest nieszkodliwa, ale bezużyteczna: obserwujący znikają albo nigdy nie oglądają. Żadna z opcji nie jest warta ryzyka."),
            ("Jak zdobyć obserwujących na TikToku bez płacenia?", "Wygrywa regularność: publikuj kilka razy w tygodniu, zaczynaj od najciekawszej sekundy, używaj dźwięków i tematów, które ludzie oglądają teraz, i rozmawiaj z komentującymi. To wolniejsze niż kampania, ale to ten sam rodzaj wzrostu."),
            ("Co robi kalkulator na tej stronie?", "Wpisujesz dzisiejszą liczbę obserwujących i swój cel, a on pokazuje mniej więcej, ilu miesięcy potrzebuje każdy pakiet, żeby tam dojść, na podstawie ich typowych miesięcznych zakresów. Obliczenia dzieją się na Twoim urządzeniu i nigdy ich nie widzimy."),
        ],
    },
    {
        "service": "followers",
        "modifier": "free-trial",
        "plan": "starter",
        "slug": "tiktok/obserwujacy/darmowy-test",
        "label": "Darmowy test obserwujących na TikToku",
        "title": "Darmowy test obserwujących na TikToku? Dlaczego nie | Growsterr",
        "description": "Liczysz na darmowy test, zanim kupisz obserwujących na TikToku? Nie oferujemy go. Wyjaśniamy dlaczego i jak pierwszy płatny miesiąc działa jak uczciwy test.",
        "h1": ("Darmowy test obserwujących na TikToku? ", "Nie, ale miesiąc powie Ci sporo."),
        "intro": "Jeśli chcesz kupić obserwujących na TikToku po darmowym teście, oto nasza prosta odpowiedź: nie robimy testów. Każda kampania pokazuje Twój profil prawdziwym ludziom, a to kosztuje nas od pierwszego dnia. Zamiast tego oferujemy miesięczny pakiet bez umowy: spróbuj miesiąca w pakiecie {starter_name} za {starter_price}, śledź panel i zrezygnuj w każdej chwili, jeśli to nie dla Ciebie.",
        "hero": {"image": "tiktok-watch-time", "alt": "Twórca przegląda pierwszy miesiąc kampanii wzrostu na TikToku"},
        "sections": [
            {
                "h2": "Dlaczego darmowe testy obserwujących to sygnał ostrzegawczy",
                "p": [
                    "Test 50 czy 100 obserwujących prawie nic nie kosztuje sprzedawcy, gdy obserwujący to konta, i właśnie dlatego takie testy istnieją. To próbka produktu: jeśli za darmo dostajesz boty, po zapłacie też dostaniesz boty.",
                    "Prawdziwego zasięgu nie da się rozdać jako próbki. Żeby sprowadzić na Twój profil choćby garstkę prawdziwych ludzi, ktoś płaci za pokazanie go wielu innym, bo tylko część z nich zacznie obserwować.",
                ],
            },
            {
                "h2": "Co sprawdzić w pierwszym miesiącu",
                "ul": [
                    "Panel: dzienne zestawienie odwiedzających z kampanii i części, która została, żeby obserwować.",
                    "Twoje filmy: czy nowsze zbierają więcej wyświetleń i komentarzy od ludzi, których nie znasz?",
                    "Skąd są odwiedzający: panel pokazuje wizyty według kraju, więc widzisz kierowanie w działaniu.",
                    "Liczbę obserwujących kilka tygodni później: prawdziwi ludzie nie znikają falami.",
                ],
            },
            {
                "h2": "Rezygnacja jest częścią umowy",
                "p": [
                    "Możesz zrezygnować na swoim koncie, kiedy chcesz, bez podawania powodu i bez dzwonienia do kogokolwiek. Opłacony miesiąc trwa do końca, więc widzisz cały test, a po nim nic nie jest pobierane.",
                ],
            },
        ],
        "faqs": [
            ("Czy jest darmowy okres próbny obserwujących na TikToku?", "Nie u nas: nie ma okresu próbnego ani darmowej próbki. Możesz zacząć od jednego miesiąca w pakiecie {starter_name} i przestać, kiedy zechcesz."),
            ("Czy muszę się zobowiązać na więcej niż miesiąc?", "Nie. Każdy pakiet odnawia się co miesiąc, dopóki nie zrezygnujesz, więc najdłużej jesteś zobowiązany na jeden miesiąc."),
            ("Kiedy będę wiedzieć, czy to działa?", "Pierwsze liczby zwykle pojawiają się w panelu w ciągu kilku dni. Pod koniec pierwszego miesiąca masz pełny obraz tego, co przyniosła kampania."),
            ("Dlaczego mam płacić, zanim zobaczę efekty?", "Bo kampania kosztuje od pierwszego dnia: płacimy za pokazanie Twojego profilu ludziom. W zamian dostajesz przejrzystość: zmierzone liczby każdego dnia, typowe zakresy z góry i przycisk rezygnacji, który zawsze należy do Ciebie."),
            ("Co zostaje, jeśli przestanę po jednym miesiącu?", "Każdy zdobyty obserwujący. Każdy z nich zaczął obserwować Twoje konto z wyboru, a ten wybór nie wygasa razem z subskrypcją. Rezygnacja oznacza tylko brak nowych dni kampanii po końcu opłaconego miesiąca."),
        ],
    },
    {
        "service": "followers",
        "modifier": "smm-panel",
        "slug": "tiktok/obserwujacy/panel-smm",
        "label": "Alternatywa dla panelu SMM do TikToka",
        "title": "Panel SMM do TikToka? Jak działa agencja | Growsterr",
        "description": "Szukasz panelu SMM do TikToka? Nie jesteśmy panelem. Panele odsprzedają obserwujących i polubienia hurtem; my prowadzimy kampanie do prawdziwych ludzi.",
        "h1": ("Szukasz panelu SMM do TikToka? ", "Jesteśmy agencją, nie panelem."),
        "intro": "Myślisz o kupnie obserwujących na TikToku z panelu SMM? Panel działa jak hurtownia: wybierasz usługę, wpisujesz ilość i link, a liczby przychodzą z puli kont, często odsprzedawanych z panelu do panelu. Growsterr działa odwrotnie. Prowadzimy miesięczną kampanię, która pokazuje Twój profil prawdziwym ludziom, opiekuje się nią zespół, a panel pokazuje, co zmierzyła.",
        "hero": {"image": "tiktok-hub", "alt": "Profil na TikToku rośnie dzięki kampanii, a nie hurtowemu formularzowi zamówień"},
        "sections": [
            {
                "h2": "Jak działa panel i dlaczego jest tani",
                "p": [
                    "Panele wystawiają obserwujących, polubienia i wyświetlenia na tysiące, każdą pozycję z ceną, tempem i czasem okresem uzupełnień. Za większością stoi ten sam towar: konta stworzone, żeby obserwować, lajkować i odtwarzać na polecenie. Tani panel SMM do TikToka jest tani, bo w całym tym łańcuchu nie ma człowieka, który by cokolwiek decydował.",
                ],
            },
            {
                "h2": "Polubienia i wyświetlenia na TikToku z panelu",
                "p": [
                    "Polubienia i wyświetlenia z panelu lądują pod filmem, którego link wkleisz, w zamówionej liczbie. To je zdradza: prawdziwi widzowie nie rozdają polubień w okrągłych liczbach, a film z dziesiątkami tysięcy odtworzeń i średnim czasem oglądania jednej sekundy mówi, co się stało, gdy tylko otworzysz jego statystyki.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Statystyki TikToka pokazują wyświetlenia obok średniego czasu oglądania filmu"},
            },
            {
                "h2": "Co daje Ci agencja zamiast tego",
                "ul": [
                    "Kampanię, a nie zamówienie: Twój profil jest pokazywany prawdziwym ludziom codziennie przez 30 dni.",
                    "Miejsce, a nie pulę: wybierasz miasto, region lub kraj, z którego pochodzą Twoi obserwujący.",
                    "Zespół, który prowadzi kampanię, i panel, który codziennie mierzy wizyty i nowych obserwujących.",
                    "Polubienia, wyświetlenia i komentarze od tych samych ludzi, którzy obserwują, nigdy na tysiące.",
                ],
            },
        ],
        "faqs": [
            ("Czy Growsterr to panel SMM?", "Nie. Nie sprzedajemy obserwujących, polubień ani wyświetleń na sztuki. Sprzedajemy miesięczne pakiety wzrostu, prowadzone jako promowane kampanie do prawdziwych ludzi, z zespołem za każdą z nich."),
            ("Czy kupowanie obserwujących na TikToku z panelu jest bezpieczne?", "Nie wypowiadamy się za żaden panel ani za to, jak TikTok traktuje konto. Wytyczne społeczności TikToka uznają sztucznie pompowanych obserwujących, polubienia i wyświetlenia za fałszywe zaangażowanie, a konta obserwujące na polecenie są dokładnie tym."),
            ("Dlaczego panel kosztuje o tyle mniej?", "Cena panelu musi pokryć tylko konta i oprogramowanie. Nasza pokrywa promowane kampanie, które docierają do prawdziwych ludzi, i zespół, który je prowadzi. Mimo to po podzieleniu przez {starter_audience} obserwujących, których {starter_name} zwykle daje, prawdziwy obserwujący kosztuje niewiele."),
            ("Czy oferujecie zamówienia hurtowe albo API jak panel?", "Nie. Nie ma ceny za tysiąc, hurtowego formularza zamówień ani API dla odsprzedawców. Każdy pakiet rozwija jedno konto, wybrane przez osobę, która go zamawia."),
            ("Czy uzupełniacie obserwujących tak jak panele?", "Nie ma czego uzupełniać. Uzupełnienia istnieją, bo obserwujący z paneli znikają, gdy TikTok usuwa konta. Ludzie, którzy Cię obserwują, zostają, chyba że sami zdecydują inaczej."),
        ],
    },
    {
        "service": "followers",
        "modifier": "female",
        "slug": "tiktok/obserwujacy/kobiety",
        "label": "Obserwujące kobiety na TikToku",
        "title": "Obserwujące kobiety na TikToku? Prawda | Growsterr",
        "description": "Chcesz kupić obserwujące kobiety na TikToku? Nie kierujemy według płci i nikt nie może z prawdziwymi ludźmi. Co decyduje o tym, kto Cię obserwuje.",
        "h1": ("Obserwujące kobiety na TikToku? ", "Twoje filmy wybierają publiczność."),
        "intro": "Jeśli chcesz kupić obserwujące kobiety na TikToku, uczciwa odpowiedź brzmi: nie możemy ich sprzedać i nie może nikt, kto pracuje z prawdziwymi ludźmi. Nie kierujemy według płci: nasze kampanie celują w miejsce, a obserwują ci, którym podobają się Twoje filmy. Serwisy obiecujące kobiece obserwujące sprzedają konta ze zdjęciami kobiet, a nie kobiety.",
        "hero": {"image": "tiktok-creator", "alt": "Twórczyni nagrywa film na TikToka dla publiczności, do której chce dotrzeć"},
        "sections": [
            {
                "h2": "Dlaczego nie oferujemy kierowania według płci",
                "p": [
                    "Żeby dostarczać wyłącznie kobiety, serwis musiałby wiedzieć, kim jest każda osoba, i nie pokazywać Twojego profilu nikomu innemu. Prawdziwa publiczność tak nie działa. Pokazujemy Twój profil ludziom w wybranym przez Ciebie miejscu, a obserwować może każdy, komu podobają się Twoje filmy. Paczka z etykietą „kobiety” to paczka profili przebranych tak, żeby tak wyglądały.",
                ],
            },
            {
                "h2": "Co naprawdę kształtuje to, kto Cię obserwuje",
                "ul": [
                    "Tematy, które poruszasz, i twórcy, których ludzie już dla nich oglądają.",
                    "Dźwięki, trendy i formaty, których używasz, i społeczności wokół nich.",
                    "Twój język i miejsce, w którym mieszka Twoja publiczność, a na nie możemy kierować.",
                    "To, do kogo mówisz w opisach i odpowiedziach: ludzie obserwują, gdy film wydaje się zrobiony dla nich.",
                ],
            },
            {
                "h2": "Sprawdź swoją publiczność w statystykach TikToka",
                "p": [
                    "Statystyki TikToka pokazują podział Twoich obserwujących według płci, wiek i najważniejsze lokalizacje. Zajrzyj tam przed i po miesiącu wzrostu. Jeśli chcesz więcej kobiet w swojej publiczności, zmiana przyjdzie z filmów, które robisz, a statystyki powiedzą Ci, czy się dzieje.",
                ],
                "image": {"image": "tiktok-likes", "alt": "Publiczność twórcy na TikToku reaguje polubieniami na nowy film"},
            },
        ],
        "faqs": [
            ("Czy mogę wybrać wyłącznie obserwujące kobiety?", "Nie. Kierujemy według miejsca, nigdy według płci, a ludzie obserwują z własnego wyboru. Każdy, kto oferuje obserwujących wyłącznie kobiet, oferuje fałszywe profile."),
            ("Dlaczego niektóre serwisy sprzedają obserwujące kobiety?", "Bo zdjęcie profilowe łatwo dobrać, gdy konto tworzy skrypt. Zdjęcie to jedyna kobieca rzecz w takim koncie: nikt za nim nie stoi, żeby oglądać, lajkować czy cokolwiek kupić."),
            ("Moje produkty są dla kobiet. Jak do nich dotrzeć?", "Rób filmy, które mówią do ludzi, na których Ci zależy, i przy zamówieniu wskaż miejsce, w którym mieszkają. Twoje treści decydują, kto obserwuje; kampania dba o to, żeby ludzie w tym miejscu je zobaczyli."),
            ("Czy możecie zamiast tego kierować według wieku albo zainteresowań?", "Nie. Kampanie celujemy wyłącznie według lokalizacji, czy to miasto, region, czy cały kraj. W obrębie tego miejsca selekcję robią Twoje filmy."),
            ("Czy nowi obserwujący będą prawdziwymi ludźmi?", "Tak, każdy z nich. Właśnie dlatego nie możemy ich sortować: prawdziwi ludzie przychodzą tacy, jacy są, i obserwują, bo spodobało im się to, co zobaczyli."),
        ],
    },
    # --- Likes ----------------------------------------------------------------------------
    {
        "service": "likes",
        "modifier": "cheap",
        "plan": "starter",
        "slug": "tiktok/polubienia/tanio",
        "label": "Tanie polubienia na TikToku",
        "title": "Tanie polubienia na TikToku? Ile kosztuje prawdziwe | Growsterr",
        "description": "Tanie polubienia na TikToku? Nie wyceniamy polubień za tysiąc. Pakiety dają polubienia od prawdziwych widzów, około {starter_likes} w typowym miesiącu.",
        "h1": ("Tanie polubienia na TikToku? ", "Porównuj polubienia z widzami za nimi."),
        "intro": "Ludzie, którzy chcą tanio kupić polubienia na TikToku, zwykle porównują cenę za tysiąc. My tak nie wyceniamy polubień i nigdy nie sprzedajemy ich osobno. Pakiet sprowadza do Ciebie prawdziwych ludzi, a oni stukają w serce pod tym, co im się podoba: zwykle {starter_likes} polubień miesięcznie w pakiecie {starter_name} za {starter_price}, razem z nowymi obserwującymi i komentarzami, więc każde polubienie to mały ułamek ceny.",
        "hero": {"image": "tiktok-likes", "alt": "Serca od prawdziwych widzów zbierają się pod filmami twórcy na TikToku"},
        "sections": [
            {
                "h2": "Dlaczego polubienia za dolara kosztują więcej, niż się wydaje",
                "p": [
                    "Polubienia sprzedaje się po dolarze za tysiąc, gdy nikt wcześniej nie obejrzał filmu. Każdy może zestawić polubienia filmu z liczbą wyświetleń na Twoim profilu, a statystyki dodają czas oglądania, więc polubienia, które wyprzedzają całą resztę, sprawiają, że liczby filmu sobie przeczą. Cena była niska, a film wygląda teraz na kupiony.",
                ],
            },
            {
                "h2": "Co obejmuje cena pakietu",
                "ul": [
                    "Zasięg: 30 dni promowanych kampanii, które pokazują Twój profil prawdziwym użytkownikom TikToka.",
                    "Obserwujących: {starter_audience} nowych w typowym miesiącu w pakiecie {starter_name}.",
                    "Polubienia: {starter_likes} w typowym miesiącu, od tych samych ludzi, pod filmami, które sami wybiorą.",
                    "Komentarze: {starter_comments} w typowym miesiącu, ich własnymi słowami.",
                    "Panel z tym, co zmierzono, i zespół za kampanią.",
                ],
            },
            {
                "h2": "Jak dostać więcej polubień za swoje pieniądze",
                "p": [
                    "To, ile polubień przynosi pakiet, zależy częściowo od Twoich filmów: ludzie z kampanii lajkują to, co im się podoba. Publikuj dalej w trakcie, przypnij filmy, które pokazują Cię najlepiej, i daj widzom powód, żeby zostali dłużej niż pierwsze sekundy. Każdy dobry film daje temu samemu zasięgowi więcej do reagowania.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Twórca przypina ulubione filmy na górze profilu na TikToku"},
            },
        ],
        "faqs": [
            ("Ile kosztują u Was polubienia na TikToku?", "Polubienia nie mają własnej ceny. Są w każdym pakiecie: {starter_name} za {starter_price} miesięcznie zwykle daje {starter_likes}, razem z obserwującymi i komentarzami od tych samych ludzi."),
            ("Czy mogę kupić małą, tanią paczkę polubień pod jeden film?", "Nie. Nie sprzedajemy polubień pod filmy i nie możemy skierować polubień pod konkretny. Ludzie, którzy odwiedzają Twój profil, sami wybierają filmy, które polubią, często te na górze."),
            ("Dlaczego tanie polubienia na TikToku są ryzykowne?", "Pochodzą z kont, które lajkują na polecenie. TikTok usuwa fałszywe polubienia w regularnych czystkach, a jego zasady traktują kupione zaangażowanie jako fałszywe. Pieniądze i tak przepadają; czasem polubienia też."),
            ("Czy {starter_name} wystarczy, jeśli chodzi o polubienia?", "Dla większości nowych i małych kont tak: typowy miesiąc w nim to {starter_likes} polubień. Jeśli Twoje filmy już mają stałe wyświetlenia, {rising_name} dociera do większej liczby ludzi i zwykle daje {rising_likes}."),
            ("Czy płacę za każde polubienie?", "Nie. Płacisz jedną miesięczną cenę za pakiet, a polubienia to część tego, co robią prawdziwi ludzie, gdy już Cię znajdą. Ich liczba zmienia się z Twoimi filmami, w typowym zakresie."),
        ],
    },
    {
        "service": "likes",
        "modifier": "fast",
        "slug": "tiktok/polubienia/szybko",
        "label": "Szybkie polubienia na TikToku, uczciwie",
        "title": "Polubienia na TikToku „natychmiast”? Cena pośpiechu | Growsterr",
        "description": "Chcesz polubień na TikToku „natychmiast”? Takie przychodzą, zanim ktokolwiek obejrzy, czyli od botów. Nasze dają prawdziwi widzowie, codziennie.",
        "h1": ("Polubienia na TikToku „natychmiast”? ", "Prawdziwe polubienie czeka na film."),
        "intro": "Jeśli chcesz kupić polubienia na TikToku „natychmiast”, pomyśl, czym jest polubienie: stuknięciem po obejrzeniu czegoś, co Ci się spodobało. Polubienia „natychmiast” pomijają oglądanie, dlatego pochodzą z kont, a nie od widzów. Nasze przychodzą wolniej: prawdziwi ludzie codziennie odkrywają Twój profil, oglądają i lajkują to, co ich trzyma, zwykle {pick_likes} polubień miesięcznie z pakietem {pick_name}.",
        "hero": {"image": "tiktok-watch-time", "alt": "Widz ogląda film na TikToku do końca, zanim stuknie w serce"},
        "sections": [
            {
                "h2": "Polubienia, które przychodzą przed wyświetleniami",
                "p": [
                    "Gdy sto polubień trafia pod film w ciągu minuty, zwykle lądują, zanim dogonią je odtworzenia. Każdy może porównać polubienia filmu z liczbą wyświetleń, a statystyki dodają średni czas oglądania. Prawdziwe polubienia idą za wyświetleniami; te „natychmiast” wyprzedzają je, a tej kolejności trudno nie zauważyć.",
                ],
            },
            {
                "h2": "Jak szybko przychodzą prawdziwe polubienia",
                "ul": [
                    "Kampania rusza w ciągu kilku dni od zamówienia.",
                    "Od tego momentu ludzie odwiedzają Twój profil codziennie, a polubienia zaczynają się od ich pierwszych wizyt.",
                    "Każdy sam decyduje, które filmy obejrzeć i polubić; nie możemy skierować polubień pod jeden film ani zgrać ich z publikacją.",
                    "W skali miesiąca polubienia składają się na typowy zakres, nigdy na stałą dostawę.",
                ],
            },
            {
                "h2": "Gdy szybko potrzebujesz polubień pod nowym filmem",
                "p": [
                    "Polubienia w pierwszej godzinie po publikacji dają ci, którzy widzą film wcześnie: obserwujący, którzy zaglądają, i pierwsi widzowie, którym TikTok go pokazuje. To dźwignia, którą kontrolujesz. Zwiększ liczbę prawdziwych obserwujących, którzy oglądają, a każdy nowy film zacznie z większą ich liczbą. Pakiet robi to równo; polubienia „natychmiast” tylko dekorują jeden film.",
                ],
                "image": {"image": "tiktok-hub", "alt": "Świeżo opublikowany film na TikToku zbiera pierwsze polubienia od obserwujących"},
            },
        ],
        "faqs": [
            ("Czy mogę dostać polubienia natychmiast pod nowy film na TikToku?", "Nie. Nie wysyłamy polubień pod konkretny film i nie zgrywamy ich z Twoim harmonogramem publikacji. Ludzie znajdują Twój profil przez cały miesiąc i lajkują to, co im się podoba."),
            ("Jak szybko zaczynają się polubienia?", "Zwykle w pierwszych dniach kampanii, gdy ludzie zaczynają trafiać na Twój profil. Potem przychodzą każdego dnia."),
            ("Dlaczego polubienia „natychmiast” to problem?", "Nie stoi za nimi żaden widz, więc pompują jedną liczbę, a czas oglądania, obserwowania i komentarze stoją w miejscu. Taki film wygląda na podparty, i dla ludzi, i w Twoich własnych statystykach."),
            ("Czy szybkie polubienia pomagają trafić na stronę Dla Ciebie?", "Nikt nie może obiecać miejsca na stronie Dla Ciebie i my tego nie robimy. Polubienia od ludzi, którzy obejrzeli, to część tego, jak film zdobywa szerszą publiczność; polubienia od kont, które nie oglądały, nie są."),
            ("Czy jest dzienna liczba polubień?", "Nie ma stałej dziennej liczby. Z pakietem {pick_name} polubienia zwykle składają się na {pick_likes} w miesiąc, więcej w ruchliwe dni, mniej w spokojne."),
        ],
    },
    {
        "service": "likes",
        "modifier": "free",
        "plan": "starter",
        "tool": "engagement-calculator",
        "slug": "tiktok/polubienia/za-darmo",
        "label": "Darmowe polubienia na TikToku: co za nimi stoi",
        "title": "Darmowe polubienia na TikToku: ile kosztują | Growsterr",
        "description": "Szukasz darmowych polubień na TikToku co 24 godziny? Nie rozdajemy ich. Czym są te codzienne oferty, plus darmowy kalkulator Twojego wskaźnika zaangażowania.",
        "h1": ("Darmowe polubienia na TikToku? ", "Zmierz polubienia, które już zdobywasz."),
        "intro": "Nie oferujemy darmowych polubień na TikToku, ani raz, ani co 24 godziny. Strony, które to robią, rozdają polubienia z kont lajkujących na polecenie i zwykle chcą w zamian Twojej nazwy użytkownika, maila albo logowania. Za darmo dajemy kalkulator na tej stronie: wpisz swoje liczby i zobacz, ilu Twoich obserwujących naprawdę reaguje na Twoje filmy.",
        "hero": {"image": "tiktok-likes", "alt": "Film na TikToku z polubieniami od widzów, którzy naprawdę go obejrzeli"},
        "sections": [
            {
                "h2": "Darmowe polubienia na TikToku co 24 godziny: jak to działa",
                "p": [
                    "Strony z codziennym odbiorem pozwalają wpisać nazwę użytkownika i raz dziennie zgarnąć małą paczkę polubień, często około 100. Polubienia za każdym razem pochodzą z tej samej puli kont, a prawdziwą ceną jest to, co oddajesz: mail do marketingu, uwagę dla reklam, czasem logowanie. Każda strona z Twoim logowaniem może też używać Twojego konta, lajkując cudze filmy w Twoim imieniu.",
                ],
            },
            {
                "h2": "A darmowe polubienia komentarzy na TikToku?",
                "p": [
                    "Polubienia komentarzy pochodzą z tych samych miejsc i mają tę samą wadę: nikt nie przeczytał komentarza. Pod Twoimi filmami polubienia komentarzy pojawiają się same, gdy toczy się rozmowa warta dołączenia. Odpowiadaj szybko na pierwsze komentarze i przypnij ten, który chcesz, żeby ludzie zobaczyli.",
                ],
            },
            {
                "h2": "Sposoby na więcej polubień bez płacenia",
                "ul": [
                    "Zacznij od momentu, który zatrzymuje przewijanie, a nie od wstępu.",
                    "Niech film trwa tyle, ile potrzebuje pomysł, i ani chwili dłużej: lajkują ci, którzy dotrwają do końca.",
                    "Publikuj, gdy Twoi obserwujący są aktywni; statystyki TikToka pokazują godziny.",
                    "Odpowiadaj na komentarze, zwłaszcza filmami, żeby ludzie mieli powód wracać.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Twórca odpowiada na komentarz widza nowym filmem na TikToku"},
            },
        ],
        "faqs": [
            ("Czy oferujecie darmowe polubienia na TikToku?", "Nie. Nie rozdajemy polubień, nie robimy okresów próbnych i nie dajemy próbek. Polubienia są w naszych miesięcznych pakietach, od prawdziwych ludzi, którzy znajdują Twój profil, a zrezygnować możesz w każdej chwili."),
            ("Czy mogę bezpiecznie dostać 100 darmowych polubień na TikToku?", "Nie od prawdziwych ludzi. Sto polubień rozdanych za nic pochodzi z kont zrobionych do tego celu, a strony, które je dają, zwykle chcą czegoś od Ciebie w zamian. Bezpieczne polubienia dają ludzie, którzy obejrzeli."),
            ("Co pokazuje kalkulator zaangażowania?", "Wpisz liczbę obserwujących oraz średnią liczbę polubień i komentarzy na film, a dostaniesz swój wskaźnik zaangażowania: jaka część publiczności reaguje. Działa w przeglądarce; nigdy nie dostajemy tych liczb."),
            ("Czy darmowe polubienia mogą obniżyć mój wskaźnik zaangażowania?", "Pośrednio. Konta, które za nimi stoją, nigdy nie wracają, a jeśli także Cię obserwują, liczba obserwujących rośnie, a reakcje nie. To ściąga wskaźnik w dół."),
            ("Ile polubień dałby płatny pakiet?", "W pakiecie {starter_name} ({starter_price} miesięcznie) typowy miesiąc to {starter_likes} polubień, wszystkie od ludzi, którzy też Cię obserwują. Większe pakiety docierają do większej liczby ludzi i dają więcej."),
        ],
    },
    # --- Views ----------------------------------------------------------------------------
    {
        "service": "views",
        "modifier": "cheap",
        "plan": "starter",
        "slug": "tiktok/wyswietlenia/tanio",
        "label": "Tanie wyświetlenia na TikToku",
        "title": "Tanie wyświetlenia na TikToku? To nie widzowie | Growsterr",
        "description": "Chcesz tanio kupić wyświetlenia na TikToku, nawet za dolara? Odtworzenie łatwo podrobić i niczego nie dowodzi. Nasze pakiety dają widzów, którzy oglądają.",
        "h1": ("Tanie wyświetlenia na TikToku? ", "Płać za oglądanie, a nie za odtworzenia."),
        "intro": "Jeśli chcesz tanio kupić wyświetlenia na TikToku, warto wiedzieć, dlaczego wyświetlenia to najtańsza liczba na platformie: wyświetlenie liczy się, gdy tylko film zacznie się odtwarzać, więc łatwo je zrobić bez widza. Nie sprzedajemy wyświetleń i nie liczymy ich z góry. Nasze pakiety sprowadzają na Twój profil prawdziwych ludzi, a ich wyświetlenia przychodzą z czasem oglądania, polubieniami i obserwowaniami.",
        "hero": {"image": "tiktok-watch-time", "alt": "Prawdziwi widzowie oglądają film na TikToku do samego końca"},
        "sections": [
            {
                "h2": "Czym naprawdę są wyświetlenia na TikToku za dolara",
                "p": [
                    "Dolar za tysiące wyświetleń kupuje odtworzenia: film włączany i porzucany przez program, raz za razem. Licznik rośnie. Średni czas oglądania i odsetek widzów, którzy oglądają do końca, spadają, a to właśnie te liczby pokazują, czy film kogokolwiek trzyma.",
                ],
            },
            {
                "h2": "Pakiet z wyświetleniami na TikToku, uczciwie",
                "p": [
                    "Nasze pakiety nie są wyceniane za wyświetlenie. Płacisz jedną miesięczną cenę, {starter_price} za {starter_name}, a my codziennie pokazujemy Twój profil prawdziwym ludziom. Zainteresowani oglądają Twoje filmy, często kilka, a te wyświetlenia przynoszą to, czego same wyświetlenia nigdy nie dają: czas oglądania, polubienia, komentarze i nowych obserwujących.",
                ],
            },
            {
                "h2": "Co sprawdzić w statystykach po kupnie wyświetleń",
                "ul": [
                    "Średni czas oglądania: prawdziwi widzowie zostawiają sekundy albo minuty; kupione odtworzenia prawie nic.",
                    "Obejrzenia całego filmu: odsetek widzów, którzy dotarli do końca.",
                    "Źródła ruchu: skąd przyszły wyświetlenia, na przykład ze strony Dla Ciebie, z Twojego profilu albo z kanału Obserwowane.",
                    "Nowych obserwujących w dni, gdy przyszły wyświetlenia: prawdziwi widzowie czasem obserwują; odtworzenia nigdy.",
                ],
                "image": {"image": "tiktok-hub", "alt": "Twórca czyta czas oglądania i źródła ruchu w statystykach TikToka"},
            },
        ],
        "faqs": [
            ("Ile kosztują wyświetlenia na TikToku w Growsterr?", "Wyświetlenia nie mają osobnej ceny. Są w każdym pakiecie, od ludzi, których sprowadza nasza kampania, i nie liczymy ich z góry. Pakiety zaczynają się od {from_price} miesięcznie."),
            ("Czy mogę kupić wyświetlenia na TikToku za dolara?", "Nie tutaj i nie u nikogo, kto pracuje z ludźmi. Za dolara nie pokażesz filmu tysiącom ludzi, którzy zdecydują się go obejrzeć. Kupisz za to zautomatyzowane odtworzenia, które pompują licznik i nic poza tym."),
            ("Dlaczego w Waszych pakietach nie ma liczby wyświetleń?", "Bo każde wyświetlenie to człowiek, który decyduje się obejrzeć, a ludzie co miesiąc decydują inaczej. Podajemy typowe zakresy dla obserwujących, polubień i komentarzy, a wyświetlenia przychodzą razem z nimi."),
            ("Czy tanie wyświetlenia pomogą mojemu filmowi zrobić viral?", "Nie. Film rozchodzi się, gdy ludzie, którzy go widzą, oglądają, powtarzają i udostępniają. Odtworzenia bez oglądania sprawiają, że film wygląda, jakby stracił wszystkich w pierwszej sekundzie."),
            ("Który pakiet kosztuje najmniej?", "Najtańszy jest {starter_name}, {starter_price} miesięcznie. Codziennie sprowadza na Twój profil prawdziwych ludzi, z których zwykle {starter_audience} zaczyna obserwować, a ich wyświetlenia, polubienia i komentarze przychodzą razem z nimi."),
        ],
    },
    {
        "service": "views",
        "modifier": "fast",
        "slug": "tiktok/wyswietlenia/szybko",
        "label": "Szybkie wyświetlenia na TikToku, wyjaśniamy",
        "title": "Wyświetlenia na TikToku „natychmiast”? Co to znaczy | Growsterr",
        "description": "Chcesz wyświetleń na TikToku „natychmiast”? To odtworzenia bez widzów, czyli boty. Nasza kampania rusza szybko, a prawdziwi ludzie oglądają codziennie.",
        "h1": ("Wyświetlenia na TikToku „natychmiast”? ", "Szybki start, a potem wzrost każdego dnia."),
        "intro": "Gdy ludzie kupują wyświetlenia na TikToku „natychmiast”, dostają licznik, który skacze, gdy nikt nie ogląda. My działamy w tempie widzów: kampania rusza w ciągu kilku dni od zamówienia, ludzie wcześnie zaczynają trafiać na Twój profil i oglądają filmy, które ich złapią. Wyświetlenia dają ci ludzie, każdego dnia, w ramach Twojego pakietu.",
        "hero": {"image": "tiktok-hub", "alt": "Ludzie odkrywają profil na TikToku i zaczynają oglądać jego filmy"},
        "sections": [
            {
                "h2": "Szybka realizacja wyświetleń: co jest możliwe",
                "p": [
                    "Szybka realizacja jest możliwa dla startu kampanii, a nie dla samych wyświetleń. Uruchomienie zajmuje niewiele czasu; potem wyświetlenia przychodzą w tempie, w jakim ludzie Cię odkrywają. Prawdziwy widz potrzebuje kilku sekund, żeby zdecydować, czy oglądać dalej, a kampania potrzebuje dni, żeby dotrzeć do wystarczającej ich liczby.",
                ],
            },
            {
                "h2": "Dlaczego wyświetlenia „natychmiast” łatwo wypatrzyć",
                "ul": [
                    "Tysiące wyświetleń, a obok prawie żadnych polubień, komentarzy ani udostępnień.",
                    "Średni czas oglądania, który ledwo drgnie, gdy licznik skacze.",
                    "Wyświetlenia, które przychodzą jednym blokiem, a potem stają w miejscu.",
                    "Brak nowych obserwujących w dniu skoku.",
                ],
            },
            {
                "h2": "Szybkie, prawdziwe wyświetlenia: gdzie trafiają",
                "p": [
                    "Nie możemy wysłać wyświetleń pod jeden film ani zgrać ich z godziną publikacji. Ludzie, którzy trafiają na Twój profil, sami wybierają, co obejrzeć: film na górze, przypięty, coś, co przyciągnęło ich wzrok w siatce. To wolniejsze niż licznik i właśnie dlatego wyświetlenia przychodzą z czasem oglądania.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Widz wybiera z siatki profilu twórcy, który film na TikToku obejrzeć"},
            },
        ],
        "faqs": [
            ("Kiedy przychodzą pierwsze wyświetlenia?", "Zwykle w pierwszych dniach kampanii, gdy ludzie zaczynają odwiedzać Twój profil. Potem przychodzą każdego dnia, w miarę jak kolejni ludzie Cię odkrywają."),
            ("Czy możecie dostarczyć wyświetlenia natychmiast pod nowy film?", "Nie. Nie dostarczamy wyświetleń pod wybrany film, a wyświetlenia „natychmiast” pochodzą tylko z zautomatyzowanych odtworzeń. Nasi widzowie sami wybierają, które filmy oglądają."),
            ("Czy szybka realizacja jest bezpieczniejsza niż „natychmiast”?", "Problemem nie jest tempo, tylko to, kto ogląda. Wolno sączone zautomatyzowane odtworzenia są równie puste jak te „natychmiast”. Wyświetlenia od ludzi to jedyny rodzaj wart posiadania, w każdym tempie."),
            ("Czy szybkie wyświetlenia pomagają na stronie Dla Ciebie?", "Nikt nie może obiecać miejsca na stronie Dla Ciebie. Filmowi pomaga to, że ludzie oglądają go do końca i reagują, a to robią prawdziwi widzowie, a zautomatyzowane wyświetlenia nigdy."),
            ("Gdzie zobaczę, jak rosną moje wyświetlenia?", "Twój panel dotyczy ludzi: ilu odwiedziło Twój profil dzięki kampanii i ilu z nich zaczęło obserwować. Wyświetlenia widać we własnych statystykach TikToka, obok czasu oglądania, i to najlepsze miejsce, żeby zobaczyć prawdziwych widzów w akcji."),
        ],
    },
    {
        "service": "views",
        "modifier": "free",
        "plan": "starter",
        "tool": "engagement-calculator",
        "slug": "tiktok/wyswietlenia/za-darmo",
        "label": "Darmowe wyświetlenia na TikToku: co w ofercie",
        "title": "1000 darmowych wyświetleń na TikToku? Prawda | Growsterr",
        "description": "Szukasz darmowych wyświetleń na TikToku, na przykład 1000 za darmo? Nie rozdajemy ich. Co dają takie oferty i jak zdobyć prawdziwe wyświetlenia bez płacenia.",
        "h1": ("Darmowe wyświetlenia na TikToku? ", "Zdobywaj takie, za którymi ktoś ogląda."),
        "intro": "Chcesz dostać 1000 wyświetleń na TikToku za darmo? Nie rozdajemy wyświetleń i nie robimy okresów próbnych. Darmowe wyświetlenia to odtworzenia włączane przez program: podbijają licznik jednego filmu i zostawiają czas oglądania tam, gdzie był. Na tej stronie znajdziesz uczciwe sposoby na więcej wyświetleń bez płacenia, kalkulator do sprawdzenia zaangażowania i nasze pakiety, jeśli chcesz do tego prawdziwych ludzi.",
        "hero": {"image": "tiktok-creator", "alt": "Twórca ustawia telefon, żeby nagrać film na TikToka wart obejrzenia"},
        "sections": [
            {
                "h2": "Co daje oferta 1000 darmowych wyświetleń na TikToku",
                "p": [
                    "Wklejasz link do filmu, czekasz, a licznik rośnie o tysiąc. Nikt nie widział filmu. Odtworzenia pochodzą z automatycznych sesji, które go włączają i zatrzymują, a ludzie, którzy je oferują, zarabiają gdzie indziej: na reklamach na stronie, na Twoim adresie e-mail albo na płatnych paczkach, które sprzedadzą Ci potem.",
                ],
            },
            {
                "h2": "Darmowe wyświetlenia na TikToku po wolnej, prawdziwej drodze",
                "ul": [
                    "Niech pierwsza sekunda się liczy: pytanie, odsłona albo ruch, zanim padnie jakikolwiek wstęp.",
                    "Użyj dźwięku albo tematu, który ludzie oglądają teraz, póki jeszcze rośnie.",
                    "Dodaj napisy na ekranie, bo wielu ludzi przewija bez dźwięku.",
                    "Publikuj regularnie, żeby każdy film trafiał do ludzi, którym spodobał się poprzedni.",
                    "Odpowiedz na komentarz filmem: osoba, która pytała, już czeka, żeby go obejrzeć.",
                ],
            },
            {
                "h2": "Wyświetlenia, za którymi stoją ludzie",
                "p": [
                    "Nasze pakiety nie liczą wyświetleń; sprowadzają widzów. Każdego dnia prawdziwi ludzie w wybranym przez Ciebie miejscu odkrywają Twój profil i oglądają to, co ich złapie. Ich wyświetlenia przychodzą z polubieniami, komentarzami i obserwowaniami, dlatego wyświetlenie od człowieka waży więcej niż tysiąc od skryptu.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Nowi widzowie z wybranego miasta oglądają filmy twórcy na TikToku"},
            },
        ],
        "faqs": [
            ("Czy mogę dostać darmowe wyświetlenia na TikToku od Growsterr?", "Nie. Nie rozdajemy wyświetleń, nie dajemy darmowych próbek i nie robimy okresów próbnych. Wyświetlenia dają prawdziwi ludzie, których sprowadzają nasze pakiety, od {from_price} miesięcznie, a zrezygnować możesz, kiedy chcesz."),
            ("Czy strony z darmowymi wyświetleniami na TikToku są bezpieczne?", "Większość potrzebuje tylko linku do filmu, więc Twoje konto nie jest narażone tak jak przy logowaniu. Ale wyświetlenia są zautomatyzowane, a film pełen odtworzeń, których nikt nie oglądał, ma liczby, które się nie sumują."),
            ("Jak odróżnić prawdziwe wyświetlenia od zautomatyzowanych?", "W statystykach filmu zestaw wyświetlenia ze średnim czasem oglądania i odsetkiem osób, które obejrzały do końca. Prawdziwi widzowie zostawiają czas oglądania; zautomatyzowane odtworzenia nie."),
            ("Po co kalkulator zaangażowania na stronie o wyświetleniach?", "Bo same wyświetlenia mówią niewiele. Kalkulator daje Twój wskaźnik zaangażowania, czyli odsetek obserwujących, którzy reagują na Twoje filmy, liczony w przeglądarce; nic nie trafia do nas."),
            ("Czy Wasze pakiety dają ustaloną liczbę wyświetleń?", "Nie. Każde wyświetlenie to ktoś, kto decyduje się obejrzeć, więc nie liczymy ich z góry. Ci sami ludzie, którzy oglądają, zostawiają zwykle {starter_likes} polubień miesięcznie w pakiecie {starter_name}, a wielu zaczyna obserwować."),
        ],
    },
    {
        "service": "views",
        "modifier": "free-trial",
        "plan": "starter",
        "slug": "tiktok/wyswietlenia/darmowy-test",
        "label": "Darmowy test wyświetleń na TikToku",
        "title": "Darmowy test wyświetleń na TikToku? Miesiąc bez umowy | Growsterr",
        "description": "Szukasz darmowego testu wyświetleń na TikToku? Nie oferujemy go. Dlaczego test wyświetleń niczego nie dowodzi i co pokazuje pierwszy miesiąc bez umowy.",
        "h1": ("Darmowy test wyświetleń na TikToku? ", "Dowiódłby tylko, że licznik się rusza."),
        "intro": "Jeśli chcesz wypróbować darmowy test wyświetleń na TikToku przed zakupem, powiemy to, co powiedzielibyśmy znajomemu: test wyświetleń pokazuje, że licznik może pójść w górę, a to już wiesz. Nie pokaże, czy ktokolwiek oglądał. Nie robimy testów. Oferujemy miesięczny pakiet, który anulujesz w każdej chwili, więc Twój pierwszy miesiąc to prawdziwy test z prawdziwymi ludźmi.",
        "hero": {"image": "tiktok-likes", "alt": "Twórca porównuje miesiąc wyświetleń na TikToku z polubieniami od prawdziwych widzów"},
        "sections": [
            {
                "h2": "Dlaczego test wyświetleń niczego nie dowodzi",
                "p": [
                    "Testowe wyświetlenia to zwykle kilkaset albo tysiąc odtworzeń pod wybranym filmem, dostarczonych w kilka minut. Pokazują tempo i nic więcej, bo wyświetlenia to jedyna liczba, którą każdy wyprodukuje bez publiczności. Test na nich oparty sprawdza oprogramowanie sprzedawcy, a nie Twój film.",
                ],
            },
            {
                "h2": "Co zamiast tego pokazuje pierwszy miesiąc",
                "ul": [
                    "Czy prawdziwi ludzie trafiają na Twój profil: panel codziennie liczy wizyty z kampanii.",
                    "Czy zostają: czas oglądania Twoich filmów w statystykach TikToka.",
                    "Czy obserwują: nowi obserwujący dzień po dniu, z miejsca, które wskazałeś.",
                    "Które filmy wybierają: te, które zbierają nowe polubienia i komentarze.",
                ],
            },
            {
                "h2": "Jak przestać, jeśli to nie dla Ciebie",
                "p": [
                    "Nie ma umowy ani okresu wypowiedzenia. Zatrzymaj subskrypcję na swoim koncie, kiedy zdecydujesz; kampania trwa do końca opłaconego miesiąca, a kolejna płatność nie zostanie pobrana. Jeśli to dla Ciebie, nic nie rób, a pakiet się odnowi.",
                ],
            },
        ],
        "faqs": [
            ("Czy oferujecie darmowy test wyświetleń na TikToku?", "Nie. Nie robimy testów i nie dajemy próbek. Możesz zacząć od {starter_name} za {starter_price} na miesiąc i zrezygnować w każdej chwili."),
            ("Czy mogę kupić małą testową paczkę wyświetleń?", "Nie. Wyświetlenia nie są sprzedawane osobno ani w paczkach; przychodzą z prawdziwymi ludźmi, których sprowadza każdy pakiet."),
            ("Dlaczego zacząć od płatnego miesiąca, a nie od testu?", "Prawdziwy zasięg kosztuje od pierwszego dnia, a miesiąc wystarczy, żeby zobaczyć wzór: wizyty, obserwowania i filmy, które ludzie wybierają. Kilka godzin testowych wyświetleń pokazałoby tylko poruszającą się liczbę."),
            ("Czy wyświetlenia zostają po końcu miesiąca?", "Już policzone wyświetlenia zostają pod filmami. Gdy pakiet się kończy, przestają przychodzić nowi odwiedzający z kampanii, a Twoje filmy żyją dalej z publicznością, którą zbudowałeś, w tym ze zdobytymi obserwującymi."),
            ("Który pakiet wypróbować najpierw?", "{starter_name} pasuje do większości kont na starcie. Jeśli Twoje filmy już same mają stałe wyświetlenia, {rising_name} od pierwszego dnia dociera do większej liczby ludzi."),
        ],
    },
    # --- Comments -------------------------------------------------------------------------
    {
        "service": "comments",
        "modifier": "fast",
        "slug": "tiktok/komentarze/szybko",
        "label": "Szybkie komentarze na TikToku, uczciwie",
        "title": "Komentarze na TikToku „natychmiast”? Dlaczego nie | Growsterr",
        "description": "Chcesz komentarzy na TikToku „natychmiast”? Prawdziwy komentarz wymaga kogoś, kto obejrzał. Nasze przychodzą przez cały miesiąc, zwykle {starter_comments}.",
        "h1": ("Komentarze na TikToku „natychmiast”? ", "Ktoś musi najpierw obejrzeć."),
        "intro": "Jeśli chcesz kupić komentarze na TikToku „natychmiast”, wyobraź sobie, skąd miałyby się wziąć: nikt nie obejrzy filmu, nie wymyśli, co powiedzieć, i nie napisze tego sekundy po płatności. Komentarze „natychmiast” są napisane z góry, z kont, które nigdy nie oglądały. Nasze piszą prawdziwi ludzie, których kampania sprowadza na Twój profil, po kilku przez cały miesiąc: zwykle {starter_comments} w pakiecie {starter_name}.",
        "hero": {"image": "tiktok-creator", "alt": "Twórca czyta nowe komentarze widzów pod filmem na TikToku"},
        "sections": [
            {
                "h2": "Jak wyglądają komentarze „natychmiast”",
                "p": [
                    "Przychodzą gromadą, w odstępach kilku minut, z profili bez filmów. Są krótkie i pasowałyby pod każdy film: emoji ognia, „tak prawdziwe”, „uwielbiam to”. Widzowie to zauważają, tak samo jak każdy, kto ocenia Twoje konto pod kątem współpracy, bo to w komentarzach ludzie sprawdzają, kto naprawdę ogląda.",
                ],
            },
            {
                "h2": "Prawdziwe tempo komentarzy",
                "ul": [
                    "Ludzie najpierw oglądają, a potem decydują, czy mają coś do powiedzenia. Większość nie ma i to normalne.",
                    "W ramach pakietu mniej więcej jeden nowy obserwujący na dziesięciu zostawia gdzieś komentarz, własnymi słowami.",
                    "Komentarze rozkładają się na cały miesiąc i na filmy, które ludzie wybierają; nie możemy ich wysłać pod jeden film.",
                    "Odpowiedzi rodzą odpowiedzi: jeden prawdziwy komentarz często przyciąga kolejne.",
                ],
            },
            {
                "h2": "Jak szybciej dostać komentarze pod własnymi filmami",
                "p": [
                    "Najszybsze prawdziwe komentarze bierze się z pytania. Zakończ film pytaniem, na które da się odpowiedzieć jednym słowem, odpowiedz pierwszym komentującym w ciągu godziny i zamień dobry komentarz w kolejny film. Te nawyki sprawiają, że w komentarzach się dzieje, z kampanią lub bez niej.",
                ],
                "image": {"image": "tiktok-likes", "alt": "Widzowie odpowiadają na pytanie, które twórca zadał na końcu filmu na TikToku"},
            },
        ],
        "faqs": [
            ("Czy mogę dostać komentarze na TikToku natychmiast?", "Nie. Komentarze „natychmiast” mogą pochodzić tylko ze skryptu. Nasze piszą ludzie, którzy obejrzeli Twoje filmy, więc przychodzą przez dni i tygodnie, a nie minuty."),
            ("Kiedy zobaczę pierwsze komentarze?", "Zwykle w pierwszym tygodniu, gdy ludzie znajdą Twój profil i obejrzą kilka filmów. Przychodzą dalej, dopóki trwa kampania."),
            ("Czy mogę wybrać, który film dostanie komentarze?", "Nie. Ludzie komentują filmy, które ich poruszą, a my nie możemy kierować ich pod żaden konkretny. Najwięcej zbierają zwykle Twoje najmocniejsze i najnowsze filmy."),
            ("Ile komentarzy daje typowy miesiąc w każdym pakiecie?", "Rośnie to z zasięgiem: {pro_comments} w typowym miesiącu w pakiecie {pro_name}, {rising_comments} w {rising_name}, {starter_comments} w {starter_name}. To zakresy, nie liczby: komentowanie to wybór każdej osoby."),
            ("Czy komentarze są sprzedawane osobno?", "Nie. Są w każdym pakiecie, od tych samych ludzi, którzy obserwują i lajkują."),
        ],
    },
    {
        "service": "comments",
        "modifier": "free",
        "plan": "starter",
        "tool": "engagement-calculator",
        "slug": "tiktok/komentarze/za-darmo",
        "label": "Darmowe komentarze na TikToku",
        "title": "Darmowe komentarze na TikToku: prawdziwe bez płacenia | Growsterr",
        "description": "Chcesz darmowych komentarzy na TikToku? Nie rozdajemy ich, a generatory wrzucają gotowe zdania. Jak za darmo zdobyć komentarze od prawdziwych widzów.",
        "h1": ("Darmowe komentarze na TikToku? ", "Zamiast tego zacznij rozmowę."),
        "intro": "Nie oferujemy darmowych komentarzy na TikToku, a strony, które to robią, wrzucają te same krótkie zdania z kont, którymi nikt nie zarządza. Dobra wiadomość: prawdziwe komentarze to jedyny rodzaj zaangażowania, który możesz wywołać sam, za darmo, dając widzom coś, na co mogą odpowiedzieć. Oto jak, plus kalkulator, który pokaże, jak bardzo zaangażowana jest już Twoja publiczność.",
        "hero": {"image": "tiktok-hub", "alt": "Żywa sekcja komentarzy pod filmem na TikToku, w której widzowie sobie odpowiadają"},
        "sections": [
            {
                "h2": "Jak zdobyć komentarze na TikToku za darmo",
                "ul": [
                    "Zadaj w filmie jedno konkretne pytanie: „Którą byś wybrał?” dostaje odpowiedzi, a „co myślicie?” nie.",
                    "Zostaw coś otwartego: brakujący krok, wybór, drugą część, o którą ludzie mogą poprosić.",
                    "Odpowiadaj na komentarze filmami, żeby komentujący widzieli, jak ich słowa stają się treścią.",
                    "Przypnij komentarz, na który najbardziej chcesz, żeby inni odpowiedzieli.",
                    "Odpowiadaj wcześnie: pierwsze odpowiedzi nadają ton wszystkim, którzy przyjdą później.",
                ],
            },
            {
                "h2": "Co wrzucają generatory komentarzy",
                "p": [
                    "Generatory komentarzy i aplikacje do wymiany zapełniają film zdaniami w rodzaju „super”, „wow” albo pojedynczym emoji, z profili bez historii. Aplikacje do wymiany oczekują też, że w zamian będziesz komentować filmy obcych, więc Twoje imię ląduje pod treściami, których nigdy nie oglądałeś. Nic z tego nie brzmi jak widz, bo nic z tego nim nie jest.",
                ],
            },
            {
                "h2": "Komentarze od prawdziwych ludzi, w pakiecie",
                "p": [
                    "Jeśli chcesz mieć w komentarzach więcej ludzi, niż przynosi Twój własny zasięg, nasze pakiety ich sprowadzają: prawdziwych ludzi, którzy znajdują Twój profil, oglądają i czasem mają coś do powiedzenia. Zwykle {starter_comments} komentarzy miesięcznie w pakiecie {starter_name} za {starter_price}, ich własnymi słowami, razem z nowymi obserwującymi i polubieniami.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Twórca przypina pytanie widza na górze komentarzy"},
            },
        ],
        "faqs": [
            ("Czy Growsterr będzie publikować darmowe komentarze pod moimi filmami?", "Nie. Nie rozdajemy komentarzy, nie robimy okresów próbnych i nie sprzedajemy ich osobno. Są w naszych miesięcznych pakietach, pisane przez prawdziwych ludzi, a zrezygnować możesz w każdej chwili."),
            ("Dlaczego niektóre filmy dostają tak dużo komentarzy?", "Zwykle dlatego, że do nich zapraszają: mocna opinia, pytanie, błąd, który ludzie chcą poprawić, albo temat, na którym ludziom zależy. Komentarze idą za rozmową, a nie za liczbą wyświetleń."),
            ("Po co najpierw sprawdzać wskaźnik zaangażowania?", "Pokazuje, jaka część Twoich obserwujących reaguje na przeciętny film polubieniem albo komentarzem. Jeśli wskaźnik jest niski, sama większa liczba obserwujących tego nie naprawi; naprawią to filmy, które dają ludziom coś, na co mogą zareagować."),
            ("Czy aplikacje do wymiany komentarzy są bezpieczne?", "Wymagają, żebyś działał we własnym imieniu, komentując filmy obcych, a niektóre chcą Twojego logowania. Nawet te nieszkodliwe zostawiają Twoją sekcję komentarzy pełną słów, których nikt nie miał na myśli."),
            ("Czy mogę napisać komentarze, a Wy je opublikujecie?", "Nie. Nigdy nie piszemy ani nie publikujemy komentarzy; ludzie piszą swoje. Właśnie dlatego warto je czytać."),
        ],
    },
    {
        "service": "comments",
        "modifier": "ai",
        "slug": "tiktok/komentarze/ai",
        "label": "Komentarze na TikToku pisane przez AI",
        "title": "Komentarze AI na TikToku? Ludzie piszą lepiej | Growsterr",
        "description": "Myślisz o komentarzach na TikToku pisanych przez AI? Brzmią gładko i nic nie mówią. Nasze piszą prawdziwi widzowie, własnymi słowami, w każdym pakiecie.",
        "h1": ("Komentarze na TikToku od AI? ", "Widzowie to wyczują."),
        "intro": "AI napisze sto komentarzy na TikToka w minutę i właśnie w tym problem z ich kupowaniem: żaden z autorów nie obejrzał Twojego filmu. Komentarze od AI brzmią gładko, chwalą ogólnikowo i przychodzą z kont, które istnieją po to, żeby je publikować. Nie używamy AI ani skryptów. Nasze piszą prawdziwi ludzie, którzy znaleźli Twój profil i mieli coś do powiedzenia, około {starter_comments} w typowym miesiącu w pakiecie {starter_name}.",
        "hero": {"image": "tiktok-watch-time", "alt": "Widz pisze osobisty komentarz po obejrzeniu filmu na TikToku"},
        "sections": [
            {
                "h2": "Jak zdradzają się komentarze od AI",
                "ul": [
                    "Opisują film ogólnikami, nigdy szczegółem, który wyłapałby tylko widz.",
                    "Są wygładzone i grzeczne, bez slangu, literówek i wewnętrznych żartów prawdziwej sekcji komentarzy.",
                    "Nie odpowiadają sobie nawzajem i nie wracają do rozmowy.",
                    "Konta, które je publikują, nie mają filmów, obserwujących ani historii.",
                ],
            },
            {
                "h2": "Co daje prawdziwy komentarz, a czego nie da AI",
                "p": [
                    "Prawdziwy komentarz to człowiek, który mówi Ci, co trafiło: żart, który powtórzy, krok, na którym utknął, produkt, który chce kupić. To informacja, którą wykorzystasz w kolejnym filmie. Komentarz od AI mówi tylko, że ktoś za niego zapłacił, i to samo wyczytują ludzie, którzy czytają Twoje komentarze.",
                ],
            },
            {
                "h2": "Skąd biorą się nasze komentarze",
                "p": [
                    "Nasze kampanie codziennie pokazują Twój profil prawdziwym ludziom, w wybranym przez Ciebie mieście, regionie lub kraju. Część z nich ogląda, część obserwuje, a część komentuje: w swoim języku, o Twoim filmie, po swojemu. Nikt nie pisze za nich i żaden program nie pisze za nas.",
                ],
                "image": {"image": "tiktok-likes", "alt": "Prawdziwi widzowie zostawiają różne, konkretne komentarze pod tym samym filmem na TikToku"},
            },
        ],
        "faqs": [
            ("Czy używacie AI do pisania komentarzy na TikToku?", "Nie. Każdy komentarz pisze człowiek, ze swojego konta, o filmie, który obejrzał. W ogóle nie piszemy, nie generujemy i nie publikujemy komentarzy."),
            ("Czy komentarze pisane przez AI łamią zasady TikToka?", "Wytyczne społeczności TikToka uznają fałszywe zaangażowanie, w tym komentarze z kont stworzonych do ich publikowania, za niezgodne z zasadami. Nie powiemy, jak TikTok potraktuje konkretny przypadek; po prostu takich nie sprowadzamy."),
            ("Czy komentarze od AI mogą sprawić, że film wygląda na popularny?", "Na szybki rzut oka może. Dla każdego, kto je przeczyta albo zauważy, że żaden komentarz nie wspomina niczego konkretnego, wyglądają dokładnie na to, czym są."),
            ("Czy prawdziwe komentarze będą po polsku?", "Będą w języku, którym mówi komentujący, a ten zwykle pasuje do wybranego przez Ciebie miejsca. Skieruj kampanię na Polskę, a większość komentarzy będzie po polsku."),
            ("Czy mogę używać AI do odpowiadania na własne komentarze?", "To Twoja decyzja, ale to w odpowiedziach ludzie decydują, czy warto Cię obserwować. Szybka, osobista odpowiedź Twoim głosem zrobi więcej niż wygładzona."),
        ],
    },
    {
        "service": "comments",
        "modifier": "custom",
        "slug": "tiktok/komentarze/wlasna-tresc",
        "label": "Komentarze na TikToku z własną treścią",
        "title": "Komentarze z własną treścią na TikToku? | Growsterr",
        "description": "Chcesz kupić komentarze na TikToku z własną treścią? Nie publikujemy komentarzy ze scenariusza. Prawdziwi widzowie piszą swoje: zwykle {starter_comments} miesięcznie.",
        "h1": ("Komentarze na TikToku z własną treścią? ", "Najlepszych nie piszesz Ty."),
        "intro": "Komentarze na TikToku z własną treścią pozwalają Ci napisać słowa i kazać kontom opublikować je pod Twoim filmem. To kuszące: właściwe pytanie, właściwa pochwała, dokładnie tam, gdzie chcesz. Nie oferujemy tego, bo komentarz, który napisałeś, to wciąż Twój głos, tylko na cudzym profilu. Nasze komentarze piszą prawdziwi ludzie, którzy oglądają Twoje filmy i sami decydują, co powiedzieć.",
        "hero": {"image": "tiktok-creator", "alt": "Twórca czyta na telefonie spontaniczne komentarze widzów"},
        "sections": [
            {
                "h2": "Kłopot z komentarzami, które piszesz sam",
                "p": [
                    "Komentarze ze scenariusza zwykle brzmią jak ich autor. Chwalą produkt z nazwy, zadają dokładnie to pytanie, na które film odpowiada za chwilę, i zgadzają się trochę zbyt gładko. Widzowie, którzy codziennie czytają komentarze, rozpoznają ten wzór, a kupiona rozmowa każe im wątpić także w to, co było prawdziwe.",
                ],
            },
            {
                "h2": "Kształtuj rozmowę, nie pisząc jej",
                "ul": [
                    "Przypnij własny komentarz z pytaniem, które wpisałbyś do scenariusza.",
                    "Powiedz to w opisie albo zakończ tym film.",
                    "Odpowiedz na komentarz najbliższy temu, czego chciałeś, i przypnij tę odpowiedź.",
                    "Zamień najlepsze prawdziwe pytanie w kolejny film.",
                ],
            },
            {
                "h2": "Prawdziwe komentarze, w każdym pakiecie",
                "p": [
                    "Każdego dnia pakietu prawdziwi ludzie trafiają na Twój profil dzięki naszym kampaniom. Część z nich komentuje, własnymi słowami i we własnym języku, pod wybranymi przez siebie filmami: około {starter_comments} komentarzy w typowym miesiącu w pakiecie {starter_name}, a więcej w większych pakietach. Nie wybierasz, co powiedzą, i właśnie dlatego komentarze są wiarygodne.",
                ],
                "image": {"image": "tiktok-hub", "alt": "Spontaniczne komentarze prawdziwych widzów pod filmem twórcy na TikToku"},
            },
        ],
        "faqs": [
            ("Czy mogę przesłać Wam komentarze, które chcę opublikować?", "Nie. Nie publikujemy komentarzy i nie możemy prosić ludzi, żeby napisali coś konkretnego. Wszystko, co pojawia się w Twoich komentarzach dzięki naszym kampaniom, to czyjaś własna reakcja."),
            ("A komentarze ze scenariusza na premierę produktu?", "Premiera to moment, gdy szczere reakcje liczą się najbardziej: ludzie czytają komentarze, żeby zdecydować, czy kupić. Rozwijaj konto w tygodniach przed nią, żeby prawdziwi ludzie byli na miejscu i zareagowali, gdy film się pojawi."),
            ("Czy komentarze z własną treścią mogą zaszkodzić mojej wiarygodności?", "Mogą, bo to w komentarzach ludzie sprawdzają, czy publiczność jest prawdziwa. Kilka, które brzmią jak reklama, potrafi zniweczyć zaufanie zbudowane przez te szczere."),
            ("Czy mogę usuwać komentarze, które mi się nie podobają?", "Tak. Twoja sekcja komentarzy należy do Ciebie: możesz usuwać, filtrować i przypinać komentarze albo wyłączyć je pod filmem. Prawdziwi ludzie czasem napiszą coś, czego Ty byś nie napisał, i to część powodu, dla którego się im ufa."),
            ("Czy potrzebujecie mojego konta, żeby publikować komentarze?", "Nie. Nigdy niczego nie publikujemy i nigdy nie potrzebujemy Twojego hasła. Ludzie, którzy komentują, używają własnych kont."),
        ],
    },
]
