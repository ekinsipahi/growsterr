"""Danish UI of the money pages (mirrors en/ui.py key by key).
{profile} profil/kanal and {handle} brugernavn/kanalhandle share a gender, so "din {profile}"
and "dit {handle}" read right on every platform; {content} is plural (dine opslag, dine videoer)."""

UI = {
    # Words that change with the platform or the service
    "audience": {"instagram": "følgere", "tiktok": "følgere", "youtube": "abonnenter"},
    "follow": {"instagram": "følge", "tiktok": "følge", "youtube": "abonnere"},
    "profile": {"instagram": "profil", "tiktok": "profil", "youtube": "kanal"},
    "handle": {"instagram": "brugernavn", "tiktok": "brugernavn", "youtube": "kanalhandle"},
    "content": {"instagram": "opslag", "tiktok": "videoer", "youtube": "videoer"},
    "service_names": {"followers": "Følgere", "subscribers": "Abonnenter", "likes": "Likes",
                      "views": "Visninger", "comments": "Kommentarer"},
    "service_words": {"followers": "følgere", "subscribers": "abonnenter", "likes": "likes",
                      "views": "visninger", "comments": "kommentarer"},

    # Page chrome
    "home": "Forside",
    "crumbs_label": "Brødkrummesti",
    "eyebrow": "{platform} · {service_name}",
    "eyebrow_hub": "Vækst på {platform}",
    "cta": "Start med {pick_name}",
    "cta_more": "Se alle pakker",
    "trust": ["Rigtige mennesker, aldrig bots", "Vi beder aldrig om din adgangskode", "Månedligt, opsig når som helst"],
    "product_name": "Vækstpakker til {platform}",
    "sticky_cta": "Kom i gang",

    # Packages
    "packages_title": "Vælg din pakke",
    "packages_lead": "Tre månedlige pakker. Nye {audience}, likes, visninger og kommentarer kommer sammen, fra de samme rigtige mennesker.",
    "packages_note": "Typiske intervaller pr. måned, ikke et fast antal: hver af dine nye {audience} er et rigtigt menneske, der har valgt at {follow}, så hver måned er lidt forskellig.",

    # What's included: the page's own service comes first, then the rest in this order.
    "included_title": "Det er inkluderet",
    "included_lead": "Hver pakke giver hele billedet, fra de samme rigtige mennesker.",
    "included_items": {
        "audience": ("Nye {audience}", "Rigtige mennesker, der har fundet din {profile} og valgt at {follow}. Typisk {starter_audience} om måneden med {starter_name}."),
        "likes": ("Likes fra de samme mennesker", "Typisk {starter_likes} om måneden med {starter_name}, på de {content}, de kan lide."),
        "comments": ("Kommentarer med deres egne ord", "Typisk {starter_comments} om måneden med {starter_name}. Skrevet af mennesker, aldrig efter manuskript."),
        "views": ("Visninger, der følger med", "De samme mennesker ser dine {content} af egen drift. Vi tæller ikke visninger på forhånd: hver visning er et menneske."),
        "days": ("Fordelt over 30 dage", "Lidt hver dag, fra det sted, du vælger. Aldrig det hele på én gang."),
        "dashboard": ("Dit dashboard", "Det, vi har målt, dag for dag: besøg fra din kampagne og de nye {audience}, de har givet."),
    },

    # How it works: the subscription, step by step
    "steps_title": "Sådan fungerer det",
    "steps_lead": "Et månedligt abonnement: du vælger pakken, vi kører kampagnen, rigtige mennesker bestemmer.",
    "steps": [
        ("Vælg en pakke", "{starter_name}, {rising_name} eller {pro_name}, betales månedligt. Opsig når som helst fra din konto."),
        ("Vi starter din kampagne", "Giv os dit {handle} på {platform}, og fortæl, hvor dit publikum skal komme fra. Vi beder aldrig om din adgangskode."),
        ("Rigtige mennesker finder din {profile}", "Hver dag bliver din {profile} vist for rigtige mennesker. De, der kan lide det, de ser, vælger selv at {follow}, like og kommentere."),
        ("Dit dashboard viser, hvad vi har målt", "Besøg fra din kampagne og de nye {audience}, de har givet, dag for dag. Målte tal, aldrig gæt."),
    ],

    # Real people vs bots / instant
    "compare_title": "Rigtige mennesker, ikke bots",
    "compare_lead": "Øjeblikkeligt betyder bots: intet rigtigt menneske vælger at {follow} sekunder efter en betaling.",
    "compare_cols": ("Hvad der ændrer sig", "Øjeblikkelige tjenester og bots", "Growsterr"),
    "compare": [
        ("Hvem de er", "Bots og falske profiler", "Rigtige mennesker, der valgte at {follow}"),
        ("Tempo", "Tusindvis på få minutter", "Lidt hver dag, hele måneden"),
        ("Likes og kommentarer", "Sælges separat, fra flere bots", "Fra de samme mennesker, i din pakke"),
        ("Din rækkevidde", "Falder stille og roligt: et publikum, der aldrig engagerer sig, fortæller {platform}, at dine {content} ikke er værd at vise", "Vokser med mennesker, der ser, liker og kommer igen"),
        ("Din adgangskode", "Bliver ofte efterspurgt", "Aldrig"),
        ("Det, du ser", "Et tal, der kan forsvinde ved næste oprydning", "Et dashboard med det, vi har målt"),
    ],

    # Quantity pages: how a monthly package gets you to the goal
    "quantity_title": "Sådan når du {quantity} {service}",
    "quantity_lead": "Vi sælger ikke en fast pakke med {quantity}. Rigtige mennesker bestemmer selv, så en månedlig pakke bringer dig derhen i et naturligt tempo.",
    "pace_title": "Typisk tempo med {pick_name}",
    "pace_month": "Måned {n}",
    "pace_goal": "Mål: {quantity}",
    "pace_note": "Typiske intervaller ud fra, hvad rigtige mennesker gør, aldrig et løfte. Nogle måneder giver mere, andre mindre.",
    "by_plan_title": "Tid til {quantity}, pr. pakke",
    "a_month": "{range} om måneden",
    "when_first": "typisk inden for den første måned",
    "when_about": "typisk omkring {n} måneder",
    "when_range": "typisk {low}–{high} måneder",
    "views_pace": "Visninger kommer fra de samme rigtige mennesker, der finder din {profile}, så vi tæller dem ikke på forhånd. {pick_name} er den pakke, der passer bedst til dette mål.",

    # FAQ, related pages, closing
    "faq_title": "Spørgsmål og svar",
    "related_title": "Udforsk mere",
    "related": {
        "platform": "Mere om {platform}",
        "platforms": "På andre platforme",
        "quantities": "Andre mål",
        "modifiers": "Andre måder at vokse på",
        "articles": "Læs videre",
        "hubs": "Voks med rigtige mennesker på",
    },
    # The tools a page can carry ("tool"): they run in the browser, nothing is sent.
    "tools": {
        "calculate": "Beregn",
        "followers": "Følgere",
        "avg_likes": "Gennemsnitlige likes pr. opslag",
        "avg_comments": "Gennemsnitlige kommentarer pr. opslag",
        "engagement_title": "Din engagementrate",
        "engagement_lead": "Hvor mange af dine følgere reagerer på et almindeligt opslag? Indtast tallene fra dine seneste opslag.",
        "engagement_result": "Din engagementrate er {rate} %.",
        "engagement_note": "Raten stiger, når de mennesker, der følger dig, faktisk går op i dine opslag. Følgere, der aldrig reagerer, trækker den ned, uanset hvor mange de er.",
        "growth_title": "Hvor lang tid til dit mål?",
        "growth_lead": "Indtast, hvor du er, og hvor du vil hen. Vi regner det ud fra hver pakkes typiske interval pr. måned.",
        "current": "Følgere i dag",
        "goal": "Dit mål",
        "when_first": "typisk inden for den første måned",
        "when_range": "typisk {low}–{high} måneder",
        "when_about": "omkring {n} måneder",
        "reached": "Du er der allerede.",
        "growth_note": "Typiske intervaller, ikke et løfte: rigtige mennesker bestemmer selv, om de vil følge.",
    },
    # Eyebrow above the headline of pages outside the platform x service grid (by "kind").
    "article_eyebrows": {
        "guide": "Guide",
        "alternative": "Sammenligning",
        "payment": "Betaling",
        "agency": "Vækstbureau",
        "tool": "Værktøj",
        "intent": "Ærligt svar",
    },
    "cta_title": "Klar til at vokse på {platform}?",
    "cta_text": "Vælg en pakke, så starter vi din kampagne. Rigtige mennesker bestemmer resten, og dit dashboard viser, hvad vi har målt.",

    # Platform hubs
    "services_title": "Det får vi til at vokse på {platform}",
    "services_lead": "Én pakke giver det hele, fra de samme rigtige mennesker.",
    "teasers": {
        "audience": "Rigtige mennesker, der finder din {profile} og vælger at {follow}.",
        "likes": "Likes fra mennesker, der kan lide dine {content}.",
        "views": "Visninger fra mennesker, der vælger at se med, aldrig fra scripts.",
        "comments": "Kommentarer skrevet af rigtige mennesker, med deres egne ord.",
    },
    "explore": "Udforsk",
    "in_package": "Med i hver pakke",
    "goals_title": "Flere måder at vokse på {platform}",
    "other_hubs_title": "Vi hjælper dig også med at vokse på",
}
