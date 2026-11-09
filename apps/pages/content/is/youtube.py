"""Icelandic YouTube pages: the hub and subscribers (mirrors en/youtube.py)."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "youtube",
        "label": "YouTube",
        "title": "Vaxtarpakkar á YouTube fyrir efnishöfunda | Growsterr",
        "description": "Láttu YouTube-rásina vaxa með raunverulegu fólki: mánaðarpakkar færa þér áskrifendur, læk og athugasemdir frá áhorfendum sem völdu áskrift. Frá {from_price}/mán.",
        "h1": ("Láttu YouTube-rásina þína vaxa ", "með raunverulegum áhorfendum."),
        "intro": "Mánaðarlegir vaxtarpakkar fyrir efnishöfunda. Raunverulegt fólk finnur rásina þína, horfir á myndböndin þín og skráir sig í áskrift þegar því líkar það sem það sér. Stjórnborðið sýnir það sem við mældum, dag frá degi.",
        "hero": {"image": "youtube-hub", "alt": "YouTube-rás sem fær áskrifendur, læk og athugasemdir frá raunverulegum áhorfendum"},
        "sections": [
            {
                "h2": "Það eru áskrifendurnir sem horfa sem skipta máli",
                "p": [
                    "YouTube mælir með myndböndum sem fólk horfir á, lækar og kemur aftur að. Áskrifandi sem horfir aldrei er verri en enginn: hann lækkar hlutfall markhópsins sem tekur þátt.",
                    "Hver áskrifandi sem við færum þér er manneskja sem fann rásina þína og valdi að skrá sig í áskrift. Læk, áhorf og athugasemdir koma frá sama fólkinu, innifalin í pakkanum.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Áhorfendur horfa á YouTube-myndband efnishöfundar og skrifa athugasemdir"},
            },
            {
                "h2": "Fyrir rásir sem birta efni af alúð",
                "p": [
                    "Kennslumyndbönd, vlogg, tónlist eða tölvuleikir: ef þú birtir reglulega gefa raunverulegir áhorfendur hverju nýju myndbandi betri byrjun. Byrjaðu með {starter_name} og færðu þig upp þegar rásin þín er tilbúin fyrir meira.",
                ],
                "ul": [
                    "Þú segir okkur frá hvaða borg, landshluta eða landi markhópurinn á að koma.",
                    "Áskrifendur, læk og athugasemdir koma saman, frá sama fólkinu.",
                    "Rásin þín er áfram þín: við biðjum aldrei um lykilorðið þitt.",
                ],
                "image": {"image": "youtube-channel", "alt": "Efnishöfundur klippir YouTube-myndband í heimastúdíói"},
            },
        ],
        "faqs": [
            ("Eru áskrifendurnir raunverulegt fólk?", "Já. Hver áskrifandi er raunveruleg manneskja sem fann rásina þína og valdi að skrá sig í áskrift. Engir bottar, engir falskir reikningar, ekkert samstundis."),
            ("Hve marga áskrifendur færir pakki?", "Yfirleitt {starter_audience} nýja áskrifendur á mánuði með {starter_name}, {rising_audience} með {rising_name} og {pro_audience} með {pro_name}. Dæmigerð bil, ekki föst tala."),
            ("Þurfið þið Google- eða YouTube-lykilorðið mitt?", "Aldrei. Við þurfum aðeins auðkenni rásarinnar (@handle) og rásin þarf að vera opin."),
            ("Get ég keypt áhorf eða læk stök?", "Nei. Áhorf, læk og athugasemdir eru innifalin í hverjum pakka, frá sama raunverulega fólkinu og skráir sig í áskrift."),
            ("Get ég sagt upp hvenær sem er?", "Já. Pakkarnir endurnýjast mánaðarlega og þú getur sagt þeim upp á reikningnum þínum. Mánuðurinn sem þú hefur greitt fyrir gildir til enda."),
        ],
    },
    {
        "service": "subscribers",
        "slug": "youtube/askrifendur",
        "label": "YouTube-áskrifendur",
        "title": "Raunverulegir YouTube-áskrifendur sem horfa | Growsterr",
        "description": "YouTube-áskrifendur sem eru raunverulegt fólk: áhorfendur sem fundu rásina þína og völdu áskrift, með læk og athugasemdir. Frá {from_price} á mánuði.",
        "h1": ("YouTube-áskrifendur ", "sem horfa í alvöru."),
        "intro": "Raunverulegt fólk finnur rásina þína, horfir á myndböndin þín og skráir sig í áskrift þegar því líkar það sem það sér. Yfirleitt {starter_audience} nýir áskrifendur á mánuði með {starter_name}, með læk og athugasemdir frá sömu áhorfendum.",
        "hero": {"image": "youtube-subscribers", "alt": "Síða YouTube-rásar sem fær nýja áskrifendur frá raunverulegum áhorfendum"},
        "sections": [
            {
                "h2": "Áskrifandi ætti að vera áhorfandi",
                "p": [
                    "Á YouTube gerir áskrifandi aðeins gagn ef hann horfir. Raunverulegir áskrifendur sjá næsta myndbandið þitt, horfa á það, læka það og skrifa stundum athugasemd, og það er það sem YouTube horfir á þegar það ákveður hverju á að mæla með.",
                    "Bottaáskrifendur horfa aldrei. Þeir láta rás líta út fyrir að vera stærri á meðan myndböndin hennar ná til færra fólks.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Raunverulegir áhorfendur skrá sig í áskrift að YouTube-rás eftir að hafa horft á myndband"},
            },
            {
                "h2": "Svona lítur mánuður út",
                "ul": [
                    "Fyrstu dagarnir: herferðin hefst og fyrstu áhorfendurnir berast.",
                    "Í hverri viku: nýir áskrifendur, læk og athugasemdir, nokkur á hverjum degi.",
                    "Í lok mánaðarins: yfirleitt {pick_audience} nýir áskrifendur með {pick_name}.",
                ],
            },
            {
                "h2": "Hvaðan áhorfendurnir þínir koma",
                "p": [
                    "Segðu okkur frá hvaða borg, landshluta eða landi markhópurinn þinn á að koma. Við sýnum rásina þína fyrst raunverulegu fólki þar; þar sem best viðeigandi markhópurinn er stærri geta fleiri komið frá nærliggjandi svæðum.",
                ],
            },
        ],
        "faqs": [
            ("Hve hratt koma áskrifendurnir?", "Svolítið á hverjum degi, allan mánuðinn. Aldrei allt í einu: raunverulegt fólk skráir sig í áskrift á sínum eigin hraða."),
            ("Munu þeir horfa á myndböndin mín?", "Þetta er raunverulegt fólk sem valdi að skrá sig í áskrift eftir að hafa séð rásina þína. Hvað það horfir á næst er undir því komið, eins og hjá öllum markhópum, og einmitt þess vegna skiptir það máli."),
            ("Fæ ég líka læk og athugasemdir?", "Já, frá sömu áhorfendum: yfirleitt {pick_likes} læk og {pick_comments} athugasemdir á mánuði með {pick_name}."),
            ("Þurfið þið lykilorðið mitt?", "Aldrei. Við þurfum aðeins auðkenni rásarinnar og rásin þarf að vera opin."),
        ],
    },
]
