"""Polish Instagram pages: comments, likes, and the ways people ask for followers and likes
(stopniowo, organicznie, lokalnie, konto prywatne...). Mirrors en/instagram_core.py. Keys and
placeholders: docs/CONTENT.md; word forms: pl/ui.py."""

UPDATED = "2026-11-09"

PAGES = [
    # --- Comments -----------------------------------------------------------------------
    {
        "service": "comments",
        "slug": "instagram/komentarze",
        "label": "Komentarze na Instagramie",
        "title": "Kup komentarze na Instagramie od prawdziwych ludzi | Growsterr",
        "description": "Chcesz kupić komentarze na Instagramie? U nas są w każdym pakiecie, a piszą je prawdziwi ludzie własnymi słowami. Zwykle {starter_comments} miesięcznie.",
        "h1": ("Kup komentarze na Instagramie ", "od ludzi, którzy piszą szczerze."),
        "intro": "Jeśli chcesz kupić komentarze na Instagramie, wiedz, że dostarczamy je tylko w jeden sposób: w miesięcznym pakiecie, od prawdziwych ludzi, którzy odkrywają Twoje posty i mają coś do powiedzenia. Zwykle {starter_comments} komentarzy miesięcznie w pakiecie {starter_name}, {pick_comments} w pakiecie {pick_name}.",
        "hero": {"image": "instagram-real-people", "alt": "Ludzie zostawiają pod postem na Instagramie własne komentarze, pytania i emoji"},
        "sections": [
            {
                "h2": "Jak wygląda prawdziwa sekcja komentarzy",
                "p": [
                    "Prawdziwe komentarze są nierówne. Ktoś pyta, skąd jest kurtka, ktoś inny oznacza znajomego, jeszcze ktoś pisze dwa słowa i emoji. Właśnie ta nierówność sprawia, że sekcja komentarzy jest wiarygodna, i właśnie jej nie da się podrobić skryptem.",
                    "Komentarze kupowane hurtem zwykle przychodzą jako niemal identyczne zdania z kont, które same nic nie publikują. Każdy, kto przewija feed, to zauważy, także marki i współpracownicy, na których chcesz zrobić wrażenie.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "Twórca przy biurku odpowiada na komentarze pod postem na Instagramie"},
            },
            {
                "h2": "Ile komentarzy daje każdy pakiet",
                "ul": [
                    "{starter_name} za {starter_price} miesięcznie zwykle daje {starter_comments} komentarzy, pod postami, które ludziom najbardziej się podobają.",
                    "{rising_name} za {rising_price} zwykle daje {rising_comments}, a Ty wybierasz posty, które dostają uwagę.",
                    "{pro_name} za {pro_price} zwykle daje {pro_comments}, do tego priorytetowe miejsce i bezpośrednią linię na WhatsAppie.",
                ],
            },
            {
                "h2": "Dlaczego komentarze są tylko w pakiecie",
                "p": [
                    "Post z czterdziestoma komentarzami i tuzinem polubień sam mówi, co się stało. Komentarze wyglądają dobrze tylko obok obserwowań, polubień i wyświetleń, które przynosi prawdziwa uwaga. Dlatego sprowadzamy uwagę, a komentarze z niej wyrastają.",
                ],
            },
        ],
        "faqs": [
            ("Czy mogę dostać komentarze na Instagramie bez pakietu?", "Nie. Komentarze są tylko w naszych miesięcznych pakietach i piszą je ludzie, którzy trafili na Twój profil dzięki naszym kampaniom. Nikt nie pisze ich na zamówienie, dlatego brzmią jak rozmowa."),
            ("Czy mogę wybrać, co napiszą?", "Nie. Ludzie piszą własnymi słowami, więc nie ma czego oskryptować, a komentarze pisane według wytycznych rzadko brzmią jak czyjaś szczera reakcja. Możesz za to, w pakiecie {rising_name} lub {pro_name}, wybrać, gdzie trafia uwaga: posty, które wskażesz."),
            ("Kiedy pojawiają się komentarze?", "Przez cały miesiąc, po kilka naraz, w miarę jak ludzie odkrywają Twoje posty. Sto komentarzy w dziesięć minut to byłby skrypt, a nie publiczność."),
            ("Czy komentarze pomagają postom dotrzeć do większej liczby osób?", "Komentarze pokazują, że post kogoś obchodzi, a Instagram to zauważa. Prawdziwe do tego się dokładają. Nie obiecujemy zasięgu, bo nikt uczciwy nie może, ale komentarze ze skryptu dodają tylko szumu."),
            ("Czy potrzebujecie mojego hasła?", "Nie. Potrzebujemy nazwy użytkownika na Instagramie i miejsca, z którego mają pochodzić Twoi odbiorcy. Konto powinno być publiczne, żeby ludzie mogli czytać Twoje posty i dołączać do rozmowy."),
        ],
    },
    # --- Followers: the ways people ask for them ---------------------------------------
    {
        "service": "followers",
        "modifier": "gradual",
        "slug": "instagram/obserwujacy/stopniowo",
        "label": "Obserwujący na Instagramie stopniowo",
        "title": "Obserwujący na Instagramie codziennie, nie hurtem | Growsterr",
        "description": "Kup obserwujących na Instagramie stopniowo, a nie jednym rzutem: prawdziwi ludzie znajdują Twój profil codziennie przez 30 dni, bez nagłych skoków.",
        "h1": ("Obserwujący na Instagramie codziennie, ", "tak jak ludzie naprawdę obserwują."),
        "intro": "Jeśli wolisz kupić obserwujących na Instagramie stopniowo, a nie wszystkich naraz, myślisz już jak publiczność. Nasze kampanie pokazują Twój profil prawdziwym ludziom każdego dnia przez 30 dni, więc obserwujący przybywają po trochu, dzień po dniu: zwykle {pick_audience} w miesiąc z pakietem {pick_name}.",
        "hero": {"image": "instagram-followers-1000", "alt": "Liczba obserwujących na Instagramie rośnie po trochu każdego dnia przez cały miesiąc"},
        "sections": [
            {
                "h2": "Dostawa kroplówką to ustawienie. Codzienny wzrost to kampania.",
                "p": [
                    "Niektóre serwisy sprzedają powolną „kroplówkę”: paczkę kont wypuszczaną po kilka naraz, żeby wykres wyglądał naturalnie. To dalej boty, zamaskowane jest tylko tempo.",
                    "Nasze tempo w ogóle nie jest ustawieniem. Twój profil jest pokazywany ludziom codziennie, a każde obserwowanie dzieje się wtedy, gdy ktoś tak zdecyduje. Łagodna krzywa to po prostu to, jak z zewnątrz wygląda wybór ludzi.",
                ],
            },
            {
                "h2": "Dlaczego powoli działa lepiej niż wszystko naraz",
                "ul": [
                    "Równy wzrost wygląda na to, czym jest: konto, które ludzie wciąż odkrywają.",
                    "Nowi obserwujący z każdego dnia trafiają na Twój kolejny post, póki ich zainteresowanie jest świeże.",
                    "Nie ma nagłego skoku, który marka albo obserwujący mogliby zakwestionować.",
                    "Widzisz, co działa, bo każdy dzień to osobny punkt danych.",
                ],
            },
            {
                "h2": "Jak czytać swoje dzienne liczby",
                "p": [
                    "Panel pokazuje dla każdego dnia, ile osób odwiedziło Twój profil dzięki kampanii i ile z nich zaczęło Cię obserwować. Jedne dni są bardziej ruchliwe od innych: mocny post, weekend, święto. W skali miesiąca składają się na typowy zakres, a nie na stały dzienny limit.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "Twórca sprawdza wykres wizyt na profilu i nowych obserwujących dzień po dniu"},
            },
        ],
        "faqs": [
            ("Ilu obserwujących dostanę każdego dnia?", "Nie ma stałej dziennej liczby, bo ludzie decydują sami. W ciągu miesiąca {pick_name} zwykle daje {pick_audience}, więc przeciętny dzień przynosi kawałek tej liczby: jednego dnia więcej, innego mniej."),
            ("Czy mogę sam ustawić tempo dostawy?", "Nie, i nie musisz. Tempo wyznaczają ludzie, a nie pokrętło: kampania działa codziennie, a obserwujący przychodzą wtedy, gdy ktoś tak wybierze."),
            ("Czy stopniowy wzrost jest mniej ryzykowny niż duża paczka?", "Setki obserwujących w godzinę to ślad, który zostawiają boty. Stopniowy wzrost z prawdziwymi ludźmi takiego śladu nie zostawia, bo nim nie jest. Nie wypowiadamy się za Instagram w sprawie żadnego konta; możemy tylko dopilnować, żeby każdy obserwujący od nas był człowiekiem."),
            ("Czy stopniowo znaczy mniej?", "Nie. Stopniowo opisuje kształt, nie sumę. Typowy miesięczny zakres jest taki sam, niezależnie od tego, czy ktoś zaobserwuje Cię drugiego, czy dwudziestego dziewiątego dnia. Po prostu przychodzi tak, jak buduje się publiczność."),
            ("Czy polubienia i komentarze też przychodzą stopniowo?", "Tak. Ci sami ludzie lajkują i komentują, gdy trafiają na Twoje posty, więc jedno i drugie rośnie razem z obserwującymi. Z pakietem {pick_name} to zwykle {pick_likes} polubień i {pick_comments} komentarzy w miesiąc."),
        ],
    },
    {
        "service": "followers",
        "modifier": "live",
        "slug": "instagram/obserwujacy/na-zywo",
        "label": "Obserwujący na Instagramie: realizacja i live",
        "title": "Szybka realizacja obserwujących na Instagramie | Growsterr",
        "description": "Jak szybka jest realizacja, gdy kupujesz obserwujących od prawdziwych ludzi? Kampania rusza szybko, rośnie codziennie i buduje widownię na Twoje live.",
        "h1": ("Obserwujący na Instagramie z szybką realizacją? ", "Oto co znaczy „szybko”."),
        "intro": "Kupno obserwujących na Instagramie z szybką realizacją zwykle oznacza jedno z dwóch: licznik, który skacze w kilka minut, albo kampanię, która rusza od razu i trwa dalej. My robimy tylko to drugie. Kampania startuje szybko, prawdziwi ludzie przychodzą od pierwszych dni, a panel pokazuje, co przyniósł każdy dzień.",
        "hero": {"image": "instagram-creator-studio", "alt": "Twórca przygotowuje się do transmisji na żywo na Instagramie przy biurku"},
        "sections": [
            {
                "h2": "Szybko tam, gdzie to ważne, nigdy „natychmiast”",
                "p": [
                    "Szybki jest start. Uruchamiamy kampanię wkrótce po zamówieniu, a ludzie zaczynają widzieć Twój profil od pierwszych dni. Nie wciśniemy za to miesiąca prawdziwych decyzji w godzinę, bo jedyny sposób, żeby to zrobić, to konta, którymi nikt nie zarządza.",
                    "Porównując czas realizacji, patrz więc na to, kiedy zaczyna się prawdziwy wzrost i czy trwa dalej, a nie na to, jak szybko podskakuje liczba.",
                ],
            },
            {
                "h2": "Obserwujący na Twoje transmisje live",
                "p": [
                    "Widzowie live to po prostu obserwujący, którzy wpadają, gdy nadajesz na żywo. Instagram może powiadomić Twoich obserwujących o starcie transmisji, więc więcej osób, które same zdecydowały się Cię obserwować, to więcej osób, które mogą zajrzeć.",
                    "Nie sprzedajemy widzów na transmisje i nikt nie może obiecać tłumu o konkretnej godzinie: ludzie dołączają, gdy są zainteresowani i akurat mają czas. Obserwujący, których zdobywasz przez miesiąc, robią to najczęściej.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Obserwujący dołączają do transmisji live twórcy na Instagramie i komentują na bieżąco"},
            },
            {
                "h2": "Polubienia też przychodzą stopniowo",
                "p": [
                    "Polubienia mają ten sam rytm. Zostawiają je ludzie, którzy odkrywają Twój profil, więc spływają na posty powoli przez cały miesiąc, zwykle {pick_likes} z pakietem {pick_name}. Nie ma osobnego zamówienia polubień do zaplanowania ani nagłego wysypu do tłumaczenia.",
                ],
            },
        ],
        "faqs": [
            ("Jak szybko rusza realizacja?", "Szybko. Po złożeniu zamówienia uruchamiamy kampanię, a ludzie zaczynają odwiedzać Twój profil od pierwszych dni. Obserwowania zaczynają się razem z tymi wizytami i trwają cały miesiąc."),
            ("Czy mogę dostać obserwujących natychmiast?", "Nie. Dostawa „natychmiast” działa tylko z botami, bo żaden człowiek nie zaczyna obserwować konta kilka sekund po płatności. My zaczynamy szybko i rośniemy codziennie."),
            ("Czy będę mieć nowych obserwujących przed dzisiejszym live?", "Może kilku, jeśli kampania już trwa, ale nie zgramy ludzi z godziną transmisji. Jeśli zależy Ci na konkretnym live, zacznij kilka tygodni wcześniej, żeby nowi obserwujący zdążyli Cię poznać."),
            ("Czy sprzedajecie widzów na transmisje live na Instagramie?", "Nie. Widzowie live musieliby oglądać w konkretnej minucie, a tego nikt nie dostarczy uczciwie. Obserwujący, których sprowadzamy, mogą dołączać do Twoich transmisji sami z siebie."),
            ("Gdzie mogę śledzić realizację?", "W panelu, który dzień po dniu liczy wizyty na profilu z naszej kampanii i obserwowania, które z nich wyniknęły. Ogólna liczba obserwujących na Twoim koncie zmienia się też z innych powodów, w tym przez odobserwowania."),
        ],
    },
    {
        "service": "followers",
        "modifier": "no-drop",
        "slug": "instagram/obserwujacy/bez-spadkow",
        "label": "Obserwujący na Instagramie, którzy zostają",
        "title": "Trwali obserwujący na Instagramie, bez spadków | Growsterr",
        "description": "Chcesz kupić trwałych obserwujących na Instagramie, bez spadków? Boty znikają przy czystkach. Prawdziwi ludzie zostają, bo obserwowanie to był ich pomysł.",
        "h1": ("Trwali obserwujący na Instagramie ", "zaczynają się od prawdziwych ludzi."),
        "intro": "Każdy, kto szuka trwałych obserwujących na Instagramie, widział już ten drugi rodzaj: skok, a potem powolny wyciek w dół. Obserwujący odpadają, gdy od początku nie byli ludźmi. Nasi to ludzie, którzy sami zdecydowali się Cię obserwować, więc zostają tak jak każda prawdziwa publiczność, a jeśli ktoś odchodzi, to z takich samych powodów jak każdy obserwujący.",
        "hero": {"image": "instagram-followers", "alt": "Liczba obserwujących na Instagramie trzyma się i rośnie przez kilka miesięcy"},
        "sections": [
            {
                "h2": "Dlaczego kupieni obserwujący znikają",
                "p": [
                    "Instagram regularnie usuwa fałszywe i spamerskie konta. Jeśli Twoi obserwujący to właśnie takie konta, każda czystka odgryza kawałek Twojej liczby. Uzupełnienia dobijają ją z powrotem tym samym towarem, a cykl zaczyna się od nowa.",
                    "Człowieka czystka nie usuwa. Odchodzi tylko wtedy, gdy sam przestanie obserwować, a to zdarza się dużo rzadziej i Twoje posty mają na to wpływ.",
                ],
            },
            {
                "h2": "Co sprawia, że obserwujący zostają",
                "ul": [
                    "Sami Cię wybrali, a obserwowanie, które zaczyna się od zainteresowania, zwykle trwa.",
                    "Pochodzą stamtąd, gdzie mieszka Twoja publiczność, więc Twoje posty są dla nich zrozumiałe.",
                    "Widzą Twoje kolejne posty, a każdy dobry to powód, żeby zostać.",
                    "Twój rytm znaczy więcej niż cokolwiek, co robimy my: ludzie zostają dla postów, na które czekają.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Wieloletni obserwujący wciąż lajkują i komentują najnowszy post twórcy"},
            },
            {
                "h2": "„Bez spadków”, uczciwie zdefiniowane",
                "p": [
                    "Nie powiemy Ci, że nikt nigdy nie przestanie Cię obserwować, bo ludzie tak nie działają. Możemy powiedzieć, że nie zobaczysz fal strat, jakie powodują fałszywe konta, a panel dzień po dniu pokazuje nowych obserwujących z naszej kampanii, więc zawsze wiesz, co przyszło od nas.",
                ],
            },
        ],
        "faqs": [
            ("Czy Wasi obserwujący są na stałe?", "To prawdziwi ludzie, więc zostają tak długo, jak chcą. Nikt nie może obiecać, że człowiek nigdy nie przestanie obserwować; możemy powiedzieć, że żaden z nich nie jest fałszywym kontem czekającym na usunięcie."),
            ("Czy uzupełniacie obserwujących, jeśli ubędą?", "Nie, bo nie ma czego uzupełniać. Uzupełnienia istnieją dla obserwujących, którzy znikają w czystkach. Nasi to ludzie, a pojedyncze odobserwowanie to część każdej prawdziwej publiczności."),
            ("Dlaczego kupieni obserwujący znikają?", "Zwykle wcale nie przestają obserwować: to konta zostają usunięte. Instagram kasuje fałszywe i spamerskie profile falami, a liczba obserwujących spada razem z nimi."),
            ("Co stanie się z moimi obserwującymi, gdy zrezygnuję?", "Zostaną. Obserwowali Cię, bo chcieli, a nie dlatego, że kazała im subskrypcja. Rezygnacja oznacza tylko, że po końcu opłaconego miesiąca przestajemy sprowadzać nowych ludzi; ci, których zdobyłeś, dalej Cię obserwują."),
            ("Jak zatrzymać obserwujących, których zdobywam?", "Publikuj regularnie, odpowiadaj na komentarze i daj nowym obserwującym powód do powrotu w ich pierwszych tygodniach. Ludzie zostają z tych samych powodów, dla których zaczęli obserwować."),
        ],
    },
    {
        "service": "followers",
        "modifier": "organic",
        "slug": "instagram/obserwujacy/organiczni",
        "label": "Organiczni obserwujący na Instagramie",
        "title": "Kup organicznych obserwujących na Instagramie | Growsterr",
        "description": "Czy można kupić organicznych obserwujących na Instagramie? Możesz zapłacić za to, by codziennie widzieli Cię prawdziwi ludzie. Obserwowanie zostaje ich decyzją.",
        "h1": ("Kupić organicznych obserwujących na Instagramie? ", "Zapłać za zasięg, ludzie wybiorą."),
        "intro": "Ściśle mówiąc, nikt nie może kupić organicznych obserwujących na Instagramie: obserwowanie jest organiczne, bo wybrał je człowiek. Kupić możesz zasięg. Każdego dnia prawdziwi ludzie w wybranym przez Ciebie miejscu trafiają na Twój profil dzięki naszym kampaniom, a każde obserwowanie, które z tego wynika, to czyjaś samodzielna decyzja.",
        "hero": {"image": "instagram-real-people", "alt": "Ludzie trafiają na profil twórcy na Instagramie i decydują się go obserwować"},
        "sections": [
            {
                "h2": "Gdzie kończy się płatne, a zaczyna organiczne",
                "p": [
                    "Nasze kampanie są promowane: płacimy, żeby pokazać Twój profil ludziom w naszej sieci partnerskiej. Ta część jest płatna i mówimy to wprost. Wszystko, co dzieje się dalej, już nie. Nikt nie jest proszony o obserwowanie i nikt nie obserwuje w ramach wymiany.",
                    "To ten sam układ co reklama albo wzmianka na czyimś profilu: płacisz za przedstawienie, a publiczność decyduje.",
                ],
            },
            {
                "h2": "Organiczni obserwujący z Twojej okolicy",
                "p": [
                    "Organiczny wzrost działa najlepiej, gdy widzą Cię ludzie, których to może obchodzić. Podaj miasto, region lub kraj, w którym mieszka Twoja publiczność, a tam pokażemy Twój profil najpierw. Piekarnia w Poznaniu i twórca podróżniczy z odbiorcami w całej Europie potrzebują innych ludzi, więc celujemy odpowiednio.",
                ],
            },
            {
                "h2": "Czego organiczny wzrost nie obejmuje",
                "ul": [
                    "Wymian follow za follow i grup zaangażowania.",
                    "Botów i fałszywych profili, nieważne jak powoli wypuszczanych.",
                    "Jakiegokolwiek logowania: hasło zostaje u Ciebie.",
                    "Wysypów obserwujących szybszych, niż zdołałaby jakakolwiek prawdziwa publiczność.",
                ],
            },
        ],
        "faqs": [
            ("Czy płatne kampanie to naprawdę wzrost organiczny?", "Zasięg jest płatny, obserwowanie nie. Każdy nowy obserwujący zobaczył Twój profil i zdecydował sam, a właśnie to czyni obserwującego organicznym."),
            ("Czy będę codziennie zdobywać prawdziwych obserwujących?", "Tak. Kampania działa każdego dnia miesiąca, a ludzie zaczynają Cię obserwować, gdy Cię odkrywają. Jedne dni przynoszą więcej niż inne; w skali miesiąca to zwykle {pick_audience} z pakietem {pick_name}."),
            ("Czy to to samo co samodzielne reklamy na Instagramie?", "Podobne w duchu, inne w praktyce. Kampanie prowadzimy w naszej sieci partnerskiej, opiekuje się nimi nasz zespół, a Ty widzisz w panelu zmierzone wizyty i nowych obserwujących. Nie potrzebujesz konta reklamowego ani budżetu do pilnowania."),
            ("Czy organiczny wzrost pomaga postom docierać dalej?", "Bardziej, niż kiedykolwiek mogłyby kupione liczby, bo organiczni obserwujący naprawdę widzą Twoje posty i na nie reagują. To, jak daleko zajdzie pojedynczy post, wciąż zależy od samego posta."),
            ("Czy organiczny wzrost jest wolniejszy?", "Jest równiejszy. Miesiąc organicznego wzrostu przychodzi dzień po dniu zamiast w godzinę i nie kończy się spadkiem, który przynoszą wysypy botów."),
        ],
    },
    {
        "service": "followers",
        "modifier": "private-account",
        "slug": "instagram/obserwujacy/konto-prywatne",
        "label": "Obserwujący na prywatne konto na Instagramie",
        "title": "Obserwujący na prywatnym koncie na Instagramie | Growsterr",
        "description": "Czy można kupić obserwujących na prywatne konto na Instagramie? Ludzie mogą tam tylko wysłać prośbę, więc na czas kampanii prosimy o profil publiczny.",
        "h1": ("Obserwujący na prywatnym koncie na Instagramie? ", "Na czas wzrostu przejdź na publiczne."),
        "intro": "Jeśli chcesz kupić lub zdobyć obserwujących na prywatne konto na Instagramie, oto uczciwy haczyk: prywatnego konta nie da się po prostu zaobserwować, można tylko o to poprosić. Dlatego prosimy, by na czas kampanii profil był publiczny. Nadal sam decydujesz, co na nim jest, a my nigdy nie potrzebujemy Twojego hasła.",
        "hero": {"image": "instagram-followers", "alt": "Prywatny profil na Instagramie z kłódką obok tego samego profilu ustawionego jako publiczny"},
        "sections": [
            {
                "h2": "Co prywatne konto robi z kampanią",
                "p": [
                    "Gdy ktoś trafia na prywatny profil, widzi nazwę, bio i kłódkę. Może poprosić o możliwość obserwowania, ale nie zobaczy ani jednego posta, więc większość ludzi idzie dalej. Tych kilku, którzy wyślą prośbę, czeka potem, aż zatwierdzisz ich po kolei.",
                    "Kampania, która prowadzi ludzi pod zamknięte drzwi, marnuje większość swojego zasięgu. Na publicznym profilu ci sami ludzie mogą przejrzeć Twoje posty, wyrobić sobie zdanie i od razu zacząć obserwować.",
                ],
            },
            {
                "h2": "Jeśli serwis mówi, że prywatne konto to żaden problem",
                "p": [
                    "Liczba obserwujących na prywatnym koncie może rosnąć tylko wtedy, gdy prośby są zatwierdzane. Jeśli ktoś obiecuje tam obserwujących bez Twojego zatwierdzania, musiałby zatwierdzać sam, z wnętrza Twojego konta. Oddanie mu do tego hasła to jedyna rzecz, której nie powinieneś robić nigdy.",
                ],
            },
            {
                "h2": "Konto publiczne bez utraty kontroli",
                "ul": [
                    "Przełącz konto na publiczne na czas kampanii i wróć do prywatnego, kiedy chcesz.",
                    "Zarchiwizuj posty, które wolisz zachować dla siebie; nic nie zostaje usunięte.",
                    "Osobiste relacje udostępniaj Bliskim znajomym zamiast wszystkim.",
                    "Każdy, kto zacznie Cię obserwować, gdy konto jest publiczne, zostaje obserwującym także po powrocie do prywatnego.",
                ],
            },
        ],
        "faqs": [
            ("Czy rozwijacie prywatne konta na Instagramie?", "Tylko odrobinę, więc nawet nie próbujemy. Ludzie mogą poprosić o obserwowanie, ale nie widzą Twoich postów, więc mało kto to robi. Utrzymaj konto publiczne na czas kampanii, a ona zrobi swoje."),
            ("Czy stracę obserwujących, gdy wrócę do prywatnego konta?", "Nie. Ludzie, którzy już Cię obserwują, zostają po przełączeniu na prywatne. Nowi odwiedzający musieliby wysyłać prośby, więc wzrost zwalnia, dopóki konto jest prywatne."),
            ("Czy muszę zatwierdzać prośby o obserwowanie?", "Nie, dopóki konto jest publiczne: ludzie obserwują bezpośrednio. Jeśli w połowie miesiąca przełączysz się na prywatne, nowe prośby czekają na Ciebie, a kampania przynosi dużo mniej obserwujących."),
            ("Czy potrzebujecie dostępu do konta, żeby je rozwijać?", "Nie. Dane logowania zostają u Ciebie; potrzebujemy tylko nazwy użytkownika i publicznego profilu, który ludzie od nas mogą obejrzeć."),
            ("Czy polubienia działają na prywatnym koncie?", "Tylko od osób, które już Cię obserwują, bo nikt inny nie widzi postów. To kolejny powód, dla którego kampania potrzebuje publicznego profilu."),
        ],
    },
    {
        "service": "followers",
        "modifier": "real",
        "slug": "instagram/obserwujacy/aktywni",
        "label": "Aktywni obserwujący na Instagramie",
        "title": "Aktywni obserwujący na Instagramie, którzy reagują | Growsterr",
        "description": "Aktywni obserwujący na Instagramie to ludzie, którzy lajkują, komentują i oglądają. U nas polubienia dają te same osoby: zwykle {pick_likes} miesięcznie.",
        "h1": ("Kup aktywnych obserwujących na Instagramie, ", "którzy naprawdę reagują."),
        "intro": "Gdy ktoś chce kupić aktywnych obserwujących na Instagramie, ma na myśli ludzi, którzy lajkują, komentują i oglądają, a nie liczbę, która stoi w miejscu. To możliwe tylko z prawdziwymi ludźmi, więc tylko takich sprowadzamy: osoby, które odkrywają Twój profil, decydują się obserwować i reagują na posty, które im się podobają.",
        "hero": {"image": "instagram-real-people", "alt": "Nowi obserwujący na Instagramie lajkują post i zaczynają rozmowę w komentarzach"},
        "sections": [
            {
                "h2": "Wyglądać na prawdziwego a być prawdziwym",
                "p": [
                    "Niektórzy obserwujący są zrobieni tak, żeby wyglądać na prawdziwych: pożyczone zdjęcie, kilka postów, wiarygodne imię. Przechodzą szybki rzut oka i oblewają całą resztę. Nigdy nie polubią Twojego nowego posta, nie obejrzą rolki do końca, nie zadadzą pytania w komentarzu.",
                    "Wysoka jakość w jedynym sensie, który ma znaczenie, oznacza człowieka, który mógłby to wszystko zrobić. Zdjęcia profilowe i bio to kosmetyka; sprawdzianem są interakcje.",
                ],
            },
            {
                "h2": "Aktywność przychodzi razem z obserwującymi",
                "p": [
                    "Ponieważ nasi obserwujący to ludzie, aktywność przychodzi razem z nimi, z tych samych kont. Z pakietem {pick_name} typowy miesiąc to {pick_audience} nowych obserwujących, a do tego {pick_likes} polubień i {pick_comments} komentarzy.",
                ],
            },
            {
                "h2": "Jak sprawdzić, czy obserwujący są aktywni",
                "ul": [
                    "Porównaj polubienia z liczbą obserwujących pod kilkoma ostatnimi postami: prawdziwy wzrost rusza jedno i drugie.",
                    "Czytaj komentarze: prawdziwe odnoszą się do posta, te od botów pasowałyby pod cokolwiek.",
                    "Otwórz kilka profili nowych obserwujących: u prawdziwych ludzi są nierówne i konkretne.",
                    "Obserwuj sumę przez kilka tygodni: aktywni obserwujący nie znikają falami.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "Twórca porównuje polubienia i komentarze pod ostatnimi postami na Instagramie"},
            },
        ],
        "faqs": [
            ("Co sprawia, że obserwujący jest aktywny?", "To człowiek, który widzi Twoje posty i czasem reaguje: polubieniem, komentarzem, obejrzaną rolką, udostępnieniem. Nikt nie reaguje na każdy post i to jest normalne."),
            ("Czy nowi obserwujący będą lajkować moje posty?", "Wielu tak. Polubienia pochodzą od tych samych ludzi, którzy obserwują, i z pakietem {pick_name} zwykle składają się na {pick_likes} miesięcznie. Ludzie lajkują to, co im się podoba, więc najwięcej zbierają Twoje najlepsze posty."),
            ("Czy to obserwujący dobrej jakości?", "To ludzie, którzy zdecydowali się Cię obserwować, z miejsca, które wskazałeś. Nie oceniamy obserwujących po tym, jak dopracowane mają profile; zależy nam na tym, żeby za każdym stał ktoś prawdziwy."),
            ("Czy obserwujący wyglądają na prawdziwych?", "Są prawdziwi, więc wyglądają jak zwykli użytkownicy Instagrama: mają własne zdjęcia, znajomych i nawyki. Jedne profile są bardzo aktywne, inne ciche, jak w każdej publiczności."),
            ("Czy Growsterr to prawdziwa firma, czy pośrednik?", "Jesteśmy agencją wzrostu, częścią Sterr Agency (Sterr Technologies OÜ, Tallinn, Estonia), a każdą kampanię prowadzi zespół. Sprowadzamy ludzi na Twój profil; nie odsprzedajemy zapasów obserwujących."),
        ],
    },
    {
        "service": "followers",
        "modifier": "safe",
        "slug": "instagram/obserwujacy/bezpiecznie",
        "label": "Bezpieczni obserwujący na Instagramie",
        "title": "Gdzie bezpiecznie kupić obserwujących na Instagramie | Growsterr",
        "description": "Szukasz sprawdzonej strony, żeby kupić obserwujących na Instagramie? Kim jesteśmy, jak płacisz, o co nigdy nie prosimy i co sprawdzić w każdym serwisie wzrostu.",
        "h1": ("Kup obserwujących na Instagramie na pewnej stronie: ", "jak to rozpoznać."),
        "intro": "Zanim kupisz obserwujących na Instagramie na stronie, która nazywa się sprawdzoną, warto zapytać, kto za nią stoi i co może pójść nie tak. Oto nasza strona, wprost: kim jesteśmy, jak działają płatności, co robimy z Twoim kontem (nic) i co sprawdzilibyśmy w każdym serwisie wzrostu, łącznie z nami.",
        "hero": {"image": "instagram-hub", "alt": "Twórca z Instagrama sprawdza dane serwisu wzrostu przed rejestracją"},
        "sections": [
            {
                "h2": "Komu płacisz",
                "p": [
                    "Growsterr to produkt Sterr Agency, prowadzony przez Sterr Technologies OÜ, spółkę zarejestrowaną w Tallinnie w Estonii, z siedzibą główną w Turcji. Płacisz kartą przez kasę Stripe albo przez Apple Pay lub Google Pay, jeśli Twoje urządzenie je obsługuje, a dane karty trafiają do Stripe, nie do nas.",
                    "To miesięczna subskrypcja. Możesz ją sam anulować, kiedy chcesz, a kampania trwa do końca opłaconego miesiąca.",
                ],
            },
            {
                "h2": "Co robimy z Twoim kontem: nic",
                "p": [
                    "Nigdy się nie logujemy, nic nie publikujemy, nikogo nie obserwujemy w Twoim imieniu i nie ruszamy żadnych ustawień. Kampania dzieje się poza Twoim kontem: ludzie widzą Twój profil w naszej sieci partnerskiej i odwiedzają go tak, jak odwiedziliby każdy polecony im profil.",
                ],
            },
            {
                "h2": "Pięć rzeczy do sprawdzenia w każdym serwisie wzrostu",
                "ul": [
                    "Czy prosi o hasło? Uczciwy serwis nigdy go nie potrzebuje.",
                    "Czy obiecuje tysiące obserwujących w kilka minut? Takie tempo dają tylko boty.",
                    "Czy liczby to zakresy, czy obietnice? Ludzi nie da się policzyć z góry.",
                    "Czy możesz zrezygnować sam, bez pisania do kogokolwiek?",
                    "Czy za stroną stoi nazwa firmy i kraj?",
                ],
            },
        ],
        "faqs": [
            ("Czy Growsterr to uczciwy serwis?", "Tak. Jesteśmy zarejestrowaną firmą, płatności idą wyłącznie przez Stripe, a każdą kampanię prowadzi zespół i mierzy ją w Twoim panelu. Możesz zrezygnować w dowolnym momencie na swoim koncie."),
            ("Czy to bezpieczne dla mojego konta na Instagramie?", "Nie wypowiadamy się za Instagram i nikt uczciwy nie obieca, jak potraktuje on konto. Możemy powiedzieć, że nie robimy rzeczy, które narażają konta: żadnego logowania, żadnych botów, żadnych wysypów obserwujących."),
            ("Czego od mnie potrzebujecie?", "Nazwy użytkownika na Instagramie, miejsca, z którego mają pochodzić nowi obserwujący, i publicznego profilu. To cała lista."),
            ("Czy mogę ufać liczbom, które pokazujecie?", "Są zmierzone, a nie szacowane: panel pokazuje dzień po dniu wizyty z naszej kampanii i nowych obserwujących wśród nich. Przed zamówieniem podajemy typowe zakresy, nigdy obietnice, bo ludzie decydują sami."),
            ("Czy zapłacę coś po rezygnacji?", "Nie. Rezygnacja zatrzymuje odnawianie subskrypcji. Opłacony miesiąc zostaje Twój, a po nim nic nie jest pobierane."),
        ],
    },
    {
        "service": "followers",
        "modifier": "targeted",
        "slug": "instagram/obserwujacy/lokalni",
        "label": "Lokalni obserwujący na Instagramie",
        "title": "Lokalni obserwujący na Instagramie z Twojego miasta | Growsterr",
        "description": "Kup lokalnych obserwujących na Instagramie z miasta, regionu lub kraju, który wskażesz: prawdziwych ludzi, którzy mieszkają tam, gdzie Twoi klienci, codziennie.",
        "h1": ("Kup lokalnych obserwujących na Instagramie ", "z miejsca, które wskażesz."),
        "intro": "Kawiarnia w Krakowie niewiele zyska na obserwujących z drugiego końca świata. Gdy kupujesz lokalnych obserwujących na Instagramie, miejsce jest najważniejsze, więc pytamy o nie na początku: z jakiego miasta, regionu lub kraju mają pochodzić nowi obserwujący? Potem kierujemy kampanię do ludzi, którzy tam mieszkają.",
        "hero": {"image": "instagram-followers", "alt": "Nowi obserwujący z tego samego miasta pojawiają się na profilu lokalnej firmy na Instagramie"},
        "sections": [
            {
                "h2": "Dlaczego lokalność znaczy więcej niż suma",
                "p": [
                    "Dla sklepu, studia, restauracji albo twórcy, który spotyka się z ludźmi na żywo, obserwujący, który może Cię odwiedzić, jest wart kilku, którzy nie mogą. Lokalni obserwujący mogą wejść do środka, polecić Cię znajomym i rozpoznać ulicę, na której nagrywałeś.",
                    "To także trzyma Twoją publiczność w spójności. Gdy większość obserwujących łączy miejsce i język, więcej z nich rozumie każdy post.",
                ],
            },
            {
                "h2": "Jak działa kierowanie na miejsce",
                "ul": [
                    "Przy zamówieniu podajesz miasto, region albo cały kraj.",
                    "Najpierw pokazujemy Twój profil ludziom właśnie tam, każdego dnia miesiąca.",
                    "Jeśli dopasowana publiczność jest tam mała, część obserwujących może przyjść z okolicy, a nie z jakiegoś przypadkowego miejsca.",
                    "Resztę robią Twoje treści: ludzie obserwują, gdy Twoje posty do nich przemawiają.",
                ],
            },
            {
                "h2": "Obserwujący z kraju, w którym działasz",
                "p": [
                    "Obserwujący z kraju, dla którego nigdy nic nie publikujesz, w niczym Ci nie pomogą, nieważne, jaki to kraj. Jeśli Twoi klienci są w Polsce, szukamy ludzi w Polsce; jeśli tylko we Wrocławiu, powiedz to, a zaczniemy od Wrocławia.",
                ],
            },
        ],
        "faqs": [
            ("Czy mogę wybrać miasto, a nie tylko kraj?", "Tak. Miasto, region albo cały kraj, wszystko działa. Miasto daje najbardziej skupioną publiczność; region lub kraj dają kampanii więcej ludzi do dotarcia."),
            ("Czy mogę uniknąć obserwujących z Indii albo innego kraju, w którym nie działam?", "Tak. Ty wybierasz, skąd pochodzą Twoi obserwujący, a my kierujemy kampanię właśnie tam. Z obserwującymi z żadnego kraju nie ma nic złego; pytanie brzmi, czy to Twoja publiczność. Jeśli Twoi klienci są w Niemczech, szukamy ludzi w Niemczech."),
            ("Czy każdy obserwujący będzie z mojego miasta?", "Najpierw pokazujemy Twój profil właśnie tam. Gdy dobrze dopasowana publiczność jest większa w okolicy, część obserwujących może przyjść stamtąd, więc myśl o tym jak o celowaniu w Twoje miasto, a nie o ogrodzeniu go."),
            ("Czy kierowanie lokalne kosztuje dodatkowo?", "Nie. Ma je każdy pakiet, od {starter_name} za {starter_price} miesięcznie."),
            ("Czy mogę kierować według wieku albo zainteresowań?", "Kierujemy wyłącznie według miejsca. W jego obrębie to Twoje treści decydują, kto obserwuje, bo ludzie obserwują to, co ich interesuje."),
            ("Czy kierowanie lokalne pasuje do biznesu online?", "Tak, jeśli Twoja publiczność mieszka w konkretnym miejscu: obszarze językowym, kraju, rynku, na który wchodzisz. Jeśli Twoi kupujący są rozsiani po całym kraju, wskaż kraj."),
        ],
    },
    {
        "service": "followers",
        "modifier": "viral",
        "slug": "instagram/obserwujacy/viral",
        "label": "Obserwujący na Instagramie a viral",
        "title": "Viral na Instagramie: co dają obserwujący | Growsterr",
        "description": "Czy można kupić obserwujących na Instagramie, żeby zrobić viral? Viralu nikt nie obieca. Prawdziwi obserwujący dają postom więcej osób, które je udostępnią.",
        "h1": ("Obserwujący na Instagramie, żeby zrobić viral? ", "Zdobądź ludzi, którzy udostępniają."),
        "intro": "Nikt nie sprzeda Ci viralowego posta, cokolwiek napisano na jego stronie. Post rozchodzi się dzięki ludziom: oglądają, wysyłają go znajomym, zapisują, a Instagram pokazuje go kolejnym podobnym osobom. Jeśli viral to powód, dla którego chcesz kupić obserwujących na Instagramie, kup tę część, która może pomóc: więcej prawdziwych ludzi, którzy pierwsi zobaczą Twój kolejny post.",
        "hero": {"image": "instagram-followers-1000", "alt": "Linia obserwujących twórcy podskakuje po popularnej rolce, a potem się utrzymuje"},
        "sections": [
            {
                "h2": "Dlaczego duża liczba nie sprawia, że post się rozchodzi",
                "p": [
                    "Post idzie dalej, gdy reagują na niego ludzie, którzy widzą go pierwsi. Tysiące obserwujących, którzy nigdy nie reagują, dają mu gorszy start niż kilkuset, którzy reagują, bo Instagram widzi post zignorowany przez swoją pierwszą publiczność.",
                ],
            },
            {
                "h2": "Co prawdziwi obserwujący dają viralowemu momentowi",
                "ul": [
                    "Więcej pierwszych widzów każdego posta: to oni decydują, czy pójdzie dalej.",
                    "Udostępnienia i zapisania, które mogą dać tylko ludzie.",
                    "Profil wart obserwowania, gdy post naprawdę wystrzeli, więc po tym momencie coś zostaje.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Ludzie wysyłają post twórcy z Instagrama znajomym w wiadomościach"},
            },
            {
                "h2": "Uczciwe szanse",
                "p": [
                    "Większość postów nie staje się viralem, ani naszych, ani niczyich. Stały wzrost sprawia, że posty, które mogą wystrzelić, robią to częściej, a te, które nie wystrzelą, i tak są warte publikacji. Taki układ proponujemy: żadnej obietnicy konkretnego momentu, za to lepsza pozycja startowa dla każdego posta.",
                ],
            },
        ],
        "faqs": [
            ("Czy możecie sprawić, że mój post stanie się viralem?", "Nie, i uważaj na każdego, kto twierdzi, że może. Viral zależy od posta, momentu i wyborów tysięcy ludzi. My możemy codziennie sprowadzać na Twój profil nowych, prawdziwych widzów, co daje każdemu postowi lepszy start."),
            ("Czy viralowe posty przynoszą obserwujących?", "Często, jeśli profil za postem daje ludziom powód, by zostać. Dlatego rozwijamy profil, a nie pojedynczy post: gdy coś wystrzeli, nowi znajdują aktywną publiczność i dorobek, który warto przejrzeć."),
            ("Czy kupowanie obserwujących pomaga algorytmowi?", "Kupione boty działają tu przeciwko Tobie, bo każdy post wygląda przez nie na zignorowany. Prawdziwi obserwujący, którzy reagują, pomagają każdemu postowi lepiej wystartować. Ani jedno, ani drugie nie jest przełącznikiem."),
            ("Który pakiet pasuje do posta, który może wystrzelić?", "{rising_name} lub {pro_name}. Oba pozwalają wskazać posty, które mają dostać więcej uwagi, więc ten, w który wierzysz, zobaczy więcej prawdziwych ludzi. {pro_name} dodaje priorytetowe miejsce."),
            ("Kiedy zauważę różnicę?", "Kampania rusza szybko, a nowi obserwujący przychodzą od pierwszych dni. To, czy post wystrzeli, nigdy nie ma terminu; Twój wzrost ma."),
        ],
    },
    # --- Likes ----------------------------------------------------------------------------
    {
        "service": "likes",
        "slug": "instagram/polubienia",
        "label": "Polubienia na Instagramie",
        "title": "Polubienia na Instagramie od prawdziwych ludzi | Growsterr",
        "description": "Polubienia na Instagramie od ludzi, którzy zobaczyli Twój post i im się spodobał, w każdym miesięcznym pakiecie: zwykle {starter_likes} w pakiecie {starter_name}.",
        "h1": ("Polubienia na Instagramie ", "od ludzi, którym post się spodobał."),
        "intro": "Chcesz kupić polubienia na Instagramie pod swoje posty? U nas nigdy nie są sprzedawane osobno. Każdy pakiet sprowadza na Twój profil prawdziwych ludzi, a oni lajkują posty, które im się podobają: {starter_name} zwykle daje {starter_likes} polubień miesięcznie, {pick_name} {pick_likes}, razem z nowymi obserwującymi i komentarzami.",
        "hero": {"image": "instagram-hub", "alt": "Polubienia od prawdziwych ludzi zbierają się na siatce postów na Instagramie"},
        "sections": [
            {
                "h2": "Polubienie to dopiero początek",
                "p": [
                    "Na Instagramie polubienie to często pierwsza z kilku rzeczy, które ktoś robi: otwiera Twój profil, przegląda kilka kolejnych postów, zaczyna obserwować, wraca za tydzień. Polubienia kupione osobno kończą się na pierwszym kroku, a post z mnóstwem polubień i niczym więcej wokół dokładnie tak wygląda.",
                    "Nasze pochodzą od ludzi, którzy są na tej drodze. Dlatego przychodzą razem z obserwowaniami i komentarzami, a nie same.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Osoba lajkuje post na Instagramie, a potem otwiera profil twórcy"},
            },
            {
                "h2": "Polubienia pod postami, które wybierzesz",
                "p": [
                    "W pakiecie {starter_name} polubienia trafiają tam, gdzie ludziom najbardziej się podoba, zwykle pod najnowsze posty. {rising_name} i {pro_name} pozwalają wybrać, które posty dostają uwagę: przydaje się to przy premierze, współpracy albo poście, który chcesz pokazać.",
                ],
            },
            {
                "h2": "Gdzie kupić polubienia na Instagramie w 2026 roku",
                "ul": [
                    "Bez aplikacji do instalowania i bez logowania: strona, która chce jednego lub drugiego, prosi o niewłaściwy rodzaj dostępu.",
                    "Polubienia, które przychodzą z wyświetleniami i obserwowaniami, a nie przed nimi.",
                    "Typowe zakresy zamiast dokładnych liczb, bo decydują ludzie.",
                    "Firma, którą da się nazwać, i kasa, którą znasz: u nas to Sterr Technologies OÜ, a karty obsługuje Stripe.",
                ],
            },
        ],
        "faqs": [
            ("Czy mogę kupić polubienia pod jeden post?", "Nie jako jednorazowe zamówienie. Polubienia są w miesięcznym pakiecie i pochodzą od ludzi, którzy odkrywają Twój profil. Z pakietem {rising_name} lub {pro_name} możesz skierować tę uwagę na wybrane posty."),
            ("Czy jest aplikacja do polubień na Instagramie?", "Nie mamy żadnej i nie potrzebujesz jej. Zamawiasz na stronie, płacisz przez Stripe i śledzisz kampanię na swoim koncie z dowolnego urządzenia. Nigdy nie potrzebujemy Twoich danych logowania do Instagrama."),
            ("Ile polubień daje każdy pakiet?", "Zwykle {starter_likes} miesięcznie w pakiecie {starter_name}, {rising_likes} w {rising_name} i {pro_likes} w {pro_name}. To zakresy, nie liczby: każde polubienie to czyjś wybór."),
            ("Kiedy zaczynają się polubienia?", "Gdy tylko kampania działa i pierwsi ludzie trafiają na Twój profil, zwykle w pierwszych dniach. Przychodzą dalej przez cały miesiąc, nigdy jednym wysypem."),
            ("Czy polubienia wciąż się liczą, skoro można ukryć ich liczbę?", "Instagram pozwala ukrywać liczbę polubień, więc liczba na ekranie znaczy mniej niż kiedyś. Wciąż liczy się to, że ludzie reagują na Twoje posty, a właśnie to odzwierciedlają prawdziwe polubienia."),
        ],
    },
    {
        "service": "likes",
        "modifier": "comment-likes",
        "slug": "instagram/polubienia/pod-komentarzami",
        "label": "Polubienia komentarzy na Instagramie",
        "title": "Polubienia komentarzy na Instagramie: co działa | Growsterr",
        "description": "Chcesz kupić polubienia pod komentarzami na Instagramie? Nie sprzedajemy ich. Ludzie, którzy trafiają na Twoje posty, czytają wątek i lajkują trafne odpowiedzi.",
        "h1": ("Polubienia komentarzy na Instagramie ", "dają ludzie, którzy czytają wątek."),
        "intro": "Ludzie kupują polubienia komentarzy na Instagramie z dwóch powodów: żeby wypchnąć swój komentarz wyżej pod cudzym postem albo żeby ich własna sekcja komentarzy wyglądała na bardziej ruchliwą. Nie sprzedajemy ani jednego, ani drugiego. Sprowadzamy na Twój profil prawdziwych ludzi, a ci, którzy czytają komentarze, sami lajkują odpowiedzi, z którymi się zgadzają.",
        "hero": {"image": "instagram-real-people", "alt": "Ruchliwy wątek komentarzy pod postem na Instagramie z polubieniami przy najlepszych odpowiedziach"},
        "sections": [
            {
                "h2": "Komentarze pod cudzymi postami",
                "p": [
                    "Mocno polubiony komentarz wysoko pod postem dużego konta może przysłać Ci odwiedzających, dlatego ludzie szukają polubień komentarzy. Nie prowadzimy kampanii pod cudzymi postami. Pracujemy na Twoim własnym profilu: pokazujemy go prawdziwym ludziom, a oni decydują, co tam zrobią.",
                ],
            },
            {
                "h2": "Polubienia komentarzy pod Twoimi postami",
                "p": [
                    "Pod Twoimi postami polubienia komentarzy pojawiają się naturalnie, gdy tylko zaczyna się rozmowa. Ludzie, którzy przychodzą dzięki kampanii, czytają komentarze, na niektóre odpowiadają i lajkują te, z którymi się zgadzają, także Twoje. Nie liczymy tych polubień i ich nie prognozujemy, bo nikt nie przewidzi, którą odpowiedź ktoś polubi.",
                    "Co liczymy: z pakietem {pick_name} miesiąc zwykle przynosi {pick_likes} polubień pod Twoimi postami i {pick_comments} komentarzy.",
                ],
            },
            {
                "h2": "Trzy sposoby na więcej polubień pod Twoimi odpowiedziami",
                "ul": [
                    "Odpowiadaj szybko na pierwsze komentarze, póki ludzie są jeszcze przy poście.",
                    "Odpowiadaj czymś, co warto przeczytać: wskazówką, szczegółem, pytaniem zwrotnym.",
                    "Przypnij komentarz, który zaczyna rozmowę, na jakiej Ci zależy.",
                ],
            },
        ],
        "faqs": [
            ("Czy sprzedajecie polubienia komentarzy na Instagramie?", "Nie. Polubienia komentarzy, jak każde inne polubienia, pochodzą tylko od ludzi, którzy sami chcą je dać. Nasze pakiety sprowadzają tych ludzi pod Twoje posty; co polubią w wątku, zależy od nich."),
            ("Czy możecie wypchnąć mój komentarz na górę pod postem innego konta?", "Nie. Rozwijamy wyłącznie Twój własny profil i nie wysyłamy polubień do komentarzy nigdzie indziej."),
            ("Czy w mojej sekcji komentarzy zrobi się ruchliwiej?", "Zwykle tak, bo więcej ludzi widzi Twoje posty. Z pakietem {pick_name} przychodzi zwykle {pick_comments} komentarzy miesięcznie, a komentarze przyciągają kolejne odpowiedzi i polubienia."),
            ("Czy polubienia komentarzy wliczają się w liczby pakietu?", "Nie. Nasze typowe zakresy liczą polubienia pod Twoimi postami. Polubienia pojedynczych komentarzy dochodzą do tego, gdy tylko ludzie je dają."),
            ("Czy zalogujecie się na moje konto?", "Nie. Nikt po naszej stronie nie dotyka Twojego konta, a Twoje hasło nigdy nie wychodzi poza Ciebie. Wszystko, co dzieje się pod Twoimi postami, robią ludzie, ze swoich własnych kont."),
        ],
    },
    {
        "service": "likes",
        "modifier": "gradual",
        "slug": "instagram/polubienia/stopniowo",
        "label": "Polubienia na Instagramie stopniowo",
        "title": "Polubienia na Instagramie stopniowo, przez wiele dni | Growsterr",
        "description": "Chcesz kupić polubienia na Instagramie powoli, bez nagłego skoku? Nasze dają prawdziwi ludzie, którzy znajdują Twoje posty przez cały miesiąc.",
        "h1": ("Polubienia na Instagramie stopniowo, ", "bo ludzie się nie spieszą."),
        "intro": "Jeśli chcesz kupić polubienia na Instagramie powoli, wiesz już, że setki polubień w dwie minuty wyglądają źle. Powoli to dobry kierunek, ale tempo to tylko połowa sprawy. Nasze polubienia przychodzą stopniowo, bo dają je prawdziwi ludzie, którzy znajdują Twoje posty przez dni i tygodnie, a nie kolejka ustawiona na minutnik.",
        "hero": {"image": "instagram-followers-1000", "alt": "Polubienia pod postem na Instagramie łagodnie przybywają przez kilka dni"},
        "sections": [
            {
                "h2": "Jak polubienia rosną pod prawdziwym postem",
                "p": [
                    "Post zbiera polubienia po krzywej: najpierw fala od ludzi, którzy widzą go wkrótce po publikacji, potem długi ogon, gdy ktoś znajduje go na Twoim profilu, przez hashtag albo w wiadomości od znajomego. Ten ogon może ciągnąć się tygodniami.",
                    "Nasze kampanie dokładają ludzi w każdym miejscu tej krzywej. Odwiedzają Twój profil przez cały miesiąc, przewijają posty i lajkują to, co im się podoba, więc polubienia zbierają także starsze posty, a nie tylko najnowszy.",
                ],
            },
            {
                "h2": "Dlaczego minutnik to nie to samo co czas",
                "p": [
                    "Wolno wypuszczane polubienia od botów rozwiązują nie ten problem. Skok znika, ale konta za polubieniami dalej nic nie oglądają, nie obserwują i nie komentują, a polubienia bez wyświetleń, obserwowań i komentarzy wyglądają równie dziwnie w wolnym tempie.",
                ],
            },
            {
                "h2": "Kiedy powoli to nie to, czego chcesz",
                "p": [
                    "Jeśli potrzebujesz ściany polubień pod postem w ciągu godziny, jesteśmy złym wyborem i wolimy powiedzieć to od razu. Jeśli chcesz, żeby każdy post zbierał polubienia od ludzi, których to obchodzi, właśnie do tego jesteśmy stworzeni.",
                ],
            },
        ],
        "faqs": [
            ("Jak wolno przychodzą polubienia?", "W tempie, w jakim ludzie znajdują Twoje posty: część w pierwszych dniach kampanii, więcej w kolejnych tygodniach. Nie ma minutnika ani paczek, więc żadne dwa dni nie wyglądają tak samo."),
            ("Czy mogę wybrać tempo polubień?", "Nie, i to celowe. Tempo wynika z ludzi odwiedzających Twój profil. Z pakietem {rising_name} lub {pro_name} możesz za to wybrać, które posty dostają uwagę."),
            ("Czy starsze posty też dostaną polubienia?", "Często tak. Ludzie, którzy odkrywają Twój profil, przewijają wstecz i lajkują to, co im się podoba, więc polubienia rozkładają się po całym feedzie, zamiast piętrzyć się pod jednym postem."),
            ("Czy powolne polubienia wyglądają naturalniej?", "Powoli wygląda naturalnie tylko wtedy, gdy stoją za tym ludzie. Nasze tak wyglądają, bo tak jest: za każdym polubieniem stoi osoba, która może też zacząć obserwować albo skomentować."),
            ("Ile polubień przychodzi w miesiąc?", "Z pakietem {pick_name} zwykle {pick_likes} w ciągu 30 dni. To zakres, a nie limit, bo ludzie lajkują we własnym tempie."),
        ],
    },
    {
        "service": "likes",
        "modifier": "monthly",
        "slug": "instagram/polubienia/co-miesiac",
        "label": "Polubienia na Instagramie co miesiąc",
        "title": "Polubienia na Instagramie co miesiąc, bez zamówień | Growsterr",
        "description": "Kup polubienia na Instagramie co miesiąc zamiast pod każdy post: jedna subskrypcja, prawdziwi ludzie, polubienia cały miesiąc. Anulujesz, kiedy chcesz.",
        "h1": ("Automatyczne polubienia na Instagramie co miesiąc, ", "od ludzi, nie ze skryptu."),
        "intro": "Jeśli chcesz kupić automatyczne polubienia na Instagramie na cały miesiąc, pewnie masz dość myślenia o polubieniach post po poście. Właśnie to załatwia pakiet. Subskrybujesz raz, my prowadzimy kampanię codziennie, a prawdziwi ludzie lajkują posty, które im się podobają, przez cały miesiąc: zwykle {pick_likes} polubień z pakietem {pick_name}. Odnawia się co miesiąc, dopóki nie zrezygnujesz.",
        "hero": {"image": "instagram-creator-studio", "alt": "Twórca planuje miesiąc postów na Instagram na ściennym kalendarzu"},
        "sections": [
            {
                "h2": "Automatyczne, ale nie zautomatyzowane",
                "p": [
                    "Autopolubienia to zwykle program, który wyłapuje każdy nowy post i w kilka minut wystrzeliwuje w niego ustaloną liczbę polubień. To automatyczne, a każde z tych polubień pochodzi z konta, z którego nikt nie korzysta.",
                    "Nasze są automatyczne w innym sensie: nie musisz nic robić przy żadnym poście. Kampania trwa, ludzie wciąż odkrywają Twój profil, a polubienia, które zostawiają, są ich własne.",
                ],
            },
            {
                "h2": "Co zmienia miesięczny pakiet",
                "ul": [
                    "Jedna cena na miesiąc, {pick_price} za {pick_name}, zamiast zamówienia pod każdy post.",
                    "Żadnych liczb do ustawiania i żadnych godzin do planowania.",
                    "Polubienia pod nowymi i starszymi postami, w miarę jak ludzie je znajdują.",
                    "Miesiąc polubień to miesiąc informacji zwrotnej: widzisz, które posty ludziom naprawdę się podobają.",
                    "Możesz przestać, kiedy chcesz, bez okresu wypowiedzenia.",
                ],
            },
        ],
        "faqs": [
            ("Czy nowe posty dostają polubienia automatycznie?", "Decydują ludzie, więc nie ma stałej liczby na post. Nowe posty to zwykle miejsce, od którego ludzie zaczynają, a z pakietem {rising_name} lub {pro_name} możesz wskazać, które posty mają dostać uwagę."),
            ("Czy subskrypcja odnawia się automatycznie?", "Tak. Stripe odnawia ją co miesiąc na wybranej przez Ciebie metodzie płatności. Rezygnacja zajmuje chwilę na Twoim koncie, a opłacony miesiąc i tak trwa do końca."),
            ("Ilu postów potrzebuję?", "Nie ma minimum, ale polubienia pochodzą od ludzi przeglądających Twój profil, więc kilka świeżych postów daje im coś, co może się spodobać. Publikowanie w trakcie miesiąca daje każdemu nowemu odwiedzającemu więcej do polubienia."),
            ("Czy mogę zmienić pakiet z miesiąca na miesiąc?", "Tak. Zacznij od pakietu, który pasuje dziś, i przejdź wyżej, gdy Twoje posty będą gotowe na więcej ludzi."),
            ("Czy to to samo co program do autopolubień?", "Nie. Program, który lajkuje każdy post według minutnika, korzysta z kont, za którymi nikt nie stoi. Nasze polubienia pochodzą od ludzi, którzy odwiedzili Twój profil i którym post się spodobał."),
        ],
    },
    {
        "service": "likes",
        "modifier": "no-drop",
        "slug": "instagram/polubienia/bez-spadkow",
        "label": "Polubienia na Instagramie, które zostają",
        "title": "Polubienia na Instagramie bez spadków, na stałe | Growsterr",
        "description": "Chcesz kupić polubienia na Instagramie, które nie znikają? Znikają, gdy konta za nimi są usuwane. Nasze dają prawdziwi ludzie, więc zostają.",
        "h1": ("Polubienia na Instagramie, które zostają, ", "bo dał je człowiek."),
        "intro": "Polubienia znikają głównie z jednego powodu: konta, które je dały, zostają usunięte. Jeśli chcesz kupić polubienia na Instagramie bez spadków, trwałe są tylko te od ludzi. Nasze takie są, więc polubienie pod Twoim postem zostaje, chyba że osoba, która je dała, zmieni zdanie.",
        "hero": {"image": "instagram-hub", "alt": "Post na Instagramie, którego polubienia trzymają się tygodnie po publikacji"},
        "sections": [
            {
                "h2": "Dokąd znikają polubienia",
                "p": [
                    "Polubienie należy do konta, które je dało. Gdy Instagram usuwa fałszywe lub spamerskie konta, każde polubienie, które zostawiły, znika razem z nimi, często kilka tygodni po zamówieniu. Post może stracić dużą część polubień z dnia na dzień, a każdy, kto widział go wcześniej, zauważy lukę.",
                ],
            },
            {
                "h2": "Dlaczego polubienia od ludzi się trzymają",
                "p": [
                    "Konta człowieka czystka nie zmiata. Jego polubienie zostaje pod Twoim postem tak długo, jak on tego chce, a ludzie rzadko wracają, żeby cofnąć polubienie czegoś, co im się podobało.",
                    "Prawdziwe polubienia także wciąż przybywają. Starsze posty zbierają nowe polubienia, gdy kolejni ludzie znajdują Twój profil, więc licznik posta może rosnąć długo po publikacji.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Nowi odwiedzający lajkują starszy post na Instagramie kilka tygodni po publikacji"},
            },
        ],
        "faqs": [
            ("Czy polubienia kiedyś spadną?", "Nie tak jak kupione. Każde polubienie pochodzi z czyjegoś własnego konta, więc znika tylko wtedy, gdy ta osoba je cofnie albo usunie konto, a to rzadkie i dzieje się pojedynczo."),
            ("Czy jest okres uzupełniania?", "Nie ma okresu uzupełniania, bo nie spodziewamy się spadku. Uzupełnienia naprawiają problem, którego nie tworzymy."),
            ("Czy polubienia pod rolkami też zostają?", "Tak. Polubienie zostaje pod każdym postem, zdjęciem, karuzelą czy rolką, dopóki istnieje konto, które je dało."),
            ("Jak sprawdzić, czy wcześniejsze polubienia były od botów?", "Szukaj nagłych spadków po czystce, polubień znacznie przewyższających wyświetlenia i lajkujących, których profile nie mają żadnych własnych postów. Polubienia od ludzi rzadko mają którąkolwiek z tych cech."),
            ("Ile polubień daje pakiet?", "{pick_name} zwykle daje {pick_likes} miesięcznie, rozłożonych na posty, które ludziom się podobają. Zostają, a polubienia z kolejnego miesiąca dochodzą do nich."),
        ],
    },
    {
        "service": "likes",
        "modifier": "organic",
        "slug": "instagram/polubienia/organiczne",
        "label": "Organiczne polubienia na Instagramie",
        "title": "Organiczne polubienia na Instagramie od ludzi | Growsterr",
        "description": "Kup organiczne polubienia na Instagramie i dostań szczerą informację zwrotną: prawdziwi ludzie widzą Twoje posty i lajkują tylko to, co im się podoba.",
        "h1": ("Organiczne polubienia na Instagramie ", "i to, co Ci mówią."),
        "intro": "Gdy kupujesz organiczne polubienia na Instagramie, dostajesz coś, czego kupione polubienia dać nie mogą: szczerą informację zwrotną. Nasze kampanie pokazują Twoje posty prawdziwym ludziom, a oni lajkują tylko to, co im się podoba. Niektóre posty zbiorą dużo więcej niż inne, a ta różnica mówi Ci, czego chce Twoja publiczność.",
        "hero": {"image": "instagram-real-people", "alt": "Ludzie różnie reagują na rząd postów na Instagramie, jedne lajkując bardziej niż inne"},
        "sections": [
            {
                "h2": "Nierówne polubienia to dobry znak",
                "p": [
                    "Kupione polubienia są podejrzanie równe: każdy post dostaje mniej więcej tyle samo, cokolwiek przedstawia. Organiczne się różnią. Mocna rolka wysuwa się na prowadzenie, spokojne zdjęcie zostaje w tyle, a cały obraz wygląda jak publiczność z własnym zdaniem, bo nią jest.",
                ],
            },
            {
                "h2": "Jak wykorzystać polubienia, żeby publikować lepiej",
                "ul": [
                    "Porównaj trzy najlepsze posty miesiąca: co mają wspólnego?",
                    "Zauważ, który format ludzie lajkują najczęściej: rolki, karuzele czy zdjęcia.",
                    "Publikuj więcej tego, co działa, i sprawdź, czy polubienia idą za tym.",
                    "Z pakietem {rising_name} lub {pro_name} skieruj dodatkową uwagę na post, który testuje nowy pomysł.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "Twórca sortuje posty z zeszłego miesiąca według liczby polubień"},
            },
            {
                "h2": "Jak organiczne polubienia trafiają pod Twoje posty",
                "p": [
                    "Pokazujemy Twój profil ludziom w naszej sieci partnerskiej, w wybranym przez Ciebie mieście, regionie lub kraju. Przeglądają go, obserwują, jeśli chcą, i lajkują posty, które ich zatrzymają. Nikt nie jest proszony o polubienie czegokolwiek.",
                ],
            },
        ],
        "faqs": [
            ("Czy płacenie za zasięg sprawia, że polubienia nie są organiczne?", "Nie. Płacenie za to, by Cię zobaczono, to zasada działania każdej reklamy i każdego promowanego posta. Samo polubienie to wciąż czyjaś własna reakcja na Twój post."),
            ("Czy każdy post dostanie polubienia?", "Większość postów, które ludziom się podobają, tak, ale nie po równo, i właśnie o to chodzi. Najwięcej zbierają zwykle Twoje najlepsze posty."),
            ("Ilu organicznych polubień mogę się spodziewać?", "Typowy miesiąc z pakietem {pick_name} to {pick_likes}. Suma to zakres; to, jak rozłoży się na posty, zależy od ludzi, którzy je zobaczą."),
            ("Czy organiczne polubienia przychodzą z obserwującymi?", "Tak. Ludzie, którzy lajkują Twoje posty, często też zaczynają obserwować: zwykle {pick_audience} nowych obserwujących miesięcznie z pakietem {pick_name}, a część zostawia komentarze."),
            ("Dlaczego to lepsze niż stała liczba na post?", "Bo stała liczba nic Ci nie mówi. Organiczne polubienia rosną i spadają z każdym postem, więc pokazują, co trafia, a co nie."),
        ],
    },
    {
        "service": "likes",
        "modifier": "private-account",
        "slug": "instagram/polubienia/konto-prywatne",
        "label": "Polubienia na prywatnym koncie na Instagramie",
        "title": "Polubienia na prywatne konto na Instagramie? | Growsterr",
        "description": "Czy można kupić polubienia na prywatne konto na Instagramie? Posty widzą tylko zatwierdzeni obserwujący, więc nikt nowy ich nie polubi. Oto co działa.",
        "h1": ("Polubienia na prywatnym koncie na Instagramie ", "mogą dać tylko obserwujący."),
        "intro": "Zanim kupisz polubienia na prywatne konto na Instagramie, poznaj ograniczenie: na prywatnym profilu posty widzą tylko zatwierdzeni obserwujący, więc tylko oni mogą je polubić. Każdy, kogo kampania sprowadzi na Twój profil, trafi na kłódkę. Dlatego na czas kampanii profil musi być publiczny, a prywatność tam, gdzie się liczy, da się zachować na kilka dobrych sposobów.",
        "hero": {"image": "instagram-hub", "alt": "Post na Instagramie, który mogą zobaczyć i polubić tylko zatwierdzeni obserwujący"},
        "sections": [
            {
                "h2": "Kto może polubić post na prywatnym koncie",
                "p": [
                    "Tylko osoby, które zatwierdziłeś. Wszyscy inni widzą Twoją nazwę, bio i liczbę obserwujących, ale ani jednego posta, więc nie mają czego lajkować. Serwis obiecujący tam polubienia musiałby najpierw doprowadzić do zatwierdzenia swoich kont jako Twoich obserwujących, przez Ciebie albo przez kogoś zalogowanego jako Ty.",
                ],
            },
            {
                "h2": "Prywatność w praktyce",
                "ul": [
                    "Prowadź drugie, publiczne konto do pracy, a osobiste zostaw prywatne.",
                    "Ukryj liczbę polubień pod dowolnym postem, jeśli wolisz, żeby nie była widoczna.",
                    "Wyłącz komentarze pod postami, którymi chcesz się podzielić bez rozmowy.",
                ],
            },
            {
                "h2": "Co się zmienia, gdy profil jest publiczny",
                "p": [
                    "Ludzie widzą Twoje posty i lajkują te, które im się podobają; z pakietem {pick_name} to zwykle {pick_likes} polubień w miesiąc, razem z nowymi obserwującymi i komentarzami. Nadal sam decydujesz, co publikujesz i z kim rozmawiasz.",
                ],
            },
        ],
        "faqs": [
            ("Czy osoby, które mnie nie obserwują, mogą polubić posty na prywatnym koncie?", "Nie. Instagram pokazuje posty prywatnego konta tylko zatwierdzonym obserwującym, więc nikt inny nie może ich polubić."),
            ("Czy po kampanii muszę zostać przy koncie publicznym?", "Nie, to Twój wybór, a polubienia, które już są pod postami, zostają. Gdy konto jest prywatne, nowi ludzie nie widzą jednak Twoich postów, więc trwająca kampania nie może przynieść polubień."),
            ("Czy mogę zamiast tego rozwijać osobne konto publiczne?", "Tak. Jedno konto publiczne do pracy i jedno prywatne dla znajomych to dobre rozwiązanie. Rozwijalibyśmy to publiczne."),
            ("Czy potrzebujecie dostępu, żeby zatwierdzać prośby?", "Nie. Hasło zostaje u Ciebie, a my nigdy nie logujemy się na Twoje konto. Na publicznym profilu nie ma czego zatwierdzać: ludzie obserwują i lajkują bezpośrednio."),
            ("Czy mogę ukryć liczbę polubień i dalej rosnąć?", "Tak. Ukrycie liczby zmienia tylko to, co widzą odwiedzający pod danym postem. Ludzie nadal mogą go polubić, a Ty nadal widzisz liczbę."),
        ],
    },
    {
        "service": "likes",
        "modifier": "real",
        "slug": "instagram/polubienia/prawdziwe",
        "label": "Prawdziwe polubienia na Instagramie",
        "title": "Prawdziwe polubienia na Instagramie, bez botów | Growsterr",
        "description": "Prawdziwe polubienia na Instagramie od ludzi z własnymi kontami, nigdy od botów. Przychodzą z obserwującymi i komentarzami od tych samych osób.",
        "h1": ("Prawdziwe polubienia na Instagramie, ", "każde od osoby, która tak myśli."),
        "intro": "Chcesz kupić prawdziwe polubienia na Instagramie? Prawdziwe polubienie daje ktoś, kto obejrzał Twój post i spodobało mu się to, co zobaczył. Tylko takie sprowadzamy. Każdy pakiet pokazuje Twój profil ludziom, a polubienia, które zostawiają, idą w parze z obserwowaniami, komentarzami i wyświetleniami z tych samych kont, więc Twoje zaangażowanie wygląda realnie, bo takie jest.",
        "hero": {"image": "instagram-real-people", "alt": "Różni ludzie, każdy z własnym profilem, lajkują ten sam post na Instagramie"},
        "sections": [
            {
                "h2": "Polubienia premium, jakościowe i prawdziwe",
                "p": [
                    "Wielu sprzedawców dzieli polubienia na poziomy: tanie z pustych kont, premium albo „wysokiej jakości” z kont ze zdjęciami i postami. Oba poziomy to to samo w innym przebraniu: konta, które lajkują na polecenie. Lepsze przebranie nie czyni polubienia prawdziwym.",
                    "Jakość polubienia oznacza jedno: człowiek zdecydował się je dać. Cała reszta to opakowanie.",
                ],
            },
            {
                "h2": "Prawdziwe polubienia, za którymi idzie więcej",
                "p": [
                    "Prawdziwe polubienie daje ktoś, kto może też zacząć obserwować, skomentować albo obejrzeć Twoją kolejną rolkę. Dlatego prawdziwe polubienia podnoszą resztę Twoich liczb, zamiast stać obok nich: to jeden krok w tym, co robi człowiek, a nie cała transakcja.",
                ],
            },
            {
                "h2": "Jak rozpoznać polubienia, które tylko wyglądają na prawdziwe",
                "ul": [
                    "Polubienia skaczą, a wyświetlenia, obserwowania i komentarze stoją w miejscu.",
                    "Lajkujący mają zdjęcia z banków zdjęć, mało postów i tysiące obserwowanych kont.",
                    "Setki polubień przychodzą w kilka minut po publikacji, a potem nic.",
                    "Kilka tygodni później licznik spada.",
                ],
            },
        ],
        "faqs": [
            ("Czy Wasze polubienia na Instagramie pochodzą z prawdziwych kont?", "Tak. Każde polubienie pochodzi z czyjegoś własnego konta: od osoby, która odkryła Twój profil dzięki naszej kampanii i której post się spodobał. Żadnych botów ani farm kont."),
            ("Czy sprzedajecie polubienia premium?", "Nie sprzedajemy polubień w poziomach ani osobno. Każde polubienie od nas pochodzi od człowieka, w ramach miesięcznego pakietu; najmniejszy, {starter_name}, zwykle daje {starter_likes} miesięcznie."),
            ("Czy prawdziwe polubienia zwiększą mój zasięg?", "Pomagają tak, jak potrafi tylko prawdziwe zaangażowanie, bo ludzie za nimi mogą też obserwować, komentować i udostępniać. To, gdzie trafi post, wciąż zależy od niego samego, więc nigdy nie obiecujemy zasięgu."),
            ("Dlaczego niektóre kupione polubienia wyglądają na prawdziwe?", "Bo są tak zrobione: zdjęcia profilowe, kilka postów, wiarygodne imiona. Patrz na to, co dzieje się wokół nich. Polubienia od ludzi przychodzą z wyświetleniami i obserwowaniami; przebrane przychodzą same."),
            ("Czy mogę dostać prawdziwe polubienia bez nowych obserwujących?", "Nie. Polubienia są częścią pakietu i pochodzą od ludzi, którzy znajdują Twój profil, a wielu z nich też zaczyna obserwować. Właśnie to sprawia, że polubienia wyglądają realnie."),
        ],
    },
    {
        "service": "likes",
        "modifier": "reels",
        "slug": "instagram/polubienia/rolki",
        "label": "Polubienia rolek na Instagramie",
        "title": "Polubienia pod rolki na Instagramie od widzów | Growsterr",
        "description": "Kup polubienia pod rolki na Instagramie uczciwie: ludzie oglądają Twoje filmy i lajkują te, które im się podobają, więc za każdym polubieniem stoi wyświetlenie.",
        "h1": ("Polubienia pod Twoimi rolkami ", "od ludzi, którzy naprawdę obejrzeli."),
        "intro": "Zanim kupisz polubienia pod rolki na Instagramie, warto wiedzieć, ile jest warte polubienie rolki, której nikt nie obejrzał: niewiele. Nasze polubienia pod rolkami dają prawdziwi ludzie, którzy odkryli Twój profil, obejrzeli Twoje filmy i polubili te, które ich zatrzymały, razem z nowymi obserwującymi i komentarzami.",
        "hero": {"image": "instagram-creator-studio", "alt": "Twórca montuje rolkę na Instagram na telefonie przy biurku"},
        "sections": [
            {
                "h2": "Przy rolce oglądanie jest przed lajkiem",
                "p": [
                    "Rolki żyją tym, co robią widzowie: czy oglądają do końca, odtwarzają ponownie, udostępniają, obserwują. Polubienie to jeden z tych sygnałów i znaczy najwięcej wtedy, gdy idzie za prawdziwym obejrzeniem.",
                    "Polubienia filmów kupowane osobno zwykle przychodzą bez pasujących odtworzeń. Rolkę z większą liczbą polubień niż wyświetleń łatwo wypatrzyć i nie świadczy to dobrze o tym, skąd je ma.",
                ],
            },
            {
                "h2": "Więcej osób widzi Twoje rolki",
                "ul": [
                    "Ludzie przeglądają Twój profil i oglądają rolki, które ich zatrzymają, nie tylko najnowsze.",
                    "{rising_name} i {pro_name} pozwalają pokazać konkretną rolkę większej liczbie osób.",
                    "Widzowie pochodzą z miejsca, które wybierzesz, więc Twój język i nawiązania trafiają.",
                ],
            },
            {
                "h2": "Niech pierwsze sekundy się liczą",
                "p": [
                    "Możemy sprowadzić ludzi do Twoich rolek; zatrzymanie ich to zadanie filmu. Wyraźny haczyk w pierwszej sekundzie czy dwóch, napisy dla oglądających bez dźwięku i zakończenie, które kusi, żeby obejrzeć jeszcze raz, pomagają zamienić wyświetlenie w polubienie.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Widzowie oglądają rolkę na Instagramie do końca i stukają w serce"},
            },
        ],
        "faqs": [
            ("Czy mogę skierować polubienia na konkretną rolkę?", "Tak, z pakietem {rising_name} lub {pro_name}: wybierasz, które posty i rolki dostają uwagę, a resztę robią ludzie. W pakiecie {starter_name} widzowie sami znajdują rolki, które im się podobają."),
            ("Czy polubienia rolek przychodzą z wyświetleniami?", "Tak. Ludzie oglądają, zanim polubią, więc za każdym polubieniem stoi wyświetlenie. Nie sprzedajemy ani nie liczymy wyświetleń osobno, bo każde to człowiek, który zdecydował się obejrzeć."),
            ("Czy dzięki temu moja rolka trafi do Eksploruj?", "Nikt nie może tego obiecać i my też tego nie robimy. Instagram decyduje, co trafia do Eksploruj i do feedu rolek. Widzowie, którzy oglądają i reagują, dają rolce uczciwy start; kupione polubienia bez wyświetleń dają jej dziwny."),
            ("Czy moje konto musi być publiczne?", "Tak, na czas kampanii. Osoby spoza Twoich obserwujących nie mogą oglądać rolek na prywatnym koncie, więc nie mogłyby ich też polubić."),
            ("Ile polubień dostaną moje rolki?", "Z pakietem {pick_name} zwykle {pick_likes} polubień miesięcznie pod postami i rolkami łącznie. Jak się rozłożą, zależy od tego, co ludziom podoba się najbardziej."),
        ],
    },
    {
        "service": "likes",
        "modifier": "safe",
        "slug": "instagram/polubienia/bezpiecznie",
        "label": "Bezpieczne polubienia na Instagramie",
        "title": "Bezpieczne polubienia na Instagramie: co je wyróżnia | Growsterr",
        "description": "Chcesz kupić polubienia na Instagramie bezpiecznie i uczciwie? Takie polubienie daje osoba, która widziała Twój post. Jak to rozpoznać i skąd je mamy.",
        "h1": ("Uczciwe polubienia na Instagramie ", "zaczynają się od człowieka i posta."),
        "intro": "Szukasz bezpiecznego sposobu, żeby kupić polubienia na Instagramie? Uczciwe polubienie ma dwie części: prawdziwego człowieka i post, który naprawdę zobaczył. Wszystko, co robimy, opiera się na obu. Pokazujemy Twój profil ludziom, a ci, którym podobają się Twoje posty, je lajkują, bez logowania, bez botów i bez polubień sprzedawanych osobno.",
        "hero": {"image": "instagram-hub", "alt": "Osoba przewija Instagram i zatrzymuje się, żeby polubić post, który jej się spodobał"},
        "sections": [
            {
                "h2": "Sygnały ostrzegawcze w każdej ofercie polubień",
                "ul": [
                    "Cena za tysiąc polubień: ludzi nie kupuje się na tysiące.",
                    "Realizacja w kilka minut albo obietnica dokładnych liczb.",
                    "Prośba o hasło albo logowanie przez aplikację.",
                    "Polubienia sprzedawane bez wyświetleń, obserwowań i komentarzy, które powinny im towarzyszyć.",
                ],
            },
            {
                "h2": "Dlaczego fałszywe polubienia nie są uczciwe, ktokolwiek je sprzedaje",
                "p": [
                    "Zasady Instagrama proszą, żeby nie zbierać polubień w sztuczny sposób, a polubienia z kont, które lajkują na polecenie, to dokładnie to. Nie powiemy, jak Instagram potraktuje jakiekolwiek konkretne konto, i nie będziemy zgadywać. Po prostu nie wnosimy na Twoje konto niczego sztucznego.",
                ],
            },
            {
                "h2": "Skąd biorą się nasze polubienia",
                "p": [
                    "Od ludzi, których nasze kampanie sprowadzają na Twój profil: użytkowników naszej sieci partnerskiej, w wybranym przez Ciebie miejscu, każdego dnia miesiąca. Lajkują to, co im się podoba, zwykle {pick_likes} polubień miesięcznie z pakietem {pick_name}, a wielu z nich także obserwuje i komentuje.",
                ],
            },
        ],
        "faqs": [
            ("Czy kupowanie polubień na Instagramie jest w porządku?", "Kupowanie polubień od kont, które lajkują na polecenie, jest sprzeczne z zasadami Instagrama dotyczącymi sztucznego zaangażowania. My sprzedajemy coś innego: zasięg do prawdziwych ludzi, którzy sami decydują, czy polubić."),
            ("Czy mogę stracić konto przez kupione polubienia?", "Nie wypowiadamy się za Instagram, a każdy, kto obiecuje konkretny wynik, zgaduje. Mamy wpływ na to, żeby każde polubienie od nas pochodziło od człowieka i żebyśmy nigdy nie dotykali Twoich danych logowania."),
            ("Jak płacę?", "Kartą, przez Apple Pay lub Google Pay, w bezpiecznej kasie Stripe. Płatność jest miesięczna i kończy się, gdy zrezygnujesz."),
            ("Czy prosicie o dane logowania do Instagrama?", "Nigdy. Do uruchomienia kampanii potrzebujemy nazwy użytkownika. Jeśli jakikolwiek serwis z polubieniami prosi o hasło, odejdź."),
            ("Dlaczego nie sprzedajecie polubień pod konkretny post?", "Bo ustalona liczba polubień pod ustalonym postem może pochodzić tylko z kont, które lajkują na polecenie. My sprowadzamy ludzi; polubienia to to, co robią, gdy post im się spodoba."),
        ],
    },
    {
        "service": "likes",
        "modifier": "viral",
        "slug": "instagram/polubienia/viral",
        "label": "Polubienia na Instagramie a viral",
        "title": "Polubienia a viral na Instagramie: czy to działa | Growsterr",
        "description": "Myślisz o kupnie polubień na Instagramie, żeby zrobić viral? Same polubienia nie niosą posta; robią to ludzie, którzy oglądają, udostępniają i zapisują.",
        "h1": ("Viralowe polubienia na Instagramie ", "to skutek, a nie strzał startowy."),
        "intro": "Ludzie często kupują polubienia na Instagramie, żeby post stał się viralem, w nadziei, że duża liczba przekona Instagram i wszystkich innych, że zasługuje na więcej uwagi. Rzadko tak to działa. Polubienia od ludzi, którzy obejrzeli post i im się spodobał, to znak rozpędu; polubienia nawalone pod cichy post nie są znakiem niczego. Sprowadzamy te pierwsze i nie obiecujemy viralu.",
        "hero": {"image": "instagram-followers-1000", "alt": "Polubienia, udostępnienia i zapisania rosną razem pod postem na Instagramie, który zaczyna się rozchodzić"},
        "sections": [
            {
                "h2": "Polubienia przychodzą po rozejściu się posta, nie przed",
                "p": [
                    "Gdy post wystrzeli, polubienia są widocznym śladem tysięcy ludzi, którzy go oglądają, wysyłają znajomym i zapisują na później. Skopiuj ślad bez ludzi, a dostaniesz liczbę bez ruchu.",
                ],
            },
            {
                "h2": "Co naprawdę daje postowi szansę",
                "ul": [
                    "Pierwsza publiczność, która reaguje: ludzie, którzy widzą post wcześnie i lajkują, komentują albo udostępniają.",
                    "Haczyk, który zatrzymuje, i powód, żeby wysłać post komuś dalej.",
                    "Publikowanie tam, gdzie jest Twoja publiczność, w jej języku, gdy przewija feed.",
                    "Skupienie: z pakietem {rising_name} lub {pro_name} więcej osób widzi post, który według Ciebie może pójść dalej.",
                ],
            },
            {
                "h2": "Co obiecujemy, a czego nie",
                "p": [
                    "Obiecujemy prawdziwych ludzi każdego dnia i panel z tym, co zmierzyliśmy. Nie obiecujemy milionów wyświetleń, miejsca w Eksploruj ani posta, który się rozejdzie. Kto to obiecuje, sprzedaje wygląd viralowego posta.",
                ],
            },
        ],
        "faqs": [
            ("Czy kupienie polubień sprawi, że post stanie się viralem?", "Samo w sobie nie. Liczba polubień to skutek uwagi ludzi, a kupione polubienia dodają liczbę bez uwagi. Polubienia od ludzi, którzy obejrzeli post, dają mu uczciwy start, a to najwięcej, co ktokolwiek może zaoferować."),
            ("Ile polubień potrzebuje viralowy post?", "Nie ma magicznej liczby. Post ze skromnym licznikiem może pójść dalej, jeśli ludzie, którzy go widzą, go udostępniają, a post z dużym licznikiem może utknąć."),
            ("Czy wysyłacie polubienia w pierwszej godzinie po publikacji?", "Nie zgrywamy polubień z publikacją. Ludzie przychodzą przez cały miesiąc i lajkują to, co im się podoba. Jeśli jeden post jest ważniejszy, {rising_name} i {pro_name} pozwalają wybrać posty, które dostają uwagę."),
            ("Czy udostępnienia i zapisania są w pakiecie?", "Nie liczymy ich ani nie sprzedajemy, ale się zdarzają: ludzie, którzy lajkują Twoje posty, mogą je też udostępniać i zapisywać, czego boty nigdy nie robią."),
            ("Czy wysoka liczba polubień zachęca innych do lajkowania?", "Ludzie zauważają ruchliwy post. Ale duża liczba bez komentarzy i udostępnień wygląda na wyreżyserowaną właśnie dla tych, na których chcesz zrobić wrażenie."),
        ],
    },
]
