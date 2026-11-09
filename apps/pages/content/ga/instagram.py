"""Irish Instagram pages: the hub, followers, and the 1,000-followers goal.
Keys and placeholders: docs/CONTENT.md. Numbers come from the packages ({starter_audience}...)."""

UPDATED = "2026-11-08"

PAGES = [
    {
        # The hub: no service.
        "slug": "instagram",
        "label": "Instagram",
        "title": "Pacáistí fáis Instagram do chruthaitheoirí | Growsterr",
        "description": "Fás ar Instagram le daoine fíora: tugann pacáistí míosúla leantóirí, ‘is maith liom’ agus tráchtanna ó dhaoine a shocraigh thú a leanúint. Ó {from_price} sa mhí.",
        "h1": ("Fás ar Instagram ", "le daoine fíora."),
        "intro": "Ag smaoineamh ar leantóirí, ‘is maith liom’ nó tráchtanna Instagram a cheannach? Tá an leagan macánta anseo: pacáistí fáis míosúla do chruthaitheoirí agus do thionchairí. Cuirimid do phróifíl os comhair daoine fíora, agus na daoine ar maith leo a bhfeiceann siad, leanann siad thú, tugann siad ‘is maith liom’ agus déanann siad trácht. Taispeánann do dheais cad a thomhaiseamar, lá ar lá.",
        "hero": {"image": "instagram-hub", "alt": "Próifíl cruthaitheora ar Instagram le leantóirí nua, ‘is maith liom’ agus tráchtanna ag teacht isteach"},
        "sections": [
            {
                "h2": "Fás a bhfuil cuma tuillte air",
                "p": [
                    "Tugann Instagram tosaíocht do chuntais a mbíonn daoine ag plé leo i ndáiríre. Déanann róbait a mhalairt: suíonn siad i do líon leantóirí, ní thugann siad ‘is maith liom’ riamh, ní fhéachann siad ar aon rud agus múineann siad don algarithim nach fiú do phostálacha a thaispeáint.",
                    "Oibrímidne an bealach eile. Taispeántar do phróifíl do dhaoine fíora gach lá, agus is rogha a rinne duine éigin gach leanúint. Sin é an fáth a dtagann ‘is maith liom’, féachaintí agus tráchtanna in éineacht le do leantóirí, ní mar cheannach ar leith.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Daoine fíora ag aimsiú postálacha Instagram cruthaitheora agus ag fágáil tráchtanna"},
            },
            {
                "h2": "Do chruthaitheoirí a phostálann le cuspóir",
                "p": [
                    "Branda pearsanta, leathanach nideoige nó gnó beag: fásann na pacáistí leat. Tosaigh le {starter_name} agus bog suas nuair a bheidh d'ábhar réidh le haghaidh tuilleadh.",
                ],
                "ul": [
                    "Baineann Reels, carúsail agus postálacha grianghraf ar fad tairbhe as.",
                    "Insíonn tú dúinn an chathair, an réigiún nó an tír ar cheart do do lucht féachana teacht as.",
                    "Fanann do chuntas agatsa: ní iarraimid do phasfhocal riamh.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "Cruthaitheoir ag pleanáil ábhar Instagram ag deasc"},
            },
        ],
        "faqs": [
            ("An daoine fíora iad na leantóirí?", "Is ea. Is duine fíor gach leantóir a chonaic do phróifíl agus a shocraigh thú a leanúint. Ní úsáidimid róbait, próifílí bréige ná seachadadh ar an toirt riamh."),
            ("Cé mhéad leantóir a thugann pacáiste?", "Leantóirí nua sa mhí, de ghnáth: {starter_audience} le {starter_name}, {rising_audience} le {rising_name} agus {pro_audience} le {pro_name}. Is raonta tipiciúla iad, ní líon seasta: socraíonn daoine fíora dóibh féin."),
            ("An dteastaíonn mo phasfhocal Instagram uaibh?", "Ní theastaíonn riamh. Níl uainn ach d'ainm úsáideora. Coinnigh do chuntas poiblí ionas gur féidir leis na daoine a aimsíonn é thú a leanúint."),
            ("An féidir liom ‘is maith liom’ nó tráchtanna a cheannach leo féin?", "Ní féidir. Tagann ‘is maith liom’, féachaintí agus tráchtanna laistigh de gach pacáiste, ó na daoine fíora céanna a leanann thú. Sin a choinníonn d'uimhreacha nádúrtha."),
            ("An féidir liom cealú am ar bith?", "Is féidir. Athnuaitear na pacáistí gach mí agus is féidir leat cealú ó do chuntas. Leanann an mhí atá íoctha agat go dtí a deireadh."),
        ],
    },
    {
        "service": "followers",
        "slug": "instagram/leantoiri",
        "label": "Leantóirí Instagram",
        "title": "Ceannaigh leantóirí fíora Instagram, gach mí | Growsterr",
        "description": "Ceannaigh leantóirí Instagram ar daoine fíora iad a shocraigh thú a leanúint, le ‘is maith liom’ agus tráchtanna ó na daoine céanna. Ó {from_price} sa mhí.",
        "h1": ("Leantóirí Instagram ", "a shocraigh thú a leanúint."),
        "intro": "Ceannaigh leantóirí Instagram ar an mbealach macánta: aimsíonn daoine fíora do phróifíl gach lá, agus na daoine ar maith leo a bhfeiceann siad, leanann siad thú. De ghnáth, {starter_audience} leantóir nua sa mhí le {starter_name}, agus ‘is maith liom’ agus tráchtanna ó na daoine céanna.",
        "hero": {"image": "instagram-followers", "alt": "Próifíl Instagram ag fáil leantóirí nua ó dhaoine fíora"},
        "sections": [
            {
                "h2": "Cén fáth a bhfuil níos mó luach i leantóirí fíora",
                "p": [
                    "Ní fiú leantóir ach amháin má tá duine taobh thiar de. Feiceann leantóirí fíora do chéad phostáil eile, tugann siad ‘is maith liom’ di, déanann siad trácht uirthi agus roinneann siad í, agus is ar an rannpháirtíocht sin a fhéachann Instagram nuair a shocraíonn sé cé eile a fheicfidh d'ábhar.",
                    "Ní féidir le róbait aon cheann de sin a dhéanamh. Ardaíonn siad uimhir ar feadh cúpla lá, imíonn siad sa chéad ghlanadh eile, agus laghdaíonn na cinn a fhanann líon na ndaoine a fheiceann do phostálacha, go ciúin.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Daoine fíora ag tabhairt ‘is maith liom’ agus ag déanamh tráchta ar phostáil Instagram cruthaitheora"},
            },
            {
                "h2": "Cárb as a dtagann do leantóirí nua",
                "p": [
                    "Inis dúinn an chathair, an réigiún nó an tír ar cheart do do lucht féachana teacht as. Taispeánaimid do phróifíl do dhaoine fíora ansin ar dtús; má tá an lucht féachana is fearr a oireann níos mó in áit in aice láimhe, d'fhéadfadh níos mó acu teacht as sin.",
                ],
            },
            {
                "h2": "An chuma atá ar mhí amháin",
                "ul": [
                    "Na chéad laethanta: tosaíonn d'fheachtas agus tagann na chéad chuairteanna.",
                    "Gach seachtain: leantóirí nua, ‘is maith liom’ agus tráchtanna, beagán gach lá.",
                    "Faoi dheireadh na míosa: {pick_audience} leantóir nua de ghnáth le {pick_name}.",
                ],
            },
        ],
        "faqs": [
            ("Cé chomh tapa a thagann na leantóirí?", "Beagán gach lá, ar feadh na míosa ar fad. Ní thagann siad uile le chéile choíche: leanann daoine fíora ar a luas féin, agus is róbat é aon rud a thagann ar an toirt."),
            ("An stopfaidh mo leantóirí nua de mo leanúint?", "D'fhéadfadh cuid acu, mar a athraíonn aon lucht féachana fíor. Fanann leantóirí fíora i bhfad níos minice ná róbait, a imíonn ina dtonnta."),
            ("An bhfaighidh mé ‘is maith liom’ agus tráchtanna freisin?", "Gheobhaidh, ó na daoine céanna: {pick_likes} ‘is maith liom’ agus {pick_comments} trácht sa mhí de ghnáth le {pick_name}."),
            ("An bhfuil sé sábháilte do mo chuntas?", "Ní iarraimid do phasfhocal riamh agus ní logálaimid isteach i do chuntas riamh. Aimsíonn daoine do phróifíl agus socraíonn siad dóibh féin, díreach mar a aimsíonn aon leantóir thú."),
            ("An féidir liom a roghnú cárb as mo leantóirí?", "Is féidir. Inis dúinn an chathair, an réigiún nó an tír nuair a ordaíonn tú. Dírímid ansin ar dtús; má tá lucht féachana atá an-chosúil níos mó in aice láimhe, d'fhéadfadh cuid de do leantóirí teacht as sin."),
        ],
    },
    {
        "service": "followers",
        "quantity": 1000,
        "slug": "instagram/leantoiri/1000",
        "label": "{quantity} leantóir Instagram",
        "title": "{quantity} leantóir Instagram ó dhaoine fíora | Growsterr",
        "description": "Bain amach {quantity} leantóir Instagram le daoine fíora, ní le róbait. Tugann {pick_name} {pick_audience} sa mhí de ghnáth, le ‘is maith liom’ agus tráchtanna.",
        "h1": ("{quantity} leantóir Instagram, ", "agus gach duine acu fíor."),
        "intro": "Ní dhíolaimid pacáiste de {quantity} róbat. Fásaimid do chuntas le daoine fíora: tugann {pick_name} {pick_audience} leantóir nua sa mhí de ghnáth, mar sin is iondúil go mbíonn {quantity} ar d'acmhainn sa chéad mhí.",
        "hero": {"image": "instagram-followers-1000", "alt": "Líne ag ardú de leantóirí nua Instagram ag sroicheadh na chéad chloiche míle"},
        "sections": [
            {
                "h2": "Cén fáth nach {quantity} leantóir in uair an chloig?",
                "p": [
                    "Mar ní leanann aon duine fíor cuntas cúpla soicind tar éis íocaíochta. Seirbhísí a sheachadann {quantity} leantóir in uair an chloig, seachadann siad róbait: ní thugann siad ‘is maith liom’, ní dhéanann siad trácht agus imíonn siad ina dtonnta.",
                    "Déanann na cinn a fhanann níos mó damáiste fós. Laghdaíonn gach leantóir nach nglacann páirt riamh an sciar de do lucht féachana a ghlacann páirt, agus sroicheann do phostálacha níos lú daoine, go ciúin.",
                ],
            },
            {
                "h2": "Do chéad mhíle, déanta i gceart",
                "p": [
                    "Athraíonn an chéad mhíle leantóir fíor an chaoi a bhfeiceann cuairteoirí nua thú. Is daoine iad a d'fhéadfadh féachaint ar do Reels, ‘is maith liom’ a thabhairt do do phostálacha agus filleadh, agus is é sin go díreach a chabhraíonn leis an gcéad mhíle eile thú a aimsiú.",
                ],
                "ul": [
                    "Daoine fíora a shocraigh thú a leanúint, ón áit a roghnaíonn tú.",
                    "‘Is maith liom’ agus tráchtanna ó na daoine céanna, laistigh den phacáiste.",
                    "Deais a thaispeánann cad a thomhaiseamar, lá ar lá.",
                ],
            },
        ],
        "faqs": [
            ("Cá fhad a thógann {quantity} leantóir fíor?", "Ag luas tipiciúil, tugann {pick_name} {pick_audience} leantóir nua sa mhí, mar sin is iondúil go mbíonn {quantity} ar d'acmhainn sa chéad mhí. Leanann daoine fíora ar a luas féin, mar sin bíonn gach mí beagán difriúil."),
            ("An pacáiste aon uaire de {quantity} é?", "Ní hea. Díolaimid fás mar phacáistí míosúla. Cosnaíonn {pick_name} {pick_price} sa mhí, agus is féidir leat é a chealú am ar bith ó do chuntas."),
            ("An bhfaighidh mé ‘is maith liom’ agus tráchtanna leo?", "Gheobhaidh, ó na daoine fíora céanna: {pick_likes} ‘is maith liom’ agus {pick_comments} trácht sa mhí de ghnáth le {pick_name}."),
            ("Cad a tharlaíonn tar éis {quantity}?", "Leanann do phacáiste ar aghaidh go dtí go gcealaíonn tú é, mar sin leanann do chuid fáis mí i ndiaidh míosa. Nuair a bheidh d'ábhar réidh le haghaidh tuilleadh, is féidir leat bogadh suas pacáiste."),
        ],
    },
]
