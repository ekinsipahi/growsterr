"""Polish YouTube pages beyond the hub and subscribers: likes, views and the ways people ask for
subscribers (prawdziwi, bezpiecznie, co miesiąc...). Mirrors en/youtube_core.py. Keys and
placeholders: docs/CONTENT.md; brief: docs/keywords/WRITING.md; word forms: pl/ui.py. Views are
never counted in advance; we never promise monetization, watch hours or retention."""

UPDATED = "2026-11-09"

PAGES = [
    # --- Likes ---------------------------------------------------------------------------
    {
        "service": "likes",
        "slug": "youtube/polubienia",
        "label": "Polubienia na YouTube",
        "title": "Kup polubienia na YouTube? Prawdziwi widzowie | Growsterr",
        "description": "Chcesz kupić polubienia na YouTube? Każde polubienie w naszych pakietach daje widz, który obejrzał, razem z nowymi subskrybentami. Od {from_price} miesięcznie.",
        "h1": ("Chcesz kupić polubienia na YouTube? ", "Zdobądź je od ludzi, którzy obejrzeli."),
        "intro": "Jeśli przyszedłeś kupić polubienia na YouTube, najpierw prosta odpowiedź: nie sprzedajemy polubień w paczkach. Każdy pakiet sprowadza na Twój kanał prawdziwych ludzi, którzy oglądają Twoje filmy i lajkują te, które im się podobają, zwykle {starter_likes} polubień miesięcznie w pakiecie {starter_name}, a w większych pakietach więcej.",
        "hero": {"image": "youtube-viewers", "alt": "Widzowie na telefonach lajkują film na YouTube, który właśnie obejrzeli"},
        "sections": [
            {
                "h2": "Co polubienie mówi YouTube",
                "p": [
                    "Polubienie to mały publiczny głos od kogoś, kto kliknął play. YouTube czyta go razem ze wszystkim innym, co zrobił ten widz: jak długo oglądał, czy zasubskrybował, czy wrócił na kolejny film.",
                    "Polubienie z konta, które nigdy nie oglądało, łamie ten wzór. Licznik pod filmem rośnie, a wszystko wokół stoi w miejscu, a zaangażowanie, które YouTube uzna za sztuczne, traktuje jak spam.",
                ],
            },
            {
                "h2": "Gdzie trafiają polubienia: filmy, muzyka i posty",
                "p": [
                    "Nowi widzowie lajkują to, co im się podoba, zwykle Twoje najnowsze filmy i ten, który przyprowadził ich na kanał. Muzycy widzą to samo przy teledyskach i lyric video: polubienia od słuchaczy, którzy włączyli utwór i chcieli więcej.",
                    "Posty w społeczności działają inaczej. Twoi subskrybenci widzą je w swoim feedzie i mogą je polubić sami z siebie, ale zakresy, które podajemy, to polubienia pod filmami.",
                ],
                "image": {"image": "youtube-channel", "alt": "Muzyk nagrywa piosenkę w domowym studiu do teledysku na YouTube"},
            },
            {
                "h2": "Dlaczego polubienia przychodzą z subskrybentami",
                "p": [
                    "Polubienie to najlżejsza rzecz, jaką może zrobić widz. W pakiecie idzie w parze z cięższymi sygnałami od tych samych ludzi: subskrypcją, komentarzem, powrotem na kolejny film. Gdy te liczby rosną razem, opisują kanał, który ludzie lubią, bo taki właśnie jest.",
                ],
            },
        ],
        "faqs": [
            ("Czy mogę kupić polubienia na YouTube bez subskrybentów?", "Nie. Polubienia są w każdym pakiecie, razem z nowymi subskrybentami i komentarzami od tych samych prawdziwych ludzi. Polubienie, za którym nikt nie ogląda, to rodzaj zaangażowania, który YouTube traktuje jak spam."),
            ("Ile polubień daje typowy miesiąc?", "Z pakietem {pick_name} zwykle {pick_likes}, czyli mniej więcej dwa, trzy polubienia na każdego nowego subskrybenta. Prawdziwi ludzie decydują, co polubić, więc żadne dwa miesiące nie są takie same."),
            ("Czy mogę dostać polubienia pod postem w społeczności na YouTube?", "Nie jako osobne zamówienie. Nowi subskrybenci widzą Twoje posty w społeczności w swoim feedzie, a część polubi je, bo zechce. Typowe zakresy w każdym pakiecie liczą polubienia pod filmami."),
            ("Czy teledyski też dostają polubienia?", "Tak. Jeśli Twój kanał jest muzyczny, ludzie, których sprowadzamy, to słuchacze, którzy włączyli Twoje utwory i polubili te, które im się spodobały. Możesz skierować kampanię na miasto, region lub kraj, w którym są Twoi słuchacze."),
            ("Które moje filmy zostaną polubione?", "Wybierają prawdziwi widzowie, więc zwykle są to Twoje najnowsze filmy i ten, który jako pierwszy przyprowadził ich na kanał."),
            ("Kiedy pojawiają się pierwsze polubienia?", "W pierwszych dniach kampanii, gdy przychodzą pierwsi widzowie, a potem po kilka każdego dnia przez resztę miesiąca."),
        ],
    },
    {
        "service": "likes",
        "modifier": "comment-likes",
        "slug": "youtube/polubienia/pod-komentarzami",
        "label": "Polubienia komentarzy na YouTube",
        "title": "Polubienia komentarzy na YouTube: skąd prawdziwe | Growsterr",
        "description": "Myślisz o kupnie polubień komentarzy na YouTube? Nie wypychamy jednego komentarza. Prawdziwi widzowie czytają wątki i lajkują to, z czym się zgadzają.",
        "h1": ("Polubienia komentarzy na YouTube? ", "Zbuduj sekcję komentarzy wartą polubień."),
        "intro": "Ludzie, którzy kupują polubienia komentarzy na YouTube, zwykle chcą wypchnąć jeden komentarz na górę. Tego nie sprzedajemy. Sprowadzamy na Twój kanał prawdziwych widzów, a ci, którzy czytają komentarze pod Twoimi filmami, lajkują odpowiedzi, pytania i żarty, które do nich przemawiają, w tym Twój przypięty komentarz.",
        "hero": {"image": "youtube-viewers", "alt": "Widz przewija komentarze pod filmem na YouTube i lajkuje odpowiedź"},
        "sections": [
            {
                "h2": "Jeden komentarz na górze to nie cel",
                "p": [
                    "Komentarz z setkami polubień pod filmem, który ledwo drgnął, rzuca się w oczy każdemu, kto czyta wątek. Polubienia komentarzy to zaangażowanie jak każde inne, więc polubienia ze skryptów też podlegają zasadom YouTube dotyczącym spamu.",
                    "A jeśli komentarz jest pod filmem innego twórcy, w ogóle nie zajmujemy się jego podbijaniem. Rozwijamy Twój własny kanał, z ludźmi, którzy go wybierają.",
                ],
            },
            {
                "h2": "Jak ożywa sekcja komentarzy",
                "p": [
                    "Prawdziwi widzowie czytają komentarze po obejrzeniu. Odpowiadają, lajkują komentarze, z którymi się zgadzają, i zostawiają własne: zwykle {pick_comments} nowych komentarzy miesięcznie z pakietem {pick_name}, pisanych przez ludzi, a nie skrypty.",
                ],
                "ul": [
                    "Przypnij komentarz, który zadaje widzom prawdziwe pytanie. Odpowiedzi zaczynają własne wątki.",
                    "Odpowiadaj na pierwsze komentarze pod nowym filmem. Twórca w wątku przyciąga do niego więcej ludzi.",
                    "Dawaj serduszka komentarzom, które Ci się podobają. Widzowie to zauważają i wracają porozmawiać.",
                ],
                "image": {"image": "youtube-channel", "alt": "Twórca przypina pytanie w komentarzach pod nowym filmem na YouTube"},
            },
            {
                "h2": "Co pakiet liczy, a czego nie",
                "p": [
                    "Subskrybenci, polubienia filmów i komentarze mają typowe miesięczne zakresy. Polubienia komentarzy nie mają: zdarzają się, gdy jeden widz zgadza się z drugim, a tego nikt nie zaplanuje.",
                ],
            },
        ],
        "faqs": [
            ("Czy możecie dodać polubienia mojemu komentarzowi pod filmem innego kanału?", "Nie. Rozwijamy Twój własny kanał z prawdziwymi ludźmi, którzy go wybierają. Podbijanie komentarza pod cudzym filmem nie jest częścią tego, co robimy."),
            ("Czy polubienia komentarzy przychodzą z pakietem?", "Przychodzą tak, jak na każdym żywym kanale: od prawdziwych widzów, którzy czytają wątki pod Twoimi filmami. Nie liczymy ich z góry, bo każde to człowiek, który się z kimś zgadza."),
            ("Czy w moich komentarzach naprawdę zrobi się ruchliwiej?", "Gdy przychodzą ludzie, tak: zwykle {starter_comments} nowych komentarzy miesięcznie w pakiecie {starter_name}, {rising_comments} w {rising_name} i {pro_comments} w {pro_name}, od tych samych ludzi, którzy subskrybują."),
            ("Czy komentarze piszą boty albo AI?", "Nie. Każdy komentarz pochodzi od człowieka, który obejrzał Twój film i miał coś do powiedzenia. Nigdy nie piszemy komentarzy ani scenariuszy dla nikogo."),
            ("Czy możecie wysłać polubienia pod jeden komentarz pod moim filmem?", "Nie. Promujemy Twój kanał, a widzowie decydują, które komentarze zasługują na polubienie, także Twój. Najwięcej zbiera zwykle przypięty komentarz, który pyta o coś prawdziwego."),
            ("Czy kupowanie polubień komentarzy na YouTube jest ryzykowne?", "Od serwisu z botami tak: polubienia komentarzy to zaangażowanie, a YouTube traktuje sztuczne zaangażowanie jak spam. Polubienia od ludzi, którzy naprawdę przeczytali wątek, to zwykłe życie kanału."),
        ],
    },
    {
        "service": "likes",
        "modifier": "live",
        "slug": "youtube/polubienia/live",
        "label": "Polubienia na transmisji na YouTube",
        "title": "Polubienia na live na YouTube? Prawdziwy czat | Growsterr",
        "description": "Zanim kupisz polubienia na live na YouTube: na transmisji dają je ludzie z czatu. Rozwijamy prawdziwych subskrybentów, którzy mogą dołączyć. Od {from_price}.",
        "h1": ("Polubienia na live na YouTube? ", "Dają je ludzie z Twojego czatu."),
        "intro": "Zanim kupisz polubienia na transmisję na YouTube, pomyśl, kto naciska przycisk: ludzie, którzy naprawdę oglądają Twój live. Nie wrzucimy polubień w transmisję o konkretnej minucie i nie będziemy udawać, że potrafimy. Rozwijamy prawdziwych subskrybentów, którzy mogą zobaczyć, że nadajesz, i sami zdecydować, czy dołączyć.",
        "hero": {"image": "youtube-channel", "alt": "Twórca nadaje na żywo na YouTube zza biurka z kamerą i mikrofonem"},
        "sections": [
            {
                "h2": "Polubienie na live to reakcja, a nie liczba",
                "p": [
                    "Podczas transmisji polubienia przychodzą, gdy coś dzieje się na ekranie: decydująca akcja, dobra odpowiedź, piosenka, o którą prosił czat. To publiczność reagująca na bieżąco.",
                    "Polubienia z kont, które nie oglądają, nie reagują na nic. Lądują blokiem obok cichego czatu, a każdy prawdziwy człowiek, który dołącza, widzi, że jedno nie pasuje do drugiego.",
                ],
            },
            {
                "h2": "Jak zamienić najlepsze momenty transmisji w polubienia",
                "ul": [
                    "Poproś o polubienia raz, w kulminacyjnym momencie, a nie w pierwszej minucie.",
                    "Czytaj na głos nicki z czatu: ludzie lajkują transmisje, w których czują się częścią.",
                    "Przypnij komentarz, który mówi spóźnionym, co się dzieje, żeby zostali na tyle długo, by zareagować.",
                    "Zostaw powtórkę na kanale, żeby ci, którzy przegapili transmisję, mogli ją obejrzeć i polubić.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Ludzie piszą i reagują na czacie transmisji na YouTube, gdy twórca mówi"},
            },
            {
                "h2": "Rozwijaj publiczność przed kolejną transmisją",
                "p": [
                    "Subskrybenci, których sprowadzamy, to prawdziwi ludzie, którzy znaleźli Twój kanał i postanowili zostać. Część z nich będzie na Twoim kolejnym czacie, we własnym rytmie. Im większa ta grupa, tym więcej ludzi zareaguje, gdy na transmisji wydarzy się coś dobrego.",
                ],
            },
        ],
        "faqs": [
            ("Czy możecie wysłać polubienia w trakcie mojej transmisji?", "Nie. Prawdziwi ludzie mają własny rozkład dnia, więc nikt uczciwy nie obieca reakcji o konkretnej godzinie. Rozwijamy publiczność, która może oglądać, gdy nadajesz."),
            ("Czy nowi subskrybenci będą oglądać moje transmisje?", "Część z nich, w dni, które im pasują. Wybrali Twój kanał po tym, jak go zobaczyli, więc Twoje transmisje mogą do nich dotrzeć; czy dołączą, to ich decyzja."),
            ("Czy ludzie mogą polubić transmisję po jej zakończeniu?", "Tak. Powtórka zostaje na kanale jako film, a każdy, kto obejrzy ją później, może ją polubić."),
            ("Dlaczego nie kupić polubień na live od serwisu z botami?", "Bo transmisja to miejsce, gdzie fałszywe zaangażowanie najłatwiej wypatrzyć. Setki polubień obok milczącego czatu mówią każdemu, kto dołącza, że pokój nie jest tym, na co wygląda."),
            ("Jak duża może być widownia moich transmisji?", "To zależy od transmisji, ale pula rośnie każdego dnia: {pick_name} zwykle dodaje {pick_audience} subskrybentów w miesiąc, a każdy z nich może być na czacie następnym razem."),
        ],
    },
    {
        "service": "likes",
        "modifier": "shorts",
        "slug": "youtube/polubienia/shorts",
        "label": "Polubienia YouTube Shorts",
        "title": "Polubienia pod YouTube Shorts, te prawdziwe | Growsterr",
        "description": "Polubienia pod YouTube Shorts od prawdziwych ludzi, którzy przestali przewijać, nigdy od botów. W miesięcznym pakiecie z subskrybentami, od {from_price}.",
        "h1": ("Polubienia pod YouTube Shorts? ", "Zdobądź je od ludzi, którzy przestali przewijać."),
        "intro": "W kanale Shorts polubienie oznacza, że ktoś przestał przewijać na tyle długo, żeby go to obeszło. Jeśli chcesz kupić polubienia pod YouTube Shorts, tylko takie są coś warte: od prawdziwych ludzi, których codziennie sprowadzamy na Twój kanał, a którzy oglądają, lajkują i czasem subskrybują.",
        "hero": {"image": "youtube-viewers", "alt": "Ludzie oglądają YouTube Shorts na telefonach i stukają w polubienie"},
        "sections": [
            {
                "h2": "Ile jest warte polubienie pod Shortem",
                "p": [
                    "Shorts lecą w kanale, przez który ludzie przechodzą szybko. Polubienie pochodzi tam od widza, który pozwolił Twojemu Shortowi się odtworzyć, często więcej niż raz, i uznał, że zasłużył na stuknięcie.",
                    "Wygenerowane polubienia pomijają to wszystko. Piętrzą się pod Shortem, którego nikt nie oglądał dalej, a to odwrotność tego, co polubienie ma mówić.",
                ],
            },
            {
                "h2": "Co sprawia, że Short jest wart polubienia",
                "ul": [
                    "Zacznij od puenty. Pierwsza sekunda decyduje, czy ludzie zostaną.",
                    "Niech zakończenie prowadzi z powrotem do początku, żeby powtórka wydawała się naturalna.",
                    "Dodawaj napisy: wielu ludzi przewija bez dźwięku.",
                    "Zakończ jednym wyraźnym powodem, żeby odwiedzić Twój kanał.",
                ],
                "image": {"image": "youtube-channel", "alt": "Twórca nagrywa pionowego Shorta na YouTube telefonem trzymanym w wyciągniętej ręce"},
            },
            {
                "h2": "Co pakiet robi dla Twoich Shorts",
                "ul": [
                    "Promujemy Twój kanał; widzowie, którzy go odkryją, sami wybierają Shorts i filmy do obejrzenia.",
                    "{pick_name} zwykle dodaje w miesiąc {pick_likes} polubień, rozłożonych na to, co ludziom się spodobało.",
                    "Podaj miasto, region lub kraj, żeby Twoje Shorts trafiały do ludzi w miejscu, dla którego je robisz.",
                ],
            },
        ],
        "faqs": [
            ("Czy mogę dostać polubienia tylko pod jednym Shortem?", "Nie jednorazowo. Polubienia przychodzą w miesięcznym pakiecie, rozłożone na Shorts i filmy, które ludziom się podobają, razem z subskrybentami i komentarzami."),
            ("Czy polubienia pod Shorts pomagają moim długim filmom?", "Pośrednio. Część ludzi, którym spodoba się Short, otwiera kanał, który za nim stoi, a niektórzy z nich oglądają potem dłuższe filmy i subskrybują."),
            ("Jak szybko przychodzą polubienia pod moje Shorts?", "Od pierwszych dni kampanii, potem po kilka każdego dnia przez cały miesiąc. Tysiące polubień pod Shortsem w ciągu godziny pochodzą od botów, a nie od widzów."),
            ("Kto lajkuje moje Shorts?", "Ludzie, którzy trafili na Twój kanał dzięki naszej kampanii, w wybranej przez Ciebie lokalizacji. Sami zdecydowali się obejrzeć i sami zdecydowali się polubić; nikt ich nie prosił."),
            ("Czy ludzie będą też komentować moje Shorts?", "Niektórzy tak. Na całym kanale {pick_name} zwykle daje {pick_comments} komentarzy miesięcznie, a każdy napisała osoba, która go zostawiła."),
        ],
    },
    # --- Subscribers ---------------------------------------------------------------------
    {
        "service": "subscribers",
        "modifier": "gradual",
        "slug": "youtube/subskrybenci/stopniowo",
        "label": "Subskrybenci YouTube stopniowo",
        "title": "Subskrybenci YouTube powoli i równo | Growsterr",
        "description": "Subskrybenci YouTube powoli i równo: prawdziwi ludzie, którzy subskrybują po kilku, każdego dnia miesiąca, we własnym tempie. Od {from_price} miesięcznie.",
        "h1": ("Subskrybenci YouTube powoli i równo? ", "To jedyne tempo, jakie mają prawdziwi ludzie."),
        "intro": "Jeśli chcesz kupić subskrybentów YouTube powoli i równo, prosisz o właściwą rzecz. Tutaj powoli to po prostu to, co robią ludzie: odkrywają Twój kanał w swoim czasie, oglądają film czy dwa i decydują. Z pakietem {pick_name} składa się to zwykle na {pick_audience} w ciągu miesiąca.",
        "hero": {"image": "youtube-subscribers", "alt": "Liczba subskrybentów kanału na YouTube rośnie po trochu każdego dnia przez miesiąc"},
        "sections": [
            {
                "h2": "Powolne boty to wciąż boty",
                "p": [
                    "Niektóre serwisy sprzedają opcję „kroplówki”: tych samych subskrybentów-botów, wypuszczanych po kilku, żeby krzywa wyglądała łagodnie. Zmienia się tempo, a nie to, co za nim stoi. Konta, które nigdy nie oglądają, i tak zmniejszają odsetek Twoich subskrybentów, którzy się angażują.",
                    "Stopniowo coś znaczy wtedy, gdy wynika z ludzi decydujących jeden po drugim. Żadne ustawienie tego nie podrobi i żadne nie jest potrzebne.",
                ],
            },
            {
                "h2": "Jak równy wzrost wygląda w Twoim panelu",
                "p": [
                    "Otwórz panel dowolnego dnia, a zobaczysz dwie linie: ludzi, którzy odwiedzili Twój kanał dzięki kampanii, i to, ilu z nich zasubskrybowało. Jedne dni są bardziej ruchliwe od innych, jak na każdym kanale, który ludzie odkrywają. Nie zobaczysz skoku o tysiące przez noc.",
                ],
            },
            {
                "h2": "Dlaczego na YouTube równo wygrywa z nagle",
                "p": [
                    "Kanał, który co tydzień zyskuje subskrybentów, razem z wyświetleniami i komentarzami, to kanał, który ludzie odkrywają. Każdy nowy film trafia do trochę większej grupy prawdziwych ludzi, a przez miesiące to się sumuje.",
                ],
                "image": {"image": "youtube-channel", "alt": "Twórca z YouTube przegląda na laptopie miesiąc równego wzrostu kanału"},
            },
        ],
        "faqs": [
            ("Jak wolno to „powoli”?", "Rzadko: garstka nowych subskrybentów w większość dni, nigdy paczka. W ciągu 30 dni składa się to na typowy zakres pakietu, a każdy dzień jest trochę inny."),
            ("Czy mogę wybrać, jak szybko przychodzą subskrybenci?", "Nie z dokładnością do godziny, bo ustalają to prawdziwi ludzie. Wybierasz pakiet: większy pokazuje Twój kanał większej liczbie ludzi każdego dnia."),
            ("Czy powolna kroplówka jest bezpieczniejsza dla kanału?", "Tylko jeśli subskrybenci są prawdziwi. Powolna kroplówka botów to wciąż fałszywe zaangażowanie, a prawdziwi ludzie subskrybujący we własnym tempie to zwykły wzrost."),
            ("Czy codzienni subskrybenci będą wyglądać podejrzanie?", "Nie. Kanały, które ludzie odkrywają, zyskują subskrybentów każdego dnia; to normalny kształt wzrostu. W oczy rzucają się tysiące w godzinę."),
            ("Co się dzieje, gdy kończy się miesiąc?", "Pakiet się odnawia, a kampania trwa w tym samym równym tempie, chyba że zrezygnujesz. Rezygnacja zatrzymuje kolejną płatność; bieżący miesiąc i tak trwa do końca."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "monthly",
        "slug": "youtube/subskrybenci/co-miesiac",
        "label": "Subskrybenci YouTube co miesiąc",
        "title": "Subskrybenci YouTube co miesiąc, bez zobowiązań | Growsterr",
        "description": "Kupuj subskrybentów YouTube co miesiąc: pakiet sprowadza prawdziwych ludzi na Twój kanał przez cały miesiąc, płatny kartą i z rezygnacją w każdej chwili.",
        "h1": ("Subskrybenci YouTube co miesiąc, ", "tak jak naprawdę rosną kanały."),
        "intro": "Miesięczny pakiet to dokładnie nasz model. Gdy kupujesz u nas subskrybentów YouTube co miesiąc, Twój kanał jest codziennie pokazywany prawdziwym ludziom, ci, którym się spodoba, subskrybują, a pakiet odnawia się co miesiąc, dopóki nie zdecydujesz się przestać.",
        "hero": {"image": "youtube-subscribers", "alt": "Kanał na YouTube zyskuje nowych subskrybentów miesiąc po miesiącu"},
        "sections": [
            {
                "h2": "Dlaczego subskrypcja zamiast jednorazowej paczki",
                "p": [
                    "Kanał nie jest skończony po jednym zrywie. Wciąż publikujesz, więc wciąż potrzebujesz nowych ludzi, którzy Cię znajdą. Miesięczny pakiet pasuje do tego rytmu: każdy nowy film trafia do publiczności, która wciąż rośnie.",
                    "Jednorazowe paczki działają odwrotnie. Dostarczają liczbę pierwszego dnia i nic potem, a ponieważ żadna prawdziwa publiczność nie pojawia się na zawołanie, ta liczba to prawie zawsze boty.",
                ],
            },
            {
                "h2": "Płatność miesiąc po miesiącu",
                "ul": [
                    "Płacisz kartą w bezpiecznej kasie Stripe albo przez Apple Pay i Google Pay na obsługiwanych urządzeniach.",
                    "Pakiet odnawia się co miesiąc od dnia, w którym zaczynasz.",
                    "Zatrzymanie to jedno kliknięcie na Twoim koncie, a kolejna płatność nie zostaje pobrana.",
                    "Możesz przejść na większy pakiet, gdy Twoje filmy będą gotowe na więcej ludzi.",
                ],
            },
            {
                "h2": "Co narasta miesiąc po miesiącu",
                "p": [
                    "Każdy miesiąc dodaje prawdziwych subskrybentów, którzy zostają tak długo, jak lubią Twój kanał. Przez kilka miesięcy powstaje z tego grono ludzi, którzy widzą Twoje filmy, więc każdy nowy startuje z większą ich liczbą.",
                ],
                "image": {"image": "youtube-channel", "alt": "Twórca planuje filmy na YouTube na kolejny miesiąc na ściennym kalendarzu"},
            },
        ],
        "faqs": [
            ("Czy to subskrypcja?", "Tak. Każdy pakiet to miesięczna subskrypcja płacona kartą, Apple Pay lub Google Pay przez Stripe. Nie ma jednorazowych paczek."),
            ("Ile zwykle dodaje każdy miesiąc?", "{starter_name} zwykle daje {starter_audience}, {rising_name} {rising_audience}, a {pro_name} {pro_audience}. Każdy miesiąc trochę się różni, bo każdy subskrybent to człowiek, który dokonuje wyboru."),
            ("Czy mogę zrezygnować po pierwszym miesiącu?", "Tak. Zrezygnuj na swoim koncie w dowolnym momencie; opłacony już miesiąc trwa do ostatniego dnia, a potem nic się nie odnawia."),
            ("Czy zachowam subskrybentów, jeśli zrezygnuję?", "Nikt nie odchodzi dlatego, że przestałeś płacić: to ludzie i subskrybują tak długo, jak interesuje ich Twój kanał. Rezygnacja kończy nowe kampanie; nikogo nie usuwa."),
            ("Czym mogę płacić?", "Kartą albo przez Apple Pay lub Google Pay, jeśli Twój telefon je oferuje. Wybrana metoda jest obciążana co miesiąc, dopóki nie zrezygnujesz."),
            ("Czy mogę zacząć od małego pakietu i dorosnąć do większego?", "Tak. Zacznij od tego, gdzie Twój kanał jest dziś, często od {starter_name}, i przejdź wyżej, gdy publikujesz na tyle dużo, żeby przyjąć więcej ludzi."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "no-drop",
        "slug": "youtube/subskrybenci/bez-spadkow",
        "label": "Subskrybenci YouTube bez spadków",
        "title": "Subskrybenci YouTube bez spadków i bez botów | Growsterr",
        "description": "Liczba subskrybentów spada, gdy subskrybenci nigdy nie byli prawdziwi. Nasi to ludzie, którzy wybrali Twój kanał, a nie konta czekające na usunięcie.",
        "h1": ("Subskrybenci YouTube bez spadków? ", "Zacznij od ludzi, którzy wybrali Twój kanał."),
        "intro": "Chęć kupienia subskrybentów YouTube bez spadków zwykle oznacza, że już widziałeś, jak licznik leci w dół. Subskrybenci spadają, gdy nigdy nie byli ludźmi: YouTube czyści spam i zamknięte konta, a subskrybenci-boty odchodzą razem z nimi. Nasi to prawdziwi widzowie, którzy sami zdecydowali się subskrybować, czyli rodzaj konta, który czystka ma zostawić w spokoju.",
        "hero": {"image": "youtube-subscribers", "alt": "Liczba subskrybentów na YouTube trzyma się, a przychodzą nowi prawdziwi subskrybenci"},
        "sections": [
            {
                "h2": "Dlaczego liczba subskrybentów spada",
                "p": [
                    "YouTube usuwa subskrybentów, których uzna za spam, oraz konta, które zostały zamknięte. Kanały, które kupiły subskrybentów-botów, widzą, jak te liczby spadają schodkami, czasem miesiące po zakupie.",
                    "Spadek to widoczna część. Ukryta to czas, który te konta spędziły na Twoim kanale, nigdy nic nie oglądając i obniżając odsetek Twoich subskrybentów, którzy się angażują.",
                ],
            },
            {
                "h2": "Dlaczego uzupełnienie to nie rozwiązanie",
                "p": [
                    "Niektórzy sprzedawcy obiecują uzupełnić wszystko, co odpadnie. Oznacza to zastępowanie usuniętych botów świeżymi botami, co trzyma liczbę w górze, a problem przy życiu. Prawdziwego subskrybenta nie trzeba zastępować.",
                ],
            },
            {
                "h2": "Jak wygląda uczciwe „bez spadków”",
                "p": [
                    "Prawdziwi ludzie mogą zrezygnować z subskrypcji, jak na każdym kanale, i z czasem kilku to zrobi. To normalna rotacja, drobna przy falach, które zostawiają boty. Zostaje publiczność, która jest na miejscu, gdy publikujesz.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Wieloletni subskrybenci oglądają na kanapie najnowszy film twórcy na YouTube"},
            },
        ],
        "faqs": [
            ("Czy ktoś z nowych subskrybentów kiedyś odejdzie?", "Niektórzy mogą, jak na każdym kanale, gdy zmieniają się gusta. Nie będziesz mieć za to paczki fałszywych kont czekających, aż zostaną usunięte razem."),
            ("Czy jest uzupełnienie, jeśli subskrybenci spadną?", "Nie, bo nie ma fałszywej liczby do dobijania. Dostajesz miesięczny pakiet prawdziwych ludzi; co robią potem, to ich wybór, jak przy każdej publiczności."),
            ("Dlaczego moja liczba spadła po innym serwisie?", "Najpewniej YouTube usunął konta, które uznał za spam, albo konta, które zostały zamknięte. Subskrybenci-boty zwykle odchodzą dużymi partiami podczas takich czystek."),
            ("Czy subskrybenci-boty mogą zaszkodzić kanałowi nawet po zniknięciu?", "Usunięcie to mniejszy problem. Gdy byli na kanale, nie obejrzeli ani jednego filmu, przez co Twoja publiczność wyglądała na mniej zaangażowaną, niż była naprawdę."),
            ("Czy mój panel zgadza się z liczbą na YouTube?", "Nie dokładnie. Panel liczy nowych subskrybentów, których przyniosła nasza kampania; suma na YouTube obejmuje też wzrost z innych źródeł i każdego, kto zrezygnował z subskrypcji."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "organic",
        "slug": "youtube/subskrybenci/organiczni",
        "label": "Organiczni subskrybenci YouTube",
        "title": "Organiczni subskrybenci YouTube: jak to działa | Growsterr",
        "description": "Czy można kupić organicznych subskrybentów YouTube? Płacimy za przedstawienie kanału w promowanych kampaniach; decyzja o subskrypcji należy do widza.",
        "h1": ("Organiczni subskrybenci YouTube? ", "Płacimy za przedstawienie. Oni wybierają."),
        "intro": "Oto uczciwa odpowiedź dla każdego, kto chce kupić organicznych subskrybentów YouTube: nikt nie sprzeda Ci decyzji. Płacimy za przedstawienie. Twój kanał jest pokazywany prawdziwym ludziom w promowanych kampaniach w naszej sieci partnerskiej, a kto subskrybuje, robi to, bo chce.",
        "hero": {"image": "youtube-subscribers", "alt": "Nowi subskrybenci dołączają do kanału na YouTube po odkryciu jego filmów"},
        "sections": [
            {
                "h2": "Granica między płatnym a organicznym",
                "p": [
                    "Każdy kanał, który się reklamuje, płaci za uwagę. To, co dzieje się dalej, albo jest organiczne, albo nie: człowiek ogląda, film mu się podoba albo nie, subskrybuje albo idzie dalej.",
                    "Trzymamy tę granicę czystą. Płacimy, żeby codziennie pokazywać Twój kanał ludziom; nigdy nie płacimy nikomu za subskrypcję, nigdy nie wymieniamy subskrypcji i nigdy nie używamy kont działających na polecenie.",
                ],
            },
            {
                "h2": "Jak odróżnić organicznych subskrybentów od reszty",
                "ul": [
                    "Ich nicki pojawiają się w komentarzach pod Twoim kolejnym filmem.",
                    "Ich komentarze brzmią jak ludzie: pytania, żarty, czasem niezgoda.",
                    "Nowi subskrybenci przychodzą razem z wizytami na kanale, nigdy bez nich.",
                    "Zostają po zakończeniu kampanii, bo nic ich tam nie trzymało.",
                ],
            },
            {
                "h2": "Organicznie nie musi znaczyć czekać",
                "p": [
                    "Organiczny wzrost często wyobraża się jako lata czekania na jeden szczęśliwy film. Promowana kampania skraca czekanie: prawdziwi ludzie widzą Twój kanał od pierwszych dni. Jedynej rzeczy nie skróci: ich decyzji, a to właśnie ta część jest warta zachowania.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Ktoś z kawą w ręku klika subskrypcję kanału, który znalazł tego ranka"},
            },
        ],
        "faqs": [
            ("Jeśli promujecie mój kanał, czy wzrost jest wciąż organiczny?", "Subskrypcje tak. Płacimy za to, żeby Twój kanał był pokazywany; nikt nie dostaje pieniędzy ani nagrody za subskrypcję. Każdy subskrybent zdecydował sam, po obejrzeniu Twoich filmów."),
            ("Czy korzystacie z sub za sub albo sieci wymian?", "Nigdy. Ludzie, którzy subskrybują, żeby dostać subskrypcję w zamian, nie interesują się Twoimi filmami i rzadko je oglądają, a YouTube liczy takie wymiany jako fałszywe zaangażowanie."),
            ("Ile daje organiczny wzrost w miesiąc?", "{pick_name} zwykle ląduje gdzieś w przedziale {pick_audience} miesięcznie. Ponieważ każdy to człowiek, który wybiera, to zakres, a nie liczba."),
            ("Czy organiczni subskrybenci będą oglądać moje filmy?", "Wybrali Twój kanał po tym, jak go zobaczyli, a to najlepszy start, jaki może mieć subskrybent. Czy obejrzą każdy film, zależy od filmu, jak u wszystkich."),
            ("Czy muszę coś robić w trakcie kampanii?", "Utrzymuj kanał publiczny i publikuj dalej. Im bardziej Twoje filmy odpowiadają temu, co obiecuje strona kanału, tym więcej odwiedzających decyduje się subskrybować."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "real",
        "slug": "youtube/subskrybenci/prawdziwi",
        "label": "Prawdziwi subskrybenci YouTube",
        "title": "Prawdziwi subskrybenci YouTube, do sprawdzenia | Growsterr",
        "description": "Prawdziwi, autentyczni, wysokiej jakości: cztery rzeczy, które sprawdzisz u każdego subskrybenta YouTube, i jak sprowadzamy ludzi, którzy je spełniają.",
        "h1": ("Prawdziwi subskrybenci YouTube. ", "Oto jak to sprawdzić."),
        "intro": "Gdy ludzie kupują subskrybentów YouTube, słowo „prawdziwi” dodają, gdy raz już się sparzyli. Uważamy, że powinno ono znaczyć coś, co da się sprawdzić: człowieka, który trafił na Twój kanał, uznał, że warto go subskrybować, a potem pojawia się w Twoich wyświetleniach, polubieniach i komentarzach.",
        "hero": {"image": "youtube-subscribers", "alt": "Strona kanału na YouTube, na którą przez miesiąc przychodzą prawdziwi subskrybenci"},
        "sections": [
            {
                "h2": "Cztery znaki, że subskrybent jest prawdziwy",
                "p": [
                    "Wysoka jakość, autentyczni, prawdziwi: każdy sprzedawca używa tych słów. Oto sprawdziany, które je od siebie odróżniają.",
                ],
                "ul": [
                    "Najpierw była wizyta: ktoś otworzył Twój kanał, zanim zasubskrybował.",
                    "Oglądają: wyświetlenia Twojego kolejnego filmu rosną razem z liczbą subskrybentów.",
                    "Rozmawiają, w komentarzach, których nie napisałby żaden skrypt.",
                    "Mieszkają tam, gdzie skierowałeś kampanię, w miejscu wskazanym przy zamówieniu.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Nowy subskrybent komentuje film na YouTube własnymi słowami"},
            },
            {
                "h2": "Porównaj nas z YouTube Studio",
                "p": [
                    "Nasza strona historii to Twój panel Growsterr: wizyty z kampanii na Twoim kanale i to, kto z tych osób zasubskrybował. YouTube Studio opowiada ten sam miesiąc od strony YouTube. Czytaj je razem przez miesiąc: gdy przychodzą subskrybenci, Twoje filmy powinny też zyskiwać wyświetlenia i komentarze od nowych ludzi.",
                ],
            },
            {
                "h2": "Czego prawdziwi subskrybenci nie potrafią",
                "p": [
                    "Prawdziwych ludzi nie da się zamówić na godzinę, nie da się im kazać, co skomentować, i nie mogą obiecać, że obejrzą każdy film. Każdy, kto oferuje takie rzeczy, opisuje coś innego niż ludzi. Wolimy powiedzieć Ci o ograniczeniach, niż sprzedać liczbę.",
                ],
            },
        ],
        "faqs": [
            ("Co znaczy „wysoka jakość” u subskrybentów YouTube?", "Dla nas: człowiek z własnym kontem, który wybrał Twój kanał i może oglądać, lajkować i komentować. Zdjęcia profilowe i wiek konta łatwo podrobić; prawdziwej decyzji o subskrypcji nie."),
            ("Czy Wasi subskrybenci to prawdziwi ludzie, czy konta, które kontrolujecie?", "Prawdziwi ludzie. Nie posiadamy, nie prowadzimy i nie wynajmujemy żadnych kont. Pokazujemy Twój kanał w promowanych kampaniach, a ludzie, którzy go widzą, decydują."),
            ("Czy mogę kupić prawdziwych subskrybentów YouTube online bez podawania logowania?", "Tak, i nigdy nie powinieneś nikomu go podawać. Potrzebujemy identyfikatora kanału i publicznego kanału, nic więcej."),
            ("Czy prawdziwi subskrybenci zapewnią mojemu kanałowi monetyzację?", "To decyzja YouTube, więc nigdy nie obiecujemy monetyzacji ani godzin oglądania. Prawdziwi subskrybenci mogą oglądać Twoje filmy, czego boty nigdy nie robią, ale o monetyzacji decydują wymagania i weryfikacja YouTube."),
            ("Jak wygląda miesiąc prawdziwego wzrostu?", "W pakiecie {pick_name} zwykle {pick_audience} nowych subskrybentów, przychodzących po kilku każdego dnia. Mniejszy kanał może zacząć od {starter_name} za {starter_price} miesięcznie."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "safe",
        "slug": "youtube/subskrybenci/bezpiecznie",
        "label": "Bezpieczni subskrybenci YouTube",
        "title": "Subskrybenci YouTube bezpiecznie i uczciwie | Growsterr",
        "description": "Czy kupowanie subskrybentów YouTube jest uczciwe i bezpieczne? Sprawdź, kto prowadzi serwis, o co prosi i jak przychodzą subskrybenci. Oto nasze odpowiedzi.",
        "h1": ("Uczciwi subskrybenci YouTube? ", "Najpierw sprawdź, kto za tym stoi."),
        "intro": "Zastanawiasz się, czy da się kupić subskrybentów YouTube uczciwie i bezpiecznie? Uczciwy serwis powinien przejść trzy sprawdziany: firma, którą da się nazwać, nic, co dotyka Twojego logowania, i subskrybenci, którzy są prawdziwymi ludźmi. Growsterr to produkt Sterr Agency, a oto jak odpowiadamy na każdy z nich.",
        "hero": {"image": "youtube-subscribers", "alt": "Kanał twórcy na YouTube rośnie bezpiecznie dzięki subskrybentom, którzy są prawdziwymi ludźmi"},
        "sections": [
            {
                "h2": "Komu płacisz",
                "p": [
                    "Za Growsterr stoi Sterr Agency, zarejestrowana jako Sterr Technologies OÜ w Tallinnie w Estonii, z siedzibą główną w Turcji. Płacisz przez bezpieczną kasę Stripe, a subskrypcja jest na Twoim własnym koncie, gdzie możesz ją anulować.",
                ],
            },
            {
                "h2": "Jak Twój kanał pozostaje chroniony",
                "ul": [
                    "Hasło do Google zostaje u Ciebie: nigdy o nie nie prosimy i nikt od nas nie loguje się na Twój kanał.",
                    "Nikt nie dostaje pieniędzy za subskrypcję i nie ma wymian subskrypcji.",
                    "Subskrybenci przychodzą przez cały miesiąc, nigdy paczką.",
                    "Polubienia i komentarze dają sami subskrybenci, więc każda liczba rośnie w tym samym rytmie.",
                ],
                "image": {"image": "youtube-channel", "alt": "Twórca przy biurku sprawdza ustawienia kanału na YouTube, zalogowany tylko na własnym urządzeniu"},
            },
            {
                "h2": "Sygnały ostrzegawcze w każdym serwisie wzrostu",
                "ul": [
                    "Prosi o Twoje logowanie albo o dostęp do konta Google.",
                    "Obiecuje dokładną liczbę subskrybentów na konkretny termin.",
                    "Sprzedaje subskrybentów, wyświetlenia i polubienia jako osobne paczki na tysiące.",
                    "Nie potrafi powiedzieć, skąd są subskrybenci, ani pokazać, co zmierzył.",
                ],
            },
        ],
        "faqs": [
            ("Czy kupowanie subskrybentów YouTube jest w porządku?", "Płacenie za promocję to nic nadzwyczajnego; robi to każdy kanał, który się reklamuje. Płacenie za fałszywe zaangażowanie już nie: boty, skrypty i wymiany subskrypcji YouTube traktuje jak spam. My tylko promujemy Twój kanał wśród prawdziwych ludzi, którzy decydują sami."),
            ("Czy YouTube może za to zablokować mój kanał?", "YouTube działa przeciwko fałszywemu zaangażowaniu i dlatego nigdy go nie używamy. Nie wypowiadamy się za decyzje YouTube, ale ludzie wybierający Twój kanał po jego obejrzeniu to sposób, w jaki wszędzie działa promocja."),
            ("Co muszę podać na start?", "Identyfikator kanału, miejsce, z którego ma pochodzić Twoja publiczność, i kartę płatniczą do miesięcznego pakietu. Kanał musi być publiczny, żeby ludzie mogli go subskrybować."),
            ("Czy moja płatność jest bezpieczna?", "Każdą płatność obsługuje Stripe, czy płacisz kartą, Apple Pay, czy Google Pay. Dane karty zostają w Stripe, a nie u nas."),
            ("Co, jeśli to nie dla mnie?", "Zrezygnuj na swoim koncie, kiedy chcesz. Potem nie zostanie pobrana żadna nowa płatność, a bieżący miesiąc trwa do końca."),
        ],
    },
    # --- Views ---------------------------------------------------------------------------
    {
        "service": "views",
        "slug": "youtube/wyswietlenia",
        "label": "Wyświetlenia na YouTube",
        "title": "Kup wyświetlenia na YouTube od prawdziwych ludzi | Growsterr",
        "description": "Chcesz kupić wyświetlenia filmów na YouTube? Nasze dają prawdziwi ludzie, którzy sami chcą oglądać, w pakiecie z subskrybentami i polubieniami. Od {from_price}.",
        "h1": ("Kup wyświetlenia filmów na YouTube? ", "Za każdym stoi człowiek."),
        "intro": "Jeśli chcesz kupić wyświetlenia filmów na YouTube, oto jak działają nasze. Nie ma tu cennika liczby wyświetleń. Każdy pakiet codziennie przedstawia Twój kanał prawdziwym ludziom; klikają play przy tym, co ich interesuje, a wielu potem lajkuje, komentuje i subskrybuje. Wyświetlenia przychodzą z pakietem, a każde to człowiek.",
        "hero": {"image": "youtube-viewers", "alt": "Prawdziwi ludzie włączają film twórcy na YouTube"},
        "sections": [
            {
                "h2": "Dlaczego w naszych pakietach nie ma liczby wyświetleń",
                "p": [
                    "Wyświetlenie to człowiek, który decyduje się obejrzeć, a nikt nie obieca, ilu ludzi tak zdecyduje. Każdy, kto sprzedaje dokładną liczbę wyświetleń na konkretną godzinę, sprzedaje odtworzenia generowane przez skrypty albo boty.",
                    "YouTube traktuje sztucznie pompowane wyświetlenia jak spam: może je usunąć, a do monetyzacji nigdy się nie liczą. Dlatego sprzedajemy to, za czym możemy stanąć: miesięczną kampanię, która sprowadza prawdziwych ludzi, z typowymi zakresami subskrybentów, polubień i komentarzy, które zostawiają.",
                ],
            },
            {
                "h2": "Teledyski, playlisty i długie filmy",
                "p": [
                    "Promujemy Twój kanał, a nie jeden utwór. Słuchacze, którzy go odkryją, wybierają piosenki, które ich złapią, a ci, którym utwór się spodoba, mogą przejść dalej przez Twoje playlisty; każde odtworzenie tam jest ich.",
                ],
                "image": {"image": "youtube-channel", "alt": "Muzyk wrzuca nowy teledysk na swój kanał na YouTube"},
            },
            {
                "h2": "Zanim wybierzesz stronę z wyświetleniami na YouTube",
                "ul": [
                    "Zapytaj, czym jest dla nich wyświetlenie: człowiekiem, który zdecydował się obejrzeć, czy odtworzeniem, które wygenerowali.",
                    "Sprawdź, czy wyświetlenia przychodzą same, czy z subskrybentami, polubieniami i komentarzami od tych samych ludzi.",
                    "Szukaj nazwy firmy, prawdziwej kasy i sposobu na rezygnację.",
                    "Odejdź od każdego, kto prosi o Twoje hasło do Google.",
                ],
            },
        ],
        "faqs": [
            ("Czy mogę zamówić wyświetlenia bez pakietu?", "Nie. Każde wyświetlenie od nas należy do kogoś, kto może też zasubskrybować, polubić albo skomentować, i dlatego przychodzą tylko w ramach pakietu. Licznik wyświetleń, który rośnie, gdy nic innego się nie rusza, to wzór sztucznego ruchu."),
            ("Czy powiecie mi, ilu wyświetleń się spodziewać?", "Nie podajemy liczby wyświetleń, bo każde to czyjś wybór. Podajemy typowe miesięczne zakresy: z pakietem {pick_name} {pick_audience} nowych subskrybentów i {pick_likes} polubień, a ci ludzie oglądają, zanim zrobią jedno albo drugie."),
            ("Czy jest aplikacja do kupowania wyświetleń na YouTube?", "Nie korzystamy z aplikacji. Wybierasz pakiet na naszej stronie, płacisz przez Stripe i śledzisz kampanię w panelu na swoim koncie, z dowolnej przeglądarki."),
            ("Czym są wyświetlenia „premium” na YouTube?", "Niczym, co YouTube uznaje. YouTube Premium to subskrypcja dla widzów, a nie rodzaj wyświetleń, który ktoś może Ci sprzedać. Coś warte są tylko wyświetlenia od ludzi, którzy sami kliknęli play."),
            ("Czy kupione wyświetlenia mogą sprawić, że film stanie się viralem?", "Nikt nie może tego obiecać. Prawdziwi widzowie dają filmowi więcej ludzi, którzy mogą go udostępnić, a to uczciwa wersja szansy na viral."),
            ("Czy wyświetlenia pomagają w monetyzacji kanału?", "Ani monetyzacji, ani godzin oglądania nie obiecujemy. Sztuczne wyświetlenia w ogóle się do niej nie liczą; prawdziwi widzowie mogą oglądać Twoje filmy, ale to YouTube decyduje, kto dostaje monetyzację."),
        ],
    },
    {
        "service": "views",
        "modifier": "gradual",
        "slug": "youtube/wyswietlenia/stopniowo",
        "label": "Wyświetlenia na YouTube stopniowo",
        "title": "Wyświetlenia na YouTube powoli? Tempo dają ludzie | Growsterr",
        "description": "Wyświetlenia na YouTube, które rosną powoli przez miesiąc: prawdziwi widzowie znajdują Twój kanał po kilku, z subskrybentami i polubieniami.",
        "h1": ("Wyświetlenia na YouTube powoli? ", "Prawdziwi widzowie nigdy nie przychodzą inaczej."),
        "intro": "Chęć kupienia wyświetleń na YouTube powoli to dobry odruch: film, który zyskuje wyświetlenia przez kolejne dni, to film, który ludzie odkrywają. Nikt tu nie musi włączać takiego tempa. Prawdziwi ludzie odkrywają Twój kanał każdego dnia miesiąca i oglądają to, co ich interesuje, więc Twoje wyświetlenia rosną tak, jak na każdym rozwijającym się kanale.",
        "hero": {"image": "youtube-viewers", "alt": "Widzowie odkrywają kanał na YouTube jeden po drugim przez kilka tygodni"},
        "sections": [
            {
                "h2": "Zaplanowana kroplówka to nie to samo",
                "p": [
                    "Harmonogram kroplówki rozkłada wygenerowane odtworzenia na tydzień zamiast godziny. Licznik rośnie spokojniej, ale odtworzenia wciąż przychodzą bez prawdziwego oglądania, bez polubień i bez subskrybentów. YouTube patrzy na to, co robią widzowie, a nie tylko na to, jak szybko się pojawili.",
                ],
            },
            {
                "h2": "Twoje starsze filmy też są oglądane",
                "p": [
                    "Widzowie, którzy przychodzą przez kolejne tygodnie, nie oglądają tylko najnowszego filmu. Ktoś, komu spodoba się jeden film, może otworzyć kolejny ze strony kanału, więc starsze filmy zbierają wyświetlenia w tym samym spokojnym tempie. Kroplówka skierowana na jeden link tego nie potrafi.",
                ],
                "image": {"image": "youtube-channel", "alt": "Strona kanału na YouTube z siatką starszych filmów, które zbierają nowe wyświetlenia"},
            },
            {
                "h2": "Tempo, które możesz śledzić",
                "p": [
                    "Panel śledzi ludzi, a nie odtworzenia: dzienne wizyty z kampanii na Twoim kanale i subskrybentów wśród nich. Wyświetleń tam nie ma, bo nie liczymy ich z góry; znajdziesz je w YouTube Studio, przy filmach, które ludzie wybrali.",
                ],
            },
        ],
        "faqs": [
            ("Czy jest dzienna liczba wyświetleń, na którą mogę liczyć?", "Nie ma dziennej liczby do podania: każde wyświetlenie zależy od kogoś, kto decyduje się obejrzeć. Możesz spodziewać się nowych widzów każdego dnia miesiąca, a nie skoku pierwszego dnia."),
            ("Czy mogę rozłożyć wyświetlenia na określoną liczbę dni?", "Każda kampania trwa 30 dni i odnawia się co miesiąc. W tym okresie tempo ustalają prawdziwi ludzie, więc nie planujemy wyświetleń na konkretne dni."),
            ("Czy powolne wyświetlenia wyglądają dla YouTube naturalniej?", "Tempo to tylko część. YouTube widzi też, czy widzowie oglądają dalej, lajkują film i wracają. Prawdziwi ludzie robią to w każdym tempie; zaplanowane odtworzenia nigdy."),
            ("A filmy, które opublikowałem w zeszłym roku?", "Są częścią tego. Ludzie, którym spodoba się jeden film, zwykle sprawdzają, co jeszcze jest na kanale, a starsze filmy to często miejsce, w którym lądują potem."),
            ("Co, jeśli chcę wyświetleń szybciej?", "Wybierz większy pakiet, żeby więcej ludzi widziało Twój kanał każdego dnia. Wszystko, co obiecuje tysiące wyświetleń w ciągu godziny, generuje odtworzenia, a nie znajduje widzów."),
        ],
    },
    {
        "service": "views",
        "modifier": "high-retention",
        "slug": "youtube/wyswietlenia/wysoka-retencja",
        "label": "Wyświetlenia na YouTube z wysoką retencją",
        "title": "Wyświetlenia na YouTube z wysoką retencją? Szczerze | Growsterr",
        "description": "Wyświetleń na YouTube z wysoką retencją nie da się kupić: retencję zdobywa film. Sprowadzamy prawdziwych widzów, którzy sami kliknęli play. Od {from_price}.",
        "h1": ("Wyświetlenia na YouTube z wysoką retencją? ", "Sprowadź ludzi, którzy chcą oglądać."),
        "intro": "Jeśli chcesz kupić wyświetlenia na YouTube z wysoką retencją, wiesz już, że liczba odtworzeń to nie sedno: chcesz widzów, którzy zostają. Retencji nikt jednak nie sprzeda. To to, jak długo prawdziwi ludzie decydują się oglądać. Naszą częścią jest sprowadzenie widzów, którzy sami kliknęli play; jak długo zostaną, zależy od Twojego filmu.",
        "hero": {"image": "youtube-channel", "alt": "Twórca montuje długi film na YouTube tak, żeby widzowie oglądali dalej"},
        "sections": [
            {
                "h2": "Retencja, którą da się kupić, to minutnik",
                "p": [
                    "Gdy sprzedawca oferuje wyświetlenia z ustaloną retencją, stoi za tym odtwarzacz ustawiony na określoną liczbę sekund. Ogląda tak samo, cokolwiek jest na ekranie, i nigdy nie lajkuje, nie komentuje ani nie subskrybuje. Nieważne, jak długo gra: to sztuczne zaangażowanie, a YouTube traktuje je jak spam.",
                ],
            },
            {
                "h2": "Dlaczego dopiero prawdziwi widzowie nadają retencji sens",
                "p": [
                    "Retencja ma znaczenie, bo pokazuje, że ludzie, którzy zaczęli film, chcieli oglądać dalej. To prawda tylko wtedy, gdy w ogóle sami wybrali film. Prawdziwi widzowie dają Ci uczciwe dane o retencji: gdzie zostają, gdzie odpadają i co ich przyciąga z powrotem.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Widz pochyla się, żeby obejrzeć długi film na YouTube do końca"},
            },
            {
                "h2": "Co podnosi retencję z Twojej strony",
                "ul": [
                    "Daj w pierwszych sekundach to, co obiecują tytuł i miniatura.",
                    "Wytnij powolny wstęp: najpierw pokaż sedno, potem je wyjaśnij.",
                    "Dodaj rozdziały do długich filmów, żeby widzowie przeskakiwali do tego, po co przyszli, zamiast wychodzić.",
                    "Znajdź w YouTube Studio moment, w którym widzowie odpadają, i popraw go w kolejnym filmie.",
                ],
            },
        ],
        "faqs": [
            ("Czy obiecujecie procent retencji albo godziny oglądania?", "Nie. Retencja i czas oglądania zależą od filmu i od każdego widza. Sprowadzamy prawdziwych ludzi, którzy sami zdecydowali się oglądać, i nigdy nie podajemy liczby, jak długo zostaną."),
            ("Czy ludzie obejrzą cały mój film?", "Jedni tak, inni nie, i właśnie dlatego ich dane są przydatne. YouTube Studio pokazuje, gdzie ludzie zostają, a gdzie odchodzą."),
            ("Czy wyświetlenia z wysoką retencją liczą się do monetyzacji?", "Sztuczne wyświetlenia w ogóle nie liczą się do monetyzacji, jakąkolwiek mają retencję. Czas oglądania prawdziwych widzów jest prawdziwy, ale nigdy nie obiecujemy monetyzacji; to decyzja YouTube."),
            ("Czy kampania może kierować widzów na jeden film?", "Nie kierujemy widzów na pojedyncze filmy: promujemy Twój kanał, a ludzie wybierają, co obejrzeć. Wciąż możesz ich kierować, bo polecany film na stronie kanału to pierwsze, co widzą nowi odwiedzający."),
            ("Które filmy zyskują najwięcej?", "Filmy, które dotrzymują obietnicy. Wyraźny haczyk, uczciwa miniatura i równe tempo zamieniają nowych widzów w długie oglądanie, a im więcej ludzi kampania sprowadza na Twój kanał, tym więcej z nich te filmy mogą zatrzymać."),
        ],
    },
    {
        "service": "views",
        "modifier": "live",
        "slug": "youtube/wyswietlenia/live",
        "label": "Widzowie na transmisji na YouTube",
        "title": "Wyświetlenia na live na YouTube? Zbuduj widownię | Growsterr",
        "description": "Nikt nie zapełni transmisji na YouTube prawdziwymi ludźmi o ustalonej godzinie. Rozwijamy subskrybentów, którzy mogą dołączyć do kolejnej. Od {from_price}.",
        "h1": ("Wyświetlenia na live na YouTube? ", "Zbuduj widownię, która przychodzi."),
        "intro": "Jeśli chcesz kupić wyświetlenia na transmisję na YouTube, chcesz live, który nie wydaje się pusty, gdy klikasz start. Nikt nie dostarczy prawdziwych ludzi na transmisję o ustalonej minucie i my też tak nie twierdzimy. Codziennie rozwijamy Twój kanał prawdziwymi subskrybentami, więc na każdy live może przyjść więcej osób.",
        "hero": {"image": "youtube-channel", "alt": "Twórca tuż przed startem na YouTube z zaplanowaną transmisją na ekranie"},
        "sections": [
            {
                "h2": "Dlaczego kupiony licznik na live obraca się przeciwko Tobie",
                "p": [
                    "Liczba widzów to pierwsze, co każdy widzi na transmisji. Gdy pokazuje setki, a czat milczy, każdy prawdziwy odwiedzający to zauważa. Kupieni widzowie na live nie piszą, nie reagują i nie wracają na powtórkę.",
                    "Zasady YouTube dotyczące fałszywych wyświetleń nie robią przerwy, gdy nadajesz. Licznik na live nie jest bezpieczniejszym miejscem na podróbki.",
                ],
            },
            {
                "h2": "Kto dołącza do transmisji i kiedy",
                "p": [
                    "Najczęściej dołączają subskrybenci, którzy już znają Twój kanał. Zależnie od ich ustawień YouTube może pokazać im transmisję w feedzie albo wysłać powiadomienie.",
                ],
                "ul": [
                    "Zaplanuj transmisję z wyprzedzeniem, żeby subskrybenci mogli ustawić przypomnienie.",
                    "Wybierz lokalizację publiczności, w której godzina transmisji wypada wieczorem.",
                    "Nadawaj w stały dzień, żeby widzowie wiedzieli, kiedy wrócić.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Widzowie wieczorem dołączają z telefonów do zaplanowanej transmisji na YouTube"},
            },
            {
                "h2": "Powtórka dalej zbiera wyświetlenia",
                "p": [
                    "Gdy transmisja się kończy, zostaje na kanale jako film. Nowi subskrybenci, którzy przegapili ją na żywo, mogą tam znaleźć powtórkę i obejrzeć ją, kiedy im pasuje.",
                ],
            },
        ],
        "faqs": [
            ("Czy możecie zapełnić moją transmisję, gdy nadaję?", "Nie. Prawdziwi ludzie oglądają, kiedy chcą, więc nie obiecamy nikogo o konkretnej godzinie. Rozwijamy bazę subskrybentów, z której czerpią Twoje transmisje."),
            ("Czy wybrana lokalizacja ma znaczenie dla transmisji?", "Większe niż dla zwykłych filmów. Wybierz miejsce, w którym mieszka Twoja publiczność, a godzina transmisji wypadnie w jej dzień, a nie w środku nocy."),
            ("Czy powtórka dostanie wyświetlenia z kampanii?", "Może. Powtórka to film na Twoim kanale, więc widzowie, którzy znajdą Cię po transmisji, mogą ją obejrzeć jak każdy inny film."),
            ("Czy nie mogę po prostu kupić widzów na live dla licznika?", "Możesz, ale to się obraca przeciwko Tobie. Sztuczni widzowie na transmisji to fałszywe zaangażowanie jak każde inne, a pełny licznik nad pustym czatem prawdziwi widzowie łatwo wypatrzą."),
            ("Który pakiet pasuje do kanału, który nadaje na żywo?", "{pick_name} to nasz najpopularniejszy, zwykle {pick_audience} nowych subskrybentów miesięcznie; nowszy kanał może zacząć od {starter_name}. Na każdą kolejną transmisję może przyjść więcej osób."),
        ],
    },
    {
        "service": "views",
        "modifier": "monthly",
        "slug": "youtube/wyswietlenia/co-miesiac",
        "label": "Wyświetlenia na YouTube co miesiąc",
        "title": "Wyświetlenia na YouTube pod wiele filmów, co miesiąc | Growsterr",
        "description": "Kup wyświetlenia na YouTube pod wiele filmów: miesięczny pakiet sprowadza prawdziwych widzów na cały Twój kanał, gdzie sami wybierają, co obejrzeć.",
        "h1": ("Wyświetlenia na YouTube pod wiele filmów, ", "miesiąc po miesiącu."),
        "intro": "Gdy kupujesz wyświetlenia na YouTube pod wiele filmów, tak naprawdę chcesz kanału, do którego ludzie wracają. Miesięczny pakiet jest zbudowany właśnie do tego: prawdziwi ludzie codziennie odkrywają Twój kanał i oglądają filmy, które ich interesują, a kampania odnawia się co miesiąc, więc nowe filmy wciąż trafiają na nowych widzów.",
        "hero": {"image": "youtube-viewers", "alt": "Widz przechodzi od jednego filmu na YouTube do kolejnego na tym samym kanale"},
        "sections": [
            {
                "h2": "Jeden kanał, wiele filmów",
                "p": [
                    "Zainteresowani widzowie nie kończą na jednym filmie. Ktoś, kto znajdzie Cię przez poradnik, otwiera kolejny, a potem to, co podsuwa strona Twojego kanału. Kampania zbudowana wokół kanału, a nie pojedynczego linku, idzie za tym, jak ludzie naprawdę oglądają.",
                ],
            },
            {
                "h2": "Jak kształtować, dokąd nowi widzowie pójdą dalej",
                "p": [
                    "Promujemy Twój kanał jako całość; widzowie decydują, które filmy otworzyć. Ty kontrolujesz ścieżkę, którą mają przed sobą, gdy już przyjdą.",
                ],
                "ul": [
                    "Ustaw zwiastun kanału dla odwiedzających, którzy jeszcze nie subskrybują.",
                    "Wyróżnij najmocniejszy film na górze strony kanału.",
                    "Grupuj powiązane filmy w playlisty, żeby jeden prowadził do kolejnego.",
                    "Dodaj ekrany końcowe, które wskazują film, który widz powinien obejrzeć po tym.",
                ],
            },
            {
                "h2": "Dlaczego rozłożone w czasie wygrywa z wszystkim naraz",
                "p": [
                    "Wyświetlenia rozłożone na miesiąc trafiają do każdego filmu, póki jest nowy, i podtrzymują przy życiu starsze. Jednorazowy wysyp na kilku filmach robi odwrotnie: po jednym skoku na każdym, a potem cisza.",
                ],
                "image": {"image": "youtube-channel", "alt": "Twórca układa serię filmów na YouTube do publikacji w ciągu miesiąca"},
            },
        ],
        "faqs": [
            ("Na ile filmów mogą trafić wyświetlenia?", "Nie ma listy ani limitu. Promujemy Twój kanał, a widzowie oglądają to, co ich interesuje, gdziekolwiek na nim."),
            ("Czy nowe filmy opublikowane w trakcie miesiąca dostają wyświetlenia?", "Tak. Kampania działa codziennie, więc film opublikowany w połowie miesiąca wciąż trafia na nowych ludzi, a Twoi nowi subskrybenci mogą go zobaczyć jak każdy subskrybent."),
            ("Czy cena jest za film?", "Nie, jest za miesiąc dla całego kanału: {starter_name} to {starter_price} miesięcznie, {rising_name} {rising_price}, a {pro_name} {pro_price}, niezależnie od liczby filmów. Wyświetlenia są w środku, z subskrybentami, polubieniami i komentarzami."),
            ("Czy mogę przestać po jednym miesiącu?", "Tak. Zrezygnuj na swoim koncie; opłacony miesiąc kończy się normalnie, a za kolejny nic nie jest pobierane."),
            ("Czy wyświetlenia mogą pochodzić z jednego miasta?", "Tak. Działa jedno miasto, a także region czy cały kraj. To dobre dla kanałów z lokalną publicznością, takich jak miejski przewodnik kulinarny albo lokalny kanał z wiadomościami."),
        ],
    },
    {
        "service": "views",
        "modifier": "no-drop",
        "slug": "youtube/wyswietlenia/bez-spadkow",
        "label": "Wyświetlenia na YouTube bez spadków",
        "title": "Wyświetlenia na YouTube bez spadków? Skąd spadki | Growsterr",
        "description": "Dlaczego liczba wyświetleń na YouTube spada po zakupie i czym różnią się wyświetlenia od ludzi, którzy sami kliknęli play. Od {from_price} miesięcznie.",
        "h1": ("Prawdziwe wyświetlenia na YouTube bez spadków? ", "Takie, które nigdy nie były fałszywe."),
        "intro": "Każdy, kto chce kupić prawdziwe wyświetlenia na YouTube bez spadków, zwykle widział już, jak licznik leci w dół. Wyświetlenia spadają, gdy YouTube usuwa odtworzenia, które uzna za sztuczne. Nasze dają prawdziwi ludzie, którzy sami kliknęli play, w miesięcznym pakiecie, więc nie czeka żadna paczka fałszywych odtworzeń do odebrania.",
        "hero": {"image": "youtube-channel", "alt": "Twórca w studiu sprawdza, że licznik wyświetleń filmu na YouTube się trzyma"},
        "sections": [
            {
                "h2": "Dlaczego liczba wyświetleń spada",
                "p": [
                    "YouTube weryfikuje wyświetlenia i usuwa te, których nie uważa za prawdziwe: odtworzenia od botów, skryptów i innego sztucznego ruchu. Gdy dzieje się to po zakupie, licznik spada, czasem długo po dostawie, a historia filmu pokazuje skok, a po nim spadek.",
                ],
            },
            {
                "h2": "Co możemy obiecać, a czego nie",
                "p": [
                    "Nie możemy obiecać, że YouTube nigdy nie skoryguje licznika; sprawdza cały ruch, także nasz. Możemy powiedzieć, jak powstają nasze wyświetlenia: prawdziwy człowiek widzi Twój kanał w promowanej kampanii i decyduje się obejrzeć. To rodzaj wyświetlenia, który kontrole YouTube mają zachować.",
                ],
            },
            {
                "h2": "Gdy wyświetlenia, polubienia i subskrybenci rosną razem",
                "p": [
                    "Prawdziwe wyświetlenia rzadko podróżują same. W pakiecie przychodzą z nowymi subskrybentami, polubieniami i komentarzami od tych samych ludzi, więc Twoje liczby rosną razem i nic w nich nie wygląda nie na miejscu, ani dla YouTube, ani dla widza.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Znajomi oglądają razem film na YouTube i zostawiają polubienie na koniec"},
            },
        ],
        "faqs": [
            ("Czy moje wyświetlenia kiedyś spadną?", "YouTube może skorygować licznik każdego filmu, gdy weryfikuje ruch, więc nikt uczciwie nie obieca liczby, która nigdy się nie ruszy. Wyświetlenia od ludzi, którzy sami zdecydowali się obejrzeć, to rodzaj, który ta weryfikacja ma zachować."),
            ("Czy uzupełnicie wyświetlenia, jeśli licznik spadnie?", "Nie. Uzupełnienie zamienia usunięte fałszywe odtworzenia na nowe. My sprzedajemy miesięczny pakiet prawdziwych ludzi, więc nie ma niczego sztucznego do zastąpienia."),
            ("Dlaczego moje wyświetlenia spadły po wcześniejszym zakupie?", "Najczęściej dlatego, że YouTube usunął odtworzenia, które uznał za sztuczne. Może się to stać kilka tygodni po dostawie, dlatego spadek bywa zaskoczeniem."),
            ("Czy mogę kupić wyświetlenia bez spadków pod jeden film?", "Nie jako pojedyncze zamówienie. Wyświetlenia przychodzą w miesięcznym pakiecie, który rozwija cały Twój kanał, więc może skorzystać każdy film."),
            ("Co jeszcze przychodzi z wyświetleniami?", "Resztę przynoszą sami widzowie. Z pakietem {pick_name} zwykle {pick_audience} subskrybentów, {pick_likes} polubień i {pick_comments} komentarzy miesięcznie."),
        ],
    },
    {
        "service": "views",
        "modifier": "organic",
        "slug": "youtube/wyswietlenia/organiczne",
        "label": "Organiczne, kierowane wyświetlenia na YouTube",
        "title": "Kierowane wyświetlenia na YouTube: miasto lub kraj | Growsterr",
        "description": "Kup kierowane wyświetlenia na YouTube z miasta, regionu lub kraju, w którym mieszka Twoja publiczność: organiczni widzowie, którzy sami zdecydowali się oglądać.",
        "h1": ("Kierowane wyświetlenia na YouTube, ", "z miejsca, w którym mieszka Twoja publiczność."),
        "intro": "Żeby kupić kierowane wyświetlenia na YouTube, powiedz nam, gdzie mają być Twoi widzowie: w mieście, szerszym regionie czy całym kraju. Pokazujemy tam Twój kanał prawdziwym ludziom w promowanych kampaniach, a wyświetlenia są organiczne w sensie, który się liczy: każde to ktoś, kto sam zdecydował się obejrzeć.",
        "hero": {"image": "youtube-channel", "alt": "Twórca nagrywa film na YouTube na ulicy miasta dla lokalnej publiczności"},
        "sections": [
            {
                "h2": "Dlaczego liczy się kierowanie na miejsce",
                "p": [
                    "Kanał kulinarny z Krakowa, kanał o nieruchomościach z Warszawy, kanał o grach po polsku: każdy ma publiczność, która gdzieś mieszka i mówi jakimś językiem. Widzowie z tego miejsca rozumieją Twoje filmy, wracają na kolejny i mogą zostać klientami, jeśli coś sprzedajesz.",
                    "Kierujemy kampanię najpierw na wybrane przez Ciebie miejsce. Jeśli najlepsze dopasowanie dla Twojego kanału to większa publiczność tuż za granicą, część widzów może przyjść stamtąd.",
                ],
            },
            {
                "h2": "Kierowane nie znaczy wymuszone",
                "p": [
                    "Celujemy tam, gdzie są ludzie, a potem pozwalamy im decydować. Nikt nie jest zmuszany do oglądania Twojego filmu i nic się nie odtwarza bez wyboru. Kierowane wyświetlenie to wciąż wybór i właśnie to czyni je organicznym.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Lokalni widzowie w kawiarni oglądają film na YouTube nakręcony w ich mieście"},
            },
            {
                "h2": "Jak wybrać lokalizację",
                "ul": [
                    "Wybierz miejsce, dla którego robisz filmy, a nie największe, jakie przychodzi Ci do głowy.",
                    "Dla lokalnej firmy albo kanału o mieście wybierz samo miasto.",
                    "Jeśli liczy się język, a nie miejsce, wybierz kraj, w którym mieszka większość jego użytkowników.",
                    "Przy międzynarodowej niszy zacznij od kraju, do którego widzów najbardziej chcesz dotrzeć.",
                ],
            },
        ],
        "faqs": [
            ("Jak dokładne jest kierowanie?", "Z dokładnością do miasta. Im mniejsze miejsce, tym mniejsza jego publiczność, więc w małym mieście część widzów może przyjść z okolicy."),
            ("Czy kierowanie sprawia, że wyświetlenia są mniej organiczne?", "Nie: decyzja o oglądaniu zostaje ich. Płacimy za pokazanie Twojego kanału w wybranym miejscu; potem każdy widz decyduje sam i nikt nie dostaje nagrody za oglądanie."),
            ("Czy widzowie z mojego miasta będą subskrybować?", "Niektórzy tak, jeśli Twój kanał do nich przemawia. Z pakietem {pick_name} zwykle {pick_audience} nowych subskrybentów miesięcznie, z wybranego miejsca i okolic."),
            ("Dlaczego nie wybrać jak największego obszaru?", "Większy obszar to większa pula, ale widzowie, którzy nie dzielą Twojego języka ani kontekstu, rzadko zostają. Właściwe miejsce wygrywa z największym."),
            ("Czy potrzebujecie dostępu do kanału, żeby kierować widzów?", "Nie. Kierowanie odbywa się w naszych kampaniach, a nie w ustawieniach Twojego kanału. Potrzebujemy identyfikatora kanału i lokalizacji, nigdy hasła."),
        ],
    },
    {
        "service": "views",
        "modifier": "promote",
        "slug": "youtube/wyswietlenia/promowanie",
        "label": "Promowanie filmów na YouTube",
        "title": "Wyświetlenia z AdWords na YouTube czy kampania? | Growsterr",
        "description": "Myślisz o wyświetleniach z YouTube AdWords? Promujemy Twój kanał wśród prawdziwych ludzi za Ciebie, co miesiąc, z subskrybentami, polubieniami i komentarzami.",
        "h1": ("Wyświetlenia z AdWords na YouTube? ", "Albo zostaw promocję nam."),
        "intro": "Ludzie, którzy chcą kupić wyświetlenia na YouTube przez AdWords, szukają sposobu na promocję filmu płatnym zasięgiem. Reklamy Google to jedna droga: kampania, którą sam ustawiasz, prowadzisz i opłacasz w narzędziach reklamowych Google. My jesteśmy drugą. Codziennie promujemy Twój kanał wśród prawdziwych ludzi w kampaniach w naszej sieci partnerskiej, a wyniki śledzisz w panelu.",
        "hero": {"image": "youtube-viewers", "alt": "Ludzie odkrywają promowany film na YouTube na telefonach i tabletach"},
        "sections": [
            {
                "h2": "Własne reklamy czy prowadzona kampania",
                "p": [
                    "W Google Ads, narzędziu, które zastąpiło AdWords, budujesz kampanię sam: odbiorców, stawki, budżet i samą reklamę. Płacisz w miarę, jak system wyświetla reklamę, a pilnowanie tego to Twoja praca.",
                    "Pakiet Growsterr to wersja zrobiona za Ciebie. Podajesz identyfikator kanału i docelową lokalizację; nasz zespół codziennie prowadzi promocję, a panel pokazuje wizyty na kanale i nowych subskrybentów. Jedna miesięczna cena, żadnych stawek do pilnowania.",
                ],
            },
            {
                "h2": "Do czego powinno prowadzić promowane wyświetlenie",
                "p": [
                    "Płatne wyświetlenie zwraca się tylko wtedy, gdy widz robi coś dalej: ogląda kolejny film, lajkuje, subskrybuje. Dlatego nasze pakiety są zbudowane wokół subskrybentów, z polubieniami, komentarzami i wyświetleniami od tych samych ludzi, a nie wokół liczby odtworzeń.",
                ],
                "image": {"image": "youtube-channel", "alt": "Twórca sprawdza nowych subskrybentów filmu na YouTube po starcie promocji"},
            },
            {
                "h2": "Czego nie robimy",
                "ul": [
                    "Nie ustawiamy ani nie prowadzimy Google Ads i nigdy nie prosimy o dostęp do Twojego konta Google.",
                    "Nie sprzedajemy wyświetleń na tysiące ani w cenie za wyświetlenie.",
                    "Możesz wskazać jeden film, na który mają trafiać nowi widzowie, ale nie zgrywamy promocji z godziną premiery.",
                    "Nie obiecujemy monetyzacji, godzin oglądania ani miejsca w rekomendacjach.",
                ],
            },
        ],
        "faqs": [
            ("Czy to to samo co reklamy na YouTube?", "Nie. Reklamy na YouTube działają na Twoim własnym koncie Google Ads, z Twoim budżetem i ustawieniami. My promujemy Twój kanał w naszej sieci partnerskiej i prowadzimy kampanię za Ciebie; nic nie działa na Twoim koncie."),
            ("Czy możecie prowadzić moje kampanie Google Ads?", "Tego nie oferujemy. Zajmujemy się miesięcznymi pakietami wzrostu; w sprawie czegoś większego porozmawiaj z nami na WhatsAppie albo mailem."),
            ("Czym różni się koszt od reklam?", "Reklamy naliczają opłaty w miarę wyświetlania, więc wydatki zmieniają się ze stawkami i budżetem. Nasze pakiety mają stałą miesięczną cenę, {starter_price}, {rising_price} albo {pro_price}, z typowymi zakresami subskrybentów, polubień i komentarzy."),
            ("Czy mogę w tym samym czasie prowadzić własne reklamy?", "Tak. Twoje reklamy działają na Twoim koncie, a nasza kampania w naszej sieci, więc jedno nie przeszkadza drugiemu."),
            ("Które filmy promujecie?", "Twój kanał jako całość, a nie pojedynczy film, a widzowie wybierają, co obejrzeć. Umieszczenie premiery albo nowej serii w polecanym miejscu kanału pomaga nowym odwiedzającym ją znaleźć."),
        ],
    },
    {
        "service": "views",
        "modifier": "real",
        "slug": "youtube/wyswietlenia/prawdziwe",
        "label": "Prawdziwe wyświetlenia na YouTube",
        "title": "Wyświetlenia na YouTube wysokiej jakości: od ludzi | Growsterr",
        "description": "Kup wyświetlenia na YouTube wysokiej jakości od prawdziwych ludzi, którzy sami chcą oglądać, z subskrybentami i polubieniami od tych samych widzów.",
        "h1": ("Wyświetlenia na YouTube wysokiej jakości? ", "Zacznij od człowieka za każdym odtworzeniem."),
        "intro": "Zanim kupisz wyświetlenia na YouTube wysokiej jakości, warto zdefiniować jakość. Dla nas wyświetlenie wysokiej jakości ma za sobą człowieka: kogoś, kto zobaczył Twój kanał, wybrał film i obejrzał, bo go zainteresował. Tylko takie sprowadzają nasze pakiety, a ci sami ludzie także subskrybują, lajkują i komentują.",
        "hero": {"image": "youtube-viewers", "alt": "Prawdziwy widz wybiera film do obejrzenia z kanału twórcy na YouTube"},
        "sections": [
            {
                "h2": "Co odróżnia prawdziwe wyświetlenie od odtworzenia",
                "ul": [
                    "Wybrał je człowiek: nikt nie dostał pieniędzy ani skryptu, żeby kliknąć play.",
                    "Prowadzi dalej: część widzów lajkuje, komentuje albo subskrybuje.",
                    "Ma swoje miejsce: widz mieszka tam, gdzie skierowałeś kampanię.",
                    "Wytrzymuje: nie ma w nim nic sztucznego, co YouTube mógłby usunąć.",
                ],
            },
            {
                "h2": "Dlaczego stopniowane wyświetlenia od botów to wciąż nie jakość",
                "p": [
                    "Niektórzy sprzedawcy dzielą wyświetlenia na standardowe, wysokiej jakości i premium. Jakakolwiek etykieta, pytanie, które się liczy, zostaje to samo: czy człowiek zdecydował się obejrzeć? Jeśli nie, wyższa klasa oznacza tylko wyższą cenę za to samo puste odtworzenie.",
                ],
            },
            {
                "h2": "Jakość, którą odczytasz w YouTube Studio",
                "p": [
                    "Prawdziwe wyświetlenia zostawiają ślady: czas oglądania różny u różnych widzów, komentarze, które odpowiadają na Twój film, i subskrybentów zdobytych przy filmach, które ludzie oglądali. Te ślady sprawiają, że wyświetlenie jest coś warte, i właśnie ich wygenerowane odtworzenia nigdy nie zostawiają.",
                ],
                "image": {"image": "youtube-channel", "alt": "Twórca czyta w statystykach czas oglądania i komentarze filmu na YouTube"},
            },
        ],
        "faqs": [
            ("Czym wyświetlenie wysokiej jakości różni się od taniego?", "Tanie wyświetlenie to zwykle odtworzenie, po którym nic nie następuje. Wyświetlenie wysokiej jakości to człowiek, który może polubić, skomentować, zasubskrybować albo wrócić, i tylko taki rodzaj pomaga Twojemu kanałowi."),
            ("Czy mogę zobaczyć, kim są widzowie?", "Panel pokazuje wizyty z kampanii na Twoim kanale i nowych subskrybentów, a YouTube Studio pokazuje, gdzie są widzowie i jak długo oglądają. Poszczególni widzowie pozostają anonimowi, jak na każdym kanale."),
            ("Czy wyświetlenia przychodzą bez subskrybentów albo polubień?", "Nie. Przychodzą w jednym pakiecie od tych samych ludzi i to czyni je wzrostem, a nie liczbą."),
            ("Dlaczego nie ma paczek po tysiąc wyświetleń?", "Bo tysiąc wyświetleń na zamówienie to tysiąc odtworzeń, które ktoś wygenerował. Wolimy sprowadzać ludzi i pozwolić im wybierać, co obejrzeć."),
            ("Czy mogę wybrać, gdzie mieszkają widzowie?", "Tak: podaj miejsce przy zamówieniu, od jednego miasta po cały kraj. Lokalni widzowie rozumieją Twoje filmy, i dlatego ich wyświetlenia są warte więcej niż liczba."),
        ],
    },
    {
        "service": "views",
        "modifier": "safe",
        "slug": "youtube/wyswietlenia/bezpiecznie",
        "label": "Bezpieczne wyświetlenia na YouTube",
        "title": "Bezpieczne wyświetlenia na YouTube: co chroni kanał | Growsterr",
        "description": "Chcesz kupić wyświetlenia na YouTube uczciwie i bezpiecznie? Zobacz, co YouTube uznaje za fałszywe, czym to grozi i jak trafiają do Ciebie prawdziwi widzowie.",
        "h1": ("Uczciwe wyświetlenia na YouTube? ", "Wiedz, co naraża kanał."),
        "intro": "Jeśli chcesz kupić wyświetlenia na YouTube uczciwie i bezpiecznie, zacznij od tego, przeciwko czemu YouTube działa: wyświetleniom od botów, skryptów i każdemu ruchowi, który nie jest człowiekiem decydującym się obejrzeć. Zostajemy po właściwej stronie tej granicy, bo promujemy Twój kanał wyłącznie wśród prawdziwych ludzi, którzy oglądają, jeśli chcą.",
        "hero": {"image": "youtube-channel", "alt": "Twórca w cichym domowym biurze sprawdza kondycję swojego kanału na YouTube"},
        "sections": [
            {
                "h2": "Co YouTube uznaje za fałszywe wyświetlenia",
                "p": [
                    "Zasady YouTube dotyczące fałszywego zaangażowania obejmują wszystko poniżej. YouTube może usunąć takie wyświetlenia, a treści na nich zbudowane mogą zostać zdjęte.",
                ],
                "ul": [
                    "Odtworzenia od botów albo zautomatyzowanych skryptów.",
                    "Wyświetlenia od ludzi, którym zapłacono albo dano nagrodę za oglądanie.",
                    "Filmy odtwarzane automatycznie tam, gdzie widzowie ich nie wybrali.",
                    "Wyświetlenia wymieniane między kanałami.",
                ],
            },
            {
                "h2": "Jak przychodzą nasze wyświetlenia",
                "p": [
                    "Nasza sieć partnerska prowadzi promowane kampanie, które pokazują Twój kanał prawdziwym ludziom. Nikt nie dostaje pieniędzy za oglądanie, nic nie odtwarza się bez wyboru i nic nie dotyka Twojego konta na YouTube. Ludzie, którym spodoba się to, co zobaczą, oglądają więcej, lajkują, komentują i subskrybują.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Widz wybiera na telefonie promowany film na YouTube do obejrzenia"},
            },
            {
                "h2": "Bezpieczne także dla Twojego konta",
                "ul": [
                    "Pracujemy na podstawie publicznego identyfikatora kanału: bez logowania, bez próśb o dostęp.",
                    "Płatność to miesięczna subskrypcja Stripe, którą zarządzasz na swoim koncie.",
                    "Zakończenie jej zależy od Ciebie, w dowolnym momencie, bez odpowiadania na pytania.",
                ],
            },
        ],
        "faqs": [
            ("Czy kupno wyświetleń może sprawić, że film zostanie usunięty?", "Fałszywe wyświetlenia mogą: YouTube może je wyciąć z licznika, a treści łamiące zasady dotyczące fałszywego zaangażowania mogą zostać zdjęte. Wyświetlenia od ludzi, którzy sami zdecydowali się obejrzeć, to nie fałszywe zaangażowanie."),
            ("Kto prowadzi Growsterr?", "Sterr Agency, której zarejestrowana spółka to Sterr Technologies OÜ w Tallinnie w Estonii. Siedziba główna zespołu jest w Turcji."),
            ("Czy potrzebujecie mojego logowania do YouTube albo Google?", "Nie, a serwis, który o nie prosi, sam w sobie jest ryzykiem. Potrzebujemy tylko publicznego identyfikatora kanału."),
            ("Czy promowanie filmu jest na YouTube dozwolone?", "Promowanie filmu, żeby ludzie mogli go odkryć, to nic nadzwyczajnego; kanały robią to reklamami każdego dnia. YouTube stawia granicę przy sztucznych albo nagradzanych wyświetleniach, a my jesteśmy po właściwej stronie."),
            ("Co, jeśli nie będę zadowolony?", "Zatrzymaj subskrypcję na swoim koncie, a za kolejny miesiąc nic nie zostanie pobrane. Panel pokazuje, co zmierzyliśmy, więc możesz ocenić kampanię na podstawie faktów."),
        ],
    },
    {
        "service": "views",
        "modifier": "shorts",
        "slug": "youtube/wyswietlenia/shorts",
        "label": "Wyświetlenia YouTube Shorts",
        "title": "Wyświetlenia rolek na YouTube? To Shorts | Growsterr",
        "description": "Na YouTube rolki nazywają się Shorts. Sprowadzamy prawdziwych widzów, którzy oglądają Twoje Shorts dalej, w miesięcznym pakiecie z subskrybentami. Od {from_price}.",
        "h1": ("Wyświetlenia rolek na YouTube? ", "Zdobądź widzów Shorts, którzy oglądają dalej."),
        "intro": "Jeśli chcesz kupić wyświetlenia rolek na YouTube, chodzi Ci o Shorts: krótkie pionowe filmy na YouTube. Nie sprzedajemy wyświetleń Shorts hurtem. Codziennie sprowadzamy na Twój kanał prawdziwych ludzi, a ci, którym podobają się Twoje Shorts, oglądają, puszczają ponownie, lajkują i czasem subskrybują.",
        "hero": {"image": "youtube-viewers", "alt": "Ktoś ogląda YouTube Short na telefonie i pozwala mu lecieć w pętli"},
        "sections": [
            {
                "h2": "Tanie wyświetlenia Shorts łatwo podrobić i łatwo rozpoznać",
                "p": [
                    "Tanie wyświetlenia Shorts są wszędzie, bo wygenerowanie odtworzenia zajmuje sekundy. Trudna część zaczyna się po odtworzeniu: czy widz oglądał dalej, puścił ponownie, polubił, otworzył Twój kanał? Wygenerowane odtworzenia na wszystko odpowiadają „nie”, a YouTube traktuje je jak spam.",
                ],
            },
            {
                "h2": "Jak widz Shorts zostaje subskrybentem",
                "p": [
                    "Shorts to drzwi wejściowe. Prawdziwy widz, któremu spodoba się jeden, może stuknąć w Twoją nazwę, rozejrzeć się po kanale i zasubskrybować, a od tej chwili mogą do niego trafiać też Twoje dłuższe filmy. Ta ścieżka sprawia, że wyświetlenie Shorta od człowieka jest warte o wiele więcej niż odtworzenie.",
                ],
                "image": {"image": "youtube-channel", "alt": "Twórca przegląda na telefonie pionowego YouTube Shorta przed publikacją"},
            },
            {
                "h2": "Jak wycisnąć więcej z publikowanych Shorts",
                "ul": [
                    "Niech najlepsze Shorts będą łatwe do znalezienia na stronie kanału, gdzie lądują ciekawscy widzowie.",
                    "Podlinkuj w Shorcie powiązany długi film, żeby zainteresowani mieli dokąd pójść.",
                    "Publikuj w stałym rytmie, żeby nowi subskrybenci przy każdej wizycie znajdowali coś świeżego.",
                ],
            },
        ],
        "faqs": [
            ("Czy rolki na YouTube to to samo co Shorts?", "Tak. Rolki to nazwa z Instagrama; na YouTube ten sam krótki pionowy format nazywa się Shorts. Wszystko na tej stronie dotyczy Shorts."),
            ("Czy mogę kupić tanie wyświetlenia pod jednego Shorta?", "Nie ma ceny za Shorta i nie kierujemy wyświetleń na pojedynczego Shorta. Pakiet promuje Twój kanał, a widzowie wybierają Shorts, które chcą obejrzeć."),
            ("Czy możecie wprowadzić moje Shorts do kanału Shorts?", "Tej obietnicy nikt uczciwie nie złoży, więc jej nie składamy. Sprowadzamy prawdziwych widzów; jak YouTube rozpowszechni potem Shorta, to jego własna decyzja."),
            ("Dlaczego nie podajecie liczby wyświetleń Shorts?", "Shorta można puścić ponownie, pominąć albo zapętlić, a liczbę wyświetleń obiecaną z góry da się spełnić tylko generowaniem odtworzeń. Podajemy typowe miesięczne zakresy tego, co ludzie robią po obejrzeniu: subskrybują, lajkują i komentują."),
            ("Czy kupowanie wyświetleń YouTube Shorts jest bezpieczne?", "Od serwisu z botami nie: fałszywe odtworzenie jest fałszywe, czy film trwa trzydzieści sekund, czy godzinę. Prawdziwi widzowie wybierający Twoje Shorts to zwykła publiczność, w jakimkolwiek formacie publikujesz."),
        ],
    },
]
