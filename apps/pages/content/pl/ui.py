"""Polish UI of the money pages (mirrors en/ui.py key by key).

Word forms the strings below are built around:
    {audience} nominative plural (obserwujący / subskrybenci)
    {follow} infinitive with its object (Cię obserwować / subskrybować)
    {profile} nominative = accusative (profil / kanał)
    {handle} accusative (nazwę użytkownika / identyfikator kanału)
    {content} nominative = accusative plural (posty / filmy)
    {service} the counting form after a number (obserwujących, polubień...)
"""

UI = {
    # Words that change with the platform or the service
    "audience": {"instagram": "obserwujący", "tiktok": "obserwujący", "youtube": "subskrybenci"},
    "follow": {"instagram": "Cię obserwować", "tiktok": "Cię obserwować", "youtube": "subskrybować"},
    "profile": {"instagram": "profil", "tiktok": "profil", "youtube": "kanał"},
    "handle": {"instagram": "nazwę użytkownika", "tiktok": "nazwę użytkownika", "youtube": "identyfikator kanału"},
    "content": {"instagram": "posty", "tiktok": "filmy", "youtube": "filmy"},
    "service_names": {"followers": "Obserwujący", "subscribers": "Subskrybenci", "likes": "Polubienia",
                      "views": "Wyświetlenia", "comments": "Komentarze"},
    "service_words": {"followers": "obserwujących", "subscribers": "subskrybentów", "likes": "polubień",
                      "views": "wyświetleń", "comments": "komentarzy"},

    # Page chrome
    "home": "Strona główna",
    "crumbs_label": "Ścieżka nawigacji",
    "eyebrow": "{platform} · {service_name}",
    "eyebrow_hub": "{platform}: prawdziwy wzrost",
    "cta": "Zacznij od {pick_name}",
    "cta_more": "Zobacz wszystkie pakiety",
    "trust": ["Prawdziwi ludzie, nigdy boty", "Nigdy nie prosimy o hasło", "Co miesiąc, rezygnujesz, kiedy chcesz"],
    "product_name": "{platform}: pakiety wzrostu",
    "sticky_cta": "Zacznij",

    # Packages
    "packages_title": "Wybierz pakiet",
    "packages_lead": "Trzy pakiety miesięczne. Nowi {audience}, polubienia, wyświetlenia i komentarze przychodzą razem, od tych samych prawdziwych ludzi.",
    "packages_note": "Typowe miesięczne zakresy, a nie stała liczba: wszyscy Twoi nowi {audience} to prawdziwi ludzie, którzy sami zdecydowali się {follow}, więc każdy miesiąc wygląda trochę inaczej.",

    # What's included: the page's own service comes first, then the rest in this order.
    "included_title": "Co zawiera pakiet",
    "included_lead": "Każdy pakiet to pełny obraz, od tych samych prawdziwych ludzi.",
    "included_items": {
        "audience": ("Nowi {audience}", "Prawdziwi ludzie, którzy odkryli Twój {profile} i zdecydowali się {follow}. Zwykle {starter_audience} miesięcznie w pakiecie {starter_name}."),
        "likes": ("Polubienia od tych samych ludzi", "Zwykle {starter_likes} miesięcznie w pakiecie {starter_name}. Ludzie lajkują te {content}, które naprawdę im się podobają."),
        "comments": ("Komentarze ich własnymi słowami", "Zwykle {starter_comments} miesięcznie w pakiecie {starter_name}. Piszą je ludzie, nigdy gotowe skrypty."),
        "views": ("Wyświetlenia w komplecie", "Ci sami ludzie sami oglądają Twoje {content}. Nie liczymy wyświetleń z góry: za każdym stoi człowiek."),
        "days": ("Rozłożone na 30 dni", "Trochę każdego dnia, z wybranej przez Ciebie lokalizacji. Nigdy wszystko naraz."),
        "dashboard": ("Twój panel", "Co zmierzyliśmy, dzień po dniu: wizyty z Twojej kampanii i nowi {audience}, których przyprowadziły."),
    },

    # How it works: the subscription, step by step
    "steps_title": "Jak to działa",
    "steps_lead": "Miesięczna subskrypcja: Ty wybierasz pakiet, my prowadzimy kampanię, a prawdziwi ludzie decydują.",
    "steps": [
        ("Wybierz pakiet", "{starter_name}, {rising_name} lub {pro_name}, płatność co miesiąc. Anulujesz w dowolnym momencie na swoim koncie."),
        ("Uruchamiamy Twoją kampanię", "Podaj {handle} w serwisie {platform} i miejsce, z którego mają pochodzić Twoi odbiorcy. Nigdy nie prosimy o hasło."),
        ("Prawdziwi ludzie odkrywają Twój {profile}", "Codziennie pokazujemy Twój {profile} prawdziwym ludziom. Komu spodoba się to, co zobaczy, ten sam decyduje się {follow}, polubić i skomentować."),
        ("Panel pokazuje, co zmierzyliśmy", "Wizyty z Twojej kampanii i nowi {audience}, których przyniosły, dzień po dniu. Zmierzone liczby, nigdy domysły."),
    ],

    # Real people vs bots / instant
    "compare_title": "Prawdziwi ludzie, nie boty",
    "compare_lead": "„Natychmiast” znaczy boty: żadna prawdziwa osoba nie decyduje się {follow} kilka sekund po płatności.",
    "compare_cols": ("Co się zmienia", "Usługi „natychmiast” i boty", "Growsterr"),
    "compare": [
        ("Kim są", "Boty i fałszywe profile", "Prawdziwi ludzie, którzy sami zdecydowali się {follow}"),
        ("Tempo", "Tysiące w kilka minut", "Trochę każdego dnia, przez cały miesiąc"),
        ("Polubienia i komentarze", "Sprzedawane osobno, od kolejnych botów", "Od tych samych ludzi, w ramach pakietu"),
        ("Twój zasięg", "Spada po cichu: odbiorcy, którzy nigdy nie reagują, to dla algorytmu {platform} sygnał, że Twoje {content} nie są warte pokazywania", "Rośnie dzięki ludziom, którzy oglądają, lajkują i wracają"),
        ("Twoje hasło", "Często wymagane", "Nigdy"),
        ("Co widzisz", "Liczba, która może zniknąć przy kolejnej czystce", "Panel z tym, co zmierzyliśmy"),
    ],

    # Quantity pages: how a monthly package gets you to the goal
    "quantity_title": "Jak dojść do {quantity} {service}",
    "quantity_lead": "Nie sprzedajemy gotowej paczki „{quantity}”. Prawdziwi ludzie decydują sami, więc miesięczny pakiet prowadzi Cię do celu w naturalnym tempie.",
    "pace_title": "Typowe tempo z pakietem {pick_name}",
    "pace_month": "Miesiąc {n}",
    "pace_goal": "Cel: {quantity}",
    "pace_note": "Typowe zakresy oparte na tym, co robią prawdziwi ludzie, nigdy obietnica. Jedne miesiące przynoszą więcej, inne mniej.",
    "by_plan_title": "Czas dojścia do {quantity} według pakietu",
    "a_month": "{range} miesięcznie",
    "when_first": "zwykle już w pierwszym miesiącu",
    "when_about": "zwykle około {n} mies.",
    "when_range": "zwykle {low}–{high} mies.",
    "views_pace": "Wyświetlenia pochodzą od tych samych prawdziwych ludzi, którzy odkrywają Twój {profile}, więc nie liczymy ich z góry. {pick_name} to pakiet, który najlepiej pasuje do tego celu.",

    # FAQ, related pages, closing
    "faq_title": "Pytania i odpowiedzi",
    "related_title": "Zobacz też",
    "related": {
        "platform": "Więcej w serwisie {platform}",
        "platforms": "Na innych platformach",
        "quantities": "Inne cele",
        "modifiers": "Inne sposoby na wzrost",
        "articles": "Czytaj dalej",
        "hubs": "Rośnij z prawdziwymi ludźmi:",
    },
    # The tools a page can carry ("tool"): they run in the browser, nothing is sent.
    "tools": {
        "calculate": "Oblicz",
        "followers": "Obserwujący",
        "avg_likes": "Średnia liczba polubień na post",
        "avg_comments": "Średnia liczba komentarzy na post",
        "engagement_title": "Twój wskaźnik zaangażowania",
        "engagement_lead": "Jaka część Twoich obserwujących reaguje na typowy post. Wpisz liczby z kilku ostatnich postów.",
        "engagement_result": "Twój wskaźnik zaangażowania wynosi {rate}%.",
        "engagement_note": "Wskaźnik rośnie, gdy osoby, które Cię obserwują, naprawdę interesują się Twoimi postami. Obserwujący, którzy nigdy nie reagują, obniżają go bez względu na to, ilu ich jest.",
        "growth_title": "Ile czasu do Twojego celu?",
        "growth_lead": "Wpisz, gdzie jesteś i dokąd chcesz dojść. Liczymy to na podstawie typowego miesięcznego zakresu każdego pakietu.",
        "current": "Obserwujący dziś",
        "goal": "Twój cel",
        "when_first": "zwykle już w pierwszym miesiącu",
        "when_range": "zwykle {low}–{high} mies.",
        "when_about": "około {n} mies.",
        "reached": "Już tam jesteś.",
        "growth_note": "Typowe zakresy, nie obietnica: prawdziwi ludzie sami decydują, czy Cię obserwować.",
    },
    # Eyebrow above the headline of pages outside the platform x service grid (by "kind").
    "article_eyebrows": {
        "guide": "Poradnik",
        "alternative": "Porównanie",
        "payment": "Płatności",
        "agency": "Agencja wzrostu",
        "tool": "Narzędzie",
        "intent": "Prosta odpowiedź",
    },
    "cta_title": "Pora na prawdziwy wzrost w serwisie {platform}",
    "cta_text": "Wybierz pakiet, a my uruchomimy Twoją kampanię. O reszcie decydują prawdziwi ludzie, a Twój panel pokazuje, co zmierzyliśmy.",

    # Platform hubs
    "services_title": "Co rozwijamy w serwisie {platform}",
    "services_lead": "Jeden pakiet daje to wszystko, od tych samych prawdziwych ludzi.",
    "teasers": {
        "audience": "Prawdziwi ludzie, którzy odkrywają Twój {profile} i decydują się {follow}.",
        "likes": "Polubienia od ludzi, którym podobają się Twoje {content}.",
        "views": "Wyświetlenia od ludzi, którzy sami chcą oglądać, nigdy od skryptów.",
        "comments": "Komentarze pisane przez prawdziwych ludzi, ich własnymi słowami.",
    },
    "explore": "Zobacz",
    "in_package": "W każdym pakiecie",
    "goals_title": "Więcej sposobów na wzrost w serwisie {platform}",
    "other_hubs_title": "Rozwijamy też",
}
