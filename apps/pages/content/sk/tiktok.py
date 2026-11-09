"""Slovak TikTok pages: the hub and likes. Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "tiktok",
        "label": "TikTok",
        "title": "Balíky rastu na TikToku pre tvorcov | Growsterr",
        "description": "Rastite na TikToku so skutočnými ľuďmi: mesačné balíky prinášajú sledovateľov, lajky a komentáre od ľudí, ktorí vás chcú sledovať. Od {from_price} mesačne.",
        "h1": ("Rastite na TikToku ", "so skutočnými ľuďmi."),
        "intro": "Mesačné balíky rastu pre tvorcov a influencerov. Skutoční ľudia objavia váš profil, pozrú si vaše videá a keď sa im páči, čo vidia, začnú vás sledovať. Váš prehľad ukazuje, čo sme namerali, deň po dni.",
        "hero": {"image": "tiktok-hub", "alt": "Profil tvorcu na TikToku, kam prichádzajú noví sledovatelia a lajky"},
        "sections": [
            {
                "h2": "Na TikToku je pozornosť všetko",
                "p": [
                    "TikTok ukáže video ďalším ľuďom, keď ho prví diváci dopozerajú, dajú mu lajk, okomentujú ho a začnú sledovať autora. Čísla bez ľudí za nimi nič z toho nepohnú.",
                    "Naše balíky privádzajú na váš profil skutočných ľudí každý deň. Pozerajú, rozhodujú sa a tí, ktorých vaše videá bavia, vás začnú sledovať a dávajú lajky. Presne taká pozornosť pomáha videu dostať sa ďalej.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Skutoční diváci pozerajú videá tvorcu na TikToku"},
            },
            {
                "h2": "Pre tvorcov, ktorí majú čo povedať",
                "p": [
                    "Humor, varenie, móda či návody: ak uverejňujete pravidelne, skutoční diváci dajú každému novému videu lepší štart. Začnite s balíkom {starter_name} a na vyšší prejdite, keď budete pripravení.",
                ],
                "ul": [
                    "Poviete nám mesto, región alebo krajinu, odkiaľ má pochádzať vaše publikum.",
                    "Sledovatelia, lajky a komentáre prichádzajú spolu, od tých istých ľudí.",
                    "Váš účet zostáva váš: nikdy nežiadame vaše heslo.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Tvorca natáča video na TikTok s telefónom na statíve"},
            },
        ],
        "faqs": [
            ("Sú sledovatelia skutoční ľudia?", "Áno. Každý sledovateľ je skutočný človek, ktorý videl váš profil a rozhodol sa vás sledovať. Nikdy nepoužívame boty, falošné účty ani okamžité doručenie."),
            ("Koľko sledovateľov balík prinesie?", "S balíkom {starter_name} typicky {starter_audience} nových sledovateľov mesačne, s {rising_name} {rising_audience} a s {pro_name} {pro_audience}. Typické rozpätia, nie pevný počet: skutoční ľudia sa rozhodujú sami."),
            ("Potrebujete moje heslo k TikToku?", "Nikdy. Stačí nám vaše používateľské meno. Nechajte účet verejný, aby vás ľudia, ktorí ho objavia, mohli sledovať."),
            ("Môžem si kúpiť zhliadnutia alebo lajky samostatne?", "Nie. Zhliadnutia, lajky a komentáre sú súčasťou každého balíka, od tých istých skutočných ľudí, ktorí vás sledujú."),
            ("Môžem kedykoľvek zrušiť?", "Áno. Balíky sa obnovujú mesačne a zrušiť ich môžete vo svojom účte. Zaplatený mesiac dobehne do konca."),
        ],
    },
    {
        "service": "likes",
        "slug": "tiktok/lajky",
        "label": "Lajky na TikToku",
        "title": "Lajky na TikToku od skutočných ľudí, v každom balíku",
        "description": "Lajky na TikToku od skutočných ľudí, ktorí pozerajú vaše videá, nie od botov. Sú v každom mesačnom balíku so sledovateľmi a komentármi. Od {from_price} mesačne.",
        "h1": ("Lajky na TikToku od skutočných ľudí. ", "V každom balíku."),
        "intro": "Lajky samostatne nepredávame. Každý balík prináša skutočných ľudí, ktorí objavia váš profil, pozerajú vaše videá a lajkujú to, čo ich baví: s balíkom {starter_name} typicky {starter_likes} lajkov mesačne.",
        "hero": {"image": "tiktok-likes", "alt": "Lajky od skutočných divákov pod videom na TikToku"},
        "sections": [
            {
                "h2": "Prečo sa lajk počíta, len keď je za ním človek",
                "p": [
                    "TikTok sleduje, čo sa okolo lajku deje: pozeral divák ďalej, začal sledovať autora, vrátil sa? Lajky od botov na všetko odpovedajú nie, takže pridajú číslo a uberú dosah.",
                    "Lajky od skutočných ľudí prichádzajú so všetkým ostatným: s časom pozerania, sledovaniami a komentármi. To je signál, ktorý pomáha videu dostať sa ďalej.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Diváci pozerajú video na TikToku až do konca a dávajú mu lajk"},
            },
            {
                "h2": "Koľko lajkov prinesie každý balík",
                "ul": [
                    "{starter_name} ({starter_price} mesačne): typicky {starter_likes} lajkov.",
                    "{rising_name} ({rising_price} mesačne): typicky {rising_likes} lajkov, na videá, ktoré si vyberiete.",
                    "{pro_name} ({pro_price} mesačne): typicky {pro_likes} lajkov, s prednostným zaradením.",
                ],
            },
            {
                "h2": "Prečo lajky nepredávame samostatne",
                "p": [
                    "Lajky, ktoré prídu bez zhliadnutí, sledovaní a komentárov, vyzerajú presne tak, akými sú. V balíku pochádza každý lajk od niekoho, kto video videl, takže vaše čísla sa hýbu spolu, tak ako pri skutočnom raste.",
                ],
            },
        ],
        "faqs": [
            ("Môžem dostať lajky na TikToku bez balíka?", "Nie. Lajky, zhliadnutia a komentáre prichádzajú len v rámci našich mesačných balíkov, od tých istých skutočných ľudí. Vďaka tomu zostávajú prirodzené."),
            ("Ktoré videá dostanú lajky?", "Skutoční ľudia lajkujú to, čo ich baví, zvyčajne vaše najnovšie videá. S balíkmi {rising_name} a {pro_name} si môžete vybrať, ktoré videá dostanú pozornosť."),
            ("Ako rýchlo lajky prichádzajú?", "Každý deň trochu, počas celého mesiaca. Nikdy nie okamžite: okamžitý lajk je bot."),
            ("Potrebujete moje heslo k TikToku?", "Nikdy. Stačí nám vaše používateľské meno a váš účet by mal byť verejný."),
        ],
    },
]
