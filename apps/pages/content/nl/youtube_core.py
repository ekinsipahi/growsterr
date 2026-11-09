"""Dutch YouTube pages naast de hub en abonnees: likes, views en de manieren waarop mensen naar
abonnees vragen (echt, veilig, maandelijks...). Keys and placeholders: docs/CONTENT.md. Brief:
docs/keywords/WRITING.md. Views worden nooit vooraf geteld; we beloven nooit monetisatie,
kijkuren of kijkduur."""

UPDATED = "2026-11-08"

PAGES = [
    # --- Likes ---------------------------------------------------------------------------
    {
        "service": "likes",
        "slug": "youtube/likes",
        "label": "YouTube-likes",
        "title": "YouTube-likes kopen? Echte kijkers, in een pakket | Growsterr",
        "description": "YouTube-likes kopen? Elke like in onze pakketten komt van een kijker die keek, samen met nieuwe abonnees en reacties. Vanaf {from_price} per maand.",
        "h1": ("Wilt u YouTube-likes kopen? ", "Krijg ze van mensen die keken."),
        "intro": "Kwam u hier om YouTube-likes te kopen? Eerst een eerlijk antwoord: likes verkopen we niet per bundel. Elk pakket brengt echte mensen naar uw kanaal die uw video's bekijken en de video's liken die ze goed vinden, doorgaans {starter_likes} likes per maand met {starter_name} en meer met de grotere pakketten.",
        "hero": {"image": "youtube-viewers", "alt": "Kijkers op hun telefoon liken een YouTubevideo die ze net hebben bekeken"},
        "sections": [
            {
                "h2": "Wat een like YouTube vertelt",
                "p": [
                    "Een like is een kleine, openbare stem van iemand die op play drukte. YouTube leest hem samen met alles wat die kijker nog meer deed: hoe lang hij keek, of hij zich abonneerde, of hij terugkwam voor de volgende upload.",
                    "Een like van een account dat nooit keek, doorbreekt dat patroon. De teller onder uw video stijgt terwijl alles eromheen stil blijft, en YouTube behandelt engagement dat het als kunstmatig beoordeelt als spam.",
                ],
            },
            {
                "h2": "Waar de likes terechtkomen: video's, muziek en posts",
                "p": [
                    "Nieuwe kijkers liken wat ze goed vinden, meestal uw nieuwste uploads en de video die hen naar uw kanaal bracht. Muzikanten zien hetzelfde bij muziekvideo's en lyricvideo's: likes van luisteraars die het nummer afspeelden en meer wilden.",
                    "Communityposts werken anders. Uw abonnees zien ze in hun feed en liken ze misschien uit zichzelf, maar de bereiken die wij noemen, gaan over likes op uw video's.",
                ],
                "image": {"image": "youtube-channel", "alt": "Een muzikant neemt in een thuisstudio een nummer op voor een YouTube-muziekvideo"},
            },
            {
                "h2": "Waarom likes samen met abonnees komen",
                "p": [
                    "Een like is het lichtste wat een kijker kan doen. In een pakket komt hij met zwaardere signalen van dezelfde mensen: een abonnement, een reactie, een terugkeer voor de volgende video. Stijgen die cijfers samen, dan beschrijven ze een kanaal waar mensen van genieten, want dat is het ook.",
                ],
            },
        ],
        "faqs": [
            ("Kan ik YouTube-likes kopen zonder abonnees?", "Nee. Likes zitten in elk pakket, samen met nieuwe abonnees en reacties van dezelfde echte mensen. Een like zonder iemand die erachter kijkt, is het soort engagement dat YouTube als spam behandelt."),
            ("Hoeveel likes brengt een typische maand?", "Met {pick_name} doorgaans {pick_likes}, ongeveer twee tot drie likes per nieuwe abonnee. Echte mensen bepalen wat ze liken, dus geen twee maanden zijn gelijk."),
            ("Kan ik likes krijgen op een YouTube-communitypost?", "Niet als aparte bestelling. Uw nieuwe abonnees kunnen uw communityposts in hun feed zien, en sommigen liken ze omdat ze dat willen. De typische bereiken in elk pakket tellen likes op video's."),
            ("Krijgen muziekvideo's ook likes?", "Ja. Is uw kanaal muziek, dan zijn de mensen die we brengen luisteraars die uw nummers afspeelden en de nummers liketen die ze goed vonden. U kunt de campagne richten op de stad, regio of het land waar uw luisteraars zitten."),
            ("Welke van mijn video's worden geliket?", "Echte kijkers kiezen zelf, dus meestal uw nieuwste uploads en de video die hen als eerste naar uw kanaal bracht."),
            ("Wanneer verschijnen de eerste likes?", "In de eerste dagen van uw campagne, als de eerste kijkers binnenkomen, en daarna elke dag een paar, de rest van de maand."),
        ],
    },
    {
        "service": "likes",
        "modifier": "comment-likes",
        "slug": "youtube/likes/reactie-likes",
        "label": "Likes op YouTube-reacties",
        "title": "Likes op YouTube-reacties kopen? Zo gaat het echt | Growsterr",
        "description": "Overweegt u likes op YouTube-reacties te kopen? Eén reactie omhoog duwen doen we niet. Echte kijkers lezen de reacties onder uw video's en liken wat ze delen.",
        "h1": ("Likes op YouTube-reacties kopen? ", "Bouw een reactiesectie die likes verdient."),
        "intro": "Wie likes op YouTube-reacties koopt, wil meestal één reactie bovenaan krijgen. Dat verkopen we niet. We brengen echte kijkers naar uw kanaal, en wie de reacties onder uw video's leest, liket de antwoorden, vragen en grappen die hem aanspreken, uw vastgezette reactie ook.",
        "hero": {"image": "youtube-viewers", "alt": "Een kijker scrolt door de reacties onder een YouTubevideo en liket een antwoord"},
        "sections": [
            {
                "h2": "Eén reactie bovenaan is niet het doel",
                "p": [
                    "Een reactie met honderden likes onder een video die nauwelijks bewoog, valt op voor iedereen die de reacties leest. Likes op reacties zijn engagement zoals elk ander, dus likes van scripts vallen ook onder de spamregels van YouTube.",
                    "En staat de reactie onder de video van een andere creator, dan is die omhoog krijgen helemaal niet iets wat wij doen. Wij laten uw eigen kanaal groeien, met mensen die ervoor kiezen.",
                ],
            },
            {
                "h2": "Zo komt een reactiesectie tot leven",
                "p": [
                    "Echte kijkers lezen de reacties nadat ze hebben gekeken. Ze antwoorden, liken de reacties waar ze het mee eens zijn en laten zelf iets achter: doorgaans {pick_comments} nieuwe reacties per maand met {pick_name}, geschreven door mensen in plaats van scripts.",
                ],
                "ul": [
                    "Zet een reactie vast die kijkers een echte vraag stelt. De antwoorden worden eigen gesprekken.",
                    "Beantwoord de eerste reacties op een nieuwe upload. Een creator in het gesprek trekt meer mensen erin.",
                    "Geef een hartje aan reacties die u leuk vindt. Kijkers merken het en komen terug om te praten.",
                ],
                "image": {"image": "youtube-channel", "alt": "Een creator zet een vraag vast in de reacties onder een nieuwe YouTube-upload"},
            },
            {
                "h2": "Wat het pakket telt, en wat niet",
                "p": [
                    "Abonnees, videolikes en reacties komen met typische maandbereiken. Likes op reacties niet: die ontstaan als de ene kijker het met de andere eens is, en dat kan niemand inplannen.",
                ],
            },
        ],
        "faqs": [
            ("Kunnen jullie likes toevoegen aan mijn reactie onder de video van een ander kanaal?", "Nee. Wij laten uw eigen kanaal groeien met echte mensen die ervoor kiezen. Een reactie onder de video van een ander omhoog tillen, hoort niet bij wat we doen."),
            ("Zitten reactie-likes in het pakket?", "Ze komen zoals op elk levendig kanaal: van echte kijkers die de reacties onder uw video's lezen. We tellen ze niet vooraf, want elke like is een mens die het met iemand eens is."),
            ("Wordt het onder mijn video's echt drukker?", "Naarmate er mensen binnenkomen, ja: doorgaans {starter_comments} nieuwe reacties per maand met {starter_name}, {rising_comments} met {rising_name} en {pro_comments} met {pro_name}, van dezelfde mensen die zich abonneren."),
            ("Worden de reacties door bots of AI geschreven?", "Nee. Elke reactie komt van een mens die uw video bekeek en iets te zeggen had. We scripten nooit reacties en schrijven ze voor niemand."),
            ("Kunnen jullie likes naar één reactie onder mijn eigen video sturen?", "Nee. We promoten uw kanaal, en kijkers bepalen welke reacties een like verdienen, de uwe ook. Een vastgezette reactie die iets echts vraagt, verzamelt er het vaakst."),
            ("Is het riskant om likes voor YouTube-reacties te kopen?", "Bij een botdienst wel: reactie-likes zijn engagement, en YouTube behandelt kunstmatig engagement als spam. Likes van mensen die de reacties echt lazen, horen gewoon bij een levend kanaal."),
        ],
    },
    {
        "service": "likes",
        "modifier": "live",
        "slug": "youtube/likes/live",
        "label": "Likes voor YouTube-livestreams",
        "title": "YouTube Live-likes kopen? Echte chat, echte likes | Growsterr",
        "description": "Voordat u YouTube-livelikes koopt: in een stream komen ze van de mensen in de chat. Wij laten de echte abonnees groeien die kunnen aanhaken. Vanaf {from_price}.",
        "h1": ("Likes voor YouTube Live kopen? ", "Ze komen van de mensen in uw chat."),
        "intro": "Voordat u likes voor YouTube Live koopt: denk na over wie op de knop drukt. Dat zijn de mensen die echt naar uw stream kijken. We kunnen geen likes in een uitzending laten vallen op een vaste minuut, en we gaan ook niet doen alsof. Wij laten de echte abonnees groeien die kunnen zien dat u live bent en ervoor kiezen erbij te komen.",
        "hero": {"image": "youtube-channel", "alt": "Een creator streamt live op YouTube vanaf een bureau met camera en microfoon"},
        "sections": [
            {
                "h2": "Een livelike is een reactie, geen getal",
                "p": [
                    "Tijdens een stream komen likes als er iets gebeurt in beeld: een beslissende actie, een goed antwoord, het nummer waar de chat om vroeg. Het is het publiek dat op het moment zelf reageert.",
                    "Likes van accounts die niet kijken, reageren nergens op. Ze landen in één blok naast een stille chat, en elke echte kijker die binnenkomt, ziet dat de twee niet bij elkaar passen.",
                ],
            },
            {
                "h2": "De beste momenten van een stream omzetten in likes",
                "ul": [
                    "Vraag één keer om likes, op een hoogtepunt, niet in de eerste minuut.",
                    "Noem namen uit de chat hardop: mensen liken streams waar ze zich deel van voelen.",
                    "Zet een reactie vast die laatkomers vertelt wat er gebeurt, zodat ze lang genoeg blijven om te reageren.",
                    "Laat de herhaling online staan, zodat wie de stream miste hem nog kan bekijken en liken.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Mensen chatten en reageren in een YouTube-livechat terwijl de creator praat"},
            },
            {
                "h2": "Laat het publiek groeien vóór de volgende stream",
                "p": [
                    "De abonnees die we brengen, zijn echte mensen die uw kanaal vonden en besloten te blijven. Sommigen zitten in uw volgende chat, wanneer het hun uitkomt. Hoe groter die groep, hoe meer mensen er zijn om te reageren als er op de stream iets moois gebeurt.",
                ],
            },
        ],
        "faqs": [
            ("Kunnen jullie likes sturen tijdens mijn livestream?", "Nee. Echte mensen hebben hun eigen agenda, dus niemand die eerlijk is, kan reacties op een bepaald tijdstip beloven. Wat wij laten groeien, is het publiek dat misschien kijkt als u live gaat."),
            ("Gaan mijn nieuwe abonnees mijn streams bekijken?", "Een deel van hen, op de dagen dat het hun uitkomt. Ze kozen uw kanaal nadat ze het zagen, dus uw streams kunnen hen bereiken; of ze erbij komen, beslissen ze zelf."),
            ("Kunnen mensen een stream liken als hij voorbij is?", "Ja. De herhaling blijft als video op uw kanaal staan, en iedereen die hem later bekijkt, kan hem liken."),
            ("Waarom geen livelikes kopen bij een botdienst?", "Omdat nep-engagement nergens zo makkelijk te zien is als in een stream. Honderden likes naast een stille chat vertellen iedereen die binnenkomt dat de ruimte niet is wat ze lijkt."),
            ("Hoe groot kan mijn streampubliek worden?", "Dat hangt af van uw streams, maar de groep groeit elke dag: {pick_name} voegt over een maand doorgaans {pick_audience} abonnees toe, en elk van hen kan de volgende keer in de chat zitten."),
        ],
    },
    {
        "service": "likes",
        "modifier": "shorts",
        "slug": "youtube/likes/shorts",
        "label": "Likes op YouTube Shorts",
        "title": "Likes op YouTube Shorts kopen? De echte soort | Growsterr",
        "description": "Likes op YouTube Shorts van echte mensen die stopten met swipen, nooit van bots. Ze zitten in een maandpakket met abonnees en reacties, vanaf {from_price}.",
        "h1": ("Likes op YouTube Shorts kopen? ", "Verdien ze bij mensen die stopten met swipen."),
        "intro": "In de Shorts-feed betekent een like dat iemand lang genoeg stopte met swipen om er iets van te vinden. Wilt u likes op YouTube Shorts kopen, dan is dat de enige soort die het hebben waard is: likes van echte mensen die we elke dag naar uw kanaal brengen, die kijken, liken en zich soms abonneren.",
        "hero": {"image": "youtube-viewers", "alt": "Mensen bekijken YouTube Shorts op hun telefoon en tikken op like"},
        "sections": [
            {
                "h2": "Wat een Shorts-like waard is",
                "p": [
                    "Shorts spelen in een feed waar mensen snel doorheen gaan. Een like daar komt van een kijker die uw Short liet doorlopen, vaak meer dan eens, en vond dat hij een tik verdiende.",
                    "Gegenereerde likes slaan dat allemaal over. Ze stapelen zich op een Short waar niemand naar bleef kijken, en dat is het tegenovergestelde van wat een like hoort te zeggen.",
                ],
            },
            {
                "h2": "Wat een Short het liken waard maakt",
                "ul": [
                    "Begin met de clou. De eerste seconde bepaalt of mensen blijven.",
                    "Laat het einde terugleiden naar het begin, zodat opnieuw kijken vanzelf gaat.",
                    "Ondertitel uw Shorts: veel mensen scrollen zonder geluid.",
                    "Sluit af met één duidelijke reden om uw kanaal te bezoeken.",
                ],
                "image": {"image": "youtube-channel", "alt": "Een creator filmt een verticale YouTube Short met een telefoon op armlengte"},
            },
            {
                "h2": "Wat het pakket voor uw Shorts doet",
                "ul": [
                    "We promoten uw kanaal; kijkers die het ontdekken, kiezen zelf de Shorts en video's die ze willen zien.",
                    "{pick_name} voegt over een maand doorgaans {pick_likes} likes toe, verspreid over wat mensen leuk vonden.",
                    "Noem ons de stad, regio of het land, zodat uw Shorts mensen bereiken op de plek waarvoor u ze maakt.",
                ],
            },
        ],
        "faqs": [
            ("Kan ik likes krijgen op één Short?", "Niet als losse bestelling. Likes komen in een maandpakket, verspreid over de Shorts en video's die mensen leuk vinden, samen met abonnees en reacties."),
            ("Helpen Shorts-likes mijn lange video's?", "Via een omweg. Sommige mensen die een Short leuk vinden, openen het kanaal erachter, en een paar van hen gaan uw langere video's kijken en abonneren zich."),
            ("Hoe snel komen likes op mijn Shorts?", "Vanaf de eerste dagen van uw campagne, en daarna elke dag een paar, de hele maand door. Duizenden Shorts-likes binnen een uur komen van bots, niet van kijkers."),
            ("Wie liket mijn Shorts?", "Mensen die uw kanaal via onze campagne tegenkwamen, op de locatie die u koos. Ze besloten te kijken en besloten te liken; niemand vroeg het hun."),
            ("Gaan mensen ook op mijn Shorts reageren?", "Sommigen wel. Over uw hele kanaal brengt {pick_name} doorgaans {pick_comments} reacties per maand, elk getypt door degene die hem achterliet."),
        ],
    },
    # --- Abonnees ------------------------------------------------------------------------
    {
        "service": "subscribers",
        "modifier": "gradual",
        "slug": "youtube/abonnees/geleidelijk",
        "label": "Geleidelijke YouTube-abonnees",
        "title": "YouTube-abonnees kopen, rustig en gestaag | Growsterr",
        "description": "Rustig en gestaag YouTube-abonnees: echte mensen die zich met een paar tegelijk abonneren, elke dag van de maand, in hun eigen tempo. Vanaf {from_price} per maand.",
        "h1": ("YouTube-abonnees rustig en gestaag kopen? ", "Een ander tempo kennen echte mensen niet."),
        "intro": "Wilt u YouTube-abonnees rustig en gestaag kopen, dan vraagt u om het juiste. Hier is langzaam gewoon wat mensen doen: ze ontdekken uw kanaal op hun eigen moment, kijken een video of twee en beslissen. Met {pick_name} komt dat over de maand doorgaans uit op {pick_audience}.",
        "hero": {"image": "youtube-subscribers", "alt": "Het abonneeaantal van een YouTube-kanaal dat een maand lang elke dag een beetje stijgt"},
        "sections": [
            {
                "h2": "Langzame bots blijven bots",
                "p": [
                    "Sommige diensten verkopen een drip-feedoptie: dezelfde botabonnees, steeds met een paar tegelijk vrijgegeven zodat de lijn er rustig uitziet. Het tempo verandert; wat erachter zit niet. Accounts die nooit kijken, verkleinen nog steeds het deel van uw abonnees dat betrokken is.",
                    "Geleidelijk betekent pas iets als het komt van mensen die een voor een beslissen. Geen instelling kan dat nabootsen, en er is er ook geen nodig.",
                ],
            },
            {
                "h2": "Zo ziet gestaag eruit op uw dashboard",
                "p": [
                    "Open uw dashboard op welke dag ook en u ziet twee lijnen: mensen die uw kanaal via de campagne bezochten, en hoeveel van hen zich abonneerden. Sommige dagen zijn drukker dan andere, zoals bij elk kanaal dat mensen aan het ontdekken zijn. Wat u niet ziet, is een sprong van duizenden in één nacht.",
                ],
            },
            {
                "h2": "Waarom gestaag het wint van plotseling op YouTube",
                "p": [
                    "Een kanaal dat elke week abonnees wint, samen met views en reacties, is een kanaal dat mensen vinden. Elke nieuwe upload bereikt een iets grotere groep echte mensen, en dat telt over maanden flink op.",
                ],
                "image": {"image": "youtube-channel", "alt": "Een YouTube-creator bekijkt een maand gestage kanaalgroei op een laptop"},
            },
        ],
        "faqs": [
            ("Hoe langzaam is langzaam?", "Dun verspreid: een handvol nieuwe abonnees op de meeste dagen, nooit een partij. Over 30 dagen telt dat op tot het typische bereik van het pakket, en elke dag is net iets anders."),
            ("Kan ik kiezen hoe snel abonnees komen?", "Niet per uur, want dat bepalen echte mensen. U kiest het pakket: een groter pakket toont uw kanaal elke dag aan meer mensen."),
            ("Is een langzame druppel veiliger voor mijn kanaal?", "Alleen als de abonnees echt zijn. Een langzame druppel bots blijft nep-engagement, terwijl echte mensen die zich in hun eigen tempo abonneren gewone groei zijn."),
            ("Zien dagelijkse abonnees er verdacht uit?", "Nee. Kanalen die mensen vinden, winnen elke dag abonnees; dat is de normale vorm van groei. Wat opvalt, zijn duizenden binnen een uur."),
            ("Wat gebeurt er als de maand voorbij is?", "Het pakket verlengt en de campagne loopt in hetzelfde gestage tempo door, tenzij u opzegt. Opzeggen stopt de volgende betaling; uw huidige maand loopt gewoon af."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "monthly",
        "slug": "youtube/abonnees/maandelijks",
        "label": "Maandelijkse YouTube-abonnees",
        "title": "YouTube-abonnees per maand, altijd opzegbaar | Growsterr",
        "description": "YouTube-abonnees per maand kopen: een pakket dat de hele maand echte mensen naar uw kanaal brengt, betaald met uw kaart en altijd opzegbaar. Vanaf {from_price}.",
        "h1": ("YouTube-abonnees per maand, ", "zoals kanalen echt groeien."),
        "intro": "Een maandpakket is precies hoe wij werken. Koopt u bij ons YouTube-abonnees per maand, dan wordt uw kanaal elke dag aan echte mensen getoond, wie het leuk vindt abonneert zich, en het pakket verlengt elke maand tot u besluit te stoppen.",
        "hero": {"image": "youtube-subscribers", "alt": "Een YouTube-kanaal krijgt maand na maand nieuwe abonnees"},
        "sections": [
            {
                "h2": "Waarom een abonnement in plaats van een eenmalig pakket",
                "p": [
                    "Een kanaal is niet klaar na één uitschieter. U blijft uploaden, dus u blijft nieuwe mensen nodig hebben die u vinden. Een maandpakket past bij dat ritme: elke nieuwe video komt bij een publiek dat nog groeit.",
                    "Eenmalige pakketten doen het omgekeerde. Ze leveren op dag één een getal en daarna niets, en omdat geen echt publiek op commando verschijnt, zijn dat bijna altijd bots.",
                ],
            },
            {
                "h2": "Maand voor maand betalen",
                "ul": [
                    "U betaalt met uw kaart via de beveiligde checkout van Stripe, of met Apple Pay en Google Pay op apparaten die het ondersteunen.",
                    "Het pakket verlengt elke maand vanaf de dag waarop u begint.",
                    "Stoppen is één klik in uw account, en daarna wordt er niets meer afgeschreven.",
                    "U kunt een pakket opschalen als uw uploads klaar zijn voor meer mensen.",
                ],
            },
            {
                "h2": "Wat er maand na maand opbouwt",
                "p": [
                    "Elke maand voegt echte abonnees toe die blijven zolang ze van uw kanaal genieten. Over een paar maanden wordt dat een basis van mensen die uw uploads zien, zodat elke nieuwe video met meer van hen begint.",
                ],
                "image": {"image": "youtube-channel", "alt": "Een creator plant de YouTube-uploads van volgende maand op een wandkalender"},
            },
        ],
        "faqs": [
            ("Is het een abonnement?", "Ja. Elk pakket is een maandabonnement, betaald met een kaart, Apple Pay of Google Pay via Stripe. Eenmalige pakketten zijn er niet."),
            ("Wat voegt elke maand doorgaans toe?", "{starter_name} brengt doorgaans {starter_audience}, {rising_name} {rising_audience} en {pro_name} {pro_audience}. Elke maand verschilt een beetje, want elke abonnee is een mens die een keuze maakt."),
            ("Kan ik na de eerste maand opzeggen?", "Ja. Zeg op elk moment op vanuit uw account; de maand die u al hebt betaald, loopt door tot de laatste dag, en daarna wordt er niets verlengd."),
            ("Houd ik mijn abonnees als ik opzeg?", "Niemand vertrekt omdat u stopt met betalen: het zijn mensen, en ze blijven geabonneerd zolang uw kanaal hen interesseert. Opzeggen beëindigt nieuwe campagnes; het haalt niemand weg."),
            ("Waarmee kan ik betalen?", "Met een kaart, of met Apple Pay of Google Pay als uw telefoon dat biedt. Wat u ook kiest, wordt elke maand opnieuw belast tot u opzegt."),
            ("Kan ik klein beginnen en doorgroeien naar een groter pakket?", "Ja. Begin waar uw kanaal nu staat, vaak met {starter_name}, en schaal op zodra u genoeg uploadt om meer mensen te verwelkomen."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "no-drop",
        "slug": "youtube/abonnees/zonder-uitval",
        "label": "YouTube-abonnees zonder uitval",
        "title": "YouTube-abonnees kopen zonder uitval, zonder bots | Growsterr",
        "description": "Abonneeaantallen dalen als de abonnees nooit echt waren. De onze zijn mensen die uw kanaal kozen, geen accounts die wachten op een opschoning. Vanaf {from_price}.",
        "h1": ("YouTube-abonnees kopen zonder uitval? ", "Begin met mensen die uw kanaal kozen."),
        "intro": "Wie YouTube-abonnees zonder uitval wil kopen, heeft meestal al eens een aantal zien zakken. Abonnees vallen af als het nooit mensen waren: YouTube ruimt spam en opgeheven accounts op, en botabonnees gaan mee. De onze zijn echte kijkers die ervoor kozen zich te abonneren, het soort account dat een opschoning juist met rust laat.",
        "hero": {"image": "youtube-subscribers", "alt": "Een YouTube-abonneeaantal blijft stabiel terwijl er nieuwe echte abonnees bijkomen"},
        "sections": [
            {
                "h2": "Waarom abonneeaantallen dalen",
                "p": [
                    "YouTube verwijdert abonnees die het als spam beoordeelt, samen met accounts die zijn opgeheven. Kanalen die botabonnees kochten, zien die aantallen in stappen dalen, soms maanden na de aankoop.",
                    "De daling is het zichtbare deel. Het onzichtbare deel is de tijd die die accounts op uw kanaal doorbrachten zonder ooit te kijken, terwijl ze het deel van uw betrokken abonnees omlaag trokken.",
                ],
            },
            {
                "h2": "Waarom aanvullen niet het antwoord is",
                "p": [
                    "Sommige verkopers beloven aan te vullen wat afvalt. Dat betekent verwijderde bots vervangen door nieuwe bots, waardoor het getal hoog blijft en het probleem ook. Een echte abonnee hoeft niet te worden vervangen.",
                ],
            },
            {
                "h2": "Zo ziet eerlijk zonder uitval eruit",
                "p": [
                    "Echte mensen kunnen zich afmelden, zoals op elk kanaal, en na verloop van tijd doen een paar dat. Dat is normaal verloop, en het is klein naast de golven die bots achterlaten. Wat blijft, is een publiek dat er nog is als u uploadt.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Trouwe abonnees bekijken op de bank de nieuwste YouTube-upload van een creator"},
            },
        ],
        "faqs": [
            ("Gaan sommige van mijn nieuwe abonnees ooit weg?", "Sommigen misschien, zoals mensen dat op elk kanaal doen als hun smaak verandert. Wat u niet hebt, is een partij nepaccounts die wacht om samen te worden verwijderd."),
            ("Wordt er aangevuld als abonnees afvallen?", "Nee, want er is geen nepaantal om op te hogen. U krijgt een maandpakket met echte mensen; wat ze daarna doen, kiezen ze zelf, zoals bij elk publiek."),
            ("Waarom daalde mijn aantal na een andere dienst?", "Waarschijnlijk verwijderde YouTube accounts die het als spam beoordeelde, of accounts die waren opgeheven. Botabonnees verdwijnen bij zulke opschoningen meestal in grote partijen."),
            ("Kunnen botabonnees mijn kanaal schaden, ook als ze weg zijn?", "Het verwijderen is het kleinere probleem. Zolang ze er waren, keken ze geen enkele upload, waardoor uw publiek minder betrokken leek dan het werkelijk was."),
            ("Komt mijn dashboard overeen met mijn aantal op YouTube?", "Niet precies. Uw dashboard telt de nieuwe abonnees die onze campagne bracht; het totaal op YouTube bevat ook groei van elders en iedereen die zich heeft afgemeld."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "organic",
        "slug": "youtube/abonnees/organisch",
        "label": "Organische YouTube-abonnees",
        "title": "Organische YouTube-abonnees kopen: zo werkt het | Growsterr",
        "description": "Kunt u organische YouTube-abonnees kopen? Wij betalen voor de kennismaking via gepromote campagnes; de keuze om te abonneren is van de kijker. Vanaf {from_price}.",
        "h1": ("Organische YouTube-abonnees kopen? ", "Wij betalen de kennismaking. Zij kiezen."),
        "intro": "Dit is het eerlijke antwoord voor iedereen die organische YouTube-abonnees wil kopen: niemand kan u een beslissing verkopen. Waar wij voor betalen, is de kennismaking. Uw kanaal wordt via gepromote campagnes in ons partnernetwerk aan echte mensen getoond, en wie zich abonneert, doet dat omdat hij het wil.",
        "hero": {"image": "youtube-subscribers", "alt": "Nieuwe abonnees sluiten zich aan bij een YouTube-kanaal nadat ze de video's ontdekten"},
        "sections": [
            {
                "h2": "De grens tussen betaald en organisch",
                "p": [
                    "Elk kanaal dat adverteert, betaalt voor aandacht. Wat daarna gebeurt, is organisch of niet: iemand kijkt, vindt de video goed of niet, en abonneert zich of gaat verder.",
                    "Wij houden die grens zuiver. We betalen om uw kanaal elke dag onder de aandacht van mensen te brengen; we betalen nooit iemand om zich te abonneren, ruilen nooit abonnementen en gebruiken nooit accounts die op commando handelen.",
                ],
            },
            {
                "h2": "Zo onderscheidt u organische abonnees van de rest",
                "ul": [
                    "Hun namen duiken op in de reacties onder uw volgende upload.",
                    "Hun reacties lezen als mensen: vragen, grappen, af en toe een andere mening.",
                    "Nieuwe abonnees komen samen met kanaalbezoeken, nooit zonder.",
                    "Ze blijven na afloop van de campagne, want niets hield hen daar vast.",
                ],
            },
            {
                "h2": "Organisch hoeft geen wachten te betekenen",
                "p": [
                    "Organische groei wordt vaak voorgesteld als jarenlang wachten op die ene geluksvideo. Een gepromote campagne verkort het wachten: echte mensen zien uw kanaal vanaf de eerste dagen. Het enige wat ze niet kan verkorten, is hun beslissing, en dat is precies het deel dat het bewaren waard is.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Iemand tikt met een kop koffie in de hand op abonneren bij een kanaal dat hij die ochtend vond"},
            },
        ],
        "faqs": [
            ("Als jullie mijn kanaal promoten, is de groei dan nog organisch?", "De abonnementen wel. Wij betalen ervoor dat uw kanaal wordt getoond; niemand wordt betaald of beloond om zich te abonneren. Elke abonnee besloot zelf, nadat hij uw video's zag."),
            ("Gebruiken jullie sub-for-sub of ruilnetwerken?", "Nooit. Mensen die zich abonneren om er een abonnement voor terug te krijgen, interesseren zich niet voor uw video's en kijken ze zelden, en YouTube rekent zulke ruilen tot nep-engagement."),
            ("Waar komt organische groei op uit in een maand?", "{pick_name} komt meestal ergens uit binnen {pick_audience} per maand. Omdat elke abonnee een mens is die kiest, is dat een bereik en geen aantal."),
            ("Gaan organische abonnees mijn video's bekijken?", "Ze kozen uw kanaal nadat ze het zagen, en dat is de beste start die een abonnee kan hebben. Of ze elke upload bekijken, hangt af van die upload, zoals bij iedereen."),
            ("Moet ik tijdens de campagne iets doen?", "Houd uw kanaal openbaar en blijf uploaden. Hoe beter uw video's passen bij wat uw kanaalpagina belooft, hoe meer bezoekers besluiten zich te abonneren."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "real",
        "slug": "youtube/abonnees/echt",
        "label": "Echte YouTube-abonnees",
        "title": "YouTube-abonnees kopen: echte mensen, te controleren | Growsterr",
        "description": "Echt, oprecht, hoge kwaliteit: vier tekens die u bij elke YouTube-abonnee kunt controleren, en hoe onze maandpakketten mensen brengen die ze doorstaan.",
        "h1": ("Echte YouTube-abonnees kopen. ", "Zo ziet u het verschil."),
        "intro": "Wie YouTube-abonnees koopt, voegt er het woord echt aan toe nadat hij zich één keer heeft gebrand. Wij vinden dat het iets moet betekenen wat u kunt controleren: een mens die uw kanaal tegenkwam, besloot dat het een abonnement waard was, en daarna opduikt in uw views, likes en reacties.",
        "hero": {"image": "youtube-subscribers", "alt": "Een YouTube-kanaalpagina waar een maand lang echte, oprechte abonnees binnenkomen"},
        "sections": [
            {
                "h2": "Vier tekens dat een abonnee echt is",
                "p": [
                    "Hoge kwaliteit, oprecht, echt: elke verkoper gebruikt deze woorden. Dit zijn de controles die ze uit elkaar halen.",
                ],
                "ul": [
                    "Er was eerst een bezoek: iemand opende uw kanaal voordat hij zich abonneerde.",
                    "Ze kijken: de views op uw volgende upload stijgen mee met het abonneeaantal.",
                    "Ze praten, in reacties die geen script zou schrijven.",
                    "Ze wonen waar u de campagne op richtte, op de plek die u bij uw bestelling noemde.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Een nieuwe abonnee reageert in eigen woorden onder een YouTubevideo"},
            },
            {
                "h2": "Leg ons naast YouTube Studio",
                "p": [
                    "Onze kant van het verhaal is uw Growsterr-dashboard: campagnebezoeken aan uw kanaal en wie daarvan zich abonneerde. YouTube Studio vertelt dezelfde maand vanuit YouTube. Lees ze samen over een maand: terwijl er abonnees bijkomen, zouden uw video's ook views en reacties van nieuwe mensen moeten krijgen.",
                ],
            },
            {
                "h2": "Wat echte abonnees niet kunnen",
                "p": [
                    "Echte mensen zijn niet per uur te bestellen, krijgen niet te horen wat ze moeten reageren en kunnen niet beloven elke upload te bekijken. Wie dat wel aanbiedt, beschrijft iets anders dan mensen. Wij vertellen u liever de grenzen dan dat we u een getal verkopen.",
                ],
            },
        ],
        "faqs": [
            ("Wat betekent hoge kwaliteit bij YouTube-abonnees?", "Voor ons: een mens met een eigen account die uw kanaal koos en kan kijken, liken en reageren. Profielfoto's en accountleeftijd zijn makkelijk na te maken; een echte beslissing om te abonneren niet."),
            ("Zijn jullie abonnees echte mensen of accounts die jullie beheren?", "Echte mensen. We bezitten, beheren of huren geen accounts. We tonen uw kanaal via gepromote campagnes, en de mensen die het zien, beslissen."),
            ("Kan ik online echte YouTube-abonnees kopen zonder mijn login te delen?", "Ja, en u moet die ook nooit met iemand delen. We hebben uw kanaalhandle en een openbaar kanaal nodig, meer niet."),
            ("Zorgen echte abonnees ervoor dat mijn kanaal wordt gemonetiseerd?", "Dat beslist YouTube, dus we beloven nooit monetisatie of kijkuren. Echte abonnees kunnen uw video's bekijken, wat bots nooit doen, maar de eigen eisen en beoordeling van YouTube bepalen wie wordt gemonetiseerd."),
            ("Hoe ziet een maand echte groei eruit?", "Met {pick_name} doorgaans {pick_audience} nieuwe abonnees, die elke dag in kleine aantallen binnenkomen. Een kleiner kanaal kan beginnen met {starter_name} voor {starter_price} per maand."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "safe",
        "slug": "youtube/abonnees/veilig",
        "label": "Veilige YouTube-abonnees",
        "title": "YouTube-abonnees kopen, betrouwbaar en veilig | Growsterr",
        "description": "Is YouTube-abonnees kopen betrouwbaar en veilig? Kijk wie de dienst runt, waar die om vraagt en hoe abonnees binnenkomen. Zo beantwoorden wij elk punt.",
        "h1": ("Betrouwbaar YouTube-abonnees kopen? ", "Kijk eerst wie erachter zit."),
        "intro": "Vraagt u zich af of u betrouwbaar en veilig YouTube-abonnees kunt kopen? Om betrouwbaar te zijn, moet een dienst drie controles doorstaan: een bedrijf dat u kunt benoemen, niets wat aan uw login komt, en abonnees die echte mensen zijn. Growsterr is een product van Sterr Agency, en zo beantwoorden we elk van die drie.",
        "hero": {"image": "youtube-subscribers", "alt": "Het YouTube-kanaal van een creator groeit veilig met abonnees van echte mensen"},
        "sections": [
            {
                "h2": "Aan wie u betaalt",
                "p": [
                    "Achter Growsterr staat Sterr Agency, ingeschreven als Sterr Technologies OÜ in Tallinn, Estland, met hoofdkantoor in Turkije. U betaalt via de beveiligde checkout van Stripe, en het abonnement staat in uw eigen account, waar u het kunt opzeggen.",
                ],
            },
            {
                "h2": "Zo blijft uw kanaal beschermd",
                "ul": [
                    "Uw Google-wachtwoord blijft van u: we vragen er nooit om, en niemand van ons logt in op uw kanaal.",
                    "Niemand wordt betaald om zich te abonneren, en er worden geen abonnementen geruild.",
                    "Abonnees komen verspreid over de maand binnen, nooit in een partij.",
                    "Likes en reacties komen van de abonnees zelf, dus elk cijfer beweegt in de pas.",
                ],
                "image": {"image": "youtube-channel", "alt": "Een creator aan een bureau controleert de kanaalinstellingen, alleen ingelogd op het eigen apparaat"},
            },
            {
                "h2": "Waarschuwingssignalen bij elke groeidienst",
                "ul": [
                    "De dienst vraagt om uw login, of om toegang tot uw Google-account.",
                    "Hij belooft een exact aantal abonnees op een vast tijdstip.",
                    "Hij verkoopt abonnees, views en likes als losse pakketten per duizend.",
                    "Hij kan niet zeggen waar abonnees vandaan komen, of laten zien wat hij heeft gemeten.",
                ],
            },
        ],
        "faqs": [
            ("Is het legitiem om YouTube-abonnees te kopen?", "Betalen voor promotie is gewoon; elk kanaal dat adverteert, doet het. Betalen voor nep-engagement niet: bots, scripts en abonnementsruil zijn wat YouTube als spam behandelt. Wij promoten uw kanaal alleen bij echte mensen die zelf beslissen."),
            ("Kan YouTube mijn kanaal hiervoor blokkeren?", "YouTube treedt op tegen nep-engagement, en daarom gebruiken we het nooit. We kunnen niet namens YouTube beslissen, maar mensen die uw kanaal kiezen nadat ze het zagen, is hoe promotie overal werkt."),
            ("Wat moet ik aanleveren om te starten?", "Uw kanaalhandle, de plek waar uw publiek vandaan moet komen, en een betaalkaart voor het maandpakket. Uw kanaal moet openbaar zijn, zodat mensen zich kunnen abonneren."),
            ("Is mijn betaling veilig?", "Stripe verwerkt elke betaling, of u nu een kaart, Apple Pay of Google Pay gebruikt. Uw kaartgegevens blijven bij Stripe, niet bij ons."),
            ("Wat als het niets voor mij is?", "Zeg op vanuit uw account wanneer u wilt. Daarna wordt er geen nieuwe betaling afgeschreven, en uw huidige maand loopt door tot het einde."),
        ],
    },
    # --- Views ---------------------------------------------------------------------------
    {
        "service": "views",
        "slug": "youtube/views",
        "label": "YouTube-views",
        "title": "YouTube-views kopen? Echte mensen, elke dag | Growsterr",
        "description": "YouTube-views kopen? De onze komen van echte mensen die zelf kiezen te kijken, in een maandpakket met abonnees, likes en reacties. Vanaf {from_price}.",
        "h1": ("YouTube-views kopen? ", "Achter elke view zit een mens."),
        "intro": "Bent u hier om YouTube-views te kopen? Zo werken de onze. U vindt hier geen menu met viewaantallen. Elk pakket stelt uw kanaal dagelijks voor aan echte mensen; die drukken op play bij wat hen interesseert, en velen gaan daarna liken, reageren en abonneren. De views komen met het pakket mee, en achter elke view zit een mens.",
        "hero": {"image": "youtube-viewers", "alt": "Echte mensen drukken op play bij de YouTubevideo van een creator"},
        "sections": [
            {
                "h2": "Waarom er geen viewaantal op onze pakketten staat",
                "p": [
                    "Een view is een mens die besluit te kijken, en niemand kan beloven hoeveel mensen dat besluiten. Wie een exact aantal views op een vast uur verkoopt, verkoopt weergaven die door scripts of bots zijn gegenereerd.",
                    "YouTube behandelt kunstmatig opgeblazen views als spam: het kan ze verwijderen, en ze tellen nooit mee voor monetisatie. Dus verkopen we waar we achter kunnen staan: een maandcampagne die echte mensen brengt, met typische bereiken voor de abonnees, likes en reacties die ze achterlaten.",
                ],
            },
            {
                "h2": "Muziekvideo's, playlists en lange uploads",
                "p": [
                    "We promoten uw kanaal, niet één nummer. Luisteraars die het ontdekken, kiezen de nummers die hen pakken, en wie van een nummer geniet, kan doorgaan met uw playlists; elke weergave daar is van hen.",
                ],
                "image": {"image": "youtube-channel", "alt": "Een muzikant uploadt een nieuwe muziekvideo naar het eigen YouTube-kanaal"},
            },
            {
                "h2": "Voordat u een site kiest om YouTube-views te kopen",
                "ul": [
                    "Vraag wat een view voor hen betekent: een mens die koos te kijken, of een weergave die zij genereerden.",
                    "Controleer of views alleen komen of samen met abonnees, likes en reacties van dezelfde mensen.",
                    "Zoek naar een bedrijfsnaam, een echte checkout en een manier om op te zeggen.",
                    "Loop weg bij iedereen die om uw Google-wachtwoord vraagt.",
                ],
            },
        ],
        "faqs": [
            ("Kan ik views bestellen zonder pakket?", "Nee. Elke view die we brengen, hoort bij iemand die zich misschien ook abonneert, liket of reageert, en daarom komen ze alleen als onderdeel van een pakket. Een viewaantal dat stijgt terwijl verder niets beweegt, is het patroon van kunstmatig verkeer."),
            ("Vertellen jullie hoeveel views ik kan verwachten?", "We plakken geen getal op views, want elke view is de keuze van een mens. Wat we wel noemen, zijn typische maandbereiken: met {pick_name} {pick_audience} nieuwe abonnees en {pick_likes} likes, en die mensen kijken voordat ze een van beide doen."),
            ("Is er een app om YouTube-views te kopen?", "We gebruiken geen app. U kiest een pakket op onze site, betaalt via Stripe en volgt uw campagne in het dashboard van uw account, vanuit elke browser."),
            ("Wat zijn premium YouTube-views?", "Niets wat YouTube kent. YouTube Premium is een abonnement voor kijkers, geen soort view die iemand u kan verkopen. De enige views die het hebben waard zijn, horen bij mensen die zelf op play drukten."),
            ("Kunnen gekochte views een video viraal laten gaan?", "Dat kan niemand beloven. Echte kijkers geven een video meer mensen die hem kunnen delen, en dat is de eerlijke versie van een virale kans."),
            ("Helpen views om mijn kanaal te monetiseren?", "Monetisatie en kijkuren beloven we niet. Kunstmatige views tellen daar helemaal niet voor mee; echte kijkers kunnen uw video's bekijken, maar YouTube beslist wie wordt gemonetiseerd."),
        ],
    },
    {
        "service": "views",
        "modifier": "gradual",
        "slug": "youtube/views/geleidelijk",
        "label": "Geleidelijke YouTube-views",
        "title": "Langzaam YouTube-views kopen? Mensen kiezen het tempo",
        "description": "Langzame YouTube-views die in de loop van de maand groeien: echte kijkers vinden uw kanaal met een paar tegelijk, met abonnees en likes. Vanaf {from_price}.",
        "h1": ("Langzaam YouTube-views kopen? ", "Echte kijkers komen nooit anders."),
        "intro": "Langzaam YouTube-views willen kopen is een goed instinct: een video die over dagen views krijgt, is een video die mensen vinden. Hier hoeft niemand dat tempo aan te zetten. Echte mensen ontdekken uw kanaal elke dag van de maand en bekijken wat hen interesseert, dus uw views groeien zoals op elk groeiend kanaal.",
        "hero": {"image": "youtube-viewers", "alt": "Kijkers ontdekken een YouTube-kanaal een voor een, verspreid over een paar weken"},
        "sections": [
            {
                "h2": "Een ingeplande druppel is iets anders",
                "p": [
                    "Een druppelschema spreidt gegenereerde weergaven over een week in plaats van een uur. De teller stijgt rustiger, maar de weergaven komen nog steeds zonder echt kijken, zonder likes en zonder abonnees. YouTube kijkt naar wat kijkers doen, niet alleen naar hoe snel ze kwamen.",
                ],
            },
            {
                "h2": "Ook uw oudere video's worden bekeken",
                "p": [
                    "Kijkers die over weken binnenkomen, bekijken niet alleen uw nieuwste upload. Wie één video leuk vindt, opent misschien een andere vanaf uw kanaalpagina, dus oudere video's krijgen in hetzelfde rustige tempo views. Een druppel gericht op één link kan dat niet.",
                ],
                "image": {"image": "youtube-channel", "alt": "Een YouTube-kanaalpagina met een raster oudere video's die nieuwe views krijgen"},
            },
            {
                "h2": "Een tempo dat u kunt volgen",
                "p": [
                    "Het dashboard volgt mensen, geen weergaven: dagelijkse campagnebezoeken aan uw kanaal en de abonnees daaronder. Views staan er niet op, omdat we ze niet vooraf tellen; u vindt ze in YouTube Studio, bij de video's die mensen kozen.",
                ],
            },
        ],
        "faqs": [
            ("Is er een vast aantal views per dag waar ik op kan rekenen?", "Er is geen dagaantal te geven: elke view hangt af van iemand die besluit te kijken. Wat u kunt verwachten, zijn nieuwe kijkers op elke dag van de maand, geen piek op dag één."),
            ("Kan ik views over een vast aantal dagen spreiden?", "Elke campagne loopt 30 dagen en verlengt maandelijks. Binnen die periode bepalen echte mensen het tempo, dus we plannen views niet per dag in."),
            ("Zien langzame views er natuurlijker uit voor YouTube?", "Snelheid is maar een deel ervan. YouTube ziet ook of kijkers blijven kijken, de video liken en terugkomen. Echte mensen doen dat in elk tempo; ingeplande weergaven nooit."),
            ("En de video's die ik vorig jaar postte?", "Die doen mee. Mensen die één video leuk vinden, kijken meestal wat er nog meer op uw kanaal staat, en oudere uploads zijn vaak waar ze daarna terechtkomen."),
            ("Wat als ik sneller views wil?", "Kies een groter pakket, zodat elke dag meer mensen uw kanaal zien. Alles wat duizenden views binnen het uur belooft, genereert weergaven en vindt geen kijkers."),
        ],
    },
    {
        "service": "views",
        "modifier": "high-retention",
        "slug": "youtube/views/hoge-kijkduur",
        "label": "YouTube-views met hoge kijkduur",
        "title": "YouTube-views met hoge kijkduur? Een eerlijk antwoord | Growsterr",
        "description": "YouTube-views met hoge kijkduur zijn niet te koop: kijkduur verdient de video. Wij brengen echte kijkers die zelf op play drukten. Vanaf {from_price} per maand.",
        "h1": ("YouTube-views met hoge kijkduur kopen? ", "Breng mensen die willen kijken."),
        "intro": "Wilt u YouTube-views met hoge kijkduur kopen, dan weet u al dat een aantal weergaven niet het punt is: u wilt kijkers die blijven. Kijkduur kan alleen niemand verkopen. Het is hoe lang echte mensen ervoor kiezen te blijven kijken. Ons deel is kijkers brengen die zelf op play drukten; hoe lang ze blijven, is aan uw video.",
        "hero": {"image": "youtube-channel", "alt": "Een creator monteert een lange YouTubevideo om kijkers vast te houden"},
        "sections": [
            {
                "h2": "Kijkduur die te koop is, is een timer",
                "p": [
                    "Biedt een verkoper views met een vaste kijkduur, dan zit daar een speler achter die een vast aantal seconden draait. Hij kijkt hetzelfde wat er ook in beeld is, en hij liket, reageert of abonneert nooit. Hoe lang hij ook speelt, het is kunstmatig engagement, en YouTube behandelt het als spam.",
                ],
            },
            {
                "h2": "Waarom echte kijkers kijkduur betekenis geven",
                "p": [
                    "Kijkduur is belangrijk omdat het laat zien dat mensen die een video begonnen, wilden blijven kijken. Dat klopt alleen als ze de video zelf kozen. Echte kijkers geven u eerlijke kijkduurgegevens: waar ze blijven, waar ze afhaken en wat hen terugbrengt.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Een kijker leunt naar voren om een lange YouTubevideo tot het eind te bekijken"},
            },
            {
                "h2": "Wat de kijkduur verhoogt, van uw kant",
                "ul": [
                    "Lever in de eerste seconden wat titel en thumbnail beloven.",
                    "Schrap de trage intro: laat eerst de kern zien en leg het daarna uit.",
                    "Voeg hoofdstukken toe aan lange video's, zodat kijkers doorspringen naar waarvoor ze kwamen in plaats van weg te gaan.",
                    "Zoek in YouTube Studio op waar kijkers afhaken, en verbeter dat moment in uw volgende upload.",
                ],
            },
        ],
        "faqs": [
            ("Beloven jullie een kijkduurpercentage of kijkuren?", "Nee. Kijkduur en kijktijd hangen af van de video en van elke kijker. Wij brengen echte mensen die kozen te kijken, en plakken nooit een getal op hoe lang ze blijven."),
            ("Gaan mensen mijn hele video uitkijken?", "Sommigen wel en sommigen niet, en juist dat maakt hun gegevens bruikbaar. YouTube Studio laat zien waar mensen blijven en waar ze vertrekken."),
            ("Tellen views met hoge kijkduur mee voor monetisatie?", "Kunstmatige views tellen helemaal niet mee voor monetisatie, wat hun kijkduur ook is. De kijktijd van echte kijkers is echt, maar monetisatie beloven we nooit; dat beslist YouTube."),
            ("Kan de campagne kijkers naar één video sturen?", "We richten kijkers niet op losse video's: we promoten uw kanaal, en mensen kiezen wat ze bekijken. U kunt ze wel sturen, want de uitgelichte video op uw kanaalpagina is het eerste wat nieuwe bezoekers zien."),
            ("Welke video's hebben er het meeste aan?", "Video's die hun belofte waarmaken. Een duidelijke haak, een eerlijke thumbnail en een vast tempo maken van nieuwe kijkers lange kijkers, en hoe meer mensen de campagne naar uw kanaal brengt, hoe meer van hen die video's kunnen vasthouden."),
        ],
    },
    {
        "service": "views",
        "modifier": "live",
        "slug": "youtube/views/live",
        "label": "Views voor YouTube-livestreams",
        "title": "Views voor YouTube Live kopen? Bouw een echt publiek | Growsterr",
        "description": "Niemand kan een YouTube-livestream op een vast uur met echte mensen vullen. Wij laten de abonnees groeien die bij uw volgende stream kunnen zijn. Vanaf {from_price}.",
        "h1": ("Views voor YouTube Live kopen? ", "Bouw het publiek dat komt opdagen."),
        "intro": "Wilt u views voor YouTube Live kopen, dan wilt u een stream die niet leeg voelt als u op start drukt. Niemand kan echte mensen op een vaste minuut naar een uitzending brengen, en dat beweren wij ook niet. Wat we wel doen, is uw kanaal elke dag laten groeien met echte abonnees, zodat elke livestream meer mensen heeft die erbij kunnen komen.",
        "hero": {"image": "youtube-channel", "alt": "Een creator staat op het punt live te gaan op YouTube met een geplande stream in beeld"},
        "sections": [
            {
                "h2": "Waarom een gekocht liveaantal averechts werkt",
                "p": [
                    "Het kijkersaantal is het eerste wat iemand ziet bij een livestream. Staan er honderden en is de chat stil, dan merkt elke echte bezoeker het. Gekochte livekijkers typen niet, reageren niet en komen niet terug voor de herhaling.",
                    "De regels van YouTube over nepviews staan niet stil als u live gaat. Een liveaantal is geen veiligere plek om te vervalsen.",
                ],
            },
            {
                "h2": "Wie er naar een stream komt, en wanneer",
                "p": [
                    "De mensen die het vaakst komen, zijn abonnees die uw kanaal al kennen. Afhankelijk van hun instellingen kan YouTube hun uw stream in hun feed tonen of een melding sturen.",
                ],
                "ul": [
                    "Plan de stream vooraf in, zodat abonnees een herinnering kunnen instellen.",
                    "Kies een publiekslocatie waar uw streamtijd in de avond valt.",
                    "Ga op een vaste dag live, zodat kijkers leren wanneer ze terug moeten komen.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Kijkers sluiten 's avonds vanaf hun telefoon aan bij een geplande YouTube-livestream"},
            },
            {
                "h2": "De herhaling blijft views opleveren",
                "p": [
                    "Als de stream afloopt, blijft hij als video op uw kanaal staan. Nieuwe abonnees die hem live misten, vinden de herhaling daar en bekijken hem wanneer het hun uitkomt.",
                ],
            },
        ],
        "faqs": [
            ("Kunnen jullie mijn stream vullen terwijl ik live ben?", "Nee. Echte mensen kijken wanneer ze willen, dus we kunnen niemand op een bepaald tijdstip beloven. Wij laten de abonneebasis groeien waar uw streams uit putten."),
            ("Maakt de locatie die ik kies uit voor streams?", "Meer dan bij gewone uploads. Kies de plek waar uw publiek woont, dan valt uw streamtijd in hun dag en niet midden in hun nacht."),
            ("Krijgt de herhaling views uit de campagne?", "Dat kan. Een herhaling is een video op uw kanaal, dus kijkers die u na de stream vinden, kunnen hem bekijken zoals elke andere upload."),
            ("Kan ik niet gewoon livekijkers kopen voor de teller?", "Dat kan, maar het werkt averechts. Kunstmatige kijkers bij een stream zijn nep-engagement zoals elk ander, en een volle teller boven een lege chat valt echte kijkers snel op."),
            ("Welk pakket past bij een kanaal dat streamt?", "{pick_name} is ons populairste, met doorgaans {pick_audience} nieuwe abonnees per maand; een nieuwer kanaal kan beginnen met {starter_name}. Elke stream daarna heeft meer mensen die erbij kunnen komen."),
        ],
    },
    {
        "service": "views",
        "modifier": "monthly",
        "slug": "youtube/views/maandelijks",
        "label": "Maandelijkse YouTube-views",
        "title": "YouTube-views voor meerdere video's? Kies per maand | Growsterr",
        "description": "YouTube-views kopen voor meerdere video's, verspreid over tijd: een maandpakket brengt echte kijkers naar uw hele kanaal, waar ze zelf kiezen. Vanaf {from_price}.",
        "h1": ("YouTube-views voor meerdere video's, ", "maand na maand."),
        "intro": "Wie YouTube-views koopt voor meerdere video's, wil eigenlijk een kanaal waar mensen naar terug blijven komen. Daar is een maandpakket precies voor gemaakt: echte mensen ontdekken uw kanaal elke dag en bekijken de video's die hen interesseren, en de campagne verlengt elke maand, zodat nieuwe uploads steeds nieuwe kijkers treffen.",
        "hero": {"image": "youtube-viewers", "alt": "Een kijker gaat op hetzelfde kanaal van de ene YouTubevideo naar de volgende"},
        "sections": [
            {
                "h2": "Eén kanaal, veel video's",
                "p": [
                    "Geïnteresseerde kijkers stoppen niet na één video. Wie u via een tutorial vindt, opent de volgende, en daarna wat uw kanaalpagina voorstelt. Een campagne rond uw kanaal, in plaats van rond één link, volgt hoe mensen echt kijken.",
                ],
            },
            {
                "h2": "Bepalen waar nieuwe kijkers daarna heen gaan",
                "p": [
                    "We promoten uw kanaal als geheel; kijkers beslissen welke video's ze openen. Wat u wel in de hand hebt, is het pad voor hen zodra ze binnen zijn.",
                ],
                "ul": [
                    "Stel een kanaaltrailer in voor bezoekers die nog niet zijn geabonneerd.",
                    "Zet uw sterkste upload bovenaan uw kanaalpagina.",
                    "Groepeer verwante video's in playlists, zodat de ene naar de volgende leidt.",
                    "Voeg eindschermen toe die verwijzen naar de video die een kijker hierna moet zien.",
                ],
            },
            {
                "h2": "Waarom gespreid beter werkt dan alles tegelijk",
                "p": [
                    "Views verspreid over een maand bereiken elke upload terwijl hij nieuw is en houden oudere video's levend. Een eenmalige uitschieter op meerdere video's doet het omgekeerde: één piek op elk ervan, en dan stilte.",
                ],
                "image": {"image": "youtube-channel", "alt": "Een creator zet een reeks YouTubevideo's klaar om in de loop van de maand te publiceren"},
            },
        ],
        "faqs": [
            ("Naar hoeveel video's kunnen de views gaan?", "Er is geen lijst en geen limiet. We promoten uw kanaal, en kijkers bekijken wat hen interesseert, waar dan ook op het kanaal."),
            ("Krijgen nieuwe uploads in de loop van de maand views?", "Ja. De campagne loopt elke dag, dus een video die u halverwege de maand publiceert, ontmoet nog steeds nieuwe mensen, en uw nieuwe abonnees kunnen hem zien zoals elke abonnee."),
            ("Is de prijs per video?", "Nee, per maand voor uw hele kanaal: {starter_name} kost {starter_price} per maand, {rising_name} {rising_price} en {pro_name} {pro_price}, hoeveel video's u ook hebt. Views zitten erin, met abonnees, likes en reacties."),
            ("Kan ik na één maand stoppen?", "Ja. Zeg op in uw account; de betaalde maand loopt gewoon af en de volgende wordt niet in rekening gebracht."),
            ("Kunnen de views uit één stad komen?", "Ja. Eén stad werkt, net als een regio of een heel land. Dat past bij kanalen met een lokaal publiek, zoals een culinaire stadsgids of een lokaal nieuwskanaal."),
        ],
    },
    {
        "service": "views",
        "modifier": "no-drop",
        "slug": "youtube/views/zonder-uitval",
        "label": "YouTube-views zonder uitval",
        "title": "Echte YouTube-views zonder uitval? Waarom aantallen dalen",
        "description": "Waarom YouTube-viewaantallen dalen na een aankoop, en waarom views van mensen die zelf op play drukten anders zijn. Vanaf {from_price} per maand.",
        "h1": ("Echte YouTube-views zonder uitval kopen? ", "Begin met views die nooit nep waren."),
        "intro": "Wie echte YouTube-views zonder uitval wil kopen, heeft meestal al eens een aantal zien zakken. Views dalen als YouTube weergaven verwijdert die het als kunstmatig beoordeelt. De onze komen van echte mensen die zelf op play drukten, in een maandpakket, dus er ligt geen partij nepweergaven klaar om te worden teruggenomen.",
        "hero": {"image": "youtube-channel", "alt": "Een creator in de studio ziet het viewaantal van een YouTubevideo stabiel blijven"},
        "sections": [
            {
                "h2": "Waarom viewaantallen dalen",
                "p": [
                    "YouTube controleert views en verwijdert de views die het niet als oprecht beschouwt: weergaven van bots, scripts en ander kunstmatig verkeer. Gebeurt dat na een aankoop, dan daalt het aantal, soms lang na de levering, en de geschiedenis van de video toont een piek gevolgd door een val.",
                ],
            },
            {
                "h2": "Wat we wel en niet kunnen beloven",
                "p": [
                    "We kunnen niet beloven dat YouTube een aantal nooit aanpast; het controleert al het verkeer, ook het onze. Wat we wel kunnen vertellen, is hoe onze views ontstaan: een echt mens ziet uw kanaal via een gepromote campagne en kiest ervoor te kijken. Dat is het soort view dat de controles van YouTube juist willen behouden.",
                ],
            },
            {
                "h2": "Als views, likes en abonnees samen stijgen",
                "p": [
                    "Echte views reizen zelden alleen. In een pakket komen ze met nieuwe abonnees, likes en reacties van dezelfde mensen, dus uw cijfers stijgen samen en niets valt uit de toon, voor YouTube noch voor een kijker.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Vrienden kijken samen een YouTubevideo en laten aan het eind een like achter"},
            },
        ],
        "faqs": [
            ("Gaan mijn views ooit omlaag?", "YouTube kan het aantal van elke video aanpassen als het verkeer controleert, dus niemand kan eerlijk een getal beloven dat nooit beweegt. Views van mensen die kozen te kijken, zijn het soort dat die controle wil behouden."),
            ("Vullen jullie views aan als het aantal daalt?", "Nee. Aanvullen ruilt verwijderde nepweergaven in voor nieuwe. Wij verkopen in plaats daarvan een maandpakket met echte mensen, dus er valt niets kunstmatigs te vervangen."),
            ("Waarom daalden mijn views na een eerdere aankoop?", "Meestal omdat YouTube weergaven verwijderde die het als kunstmatig beoordeelde. Dat kan weken na de levering gebeuren, en daarom komt een daling vaak als een verrassing."),
            ("Kan ik views zonder uitval kopen voor één video?", "Niet als losse bestelling. Views zitten in een maandpakket dat uw hele kanaal laat groeien, dus elke video kan ervan profiteren."),
            ("Wat komt er nog meer met de views mee?", "De kijkers brengen de rest zelf mee. Met {pick_name} doorgaans {pick_audience} abonnees, {pick_likes} likes en {pick_comments} reacties per maand."),
        ],
    },
    {
        "service": "views",
        "modifier": "organic",
        "slug": "youtube/views/organisch",
        "label": "Organische, gerichte YouTube-views",
        "title": "Gerichte YouTube-views kopen? Kies stad of land | Growsterr",
        "description": "Gerichte YouTube-views kopen uit de stad, regio of het land waar uw publiek woont: organische kijkers die zelf kozen te kijken, in een maandpakket vanaf {from_price}.",
        "h1": ("Gerichte YouTube-views kopen, ", "uit de plek waar uw publiek woont."),
        "intro": "Wilt u gerichte YouTube-views kopen, vertel ons dan waar uw kijkers moeten zitten: een stad, een grotere regio of een heel land. We tonen uw kanaal via gepromote campagnes aan echte mensen daar, en de views zijn organisch op de manier die ertoe doet: achter elke view zit iemand die koos te kijken.",
        "hero": {"image": "youtube-channel", "alt": "Een creator filmt een YouTubevideo in een stadsstraat voor een lokaal publiek"},
        "sections": [
            {
                "h2": "Waarom locatie de targeting is die telt",
                "p": [
                    "Een kookkanaal in Rotterdam, een vastgoedkanaal in Antwerpen, een Turkstalig gamingkanaal: elk heeft een publiek dat ergens woont en een taal spreekt. Kijkers van die plek begrijpen uw video's, komen terug voor de volgende en worden misschien klant als u iets verkoopt.",
                    "We richten uw campagne eerst op de plek die u kiest. Is de beste match voor uw kanaal een groter publiek net over een grens, dan kan een deel van uw kijkers daarvandaan komen.",
                ],
            },
            {
                "h2": "Gericht is niet gedwongen",
                "p": [
                    "We richten op waar mensen zijn en laten hen dan beslissen. Niemand wordt gedwongen uw video te bekijken, en er speelt niets af wat niet gekozen is. Een gerichte view blijft een keuze, en dat maakt hem organisch.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Lokale kijkers in een café bekijken een YouTubevideo die in hun eigen stad is gemaakt"},
            },
            {
                "h2": "Zo kiest u uw locatie",
                "ul": [
                    "Kies de plek waarvoor uw video's gemaakt zijn, niet de grootste plek die u kunt noemen.",
                    "Voor een lokaal bedrijf of een stadskanaal kiest u de stad zelf.",
                    "Gaat het om een taal in plaats van een plek, kies dan het land waar de meeste sprekers wonen.",
                    "Voor een internationale niche begint u met het land waarvan u de kijkers het liefst bereikt.",
                ],
            },
        ],
        "faqs": [
            ("Hoe nauwkeurig is de targeting?", "Zo nauwkeurig als een stad. Hoe kleiner de plek, hoe kleiner het publiek, dus in een kleine plaats kunnen sommige kijkers uit de omliggende regio komen."),
            ("Maakt targeting de views minder organisch?", "Nee: de beslissing om te kijken blijft van hen. Wij betalen om uw kanaal te tonen op de plek die u koos; elke kijker beslist daarna zelf, en niemand wordt beloond om te kijken."),
            ("Gaan kijkers uit mijn stad zich abonneren?", "Sommigen wel, als uw kanaal hen aanspreekt. Met {pick_name} doorgaans {pick_audience} nieuwe abonnees per maand, uit de plek die u koos en de omgeving."),
            ("Waarom niet het grootst mogelijke gebied kiezen?", "Een groter gebied is een grotere vijver, maar kijkers die uw taal of context niet delen, blijven zelden. De juiste plek wint van de grootste."),
            ("Hebben jullie toegang tot mijn kanaal nodig om kijkers te targeten?", "Nee. Targeting gebeurt in onze campagnes, niet in uw kanaalinstellingen. We hebben uw handle en een locatie nodig, nooit uw wachtwoord."),
        ],
    },
    {
        "service": "views",
        "modifier": "promote",
        "slug": "youtube/views/promoten",
        "label": "Uw YouTube-video's promoten",
        "title": "YouTube-views via AdWords kopen? Zo promoten wij | Growsterr",
        "description": "Overweegt u YouTube-views via AdWords te kopen? Wij promoten uw kanaal voor u bij echte mensen, per maand, met abonnees, likes en reacties. Vanaf {from_price}.",
        "h1": ("YouTube-views via AdWords kopen? ", "Of laat ons de promotie doen."),
        "intro": "Wie YouTube-views via AdWords wil kopen, zoekt betaald bereik voor een video. De eigen advertenties van Google zijn één manier: een campagne die u zelf opzet, beheert en betaalt in de advertentietools van Google. Wij zijn een andere. We promoten uw kanaal elke dag bij echte mensen via campagnes in ons partnernetwerk, en u volgt de resultaten in uw dashboard.",
        "hero": {"image": "youtube-viewers", "alt": "Mensen ontdekken een gepromote YouTubevideo op hun telefoon en tablet"},
        "sections": [
            {
                "h2": "Zelf advertenties draaien, of een beheerde campagne",
                "p": [
                    "Met Google Ads, de tool die AdWords verving, bouwt u de campagne zelf: doelgroep, biedingen, budget en de advertentie zelf. U betaalt naarmate het systeem levert, en erop letten is uw taak.",
                    "Een Growsterr-pakket is de kant waarbij het voor u wordt gedaan. U geeft ons uw kanaalhandle en een doellocatie; ons team voert de promotie elke dag, en uw dashboard toont kanaalbezoeken en nieuwe abonnees. Eén maandprijs, geen biedingen om te beheren.",
                ],
            },
            {
                "h2": "Waar een gepromote view naartoe moet leiden",
                "p": [
                    "Een betaalde view loont alleen als de kijker daarna iets doet: nog een video bekijken, liken, abonneren. Daarom zijn onze pakketten rond abonnees gebouwd, met likes, reacties en views van dezelfde mensen, en niet rond een aantal weergaven.",
                ],
                "image": {"image": "youtube-channel", "alt": "Een creator bekijkt de nieuwe abonnees van een YouTubevideo nadat een promotie startte"},
            },
            {
                "h2": "Wat we niet doen",
                "ul": [
                    "We zetten geen Google Ads op en beheren die niet, en we vragen nooit om toegang tot uw Google-account.",
                    "We verkopen geen views per duizend of tegen een prijs per view.",
                    "U kunt één video noemen waar nieuwe kijkers op terechtkomen, maar we stemmen promotie niet af op een lanceeruur.",
                    "We beloven geen monetisatie, kijkuren of een plek in de aanbevelingen.",
                ],
            },
        ],
        "faqs": [
            ("Is dit hetzelfde als YouTube-advertenties draaien?", "Nee. YouTube-advertenties draaien in uw eigen Google Ads-account, met uw budget en instellingen. Wij promoten uw kanaal via ons partnernetwerk en voeren de campagne voor u; er draait niets in uw account."),
            ("Kunnen jullie mijn Google Ads-campagnes beheren?", "Dat bieden we niet aan. Ons werk zijn maandelijkse groeipakketten; voor iets groters kunt u met ons praten via WhatsApp of e-mail."),
            ("Hoe verschillen de kosten van advertenties?", "Advertenties rekenen af naarmate ze leveren, dus wat u uitgeeft, beweegt mee met uw biedingen en budget. Onze pakketten hebben een vaste maandprijs, {starter_price}, {rising_price} of {pro_price}, met typische bereiken voor abonnees, likes en reacties."),
            ("Kan ik tegelijk mijn eigen advertenties draaien?", "Ja. Uw advertenties draaien in uw account en onze campagne in ons netwerk, dus het een zit het ander niet in de weg."),
            ("Welke video's promoten jullie?", "Uw kanaal als geheel, niet één upload, en kijkers kiezen wat ze bekijken. Zet een lancering of een nieuwe serie op de uitgelichte plek van uw kanaal, dan vinden nieuwe bezoekers hem makkelijker."),
        ],
    },
    {
        "service": "views",
        "modifier": "real",
        "slug": "youtube/views/echt",
        "label": "Echte YouTube-views",
        "title": "YouTube-views van kwaliteit kopen? Elk is een mens | Growsterr",
        "description": "YouTube-views van kwaliteit kopen, van echte mensen die zelf kozen te kijken, met abonnees, likes en reacties van dezelfde kijkers. Vanaf {from_price}.",
        "h1": ("YouTube-views van kwaliteit kopen? ", "Begin met een mens achter elke weergave."),
        "intro": "Voordat u YouTube-views van kwaliteit koopt, helpt het om kwaliteit te definiëren. Voor ons heeft een kwaliteitsview een mens erachter: iemand die uw kanaal zag, een video koos en keek omdat het hem interesseerde. Dat is de enige soort die onze pakketten brengen, en dezelfde mensen abonneren, liken en reageren ook.",
        "hero": {"image": "youtube-viewers", "alt": "Een echte kijker kiest een YouTubevideo om te bekijken op het kanaal van een creator"},
        "sections": [
            {
                "h2": "Wat een echte view onderscheidt van een weergave",
                "ul": [
                    "Een mens koos ervoor: niemand werd betaald of gescript om op play te drukken.",
                    "Hij leidt ergens heen: sommige kijkers liken, reageren of abonneren.",
                    "Hij heeft een thuis: de kijker woont waar u de campagne op richtte.",
                    "Hij houdt stand: er zit niets kunstmatigs in wat YouTube kan verwijderen.",
                ],
            },
            {
                "h2": "Waarom gegradeerde botviews nog steeds geen kwaliteit zijn",
                "p": [
                    "Sommige verkopers delen hun views in als standaard, hoge kwaliteit of premium. Wat het label ook is, de vraag die telt blijft dezelfde: koos een mens ervoor te kijken? Zo niet, dan betekent een hogere klasse alleen een hogere prijs voor dezelfde lege weergave.",
                ],
            },
            {
                "h2": "Kwaliteit die u in YouTube Studio kunt lezen",
                "p": [
                    "Echte views laten sporen na: kijktijd die per kijker verschilt, reacties die op uw video ingaan, en abonnees die u wint op de video's die mensen bekeken. Die sporen maken een view waardevol, en precies die laten gegenereerde weergaven nooit achter.",
                ],
                "image": {"image": "youtube-channel", "alt": "Een creator leest kijktijd en reacties van een YouTubevideo in de statistieken"},
            },
        ],
        "faqs": [
            ("Hoe verschilt een kwaliteitsview van een goedkope?", "Een goedkope view is meestal een weergave waar niets op volgt. Een kwaliteitsview is een mens die misschien liket, reageert, zich abonneert of terugkomt, en alleen die soort helpt uw kanaal."),
            ("Kan ik zien wie de kijkers zijn?", "Uw dashboard toont de kanaalbezoeken en nieuwe abonnees van uw campagne, en YouTube Studio laat zien waar kijkers zitten en hoe lang ze kijken. Individuele kijkers blijven privé, zoals op elk kanaal."),
            ("Komen views zonder abonnees of likes?", "Nee. Ze komen in één pakket van dezelfde mensen, en dat maakt ze tot groei in plaats van een getal."),
            ("Waarom geen pakketten van duizend views?", "Omdat duizend views op bestelling duizend weergaven betekent die iemand heeft gegenereerd. Wij brengen liever mensen en laten hen kiezen wat ze bekijken."),
            ("Kan ik kiezen waar de kijkers wonen?", "Ja: noem de plek bij uw bestelling, van één stad tot een heel land. Lokale kijkers begrijpen uw video's, en daardoor zijn hun views meer waard dan een getal."),
        ],
    },
    {
        "service": "views",
        "modifier": "safe",
        "slug": "youtube/views/veilig",
        "label": "Veilige YouTube-views",
        "title": "Betrouwbaar YouTube-views kopen: wat een kanaal veilig houdt",
        "description": "Betrouwbaar en veilig YouTube-views kopen? Zie wat YouTube als nep beschouwt, wat dat voor uw kanaal betekent en hoe echte kijkers u via ons bereiken.",
        "h1": ("Betrouwbaar YouTube-views kopen? ", "Weet wat een kanaal in gevaar brengt."),
        "intro": "Wilt u betrouwbaar en veilig YouTube-views kopen, begin dan bij waar YouTube tegen optreedt: views van bots, scripts en elk verkeer dat geen mens is die ervoor kiest te kijken. Wij blijven aan de goede kant van die grens door uw kanaal alleen te promoten bij echte mensen, die kijken als ze dat willen.",
        "hero": {"image": "youtube-channel", "alt": "Een creator bekijkt in een rustig thuiskantoor hoe het YouTube-kanaal ervoor staat"},
        "sections": [
            {
                "h2": "Wat YouTube als nepviews beschouwt",
                "p": [
                    "De regels van YouTube over nep-engagement gelden voor al het volgende. YouTube kan de views verwijderen, en content die erop is gebouwd, kan offline worden gehaald.",
                ],
                "ul": [
                    "Weergaven van bots of geautomatiseerde scripts.",
                    "Views van mensen die worden betaald of beloond om te kijken.",
                    "Video's die automatisch afspelen waar kijkers er nooit voor kozen.",
                    "Views die tussen kanalen worden geruild.",
                ],
            },
            {
                "h2": "Zo komen onze views binnen",
                "p": [
                    "Ons partnernetwerk voert gepromote campagnes die uw kanaal onder de aandacht van echte mensen brengen. Niemand wordt betaald om te kijken, er speelt niets af zonder dat het gekozen is, en niets raakt uw YouTube-account aan. Mensen die leuk vinden wat ze zien, kijken meer, liken, reageren en abonneren.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Een kijker kiest op de telefoon een gepromote YouTubevideo om te bekijken"},
            },
            {
                "h2": "Ook veilig voor uw account",
                "ul": [
                    "We werken vanuit uw openbare kanaalhandle: geen login, geen toegangsverzoeken.",
                    "Betalen gaat via een maandelijks Stripe-abonnement dat u vanuit uw account beheert.",
                    "Stoppen bepaalt u zelf, op elk moment, zonder vragen te hoeven beantwoorden.",
                ],
            },
        ],
        "faqs": [
            ("Kan views kopen ervoor zorgen dat mijn video wordt verwijderd?", "Nepviews kunnen dat: YouTube kan ze uit het aantal halen, en content die de regels over nep-engagement overtreedt, kan offline worden gehaald. Views van mensen die kozen te kijken, zijn geen nep-engagement."),
            ("Wie runt Growsterr?", "Sterr Agency, met als ingeschreven bedrijf Sterr Technologies OÜ in Tallinn, Estland. Het hoofdkantoor van het team staat in Turkije."),
            ("Hebben jullie mijn YouTube- of Google-login nodig?", "Nee, en een dienst die erom vraagt, is op zich al een risico. We hebben alleen uw openbare kanaalhandle nodig."),
            ("Mag een video op YouTube gepromoot worden?", "Een video promoten zodat mensen hem kunnen ontdekken, is heel gewoon; kanalen doen het elke dag met advertenties. YouTube trekt de grens bij kunstmatige of beloonde views, en wij blijven aan de goede kant ervan."),
            ("Wat als ik niet tevreden ben?", "Stop het abonnement in uw account, dan wordt er geen nieuwe maand in rekening gebracht. Uw dashboard toont wat we hebben gemeten, dus u kunt de campagne op feiten beoordelen."),
        ],
    },
    {
        "service": "views",
        "modifier": "shorts",
        "slug": "youtube/views/shorts",
        "label": "Views op YouTube Shorts",
        "title": "YouTube-reelviews kopen? Op YouTube heten ze Shorts | Growsterr",
        "description": "Op YouTube heten reels Shorts. Wij brengen echte kijkers die uw Shorts blijven bekijken, in een maandpakket met abonnees. Vanaf {from_price} per maand.",
        "h1": ("Views voor YouTube-reels kopen? ", "Krijg Shorts-kijkers die blijven kijken."),
        "intro": "Wilt u views voor YouTube-reels kopen, dan bedoelt u Shorts: de korte, verticale video's van YouTube. Shorts-views verkopen we niet in bulk. We brengen elke dag echte mensen naar uw kanaal, en wie van uw Shorts geniet, kijkt, kijkt nog eens, liket en abonneert zich soms.",
        "hero": {"image": "youtube-viewers", "alt": "Iemand bekijkt een YouTube Short op de telefoon en laat hem herhalen"},
        "sections": [
            {
                "h2": "Goedkope Shorts-views zijn makkelijk na te maken en makkelijk te doorzien",
                "p": [
                    "Goedkope Shorts-views zijn overal, omdat een weergave in seconden te genereren is. Wat er na de weergave gebeurt, is het moeilijke deel: bleef de kijker kijken, keek hij opnieuw, liket hij, opende hij uw kanaal? Gegenereerde weergaven zeggen op alles nee, en YouTube behandelt ze als spam.",
                ],
            },
            {
                "h2": "Zo wordt een Shorts-kijker een abonnee",
                "p": [
                    "Shorts zijn een voordeur. Een echte kijker die er een leuk vindt, kan op uw naam tikken, rondkijken op uw kanaal en zich abonneren, en vanaf dan kunnen ook uw langere video's hem bereiken. Door die route is een Shorts-view van een mens zoveel meer waard dan een weergave.",
                ],
                "image": {"image": "youtube-channel", "alt": "Een creator bekijkt een verticale YouTube Short op de telefoon voordat hij hem publiceert"},
            },
            {
                "h2": "Meer halen uit de Shorts die u post",
                "ul": [
                    "Houd uw beste Shorts goed vindbaar op uw kanaalpagina, waar nieuwsgierige kijkers terechtkomen.",
                    "Koppel vanuit uw Short een verwante lange video, zodat geïnteresseerde kijkers ergens heen kunnen.",
                    "Post in een vast ritme, zodat nieuwe abonnees bij elk bezoek iets nieuws vinden.",
                ],
            },
        ],
        "faqs": [
            ("Zijn YouTube-reels hetzelfde als Shorts?", "Ja. Reels is de naam die Instagram gebruikt; op YouTube heet hetzelfde korte, verticale formaat Shorts. Alles op deze pagina geldt voor Shorts."),
            ("Kan ik goedkope views kopen voor één Short?", "Er is geen prijs per Short, en we richten views niet op één Short. Een pakket promoot uw kanaal, en kijkers kiezen de Shorts die ze willen zien."),
            ("Kunnen jullie mijn Shorts in de Shorts-feed krijgen?", "Dat kan niemand eerlijk beloven, dus wij doen het ook niet. We brengen echte kijkers; hoe YouTube een Short daarna verspreidt, is zijn eigen beslissing."),
            ("Waarom noemen jullie geen aantal Shorts-views?", "Een Short kan worden herhaald, overgeslagen of in een loop gespeeld, en een vooraf beloofd viewaantal is alleen te halen door weergaven te genereren. Wij noemen typische maandbereiken voor wat mensen na het kijken doen: abonneren, liken en reageren."),
            ("Is het veilig om YouTube Shorts-views te kopen?", "Bij een botdienst niet: een nepweergave is nep, of de video nu dertig seconden of een uur duurt. Echte kijkers die uw Shorts kiezen, zijn een gewoon publiek, welk formaat u ook post."),
        ],
    },
]
