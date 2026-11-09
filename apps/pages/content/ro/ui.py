"""Romanian UI of the money pages: section titles and the blocks every page shares (mirrors en/ui.py).

Word forms, chosen so every sentence below stays grammatical:
    {audience} urmăritori/abonați (unarticulated plural: "{audience} noi", "de {audience}")
    {follow} te urmărească/se aboneze (always after "să")
    {profile} profilul/canalul (articulated: "{profile} tău", "îți descoperă {profile}")
    {handle} numele de utilizator/handle-ul canalului · {content} postările/videoclipurile ("{content} tale")
    {service} after "{quantity} de"
"""

UI = {
    # Words that change with the platform or the service
    "audience": {"instagram": "urmăritori", "tiktok": "urmăritori", "youtube": "abonați"},
    "follow": {"instagram": "te urmărească", "tiktok": "te urmărească", "youtube": "se aboneze"},
    "profile": {"instagram": "profilul", "tiktok": "profilul", "youtube": "canalul"},
    "handle": {"instagram": "numele de utilizator", "tiktok": "numele de utilizator", "youtube": "handle-ul canalului"},
    "content": {"instagram": "postările", "tiktok": "videoclipurile", "youtube": "videoclipurile"},
    "service_names": {"followers": "Urmăritori", "subscribers": "Abonați", "likes": "Like-uri",
                      "views": "Vizualizări", "comments": "Comentarii"},
    "service_words": {"followers": "urmăritori", "subscribers": "abonați", "likes": "like-uri",
                      "views": "vizualizări", "comments": "comentarii"},

    # Page chrome
    "home": "Acasă",
    "crumbs_label": "Fir de navigare",
    "eyebrow": "{platform} · {service_name}",
    "eyebrow_hub": "Creștere pe {platform}",
    "cta": "Începe cu {pick_name}",
    "cta_more": "Vezi toate pachetele",
    "trust": ["Oameni reali, niciodată boți", "Nu îți cerem niciodată parola", "Lunar, anulezi oricând"],
    "product_name": "Pachete de creștere pe {platform}",
    "sticky_cta": "Începe",

    # Packages
    "packages_title": "Alege-ți pachetul",
    "packages_lead": "Trei pachete lunare. Fiecare aduce {audience} noi, like-uri, vizualizări și comentarii, toate de la aceiași oameni reali.",
    "packages_note": "Intervale lunare obișnuite, nu un număr fix: fiecare dintre noii tăi {audience} este un om real care a ales să {follow}, așa că fiecare lună e puțin diferită.",

    # What's included: the page's own service comes first, then the rest in this order.
    "included_title": "Ce primești",
    "included_lead": "Fiecare pachet aduce totul la un loc, de la aceiași oameni reali.",
    "included_items": {
        "audience": ("Noi {audience}", "Oameni reali care ți-au descoperit {profile} și au ales să {follow}. De obicei {starter_audience} pe lună cu {starter_name}."),
        "likes": ("Like-uri de la aceiași oameni", "De obicei {starter_likes} pe lună cu {starter_name}, la {content} care le plac."),
        "comments": ("Comentarii scrise cu vorbele lor", "De obicei {starter_comments} pe lună cu {starter_name}. Scrise de oameni, niciodată după un scenariu."),
        "views": ("Vizualizări care vin la pachet", "Aceiași oameni se uită singuri la {content} tale. Nu numărăm vizualizările dinainte: fiecare vine de la un om."),
        "days": ("Repartizat pe 30 de zile", "Câte puțin în fiecare zi, din locația pe care o alegi. Niciodată totul deodată."),
        "dashboard": ("Panoul tău", "Ce am măsurat, zi de zi: vizitele din campania ta și noii {audience} pe care i-au adus."),
    },

    # How it works: the subscription, step by step
    "steps_title": "Cum funcționează",
    "steps_lead": "Un abonament lunar: tu alegi pachetul, noi derulăm campania, oamenii reali decid.",
    "steps": [
        ("Alegi un pachet", "{starter_name}, {rising_name} sau {pro_name}, cu plată lunară. Anulezi oricând din contul tău."),
        ("Pornim campania ta", "Spune-ne {handle} de pe {platform} și de unde să vină publicul tău. Nu îți cerem niciodată parola."),
        ("Oameni reali îți descoperă {profile}", "În fiecare zi, {profile} tău le este arătat unor oameni reali. Cei cărora le place ce văd aleg singuri să {follow}, să dea like și să comenteze."),
        ("Panoul îți arată ce am măsurat", "Vizitele din campania ta și noii {audience} pe care i-au adus, zi de zi. Cifre măsurate, niciodată presupuneri."),
    ],

    # Real people vs bots / instant
    "compare_title": "Oameni reali, nu boți",
    "compare_lead": "Instant înseamnă boți: niciun om real nu alege să {follow} la câteva secunde după o plată.",
    "compare_cols": ("Ce se schimbă", "Servicii instant și cu boți", "Growsterr"),
    "compare": [
        ("Cine sunt", "Boți și profiluri false", "Oameni reali care au ales să {follow}"),
        ("Viteza", "Mii în câteva minute", "Câte puțin în fiecare zi, toată luna"),
        ("Like-uri și comentarii", "Vândute separat, de la alți boți", "De la aceiași oameni, incluse în pachet"),
        ("Acoperirea ta", "Scade pe tăcute: un public care nu interacționează îi spune lui {platform} că {content} tale nu merită arătate", "Crește cu oameni care se uită, dau like și revin"),
        ("Parola ta", "Adesea cerută", "Niciodată"),
        ("Ce vezi", "Un număr care poate dispărea la următoarea curățenie", "Un panou cu ce am măsurat"),
    ],

    # Quantity pages: how a monthly package gets you to the goal
    "quantity_title": "Cum ajungi la {quantity} de {service}",
    "quantity_lead": "Nu vindem un pachet fix de {quantity}. Oamenii reali decid singuri, așa că un pachet lunar te duce acolo într-un ritm natural.",
    "pace_title": "Ritmul obișnuit cu {pick_name}",
    "pace_month": "Luna {n}",
    "pace_goal": "Obiectiv: {quantity}",
    "pace_note": "Intervale obișnuite, din ce fac oamenii reali, niciodată o promisiune. Unele luni aduc mai mult, altele mai puțin.",
    "by_plan_title": "Timpul până la {quantity}, pe pachete",
    "a_month": "{range} pe lună",
    "when_first": "de obicei în prima lună",
    "when_about": "de obicei cam {n} luni",
    "when_range": "de obicei {low}–{high} luni",
    "views_pace": "Vizualizările vin de la aceiași oameni reali care îți descoperă {profile}, așa că nu le numărăm dinainte. {pick_name} este pachetul care se potrivește cel mai bine acestui obiectiv.",

    # FAQ, related pages, closing
    "faq_title": "Întrebări și răspunsuri",
    "related_title": "Explorează mai departe",
    "related": {
        "platform": "Mai multe despre {platform}",
        "platforms": "Pe alte platforme",
        "quantities": "Alte obiective",
        "modifiers": "Alte moduri de a crește",
        "articles": "Citește în continuare",
        "hubs": "Crește cu oameni reali pe",
    },
    # The tools a page can carry ("tool"): they run in the browser, nothing is sent.
    "tools": {
        "calculate": "Calculează",
        "followers": "Urmăritori",
        "avg_likes": "Like-uri în medie pe postare",
        "avg_comments": "Comentarii în medie pe postare",
        "engagement_title": "Rata ta de interacțiune",
        "engagement_lead": "Câți dintre urmăritorii tăi reacționează la o postare obișnuită. Introdu cifrele de la ultimele tale postări.",
        "engagement_result": "Rata ta de interacțiune este {rate}%.",
        "engagement_note": "Rata crește atunci când oamenilor care te urmăresc chiar le pasă de postările tale. Urmăritorii care nu reacționează niciodată o scad, oricât de mulți ar fi.",
        "growth_title": "Cât durează până la obiectiv?",
        "growth_lead": "Introdu unde ești acum și unde vrei să ajungi. Calculăm pe baza intervalului lunar obișnuit al fiecărui pachet.",
        "current": "Urmăritori azi",
        "goal": "Obiectivul tău",
        "when_first": "de obicei în prima lună",
        "when_range": "de obicei {low}–{high} luni",
        "when_about": "cam {n} luni",
        "reached": "Ai ajuns deja acolo.",
        "growth_note": "Intervale obișnuite, nu o promisiune: oamenii reali decid singuri dacă te urmăresc.",
    },
    # Eyebrow above the headline of pages outside the platform x service grid (by "kind").
    "article_eyebrows": {
        "guide": "Ghid",
        "alternative": "Comparație",
        "payment": "Plăți",
        "agency": "Agenție de creștere",
        "tool": "Instrument",
        "intent": "Răspuns direct",
    },
    "cta_title": "Gata să crești pe {platform}?",
    "cta_text": "Alege un pachet și pornim campania ta. Oamenii reali decid restul, iar panoul îți arată ce am măsurat.",

    # Platform hubs
    "services_title": "Ce creștem pe {platform}",
    "services_lead": "Un singur pachet aduce totul, de la aceiași oameni reali.",
    "teasers": {
        "audience": "Oameni reali care îți descoperă {profile} și aleg să {follow}.",
        "likes": "Like-uri de la oamenii cărora le plac {content} tale.",
        "views": "Vizualizări de la oameni care aleg să se uite, niciodată de la scripturi.",
        "comments": "Comentarii scrise de oameni reali, cu vorbele lor.",
    },
    "explore": "Explorează",
    "in_package": "În fiecare pachet",
    "goals_title": "Mai multe moduri de a crește pe {platform}",
    "other_hubs_title": "Creștem și pe",
}
