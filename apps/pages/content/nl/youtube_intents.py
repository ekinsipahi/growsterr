UPDATED = "2026-11-08"

# Dutch YouTube intent pages: zoekopdrachten naar wat we niet verkopen (goedkoop, direct, gratis,
# gratis proefperiode, panels). Elke pagina antwoordt eerlijk en leidt naar het maandpakket.
# Keys and placeholders: docs/CONTENT.md; angles: docs/keywords/WRITING.md.

PAGES = [
    # --- Abonnees ------------------------------------------------------------------------
    {
        "service": "subscribers",
        "modifier": "cheap",
        "slug": "youtube/abonnees/goedkoop",
        "label": "Goedkope YouTube-abonnees?",
        "plan": "starter",
        "title": "YouTube-abonnees kopen voor $1? Wat ze u kosten | Growsterr",
        "description": "YouTube-abonnees van $1 kijken nooit en worden opgeruimd. Voor {starter_price} per maand brengt {starter_name} doorgaans {starter_audience} echte kijkers.",
        "h1": ("YouTube-abonnees van $1 ", "kijken nooit één video."),
        "intro": "Overweegt u YouTube-abonnees te kopen voor $1? Voor die prijs krijgt u accounts die nooit zullen kijken, liken of reageren, en YouTube haalt spamaccounts regelmatig uit abonneeaantallen. Wij vragen meer en brengen kijkers: {starter_audience} nieuwe abonnees in een typische maand met {starter_name}, voor {starter_price}, stuk voor stuk mensen die uw kanaal vonden en besloten zich te abonneren.",
        "hero": {"image": "youtube-subscribers", "alt": "Het abonneeaantal van een YouTube-kanaal groeit met echte kijkers"},
        "sections": [
            {
                "h2": "De prijs van een abonnee die nooit kijkt",
                "p": [
                    "Op YouTube telt wat abonnees doen zwaarder dan hoeveel het er zijn. Een lijst vol accounts die nooit op play drukken, laat elke nieuwe upload minder interessant lijken dan hij is.",
                    "Een goedkope abonnee is dus niet goedkoop. U betaalt één keer met geld en nog een keer met de views die u misloopt.",
                ],
            },
            {
                "h2": "Wat een echte abonnee kost",
                "p": [
                    "Neem {starter_name}: {starter_price} per maand, en doorgaans {starter_audience} abonnees die echte kijkers zijn uit de plek die u kiest. Per persoon is dat een kwestie van centen, en hun likes en reacties zitten bij de prijs inbegrepen.",
                ],
            },
            {
                "h2": "Een lage prijs zonder het risico",
                "ul": [
                    "Geen wachtwoord en geen toegang tot uw Google-account: alleen uw kanaalhandle.",
                    "Maandelijks betalen met uw kaart via Stripe, opzegbaar vanuit uw account.",
                    "Abonnees, likes en reacties voor één prijs, van dezelfde mensen.",
                ],
            },
        ],
        "faqs": [
            ("Wat kosten echte YouTube-abonnees?", "Onze pakketten beginnen bij {starter_price} per maand. {starter_name} brengt doorgaans {starter_audience} nieuwe abonnees; {rising_name}, voor {rising_price}, brengt {rising_audience}; {pro_name}, voor {pro_price}, brengt {pro_audience}."),
            ("Waarom verkopen sommige sites abonnees zo goedkoop?", "Omdat ze accounts verkopen, geen kijkers. Accounts in bulk aanmaken of huren kost bijna niets; mensen vinden die uw kanaal willen bekijken wel."),
            ("Is er een heel goedkope optie voor een klein kanaal?", "{starter_name} is gemaakt voor nieuwe en kleine kanalen, en het is onze laagste prijs."),
            ("Kunnen goedkope abonnees mijn kanaal in de problemen brengen?", "Dat kan. Het beleid van YouTube over nep-engagement geldt ook voor gekochte abonnees, en kanalen die ze gebruiken, lopen het risico dat video's worden verwijderd of het kanaal wordt bestraft."),
            ("Zitten views bij de prijs inbegrepen?", "Ja. Uw nieuwe abonnees kijken, liken en reageren uit zichzelf, allemaal binnen het pakket. We plakken geen getal op views, want elke view is iemand die ervoor kiest op play te drukken."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "fast",
        "slug": "youtube/abonnees/snel",
        "label": "Snel YouTube-abonnees?",
        "title": "Snel YouTube-abonnees kopen: echt, niet direct | Growsterr",
        "description": "Echte, directe én actieve YouTube-abonnees bestaan niet tegelijk. De onze zijn echt en actief: uw campagne start binnen dagen en abonnees komen dagelijks.",
        "h1": ("Echt, actief én direct? ", "Maar twee daarvan kunnen kloppen."),
        "intro": "Wilt u snel YouTube-abonnees kopen die echt, direct en actief tegelijk zijn? Maar twee daarvan kunnen samen kloppen. Directe abonnees zijn geen mensen, en echte mensen abonneren zich niet op de seconde dat u betaalt. Wij brengen snel echte, actieve abonnees: de campagne loopt binnen de eerste dagen, en vanaf dan voegt {pick_name} er doorgaans {pick_audience} per maand toe, elke dag een paar.",
        "hero": {"image": "youtube-subscribers", "alt": "Nieuwe abonnees sluiten zich dag na dag aan bij een YouTube-kanaal"},
        "sections": [
            {
                "h2": "Waarom direct op YouTube nep betekent",
                "p": [
                    "Een echt mens abonneert zich nadat hij iets heeft bekeken: een video, een Short, een kanaaltrailer. Dat kost minstens minuten, en het gebeurt wanneer hij eraan toekomt. Abonnees die per honderd verschijnen vlak na een betaling, hebben het kijken overgeslagen, en dat zegt dat het geen mensen waren.",
                ],
            },
            {
                "h2": "Hoe snel echte abonnees komen",
                "p": [
                    "Het opzetten kost de eerste dagen na uw bestelling. Vanaf dan vinden elke dag nieuwe kijkers uw kanaal, en wie leuk vindt wat hij ziet, abonneert zich. Het dashboard toont elke dag zoals wij die meten, dus u ziet het tempo vanaf de eerste week.",
                ],
            },
            {
                "h2": "Snelheid waar u iets aan hebt",
                "ul": [
                    "Upload terwijl de campagne loopt, zodat nieuwe abonnees iets hebben om hierna te bekijken.",
                    "Maak uw kanaalpagina op orde: een duidelijke banner, een trailer en playlists in een logische volgorde.",
                    "Kies {pro_name} voor het grootste maandbereik: doorgaans {pro_audience} nieuwe abonnees.",
                ],
            },
        ],
        "faqs": [
            ("Hoe snel stijgt mijn abonneeaantal?", "Binnen de eerste dagen van uw campagne: eerst met een paar tegelijk, daarna elke dag, de hele maand door."),
            ("Kunnen jullie direct 1.000 abonnees toevoegen?", "Nee, met echte mensen kan niemand dat. Duizend in een uur betekent duizend accounts die nooit zullen kijken, en precies die ruimt YouTube op."),
            ("Zijn jullie abonnees actief?", "Het zijn echte mensen die zich abonneerden nadat ze uw kanaal zagen, dus ze zijn zo actief als elke kijker: ze kijken, liken en reageren als een video hen interesseert."),
            ("Welk pakket is het snelst?", "{pro_name} brengt elke maand de meeste: doorgaans {pro_audience} nieuwe abonnees. {starter_name} en {rising_name} brengen kleinere bereiken, op dezelfde manier over de maand verspreid."),
            ("Schaadt snelle groei mijn kanaal?", "Niet in dit tempo. Abonnees komen dagelijks van echte kijkers, en zo winnen groeiende kanalen ze sowieso."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "free",
        "slug": "youtube/abonnees/gratis",
        "label": "Gratis YouTube-abonnees?",
        "plan": "starter",
        "tool": "growth-calculator",
        "title": "Gratis YouTube-abonnees? Een beter plan | Growsterr",
        "description": "Gratis YouTube-abonnees komen van sub-for-sub-ruilen of bots. Die bieden we niet, maar onze gratis groeicalculator laat zien hoe lang echte groei duurt.",
        "h1": ("Gratis YouTube-abonnees? ", "Plan liever voor echte."),
        "intro": "Zoekt u gratis YouTube-abonnees, of 1.000 voor $5? Geen van beide brengt mensen die kijken: gratis aanbiedingen draaien op sub-for-sub-ruilen of botaccounts. Wij geven geen abonnees weg. Het gratis deel van deze pagina is de groeicalculator: vul in waar uw kanaal nu staat en waar u heen wilt, en hij schat hoeveel maanden elk pakket doorgaans nodig heeft.",
        "hero": {"image": "youtube-channel", "alt": "Een YouTuber plant een abonneedoel voor de komende maanden"},
        "sections": [
            {
                "h2": "Sub-for-sub en andere gratis trucs",
                "ul": [
                    "Sub-for-sub-groepen: u abonneert zich op vreemden, zij abonneren zich terug, en niemand kijkt naar iemand.",
                    "Gratis abonneesites die vragen in te loggen met Google en daarna uw account gebruiken om zich op anderen te abonneren.",
                    "Piepkleine gratis partijen van botaccounts, aangeboden zodat u een grotere koopt.",
                ],
                "p": [
                    "Ze vullen allemaal uw aantal met mensen die geen interesse hebben in uw video's, en dat is erger dan minder abonnees hebben.",
                ],
            },
            {
                "h2": "Over die 1.000",
                "p": [
                    "Duizend abonnees is voor veel kanalen een mijlpaal, vaak vanwege het YouTube-partnerprogramma. Gekochte of geruilde abonnees voegen geen kijktijd toe, en YouTube behandelt ze als nep-engagement. Monetisatie beloven wij ook niet: we brengen echte kijkers, en de rest hangt af van uw video's en van YouTube.",
                ],
            },
            {
                "h2": "Plan het met de groeicalculator",
                "p": [
                    "De calculator bovenaan is gratis en werkt in uw browser. Vul uw abonneeaantal in waar hij om uw huidige volgers vraagt, en uw doel als doel. Hij rekent uit hoeveel maanden elk pakket doorgaans nodig heeft, op basis van het typische maandbereik van elk pakket.",
                ],
            },
        ],
        "faqs": [
            ("Kan ik gratis YouTube-abonnees krijgen?", "Geen echte van ons. Elke abonnee die we brengen, is een kijker die via een betaalde campagne is bereikt. De calculator hier is het gratis deel, en die kunt u zo vaak gebruiken als u wilt."),
            ("Zijn 1.000 YouTube-abonnees voor $5 echt?", "Geen echte campagne vindt voor vijf dollar duizend mensen die uw kanaal willen. Voor die prijs zijn de abonnees accounts, geen kijkers."),
            ("Hoe lang duurt het om 1.000 echte abonnees te halen?", "Dat hangt af van uw startpunt. {starter_name} brengt doorgaans {starter_audience} nieuwe abonnees per maand; vul uw eigen cijfers in de calculator hierboven in om de maanden voor uw kanaal te zien."),
            ("Is sub-for-sub in strijd met de regels van YouTube?", "Ja. Het beleid van YouTube over nep-engagement geldt ook voor het ruilen van abonnementen, dus het kan een kanaal in gevaar brengen. Bovendien levert het abonnees op die nooit kijken."),
            ("Waar begint een klein kanaal het best?", "Met {starter_name}, voor {starter_price} per maand, en zonder contract na de maand waarin u zit."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "free-trial",
        "slug": "youtube/abonnees/gratis-proefperiode",
        "label": "Gratis proefperiode YouTube-abonnees?",
        "plan": "starter",
        "title": "YouTube-abonnees met gratis proefperiode? | Growsterr",
        "description": "Geen gratis proefperiode voor YouTube-abonnees: een proefje van één dag bewijst niets. Uw eerste maand toont echte kijkers, gemeten, zonder contract.",
        "h1": ("Een gratis proef met YouTube-abonnees ", "bewijst niets. Een maand wel."),
        "intro": "Wilt u YouTube-abonnees kopen na een gratis proefperiode? Dan zijn we eerlijk: die bieden we niet. Een proef van 100 abonnees op één dag zou alleen laten zien dat een verkoper accounts over heeft. Uw eerste maand is hoe u ons beoordeelt: {starter_name} voor {starter_price}, echte kijkers vanaf de eerste dagen, een dashboard met wat we hebben gemeten en geen contract na die maand.",
        "hero": {"image": "youtube-hub", "alt": "De statistieken van een YouTube-kanaal tijdens een eerste maand echte groei"},
        "sections": [
            {
                "h2": "Wat een proef u niet kan laten zien",
                "p": [
                    "De vraag is niet of een getal omhoog kan. De vraag is of echte mensen kijken, liken en blijven, en dat ziet u pas na weken. Een proefje van één dag is een verkooptruc, geen test.",
                ],
            },
            {
                "h2": "Zo controleert u ons tijdens de maand",
                "ul": [
                    "Open het dashboard om de paar dagen: bezoeken uit de campagne en nieuwe abonnees, zoals gemeten.",
                    "Bekijk uw videostatistieken: kijken nieuwe kijkers echt?",
                    "Lees de reacties: mensen die in eigen woorden over uw video's schrijven.",
                    "Beslis vóór de verlengdatum; u kunt op elk moment opzeggen vanuit uw account.",
                ],
            },
        ],
        "faqs": [
            ("Hebben jullie een gratis proefperiode voor YouTube?", "Nee. We doen geen proefperiodes, op geen enkel platform. Een maand is het kortste pakket, en u kunt opzeggen voordat de volgende begint."),
            ("Waarom geen proef als andere sites die wel bieden?", "Elke abonnee die we brengen, komt uit een echte campagne die vanaf dag één geld kost. Verkopers die gratis proefjes kunnen weggeven, sturen meestal accounts, geen kijkers."),
            ("Wat gebeurt er als ik na één maand opzeg?", "Er wordt niets meer afgeschreven, en de betaalde maand loopt door tot het einde. Echte abonnees worden niet teruggenomen; ze blijven, tenzij ze zelf besluiten te vertrekken."),
            ("Zie ik binnen de eerste maand resultaat?", "U ziet het tempo: elke dag nieuwe abonnees, doorgaans {starter_audience} over de maand met {starter_name}. Typisch, niet vast, want elke abonnee is iemand die zelf beslist."),
            ("Kan ik eerst een kleiner pakket proberen?", "{starter_name} is ons kleinste en de logische plek om te beginnen. Later kunt u opschalen als uw kanaal meer nodig heeft."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "smm-panel",
        "slug": "youtube/abonnees/smm-panel",
        "label": "YouTube-abonnees via een SMM-panel?",
        "title": "YouTube-abonnees kopen via een SMM-panel? | Growsterr",
        "description": "SMM-panels verkopen YouTube-abonnees en views per duizend, met aanvullingen omdat ze dalen. Wij zijn een bureau: echte kijkers en een gemeten dashboard.",
        "h1": ("Panelabonnees komen met een aanvulknop. ", "De onze hebben er geen nodig."),
        "intro": "Voordat u YouTube-abonnees of views koopt via een SMM-panel, let op de aanvuloptie die panels er vaak naast zetten: ze verwachten dat de aantallen dalen. Panels verkopen botverkeer in bulk door. Wij werken als bureau: mensen uit ons team houden uw campagne in de gaten, echte kijkers vinden uw kanaal en abonneren zich, en het dashboard rapporteert wat we hebben gemeten.",
        "hero": {"image": "youtube-channel", "alt": "Een creator bekijkt een dashboard met gemeten nieuwe YouTube-abonnees"},
        "sections": [
            {
                "h2": "Abonnees en views per duizend",
                "p": [
                    "Op een panel staan YouTube-abonnees, views en kijktijd in één lijst, geprijsd per duizend, met opmerkingen over starttijden en aanvullingen. Niemand kijkt naar uw kanaal. De bestelling gaat in een wachtrij, en accounts doen wat de wachtrij zegt.",
                    "Panelviews werken net zo: weergaven zonder dat iemand besloot te kijken, het soort dat YouTube uit viewaantallen probeert te filteren.",
                ],
            },
            {
                "h2": "Wat er verandert met een bureau",
                "ul": [
                    "Mensen in plaats van wachtrijen: uw kanaal wordt elke dag aan echte kijkers getoond.",
                    "Elke abonnee, like, view en reactie is terug te voeren op een mens.",
                    "Een team achter uw campagne, en een manier om ons te bereiken als u vragen hebt.",
                    "Een dashboard met wat we hebben gemeten, geen teller die moet worden bijgevuld.",
                ],
            },
        ],
        "faqs": [
            ("Zijn panelabonnees echte mensen?", "Nee. Panels verkopen bulkverkeer door van accounts die zich op instructie abonneren, en daarom horen aanvullingen bij het aanbod."),
            ("Verkopen jullie YouTube-views los?", "Nee. Views zijn geen aparte regel. Ze komen van de mensen die onze campagne bereikt, dezelfden die zich abonneren, liken en reageren."),
            ("Kunnen panelviews mijn kanaal in de problemen brengen?", "Ja. Kunstmatige views overtreden de regels van YouTube over nep-engagement; ze kunnen uit uw aantal worden gehaald, en herhaald gebruik brengt het kanaal in gevaar."),
            ("Bieden jullie een wederverkoperspanel aan?", "Nee. We verkopen niet in bulk of via wederverkopers: elk pakket is een campagne rond één kanaal. Bureaus met meerdere kanalen kunnen contact opnemen om het te bespreken."),
            ("Wat brengt een pakket per maand?", "{pick_name} brengt doorgaans {pick_audience} nieuwe abonnees per maand, echte kijkers die verspreid over alle 30 dagen binnenkomen."),
        ],
    },
    # --- Views ----------------------------------------------------------------------------
    {
        "service": "views",
        "modifier": "cheap",
        "slug": "youtube/views/goedkoop",
        "label": "Goedkope YouTube-views?",
        "plan": "starter",
        "title": "Goedkoop YouTube-views kopen? Wat een dollar oplevert | Growsterr",
        "description": "Goedkope YouTube-views voor een dollar per duizend zijn weergaven, geen kijkers. Ons maandpakket brengt echte mensen die kijken, abonneren en reageren.",
        "h1": ("Goedkope YouTube-views ", "zijn weergaven, geen kijkers."),
        "intro": "Bent u van plan goedkoop YouTube-views te kopen, zeg duizend voor een dollar? Weet dan wat er binnenkomt: weergaven van scripts of bulkaccounts die hooguit een paar seconden kijken, en die YouTube uit uw aantal kan halen. Views verkopen we niet los. Ons maandpakket brengt echte mensen naar uw kanaal, en die kijken, liken, reageren en abonneren uit eigen keuze.",
        "hero": {"image": "youtube-viewers", "alt": "Echte kijkers bekijken een YouTubevideo tot het eind"},
        "sections": [
            {
                "h2": "Wat een view waard is",
                "p": [
                    "Een view helpt als er een mens kijkt. Hoe lang hij blijft, of hij liket en welke video hij daarna aanklikt, laat YouTube zien dat een video meer kijkers verdient. Een goedkope view telt één op bij de teller en geeft YouTube niets om mee te werken.",
                    "Een groot viewaantal met bijna geen kijktijd geeft bovendien een tegenstrijdig signaal, en de gekochte weergaven kunnen hoe dan ook worden verwijderd.",
                ],
            },
            {
                "h2": "Een YouTube-viewpakket, de eerlijke soort",
                "p": [
                    "We verkopen wel een pakket, alleen geen pakket views. {starter_name} kost {starter_price} per maand: doorgaans {starter_audience} nieuwe abonnees, {starter_likes} likes en {starter_comments} reacties van echte kijkers, plus de views die diezelfde mensen aan uw video's geven.",
                    "Views tellen we niet vooraf. Ze volgen uw content in plaats van een quotum, want elke view is iemands keuze.",
                ],
            },
            {
                "h2": "Prijs per view of prijs per kijker",
                "p": [
                    "Tel kijkers, geen views. Eén echte abonnee kan tientallen van uw video's bekijken in de maanden dat hij blijft. Een dollar aan gescripte weergaven kijkt na vandaag niets meer.",
                ],
            },
        ],
        "faqs": [
            ("Wat kosten YouTube-views bij jullie?", "Views hebben geen eigen prijs. Het kleinste pakket, {starter_name}, kost {starter_price} per maand en brengt abonnees, likes en reacties, met views van diezelfde mensen."),
            ("Waarom zijn views voor 1 dollar zo goedkoop?", "Omdat niemand ernaar kijkt. Scripts en bulkaccounts maken weergaven voor bijna niets, en weergaven is alles wat ze maken."),
            ("Brengen goedkope views mij echte kijkers?", "Waarschijnlijk niet. YouTube kijkt naar hoe mensen op een video reageren, niet alleen naar het aantal, en gekochte views reageren niet."),
            ("Kan ik kiezen welke video's kijkers krijgen?", "Nee. De campagne promoot uw kanaal als geheel, en kijkers kiezen wat ze bekijken. Sterke titels en thumbnails helpen hen uw beste werk te vinden."),
            ("Is er een heel goedkoop pakket alleen voor views?", "Een pakket met alleen views onder {starter_name} voor {starter_price} per maand bestaat niet, want views komen van de mensen die een pakket brengt."),
        ],
    },
    {
        "service": "views",
        "modifier": "fast",
        "slug": "youtube/views/snel",
        "label": "Snel YouTube-views?",
        "title": "Snel YouTube-views kopen? Zo komen echte kijkers | Growsterr",
        "description": "Directe YouTube-views, ook voor premières, komen van scripts. Echte kijkers vinden uw kanaal vanaf de eerste dagen van uw campagne en blijven komen.",
        "h1": ("Snel YouTube-views? ", "Kijkers worden niet bezorgd."),
        "intro": "Wilt u snel YouTube-views kopen, met directe levering? Views die op een timer worden geleverd, komen van scripts, niet van mensen: een echte kijker klikt als een video zijn aandacht trekt. Wij verkopen en leveren geen views. We brengen elke dag echte mensen naar uw kanaal, vanaf de eerste dagen van uw campagne, en die kijken, liken en abonneren uit zichzelf.",
        "hero": {"image": "youtube-viewers", "alt": "Kijkers ontdekken de nieuwe YouTube-upload van een creator"},
        "sections": [
            {
                "h2": "Snelle levering is een pakketpostwoord",
                "p": [
                    "Levertijden zijn logisch voor dingen in dozen. Bij views betekent een leversnelheid dat een machine op play drukt, en die weergaven komen zonder kijktijd die iets waard is.",
                ],
            },
            {
                "h2": "Premièreviews hebben echte mensen nodig",
                "p": [
                    "Een première is een moment: mensen die wachten, chatten en samen kijken. Gekochte premièreviews kunnen een teller vullen, maar nooit de chat. Wij kunnen ook geen publiek naar een vaste minuut brengen, en we gaan niet doen alsof.",
                    "Wat helpt, is een grotere basis van echte abonnees, die de première op hun startpagina of in hun abonnementenfeed kunnen zien en op herinneren kunnen tikken.",
                ],
            },
            {
                "h2": "Hoe snel echte views opbouwen",
                "ul": [
                    "In de eerste dagen gaat uw campagne live en bereiken nieuwe kijkers uw kanaal.",
                    "Elke upload deze maand staat klaar voor de mensen die zich vorige week abonneerden.",
                    "Views blijven van die abonnees komen zolang ze van uw video's genieten.",
                ],
            },
        ],
        "faqs": [
            ("Hoe snel stijgen mijn views?", "Zodra de campagne live is, en dat gebeurt in de eerste dagen, stijgen views naarmate nieuwe mensen uw kanaal vinden. Ze groeien mee met uw publiek in plaats van op één video te springen."),
            ("Kunnen jullie directe views naar een nieuwe upload sturen?", "Nee. Directe views komen van scripts. Echte views op een nieuwe upload komen van mensen die hem in hun feed of aanbevelingen zien, en het is onze taak die groep te laten groeien."),
            ("Kunnen jullie mijn première vullen met livekijkers?", "Niemand kan echte mensen op een bepaalde minuut beloven. Echte abonnees laten groeien vóór een première geeft u meer mensen die misschien afstemmen."),
            ("Worden views meegeteld in mijn pakket?", "Ze zitten erin, zonder vast aantal. Dezelfde mensen die abonneren, liken en reageren, kijken ook, dus views volgen uw publiek."),
            ("Welk pakket brengt de meeste views?", "We bepalen de omvang van pakketten niet op views. Een groter pakket bereikt meer mensen, dus {pro_name}, met doorgaans {pro_audience} nieuwe abonnees per maand, betekent meestal meer mensen die kijken."),
        ],
    },
    {
        "service": "views",
        "modifier": "free",
        "slug": "youtube/views/gratis",
        "label": "Gratis YouTube-views?",
        "plan": "starter",
        "tool": "engagement-calculator",
        "title": "1.000 gratis YouTube-views? Waarom ze niet helpen | Growsterr",
        "description": "Gratis YouTube-views, ook voor Shorts, komen van ruilsites en scripts. Wij geven geen views weg; check uw engagement met onze gratis calculator.",
        "h1": ("1.000 gratis YouTube-views ", "kijken uw video niet. Echte mensen wel."),
        "intro": "Aanbiedingen voor 1.000 gratis YouTube-views, of gratis Shorts-views, draaien op viewruil, autoplaytrucs of botweergaven, en geen ervan brengt iemand die kijkt. Wij geven geen views weg. De engagementcalculator hieronder kost niets, en hij vertelt u welk deel van uw abonnees op een typische video reageert. Wilt u dat meer echte mensen kijken, dan brengen onze pakketten ze.",
        "hero": {"image": "youtube-channel", "alt": "Een YouTuber bekijkt likes en reacties op recente video's"},
        "sections": [
            {
                "h2": "Waar gratis views vandaan komen",
                "ul": [
                    "Viewruil: u bekijkt video's van vreemden voor tegoed, en zij spelen de uwe af met het geluid uit.",
                    "Embeds en autoplaytrucs die een weergave tellen die niemand koos.",
                    "Botweergaven die in kleine partijen worden uitgedeeld om u grotere te verkopen.",
                    "Gratis Shorts-views van scripts die na een seconde wegswipen.",
                ],
            },
            {
                "h2": "Controleer uw engagement met de calculator",
                "p": [
                    "Deze calculator draait volledig in uw browser, kosteloos. Waar hij om volgers vraagt, vult u uw abonnees in; voeg daarna het gemiddelde aantal likes en reacties op uw recente video's toe. De uitkomst is het deel van uw publiek dat reageert, een veel betere gezondheidscheck dan een viewaantal.",
                ],
            },
            {
                "h2": "Gratis manieren om meer views te verdienen",
                "ul": [
                    "Besteed net zoveel tijd aan titel en thumbnail als aan de montage; die bepalen de klik.",
                    "Kom in de eerste seconden van een video of Short ter zake.",
                    "Voeg eindschermen en playlists toe, zodat de ene view naar de volgende leidt.",
                    "Beantwoord reacties; mensen komen terug naar gesprekken.",
                ],
            },
        ],
        "faqs": [
            ("Kan ik gratis 1.000 YouTube-views krijgen?", "Niet van echte mensen, en niet van ons. Een gratis duizend komt van ruilsites of scripts. De calculator op deze pagina is het deel dat echt gratis is."),
            ("Zijn gratis Shorts-views anders?", "Nee. Ze komen van dezelfde trucs. Een Short reist alleen als echte mensen hem uitkijken, dus weergaven van scripts helpen hem niet."),
            ("Kunnen gratis views mijn kanaal een straf opleveren?", "Dat is een reëel risico. Views van geautomatiseerde systemen of ruilsites vallen onder het beleid van YouTube over nep-engagement, waardoor YouTube ze kan verwijderen of tegen het kanaal kan optreden."),
            ("Hebben jullie een gratis viewpakket?", "Nee. Het kleinste pakket is {starter_name} voor {starter_price} per maand, en views zitten erin, van de echte mensen die zich abonneren."),
            ("Wat vertelt de engagementratio mij?", "Hoeveel van uw publiek er echt is. Een lage ratio met een groot abonneeaantal betekent meestal dat veel abonnees zijn gestopt met kijken, of dat nooit deden."),
        ],
    },
    {
        "service": "views",
        "modifier": "free-trial",
        "slug": "youtube/views/gratis-proefperiode",
        "label": "Gratis proefperiode YouTube-views?",
        "plan": "starter",
        "title": "YouTube-views met gratis proefperiode? Test ons echt | Growsterr",
        "description": "Een gratis proefperiode voor YouTube-views is er niet, en views verkopen we niet los. Test ons met één maand echte kijkers en de statistieken van YouTube.",
        "h1": ("Een proef met YouTube-views ", "bewijst alleen dat een teller kan bewegen."),
        "intro": "Hoopt u YouTube-views te kopen met een gratis proefperiode, voordat u iets betaalt? Hier is geen proef, en views worden ook nooit los verkocht. Een proef van een paar duizend views in een uur zou alleen laten zien dat iemand scripts heeft. Wat wij bieden, is een maandpakket dat echte mensen naar uw kanaal brengt, met views van diezelfde mensen, en u kunt altijd opzeggen.",
        "hero": {"image": "youtube-hub", "alt": "Een creator vergelijkt YouTube-statistieken met een groeidashboard"},
        "sections": [
            {
                "h2": "Wat een viewproef meet",
                "p": [
                    "Eén ding: of het getal beweegt. Het zegt niets over wie keek, hoe lang, of dat iemand terugkwam. Dat zijn de vragen die ertoe doen, en alleen echte kijkers kunnen ze beantwoorden.",
                ],
            },
            {
                "h2": "Test ons met de eigen cijfers van YouTube",
                "p": [
                    "Open in uw eerste maand YouTube Studio naast ons dashboard. Kijk naar terugkerende kijkers, gemiddelde kijkduur en nieuwe abonnees. Echte mensen laten in die cijfers een spoor achter dat gekochte weergaven nooit achterlaten.",
                ],
            },
        ],
        "faqs": [
            ("Is er een proefperiode voor YouTube-views?", "Geen proefperiodes, voor views of voor iets anders. De kortste verbintenis is één maand van een pakket, en u kunt opzeggen voordat die verlengt."),
            ("Kan ik een klein viewpakket kopen om te testen?", "We verkopen views niet als apart pakket, klein of groot. {starter_name}, voor {starter_price} per maand, is de kleinste manier om te beginnen."),
            ("Hoe onderscheid ik echte views van gekochte?", "Kijk verder dan het aantal: kijktijd, terugkerende kijkers en de reacties die mensen schrijven, vertellen u wie er echt is."),
            ("Wat als ik na de eerste maand opzeg?", "Uw pakket stopt als de betaalde maand afloopt. Kijkers die zich abonneerden, blijven geabonneerd, tenzij ze zelf besluiten te vertrekken."),
            ("Komen views samen met abonnees?", "Ja. Elk pakket brengt nieuwe abonnees, likes en reacties, en diezelfde mensen bekijken uw video's."),
        ],
    },
]
