"""Czech Instagram pages: the hub, followers, and the 1,000-followers goal.
Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-08"

PAGES = [
    {
        # The hub: no service.
        "slug": "instagram",
        "label": "Instagram",
        "title": "Balíčky růstu na Instagramu pro tvůrce | Growsterr",
        "description": "Rosťte na Instagramu se skutečnými lidmi: měsíční balíčky přinášejí nové sledující, lajky a komentáře od lidí, kteří vás chtějí sledovat. Od {from_price} měsíčně.",
        "h1": ("Rosťte na Instagramu ", "se skutečnými lidmi."),
        "intro": "Měsíční balíčky růstu pro tvůrce a influencery. Váš profil ukazujeme skutečným lidem a ti, kterým se líbí, co vidí, vás začnou sledovat, dávají lajky a komentují. V přehledu uvidíte, co jsme naměřili, den po dni.",
        "hero": {"image": "instagram-hub", "alt": "Instagramový profil tvůrce, kterému přibývají noví sledující, lajky a komentáře"},
        "sections": [
            {
                "h2": "Růst, který vypadá zaslouženě",
                "p": [
                    "Instagram odměňuje účty, na které lidé opravdu reagují. Boti dělají opak: sedí ve vašem počtu sledujících, nikdy nedají lajk, nic nezhlédnou a učí algoritmus, že vaše příspěvky nestojí za zobrazení.",
                    "My na to jdeme obráceně. Váš profil se každý den ukazuje skutečným lidem a každé sledování je něčí vlastní rozhodnutí. Proto lajky, zhlédnutí a komentáře přicházejí spolu se sledujícími, a ne jako samostatný nákup.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Skuteční lidé objevují instagramové příspěvky tvůrce a píšou komentáře"},
            },
            {
                "h2": "Pro tvůrce, kteří publikují s rozmyslem",
                "p": [
                    "Osobní značka, tematický profil nebo malá firma: balíčky rostou s vámi. Začněte s balíčkem {starter_name} a přejděte výš, až bude váš obsah připravený na víc.",
                ],
                "ul": [
                    "Prospívá to reels, karuselům i fotkám.",
                    "Řeknete nám město, region nebo zemi, odkud má vaše publikum přicházet.",
                    "Účet zůstává váš: heslo po vás nikdy nechceme.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "Tvůrce u psacího stolu plánuje obsah na Instagram"},
            },
        ],
        "faqs": [
            ("Jsou sledující skuteční lidé?", "Ano. Každý sledující je skutečný člověk, který viděl váš profil a rozhodl se vás sledovat. Nikdy nepoužíváme boty, falešné profily ani okamžité doručení."),
            ("Kolik sledujících balíček přinese?", "{starter_name} obvykle přinese {starter_audience} nových sledujících měsíčně, {rising_name} {rising_audience} a {pro_name} {pro_audience}. Jde o typická rozpětí, ne o pevný počet: skuteční lidé se rozhodují sami."),
            ("Potřebujete moje heslo k Instagramu?", "Nikdy. Stačí nám vaše uživatelské jméno. Nechte účet veřejný, aby vás lidé, kteří ho objeví, mohli sledovat."),
            ("Můžu si koupit lajky nebo komentáře samostatně?", "Ne. Lajky, zhlédnutí a komentáře jsou součástí každého balíčku a přicházejí od stejných skutečných lidí, kteří vás sledují. Díky tomu vaše čísla zůstávají přirozená."),
            ("Můžu předplatné kdykoli zrušit?", "Ano. Balíčky se obnovují měsíčně a zrušit je můžete ve svém účtu. Zaplacený měsíc doběhne do konce."),
        ],
    },
    {
        "service": "followers",
        "slug": "instagram/sledujici",
        "label": "Sledující na Instagramu",
        "title": "Skuteční sledující na Instagramu každý měsíc | Growsterr",
        "description": "Sledující na Instagramu, kteří jsou skuteční lidé a sami se rozhodli vás sledovat, s lajky a komentáři od stejných lidí. Měsíční balíčky od {from_price}.",
        "h1": ("Sledující na Instagramu, ", "kteří si vás sami vybrali."),
        "intro": "Skuteční lidé každý den objevují váš profil a ti, kterým se líbí, co vidí, vás začnou sledovat. S balíčkem {starter_name} obvykle {starter_audience} nových sledujících měsíčně, s lajky a komentáři od stejných lidí.",
        "hero": {"image": "instagram-followers", "alt": "Instagramový profil, kterému přibývají noví sledující, skuteční lidé"},
        "sections": [
            {
                "h2": "Proč mají skuteční sledující větší hodnotu",
                "p": [
                    "Sledující má smysl jen tehdy, když za ním stojí člověk. Skuteční sledující uvidí váš další příspěvek, dají mu lajk, okomentují ho a sdílejí, a právě na toto zapojení se Instagram dívá, když rozhoduje, komu váš obsah ukáže dál.",
                    "Boti nic z toho nedokážou. Na pár dní zvednou číslo, při příští čistce zmizí a ti, kteří zůstanou, vám potichu snižují dosah.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Skuteční lidé dávají lajky a komentují instagramový příspěvek tvůrce"},
            },
            {
                "h2": "Odkud vaši noví sledující přicházejí",
                "p": [
                    "Řekněte nám město, region nebo zemi, odkud má vaše publikum přicházet. Váš profil ukážeme nejdřív skutečným lidem tam; kde je nejlépe odpovídající publikum větší, může jich víc přijít z okolí.",
                ],
            },
            {
                "h2": "Jak vypadá jeden měsíc",
                "ul": [
                    "První dny: kampaň se rozběhne a přicházejí první návštěvy.",
                    "Každý týden: noví sledující, lajky a komentáře, pár každý den.",
                    "Na konci měsíce: s balíčkem {pick_name} obvykle {pick_audience} nových sledujících.",
                ],
            },
        ],
        "faqs": [
            ("Jak rychle sledující přibývají?", "Každý den kousek, po celý měsíc. Nikdy všechno najednou: skuteční lidé sledují vlastním tempem a cokoli okamžitého je bot."),
            ("Přestanou mě noví sledující sledovat?", "Někteří možná ano, tak jako se mění každé skutečné publikum. Skuteční sledující ale zůstávají mnohem častěji než boti, kteří mizí ve vlnách."),
            ("Dostanu i lajky a komentáře?", "Ano, od stejných lidí: s balíčkem {pick_name} obvykle {pick_likes} lajků a {pick_comments} komentářů měsíčně."),
            ("Je to pro můj účet bezpečné?", "Heslo po vás nikdy nechceme a do vašeho účtu se nikdy nepřihlašujeme. Lidé najdou váš profil a rozhodnou se sami, stejně jako kterýkoli jiný sledující."),
            ("Můžu si vybrat, odkud sledující budou?", "Ano. Při objednávce nám napište město, region nebo zemi. Míříme nejdřív tam; když je podobné publikum v okolí větší, část sledujících může přijít odtud."),
        ],
    },
    {
        "service": "followers",
        "quantity": 1000,
        "slug": "instagram/sledujici/1000",
        "label": "{quantity} sledujících na Instagramu",
        "title": "{quantity} sledujících na Instagramu od skutečných lidí",
        "description": "Dosáhněte {quantity} sledujících na Instagramu se skutečnými lidmi, ne s boty. {pick_name} obvykle přinese {pick_audience} měsíčně, i s lajky a komentáři.",
        "h1": ("{quantity} sledujících na Instagramu, ", "každý z nich skutečný."),
        "intro": "Neprodáváme balík {quantity} botů. Váš účet rozvíjíme se skutečnými lidmi: {pick_name} obvykle přinese {pick_audience} nových sledujících měsíčně, takže {quantity} bývá na dosah už v prvním měsíci.",
        "hero": {"image": "instagram-followers-1000", "alt": "Rostoucí křivka nových sledujících na Instagramu dosahuje prvního milníku"},
        "sections": [
            {
                "h2": "Proč ne {quantity} sledujících za hodinu?",
                "p": [
                    "Protože žádný skutečný člověk nezačne sledovat účet pár sekund po zaplacení. Služby, které dodají {quantity} sledujících za hodinu, dodávají boty: nedávají lajky, nekomentují a mizí ve vlnách.",
                    "Ti, kteří zůstanou, škodí ještě víc. Každý sledující, který nikdy nereaguje, snižuje podíl publika, které reaguje, a vaše příspěvky potichu oslovují méně lidí.",
                ],
            },
            {
                "h2": "Prvních tisíc, a pořádně",
                "p": [
                    "Prvních tisíc skutečných sledujících mění to, jak vás vidí noví návštěvníci. Jsou to lidé, kteří se možná podívají na vaše reels, dají lajk vašim příspěvkům a vrátí se, a právě to pomáhá, aby vás našla další tisícovka.",
                ],
                "ul": [
                    "Skuteční lidé, kteří se rozhodli vás sledovat, z lokality, kterou zvolíte.",
                    "Lajky a komentáře od stejných lidí, v rámci balíčku.",
                    "Přehled toho, co jsme naměřili, den po dni.",
                ],
            },
        ],
        "faqs": [
            ("Jak dlouho trvá získat {quantity} skutečných sledujících?", "V typickém tempu přinese {pick_name} {pick_audience} nových sledujících měsíčně, takže {quantity} bývá na dosah už v prvním měsíci. Skuteční lidé sledují vlastním tempem, takže každý měsíc vypadá trochu jinak."),
            ("Je to jednorázový balík {quantity} sledujících?", "Ne. Růst prodáváme jako měsíční balíčky. {pick_name} stojí {pick_price} měsíčně a zrušit ho můžete kdykoli ve svém účtu."),
            ("Dostanu k nim i lajky a komentáře?", "Ano, od stejných skutečných lidí: s balíčkem {pick_name} obvykle {pick_likes} lajků a {pick_comments} komentářů měsíčně."),
            ("Co bude po {quantity} sledujících?", "Váš balíček běží, dokud ho nezrušíte, takže růst pokračuje měsíc za měsícem. Až bude váš obsah připravený na víc, můžete přejít na vyšší balíček."),
        ],
    },
]
