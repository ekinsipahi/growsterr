UPDATED = "2026-11-09"

# Italian YouTube intent pages: searches for things we don't sell (economici, istantanei, gratis,
# prova gratuita, pannelli). Each answers honestly, then leads to the monthly package. Mirrors
# en/youtube_intents.py variant by variant. Keys and placeholders: docs/CONTENT.md; angles:
# docs/keywords/WRITING.md.

PAGES = [
    # --- Iscritti -------------------------------------------------------------------------
    {
        "service": "subscribers",
        "modifier": "cheap",
        "slug": "youtube/iscritti/economici",
        "label": "Iscritti YouTube economici?",
        "plan": "starter",
        "title": "Comprare iscritti YouTube a 1 dollaro? Cosa costano | Growsterr",
        "description": "Gli iscritti YouTube da 1 dollaro non guardano mai. Per {starter_price} al mese, {starter_name} porta di solito {starter_audience} spettatori reali che si iscrivono.",
        "h1": ("Gli iscritti YouTube da 1 dollaro ", "non guardano mai nemmeno un video."),
        "intro": "Stai pensando di comprare iscritti YouTube a 1 dollaro? A quel prezzo ricevi account che non guarderanno, non metteranno like e non commenteranno mai, e YouTube rimuove di continuo gli account di spam dagli iscritti. Noi chiediamo di più e portiamo spettatori: {starter_audience} nuovi iscritti in un mese tipico con {starter_name}, a {starter_price}, ognuno una persona che ha trovato il tuo canale e ha deciso di iscriversi.",
        "hero": {"image": "youtube-subscribers", "alt": "Il numero di iscritti di un canale YouTube che cresce con spettatori reali"},
        "sections": [
            {
                "h2": "Il costo di un iscritto che non guarda mai",
                "p": [
                    "Su YouTube conta più cosa fanno gli iscritti che quanti sono. Un elenco pieno di account che non premono mai play fa sembrare ogni nuovo video meno interessante di quanto sia.",
                    "Quindi un iscritto economico non è economico. Lo paghi una volta in denaro e una seconda volta in visualizzazioni che non arrivano.",
                ],
            },
            {
                "h2": "Quanto costa un iscritto reale",
                "p": [
                    "Prendi {starter_name}: {starter_price} al mese, e di solito {starter_audience} iscritti che sono spettatori reali dalla zona che scegli. Per persona è questione di centesimi, e i loro like e commenti sono compresi nel prezzo.",
                ],
            },
            {
                "h2": "Un prezzo basso senza rischi",
                "ul": [
                    "Nessuna password e nessun accesso al tuo account Google: solo l'handle del tuo canale.",
                    "Addebito mensile con carta tramite Stripe, disdicibile dal tuo account.",
                    "Iscritti, like e commenti in un unico prezzo, dalle stesse persone.",
                ],
            },
        ],
        "faqs": [
            ("Quanto costano gli iscritti YouTube reali?", "I nostri pacchetti partono da {starter_price} al mese. {starter_name} porta di solito {starter_audience} nuovi iscritti; {rising_name}, a {rising_price}, ne porta {rising_audience}; {pro_name}, a {pro_price}, ne porta {pro_audience}."),
            ("Perché alcuni siti vendono iscritti a così poco?", "Perché vendono account, non spettatori. Creare o affittare account in serie costa pochissimo; trovare persone che vogliono guardare il tuo canale no."),
            ("C'è un'opzione molto economica per un canale piccolo?", "{starter_name} è pensato per canali nuovi e piccoli, ed è il nostro prezzo più basso."),
            ("Gli iscritti economici possono mettere nei guai il mio canale?", "Possono. Le norme di YouTube sull'engagement falso coprono gli iscritti comprati, e i canali che li usano rischiano la rimozione dei video o penalizzazioni."),
            ("Le visualizzazioni sono incluse nel prezzo?", "Sì. I tuoi nuovi iscritti guardano, mettono like e commentano di loro iniziativa, tutto dentro il pacchetto. Non diamo un numero alle visualizzazioni, perché ognuna è qualcuno che sceglie di premere play."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "fast",
        "slug": "youtube/iscritti/veloci",
        "label": "Iscritti YouTube veloci?",
        "title": "Iscritti YouTube veloci: reali, non istantanei | Growsterr",
        "description": "Iscritti YouTube reali, attivi e istantanei? Non tutti e tre. I nostri sono reali e attivi: la campagna parte in pochi giorni e arrivano ogni giorno.",
        "h1": ("Reali, attivi e istantanei? ", "Solo due di queste cose possono essere vere."),
        "intro": "Vuoi comprare iscritti YouTube veloci, reali, istantanei e attivi tutto insieme? Solo due di queste cose possono stare insieme. Gli iscritti istantanei non sono persone, e le persone reali non si iscrivono appena paghi. Noi portiamo in fretta iscritti reali e attivi: la campagna è attiva entro i primi giorni, e da lì {pick_name} aggiunge di solito {pick_audience} iscritti al mese, qualcuno ogni giorno.",
        "hero": {"image": "youtube-subscribers", "alt": "Nuovi iscritti si uniscono a un canale YouTube giorno dopo giorno"},
        "sections": [
            {
                "h2": "Perché su YouTube istantaneo significa falso",
                "p": [
                    "Una persona reale si iscrive dopo aver guardato qualcosa: un video, uno Short, un trailer del canale. Ci vogliono almeno minuti, e succede quando ne ha voglia. Gli iscritti che compaiono a centinaia subito dopo un pagamento hanno saltato la visione, il che ti dice che non erano persone.",
                ],
            },
            {
                "h2": "Quanto in fretta arrivano gli iscritti reali",
                "p": [
                    "La preparazione richiede i primi giorni dopo l'ordine. Da lì in poi, nuovi spettatori trovano il tuo canale ogni giorno, e chi apprezza ciò che guarda si iscrive. La dashboard mostra ogni giorno man mano che lo misuriamo, così vedi il ritmo fin dalla prima settimana.",
                ],
            },
            {
                "h2": "Una velocità che puoi sfruttare",
                "ul": [
                    "Carica video mentre la campagna è attiva, così i nuovi iscritti hanno qualcosa da guardare dopo.",
                    "Sistema la pagina del canale: un banner chiaro, un trailer e playlist in un ordine sensato.",
                    "Scegli {pro_name} per l'intervallo mensile più ampio: di solito {pro_audience} nuovi iscritti.",
                ],
            },
        ],
        "faqs": [
            ("Quanto in fretta salirà il mio numero di iscritti?", "Entro i primi giorni della campagna: pochi alla volta all'inizio, poi ogni giorno per tutto il mese."),
            ("Potete aggiungere 1.000 iscritti all'istante?", "No, nessuno può farlo con persone reali. Mille in un'ora significano mille account che non guarderanno mai, e sono proprio quelli che YouTube ripulisce."),
            ("I vostri iscritti sono attivi?", "Sono persone reali che si sono iscritte dopo aver visto il tuo canale, quindi sono attive come qualsiasi spettatore: guardano, mettono like e commentano quando un video le interessa."),
            ("Quale pacchetto è il più veloce?", "{pro_name} porta di più ogni mese: di solito {pro_audience} nuovi iscritti. {starter_name} e {rising_name} portano intervalli più piccoli, distribuiti allo stesso modo nel mese."),
            ("Una crescita veloce danneggerà il mio canale?", "Non a questo ritmo. Gli iscritti arrivano ogni giorno da spettatori reali, che è comunque il modo in cui i canali in crescita li guadagnano."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "free",
        "slug": "youtube/iscritti/gratis",
        "label": "Iscritti YouTube gratis?",
        "plan": "starter",
        "tool": "growth-calculator",
        "title": "Iscritti YouTube gratis? Ecco un piano migliore | Growsterr",
        "description": "Gli iscritti YouTube gratis arrivano da scambi sub-for-sub o da bot. Non li offriamo: il nostro calcolatore gratuito mostra quanto richiede una crescita reale.",
        "h1": ("Iscritti YouTube gratis? ", "Pianifica invece quelli reali."),
        "intro": "Cerchi iscritti YouTube gratis, o 1.000 per 5 dollari? Nessuna delle due cose porta persone che guardano: le offerte gratuite si basano su scambi sub-for-sub o su account bot. Non regaliamo iscritti. La parte gratuita di questa pagina è il calcolatore di crescita: inserisci dove si trova il tuo canale e dove vuoi portarlo, e stima i mesi che richiede di solito ogni pacchetto.",
        "hero": {"image": "youtube-channel", "alt": "Uno youtuber pianifica un obiettivo di iscritti per i prossimi mesi"},
        "sections": [
            {
                "h2": "Sub-for-sub e altri trucchi gratuiti",
                "ul": [
                    "Gruppi sub-for-sub: ti iscrivi a sconosciuti, loro ricambiano, e nessuno guarda nessuno.",
                    "Siti di iscritti gratis che ti chiedono di accedere con Google, poi usano il tuo account per iscriversi ad altri.",
                    "Piccoli blocchi gratuiti da account bot, offerti perché tu ne compri uno più grande.",
                ],
                "p": [
                    "Tutti riempiono il tuo numero di persone che non hanno alcun interesse per i tuoi video, il che è peggio che avere meno iscritti.",
                ],
            },
            {
                "h2": "A proposito di quei 1.000",
                "p": [
                    "Mille iscritti sono un traguardo per molti canali, spesso per via del Programma partner di YouTube. Gli iscritti comprati o scambiati non aggiungono tempo di visualizzazione, e YouTube li tratta come engagement falso. Nemmeno noi promettiamo la monetizzazione: portiamo spettatori reali, e il resto dipende dai tuoi video e da YouTube.",
                ],
            },
            {
                "h2": "Pianificalo con il calcolatore di crescita",
                "p": [
                    "Il calcolatore in alto è gratuito e funziona nel tuo browser. Inserisci il tuo numero di iscritti dove chiede i follower di oggi, e il tuo traguardo come obiettivo. Calcola quanti mesi richiede di solito ogni pacchetto, partendo dall'intervallo mensile tipico di ciascuno.",
                ],
            },
        ],
        "faqs": [
            ("Posso avere iscritti YouTube gratis?", "Non reali, e non da noi. Ogni iscritto che portiamo è uno spettatore raggiunto da una campagna a pagamento. La parte gratuita è il calcolatore qui, senza limiti a quante volte lo usi."),
            ("1.000 iscritti YouTube per 5 dollari sono reali?", "No. Nessuna campagna reale può trovare mille persone che vogliono il tuo canale per cinque dollari. A quel prezzo gli iscritti sono account, non spettatori."),
            ("Quanto ci vuole per arrivare a 1.000 iscritti reali?", "Dipende da dove parti. {starter_name} porta di solito {starter_audience} nuovi iscritti al mese; inserisci i tuoi numeri nel calcolatore qui sopra per vedere i mesi per il tuo canale."),
            ("Il sub-for-sub è contro le regole di YouTube?", "Sì. Le norme di YouTube sull'engagement falso coprono lo scambio di iscrizioni, quindi può mettere a rischio un canale. Porta anche iscritti che non guardano mai."),
            ("Da dove dovrebbe partire un canale piccolo?", "Da {starter_name}, a {starter_price} al mese, senza nessun contratto oltre il mese in corso."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "free-trial",
        "slug": "youtube/iscritti/prova-gratuita",
        "label": "Prova gratuita di iscritti YouTube?",
        "plan": "starter",
        "title": "Iscritti YouTube con una prova gratuita? | Growsterr",
        "description": "Qui non c'è una prova gratuita di iscritti YouTube: un campione di un giorno non dimostra niente. Il primo mese mostra spettatori reali e misurati.",
        "h1": ("Una prova gratuita di iscritti YouTube ", "non dimostrerebbe niente. Un mese sì."),
        "intro": "Se vuoi comprare iscritti YouTube dopo una prova gratuita, saremo diretti: non la offriamo. Una prova di 100 iscritti in un giorno dimostrerebbe solo che un venditore ha account da parte. Il tuo primo mese è il modo per giudicarci: {starter_name} a {starter_price}, spettatori reali che arrivano dai primi giorni, una dashboard di ciò che abbiamo misurato e nessun contratto oltre il mese.",
        "hero": {"image": "youtube-hub", "alt": "Le statistiche di un canale YouTube durante un primo mese di crescita reale"},
        "sections": [
            {
                "h2": "Cosa non può mostrarti una prova",
                "p": [
                    "La domanda non è se un numero può salire. È se persone reali guardano, mettono like e restano, e per vederlo servono settimane. Un campione di un giorno è un trucco di vendita, non un test.",
                ],
            },
            {
                "h2": "Come controllarci durante il mese",
                "ul": [
                    "Apri la dashboard ogni pochi giorni: visite dalla campagna e nuovi iscritti, così come li misuriamo.",
                    "Guarda le statistiche dei tuoi video: i nuovi spettatori stanno guardando?",
                    "Leggi i commenti: persone che scrivono dei tuoi video con parole loro.",
                    "Decidi prima della data di rinnovo; puoi disdire dal tuo account in qualsiasi momento.",
                ],
            },
        ],
        "faqs": [
            ("Avete una prova gratuita per YouTube?", "No. Non facciamo prove su nessuna piattaforma. Un mese è il pacchetto più breve, e puoi disdire prima che inizi il successivo."),
            ("Perché niente prova se altri siti la offrono?", "Ogni iscritto che portiamo arriva da una campagna reale che costa dal primo giorno. I venditori che possono permettersi campioni gratuiti di solito mandano account, non spettatori."),
            ("Cosa succede se disdico dopo un mese?", "Non viene addebitato altro, e il mese pagato arriva fino alla fine. Gli iscritti reali non vengono ritirati; restano finché non decidono di andarsene."),
            ("Vedrò risultati entro il primo mese?", "Vedrai il ritmo: nuovi iscritti che arrivano ogni giorno, di solito {starter_audience} nel mese con {starter_name}. Tipici, non fissi, perché ognuno è qualcuno che decide da sé."),
            ("Posso provare prima un pacchetto più piccolo?", "{starter_name} è il nostro pacchetto più piccolo e il punto di partenza naturale. Puoi salire più avanti se il tuo canale ha bisogno di più."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "smm-panel",
        "slug": "youtube/iscritti/pannello-smm",
        "label": "Iscritti YouTube da pannelli SMM?",
        "title": "Comprare iscritti YouTube su un pannello SMM? | Growsterr",
        "description": "I pannelli SMM vendono iscritti e visualizzazioni YouTube a migliaia, con ricariche perché calano. Noi siamo un'agenzia con spettatori reali.",
        "h1": ("Gli iscritti dei pannelli hanno il pulsante di ricarica. ", "I nostri non ne hanno bisogno."),
        "intro": "Prima di comprare iscritti o visualizzazioni YouTube su un pannello SMM, nota l'opzione di ricarica che i pannelli mettono spesso accanto: si aspettano che i numeri calino. I pannelli rivendono traffico di bot all'ingrosso. Noi lavoriamo invece come agenzia: persone del nostro team seguono la tua campagna, spettatori reali trovano il tuo canale e si iscrivono, e la dashboard riporta ciò che abbiamo misurato.",
        "hero": {"image": "youtube-channel", "alt": "Un creator controlla una dashboard di nuovi iscritti YouTube misurati"},
        "sections": [
            {
                "h2": "Iscritti e visualizzazioni a migliaia",
                "p": [
                    "Su un pannello, iscritti, visualizzazioni e ore di visualizzazione YouTube stanno in un unico elenco, con prezzi per mille e note su tempi di avvio e ricariche. Nessuno guarda il tuo canale. L'ordine entra in una coda, e gli account fanno ciò che dice la coda.",
                    "Le visualizzazioni dei pannelli funzionano allo stesso modo: riproduzioni senza nessuno che decida di guardare, il tipo che YouTube lavora per filtrare dal conteggio delle visualizzazioni.",
                ],
            },
            {
                "h2": "Cosa cambia con un'agenzia",
                "ul": [
                    "Persone invece di code: il tuo canale viene mostrato a spettatori reali ogni giorno.",
                    "Ogni iscritto, like, visualizzazione e commento risale a una persona.",
                    "Un team dietro la tua campagna, e un modo per raggiungerci quando hai domande.",
                    "Una dashboard di ciò che abbiamo misurato, non un contatore da rabboccare.",
                ],
            },
        ],
        "faqs": [
            ("Gli iscritti dei pannelli sono persone reali?", "No. I pannelli rivendono traffico all'ingrosso da account che si iscrivono su istruzione, ed è per questo che le ricariche fanno parte dell'offerta."),
            ("Vendete visualizzazioni YouTube da sole?", "No. Le visualizzazioni non sono una voce a parte. Arrivano dalle persone raggiunte dalla nostra campagna, le stesse che si iscrivono, mettono like e commentano."),
            ("Le visualizzazioni dei pannelli possono mettere nei guai il mio canale?", "Sì. Le visualizzazioni artificiali violano le regole di YouTube sull'engagement falso; possono essere tolte dal tuo conteggio, e l'uso ripetuto mette a rischio il canale."),
            ("Offrite un pannello per rivenditori?", "No. Non vendiamo all'ingrosso né tramite rivenditori: ogni pacchetto è una campagna costruita intorno a un canale. Le agenzie con più canali possono contattarci per parlarne."),
            ("Cosa porta un pacchetto ogni mese?", "{pick_name} porta di solito {pick_audience} nuovi iscritti al mese, spettatori reali che arrivano in tutti i 30 giorni."),
        ],
    },
    # --- Visualizzazioni --------------------------------------------------------------------
    {
        "service": "views",
        "modifier": "cheap",
        "slug": "youtube/visualizzazioni/economiche",
        "label": "Visualizzazioni YouTube economiche?",
        "plan": "starter",
        "title": "Visualizzazioni YouTube economiche? Cosa ottieni | Growsterr",
        "description": "Visualizzazioni YouTube economiche a un dollaro per mille? Sono riproduzioni, non spettatori. Noi portiamo persone reali che guardano e si iscrivono.",
        "h1": ("Le visualizzazioni YouTube economiche ", "sono riproduzioni, non spettatori."),
        "intro": "Se pensi di comprare visualizzazioni YouTube economiche, magari mille per un dollaro, sappi cosa arriva: riproduzioni da script o da account all'ingrosso che guardano al massimo qualche secondo, e YouTube può toglierle dal tuo conteggio. Non vendiamo visualizzazioni a parte. Il nostro pacchetto mensile porta persone reali sul tuo canale, che guardano, mettono like, commentano e si iscrivono per scelta.",
        "hero": {"image": "youtube-viewers", "alt": "Spettatori reali guardano un video YouTube fino alla fine"},
        "sections": [
            {
                "h2": "Quanto vale una visualizzazione",
                "p": [
                    "Una visualizzazione aiuta quando una persona guarda. Quanto resta, se mette like e su quale video clicca dopo sono ciò che mostra a YouTube che un video merita più spettatori. Una visualizzazione economica aggiunge uno al contatore e non dà a YouTube niente su cui basarsi.",
                    "Un numero di visualizzazioni alto con un tempo di visualizzazione quasi nullo manda anche un segnale contraddittorio, e le riproduzioni comprate possono comunque essere rimosse.",
                ],
            },
            {
                "h2": "Un pacchetto per YouTube, quello onesto",
                "p": [
                    "Un pacchetto lo vendiamo, solo non un pacchetto di visualizzazioni. {starter_name} costa {starter_price} al mese: di solito {starter_audience} nuovi iscritti, {starter_likes} like e {starter_comments} commenti da spettatori reali, più le visualizzazioni che quelle stesse persone danno ai tuoi video.",
                    "Le visualizzazioni non si contano in anticipo. Seguono i tuoi contenuti e non una quota, perché ognuna è la scelta di qualcuno.",
                ],
            },
            {
                "h2": "Prezzo per visualizzazione o prezzo per spettatore",
                "p": [
                    "Conta gli spettatori, non le visualizzazioni. Un iscritto reale può guardare decine dei tuoi video nei mesi in cui resta. Un dollaro di riproduzioni da script non guarda niente dopo oggi.",
                ],
            },
        ],
        "faqs": [
            ("Quanto costano le visualizzazioni YouTube con voi?", "Le visualizzazioni non hanno un prezzo a parte. Il pacchetto più piccolo, {starter_name}, costa {starter_price} al mese e porta iscritti, like e commenti, con le visualizzazioni di quelle stesse persone."),
            ("Perché le visualizzazioni da 1 dollaro costano così poco?", "Perché nessuno le guarda. Script e account all'ingrosso possono produrre riproduzioni quasi a costo zero, e le riproduzioni sono tutto ciò che producono."),
            ("Le visualizzazioni economiche mi porteranno spettatori reali?", "Difficilmente. YouTube guarda come le persone rispondono a un video, non solo il numero, e le visualizzazioni comprate non rispondono."),
            ("Posso scegliere quali video ricevono spettatori?", "No. La campagna promuove il tuo canale nel suo insieme, e gli spettatori scelgono cosa guardare. Titoli e miniature forti li aiutano a trovare i tuoi lavori migliori."),
            ("C'è un pacchetto molto economico solo per le visualizzazioni?", "Non esiste un'opzione di sole visualizzazioni sotto {starter_name} a {starter_price} al mese, perché le visualizzazioni arrivano dalle persone che porta un pacchetto."),
        ],
    },
    {
        "service": "views",
        "modifier": "fast",
        "slug": "youtube/visualizzazioni/veloci",
        "label": "Visualizzazioni YouTube veloci?",
        "title": "Visualizzazioni YouTube veloci? Ecco come funziona | Growsterr",
        "description": "Le visualizzazioni YouTube istantanee, anche per le première, arrivano da script. Gli spettatori reali arrivano dai primi giorni della campagna e continuano.",
        "h1": ("Visualizzazioni YouTube veloci? ", "Gli spettatori non arrivano per corriere."),
        "intro": "Vuoi comprare visualizzazioni YouTube veloci, con consegna istantanea? Le visualizzazioni consegnate a tempo arrivano da script, non da persone: uno spettatore reale clicca quando un video attira la sua attenzione. Noi non vendiamo né consegniamo visualizzazioni. Portiamo persone reali sul tuo canale ogni giorno fin dai primi giorni della campagna, e guardano, mettono like e si iscrivono di loro iniziativa.",
        "hero": {"image": "youtube-viewers", "alt": "Spettatori scoprono il nuovo video YouTube di un creator"},
        "sections": [
            {
                "h2": "La consegna rapida è una parola da pacchi",
                "p": [
                    "I tempi di consegna hanno senso per le cose nelle scatole. Per le visualizzazioni, una velocità di consegna significa che una macchina sta premendo play, e quelle riproduzioni non portano nessun tempo di visualizzazione che valga qualcosa.",
                ],
            },
            {
                "h2": "Le visualizzazioni di una première hanno bisogno di persone reali",
                "p": [
                    "Una première è un momento: persone che aspettano, scrivono in chat e guardano insieme. Le visualizzazioni comprate per una première possono riempire un contatore ma mai la chat. Nemmeno noi possiamo portare un pubblico a un minuto preciso, e non faremo finta di poterlo fare.",
                    "Ciò che aiuta è una base più ampia di iscritti reali, che possono vedere la première nella loro home o nel feed delle iscrizioni e toccare per ricevere un promemoria.",
                ],
            },
            {
                "h2": "Quanto in fretta crescono le visualizzazioni reali",
                "ul": [
                    "Nei primi giorni, la tua campagna parte e nuovi spettatori raggiungono il tuo canale.",
                    "Ogni video caricato questo mese è lì per le persone che si sono iscritte la settimana scorsa.",
                    "Le visualizzazioni continuano ad arrivare da quegli iscritti finché i tuoi video piacciono loro.",
                ],
            },
        ],
        "faqs": [
            ("Quanto in fretta saliranno le mie visualizzazioni?", "Una volta attiva la campagna, cosa che succede nei suoi primi giorni, le visualizzazioni salgono man mano che persone nuove trovano il tuo canale. Crescono con il tuo pubblico invece di saltare su un solo video."),
            ("Potete mandare visualizzazioni istantanee a un nuovo video?", "No. Le visualizzazioni istantanee arrivano da script. Le visualizzazioni reali su un nuovo video arrivano da persone che lo vedono nel loro feed o tra i consigliati, e il nostro lavoro è far crescere quel gruppo."),
            ("Potete riempire la mia première di spettatori in diretta?", "Nessuno può promettere persone reali a un minuto preciso. Far crescere iscritti reali prima di una première ti dà più persone che potrebbero collegarsi."),
            ("Le visualizzazioni sono contate nel mio pacchetto?", "Sono incluse, senza un numero fisso. Le stesse persone che si iscrivono, mettono like e commentano guardano anche, quindi le visualizzazioni seguono il tuo pubblico."),
            ("Quale pacchetto porta più visualizzazioni?", "Non dimensioniamo i pacchetti sulle visualizzazioni. Un pacchetto più grande raggiunge più persone, quindi {pro_name}, con di solito {pro_audience} nuovi iscritti al mese, significa di norma più persone che guardano."),
        ],
    },
    {
        "service": "views",
        "modifier": "free",
        "slug": "youtube/visualizzazioni/gratis",
        "label": "Visualizzazioni YouTube gratis?",
        "plan": "starter",
        "tool": "engagement-calculator",
        "title": "Visualizzazioni YouTube gratis? Perché non aiutano | Growsterr",
        "description": "Visualizzazioni YouTube gratis, anche sugli Shorts? Arrivano da scambi e script. Controlla invece il tuo engagement con il calcolatore gratuito.",
        "h1": ("1.000 visualizzazioni YouTube gratis ", "non guarderanno il tuo video. Le persone reali sì."),
        "intro": "Le offerte di 1.000 visualizzazioni YouTube gratis, anche sugli Shorts, usano scambi, trucchi di autoplay o riproduzioni di bot, e nessuna porta qualcuno che guarda. Non regaliamo visualizzazioni. Il calcolatore di engagement qui sotto è gratuito e ti dice quale quota dei tuoi iscritti reagisce a un video tipico. Quando vuoi più persone reali a guardare, i nostri pacchetti le portano.",
        "hero": {"image": "youtube-channel", "alt": "Uno youtuber controlla like e commenti dei suoi video recenti"},
        "sections": [
            {
                "h2": "Da dove arrivano le visualizzazioni gratis",
                "ul": [
                    "Scambi di visualizzazioni: guardi i video di sconosciuti per guadagnare crediti, e loro fanno partire i tuoi senza audio.",
                    "Incorporamenti e trucchi di autoplay che contano una riproduzione che nessuno ha scelto.",
                    "Riproduzioni di bot regalate in piccoli blocchi per venderti quelli più grandi.",
                    "Visualizzazioni gratis per gli Shorts da script che scorrono via dopo un secondo.",
                ],
            },
            {
                "h2": "Controlla il tuo engagement con il calcolatore",
                "p": [
                    "Questo calcolatore funziona interamente nel tuo browser, senza costi. Dove chiede i follower, inserisci i tuoi iscritti; poi aggiungi la media di like e commenti dei tuoi video recenti. Il risultato è la quota del tuo pubblico che reagisce, un controllo dello stato di salute molto migliore di un numero di visualizzazioni.",
                ],
            },
            {
                "h2": "Modi gratuiti per guadagnare più visualizzazioni",
                "ul": [
                    "Dedica a titolo e miniatura lo stesso tempo che dedichi al montaggio; sono loro a decidere il clic.",
                    "Arriva al punto nei primi secondi di un video o di uno Short.",
                    "Aggiungi schermate finali e playlist, così una visualizzazione porta alla successiva.",
                    "Rispondi ai commenti; le persone tornano nelle conversazioni.",
                ],
            },
        ],
        "faqs": [
            ("Posso avere 1.000 visualizzazioni YouTube gratis?", "Non da persone reali, e non da noi. Mille visualizzazioni gratis arrivano da scambi o script. Il calcolatore in questa pagina è la parte davvero gratuita."),
            ("Le visualizzazioni gratis per gli Shorts sono diverse?", "No. Arrivano dagli stessi trucchi. Uno Short viaggia solo quando persone reali lo guardano fino alla fine, quindi le riproduzioni da script non lo aiutano."),
            ("Le visualizzazioni gratis possono far penalizzare il mio canale?", "È un rischio concreto. Le visualizzazioni da sistemi automatici o da scambi rientrano nelle norme di YouTube sull'engagement falso, che permettono a YouTube di rimuoverle o di agire contro il canale."),
            ("Avete un pacchetto di visualizzazioni gratuito?", "No. Il pacchetto più piccolo è {starter_name} a {starter_price} al mese, e le visualizzazioni arrivano al suo interno, dalle persone reali che si iscrivono."),
            ("Cosa mi dice il tasso di engagement?", "Quanta parte del tuo pubblico c'è davvero. Un tasso basso con molti iscritti di solito significa che molti iscritti hanno smesso di guardare, o non l'hanno mai fatto."),
        ],
    },
    {
        "service": "views",
        "modifier": "free-trial",
        "slug": "youtube/visualizzazioni/prova-gratuita",
        "label": "Prova gratuita di visualizzazioni YouTube?",
        "plan": "starter",
        "title": "Visualizzazioni YouTube in prova gratuita? | Growsterr",
        "description": "Niente prova gratuita di visualizzazioni YouTube. Mettici alla prova con un mese di spettatori reali e le statistiche di YouTube.",
        "h1": ("Una prova di visualizzazioni YouTube ", "dimostra solo che un contatore può muoversi."),
        "intro": "Speri in una prova gratuita di visualizzazioni YouTube prima di pagare? Qui non ce ne sono, e le visualizzazioni non vengono vendute da sole. Una prova di qualche migliaio di visualizzazioni in un'ora dimostrerebbe solo che qualcuno ha degli script. Offriamo invece un pacchetto mensile che porta persone reali sul tuo canale, con le visualizzazioni di quelle stesse persone, e puoi disdire quando vuoi.",
        "hero": {"image": "youtube-hub", "alt": "Un creator confronta le statistiche di YouTube con una dashboard di crescita"},
        "sections": [
            {
                "h2": "Cosa misura una prova di visualizzazioni",
                "p": [
                    "Una cosa sola: se il numero si muove. Non dice niente su chi ha guardato, per quanto tempo o se qualcuno è tornato. Sono queste le domande che contano, e solo spettatori reali possono rispondere.",
                ],
            },
            {
                "h2": "Mettici alla prova con i numeri di YouTube",
                "p": [
                    "Nel tuo primo mese, apri YouTube Studio accanto alla nostra dashboard. Guarda gli spettatori di ritorno, la durata media di visualizzazione e i nuovi iscritti. Le persone reali lasciano in quei numeri una traccia che le riproduzioni comprate non lasciano mai.",
                ],
            },
        ],
        "faqs": [
            ("C'è una prova per le visualizzazioni YouTube?", "Nessuna prova, né per le visualizzazioni né per altro. L'impegno più breve è un mese di pacchetto, e puoi disdire prima che si rinnovi."),
            ("Posso comprare un piccolo pacchetto di visualizzazioni per provare?", "Non vendiamo visualizzazioni come pacchetto a parte, né piccolo né grande. {starter_name}, a {starter_price} al mese, è il modo più piccolo per iniziare."),
            ("Come distinguo le visualizzazioni reali da quelle comprate?", "Guarda oltre il numero: tempo di visualizzazione, spettatori di ritorno e commenti che le persone scrivono ti dicono chi c'è davvero."),
            ("E se disdico dopo il primo mese?", "Il tuo pacchetto si ferma quando finisce il mese pagato. Gli spettatori che si sono iscritti restano iscritti a meno che non scelgano di andarsene."),
            ("Le visualizzazioni arrivano con gli iscritti?", "Sì. Ogni pacchetto porta nuovi iscritti, like e commenti, e quelle stesse persone guardano i tuoi video."),
        ],
    },
]
