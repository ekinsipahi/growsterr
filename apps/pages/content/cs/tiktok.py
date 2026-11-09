"""Czech TikTok pages: the hub and likes. Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "tiktok",
        "label": "TikTok",
        "title": "Balíčky růstu na TikToku pro tvůrce | Growsterr",
        "description": "Rosťte na TikToku se skutečnými lidmi: měsíční balíčky přinášejí nové sledující, lajky a komentáře od lidí, kteří vás chtějí sledovat. Od {from_price} měsíčně.",
        "h1": ("Rosťte na TikToku ", "se skutečnými lidmi."),
        "intro": "Měsíční balíčky růstu pro tvůrce a influencery. Skuteční lidé objevují váš profil, dívají se na vaše videa a začnou vás sledovat, když se jim líbí, co vidí. V přehledu uvidíte, co jsme naměřili, den po dni.",
        "hero": {"image": "tiktok-hub", "alt": "Profil tvůrce na TikToku, kterému přibývají noví sledující a lajky"},
        "sections": [
            {
                "h2": "Na TikToku je pozornost všechno",
                "p": [
                    "TikTok ukáže video více lidem, když se jeho první diváci dívají, dávají lajky, komentují a začnou sledovat. Čísla, za kterými nejsou lidé, nic z toho nerozhýbou.",
                    "Naše balíčky každý den přivádějí na váš profil skutečné lidi. Dívají se, rozhodují se a ti, které vaše videa baví, vás sledují a dávají lajky. Právě taková pozornost pomáhá videu dostat se dál.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Skuteční diváci se dívají na videa tvůrce na TikToku"},
            },
            {
                "h2": "Pro tvůrce, kteří mají co říct",
                "p": [
                    "Komedie, vaření, móda nebo návody: když publikujete pravidelně, skuteční diváci dají každému novému videu lepší start. Začněte s balíčkem {starter_name} a přejděte výš, až budete připraveni.",
                ],
                "ul": [
                    "Řeknete nám město, region nebo zemi, odkud má vaše publikum přicházet.",
                    "Sledující, lajky a komentáře přicházejí společně, od stejných lidí.",
                    "Účet zůstává váš: heslo po vás nikdy nechceme.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Tvůrce natáčí video na TikTok s telefonem na stativu"},
            },
        ],
        "faqs": [
            ("Jsou sledující skuteční lidé?", "Ano. Každý sledující je skutečný člověk, který viděl váš profil a rozhodl se vás sledovat. Nikdy nepoužíváme boty, falešné účty ani okamžité doručení."),
            ("Kolik sledujících balíček přinese?", "{starter_name} obvykle přinese {starter_audience} nových sledujících měsíčně, {rising_name} {rising_audience} a {pro_name} {pro_audience}. Typická rozpětí, ne pevný počet: skuteční lidé se rozhodují sami."),
            ("Potřebujete moje heslo k TikToku?", "Nikdy. Stačí nám vaše uživatelské jméno. Nechte účet veřejný, aby vás lidé, kteří ho objeví, mohli sledovat."),
            ("Můžu si koupit zhlédnutí nebo lajky samostatně?", "Ne. Zhlédnutí, lajky a komentáře jsou součástí každého balíčku a přicházejí od stejných skutečných lidí, kteří vás sledují."),
            ("Můžu předplatné kdykoli zrušit?", "Ano. Balíčky se obnovují měsíčně a zrušit je můžete ve svém účtu. Zaplacený měsíc doběhne do konce."),
        ],
    },
    {
        "service": "likes",
        "slug": "tiktok/lajky",
        "label": "Lajky na TikToku",
        "title": "Lajky na TikToku od skutečných lidí v každém balíčku",
        "description": "Lajky na TikToku od skutečných lidí, kteří se dívají na vaše videa, nikdy od botů. Jsou v každém měsíčním balíčku se sledujícími a komentáři. Od {from_price}.",
        "h1": ("Lajky na TikToku od skutečných lidí. ", "V každém balíčku."),
        "intro": "Lajky samostatně neprodáváme. Každý balíček přivádí skutečné lidi, kteří objeví váš profil, dívají se na vaše videa a dávají lajky tomu, co je baví: s balíčkem {starter_name} obvykle {starter_likes} lajků měsíčně.",
        "hero": {"image": "tiktok-likes", "alt": "Lajky od skutečných diváků přibývají u videa na TikToku"},
        "sections": [
            {
                "h2": "Proč lajk platí, jen když za ním stojí člověk",
                "p": [
                    "TikTok sleduje, co se kolem lajku děje: díval se divák dál, začal sledovat, vrátil se? Lajky od botů na všechno odpovídají ne, takže přidají číslo a uberou dosah.",
                    "Lajky od skutečných lidí přicházejí se vším ostatním: s časem sledování, novými sledujícími a komentáři. To je signál, který pomáhá videu dostat se dál.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Diváci dokoukají video na TikToku do konce a dají mu lajk"},
            },
            {
                "h2": "Kolik lajků který balíček přinese",
                "ul": [
                    "{starter_name} ({starter_price} měsíčně): obvykle {starter_likes} lajků.",
                    "{rising_name} ({rising_price} měsíčně): obvykle {rising_likes} lajků, na videa, která si vyberete.",
                    "{pro_name} ({pro_price} měsíčně): obvykle {pro_likes} lajků, s přednostním zařazením.",
                ],
            },
            {
                "h2": "Proč lajky neprodáváme samostatně",
                "p": [
                    "Lajky, které přijdou bez zhlédnutí, sledujících a komentářů, vypadají přesně jako to, čím jsou. V balíčku pochází každý lajk od někoho, kdo se na video díval, takže vaše čísla rostou spolu, tak jako při skutečném růstu.",
                ],
            },
        ],
        "faqs": [
            ("Můžu dostat lajky na TikToku bez balíčku?", "Ne. Lajky, zhlédnutí a komentáře přicházejí jen v rámci našich měsíčních balíčků, od stejných skutečných lidí. Díky tomu zůstávají přirozené."),
            ("Která videa lajky dostanou?", "Skuteční lidé dávají lajky tomu, co je baví, obvykle vašim nejnovějším videím. S balíčky {rising_name} a {pro_name} si můžete vybrat, která videa dostanou pozornost."),
            ("Jak rychle lajky přibývají?", "Každý den kousek, po celý měsíc. Nikdy okamžitě: okamžitý lajk je bot."),
            ("Potřebujete moje heslo k TikToku?", "Nikdy. Stačí nám vaše uživatelské jméno a účet by měl být veřejný."),
        ],
    },
]
