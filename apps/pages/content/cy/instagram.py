"""Welsh Instagram pages: the hub, followers (dilynwyr), and the 1,000-followers goal.
Keys and placeholders: docs/CONTENT.md. Numbers come from the packages ({starter_audience}...)."""

UPDATED = "2026-11-08"

PAGES = [
    {
        # The hub: no service.
        "slug": "instagram",
        "label": "Instagram",
        "title": "Pecynnau twf Instagram i grewyr | Growsterr",
        "description": "Tyfwch ar Instagram gyda phobl go iawn: mae pecynnau misol yn dod â dilynwyr newydd, hoffiadau a sylwadau gan bobl a ddewisodd eich dilyn. O {from_price} y mis.",
        "h1": ("Tyfwch ar Instagram ", "gyda phobl go iawn."),
        "intro": "Eisiau prynu dilynwyr, hoffiadau neu sylwadau Instagram? Dyma'r fersiwn onest: pecynnau twf misol i grewyr a dylanwadwyr. Rydyn ni'n rhoi eich proffil o flaen pobl go iawn, ac mae'r rhai sy'n hoffi'r hyn maen nhw'n ei weld yn eich dilyn, yn hoffi ac yn rhoi sylwadau. Mae eich dangosfwrdd yn dangos beth wnaethon ni ei fesur, dydd wrth ddydd.",
        "hero": {"image": "instagram-hub", "alt": "Proffil crëwr ar Instagram gyda dilynwyr newydd, hoffiadau a sylwadau yn cyrraedd"},
        "sections": [
            {
                "h2": "Twf sy'n edrych fel petaech chi wedi'i ennill",
                "p": [
                    "Mae Instagram yn gwobrwyo cyfrifon y mae pobl wir yn ymgysylltu â nhw. Mae bots yn gwneud y gwrthwyneb: maen nhw'n eistedd yn eich nifer dilynwyr, byth yn hoffi, byth yn gwylio ac yn dysgu'r algorithm nad yw eich postiadau'n werth eu dangos.",
                    "Rydyn ni'n gweithio'r ffordd arall. Mae eich proffil yn cael ei ddangos i bobl go iawn bob dydd, ac mae pob dilyn yn ddewis a wnaeth rhywun. Dyna pam mae hoffiadau, gwyliadau a sylwadau'n cyrraedd gyda'ch dilynwyr, nid fel pryniant ar wahân.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Pobl go iawn yn darganfod postiadau Instagram crëwr ac yn gadael sylwadau"},
            },
            {
                "h2": "Wedi'u gwneud i grewyr sy'n postio gyda phwrpas",
                "p": [
                    "Brand personol, tudalen arbenigol neu fusnes bach: mae'r pecynnau'n tyfu gyda chi. Dechreuwch gyda {starter_name} a symudwch i fyny pan fydd eich cynnwys yn barod am fwy.",
                ],
                "ul": [
                    "Mae Reels, carwseli a phostiadau lluniau i gyd ar eu hennill.",
                    "Chi sy'n dweud wrthon ni o ba ddinas, rhanbarth neu wlad y dylai eich cynulleidfa ddod.",
                    "Mae eich cyfrif yn aros yn eiddo i chi: dydyn ni byth yn gofyn am eich cyfrinair.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "Crëwr yn cynllunio cynnwys Instagram wrth ddesg"},
            },
        ],
        "faqs": [
            ("Ydy'r dilynwyr yn bobl go iawn?", "Ydyn. Mae pob dilynwr yn berson go iawn a welodd eich proffil ac a ddewisodd eich dilyn. Dydyn ni byth yn defnyddio bots, proffiliau ffug na danfon ar unwaith."),
            ("Faint o ddilynwyr mae pecyn yn eu cyflwyno?", "Fel arfer {starter_audience} o ddilynwyr newydd y mis gyda {starter_name}, {rising_audience} gyda {rising_name} a {pro_audience} gyda {pro_name}. Ystodau nodweddiadol yw'r rhain, nid nifer sefydlog: mae pobl go iawn yn penderfynu drostyn nhw'u hunain."),
            ("Oes angen fy nghyfrinair Instagram arnoch chi?", "Byth. Dim ond eich enw defnyddiwr sydd ei angen arnon ni. Cadwch eich cyfrif yn gyhoeddus fel bod y bobl sy'n ei ddarganfod yn gallu eich dilyn."),
            ("Alla i brynu hoffiadau neu sylwadau ar eu pen eu hunain?", "Na. Mae hoffiadau, gwyliadau a sylwadau'n dod y tu mewn i bob pecyn, gan yr un bobl go iawn sy'n eich dilyn. Dyna sy'n cadw eich niferoedd yn naturiol."),
            ("Alla i ganslo unrhyw bryd?", "Gallwch. Mae'r pecynnau'n adnewyddu bob mis a gallwch ganslo o'ch cyfrif. Mae'r mis rydych chi wedi talu amdano'n parhau tan ei ddiwedd."),
        ],
    },
    {
        "service": "followers",
        "slug": "instagram/dilynwyr",
        "label": "Dilynwyr Instagram",
        "title": "Prynwch ddilynwyr Instagram go iawn, bob mis | Growsterr",
        "description": "Prynwch ddilynwyr Instagram sy'n bobl go iawn ac a ddewisodd eich dilyn, gyda hoffiadau a sylwadau gan yr un bobl. Pecynnau misol o {from_price}.",
        "h1": ("Dilynwyr Instagram ", "a ddewisodd eich dilyn."),
        "intro": "Prynwch ddilynwyr Instagram yn y ffordd onest: mae pobl go iawn yn darganfod eich proffil bob dydd, ac mae'r rhai sy'n hoffi'r hyn maen nhw'n ei weld yn eich dilyn. Fel arfer {starter_audience} o ddilynwyr newydd y mis gyda {starter_name}, gyda hoffiadau a sylwadau gan yr un bobl.",
        "hero": {"image": "instagram-followers", "alt": "Proffil Instagram yn cael dilynwyr newydd gan bobl go iawn"},
        "sections": [
            {
                "h2": "Pam mae dilynwyr go iawn yn werth mwy",
                "p": [
                    "Dim ond os oes person y tu ôl iddo y mae dilynwr yn cyfrif. Mae dilynwyr go iawn yn gweld eich postiad nesaf, yn ei hoffi, yn rhoi sylw arno ac yn ei rannu, a'r ymgysylltiad hwnnw y mae Instagram yn edrych arno wrth benderfynu pwy arall ddylai weld eich cynnwys.",
                    "All bots ddim gwneud dim o hynny. Maen nhw'n codi nifer am ychydig ddyddiau, yn diflannu yn y glanhau nesaf, ac mae'r rhai sy'n aros yn tynnu eich cyrhaeddiad i lawr yn dawel.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Pobl go iawn yn hoffi ac yn rhoi sylwadau ar bostiad Instagram crëwr"},
            },
            {
                "h2": "O ble daw eich dilynwyr newydd",
                "p": [
                    "Dywedwch wrthon ni o ba ddinas, rhanbarth neu wlad y dylai eich cynulleidfa ddod. Rydyn ni'n dangos eich proffil i bobl go iawn yno yn gyntaf; lle mae'r gynulleidfa sy'n cyfateb orau yn fwy gerllaw, gall mwy ohonyn nhw ddod oddi yno.",
                ],
            },
            {
                "h2": "Sut olwg sydd ar fis",
                "ul": [
                    "Y dyddiau cyntaf: mae eich ymgyrch yn dechrau ac mae'r ymweliadau cyntaf yn cyrraedd.",
                    "Bob wythnos: dilynwyr newydd, hoffiadau a sylwadau, ychydig bob dydd.",
                    "Erbyn diwedd y mis: fel arfer {pick_audience} o ddilynwyr newydd gyda {pick_name}.",
                ],
            },
        ],
        "faqs": [
            ("Pa mor gyflym mae'r dilynwyr yn dod?", "Ychydig bob dydd, drwy'r mis cyfan. Byth i gyd ar yr un pryd: mae pobl go iawn yn dilyn ar eu cyflymder eu hunain, ac mae unrhyw beth sy'n dod ar unwaith yn fot."),
            ("Fydd fy nilynwyr newydd yn rhoi'r gorau i fy nilyn?", "Gall rhai, fel mae unrhyw gynulleidfa go iawn yn newid. Mae dilynwyr go iawn yn aros yn llawer amlach na bots, sy'n diflannu fesul ton."),
            ("Ydw i'n cael hoffiadau a sylwadau hefyd?", "Ydych, gan yr un bobl: fel arfer {pick_likes} o hoffiadau a {pick_comments} o sylwadau y mis gyda {pick_name}."),
            ("Ydy e'n ddiogel i fy nghyfrif?", "Dydyn ni byth yn gofyn am eich cyfrinair a dydyn ni byth yn mewngofnodi i'ch cyfrif. Mae pobl yn dod o hyd i'ch proffil ac yn penderfynu drostyn nhw'u hunain, yn union fel mae unrhyw ddilynwr yn dod o hyd i chi."),
            ("Alla i ddewis o ble mae fy nilynwyr yn dod?", "Gallwch. Dywedwch wrthon ni'r ddinas, y rhanbarth neu'r wlad wrth archebu. Rydyn ni'n anelu yno yn gyntaf; pan fydd cynulleidfa debyg iawn yn fwy gerllaw, gall rhai o'ch dilynwyr ddod oddi yno."),
        ],
    },
    {
        "service": "followers",
        "quantity": 1000,
        "slug": "instagram/dilynwyr/1000",
        "label": "{quantity} o ddilynwyr Instagram",
        "title": "{quantity} o ddilynwyr Instagram gan bobl go iawn | Growsterr",
        "description": "Cyrhaeddwch {quantity} o ddilynwyr Instagram gyda phobl go iawn, nid bots. Mae {pick_name} fel arfer yn dod â {pick_audience} y mis, gyda hoffiadau a sylwadau.",
        "h1": ("{quantity} o ddilynwyr Instagram, ", "a phob un yn go iawn."),
        "intro": "Dydyn ni ddim yn gwerthu pecyn o {quantity} o fots. Rydyn ni'n tyfu eich cyfrif gyda phobl go iawn: mae {pick_name} fel arfer yn dod â {pick_audience} o ddilynwyr newydd y mis, felly mae {quantity} fel arfer o fewn cyrraedd yn y mis cyntaf.",
        "hero": {"image": "instagram-followers-1000", "alt": "Llinell yn codi o ddilynwyr Instagram newydd yn cyrraedd y garreg filltir gyntaf"},
        "sections": [
            {
                "h2": "Pam nad {quantity} o ddilynwyr mewn awr?",
                "p": [
                    "Oherwydd does dim person go iawn yn dilyn cyfrif eiliadau ar ôl taliad. Mae gwasanaethau sy'n darparu {quantity} o ddilynwyr mewn awr yn darparu bots: dydyn nhw ddim yn hoffi, dydyn nhw ddim yn rhoi sylwadau ac maen nhw'n diflannu fesul ton.",
                    "Mae'r rhai sy'n aros yn gwneud mwy o ddifrod. Mae pob dilynwr sydd byth yn ymgysylltu yn gostwng cyfran y gynulleidfa sy'n ymgysylltu, ac mae eich postiadau'n cyrraedd llai o bobl, yn dawel.",
                ],
            },
            {
                "h2": "Eich mil cyntaf, wedi'i wneud yn iawn",
                "p": [
                    "Mae mil cyntaf o ddilynwyr go iawn yn newid sut mae ymwelwyr newydd yn eich gweld. Maen nhw'n bobl a allai wylio eich Reels, hoffi eich postiadau a dod yn ôl, a dyna'n union sy'n helpu'r mil nesaf i ddod o hyd i chi.",
                ],
                "ul": [
                    "Pobl go iawn sydd wedi dewis eich dilyn, o'r lleoliad a ddewiswch.",
                    "Hoffiadau a sylwadau gan yr un bobl, y tu mewn i'r pecyn.",
                    "Dangosfwrdd sy'n dangos beth wnaethon ni ei fesur, dydd wrth ddydd.",
                ],
            },
        ],
        "faqs": [
            ("Faint o amser mae {quantity} o ddilynwyr go iawn yn ei gymryd?", "Ar gyflymder nodweddiadol, mae {pick_name} yn dod â {pick_audience} o ddilynwyr newydd y mis, felly mae {quantity} fel arfer o fewn cyrraedd yn y mis cyntaf. Mae pobl go iawn yn dilyn ar eu cyflymder eu hunain, felly mae pob mis ychydig yn wahanol."),
            ("Ai pecyn untro o {quantity} yw hwn?", "Na. Rydyn ni'n gwerthu twf fel pecynnau misol. Mae {pick_name} yn {pick_price} y mis, a gallwch ganslo unrhyw bryd o'ch cyfrif."),
            ("Ydw i'n cael hoffiadau a sylwadau gyda nhw?", "Ydych, gan yr un bobl go iawn: fel arfer {pick_likes} o hoffiadau a {pick_comments} o sylwadau y mis gyda {pick_name}."),
            ("Beth sy'n digwydd ar ôl {quantity}?", "Mae eich pecyn yn parhau nes i chi ei ganslo, felly mae eich twf yn parhau fis ar ôl mis. Pan fydd eich cynnwys yn barod am fwy, gallwch symud i fyny i becyn mwy."),
        ],
    },
]
