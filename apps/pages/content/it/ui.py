"""Italian UI of the money pages ("tu"). Mirrors en/ui.py key by key.

{follow} reads after "scelto di": "seguirti" / "iscriversi".
"""

UI = {
    # Words that change with the platform or the service
    "audience": {"instagram": "follower", "tiktok": "follower", "youtube": "iscritti"},
    "follow": {"instagram": "seguirti", "tiktok": "seguirti", "youtube": "iscriversi"},
    "profile": {"instagram": "profilo", "tiktok": "profilo", "youtube": "canale"},
    "handle": {"instagram": "nome utente", "tiktok": "nome utente", "youtube": "handle del canale"},
    "content": {"instagram": "post", "tiktok": "video", "youtube": "video"},
    "service_names": {"followers": "Follower", "subscribers": "Iscritti", "likes": "Like",
                      "views": "Visualizzazioni", "comments": "Commenti"},
    "service_words": {"followers": "follower", "subscribers": "iscritti", "likes": "like",
                      "views": "visualizzazioni", "comments": "commenti"},

    # Page chrome
    "home": "Home",
    "crumbs_label": "Percorso di navigazione",
    "eyebrow": "{platform} · {service_name}",
    "eyebrow_hub": "Crescita su {platform}",
    "cta": "Inizia con {pick_name}",
    "cta_more": "Vedi tutti i pacchetti",
    "trust": ["Persone reali, mai bot", "Non chiediamo mai la tua password", "Mensile, disdici quando vuoi"],
    "product_name": "Pacchetti di crescita per {platform}",
    "sticky_cta": "Inizia",

    # Packages
    "packages_title": "Scegli il tuo pacchetto",
    "packages_lead": "Tre pacchetti mensili. Nuovi {audience}, like, visualizzazioni e commenti arrivano insieme, dalle stesse persone reali.",
    "packages_note": "Intervalli mensili tipici, non un numero fisso: ognuno dei tuoi nuovi {audience} è una persona reale che ha scelto di {follow}, quindi ogni mese è un po' diverso.",

    # What's included: the page's own service comes first, then the rest in this order.
    "included_title": "Cosa è incluso",
    "included_lead": "Ogni pacchetto porta il quadro completo, dalle stesse persone reali.",
    "included_items": {
        "audience": ("Nuovi {audience}", "Persone reali che hanno scoperto il tuo {profile} e hanno scelto di {follow}. Di solito {starter_audience} al mese con {starter_name}."),
        "likes": ("Like dalle stesse persone", "Di solito {starter_likes} al mese con {starter_name}, sui {content} che apprezzano."),
        "comments": ("Commenti con parole loro", "Di solito {starter_comments} al mese con {starter_name}. Scritti da persone, mai da copione."),
        "views": ("Visualizzazioni comprese", "Le stesse persone guardano i tuoi {content} di loro iniziativa. Non contiamo le visualizzazioni in anticipo: dietro ognuna c'è una persona."),
        "days": ("Distribuito su 30 giorni", "Un po' ogni giorno, dalla zona che scegli tu. Mai tutto in una volta."),
        "dashboard": ("La tua dashboard", "Ciò che abbiamo misurato, giorno per giorno: le visite arrivate dalla tua campagna e i nuovi {audience} che hanno portato."),
    },

    # How it works: the subscription, step by step
    "steps_title": "Come funziona",
    "steps_lead": "Un abbonamento mensile: tu scegli il pacchetto, noi gestiamo la campagna, le persone reali decidono.",
    "steps": [
        ("Scegli un pacchetto", "{starter_name}, {rising_name} o {pro_name}, con addebito mensile. Disdici quando vuoi dal tuo account."),
        ("Avviamo la tua campagna", "Dicci il tuo {handle} di {platform} e da dove deve arrivare il tuo pubblico. Non chiediamo mai la tua password."),
        ("Persone reali scoprono il tuo {profile}", "Ogni giorno il tuo {profile} viene mostrato a persone reali. Chi apprezza ciò che vede sceglie da sé di {follow}, mettere like e commentare."),
        ("La tua dashboard mostra ciò che abbiamo misurato", "Le visite arrivate dalla tua campagna e i nuovi {audience} che hanno portato, giorno per giorno. Numeri misurati, mai stime a occhio."),
    ],

    # Real people vs bots / instant
    "compare_title": "Persone reali, non bot",
    "compare_lead": "Istantaneo significa bot: nessuna persona reale sceglie di {follow} pochi secondi dopo un pagamento.",
    "compare_cols": ("Cosa cambia", "Servizi istantanei e bot", "Growsterr"),
    "compare": [
        ("Chi sono", "Bot e profili falsi", "Persone reali che hanno scelto di {follow}"),
        ("Velocità", "Migliaia in pochi minuti", "Un po' ogni giorno, per tutto il mese"),
        ("Like e commenti", "Venduti a parte, da altri bot", "Dalle stesse persone, dentro il tuo pacchetto"),
        ("La tua portata", "Cala in silenzio: un pubblico che non interagisce mai dice a {platform} che i tuoi {content} non meritano di essere mostrati", "Cresce con persone che guardano, mettono like e tornano"),
        ("La tua password", "Spesso richiesta", "Mai"),
        ("Cosa vedi", "Un numero che può sparire alla prossima pulizia", "Una dashboard con ciò che abbiamo misurato"),
    ],

    # Quantity pages: how a monthly package gets you to the goal
    "quantity_title": "Come arrivare a {quantity} {service}",
    "quantity_lead": "Non vendiamo un lotto fisso di {quantity}. Le persone reali decidono da sole, quindi un pacchetto mensile ti ci porta a un ritmo naturale.",
    "pace_title": "Ritmo tipico con {pick_name}",
    "pace_month": "Mese {n}",
    "pace_goal": "Obiettivo: {quantity}",
    "pace_note": "Intervalli tipici basati su ciò che fanno persone reali, mai una promessa. Alcuni mesi portano di più, altri di meno.",
    "by_plan_title": "Tempo per arrivare a {quantity}, per pacchetto",
    "a_month": "{range} al mese",
    "when_first": "di solito già nel primo mese",
    "when_about": "di solito circa {n} mesi",
    "when_range": "di solito {low}–{high} mesi",
    "views_pace": "Le visualizzazioni arrivano dalle stesse persone reali che scoprono il tuo {profile}, quindi non le contiamo in anticipo. {pick_name} è il pacchetto più adatto a questo obiettivo.",

    # FAQ, related pages, closing
    "faq_title": "Domande e risposte",
    "related_title": "Continua a esplorare",
    "related": {
        "platform": "Altro su {platform}",
        "platforms": "Su altre piattaforme",
        "quantities": "Altri obiettivi",
        "modifiers": "Altri modi per crescere",
        "articles": "Leggi anche",
        "hubs": "Cresci con persone reali su",
    },
    # The tools a page can carry ("tool"): they run in the browser, nothing is sent.
    "tools": {
        "calculate": "Calcola",
        "followers": "Follower",
        "avg_likes": "Like medi per post",
        "avg_comments": "Commenti medi per post",
        "engagement_title": "Il tuo tasso di engagement",
        "engagement_lead": "Quanti dei tuoi follower reagiscono a un post tipico. Inserisci i numeri dei tuoi ultimi post.",
        "engagement_result": "Il tuo tasso di engagement è {rate}%.",
        "engagement_note": "Il tasso sale quando le persone che ti seguono tengono davvero ai tuoi post. I follower che non reagiscono mai lo abbassano, qualunque sia il loro numero.",
        "growth_title": "Quanto manca al tuo obiettivo?",
        "growth_lead": "Inserisci dove sei e dove vuoi arrivare. Lo calcoliamo dall'intervallo mensile tipico di ogni pacchetto.",
        "current": "Follower oggi",
        "goal": "Il tuo obiettivo",
        "when_first": "di solito già nel primo mese",
        "when_range": "di solito {low}–{high} mesi",
        "when_about": "circa {n} mesi",
        "reached": "Ci sei già.",
        "growth_note": "Intervalli tipici, non una promessa: sono le persone reali a decidere se seguirti.",
    },
    # Eyebrow above the headline of pages outside the platform x service grid (by "kind").
    "article_eyebrows": {
        "guide": "Guida",
        "alternative": "Confronto",
        "payment": "Pagamenti",
        "agency": "Agenzia di crescita",
        "tool": "Strumento",
        "intent": "Risposta chiara",
    },
    "cta_title": "Pronto a crescere su {platform}?",
    "cta_text": "Scegli un pacchetto e avviamo la tua campagna. Il resto lo decidono persone reali, e la tua dashboard mostra ciò che abbiamo misurato.",

    # Platform hubs
    "services_title": "Cosa facciamo crescere su {platform}",
    "services_lead": "Un solo pacchetto porta tutto, dalle stesse persone reali.",
    "teasers": {
        "audience": "Persone reali che scoprono il tuo {profile} e scelgono di {follow}.",
        "likes": "Like da chi apprezza i tuoi {content}.",
        "views": "Visualizzazioni da persone che scelgono di guardare, mai da script.",
        "comments": "Commenti scritti da persone reali, con parole loro.",
    },
    "explore": "Scopri",
    "in_package": "Incluso in ogni pacchetto",
    "goals_title": "Altri modi per crescere su {platform}",
    "other_hubs_title": "Ti facciamo crescere anche su",
}
