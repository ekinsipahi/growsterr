"""Slovenian TikTok pages: the hub and likes. Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "tiktok",
        "label": "TikTok",
        "title": "Paketi za rast na TikToku za ustvarjalce | Growsterr",
        "description": "Rastite na TikToku z resničnimi ljudmi: mesečni paketi prinesejo nove sledilce, všečke in komentarje ljudi, ki so se odločili slediti. Od {from_price}/mesec.",
        "h1": ("Rastite na TikToku ", "z resničnimi ljudmi."),
        "intro": "Mesečni paketi za rast za ustvarjalce in vplivneže. Resnični ljudje odkrijejo vaš profil, si ogledajo vaše videe in vam sledijo, ko jim je všeč, kar vidijo. Nadzorna plošča dan za dnem pokaže, kaj smo izmerili.",
        "hero": {"image": "tiktok-hub", "alt": "Profil ustvarjalca na TikToku, na katerega prihajajo novi sledilci in všečki"},
        "sections": [
            {
                "h2": "Na TikToku je pozornost vse",
                "p": [
                    "TikTok video pokaže več ljudem, ko ga prvi gledalci gledajo, všečkajo, komentirajo in začnejo slediti. Številke brez ljudi za njimi ne premaknejo ničesar od tega.",
                    "Naši paketi vsak dan pripeljejo resnične ljudi na vaš profil. Gledajo in se odločajo, tisti, ki uživajo v vaših videih, pa vam sledijo in jih všečkajo. Prav takšna pozornost pomaga, da video pride dlje.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Resnični gledalci gledajo videe ustvarjalca na TikToku"},
            },
            {
                "h2": "Za ustvarjalce, ki imajo kaj povedati",
                "p": [
                    "Komedija, kuhanje, moda ali vodiči: če redno objavljate, resnični gledalci vsakemu novemu videu dajo boljši začetek. Začnite s paketom {starter_name} in preidite višje, ko ste pripravljeni.",
                ],
                "ul": [
                    "Poveste nam mesto, regijo ali državo, iz katere naj prihaja vaše občinstvo.",
                    "Sledilci, všečki in komentarji pridejo skupaj, od istih ljudi.",
                    "Vaš račun ostane vaš: nikoli ne zahtevamo vašega gesla.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Ustvarjalec snema video za TikTok s telefonom na stojalu"},
            },
        ],
        "faqs": [
            ("So sledilci resnični ljudje?", "Da. Vsak sledilec je resnična oseba, ki je videla vaš profil in se odločila, da vam bo sledila. Nikoli ne uporabljamo botov, lažnih računov ali takojšnje dostave."),
            ("Koliko sledilcev prinese paket?", "Običajno {starter_audience} novih sledilcev na mesec s paketom {starter_name}, {rising_audience} s paketom {rising_name} in {pro_audience} s paketom {pro_name}. Tipični razponi, ne fiksno število: resnični ljudje se odločajo sami."),
            ("Potrebujete moje geslo za TikTok?", "Nikoli. Potrebujemo le vaše uporabniško ime. Račun naj bo javen, da mu ljudje, ki ga odkrijejo, lahko sledijo."),
            ("Lahko kupim samo oglede ali všečke?", "Ne. Ogledi, všečki in komentarji so vključeni v vsak paket in prihajajo od istih resničnih ljudi, ki vam sledijo."),
            ("Lahko kadar koli prekličem?", "Da. Paketi se podaljšujejo mesečno, prekličete pa jih lahko v svojem računu. Plačani mesec teče do konca."),
        ],
    },
    {
        "service": "likes",
        "slug": "tiktok/vsecki",
        "label": "Všečki na TikToku",
        "title": "Všečki na TikToku od resničnih ljudi, v vsakem paketu",
        "description": "Všečki na TikToku od resničnih ljudi, ki gledajo vaše videe, nikoli od botov. Vključeni so v vsak mesečni paket, s sledilci in komentarji. Od {from_price}/mesec.",
        "h1": ("Všečki na TikToku od resničnih ljudi. ", "V vsakem paketu."),
        "intro": "Všečkov ne prodajamo posebej. Vsak paket prinese resnične ljudi, ki odkrijejo vaš profil, si ogledajo vaše videe in všečkajo tisto, v čemer uživajo: običajno {starter_likes} všečkov na mesec s paketom {starter_name}.",
        "hero": {"image": "tiktok-likes", "alt": "Všečki resničnih gledalcev, ki se dvigajo iz videa na TikToku"},
        "sections": [
            {
                "h2": "Zakaj všeček šteje le, če je za njim človek",
                "p": [
                    "TikTok spremlja, kaj se zgodi okoli všečka: je gledalec gledal naprej, začel slediti, se vrnil? Všečki botov na vse to odgovorijo z ne, zato dodajo številko in odvzamejo doseg.",
                    "Všečki resničnih ljudi pridejo skupaj z vsem ostalim: s časom gledanja, sledenjem in komentarji. To je signal, ki pomaga, da video pride dlje.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Gledalci si video na TikToku ogledajo do konca in ga všečkajo"},
            },
            {
                "h2": "Koliko všečkov prinese posamezen paket",
                "ul": [
                    "{starter_name} ({starter_price} na mesec): običajno {starter_likes} všečkov.",
                    "{rising_name} ({rising_price} na mesec): običajno {rising_likes} všečkov, na videih, ki jih izberete.",
                    "{pro_name} ({pro_price} na mesec): običajno {pro_likes} všečkov, s prednostno obravnavo.",
                ],
            },
            {
                "h2": "Zakaj všečkov ne prodajamo posebej",
                "p": [
                    "Všečki, ki pridejo brez ogledov, sledenja ali komentarjev, so videti točno takšni, kot so. V paketu vsak všeček pride od nekoga, ki si je video ogledal, zato se vaše številke premikajo skupaj, tako kot pri resnični rasti.",
                ],
            },
        ],
        "faqs": [
            ("Lahko dobim všečke na TikToku brez paketa?", "Ne. Všečki, ogledi in komentarji so na voljo le v naših mesečnih paketih, od istih resničnih ljudi. Zato ostanejo naravni."),
            ("Kateri videi dobijo všečke?", "Resnični ljudje všečkajo tisto, kar jim je všeč, običajno vaše najnovejše videe. S paketoma {rising_name} in {pro_name} lahko sami izberete, kateri videi dobijo pozornost."),
            ("Kako hitro pridejo všečki?", "Vsak dan malo, skozi ves mesec. Nikoli takoj: takojšnji všeček je bot."),
            ("Potrebujete moje geslo za TikTok?", "Nikoli. Potrebujemo le vaše uporabniško ime, račun pa naj bo javen."),
        ],
    },
]
