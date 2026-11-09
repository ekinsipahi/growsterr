"""German UI of the money pages (formal "Sie"). Mirrors en/ui.py key by key.

Grammar notes for the placeholders:
    {follow} is a noun here ("fürs {follow}" -> fürs Folgen / fürs Abonnieren).
    {profile} is Profil (neuter) or Kanal (masculine): use it only in the nominative or dative
    ("Ihr {profile}", "auf Ihrem {profile}"), where both take the same form.
    {handle} is in the dative/accusative form ("mit Ihrem {handle}").
"""

UI = {
    # Words that change with the platform or the service
    "audience": {"instagram": "Follower", "tiktok": "Follower", "youtube": "Abonnenten"},
    "follow": {"instagram": "Folgen", "tiktok": "Folgen", "youtube": "Abonnieren"},
    "profile": {"instagram": "Profil", "tiktok": "Profil", "youtube": "Kanal"},
    "handle": {"instagram": "Benutzernamen", "tiktok": "Benutzernamen", "youtube": "Kanal-Handle"},
    "content": {"instagram": "Beiträge", "tiktok": "Videos", "youtube": "Videos"},
    "service_names": {"followers": "Follower", "subscribers": "Abonnenten", "likes": "Likes",
                      "views": "Aufrufe", "comments": "Kommentare"},
    "service_words": {"followers": "Follower", "subscribers": "Abonnenten", "likes": "Likes",
                      "views": "Aufrufe", "comments": "Kommentare"},

    # Page chrome
    "home": "Startseite",
    "crumbs_label": "Navigationspfad",
    "eyebrow": "{platform} · {service_name}",
    "eyebrow_hub": "{platform}-Wachstum",
    "cta": "Mit {pick_name} starten",
    "cta_more": "Alle Pakete ansehen",
    "trust": ["Echte Menschen, niemals Bots", "Wir fragen nie nach Ihrem Passwort", "Monatlich, jederzeit kündbar"],
    "product_name": "{platform}-Wachstumspakete",
    "sticky_cta": "Starten",

    # Packages
    "packages_title": "Wählen Sie Ihr Paket",
    "packages_lead": "Drei Monatspakete. Neue {audience}, Likes, Aufrufe und Kommentare kommen zusammen, von denselben echten Menschen.",
    "packages_note": "Typische Monatswerte, keine feste Anzahl: Jeder Ihrer neuen {audience} ist ein echter Mensch, der sich selbst fürs {follow} entschieden hat. Deshalb ist jeder Monat etwas anders.",

    # What's included: the page's own service comes first, then the rest in this order.
    "included_title": "Was enthalten ist",
    "included_lead": "Jedes Paket bringt das ganze Bild, von denselben echten Menschen.",
    "included_items": {
        "audience": ("Neue {audience}", "Echte Menschen, die auf Ihrem {profile} gelandet sind und sich fürs {follow} entschieden haben. Mit {starter_name} typischerweise {starter_audience} pro Monat."),
        "likes": ("Likes von denselben Menschen", "Mit {starter_name} typischerweise {starter_likes} pro Monat, für die {content}, die ihnen gefallen."),
        "comments": ("Kommentare in eigenen Worten", "Mit {starter_name} typischerweise {starter_comments} pro Monat. Von Menschen geschrieben, nie nach Skript."),
        "views": ("Aufrufe inklusive", "Dieselben Menschen sehen sich Ihre {content} von sich aus an. Aufrufe zählen wir nicht im Voraus: Hinter jedem steht ein Mensch."),
        "days": ("Verteilt über 30 Tage", "Jeden Tag ein wenig, aus dem Ort Ihrer Wahl. Nie alles auf einmal."),
        "dashboard": ("Ihr Dashboard", "Was wir gemessen haben, Tag für Tag: Besuche aus Ihrer Kampagne und die neuen {audience}, die daraus entstanden sind."),
    },

    # How it works: the subscription, step by step
    "steps_title": "So funktioniert's",
    "steps_lead": "Ein Monatsabo: Sie wählen das Paket, wir führen die Kampagne, echte Menschen entscheiden.",
    "steps": [
        ("Paket wählen", "{starter_name}, {rising_name} oder {pro_name}, monatlich abgerechnet. Jederzeit in Ihrem Konto kündbar."),
        ("Wir starten Ihre Kampagne", "Wir starten mit Ihrem {handle} auf {platform} und dem Ort, aus dem Ihr Publikum kommen soll. Nach Ihrem Passwort fragen wir nie."),
        ("Echte Menschen finden zu Ihrem {profile}", "Ihr {profile} wird jeden Tag echten Menschen gezeigt. Wer mag, was er sieht, entscheidet sich von selbst fürs {follow}, liked und kommentiert."),
        ("Ihr Dashboard zeigt, was wir gemessen haben", "Besuche aus Ihrer Kampagne und die neuen {audience}, die daraus entstanden sind, Tag für Tag. Gemessene Zahlen, keine Schätzungen."),
    ],

    # Real people vs bots / instant
    "compare_title": "Echte Menschen, keine Bots",
    "compare_lead": "Sofort heißt Bots: Kein echter Mensch entscheidet sich Sekunden nach einer Zahlung fürs {follow}.",
    "compare_cols": ("Was sich ändert", "Sofort- und Bot-Dienste", "Growsterr"),
    "compare": [
        ("Wer sie sind", "Bots und Fake-Profile", "Echte Menschen, die sich fürs {follow} entschieden haben"),
        ("Tempo", "Tausende in Minuten", "Jeden Tag ein wenig, den ganzen Monat"),
        ("Likes und Kommentare", "Separat verkauft, von noch mehr Bots", "Von denselben Menschen, in Ihrem Paket"),
        ("Ihre Reichweite", "Sinkt leise: Ein Publikum, das nie reagiert, signalisiert {platform}, dass Ihre {content} niemand sehen will", "Wächst mit Menschen, die schauen, liken und wiederkommen"),
        ("Ihr Passwort", "Wird oft verlangt", "Nie"),
        ("Was Sie sehen", "Eine Zahl, die bei der nächsten Bereinigung verschwinden kann", "Ein Dashboard mit dem, was wir gemessen haben"),
    ],

    # Quantity pages: how a monthly package gets you to the goal
    "quantity_title": "So erreichen Sie {quantity} {service}",
    "quantity_lead": "Wir verkaufen kein festes Paket mit {quantity}. Echte Menschen entscheiden selbst, deshalb bringt Sie ein Monatspaket in natürlichem Tempo ans Ziel.",
    "pace_title": "Typisches Tempo mit {pick_name}",
    "pace_month": "Monat {n}",
    "pace_goal": "Ziel: {quantity}",
    "pace_note": "Typische Spannen aus dem, was echte Menschen tun, nie ein Versprechen. Manche Monate bringen mehr, manche weniger.",
    "by_plan_title": "Zeit bis {quantity}, nach Paket",
    "a_month": "{range} pro Monat",
    "when_first": "meist schon im ersten Monat",
    "when_about": "meist etwa {n} Monate",
    "when_range": "meist {low}–{high} Monate",
    "views_pace": "Aufrufe kommen von denselben echten Menschen, die auf Ihrem {profile} landen, deshalb zählen wir sie nicht im Voraus. {pick_name} ist das Paket, das am besten zu diesem Ziel passt.",

    # FAQ, related pages, closing
    "faq_title": "Fragen und Antworten",
    "related_title": "Weiter entdecken",
    "related": {
        "platform": "Mehr zu {platform}",
        "platforms": "Auf anderen Plattformen",
        "quantities": "Andere Ziele",
        "modifiers": "Weitere Wege zu wachsen",
        "articles": "Weiterlesen",
        "hubs": "Mit echten Menschen wachsen auf",
    },
    # The tools a page can carry ("tool"): they run in the browser, nothing is sent.
    "tools": {
        "calculate": "Berechnen",
        "followers": "Follower",
        "avg_likes": "Likes pro Beitrag im Schnitt",
        "avg_comments": "Kommentare pro Beitrag im Schnitt",
        "engagement_title": "Ihre Engagement-Rate",
        "engagement_lead": "Wie viele Ihrer Follower auf einen typischen Beitrag reagieren. Geben Sie die Zahlen Ihrer letzten Beiträge ein.",
        "engagement_result": "Ihre Engagement-Rate liegt bei {rate} %.",
        "engagement_note": "Die Rate steigt, wenn sich Ihre Follower wirklich für Ihre Beiträge interessieren. Follower, die nie reagieren, senken sie, egal wie viele es sind.",
        "growth_title": "Wie lange bis zu Ihrem Ziel?",
        "growth_lead": "Geben Sie ein, wo Sie stehen und wohin Sie wollen. Wir rechnen es aus der typischen Monatsspanne jedes Pakets aus.",
        "current": "Follower heute",
        "goal": "Ihr Ziel",
        "when_first": "meist schon im ersten Monat",
        "when_range": "meist {low}–{high} Monate",
        "when_about": "etwa {n} Monate",
        "reached": "Sie sind schon am Ziel.",
        "growth_note": "Typische Spannen, kein Versprechen: Echte Menschen entscheiden selbst, ob sie folgen.",
    },
    # Eyebrow above the headline of pages outside the platform x service grid (by "kind").
    "article_eyebrows": {
        "guide": "Ratgeber",
        "alternative": "Vergleich",
        "payment": "Zahlung",
        "agency": "Wachstumsagentur",
        "tool": "Tool",
        "intent": "Klare Antwort",
    },
    "cta_title": "Bereit, auf {platform} zu wachsen?",
    "cta_text": "Wählen Sie ein Paket, und wir starten Ihre Kampagne. Den Rest entscheiden echte Menschen, und Ihr Dashboard zeigt, was wir gemessen haben.",

    # Platform hubs
    "services_title": "Was auf {platform} mit uns wächst",
    "services_lead": "Ein Paket bringt alles zusammen, von denselben echten Menschen.",
    "teasers": {
        "audience": "Echte Menschen, die auf Ihrem {profile} landen und sich fürs {follow} entscheiden.",
        "likes": "Likes von Menschen, denen Ihre {content} gefallen.",
        "views": "Aufrufe von Menschen, die selbst entscheiden zuzuschauen, nie von Skripten.",
        "comments": "Kommentare von echten Menschen, in eigenen Worten.",
    },
    "explore": "Entdecken",
    "in_package": "In jedem Paket enthalten",
    "goals_title": "Mehr Wege, auf {platform} zu wachsen",
    "other_hubs_title": "Wir sind auch hier für Sie da",
}
