"""Slovak Instagram pages: the hub, followers, and the 1,000-followers goal. Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-08"

PAGES = [
    {
        # The hub: no service.
        "slug": "instagram",
        "label": "Instagram",
        "title": "Balíky rastu na Instagrame pre tvorcov | Growsterr",
        "description": "Rastite na Instagrame so skutočnými ľuďmi: mesačné balíky prinášajú sledovateľov, lajky a komentáre od ľudí, ktorí vás chcú sledovať. Od {from_price} mesačne.",
        "h1": ("Rastite na Instagrame ", "so skutočnými ľuďmi."),
        "intro": "Mesačné balíky rastu pre tvorcov a influencerov. Váš profil ukazujeme skutočným ľuďom a tí, ktorým sa páči, čo vidia, vás začnú sledovať, dávajú lajky a komentujú. Váš prehľad ukazuje, čo sme namerali, deň po dni.",
        "hero": {"image": "instagram-hub", "alt": "Profil tvorcu na Instagrame, kam prichádzajú noví sledovatelia, lajky a komentáre"},
        "sections": [
            {
                "h2": "Rast, ktorý pôsobí zaslúžene",
                "p": [
                    "Instagram odmeňuje účty, na ktoré ľudia skutočne reagujú. Boty robia opak: sedia vo vašom počte sledovateľov, nikdy nedajú lajk, nič nepozerajú a učia algoritmus, že vaše príspevky nestoja za zobrazenie.",
                    "My postupujeme opačne. Váš profil sa každý deň zobrazuje skutočným ľuďom a každé sledovanie je niečí slobodný výber. Preto lajky, zhliadnutia a komentáre prichádzajú spolu so sledovateľmi, nie ako samostatný nákup.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Skutoční ľudia objavujú príspevky tvorcu na Instagrame a píšu komentáre"},
            },
            {
                "h2": "Pre tvorcov, ktorí uverejňujú s jasným zámerom",
                "p": [
                    "Osobná značka, tematická stránka alebo malý podnik: balíky rastú s vami. Začnite s balíkom {starter_name} a na vyšší prejdite, keď bude váš obsah pripravený na viac.",
                ],
                "ul": [
                    "Pomôže to reels, karuselom aj fotkám.",
                    "Poviete nám mesto, región alebo krajinu, odkiaľ má pochádzať vaše publikum.",
                    "Váš účet zostáva váš: nikdy nežiadame vaše heslo.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "Tvorca pri pracovnom stole plánuje obsah pre Instagram"},
            },
        ],
        "faqs": [
            ("Sú sledovatelia skutoční ľudia?", "Áno. Každý sledovateľ je skutočný človek, ktorý videl váš profil a rozhodol sa vás sledovať. Nikdy nepoužívame boty, falošné profily ani okamžité doručenie."),
            ("Koľko sledovateľov balík prinesie?", "S balíkom {starter_name} typicky {starter_audience} nových sledovateľov mesačne, s {rising_name} {rising_audience} a s {pro_name} {pro_audience}. Sú to typické rozpätia, nie pevný počet: skutoční ľudia sa rozhodujú sami."),
            ("Potrebujete moje heslo k Instagramu?", "Nikdy. Stačí nám vaše používateľské meno. Nechajte účet verejný, aby vás ľudia, ktorí ho objavia, mohli sledovať."),
            ("Môžem si kúpiť lajky alebo komentáre samostatne?", "Nie. Lajky, zhliadnutia a komentáre sú súčasťou každého balíka, od tých istých skutočných ľudí, ktorí vás sledujú. Práve vďaka tomu zostávajú vaše čísla prirodzené."),
            ("Môžem kedykoľvek zrušiť?", "Áno. Balíky sa obnovujú mesačne a zrušiť ich môžete vo svojom účte. Zaplatený mesiac dobehne do konca."),
        ],
    },
    {
        "service": "followers",
        "slug": "instagram/sledovatelia",
        "label": "Sledovatelia na Instagrame",
        "title": "Skutoční sledovatelia na Instagrame, každý mesiac | Growsterr",
        "description": "Sledovatelia na Instagrame, ktorí sú skutoční ľudia a sami sa rozhodli vás sledovať, s lajkami a komentármi od tých istých ľudí. Balíky od {from_price} mesačne.",
        "h1": ("Sledovatelia na Instagrame, ", "ktorí sa rozhodli sledovať práve vás."),
        "intro": "Skutoční ľudia každý deň objavujú váš profil a tí, ktorým sa páči, čo vidia, vás začnú sledovať. S balíkom {starter_name} typicky {starter_audience} nových sledovateľov mesačne, s lajkami a komentármi od tých istých ľudí.",
        "hero": {"image": "instagram-followers", "alt": "Profil na Instagrame, ktorý začínajú sledovať noví skutoční ľudia"},
        "sections": [
            {
                "h2": "Prečo majú skutoční sledovatelia väčšiu hodnotu",
                "p": [
                    "Sledovateľ sa počíta, len ak je za ním človek. Skutoční sledovatelia uvidia váš ďalší príspevok, dajú mu lajk, okomentujú ho a zdieľajú, a práve na túto angažovanosť sa Instagram pozerá, keď rozhoduje, komu ešte váš obsah ukáže.",
                    "Boty nič z toho nedokážu. Na pár dní zdvihnú číslo, zmiznú pri ďalšom čistení a tie, ktoré zostanú, vám potichu znižujú dosah.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Skutoční ľudia dávajú lajky a komentujú príspevok tvorcu na Instagrame"},
            },
            {
                "h2": "Odkiaľ prichádzajú vaši noví sledovatelia",
                "p": [
                    "Povedzte nám mesto, región alebo krajinu, odkiaľ má pochádzať vaše publikum. Váš profil ukazujeme najprv skutočným ľuďom tam; kde je najlepšie zodpovedajúce publikum väčšie, viac ľudí môže prísť z okolia.",
                ],
            },
            {
                "h2": "Ako vyzerá jeden mesiac",
                "ul": [
                    "Prvé dni: vaša kampaň sa spustí a prichádzajú prvé návštevy.",
                    "Každý týždeň: noví sledovatelia, lajky a komentáre, každý deň niekoľko.",
                    "Na konci mesiaca: s balíkom {pick_name} typicky {pick_audience} nových sledovateľov.",
                ],
            },
        ],
        "faqs": [
            ("Ako rýchlo sledovatelia prichádzajú?", "Každý deň trochu, počas celého mesiaca. Nikdy nie všetci naraz: skutoční ľudia sledujú vlastným tempom a všetko okamžité je bot."),
            ("Prestanú ma noví sledovatelia sledovať?", "Niektorí možno áno, tak ako sa mení každé skutočné publikum. Skutoční sledovatelia však zostávajú oveľa častejšie ako boty, ktoré miznú vo vlnách."),
            ("Dostanem aj lajky a komentáre?", "Áno, od tých istých ľudí: s balíkom {pick_name} typicky {pick_likes} lajkov a {pick_comments} komentárov mesačne."),
            ("Je to pre môj účet bezpečné?", "Nikdy nežiadame vaše heslo a nikdy sa do vášho účtu neprihlasujeme. Ľudia nájdu váš profil a rozhodnú sa sami, tak ako vás nájde ktorýkoľvek sledovateľ."),
            ("Môžem si vybrať, odkiaľ budú moji sledovatelia?", "Áno. Pri objednávke nám napíšte mesto, región alebo krajinu. Mierime najprv tam; keď je v okolí väčšie veľmi podobné publikum, časť sledovateľov môže prísť odtiaľ."),
        ],
    },
    {
        "service": "followers",
        "quantity": 1000,
        "slug": "instagram/sledovatelia/1000",
        "label": "{quantity} sledovateľov na Instagrame",
        "title": "{quantity} skutočných sledovateľov na Instagrame | Growsterr",
        "description": "Dosiahnite {quantity} sledovateľov na Instagrame so skutočnými ľuďmi, nie botmi. {pick_name} typicky prinesie {pick_audience} mesačne, aj s lajkami a komentármi.",
        "h1": ("{quantity} sledovateľov na Instagrame, ", "každý z nich skutočný."),
        "intro": "Nepredávame balík {quantity} botov. Váš účet rozvíjame so skutočnými ľuďmi: {pick_name} typicky prinesie {pick_audience} nových sledovateľov mesačne, takže {quantity} je zvyčajne na dosah už v prvom mesiaci.",
        "hero": {"image": "instagram-followers-1000", "alt": "Stúpajúca krivka nových sledovateľov na Instagrame dosahuje prvý míľnik"},
        "sections": [
            {
                "h2": "Prečo nie {quantity} sledovateľov za hodinu?",
                "p": [
                    "Pretože žiadny skutočný človek nezačne sledovať účet pár sekúnd po platbe. Služby, ktoré dodajú {quantity} sledovateľov za hodinu, dodávajú boty: nedávajú lajky, nekomentujú a miznú vo vlnách.",
                    "Tie, ktoré zostanú, napáchajú ešte viac škody. Každý sledovateľ, ktorý nikdy nereaguje, znižuje podiel publika, ktoré reaguje, a vaše príspevky sa potichu dostanú k menšiemu počtu ľudí.",
                ],
            },
            {
                "h2": "Vaša prvá tisícka, poriadne",
                "p": [
                    "Prvá tisícka skutočných sledovateľov mení to, ako vás vnímajú noví návštevníci. Sú to ľudia, ktorí si môžu pozrieť vaše reels, lajknúť vaše príspevky a vrátiť sa, a presne to pomáha, aby vás našla ďalšia tisícka.",
                ],
                "ul": [
                    "Skutoční ľudia, ktorí sa rozhodli vás sledovať, z lokality, ktorú si vyberiete.",
                    "Lajky a komentáre od tých istých ľudí, v rámci balíka.",
                    "Prehľad, ktorý ukazuje, čo sme namerali, deň po dni.",
                ],
            },
        ],
        "faqs": [
            ("Za ako dlho získam {quantity} skutočných sledovateľov?", "Pri typickom tempe prinesie {pick_name} {pick_audience} nových sledovateľov mesačne, takže {quantity} je zvyčajne na dosah už v prvom mesiaci. Skutoční ľudia sledujú vlastným tempom, preto je každý mesiac trochu iný."),
            ("Je to jednorazový balík {quantity} sledovateľov?", "Nie. Rast predávame ako mesačné balíky. {pick_name} stojí {pick_price} mesačne a zrušiť ho môžete kedykoľvek vo svojom účte."),
            ("Dostanem s nimi aj lajky a komentáre?", "Áno, od tých istých skutočných ľudí: s balíkom {pick_name} typicky {pick_likes} lajkov a {pick_comments} komentárov mesačne."),
            ("Čo bude po dosiahnutí {quantity}?", "Váš balík beží, kým ho nezrušíte, takže rast pokračuje mesiac za mesiacom. Keď bude váš obsah pripravený na viac, môžete prejsť na vyšší balík."),
        ],
    },
]
