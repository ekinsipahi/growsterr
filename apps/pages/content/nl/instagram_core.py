"""Dutch Instagram pages: reacties, likes, en de manieren waarop mensen naar volgers en likes
vragen (geleidelijk, organisch, lokaal, privéaccount...). Keys and placeholders: docs/CONTENT.md.
Numbers come from the packages ({starter_likes}...), so they follow apps/growth/plan.py."""

UPDATED = "2026-11-08"

PAGES = [
    # --- Reacties -----------------------------------------------------------------------
    {
        "service": "comments",
        "slug": "instagram/reacties",
        "label": "Instagram-reacties",
        "title": "Instagram-reacties kopen van echte mensen | Growsterr",
        "description": "Instagram-reacties kopen? Bij ons zitten ze in elk maandpakket, geschreven door echte mensen in hun eigen woorden. Doorgaans {starter_comments} per maand.",
        "h1": ("Instagram-reacties kopen ", "van mensen die het menen."),
        "intro": "Wilt u Instagram-reacties kopen? Dan is het goed om te weten dat wij ze maar op één manier brengen: in een maandpakket, van echte mensen die uw berichten ontdekken en iets te zeggen hebben. Doorgaans {starter_comments} reacties per maand met {starter_name}, {pick_comments} met {pick_name}.",
        "hero": {"image": "instagram-real-people", "alt": "Mensen laten hun eigen reacties, vragen en emoji achter onder een Instagrambericht"},
        "sections": [
            {
                "h2": "Zo ziet een echte reactiesectie eruit",
                "p": [
                    "Echte reacties zijn ongelijk. De een vraagt waar de jas vandaan komt, de ander tagt een vriendin, een derde schrijft twee woorden en een emoji. Juist die ongelijkheid maakt een reactiesectie geloofwaardig, en precies dat kunnen gescripte reacties niet nabootsen.",
                    "Reacties die in bulk worden gekocht, komen meestal binnen als bijna identieke zinnen van accounts zonder eigen berichten. Iedereen die scrolt, ziet het, ook de merken en samenwerkingspartners die u wilt overtuigen.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "Een creator aan een bureau beantwoordt reacties onder een Instagrambericht"},
            },
            {
                "h2": "Hoeveel reacties elk pakket brengt",
                "ul": [
                    "{starter_name}, voor {starter_price} per maand, brengt doorgaans {starter_comments} reacties, op de berichten die mensen het leukst vinden.",
                    "{rising_name}, voor {rising_price}, brengt doorgaans {rising_comments}, en u kiest zelf welke berichten de aandacht krijgen.",
                    "{pro_name}, voor {pro_price}, brengt doorgaans {pro_comments}, plus voorrang bij de plaatsing en een eigen WhatsApp-lijn.",
                ],
            },
            {
                "h2": "Waarom reacties alleen in een pakket zitten",
                "p": [
                    "Een bericht met veertig reacties en een handvol likes laat iedereen zien wat er is gebeurd. Reacties zien er alleen goed uit naast de volgers, likes en views die echte aandacht oplevert. Daarom brengen wij die aandacht, en laten we de reacties daaruit groeien.",
                ],
            },
        ],
        "faqs": [
            ("Kan ik Instagram-reacties krijgen zonder pakket?", "Nee. Reacties zitten alleen in onze maandpakketten, van mensen die uw profiel via onze campagnes vonden. Niemand schrijft ze op bestelling, en daarom lezen ze als een gesprek."),
            ("Kan ik bepalen wat er in de reacties staat?", "Nee. Mensen schrijven in hun eigen woorden, dus er valt niets te scripten, en reacties naar een briefje lezen zelden als een echte reactie. Wat u wel kunt kiezen, met {rising_name} of {pro_name}, is waar de aandacht naartoe gaat: de berichten die u aanwijst."),
            ("Wanneer verschijnen de reacties?", "Verspreid over de maand, steeds een paar, terwijl mensen uw berichten ontdekken. Honderd reacties in tien minuten zou een script zijn, geen publiek."),
            ("Helpen reacties mijn berichten meer mensen te bereiken?", "Reacties laten zien dat mensen om een bericht geven, en Instagram merkt dat op. Echte reacties dragen daaraan bij. Bereik kunnen we niet beloven, en niemand die eerlijk is kan dat, maar gescripte reacties voegen alleen ruis toe."),
            ("Hebt u mijn wachtwoord nodig?", "Nee. We hebben uw Instagram-gebruikersnaam nodig en de plek waar uw publiek vandaan moet komen. Houd uw account openbaar, zodat mensen uw berichten kunnen lezen en kunnen meepraten."),
        ],
    },
    # --- Volgers: de manieren waarop mensen ernaar vragen -------------------------------
    {
        "service": "followers",
        "modifier": "gradual",
        "slug": "instagram/volgers/geleidelijk",
        "label": "Geleidelijke Instagram-volgers",
        "title": "Instagram-volgers kopen per dag, nooit in één keer | Growsterr",
        "description": "Instagram-volgers per dag in plaats van in één klap: 30 dagen lang vinden echte mensen elke dag uw profiel. Geleidelijke groei, nooit een plotselinge stapel.",
        "h1": ("Instagram-volgers per dag, ", "zoals mensen echt volgen."),
        "intro": "Wilt u Instagram-volgers liever per dag kopen dan allemaal tegelijk? Dan denkt u al als een publiek. Onze campagnes tonen uw profiel 30 dagen lang elke dag aan echte mensen, dus volgers komen geleidelijk binnen, dag na dag: doorgaans {pick_audience} in de hele maand met {pick_name}.",
        "hero": {"image": "instagram-followers-1000", "alt": "Een volgersaantal dat een maand lang elke dag een stukje stijgt"},
        "sections": [
            {
                "h2": "Drip feed is een instelling. Dagelijkse groei is een campagne.",
                "p": [
                    "Sommige diensten verkopen een trage druppel: een partij accounts die steeds per paar wordt vrijgegeven, zodat de lijn er natuurlijk uitziet. Het blijven bots; alleen de timing is vermomd.",
                    "Ons tempo is helemaal geen instelling. Uw profiel wordt elke dag aan mensen getoond, en elke volger komt op het moment dat iemand dat zelf besluit. De geleidelijke lijn is simpelweg hoe het eruitziet als mensen zelf kiezen.",
                ],
            },
            {
                "h2": "Waarom langzaam beter is dan alles tegelijk",
                "ul": [
                    "Een gestage stijging ziet eruit als wat het is: een account dat mensen blijven ontdekken.",
                    "Wie vandaag volgt, ziet uw volgende bericht terwijl de interesse nog vers is.",
                    "Er is geen plotselinge piek waar een merk of een volger vraagtekens bij zet.",
                    "U ziet wat werkt, want elke dag is een eigen meetpunt.",
                ],
            },
            {
                "h2": "Uw dagcijfers lezen",
                "p": [
                    "Uw dashboard toont per dag hoeveel mensen via de campagne uw profiel bezochten en hoeveel van hen u gingen volgen. Sommige dagen zijn drukker dan andere: een sterk bericht, een weekend, een feestdag. Over de maand tellen die dagen op tot een typisch bereik, geen vast dagquotum.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "Een creator bekijkt een grafiek met profielbezoeken en nieuwe volgers per dag"},
            },
        ],
        "faqs": [
            ("Hoeveel volgers krijg ik per dag?", "Er is geen vast dagaantal, want mensen beslissen zelf. Over de maand brengt {pick_name} doorgaans {pick_audience}, dus een gemiddelde dag brengt daar een deel van, de ene dag meer, de andere minder."),
            ("Kan ik de snelheid van de druppel zelf instellen?", "Nee, en dat hoeft ook niet. Het tempo komt van mensen, niet van een knop: de campagne loopt elke dag en volgers komen wanneer iemand daarvoor kiest."),
            ("Is geleidelijke groei minder riskant dan een grote partij?", "Honderden volgers in een uur is een patroon dat bots achterlaten. Geleidelijke groei van echte mensen laat dat patroon niet achter, omdat het geen patroon is. Hoe Instagram een account beoordeelt, kunnen we niet zeggen; we zorgen er alleen voor dat elke volger die we brengen een mens is."),
            ("Betekent geleidelijk minder groei?", "Nee. Geleidelijk zegt iets over de vorm, niet over het totaal. Het typische maandbereik is hetzelfde, of iemand nu op dag twee of op dag negenentwintig volgt; het komt alleen binnen zoals een publiek groeit."),
            ("Komen likes en reacties ook geleidelijk?", "Ja. Dezelfde mensen liken en reageren terwijl ze uw berichten vinden, dus beide groeien mee met uw volgers. Met {pick_name} komt dat doorgaans neer op {pick_likes} likes en {pick_comments} reacties per maand."),
        ],
    },
    {
        "service": "followers",
        "modifier": "live",
        "slug": "instagram/volgers/live",
        "label": "Instagram-volgers: levering en Live",
        "title": "Instagram-volgers met snelle levering, uitgelegd | Growsterr",
        "description": "Hoe snel is de levering als u Instagram-volgers koopt van echte mensen? De campagne start snel, groeit elke dag en bouwt een publiek op voor uw Lives.",
        "h1": ("Instagram-volgers met snelle levering? ", "Dit betekent snel echt."),
        "intro": "Instagram-volgers kopen met snelle levering betekent meestal een van twee dingen: een teller die binnen minuten omhoogschiet, of een campagne die snel start en blijft lopen. Wij doen alleen het tweede. Uw campagne gaat snel van start, echte mensen komen vanaf de eerste dagen, en uw dashboard toont wat elke dag opleverde.",
        "hero": {"image": "instagram-creator-studio", "alt": "Een creator maakt zich aan een bureau klaar om live te gaan op Instagram"},
        "sections": [
            {
                "h2": "Snel waar het telt, nooit direct",
                "p": [
                    "Het snelle deel is de start. We zetten uw campagne kort na uw bestelling op, en mensen zien uw profiel vanaf de eerste dagen. Wat we niet doen, is een maand aan echte beslissingen in een uur proppen, want dat kan alleen met accounts waar niemand achter zit.",
                    "Kijk bij het vergelijken van levertijden dus naar wanneer echte groei begint en of die doorgaat, niet naar hoe snel een getal verspringt.",
                ],
            },
            {
                "h2": "Volgers voor uw Instagram Lives",
                "p": [
                    "Live-volgers zijn gewoon volgers die er zijn wanneer u live gaat. Instagram kan uw volgers een melding sturen als een uitzending begint, dus meer mensen die ervoor kozen u te volgen, betekent meer mensen die misschien aanhaken.",
                    "Live-kijkers verkopen we niet, en niemand kan een menigte op een vast tijdstip beloven: mensen kijken mee als ze interesse en tijd hebben. De volgers die u in de loop van de maand krijgt, zijn degenen die dat het vaakst doen.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Volgers kijken mee met de Instagram Live van een creator en reageren tijdens de uitzending"},
            },
            {
                "h2": "Ook likes komen geleidelijk",
                "p": [
                    "Likes houden hetzelfde ritme aan. Ze komen van de mensen die uw profiel ontdekken, dus ze verschijnen in de loop van de maand rustig op uw berichten, doorgaans {pick_likes} met {pick_name}. Er is geen aparte likesbestelling om in te plannen en geen piek om uit te leggen.",
                ],
            },
        ],
        "faqs": [
            ("Hoe snel start de levering?", "Snel. Zodra uw bestelling binnen is, zetten we de campagne op en bezoeken mensen uw profiel vanaf de eerste dagen. De eerste volgers komen met die bezoeken en het gaat de hele maand door."),
            ("Kan ik directe levering krijgen?", "Nee. Directe levering werkt alleen met bots, want geen mens volgt binnen enkele seconden na een betaling. Wij starten snel en groeien elke dag."),
            ("Heb ik vóór mijn Live van vanavond nieuwe volgers?", "Misschien een paar, als uw campagne al loopt, maar we kunnen mensen niet op een uitzending afstemmen. Is een Live belangrijk voor u, begin dan een paar weken van tevoren, zodat uw nieuwe volgers u eerst wat hebben leren kennen."),
            ("Verkopen jullie kijkers voor Instagram Live?", "Nee. Live-kijkers zouden mensen moeten zijn die op een bepaalde minuut kijken, en dat kan niemand eerlijk leveren. De volgers die we brengen, kijken misschien uit zichzelf mee met uw Lives."),
            ("Waar kan ik mijn levering volgen?", "In uw dashboard, dat per dag de profielbezoeken uit onze campagne telt en de volgers die daaruit voortkwamen. Het totaal van uw account beweegt ook mee met uw andere groei en met ontvolgingen."),
        ],
    },
    {
        "service": "followers",
        "modifier": "no-drop",
        "slug": "instagram/volgers/zonder-uitval",
        "label": "Instagram-volgers die blijven",
        "title": "Blijvende Instagram-volgers: waarom mensen blijven | Growsterr",
        "description": "Blijvende Instagram-volgers kopen zonder uitval? Botaccounts verdwijnen bij opschoningen. Echte mensen blijven, want volgen was hun eigen idee.",
        "h1": ("Blijvende Instagram-volgers ", "beginnen bij echte mensen."),
        "intro": "Wie blijvende Instagram-volgers wil kopen, kent het andere soort al: een sprong omhoog, daarna een langzaam lek terug naar beneden. Volgers vallen af als het nooit mensen waren. De onze zijn mensen die ervoor kozen u te volgen, dus ze blijven zoals elk echt publiek blijft. En gaat er een weg, dan om dezelfde redenen als bij elke volger.",
        "hero": {"image": "instagram-followers", "alt": "Een Instagram-volgersaantal dat maandenlang stabiel blijft en stijgt"},
        "sections": [
            {
                "h2": "Waarom gekochte volgers afvallen",
                "p": [
                    "Instagram verwijdert regelmatig nep- en spamaccounts. Bestaan uw volgers uit zulke accounts, dan neemt elke opschoning een hap uit uw aantal. Aanvullingen vullen het getal weer aan met meer van hetzelfde, en de cirkel begint opnieuw.",
                    "Een mens wordt bij een opschoning niet verwijderd. Iemand gaat alleen weg als hij besluit te ontvolgen, en dat gebeurt veel minder vaak. Bovendien hebben uw berichten daar invloed op.",
                ],
            },
            {
                "h2": "Wat volgers laat blijven",
                "ul": [
                    "Ze kozen voor u, en een volger die met interesse begint, blijft meestal.",
                    "Ze komen uit de plek waar uw publiek woont, dus uw berichten zeggen hun iets.",
                    "Ze zien uw volgende berichten, en elk goed bericht is een reden om te blijven.",
                    "Uw ritme telt meer dan alles wat wij doen: mensen blijven voor berichten waar ze naar uitkijken.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Trouwe volgers liken en reageren nog steeds op het nieuwste bericht van een creator"},
            },
            {
                "h2": "Zonder uitval, eerlijk uitgelegd",
                "p": [
                    "We gaan u niet vertellen dat niemand ooit ontvolgt, want zo werken mensen niet. Wel kunnen we zeggen dat u niet de golven van verlies ziet die nepaccounts veroorzaken. Uw dashboard toont dag voor dag de nieuwe volgers die onze campagne bracht, dus u weet altijd wat van ons kwam.",
                ],
            },
        ],
        "faqs": [
            ("Zijn jullie volgers blijvend?", "Het zijn echte mensen, dus ze blijven zolang ze willen. Niemand kan beloven dat iemand nooit ontvolgt; wat we wel kunnen zeggen, is dat er geen enkel nepaccount tussen zit dat wacht om verwijderd te worden."),
            ("Vullen jullie aan als er volgers afvallen?", "Nee, want er valt niets aan te vullen. Aanvullingen bestaan voor volgers die bij opschoningen verdwijnen. De onze zijn mensen, en af en toe een ontvolging hoort bij elk echt publiek."),
            ("Waarom verdwijnen gekochte volgers?", "Meestal ontvolgen ze niet eens: de accounts worden verwijderd. Instagram ruimt nep- en spamprofielen in golven op, en het volgersaantal zakt met ze mee."),
            ("Wat gebeurt er met mijn volgers als ik opzeg?", "Ze blijven. Ze volgden omdat ze dat wilden, niet omdat een abonnement het ze opdroeg. Opzeggen betekent alleen dat we na afloop van uw betaalde maand geen nieuwe mensen meer brengen; wie u al hebt gewonnen, blijft uw volger."),
            ("Hoe houd ik de volgers die ik krijg?", "Post regelmatig, beantwoord reacties en geef nieuwe volgers in hun eerste weken een reden om terug te komen. Mensen blijven om dezelfde redenen als waarom ze gingen volgen."),
        ],
    },
    {
        "service": "followers",
        "modifier": "organic",
        "slug": "instagram/volgers/organisch",
        "label": "Organische Instagram-volgers",
        "title": "Organische Instagram-volgers: u betaalt voor bereik | Growsterr",
        "description": "Kunt u organische Instagram-volgers kopen? U kunt betalen om elke dag gezien te worden door echte mensen, op de plek die u kiest. Volgen blijft hun eigen keuze.",
        "h1": ("Organische Instagram-volgers kopen? ", "Betaal voor bereik, laat mensen kiezen."),
        "intro": "Strikt genomen kan niemand organische Instagram-volgers kopen: een volger is organisch omdat iemand er zelf voor koos. Wat u wel kunt kopen, is bereik. Elke dag komen echte mensen op de plek die u kiest via onze campagnes uw profiel tegen, en elke volger die daaruit voortkomt, is een eigen beslissing van iemand.",
        "hero": {"image": "instagram-real-people", "alt": "Mensen komen het Instagramprofiel van een creator tegen en kiezen ervoor te volgen"},
        "sections": [
            {
                "h2": "Waar betaald ophoudt en organisch begint",
                "p": [
                    "Onze campagnes zijn gepromoot: we betalen om uw profiel onder de aandacht te brengen van mensen in ons partnernetwerk. Dat deel is betaald, en dat zeggen we ook gewoon. Alles daarna niet. Niemand wordt gevraagd te volgen, en niemand volgt terug als onderdeel van een ruil.",
                    "Het werkt net als een advertentie of een vermelding op de pagina van iemand anders: u betaalt voor de kennismaking, het publiek beslist.",
                ],
            },
            {
                "h2": "Organische volgers, gericht op uw publiek",
                "p": [
                    "Organische groei werkt het best als de mensen die u zien er waarschijnlijk iets mee hebben. Noem de stad, regio of het land waar uw publiek woont, en daar tonen we uw profiel eerst. Een bakkerij in Haarlem en een reiscreator met lezers in heel Europa hebben andere mensen nodig, en daar mikken we op.",
                ],
            },
            {
                "h2": "Wat organisch uitsluit",
                "ul": [
                    "Follow-for-follow-ruilen en engagementgroepen.",
                    "Bots en nepprofielen, hoe langzaam ze ook worden vrijgegeven.",
                    "Inloggen in welke vorm dan ook: uw wachtwoord blijft bij u.",
                    "Volgerspieken die sneller gaan dan welk echt publiek ook zou kunnen.",
                ],
            },
        ],
        "faqs": [
            ("Zijn betaalde campagnes echt organisch?", "Het bereik is betaald, de volger niet. Elke nieuwe volger zag uw profiel en besloot zelf, en dat is precies wat een volger organisch maakt."),
            ("Krijg ik elke dag echte Instagram-volgers?", "Ja. De campagne loopt elke dag van de maand en mensen volgen terwijl ze u ontdekken. De ene dag brengt meer dan de andere; over de maand komt het met {pick_name} doorgaans neer op {pick_audience}."),
            ("Is dit hetzelfde als zelf Instagram-advertenties draaien?", "In de geest vergelijkbaar, in de praktijk anders. Wij voeren de campagnes in ons partnernetwerk, ons team houdt ze in de gaten, en u ziet gemeten bezoeken en nieuwe volgers in een dashboard. U hebt geen advertentieaccount of budget nodig om te beheren."),
            ("Helpt organische groei mijn berichten meer mensen te bereiken?", "Meer dan gekochte getallen ooit kunnen, want organische volgers zien en reageren echt op wat u post. Hoe ver één bericht reikt, hangt nog altijd van dat bericht af."),
            ("Is organische groei langzamer?", "Ze is gelijkmatiger. Een maand organische groei komt dag voor dag binnen in plaats van in een uur, en er volgt geen terugval zoals na een botpiek."),
        ],
    },
    {
        "service": "followers",
        "modifier": "private-account",
        "slug": "instagram/volgers/prive-account",
        "label": "Instagram-volgers voor een privéaccount",
        "title": "Instagram-volgers op een privéaccount krijgen | Growsterr",
        "description": "Instagram-volgers kopen voor een privéaccount? Mensen kunnen daar alleen een volgverzoek sturen, dus we vragen een openbaar profiel zolang de campagne loopt.",
        "h1": ("Volgers op een privéaccount? ", "Zet het openbaar terwijl u groeit."),
        "intro": "Wilt u volgers kopen of krijgen op een privé Instagram-account? Dan is er een eerlijke kanttekening: mensen kunnen een privéaccount niet volgen, alleen een verzoek sturen. Daarom vragen we u uw profiel openbaar te houden zolang uw campagne loopt. U bepaalt zelf wat erop staat, en uw wachtwoord hebben we nooit nodig.",
        "hero": {"image": "instagram-followers", "alt": "Een privé Instagramprofiel met een slotje naast hetzelfde profiel op openbaar"},
        "sections": [
            {
                "h2": "Wat een privéaccount met een campagne doet",
                "p": [
                    "Wie een privéprofiel vindt, ziet een naam, een bio en een slotje. Hij kan een volgverzoek sturen, maar ziet geen enkel bericht, dus de meeste mensen klikken verder. De paar die wel een verzoek sturen, wachten daarna tot u ze een voor een goedkeurt.",
                    "Een campagne die mensen naar die dichte deur stuurt, verspilt het grootste deel van haar bereik. Op een openbaar profiel kunnen dezelfde mensen door uw berichten scrollen, een besluit nemen en u zonder wachten volgen.",
                ],
            },
            {
                "h2": "Als een dienst zegt dat privéaccounts geen probleem zijn",
                "p": [
                    "Op een privéaccount stijgt een volgersaantal alleen als verzoeken worden goedgekeurd. Belooft iemand daar volgers zonder dat u iemand goedkeurt, dan moet hij dat goedkeuren zelf doen, vanuit uw account. Daarvoor uw wachtwoord afgeven, is het enige wat u nooit moet doen.",
                ],
            },
            {
                "h2": "Openbaar zonder de controle uit handen te geven",
                "ul": [
                    "Zet uw account openbaar voor de campagne en weer op privé wanneer u wilt.",
                    "Archiveer berichten die u liever voor uzelf houdt; er wordt niets verwijderd.",
                    "Deel persoonlijke verhalen met Goede vrienden in plaats van met iedereen.",
                    "Wie u volgt terwijl u openbaar bent, blijft volger als u weer op privé gaat.",
                ],
            },
        ],
        "faqs": [
            ("Kunnen jullie een privé Instagram-account laten groeien?", "Maar heel weinig, dus daar beginnen we niet aan. Mensen kunnen een verzoek sturen, maar ze zien uw berichten niet, dus weinigen doen het. Houd het account openbaar zolang de campagne loopt, dan kan die haar werk doen."),
            ("Verlies ik volgers als ik weer op privé ga?", "Nee. Wie u al volgt, blijft als u overschakelt naar privé. Nieuwe bezoekers moeten dan een verzoek sturen, dus de groei vertraagt zolang het account privé is."),
            ("Moet ik volgverzoeken goedkeuren?", "Niet zolang uw account openbaar is: mensen volgen u zonder verzoek. Schakelt u halverwege de maand naar privé, dan wachten nieuwe verzoeken op u en brengt de campagne veel minder volgers."),
            ("Hebben jullie toegang tot mijn account nodig om het te laten groeien?", "Nee. Uw inloggegevens blijven van u; we hebben alleen uw gebruikersnaam nodig, plus een openbaar profiel waar de mensen die we sturen naar kunnen kijken."),
            ("Werken likes op een privéaccount?", "Alleen van mensen die u al volgen, want verder kan niemand de berichten zien. Nog een reden waarom de campagne een openbaar profiel nodig heeft."),
        ],
    },
    {
        "service": "followers",
        "modifier": "real",
        "slug": "instagram/volgers/echt",
        "label": "Actieve Instagram-volgers",
        "title": "Actieve Instagram-volgers die liken en reageren | Growsterr",
        "description": "Actieve Instagram-volgers zijn mensen die liken, reageren en kijken. Bij ons komen likes en reacties van dezelfde accounts: doorgaans {pick_likes} per maand.",
        "h1": ("Actieve Instagram-volgers kopen ", "die echt iets doen."),
        "intro": "Wie actieve Instagram-volgers wil kopen, bedoelt volgers die liken, reageren en kijken, geen getal dat stilstaat. Dat gebeurt alleen met echte mensen, dus dat is het enige wat wij brengen: mensen die uw profiel ontdekken, ervoor kiezen u te volgen en reageren op de berichten die ze leuk vinden.",
        "hero": {"image": "instagram-real-people", "alt": "Nieuwe Instagram-volgers liken een bericht en beginnen een gesprek in de reacties"},
        "sections": [
            {
                "h2": "Echt lijken of echt zijn",
                "p": [
                    "Sommige volgers zijn gemaakt om echt te lijken: een geleende foto, een paar berichten, een geloofwaardige naam. Ze doorstaan een vluchtige blik en zakken voor al het andere. Ze liken nooit uw nieuwe bericht, kijken nooit een Reel af en stellen nooit een vraag in de reacties.",
                    "Hoge kwaliteit, in de enige betekenis die telt, is een mens die dat soort dingen zou kunnen doen. Profielfoto's en bio's zijn opsmuk; interactie is de echte test.",
                ],
            },
            {
                "h2": "Activiteit komt met de volgers mee",
                "p": [
                    "Omdat onze volgers mensen zijn, komt de activiteit met ze mee, van dezelfde accounts. Met {pick_name} brengt een typische maand {pick_audience} nieuwe volgers, samen met {pick_likes} likes en {pick_comments} reacties.",
                ],
            },
            {
                "h2": "Zo controleert u of volgers actief zijn",
                "ul": [
                    "Vergelijk likes met volgers op uw laatste berichten: echte groei beweegt allebei.",
                    "Lees de reacties: echte gaan over het bericht, botreacties passen onder alles.",
                    "Open een handvol profielen van nieuwe volgers: die van echte mensen zijn rommelig en persoonlijk.",
                    "Volg het totaal een paar weken: actieve volgers verdwijnen niet in golven.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "Een creator vergelijkt likes en reacties van recente Instagramberichten"},
            },
        ],
        "faqs": [
            ("Wat maakt een volger actief?", "Een mens die uw berichten ziet en soms reageert: een like, een reactie, een bekeken Reel, een gedeeld bericht. Niemand reageert op elk bericht, en dat is normaal."),
            ("Gaan mijn nieuwe volgers mijn berichten liken?", "Velen wel. Likes komen van dezelfde mensen die volgen, en met {pick_name} komen ze doorgaans uit op {pick_likes} per maand. Mensen liken wat ze leuk vinden, dus uw beste berichten krijgen er het meest."),
            ("Zijn dit volgers van goede kwaliteit?", "Het zijn mensen die besloten u te volgen, uit de plek die u opgaf. We beoordelen volgers niet op hoe verzorgd hun profiel eruitziet; wat telt, is dat er achter elk account iemand zit."),
            ("Zien de volgers er echt uit?", "Ze zijn echt, dus ze zien eruit als gewone Instagramgebruikers: eigen foto's, eigen vrienden, eigen gewoontes. Sommige profielen zijn druk, andere stil, zoals in elk publiek."),
            ("Is Growsterr een echte website of een wederverkoper?", "We zijn een groeibureau, onderdeel van Sterr Agency (Sterr Technologies OÜ, Tallinn, Estland), en achter elke campagne zit een team. We brengen mensen naar uw profiel; we verkopen geen volgersvoorraad door."),
        ],
    },
    {
        "service": "followers",
        "modifier": "safe",
        "slug": "instagram/volgers/veilig",
        "label": "Veilig en betrouwbaar Instagram-volgers",
        "title": "Instagram-volgers kopen bij een betrouwbare site | Growsterr",
        "description": "Op zoek naar een betrouwbare site om Instagram-volgers te kopen? Wie we zijn, hoe u betaalt, waar we nooit om vragen en wat u bij elke groeidienst controleert.",
        "h1": ("Veilig Instagram-volgers kopen: ", "zo herkent u een betrouwbare site."),
        "intro": "Voordat u Instagram-volgers koopt bij een website die zich betrouwbaar noemt, is het redelijk om te vragen wie erachter zit en wat er mis kan gaan. Hier is onze kant, zonder omwegen: wie we zijn, hoe betalen werkt, wat we met uw account doen (niets) en welke controles we bij elke groeidienst zouden doen, ook bij ons.",
        "hero": {"image": "instagram-hub", "alt": "Een Instagram-creator bekijkt de gegevens van een groeidienst voordat ze zich aanmeldt"},
        "sections": [
            {
                "h2": "Aan wie u betaalt",
                "p": [
                    "Growsterr is een product van Sterr Agency, onderdeel van Sterr Technologies OÜ, een bedrijf ingeschreven in Tallinn, Estland, met hoofdkantoor in Turkije. U betaalt met uw kaart via de checkout van Stripe, of met Apple Pay of Google Pay als uw apparaat dat ondersteunt. Uw kaartgegevens gaan naar Stripe, niet naar ons.",
                    "Het is een maandabonnement. U kunt het zelf opzeggen wanneer u wilt, en de campagne loopt door tot het einde van de betaalde maand.",
                ],
            },
            {
                "h2": "Wat we met uw account doen: niets",
                "p": [
                    "We loggen nooit in, posten nooit, volgen nooit iemand in uw naam en raken geen enkele instelling aan. De campagne speelt zich buiten uw account af: mensen zien uw profiel in ons partnernetwerk en bezoeken het zoals ze elk aanbevolen profiel zouden bezoeken.",
                ],
            },
            {
                "h2": "Vijf controles voor elke groeidienst",
                "ul": [
                    "Vraagt de dienst om uw wachtwoord? Een betrouwbare dienst heeft het nooit nodig.",
                    "Belooft hij duizenden volgers in een paar minuten? Die snelheid komt alleen van bots.",
                    "Zijn de aantallen bereiken of beloftes? Mensen laten zich niet vooraf tellen.",
                    "Kunt u zelf opzeggen, zonder iemand te hoeven mailen?",
                    "Staan er een bedrijfsnaam en een land achter de website?",
                ],
            },
        ],
        "faqs": [
            ("Is Growsterr betrouwbaar?", "Ja. We zijn een ingeschreven bedrijf, betalingen lopen uitsluitend via Stripe, en elke campagne wordt door een team uitgevoerd en in uw dashboard gemeten. U kunt op elk moment stoppen vanuit uw account."),
            ("Is het veilig voor mijn Instagram-account?", "Wij kunnen niet namens Instagram spreken, en niemand die eerlijk is kan beloven hoe het een account behandelt. Wel kunnen we zeggen dat we niets doen wat accounts in gevaar brengt: niet inloggen, geen bots, geen volgerspieken."),
            ("Wat hebben jullie van mij nodig?", "Uw Instagram-gebruikersnaam, waar uw nieuwe volgers vandaan moeten komen en een openbaar profiel. Dat is de hele lijst."),
            ("Kan ik de cijfers die jullie tonen vertrouwen?", "Ze zijn gemeten, niet geschat: uw dashboard toont dag voor dag de bezoeken die onze campagne bracht en de nieuwe volgers daaronder. Vóór uw bestelling noemen we typische bereiken, nooit beloftes, omdat mensen zelf beslissen."),
            ("Wordt er na het opzeggen nog iets afgeschreven?", "Nee. Opzeggen stopt de verlenging van het abonnement. U houdt de maand waarvoor u hebt betaald, en daarna wordt er niets meer afgeschreven."),
        ],
    },
    {
        "service": "followers",
        "modifier": "targeted",
        "slug": "instagram/volgers/lokaal",
        "label": "Lokale Instagram-volgers uit uw regio",
        "title": "Lokale Instagram-volgers kopen, uit uw eigen regio | Growsterr",
        "description": "Lokale Instagram-volgers kopen uit de stad, regio of het land dat u kiest: echte mensen die wonen waar uw klanten wonen, elke dag van de maand.",
        "h1": ("Lokale Instagram-volgers kopen ", "uit de plek die u kiest."),
        "intro": "Een café in Utrecht heeft weinig aan volgers aan de andere kant van de wereld. Wie lokale Instagram-volgers koopt, doet dat juist om de plek, dus daar vragen we eerst naar: uit welke stad, regio of welk land moeten uw nieuwe volgers komen? Daarna richten we uw campagne op de mensen die daar wonen.",
        "hero": {"image": "instagram-followers", "alt": "Nieuwe volgers uit dezelfde stad verschijnen op het Instagramprofiel van een lokaal bedrijf"},
        "sections": [
            {
                "h2": "Waarom lokaal meer telt dan het totaal",
                "p": [
                    "Voor een winkel, een studio, een restaurant of een creator die mensen in het echt ontmoet, is één volger die langs kan komen meer waard dan een paar die dat niet kunnen. Lokale volgers lopen binnen, vertellen het een vriend en herkennen de straat waar u filmde.",
                    "Het houdt uw publiek ook samenhangend. Delen de meeste volgers een plek en een taal, dan begrijpen meer van hen elk bericht.",
                ],
            },
            {
                "h2": "Zo werkt richten op een plek",
                "ul": [
                    "Bij uw bestelling noemt u een stad, een regio of een heel land.",
                    "We tonen uw profiel eerst aan mensen daar, elke dag van de maand.",
                    "Is het passende publiek daar klein, dan kunnen sommige volgers uit de omgeving komen, niet van een willekeurige plek.",
                    "Uw content doet de rest: mensen volgen als uw berichten hen aanspreken.",
                ],
            },
            {
                "h2": "Volgers uit het land waar uw klanten zitten",
                "p": [
                    "Volgers uit een land waar u nooit voor post, helpen u niet, waar dat land ook ligt. Zitten uw klanten in België, dan zoeken we mensen in België; zitten ze alleen in Amsterdam, zeg het, dan beginnen we daar.",
                ],
            },
        ],
        "faqs": [
            ("Kan ik een stad kiezen, niet alleen een land?", "Ja. Een stad, een regio of een heel land kan allemaal. Een stad geeft het meest afgebakende publiek; een regio of land geeft de campagne meer mensen om te bereiken."),
            ("Kan ik volgers uit India of een ander land waar ik niet actief ben vermijden?", "Ja. U kiest waar uw volgers vandaan komen, en daar richten we ons op. Er is niets mis met volgers uit welk land ook; de vraag is of ze uw publiek zijn. Zitten uw klanten in Nederland, dan zoeken we mensen in Nederland."),
            ("Komt elke volger uit mijn stad?", "We tonen uw profiel daar eerst. Is het goed passende publiek in de omgeving groter, dan kunnen sommige volgers daarvandaan komen. Zie het dus als gericht op uw stad, niet als afgezet rond uw stad."),
            ("Kost lokale targeting extra?", "Nee. Elk pakket heeft het, vanaf {starter_name} voor {starter_price} per maand."),
            ("Kan ik richten op leeftijd of interesses?", "We richten alleen op plek. Binnen die plek bepaalt uw content wie volgt, want mensen volgen wat hen interesseert."),
            ("Past lokale targeting bij een onlinebedrijf?", "Ja, als uw publiek ergens in het bijzonder woont: een taalgebied, een land, een markt waar u net instapt. Zitten uw kopers verspreid over een heel land, noem dan dat land."),
        ],
    },
    {
        "service": "followers",
        "modifier": "viral",
        "slug": "instagram/volgers/viraal",
        "label": "Instagram-volgers om viraal te gaan",
        "title": "Virale Instagram-volgers? Dit helpt echt | Growsterr",
        "description": "Instagram-volgers kopen om viraal te gaan? Viraal kan niemand beloven. Echte volgers geven elk bericht meer mensen die het kunnen delen, maand na maand.",
        "h1": ("Instagram-volgers kopen om viraal te gaan? ", "Laat de mensen groeien die delen."),
        "intro": "Niemand kan u een viraal bericht verkopen, wat er ook op een pagina staat. Wat een bericht laat reizen, zijn mensen: ze kijken, sturen het door naar een vriend, slaan het op, en Instagram toont het aan meer mensen zoals zij. Is viraal gaan de reden om Instagram-volgers te kopen, koop dan het deel dat kan helpen: meer echte mensen die uw volgende bericht als eersten zien.",
        "hero": {"image": "instagram-followers-1000", "alt": "De volgerslijn van een creator die na een populaire Reel omhoogspringt en daarna stabiel blijft"},
        "sections": [
            {
                "h2": "Waarom een groot getal een bericht niet laat reizen",
                "p": [
                    "Een bericht reist als de mensen die het als eersten zien erop reageren. Duizenden volgers die nooit reageren, geven het een slechtere start dan een paar honderd die dat wel doen, omdat Instagram dan een bericht ziet dat door het eerste publiek werd genegeerd.",
                ],
            },
            {
                "h2": "Wat echte volgers een viraal moment geven",
                "ul": [
                    "Meer eerste kijkers voor elk bericht: de mensen die bepalen of het verder reist.",
                    "Gedeelde en opgeslagen berichten, en die kunnen alleen mensen geven.",
                    "Een profiel dat het volgen waard is als een bericht wel aanslaat, zodat het moment iets achterlaat.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Mensen sturen het Instagrambericht van een creator door naar vrienden in hun berichten"},
            },
            {
                "h2": "De eerlijke kansen",
                "p": [
                    "De meeste berichten gaan niet viraal, die van ons niet en die van anderen ook niet. Gestage groei maakt de kans groter dat berichten die kunnen aanslaan dat ook doen, en maakt de berichten die niet aanslaan toch de moeite waard. Dat is wat we bieden: geen belofte van een moment, wel een betere startpositie voor elk bericht.",
                ],
            },
        ],
        "faqs": [
            ("Kunnen jullie mijn bericht viraal laten gaan?", "Nee, en wees voorzichtig met iedereen die zegt dat wel te kunnen. Viraal gaan hangt af van het bericht, de timing en de keuzes van duizenden mensen. Wat wij kunnen doen, is dagelijks nieuwe, echte kijkers naar uw profiel brengen, en dat geeft elk bericht een betere start."),
            ("Leveren virale berichten volgers op?", "Vaak wel, als het profiel achter het bericht mensen een reden geeft om te blijven. Daarom laten we het profiel groeien in plaats van één bericht: slaat er iets aan, dan vinden nieuwkomers een actief publiek en een stevige basis aan werk."),
            ("Helpt volgers kopen het algoritme?", "Gekochte bots werken daar tegen u, omdat elk bericht er dan genegeerd uitziet. Echte volgers die reageren, helpen elk bericht beter te starten. Geen van beide is een knop die u kunt omzetten."),
            ("Welk pakket past bij een bericht waarvan ik denk dat het kan aanslaan?", "{rising_name} of {pro_name}. Met allebei wijst u de berichten aan die meer ogen moeten krijgen, zodat meer echte mensen het bericht zien waar u in gelooft. {pro_name} geeft daarbij voorrang bij de plaatsing."),
            ("Hoe snel merk ik verschil?", "Uw campagne start snel en nieuwe volgers komen vanaf de eerste dagen. Of een bericht aanslaat, staat nooit op een planning; uw groei wel."),
        ],
    },
    # --- Likes ----------------------------------------------------------------------------
    {
        "service": "likes",
        "slug": "instagram/likes",
        "label": "Instagram-likes",
        "title": "Instagram-likes op uw berichten, van echte mensen | Growsterr",
        "description": "Instagram-likes van mensen die uw bericht zagen en het leuk vonden, in elk maandpakket: doorgaans {starter_likes} per maand met {starter_name}.",
        "h1": ("Instagram-likes ", "van mensen die het bericht leuk vonden."),
        "intro": "Wilt u Instagram-likes kopen voor uw berichten? Bij ons worden ze nooit los verkocht. Elk pakket stuurt echte mensen naar uw profiel, en die liken de berichten die ze leuk vinden: {starter_name} brengt doorgaans {starter_likes} likes per maand, {pick_name} {pick_likes}, samen met nieuwe volgers en reacties.",
        "hero": {"image": "instagram-hub", "alt": "Likes van echte mensen verzamelen zich op een raster van Instagramberichten"},
        "sections": [
            {
                "h2": "Een like is pas het begin",
                "p": [
                    "Op Instagram is een like vaak het eerste van meerdere dingen die iemand doet: hij opent uw profiel, bekijkt nog een paar berichten, volgt u en komt volgende week terug. Los gekochte likes houden op bij stap één, en een bericht met veel likes en verder niets eromheen leest precies zo.",
                    "Onze likes komen van mensen die die weg afleggen. Daarom komen ze samen met volgers en reacties, en niet in hun eentje.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Iemand liket een Instagrambericht en opent daarna het profiel van de creator"},
            },
            {
                "h2": "Likes op de berichten die u kiest",
                "p": [
                    "Met {starter_name} komen likes waar mensen ze het liefst geven, meestal op uw nieuwste berichten. Met {rising_name} en {pro_name} kiest u zelf welke berichten de aandacht krijgen, handig bij een lancering, een samenwerking of een bericht dat u gezien wilt hebben.",
                ],
            },
            {
                "h2": "Waar u in 2026 online Instagram-likes koopt",
                "ul": [
                    "Geen app om te installeren en geen login om te delen: een site die een van beide wil, vraagt om de verkeerde toegang.",
                    "Likes die samen met views en volgers komen, niet ervoor uit.",
                    "Typische bereiken in plaats van exacte aantallen, omdat mensen beslissen.",
                    "Een bedrijf dat u kunt benoemen en een checkout die u herkent: bij ons Sterr Technologies OÜ, met kaartbetalingen via Stripe.",
                ],
            },
        ],
        "faqs": [
            ("Kan ik likes kopen voor één bericht?", "Niet als losse bestelling. Likes zitten in een maandpakket, van mensen die uw profiel ontdekken. Met {rising_name} of {pro_name} kunt u die aandacht richten op de berichten die u kiest."),
            ("Is er een app voor Instagram-likes?", "Wij hebben er geen, en u hebt er ook geen nodig. U bestelt op de website, betaalt via Stripe en volgt uw campagne vanuit uw account op elk apparaat. Uw Instagram-login hebben we nooit nodig."),
            ("Hoeveel likes brengt elk pakket?", "Doorgaans {starter_likes} per maand met {starter_name}, {rising_likes} met {rising_name} en {pro_likes} met {pro_name}. Bereiken, geen vaste aantallen: elke like is de keuze van een mens."),
            ("Wanneer beginnen de likes?", "Zodra uw campagne loopt en de eerste mensen uw profiel bereiken, meestal in de eerste dagen. Ze blijven de hele maand komen, nooit in één golf."),
            ("Doen likes er nog toe nu aantallen verborgen kunnen worden?", "Op Instagram kunt u likeaantallen verbergen, dus het getal op het scherm telt minder dan vroeger. Wat nog steeds telt, is dat mensen iets met uw berichten doen, en dat is wat echte likes laten zien."),
        ],
    },
    {
        "service": "likes",
        "modifier": "comment-likes",
        "slug": "instagram/likes/reactie-likes",
        "label": "Likes op Instagram-reacties",
        "title": "Likes op Instagram-reacties kopen? Dit werkt wel | Growsterr",
        "description": "Likes op Instagram-reacties kopen? Die verkopen we niet. Mensen die uw berichten bereiken, lezen de reacties en liken de antwoorden waar ze het mee eens zijn.",
        "h1": ("Likes op Instagram-reacties ", "komen van mensen die meelezen."),
        "intro": "Mensen kopen likes op Instagram-reacties om twee redenen: om een reactie omhoog te duwen onder het bericht van iemand anders, of om hun eigen reactiesectie drukker te laten lijken. Wij verkopen geen van beide. We brengen echte mensen naar uw profiel, en wie uw reacties leest, kan uit zichzelf de antwoorden liken waar hij het mee eens is.",
        "hero": {"image": "instagram-real-people", "alt": "Een drukke reactiesectie onder een Instagrambericht, met likes op de beste antwoorden"},
        "sections": [
            {
                "h2": "Reacties onder berichten van anderen",
                "p": [
                    "Een veelgelikete reactie bovenaan het bericht van een groot account kan bezoekers uw kant op sturen, en daarom zoeken mensen naar reactie-likes. Wij voeren geen campagnes op berichten van anderen. Ons werk gebeurt op uw eigen profiel: we tonen het aan echte mensen, en zij beslissen wat ze daar doen.",
                ],
            },
            {
                "h2": "Reactie-likes onder uw eigen berichten",
                "p": [
                    "Onder uw berichten ontstaan reactie-likes vanzelf zodra er een gesprek is. Mensen die via uw campagne binnenkomen, lezen de reacties, beantwoorden er een paar en liken de reacties waar ze het mee eens zijn, de uwe ook. Die likes tellen of voorspellen we niet, want niemand kan voorspellen welk antwoord iemand gaat liken.",
                    "Wat we wel tellen: met {pick_name} brengt een maand doorgaans {pick_likes} likes op uw berichten en {pick_comments} reacties.",
                ],
            },
            {
                "h2": "Drie manieren om meer likes op uw antwoorden te krijgen",
                "ul": [
                    "Beantwoord de eerste reacties snel, terwijl mensen nog bij het bericht zijn.",
                    "Antwoord met iets wat het lezen waard is: een tip, een detail, een wedervraag.",
                    "Zet een reactie vast die het gesprek begint dat u wilt.",
                ],
            },
        ],
        "faqs": [
            ("Verkopen jullie likes op Instagram-reacties?", "Nee. Reactie-likes komen, net als elke andere like, alleen van mensen die ervoor kiezen ze te geven. Onze pakketten brengen die mensen naar uw berichten; wat ze in de reacties liken, bepalen ze zelf."),
            ("Kunnen jullie mijn reactie bovenaan het bericht van een ander account zetten?", "Nee. We laten alleen uw eigen profiel groeien, en we sturen geen likes naar reacties ergens anders."),
            ("Wordt mijn reactiesectie drukker?", "Meestal wel, omdat meer mensen uw berichten zien. Met {pick_name} komen er doorgaans {pick_comments} reacties per maand, en reacties trekken vaak zelf weer antwoorden en likes aan."),
            ("Tellen reactie-likes mee in de cijfers van het pakket?", "Nee. Onze typische bereiken tellen likes op uw berichten. Likes op afzonderlijke reacties komen daar bovenop, wanneer mensen ze geven."),
            ("Loggen jullie in op mijn account?", "Nee. Niemand van ons raakt uw account aan, en uw wachtwoord blijft altijd bij u. Alles wat er op uw berichten gebeurt, doen mensen, vanuit hun eigen account."),
        ],
    },
    {
        "service": "likes",
        "modifier": "gradual",
        "slug": "instagram/likes/geleidelijk",
        "label": "Langzame, geleidelijke Instagram-likes",
        "title": "Langzame Instagram-likes die over dagen groeien | Growsterr",
        "description": "Langzaam Instagram-likes kopen, zonder één piek? De onze komen van echte mensen die uw berichten in de loop van de maand vinden, zoals likes vanzelf groeien.",
        "h1": ("Langzame Instagram-likes, ", "want mensen nemen hun tijd."),
        "intro": "Zoekt u langzame Instagram-likes, dan weet u al dat honderden likes in twee minuten er verkeerd uitzien. Langzaam is goed, maar snelheid is maar de helft van het verhaal. Onze likes komen geleidelijk omdat ze van echte mensen komen die uw berichten in de loop van dagen en weken vinden, niet uit een wachtrij met een timer.",
        "hero": {"image": "instagram-followers-1000", "alt": "Likes op een Instagrambericht die over meerdere dagen rustig oplopen"},
        "sections": [
            {
                "h2": "Zo groeien likes op een echt bericht",
                "p": [
                    "Een bericht verzamelt likes in een curve: een eerste golf van mensen die het kort na het delen zien, daarna een lange staart als het via uw profiel, een hashtag of de berichten van een vriend wordt gevonden. Die staart kan weken duren.",
                    "Onze campagnes voegen mensen toe aan elk deel van die curve. Ze bezoeken uw profiel de hele maand door, scrollen door uw berichten en liken wat ze leuk vinden, dus ook oudere berichten krijgen likes, niet alleen het nieuwste.",
                ],
            },
            {
                "h2": "Waarom een timer niet hetzelfde is als tijd",
                "p": [
                    "Langzaam vrijgegeven likes van bots lossen het verkeerde probleem op. De piek is weg, maar de accounts achter de likes kijken, volgen en reageren nog steeds nooit. En likes zonder de views, volgers of reacties eromheen zien er in een rustig tempo net zo vreemd uit.",
                ],
            },
            {
                "h2": "Als langzaam niet is wat u zoekt",
                "p": [
                    "Hebt u binnen het uur een muur van likes op een bericht nodig, dan zijn wij de verkeerde dienst, en dat zeggen we liever nu. Wilt u dat elk bericht likes blijft verzamelen van mensen die erom geven, dan is dat precies waar we voor gebouwd zijn.",
                ],
            },
        ],
        "faqs": [
            ("Hoe langzaam komen de likes binnen?", "In het tempo waarin mensen uw berichten vinden: een deel in de eerste dagen van uw campagne, meer in de weken daarna. Er is geen timer en geen partij, dus geen twee dagen zien er hetzelfde uit."),
            ("Kan ik de snelheid van de likes kiezen?", "Nee, en dat is bewust. Het tempo komt van mensen die uw profiel bezoeken. Wat u wel kunt kiezen, met {rising_name} of {pro_name}, is welke berichten de aandacht krijgen."),
            ("Krijgen oudere berichten ook likes?", "Vaak wel. Mensen die uw profiel ontdekken, scrollen terug en liken wat ze leuk vinden, dus likes verspreiden zich over uw feed in plaats van zich op te stapelen op één bericht."),
            ("Zien langzame likes er natuurlijker uit?", "Langzaam ziet er alleen natuurlijk uit als er mensen achter zitten. Bij ons is dat zo, omdat het mensen zijn: bij elke like hoort iemand die misschien ook volgt of reageert."),
            ("Hoeveel likes komen er in een maand?", "Met {pick_name} doorgaans {pick_likes} in 30 dagen. Dat is een bereik, geen quotum, want mensen liken in hun eigen tempo."),
        ],
    },
    {
        "service": "likes",
        "modifier": "monthly",
        "slug": "instagram/likes/maandelijks",
        "label": "Maandelijkse Instagram-likes",
        "title": "Maandelijkse Instagram-likes, niet per bericht | Growsterr",
        "description": "Instagram-likes per maand in plaats van per bericht: één abonnement, echte mensen, de hele maand likes op uw berichten. Verlengt automatisch, altijd opzegbaar.",
        "h1": ("Automatische Instagram-likes per maand, ", "van mensen, niet van een script."),
        "intro": "Wilt u automatische Instagram-likes per maand, dan wilt u waarschijnlijk niet meer per bericht over likes nadenken. Dat is precies wat een pakket doet. U neemt één keer een abonnement, wij voeren elke dag uw campagne, en echte mensen liken de hele maand de berichten die ze leuk vinden: doorgaans {pick_likes} likes met {pick_name}. Het verlengt maandelijks tot u opzegt.",
        "hero": {"image": "instagram-creator-studio", "alt": "Een creator plant een maand Instagramberichten op een wandkalender"},
        "sections": [
            {
                "h2": "Automatisch, maar niet geautomatiseerd",
                "p": [
                    "Auto-likes betekent meestal software die elk nieuw bericht opmerkt en er binnen minuten een vast aantal likes op afvuurt. Dat is automatisch, en elk van die likes komt van een account dat niemand gebruikt.",
                    "Onze likes zijn automatisch in een andere zin: u hoeft per bericht niets te doen. De campagne blijft lopen, mensen blijven uw profiel ontdekken, en de likes die ze achterlaten zijn van henzelf.",
                ],
            },
            {
                "h2": "Wat een maandpakket verandert",
                "ul": [
                    "Eén prijs per maand, {pick_price} voor {pick_name}, in plaats van een bestelling per bericht.",
                    "Geen aantallen om in te stellen en geen timing om in te plannen.",
                    "Likes op nieuwe en oudere berichten, net hoe mensen ze vinden.",
                    "Een maand likes is een maand feedback: u ziet welke berichten mensen echt leuk vinden.",
                    "U kunt stoppen wanneer u wilt, zonder opzegtermijn.",
                ],
            },
        ],
        "faqs": [
            ("Krijgen nieuwe berichten automatisch likes?", "Mensen beslissen, dus er is geen vast aantal per bericht. Nieuwe berichten zijn meestal waar mensen beginnen, en met {rising_name} of {pro_name} kunt u aangeven welke berichten de aandacht moeten krijgen."),
            ("Wordt het abonnement automatisch verlengd?", "Ja. Stripe verlengt het elke maand met de betaalmethode die u koos. Opzeggen is in uw account zo gedaan, en de maand waarvoor u hebt betaald, loopt door tot het einde."),
            ("Hoeveel berichten heb ik nodig?", "Er is geen minimum, maar likes komen van mensen die door uw profiel bladeren, dus een paar recente berichten geven hun iets om te waarderen. Wie door de maand heen post, geeft elke nieuwe bezoeker meer om te liken."),
            ("Kan ik van maand tot maand van pakket wisselen?", "Ja. Begin met het pakket dat nu past en stap over wanneer uw berichten klaar zijn voor meer mensen."),
            ("Is dit hetzelfde als auto-likessoftware?", "Nee. Software die elk bericht op een timer liket, gebruikt accounts waar niemand achter zit. Onze likes komen van mensen die uw profiel bezochten en een bericht leuk vonden."),
        ],
    },
    {
        "service": "likes",
        "modifier": "no-drop",
        "slug": "instagram/likes/zonder-uitval",
        "label": "Instagram-likes die blijven",
        "title": "Instagram-likes die blijven staan | Growsterr",
        "description": "Instagram-likes kopen die blijven? Likes verdwijnen als de accounts erachter worden verwijderd. De onze komen van echte mensen, dus ze blijven gewoon staan.",
        "h1": ("Instagram-likes die blijven, ", "omdat een mens ze gaf."),
        "intro": "Likes verdwijnen vooral om één reden: de accounts die ze gaven, worden verwijderd. Wilt u Instagram-likes kopen die blijven, dan komt de blijvende soort van mensen. Die van ons dus ook: een like op uw bericht blijft staan, tenzij degene die hem gaf van gedachten verandert.",
        "hero": {"image": "instagram-hub", "alt": "Een Instagrambericht waarvan de likes weken na het delen stabiel blijven"},
        "sections": [
            {
                "h2": "Waar verdwijnende likes heen gaan",
                "p": [
                    "Een like hoort bij het account dat hem gaf. Als Instagram nep- of spamaccounts verwijdert, verdwijnt elke like die ze achterlieten mee, vaak weken na de bestelling. Een bericht kan in één nacht een groot deel van zijn likes kwijtraken, en wie eerder keek, ziet het gat.",
                ],
            },
            {
                "h2": "Waarom likes van mensen blijven",
                "p": [
                    "Het account van een mens wordt niet meegenomen bij een opschoning. Zijn like blijft op uw bericht staan zolang hij hem laat staan, en mensen gaan zelden terug om iets te ontliken wat ze leuk vonden.",
                    "Echte likes blijven bovendien komen. Oudere berichten krijgen nieuwe likes naarmate meer mensen uw profiel vinden, dus het aantal op een bericht kan nog lang na het delen stijgen.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Nieuwe bezoekers liken een ouder Instagrambericht weken nadat het online kwam"},
            },
        ],
        "faqs": [
            ("Gaan de likes ooit dalen?", "Niet zoals gekochte likes. Elke like komt van het eigen account van een mens, dus er verdwijnt er alleen een als die persoon ontliket of zijn account opheft. Dat is zeldzaam en gebeurt een voor een."),
            ("Is er een aanvulperiode?", "Er is geen aanvulperiode, omdat er geen daling te verwachten is. Aanvullingen lossen een probleem op dat wij niet veroorzaken."),
            ("Blijven likes op Reels ook staan?", "Ja. Een like blijft op elk bericht staan, foto, carrousel of Reel, zolang het account dat hem gaf er nog is."),
            ("Hoe zie ik of eerdere likes van bots kwamen?", "Let op plotselinge dalingen na een opschoning, veel meer likes dan views en likers zonder eigen berichten. Likes van mensen vertonen daar zelden iets van."),
            ("Hoeveel likes brengt een pakket?", "{pick_name} brengt doorgaans {pick_likes} per maand, verspreid over de berichten die mensen leuk vinden. Ze blijven staan, en de likes van volgende maand komen erbij."),
        ],
    },
    {
        "service": "likes",
        "modifier": "organic",
        "slug": "instagram/likes/organisch",
        "label": "Organische Instagram-likes",
        "title": "Organische Instagram-likes van mensen die u vonden | Growsterr",
        "description": "Organische Instagram-likes kopen en eerlijke feedback krijgen: echte mensen zien uw berichten via onze campagnes en liken alleen wat ze echt leuk vinden.",
        "h1": ("Organische Instagram-likes, ", "en wat ze u vertellen."),
        "intro": "Wie organische Instagram-likes koopt, krijgt iets wat gekochte likes niet kunnen geven: eerlijke feedback. Onze campagnes brengen uw berichten onder de aandacht van echte mensen, en die liken alleen wat ze leuk vinden. Sommige berichten krijgen er veel meer dan andere, en dat verschil vertelt u wat uw publiek wil.",
        "hero": {"image": "instagram-real-people", "alt": "Mensen reageren verschillend op een rij Instagramberichten en liken sommige meer dan andere"},
        "sections": [
            {
                "h2": "Ongelijke likes zijn een goed teken",
                "p": [
                    "Gekochte likes zijn verdacht gelijk: elk bericht krijgt ongeveer hetzelfde aantal, wat het ook is. Organische likes verschillen. Een sterke Reel loopt uit, een rustige foto blijft achter, en het patroon lijkt op een publiek met een mening, omdat het er een is.",
                ],
            },
            {
                "h2": "Uw likes gebruiken om beter te posten",
                "ul": [
                    "Vergelijk uw drie beste berichten van de maand: wat hebben ze gemeen?",
                    "Kijk welk formaat mensen het leukst vinden: Reels, carrousels of foto's.",
                    "Post meer van wat werkt en kijk of de likes volgen.",
                    "Geef met {rising_name} of {pro_name} extra aandacht aan een bericht waarmee u een nieuw idee test.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "Een creator sorteert de Instagramberichten van vorige maand op aantal likes"},
            },
            {
                "h2": "Zo bereiken organische likes uw berichten",
                "p": [
                    "We tonen uw profiel aan mensen in ons partnernetwerk, in de stad, regio of het land dat u kiest. Ze kijken rond, volgen als ze willen en liken de berichten die hen raken. Niemand wordt gevraagd iets te liken.",
                ],
            },
        ],
        "faqs": [
            ("Maakt betalen voor bereik de likes minder organisch?", "Nee. Betalen om gezien te worden is hoe elke advertentie en elk gepromoot bericht werkt. De like zelf is nog steeds iemands eigen reactie op uw bericht."),
            ("Krijgt elk bericht likes?", "De meeste berichten die mensen leuk vinden wel, maar niet allemaal evenveel, en daar gaat het nu juist om. Uw beste berichten krijgen meestal de meeste."),
            ("Hoeveel organische likes kan ik verwachten?", "Een typische maand met {pick_name} brengt {pick_likes}. Het totaal is een bereik; hoe het zich over berichten verdeelt, bepalen de mensen die ze zien."),
            ("Komen organische likes samen met volgers?", "Ja. De mensen die uw berichten liken, volgen u vaak ook: doorgaans {pick_audience} nieuwe volgers per maand met {pick_name}, en sommigen laten een reactie achter."),
            ("Waarom is dat beter dan een vast aantal per bericht?", "Omdat een vast aantal u niets vertelt. Organische likes stijgen en dalen met elk bericht, dus ze laten zien wat aanslaat en wat niet."),
        ],
    },
    {
        "service": "likes",
        "modifier": "private-account",
        "slug": "instagram/likes/prive-account",
        "label": "Instagram-likes op een privéaccount",
        "title": "Instagram-likes kopen voor een privéaccount? | Growsterr",
        "description": "Kunt u Instagram-likes kopen voor een privéaccount? Alleen goedgekeurde volgers zien de berichten, dus niemand nieuw kan ze liken. Dit werkt wel.",
        "h1": ("Likes op een privé Instagram-account ", "kunnen alleen van volgers komen."),
        "intro": "Voordat u Instagram-likes koopt voor een privéaccount, moet u de grens kennen: op een privéprofiel zien alleen goedgekeurde volgers uw berichten, dus alleen zij kunnen ze liken. Iedereen die een campagne naar uw profiel brengt, stuit op een slotje. Zolang uw campagne loopt, moet het profiel dus openbaar zijn, en er zijn goede manieren om privé te blijven waar het ertoe doet.",
        "hero": {"image": "instagram-hub", "alt": "Een Instagrambericht dat alleen goedgekeurde volgers kunnen zien en liken"},
        "sections": [
            {
                "h2": "Wie een bericht op een privéaccount kan liken",
                "p": [
                    "Alleen de mensen die u hebt goedgekeurd. Alle anderen zien uw naam, bio en volgersaantal, maar geen enkel bericht, dus er valt voor hen niets te liken. Een dienst die daar likes belooft, moet zijn accounts eerst als uw volgers laten goedkeuren, door u of door iemand die als u is ingelogd.",
                ],
            },
            {
                "h2": "Privé blijven, op een praktische manier",
                "ul": [
                    "Gebruik een tweede, openbaar account voor uw werk en houd uw persoonlijke account privé.",
                    "Verberg het likeaantal op elk bericht waarvan u het getal liever niet laat zien.",
                    "Zet reacties uit op berichten die u wilt delen zonder gesprek eronder.",
                ],
            },
            {
                "h2": "Wat er verandert als het profiel openbaar is",
                "p": [
                    "Mensen kunnen uw berichten zien en de berichten liken die ze leuk vinden; met {pick_name} zijn dat doorgaans {pick_likes} likes per maand, samen met nieuwe volgers en reacties. U bepaalt nog altijd zelf wat u post en met wie u praat.",
                ],
            },
        ],
        "faqs": [
            ("Kunnen mensen die mij niet volgen berichten op een privéaccount liken?", "Nee. Instagram toont de berichten van een privéaccount alleen aan goedgekeurde volgers, dus verder kan niemand ze liken."),
            ("Moet ik na de campagne openbaar blijven?", "Nee, dat kiest u zelf, en likes die al op uw berichten staan, blijven. Zolang het account privé is, kunnen nieuwe mensen uw berichten echter niet zien, dus een lopende campagne kan u dan geen likes brengen."),
            ("Kan ik in plaats daarvan een apart openbaar account laten groeien?", "Ja. Eén openbaar account voor uw werk en één privéaccount voor vrienden werkt goed. Wij laten dan het openbare account groeien."),
            ("Hebben jullie toegang nodig om verzoeken goed te keuren?", "Nee. Uw wachtwoord blijft bij u, en we loggen nooit in op uw account. Op een openbaar profiel valt er niets goed te keuren: mensen volgen en liken zonder verzoek."),
            ("Kan ik mijn likeaantallen verbergen en toch groeien?", "Ja. Het aantal verbergen verandert alleen wat bezoekers op dat bericht zien. Mensen kunnen het nog steeds liken, en u ziet het getal zelf gewoon."),
        ],
    },
    {
        "service": "likes",
        "modifier": "real",
        "slug": "instagram/likes/echt",
        "label": "Echte Instagram-likes",
        "title": "Echte Instagram-likes kopen: mensen, geen bots | Growsterr",
        "description": "Echte Instagram-likes van mensen met hun eigen account, nooit van bots. Ze komen samen met volgers en reacties van dezelfde mensen, in elk pakket.",
        "h1": ("Echte Instagram-likes, ", "elk van iemand die het meende."),
        "intro": "Wilt u echte Instagram-likes kopen? Een echte like komt van iemand die naar uw bericht keek en het leuk vond. Dat is de enige soort die wij brengen. Elk pakket toont uw profiel aan mensen, en hun likes staan naast volgers, reacties en views van dezelfde accounts, dus uw engagement ziet er realistisch uit omdat het dat is.",
        "hero": {"image": "instagram-real-people", "alt": "Verschillende mensen, elk met een eigen profiel, liken hetzelfde Instagrambericht"},
        "sections": [
            {
                "h2": "Premium likes, kwaliteitslikes en echte likes",
                "p": [
                    "Veel verkopers delen likes op in niveaus: goedkope van lege accounts, premium of hoogwaardige van accounts met foto's en berichten. Beide niveaus zijn hetzelfde in een ander jasje: accounts die op commando liken. Een betere vermomming maakt een like niet echt.",
                    "Kwaliteit betekent bij een like maar één ding: een mens koos ervoor hem te geven. De rest is verpakking.",
                ],
            },
            {
                "h2": "Echte likes doen meer dan alleen liken",
                "p": [
                    "Een echte like komt van iemand die misschien ook volgt, reageert of uw volgende Reel bekijkt. Daarom tillen echte likes de rest van uw cijfers mee in plaats van er los naast te staan: ze zijn één stap in wat een mens doet, niet de hele transactie.",
                ],
            },
            {
                "h2": "Zo herkent u likes die alleen echt lijken",
                "ul": [
                    "Likes schieten omhoog terwijl views, volgers en reacties gelijk blijven.",
                    "De profielen van de likers hebben stockfoto's, weinig berichten en duizenden gevolgde accounts.",
                    "Er komen er honderden binnen in de minuten na het posten, en daarna niets.",
                    "Het aantal zakt een paar weken later.",
                ],
            },
        ],
        "faqs": [
            ("Komen jullie Instagram-likes van echte accounts?", "Ja. Elke like komt van het eigen account van een mens: iemand die uw profiel via onze campagne ontdekte en het bericht leuk vond. Geen bots en geen accountfarms."),
            ("Verkopen jullie premium likes?", "We verkopen likes niet in niveaus en niet los. Elke like die we brengen, komt van een mens, in een maandpakket; {starter_name}, het kleinste, brengt doorgaans {starter_likes} per maand."),
            ("Vergroten echte likes mijn bereik?", "Ze helpen zoals alleen echt engagement dat kan, omdat de mensen erachter ook kunnen volgen, reageren en delen. Waar een bericht terechtkomt, hangt nog altijd af van het bericht zelf, dus bereik beloven we nooit."),
            ("Waarom zien sommige gekochte likes er echt uit?", "Omdat ze daarvoor gemaakt zijn: profielfoto's, een paar berichten, geloofwaardige namen. Kijk naar wat er omheen gebeurt. Likes van mensen komen met views en volgers; vermomde likes komen alleen."),
            ("Kan ik echte likes krijgen zonder nieuwe volgers?", "Nee. Likes komen als onderdeel van het pakket, van mensen die uw profiel vinden, en velen van hen volgen u ook. Dat houdt likes realistisch."),
        ],
    },
    {
        "service": "likes",
        "modifier": "reels",
        "slug": "instagram/likes/reels",
        "label": "Likes op Instagram Reels",
        "title": "Instagram-likes voor Reels kopen, van echte kijkers | Growsterr",
        "description": "Instagram-likes voor Reels, eerlijk geregeld: mensen bekijken uw video's en liken de video's die ze goed vinden, dus achter elke like zit een view.",
        "h1": ("Likes op uw Reels, ", "van mensen die echt keken."),
        "intro": "Voordat u Instagram-likes voor Reels koopt, is het goed om te weten wat een like waard is op een Reel die niemand bekeek: niet veel. Onze likes op Reels komen van echte mensen die uw profiel ontdekten, uw video's bekeken en de video's liketen die hen vasthielden, samen met nieuwe volgers en reacties.",
        "hero": {"image": "instagram-creator-studio", "alt": "Een creator bewerkt een Instagram Reel op een telefoon aan een bureau"},
        "sections": [
            {
                "h2": "Bij een Reel komt kijken vóór liken",
                "p": [
                    "Reels leven van wat kijkers doen: kijken ze tot het eind, kijken ze nog eens, delen ze, volgen ze? Een like is daar één signaal van, en het zegt het meest als het na een echte kijkbeurt komt.",
                    "Los gekochte videolikes komen meestal zonder bijpassende weergaven. Een Reel met meer likes dan views valt op, en zegt niets goeds over hoe hij aan die likes kwam.",
                ],
            },
            {
                "h2": "Meer van uw Reels laten zien",
                "ul": [
                    "Mensen bladeren door uw profiel en bekijken de Reels die hen pakken, niet alleen de nieuwste.",
                    "Met {rising_name} en {pro_name} zet u een bepaalde Reel voor meer mensen neer.",
                    "Kijkers komen van de plek die u kiest, dus uw taal en verwijzingen komen aan.",
                ],
            },
            {
                "h2": "Laat de eerste seconden tellen",
                "p": [
                    "Wij kunnen mensen naar uw Reels brengen; ze vasthouden is de taak van de video. Een duidelijke haak in de eerste seconde of twee, ondertitels voor wie zonder geluid kijkt en een einde dat uitnodigt tot nog een keer kijken, helpen allemaal om van een view een like te maken.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Kijkers bekijken een Instagram Reel tot het eind en tikken op like"},
            },
        ],
        "faqs": [
            ("Kan ik likes op een bepaalde Reel richten?", "Ja, met {rising_name} of {pro_name}: u kiest welke berichten en Reels de aandacht krijgen, en mensen doen de rest. Met {starter_name} vinden kijkers zelf de Reels die ze leuk vinden."),
            ("Komen Reels-likes samen met views?", "Ja. Mensen kijken voordat ze liken, dus achter elke like zit een view. Views verkopen of tellen we niet apart, omdat elke view een mens is die ervoor kiest te kijken."),
            ("Komt mijn Reel hierdoor op Verkennen?", "Dat kan niemand beloven, en wij doen dat ook niet. Instagram bepaalt wat er op Verkennen en in de Reels-feed komt. Kijkers die kijken en reageren, geven een Reel een eerlijke start; gekochte likes zonder views geven hem een vreemde start."),
            ("Moet mijn account openbaar zijn?", "Ja, zolang uw campagne loopt. Mensen buiten uw volgers kunnen geen Reels bekijken op een privéaccount, dus liken kunnen ze ze ook niet."),
            ("Hoeveel likes krijgen mijn Reels?", "Met {pick_name} doorgaans {pick_likes} likes per maand, verdeeld over uw berichten en Reels. Hoe ze zich verdelen, hangt af van wat mensen het leukst vinden."),
        ],
    },
    {
        "service": "likes",
        "modifier": "safe",
        "slug": "instagram/likes/veilig",
        "label": "Betrouwbare Instagram-likes",
        "title": "Betrouwbare Instagram-likes: wat maakt ze legitiem? | Growsterr",
        "description": "Veilig Instagram-likes kopen? Een legitieme like komt van een mens die uw bericht zag. Zo herkent u ze, en zo brengen onze maandpakketten ze.",
        "h1": ("Betrouwbare Instagram-likes ", "beginnen bij een mens en een bericht."),
        "intro": "Wilt u Instagram-likes kopen die legitiem zijn? Een legitieme like heeft twee onderdelen: een echt mens, en een bericht dat hij echt zag. Alles wat we doen, is rond die twee gebouwd. We tonen uw profiel aan mensen, en wie uw berichten leuk vindt, liket ze. Zonder logins, zonder bots en zonder likes die los worden verkocht.",
        "hero": {"image": "instagram-hub", "alt": "Iemand scrolt door Instagram en stopt om een bericht te liken dat hij leuk vindt"},
        "sections": [
            {
                "h2": "Waarschuwingssignalen in elk likesaanbod",
                "ul": [
                    "Een prijs per duizend likes: mensen zijn niet per duizend te koop.",
                    "Levering in minuten, of een belofte van exacte aantallen.",
                    "Een vraag om uw wachtwoord, of inloggen via een app.",
                    "Likes die worden verkocht zonder views, volgers of reacties erbij.",
                ],
            },
            {
                "h2": "Waarom neplikes niet legitiem zijn, wie ze ook verkoopt",
                "p": [
                    "De regels van Instagram vragen mensen om likes niet kunstmatig te verzamelen, en likes van accounts die op commando liken, zijn precies dat. Hoe Instagram één bepaald account behandelt, kunnen we niet zeggen, en we gaan er ook niet naar raden. We brengen gewoon niets kunstmatigs naar uw account.",
                ],
            },
            {
                "h2": "Waar onze likes vandaan komen",
                "p": [
                    "Van de mensen die onze campagnes naar uw profiel brengen: gebruikers in ons partnernetwerk, op de plek die u kiest, elke dag van de maand. Ze liken wat ze leuk vinden, doorgaans {pick_likes} likes per maand met {pick_name}, en velen van hen volgen en reageren ook.",
                ],
            },
        ],
        "faqs": [
            ("Is het legitiem om Instagram-likes te kopen?", "Likes kopen van accounts die op commando liken, gaat in tegen de regels van Instagram over kunstmatig engagement. Wat wij verkopen, is iets anders: bereik bij echte mensen, die zelf beslissen of ze liken."),
            ("Kan ik mijn account kwijtraken door gekochte likes?", "Wij kunnen niet namens Instagram spreken, en wie een uitkomst belooft, gokt. Wat wij wel in de hand hebben: elke like die we brengen, komt van een mens, en we raken uw login nooit aan."),
            ("Hoe betaal ik?", "Met een kaart, Apple Pay of Google Pay, via de beveiligde checkout van Stripe. U betaalt per maand en de facturering stopt zodra u opzegt."),
            ("Vragen jullie om mijn Instagram-login?", "Nooit. We hebben uw gebruikersnaam nodig om de campagne te starten. Vraagt een likesdienst om uw wachtwoord, loop dan weg."),
            ("Waarom verkopen jullie geen likes per bericht?", "Omdat een vast aantal likes op een vast bericht alleen kan komen van accounts die op commando liken. Wij brengen mensen; likes zijn wat zij doen als ze een bericht leuk vinden."),
        ],
    },
    {
        "service": "likes",
        "modifier": "viral",
        "slug": "instagram/likes/viraal",
        "label": "Instagram-likes om viraal te gaan",
        "title": "Virale Instagram-likes: wat werkt er echt? | Growsterr",
        "description": "Instagram-likes kopen om viraal te gaan? Likes alleen laten een bericht niet reizen; mensen die kijken, delen en opslaan wel. Wat echte likes wel en niet doen.",
        "h1": ("Virale Instagram-likes ", "zijn een gevolg, geen startschot."),
        "intro": "Mensen kopen vaak Instagram-likes om een bericht viraal te laten gaan, in de hoop dat een groot getal Instagram, en iedereen, ervan overtuigt dat het meer aandacht verdient. Zo werkt het zelden. Likes van mensen die een bericht bekeken en goed vonden, zijn een teken van momentum; likes opgestapeld op een stil bericht zijn een teken van niets. Wij brengen de eerste soort, en het virale deel beloven we niet.",
        "hero": {"image": "instagram-followers-1000", "alt": "Likes, gedeelde en opgeslagen berichten stijgen samen op een Instagrambericht dat begint te reizen"},
        "sections": [
            {
                "h2": "Likes komen na de verspreiding, niet ervoor",
                "p": [
                    "Als een bericht aanslaat, zijn de likes het zichtbare spoor van duizenden mensen die het bekijken, doorsturen naar vrienden en opslaan voor later. Kopieer het spoor zonder de mensen, en u krijgt het getal zonder de beweging.",
                ],
            },
            {
                "h2": "Wat een bericht echt een kans geeft",
                "ul": [
                    "Een eerste publiek dat reageert: mensen die het bericht vroeg zien en het liken, erop reageren of het delen.",
                    "Een haak die mensen laat stoppen, en een reden om het naar iemand te sturen.",
                    "Posten waar uw publiek is, in hun taal, op het moment dat ze scrollen.",
                    "Focus: met {rising_name} of {pro_name} zien meer mensen het bericht waarvan u denkt dat het kan reizen.",
                ],
            },
            {
                "h2": "Wat we beloven, en wat niet",
                "p": [
                    "We beloven echte mensen, elke dag, en een dashboard met wat we hebben gemeten. We beloven geen miljoenen views, geen plek op Verkennen en geen bericht dat zich verspreidt. Wie dat wel belooft, verkoopt de schijn van een viraal bericht.",
                ],
            },
        ],
        "faqs": [
            ("Gaat mijn bericht viraal als ik likes koop?", "Niet vanzelf. Een likeaantal is het gevolg van de aandacht van mensen, en gekochte likes voegen het getal toe zonder de aandacht. Likes van mensen die keken, geven een bericht een eerlijke start, en meer kan niemand bieden."),
            ("Hoeveel likes heeft een viraal bericht nodig?", "Er is geen magisch getal. Een bericht met een bescheiden aantal kan reizen als de mensen die het zien het delen, en een bericht met een groot aantal kan blijven steken."),
            ("Sturen jullie likes in het eerste uur nadat ik post?", "We stemmen likes niet af op een bericht. Mensen komen de hele maand door en liken wat ze leuk vinden. Is één bericht belangrijker, dan kiest u met {rising_name} en {pro_name} welke berichten de aandacht krijgen."),
            ("Zijn delen en opslaan inbegrepen?", "Die tellen of verkopen we niet, maar ze gebeuren wel: de mensen die uw berichten liken, kunnen ze ook delen en opslaan, iets wat bots nooit doen."),
            ("Liken anderen sneller bij een hoog likeaantal?", "Mensen zien wel dat een bericht druk is. Maar een groot aantal zonder reacties of gedeelde berichten ziet er geënsceneerd uit voor precies de mensen die u wilt overtuigen."),
        ],
    },
]
