"""Norwegian (Bokmål) UI of the money pages (mirrors en/ui.py key by key).
{profile}, {handle} and {content} carry the possessive (profilen din, kanalen din,
brukernavnet ditt, innleggene dine), so they read right on every platform."""

UI = {
    # Words that change with the platform or the service
    "audience": {"instagram": "følgere", "tiktok": "følgere", "youtube": "abonnenter"},
    "follow": {"instagram": "følge", "tiktok": "følge", "youtube": "abonnere"},
    "profile": {"instagram": "profilen din", "tiktok": "profilen din", "youtube": "kanalen din"},
    "handle": {"instagram": "brukernavnet ditt", "tiktok": "brukernavnet ditt", "youtube": "kanalens @-navn"},
    "content": {"instagram": "innleggene dine", "tiktok": "videoene dine", "youtube": "videoene dine"},
    "service_names": {"followers": "Følgere", "subscribers": "Abonnenter", "likes": "Likes",
                      "views": "Visninger", "comments": "Kommentarer"},
    "service_words": {"followers": "følgere", "subscribers": "abonnenter", "likes": "likes",
                      "views": "visninger", "comments": "kommentarer"},

    # Page chrome
    "home": "Hjem",
    "crumbs_label": "Brødsmulesti",
    "eyebrow": "{platform} · {service_name}",
    "eyebrow_hub": "Vekst på {platform}",
    "cta": "Start med {pick_name}",
    "cta_more": "Se alle pakkene",
    "trust": ["Ekte mennesker, aldri bots", "Vi ber aldri om passordet ditt", "Månedlig, si opp når du vil"],
    "product_name": "Vekstpakker for {platform}",
    "sticky_cta": "Kom i gang",

    # Packages
    "packages_title": "Velg pakken din",
    "packages_lead": "Tre månedlige pakker. Nye {audience}, likes, visninger og kommentarer kommer sammen, fra de samme ekte menneskene.",
    "packages_note": "Typiske intervaller per måned, ikke et fast antall: alle nye {audience} er ekte mennesker som har valgt å {follow}, så hver måned blir litt forskjellig.",

    # What's included: the page's own service comes first, then the rest in this order.
    "included_title": "Dette er inkludert",
    "included_lead": "Hver pakke gir hele bildet, fra de samme ekte menneskene.",
    "included_items": {
        "audience": ("Nye {audience}", "Ekte mennesker som har funnet {profile} og valgt å {follow}. Vanligvis {starter_audience} i måneden med {starter_name}."),
        "likes": ("Likes fra de samme menneskene", "Vanligvis {starter_likes} i måneden med {starter_name}, når de liker {content}."),
        "comments": ("Kommentarer med egne ord", "Vanligvis {starter_comments} i måneden med {starter_name}. Skrevet av mennesker, aldri etter manus."),
        "views": ("Visninger som følger med", "De samme menneskene ser {content} på eget initiativ. Vi teller ikke visninger på forhånd: hver visning er et menneske."),
        "days": ("Fordelt over 30 dager", "Litt hver dag, fra stedet du velger. Aldri alt på én gang."),
        "dashboard": ("Dashbordet ditt", "Det vi har målt, dag for dag: besøk fra kampanjen din og de nye {audience} de har gitt."),
    },

    # How it works: the subscription, step by step
    "steps_title": "Slik fungerer det",
    "steps_lead": "Et månedlig abonnement: du velger pakken, vi kjører kampanjen, ekte mennesker bestemmer.",
    "steps": [
        ("Velg en pakke", "{starter_name}, {rising_name} eller {pro_name}, fakturert månedlig. Si opp når du vil fra kontoen din."),
        ("Vi starter kampanjen din", "Gi oss {handle} på {platform}, og fortell hvor publikummet ditt skal komme fra. Vi ber aldri om passordet ditt."),
        ("Ekte mennesker oppdager {profile}", "Hver dag vises {profile} for ekte mennesker. De som liker det de ser, velger selv å {follow}, like og kommentere."),
        ("Dashbordet viser hva vi har målt", "Besøk fra kampanjen din og de nye {audience} de har gitt, dag for dag. Målte tall, aldri gjetting."),
    ],

    # Real people vs bots / instant
    "compare_title": "Ekte mennesker, ikke bots",
    "compare_lead": "Umiddelbart betyr bots: ingen ekte mennesker velger å {follow} sekunder etter en betaling.",
    "compare_cols": ("Hva som endres", "Umiddelbare tjenester og bots", "Growsterr"),
    "compare": [
        ("Hvem de er", "Bots og falske profiler", "Ekte mennesker som valgte å {follow}"),
        ("Tempo", "Tusenvis på minutter", "Litt hver dag, hele måneden"),
        ("Likes og kommentarer", "Selges separat, fra flere bots", "Fra de samme menneskene, i pakken din"),
        ("Rekkevidden din", "Synker i det stille: et publikum som aldri engasjerer seg, forteller {platform} at {content} ikke er verdt å vise", "Vokser med mennesker som ser, liker og kommer tilbake"),
        ("Passordet ditt", "Blir ofte etterspurt", "Aldri"),
        ("Det du ser", "Et tall som kan forsvinne ved neste opprydding", "Et dashbord med det vi har målt"),
    ],

    # Quantity pages: how a monthly package gets you to the goal
    "quantity_title": "Slik når du {quantity} {service}",
    "quantity_lead": "Vi selger ikke en fast pakke med {quantity}. Ekte mennesker bestemmer selv, så en månedlig pakke tar deg dit i et naturlig tempo.",
    "pace_title": "Typisk tempo med {pick_name}",
    "pace_month": "Måned {n}",
    "pace_goal": "Mål: {quantity}",
    "pace_note": "Typiske intervaller ut fra hva ekte mennesker gjør, aldri et løfte. Noen måneder gir mer, andre mindre.",
    "by_plan_title": "Tid til {quantity}, per pakke",
    "a_month": "{range} i måneden",
    "when_first": "vanligvis innen den første måneden",
    "when_about": "vanligvis rundt {n} måneder",
    "when_range": "vanligvis {low}–{high} måneder",
    "views_pace": "Visninger kommer fra de samme ekte menneskene som finner {profile}, så vi teller dem ikke på forhånd. {pick_name} er pakken som passer best til dette målet.",

    # FAQ, related pages, closing
    "faq_title": "Spørsmål og svar",
    "related_title": "Utforsk videre",
    "related": {
        "platform": "Mer om {platform}",
        "platforms": "På andre plattformer",
        "quantities": "Andre mål",
        "modifiers": "Andre måter å vokse på",
        "articles": "Les videre",
        "hubs": "Voks med ekte mennesker på",
    },
    # The tools a page can carry ("tool"): they run in the browser, nothing is sent.
    "tools": {
        "calculate": "Regn ut",
        "followers": "Følgere",
        "avg_likes": "Gjennomsnittlige likes per innlegg",
        "avg_comments": "Gjennomsnittlige kommentarer per innlegg",
        "engagement_title": "Engasjementsraten din",
        "engagement_lead": "Hvor mange av følgerne dine reagerer på et vanlig innlegg? Fyll inn tallene fra de siste innleggene dine.",
        "engagement_result": "Engasjementsraten din er {rate} %.",
        "engagement_note": "Raten stiger når de som følger deg, faktisk bryr seg om innleggene dine. Følgere som aldri reagerer, trekker den ned, uansett hvor mange de er.",
        "growth_title": "Hvor lang tid til målet ditt?",
        "growth_lead": "Fyll inn hvor du er, og hvor du vil. Vi regner ut fra hver pakkes typiske intervall per måned.",
        "current": "Følgere i dag",
        "goal": "Målet ditt",
        "when_first": "vanligvis innen den første måneden",
        "when_range": "vanligvis {low}–{high} måneder",
        "when_about": "rundt {n} måneder",
        "reached": "Du er allerede der.",
        "growth_note": "Typiske intervaller, ikke et løfte: ekte mennesker bestemmer selv om de vil følge.",
    },
    # Eyebrow above the headline of pages outside the platform x service grid (by "kind").
    "article_eyebrows": {
        "guide": "Guide",
        "alternative": "Sammenligning",
        "payment": "Betaling",
        "agency": "Vekstbyrå",
        "tool": "Verktøy",
        "intent": "Ærlig svar",
    },
    "cta_title": "Klar til å vokse på {platform}?",
    "cta_text": "Velg en pakke, så starter vi kampanjen din. Ekte mennesker bestemmer resten, og dashbordet viser hva vi har målt.",

    # Platform hubs
    "services_title": "Dette får vi til å vokse på {platform}",
    "services_lead": "Én pakke gir alt sammen, fra de samme ekte menneskene.",
    "teasers": {
        "audience": "Ekte mennesker som finner {profile} og velger å {follow}.",
        "likes": "Likes fra mennesker som liker {content}.",
        "views": "Visninger fra mennesker som velger å se, aldri fra skript.",
        "comments": "Kommentarer skrevet av ekte mennesker, med egne ord.",
    },
    "explore": "Utforsk",
    "in_package": "Med i hver pakke",
    "goals_title": "Flere måter å vokse på {platform}",
    "other_hubs_title": "Vi hjelper deg også å vokse på",
}
