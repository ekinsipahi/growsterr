"""Irish YouTube pages: the hub and subscribers (síntiúsóirí). Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "youtube",
        "label": "YouTube",
        "title": "Pacáistí fáis YouTube do chruthaitheoirí | Growsterr",
        "description": "Fás ar YouTube le daoine fíora: tugann pacáistí míosúla síntiúsóirí, ‘is maith liom’ agus tráchtanna ó lucht féachana a shocraigh liostáil. Ó {from_price} sa mhí.",
        "h1": ("Forbair do chainéal YouTube ", "le lucht féachana fíor."),
        "intro": "Ag smaoineamh ar shíntiúsóirí nó féachaintí YouTube a cheannach? Tá an leagan macánta anseo: pacáistí fáis míosúla do chruthaitheoirí. Aimsíonn daoine fíora do chainéal, féachann siad ar d'fhíseáin agus liostálann siad nuair is maith leo a bhfeiceann siad. Taispeánann do dheais cad a thomhaiseamar, lá ar lá.",
        "hero": {"image": "youtube-hub", "alt": "Cainéal YouTube ag fáil síntiúsóirí, ‘is maith liom’ agus tráchtanna ó lucht féachana fíor"},
        "sections": [
            {
                "h2": "Is iad na síntiúsóirí a fhéachann a chomhaireann",
                "p": [
                    "Molann YouTube físeáin a bhféachann daoine orthu, a dtugann siad ‘is maith liom’ dóibh agus a bhfilleann siad orthu. Is measa síntiúsóir nach bhféachann riamh ná gan aon cheann: laghdaíonn sé an sciar de do lucht féachana a ghlacann páirt.",
                    "Is duine é gach síntiúsóir a thugaimid chugat a d'aimsigh do chainéal agus a shocraigh liostáil leis. Tagann ‘is maith liom’, féachaintí agus tráchtanna ó na daoine céanna, laistigh de do phacáiste.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Lucht féachana ag féachaint ar fhíseán YouTube cruthaitheora agus ag scríobh tráchtanna"},
            },
            {
                "h2": "Do chainéil a fhoilsíonn go cúramach",
                "p": [
                    "Ranganna teagaisc, vlaganna, ceol nó cluichíocht: má fhoilsíonn tú go rialta, tugann lucht féachana fíor tús níos fearr do gach físeán nua. Tosaigh le {starter_name} agus bog suas nuair a bheidh do chainéal réidh le haghaidh tuilleadh.",
                ],
                "ul": [
                    "Insíonn tú dúinn an chathair, an réigiún nó an tír ar cheart do do lucht féachana teacht as.",
                    "Tagann síntiúsóirí, ‘is maith liom’ agus tráchtanna le chéile, ó na daoine céanna.",
                    "Fanann do chainéal agatsa: ní iarraimid do phasfhocal riamh.",
                ],
                "image": {"image": "youtube-channel", "alt": "Cruthaitheoir ag eagarthóireacht físeáin YouTube i stiúideo baile"},
            },
        ],
        "faqs": [
            ("An daoine fíora iad na síntiúsóirí?", "Is ea. Is duine fíor gach síntiúsóir a d'aimsigh do chainéal agus a shocraigh liostáil leis. Gan róbait, gan cuntais bhréige, gan aon rud ar an toirt."),
            ("Cé mhéad síntiúsóir a thugann pacáiste?", "Síntiúsóirí nua sa mhí, de ghnáth: {starter_audience} le {starter_name}, {rising_audience} le {rising_name} agus {pro_audience} le {pro_name}. Raonta tipiciúla, ní líon seasta."),
            ("An dteastaíonn mo phasfhocal Google nó YouTube uaibh?", "Ní theastaíonn riamh. Níl uainn ach ainm @ do chainéil, agus ba cheart do chainéal a bheith poiblí."),
            ("An féidir liom féachaintí nó ‘is maith liom’ a cheannach leo féin?", "Ní féidir. Tagann féachaintí, ‘is maith liom’ agus tráchtanna laistigh de gach pacáiste, ó na daoine fíora céanna a liostálann le do chainéal."),
            ("An féidir liom cealú am ar bith?", "Is féidir. Athnuaitear na pacáistí gach mí agus is féidir leat cealú ó do chuntas. Leanann an mhí atá íoctha agat go dtí a deireadh."),
        ],
    },
    {
        "service": "subscribers",
        "slug": "youtube/sintiusoiri",
        "label": "Síntiúsóirí YouTube",
        "title": "Ceannaigh síntiúsóirí fíora YouTube a fhéachann | Growsterr",
        "description": "Ceannaigh síntiúsóirí fíora YouTube: lucht féachana a d'aimsigh do chainéal agus a shocraigh liostáil, le ‘is maith liom’ agus tráchtanna. Ó {from_price} sa mhí.",
        "h1": ("Síntiúsóirí YouTube ", "a fhéachann i ndáiríre."),
        "intro": "Ceannaigh síntiúsóirí YouTube ar an mbealach macánta: aimsíonn daoine fíora do chainéal, féachann siad ar d'fhíseáin agus liostálann siad nuair is maith leo a bhfeiceann siad. De ghnáth, {starter_audience} síntiúsóir nua sa mhí le {starter_name}, le ‘is maith liom’ agus tráchtanna ón lucht féachana céanna.",
        "hero": {"image": "youtube-subscribers", "alt": "Leathanach cainéil YouTube le síntiúsóirí nua ó lucht féachana fíor"},
        "sections": [
            {
                "h2": "Ba cheart gur féachadóir é síntiúsóir",
                "p": [
                    "Ar YouTube, níl maith i síntiúsóir mura bhféachann sé. Feiceann síntiúsóirí fíora d'fhíseán nua, féachann siad air, tugann siad ‘is maith liom’ dó agus déanann siad trácht uaireanta, agus is air sin a fhéachann YouTube nuair a shocraíonn sé cad a mholfaidh sé.",
                    "Ní fhéachann síntiúsóirí atá ina róbait riamh. Cuireann siad cuma níos mó ar chainéal, fad is a shroicheann a chuid físeán níos lú daoine.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Lucht féachana fíor ag liostáil le cainéal YouTube tar éis dóibh físeán a fheiceáil"},
            },
            {
                "h2": "An chuma atá ar mhí amháin",
                "ul": [
                    "Na chéad laethanta: tosaíonn d'fheachtas agus tagann an chéad lucht féachana.",
                    "Gach seachtain: síntiúsóirí nua, ‘is maith liom’ agus tráchtanna, beagán gach lá.",
                    "Faoi dheireadh na míosa: {pick_audience} síntiúsóir nua de ghnáth le {pick_name}.",
                ],
            },
            {
                "h2": "Cárb as a dtagann do lucht féachana",
                "p": [
                    "Inis dúinn an chathair, an réigiún nó an tír ar cheart do do lucht féachana teacht as. Taispeánaimid do chainéal do dhaoine fíora ansin ar dtús; má tá an lucht féachana is fearr a oireann níos mó in áit in aice láimhe, d'fhéadfadh níos mó acu teacht as sin.",
                ],
            },
        ],
        "faqs": [
            ("Cé chomh tapa a thagann na síntiúsóirí?", "Beagán gach lá, ar feadh na míosa ar fad. Ní thagann siad uile le chéile choíche: liostálann daoine fíora ar a luas féin."),
            ("An bhféachfaidh siad ar m'fhíseáin?", "Is daoine fíora iad a shocraigh liostáil tar éis dóibh do chainéal a fheiceáil. Is fúthu féin atá sé cad air a bhféachfaidh siad ina dhiaidh sin, mar a bhíonn le haon lucht féachana, agus sin go díreach an fáth a gcomhaireann sé."),
            ("An bhfaighidh mé ‘is maith liom’ agus tráchtanna freisin?", "Gheobhaidh, ón lucht féachana céanna: {pick_likes} ‘is maith liom’ agus {pick_comments} trácht sa mhí de ghnáth le {pick_name}."),
            ("An dteastaíonn mo phasfhocal uaibh?", "Ní theastaíonn riamh. Níl uainn ach ainm @ do chainéil, agus ba cheart do chainéal a bheith poiblí."),
        ],
    },
]
