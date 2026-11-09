"""Italian YouTube pages: the hub and subscribers ("iscritti"). Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "youtube",
        "label": "YouTube",
        "title": "Pacchetti di crescita YouTube per creator | Growsterr",
        "description": "Fai crescere il tuo canale YouTube con persone reali: pacchetti mensili con iscritti, like e commenti da spettatori veri. Da {from_price} al mese.",
        "h1": ("Fai crescere il tuo canale YouTube ", "con spettatori reali."),
        "intro": "Pacchetti di crescita mensili per creator. Persone reali scoprono il tuo canale, guardano i tuoi video e si iscrivono quando apprezzano ciò che vedono. La tua dashboard mostra ciò che abbiamo misurato, giorno per giorno.",
        "hero": {"image": "youtube-hub", "alt": "Un canale YouTube che guadagna iscritti, like e commenti da spettatori reali"},
        "sections": [
            {
                "h2": "Contano gli iscritti che guardano",
                "p": [
                    "YouTube consiglia i video che le persone guardano, a cui mettono like e su cui tornano. Un iscritto che non guarda mai è peggio di nessuno: abbassa la quota del tuo pubblico che partecipa.",
                    "Ogni iscritto che portiamo è una persona che ha trovato il tuo canale e ha scelto di iscriversi. Like, visualizzazioni e commenti arrivano dalle stesse persone, dentro il tuo pacchetto.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Spettatori guardano il video YouTube di un creator e scrivono commenti"},
            },
            {
                "h2": "Per canali che pubblicano con cura",
                "p": [
                    "Tutorial, vlog, musica o gaming: se pubblichi con regolarità, spettatori reali danno a ogni nuovo video una partenza migliore. Inizia con {starter_name} e passa a un pacchetto superiore quando il tuo canale è pronto per di più.",
                ],
                "ul": [
                    "Ci dici la città, la regione o il paese da cui deve arrivare il tuo pubblico.",
                    "Iscritti, like e commenti arrivano insieme, dalle stesse persone.",
                    "Il canale resta tuo: non chiediamo mai la tua password.",
                ],
                "image": {"image": "youtube-channel", "alt": "Un creator monta un video YouTube nel suo studio di casa"},
            },
        ],
        "faqs": [
            ("Gli iscritti sono persone reali?", "Sì. Ogni iscritto è una persona reale che ha trovato il tuo canale e ha scelto di iscriversi. Niente bot, niente account falsi, niente di istantaneo."),
            ("Quanti iscritti porta un pacchetto?", "Di solito {starter_audience} nuovi iscritti al mese con {starter_name}, {rising_audience} con {rising_name} e {pro_audience} con {pro_name}. Intervalli tipici, non un numero fisso."),
            ("Vi serve la mia password di Google o YouTube?", "Mai. Ci serve solo l'handle del tuo canale, e il canale deve essere pubblico."),
            ("Posso comprare visualizzazioni o like da soli?", "No. Visualizzazioni, like e commenti sono inclusi in ogni pacchetto e arrivano dalle stesse persone reali che si iscrivono."),
            ("Posso disdire quando voglio?", "Sì. I pacchetti si rinnovano ogni mese e puoi disdire dal tuo account. Il mese già pagato prosegue fino alla fine."),
        ],
    },
    {
        "service": "subscribers",
        "slug": "youtube/iscritti",
        "label": "Iscritti YouTube",
        "title": "Iscritti YouTube reali che guardano | Growsterr",
        "description": "Iscritti YouTube che sono persone reali: spettatori che hanno trovato il tuo canale e scelto di iscriversi, con like e commenti. Da {from_price} al mese.",
        "h1": ("Iscritti YouTube ", "che guardano davvero."),
        "intro": "Persone reali scoprono il tuo canale, guardano i tuoi video e si iscrivono quando apprezzano ciò che vedono. Di solito {starter_audience} nuovi iscritti al mese con {starter_name}, con like e commenti dagli stessi spettatori.",
        "hero": {"image": "youtube-subscribers", "alt": "La pagina di un canale YouTube con nuovi iscritti da spettatori reali"},
        "sections": [
            {
                "h2": "Un iscritto dovrebbe essere uno spettatore",
                "p": [
                    "Su YouTube un iscritto è utile solo se guarda. Gli iscritti reali vedono il tuo prossimo video, lo guardano, mettono like e a volte commentano, ed è questo che YouTube osserva quando decide cosa consigliare.",
                    "Gli iscritti bot non guardano mai. Fanno sembrare un canale più grande mentre i suoi video raggiungono meno persone.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Spettatori reali si iscrivono a un canale YouTube dopo aver guardato un video"},
            },
            {
                "h2": "Com'è un mese",
                "ul": [
                    "Primi giorni: la campagna parte e arrivano i primi spettatori.",
                    "Ogni settimana: nuovi iscritti, like e commenti, un po' ogni giorno.",
                    "A fine mese: di solito {pick_audience} nuovi iscritti con {pick_name}.",
                ],
            },
            {
                "h2": "Da dove arrivano i tuoi spettatori",
                "p": [
                    "Dicci la città, la regione o il paese da cui deve arrivare il tuo pubblico. Mostriamo il tuo canale prima di tutto a persone reali lì; dove il pubblico più adatto è più numeroso nelle vicinanze, ne possono arrivare di più da lì.",
                ],
            },
        ],
        "faqs": [
            ("Quanto velocemente arrivano gli iscritti?", "Un po' ogni giorno, per tutto il mese. Mai tutti insieme: le persone reali si iscrivono con i loro tempi."),
            ("Guarderanno i miei video?", "Sono persone reali che hanno scelto di iscriversi dopo aver visto il tuo canale. Cosa guardano dopo lo decidono loro, come qualsiasi pubblico, ed è proprio per questo che conta."),
            ("Ricevo anche like e commenti?", "Sì, dagli stessi spettatori: di solito {pick_likes} like e {pick_comments} commenti al mese con {pick_name}."),
            ("Vi serve la mia password?", "Mai. Ci serve solo l'handle del tuo canale, e il canale deve essere pubblico."),
        ],
    },
]
