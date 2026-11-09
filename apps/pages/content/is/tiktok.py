"""Icelandic TikTok pages: the hub and likes ("læk") (mirrors en/tiktok.py)."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "tiktok",
        "label": "TikTok",
        "title": "Vaxtarpakkar á TikTok fyrir efnishöfunda | Growsterr",
        "description": "Vaxtu á TikTok með raunverulegu fólki: mánaðarpakkar færa þér nýja fylgjendur, læk og athugasemdir frá fólki sem valdi að fylgja þér. Frá {from_price} á mánuði.",
        "h1": ("Láttu TikTok-reikninginn vaxa ", "með raunverulegu fólki."),
        "intro": "Mánaðarlegir vaxtarpakkar fyrir efnishöfunda og áhrifavalda. Raunverulegt fólk finnur prófílinn þinn, horfir á myndböndin þín og fylgir þér þegar því líkar það sem það sér. Stjórnborðið sýnir það sem við mældum, dag frá degi.",
        "hero": {"image": "tiktok-hub", "alt": "Prófíll efnishöfundar á TikTok þar sem nýir fylgjendur og læk streyma inn"},
        "sections": [
            {
                "h2": "Á TikTok er athyglin allt",
                "p": [
                    "TikTok sýnir myndband fleirum þegar fyrstu áhorfendurnir horfa, læka, skrifa athugasemdir og fylgja. Tölur án fólks á bak við þær hreyfa ekkert af þessu.",
                    "Pakkarnir okkar færa raunverulegt fólk á prófílinn þinn á hverjum degi. Það horfir og ákveður sig, og þau sem kunna að meta myndböndin þín fylgja og læka. Það er sú athygli sem hjálpar myndbandi að dreifast.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Raunverulegir áhorfendur horfa á TikTok-myndbönd efnishöfundar"},
            },
            {
                "h2": "Fyrir efnishöfunda sem hafa eitthvað að segja",
                "p": [
                    "Grín, matargerð, tíska eða kennslumyndbönd: ef þú birtir reglulega gefa raunverulegir áhorfendur hverju nýju myndbandi betri byrjun. Byrjaðu með {starter_name} og færðu þig upp þegar tíminn er réttur.",
                ],
                "ul": [
                    "Þú segir okkur frá hvaða borg, landshluta eða landi markhópurinn á að koma.",
                    "Fylgjendur, læk og athugasemdir koma saman, frá sama fólkinu.",
                    "Reikningurinn þinn er áfram þinn: við biðjum aldrei um lykilorðið þitt.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Efnishöfundur tekur upp TikTok-myndband með síma á þrífæti"},
            },
        ],
        "faqs": [
            ("Eru fylgjendurnir raunverulegt fólk?", "Já. Hver fylgjandi er raunveruleg manneskja sem sá prófílinn þinn og valdi að fylgja þér. Við notum aldrei botta, falska reikninga eða afhendingu samstundis."),
            ("Hve marga fylgjendur færir pakki?", "Yfirleitt {starter_audience} nýja fylgjendur á mánuði með {starter_name}, {rising_audience} með {rising_name} og {pro_audience} með {pro_name}. Dæmigerð bil, ekki föst tala: raunverulegt fólk ákveður sjálft."),
            ("Þurfið þið TikTok-lykilorðið mitt?", "Aldrei. Við þurfum aðeins notandanafnið þitt. Hafðu reikninginn opinn svo fólkið sem finnur hann geti fylgt þér."),
            ("Get ég keypt áhorf eða læk stök?", "Nei. Áhorf, læk og athugasemdir eru innifalin í hverjum pakka, frá sama raunverulega fólkinu og fylgir þér."),
            ("Get ég sagt upp hvenær sem er?", "Já. Pakkarnir endurnýjast mánaðarlega og þú getur sagt þeim upp á reikningnum þínum. Mánuðurinn sem þú hefur greitt fyrir gildir til enda."),
        ],
    },
    {
        "service": "likes",
        "slug": "tiktok/laek",
        "label": "TikTok-læk",
        "title": "TikTok-læk frá raunverulegu fólki, í hverjum pakka",
        "description": "TikTok-læk frá raunverulegu fólki sem horfir á myndböndin þín, aldrei frá bottum. Læk eru innifalin í hverjum mánaðarpakka. Frá {from_price} á mánuði.",
        "h1": ("TikTok-læk frá raunverulegu fólki. ", "Innifalin í hverjum pakka."),
        "intro": "Við seljum ekki læk stök. Hver pakki færir þér raunverulegt fólk sem finnur prófílinn þinn, horfir á myndböndin þín og lækar það sem því líkar: yfirleitt {starter_likes} læk á mánuði með {starter_name}.",
        "hero": {"image": "tiktok-likes", "alt": "Læk frá raunverulegum áhorfendum rísa upp frá TikTok-myndbandi"},
        "sections": [
            {
                "h2": "Læk skiptir aðeins máli með manneskju á bak við það",
                "p": [
                    "TikTok fylgist með því sem gerist í kringum læk: hélt áhorfandinn áfram að horfa, fylgdi hann, kom hann aftur? Læk frá bottum svara öllu þessu neitandi, svo þau bæta við tölu en taka af útbreiðslunni.",
                    "Læk frá raunverulegu fólki koma með öllu hinu: áhorfstíma, nýjum fylgjendum og athugasemdum. Það er merkið sem hjálpar myndbandi að dreifast.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Áhorfendur horfa á TikTok-myndband til enda og læka það"},
            },
            {
                "h2": "Svona mörg læk færir hver pakki",
                "ul": [
                    "{starter_name} ({starter_price} á mánuði): yfirleitt {starter_likes} læk.",
                    "{rising_name} ({rising_price} á mánuði): yfirleitt {rising_likes} læk, á myndböndin sem þú velur.",
                    "{pro_name} ({pro_price} á mánuði): yfirleitt {pro_likes} læk, með forgangi í birtingu.",
                ],
            },
            {
                "h2": "Af hverju við seljum ekki læk stök",
                "p": [
                    "Læk sem koma án áhorfa, fylgjenda eða athugasemda líta nákvæmlega út eins og það sem þau eru. Í pakka kemur hvert læk frá einhverjum sem horfði á myndbandið, svo tölurnar þínar hreyfast saman, eins og raunverulegur vöxtur gerir.",
                ],
            },
        ],
        "faqs": [
            ("Get ég fengið TikTok-læk án pakka?", "Nei. Læk, áhorf og athugasemdir koma aðeins í mánaðarpökkunum okkar, frá sama raunverulega fólkinu. Það er það sem heldur þeim eðlilegum."),
            ("Hvaða myndbönd fá lækin?", "Raunverulegt fólk lækar það sem því líkar, yfirleitt nýjustu myndböndin þín. Með {rising_name} og {pro_name} geturðu valið hvaða myndbönd fá athyglina."),
            ("Hve hratt koma lækin?", "Svolítið á hverjum degi, yfir mánuðinn. Aldrei samstundis: læk sem kemur samstundis er frá botta."),
            ("Þurfið þið TikTok-lykilorðið mitt?", "Aldrei. Við þurfum aðeins notandanafnið þitt og reikningurinn þarf að vera opinn."),
        ],
    },
]
