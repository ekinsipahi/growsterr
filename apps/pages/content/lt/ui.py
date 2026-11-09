"""Lithuanian UI of the money pages (polite "jūs"). Mirrors en/ui.py key by key.

Grammar notes for the placeholders (one case each, every template below uses that case):
    {platform} stays uninflected after a generic noun ("platformoje {platform}") or as an
        attribute ("{platform} augimas").
    {audience} nominative plural ("Nauji {audience}", "visi jūsų nauji {audience} yra...").
    {follow} infinitive after "nuspręsti" ("nusprendė {follow}"), never under a negated verb.
    {profile}, {handle} accusative, objects of positive verbs only ("atranda jūsų {profile}").
    {content} accusative plural, objects of positive verbs only ("žiūri jūsų {content}").
    {service} genitive plural, the form after a round number ("{quantity} {service}").
"""

UI = {
    # Words that change with the platform or the service
    "audience": {"instagram": "sekėjai", "tiktok": "sekėjai", "youtube": "prenumeratoriai"},
    "follow": {"instagram": "jus sekti", "tiktok": "jus sekti", "youtube": "prenumeruoti"},
    "profile": {"instagram": "profilį", "tiktok": "profilį", "youtube": "kanalą"},
    "handle": {"instagram": "naudotojo vardą", "tiktok": "naudotojo vardą", "youtube": "kanalo identifikatorių"},
    "content": {"instagram": "įrašus", "tiktok": "vaizdo įrašus", "youtube": "vaizdo įrašus"},
    "service_names": {"followers": "Sekėjai", "subscribers": "Prenumeratoriai", "likes": "Patiktukai",
                      "views": "Peržiūros", "comments": "Komentarai"},
    "service_words": {"followers": "sekėjų", "subscribers": "prenumeratorių", "likes": "patiktukų",
                      "views": "peržiūrų", "comments": "komentarų"},

    # Page chrome
    "home": "Pradžia",
    "crumbs_label": "Naršymo kelias",
    "eyebrow": "{platform} · {service_name}",
    "eyebrow_hub": "{platform} augimas",
    "cta": "Pradėti su {pick_name}",
    "cta_more": "Visi paketai",
    "trust": ["Tikri žmonės, niekada botai", "Niekada neprašome jūsų slaptažodžio", "Kas mėnesį, atšaukti galima bet kada"],
    "product_name": "{platform} augimo paketai",
    "sticky_cta": "Pradėti",

    # Packages
    "packages_title": "Pasirinkite paketą",
    "packages_lead": "Trys mėnesio paketai. Nauji {audience}, patiktukai, peržiūros ir komentarai ateina kartu, iš tų pačių tikrų žmonių.",
    "packages_note": "Tipiniai mėnesio intervalai, o ne fiksuotas kiekis: visi jūsų nauji {audience} yra tikri žmonės, kurie patys nusprendė {follow}, todėl kiekvienas mėnuo šiek tiek skiriasi.",

    # What's included: the page's own service comes first, then the rest in this order.
    "included_title": "Kas įskaičiuota",
    "included_lead": "Kiekvienas paketas suteikia visą vaizdą, iš tų pačių tikrų žmonių.",
    "included_items": {
        "audience": ("Nauji {audience}", "Tikri žmonės, kurie atrado jūsų {profile} ir nusprendė {follow}. Su {starter_name} paprastai {starter_audience} per mėnesį."),
        "likes": ("Patiktukai iš tų pačių žmonių", "Su {starter_name} paprastai {starter_likes} per mėnesį, iš žmonių, kuriems patinka žiūrėti jūsų {content}."),
        "comments": ("Komentarai jų pačių žodžiais", "Su {starter_name} paprastai {starter_comments} per mėnesį. Juos rašo žmonės, niekada ne scenarijai."),
        "views": ("Peržiūros ateina kartu", "Tie patys žmonės patys žiūri jūsų {content}. Peržiūrų iš anksto neskaičiuojame: kiekviena jų yra žmogus."),
        "days": ("Paskirstyta per 30 dienų", "Po truputį kasdien, iš jūsų pasirinktos vietos. Niekada ne viskas iš karto."),
        "dashboard": ("Jūsų skydelis", "Ką išmatavome, diena po dienos: jūsų kampanijos apsilankymai ir nauji {audience}, kuriuos jie atvedė."),
    },

    # How it works: the subscription, step by step
    "steps_title": "Kaip tai veikia",
    "steps_lead": "Mėnesinė prenumerata: jūs pasirenkate paketą, mes vykdome kampaniją, tikri žmonės sprendžia.",
    "steps": [
        ("Pasirinkite paketą", "{starter_name}, {rising_name} arba {pro_name}, mokama kas mėnesį. Atšaukti galite bet kada savo paskyroje."),
        ("Pradedame jūsų kampaniją", "Nurodykite savo {platform} {handle} ir iš kur turėtų būti jūsų auditorija. Niekada neprašome jūsų slaptažodžio."),
        ("Tikri žmonės atranda jūsų {profile}", "Kasdien rodome jūsų {profile} tikriems žmonėms. Tie, kuriems patinka tai, ką mato, patys nusprendžia {follow}, paspausti „patinka“ ir komentuoti."),
        ("Skydelis rodo, ką išmatavome", "Jūsų kampanijos apsilankymai ir nauji {audience}, kuriuos jie atvedė, diena po dienos. Išmatuoti skaičiai, niekada ne spėlionės."),
    ],

    # Real people vs bots / instant
    "compare_title": "Tikri žmonės, ne botai",
    "compare_lead": "Akimirksniu reiškia botus: tikras žmogus nusprendžia {follow} tik pamatęs jūsų turinį, o ne praėjus kelioms sekundėms po mokėjimo.",
    "compare_cols": ("Kas keičiasi", "Momentinės ir botų paslaugos", "Growsterr"),
    "compare": [
        ("Kas jie", "Botai ir netikri profiliai", "Tikri žmonės, kurie nusprendė {follow}"),
        ("Greitis", "Tūkstančiai per kelias minutes", "Po truputį kasdien, visą mėnesį"),
        ("Patiktukai ir komentarai", "Parduodami atskirai, iš dar daugiau botų", "Iš tų pačių žmonių, jūsų pakete"),
        ("Jūsų pasiekiamumas", "Tyliai krenta: auditorija, kuri niekada nereaguoja, signalizuoja platformai {platform}, kad jūsų {content} verta rodyti rečiau", "Auga su žmonėmis, kurie žiūri, spaudžia „patinka“ ir grįžta"),
        ("Jūsų slaptažodis", "Dažnai prašomas", "Niekada"),
        ("Ką matote", "Skaičių, kuris gali dingti per kitą valymą", "Skydelį su tuo, ką išmatavome"),
    ],

    # Quantity pages: how a monthly package gets you to the goal
    "quantity_title": "Kaip pasiekti {quantity} {service}",
    "quantity_lead": "Neparduodame fiksuoto paketo po {quantity}. Tikri žmonės sprendžia patys, todėl mėnesio paketas jus ten nuveda natūraliu tempu.",
    "pace_title": "Tipinis tempas su {pick_name}",
    "pace_month": "Mėnuo {n}",
    "pace_goal": "Tikslas: {quantity}",
    "pace_note": "Tipiniai intervalai pagal tai, ką daro tikri žmonės, o ne pažadas. Vieni mėnesiai atneša daugiau, kiti mažiau.",
    "by_plan_title": "Laikas iki {quantity} pagal paketą",
    "a_month": "{range} per mėnesį",
    "when_first": "paprastai jau per pirmąjį mėnesį",
    "when_about": "paprastai apie {n} mėn.",
    "when_range": "paprastai {low}–{high} mėn.",
    "views_pace": "Peržiūros ateina iš tų pačių tikrų žmonių, kurie atranda jūsų {profile}, todėl jų iš anksto neskaičiuojame. Šiam tikslui geriausiai tinka {pick_name}.",

    # FAQ, related pages, closing
    "faq_title": "Klausimai ir atsakymai",
    "related_title": "Sužinokite daugiau",
    "related": {
        "platform": "Daugiau apie {platform}",
        "platforms": "Kitose platformose",
        "quantities": "Kiti tikslai",
        "modifiers": "Kiti būdai augti",
        "articles": "Skaitykite toliau",
        "hubs": "Augite su tikrais žmonėmis",
    },
    # The tools a page can carry ("tool"): they run in the browser, nothing is sent.
    "tools": {
        "calculate": "Apskaičiuoti",
        "followers": "Sekėjai",
        "avg_likes": "Vidutiniškai patiktukų per įrašą",
        "avg_comments": "Vidutiniškai komentarų per įrašą",
        "engagement_title": "Jūsų įsitraukimo rodiklis",
        "engagement_lead": "Kokia dalis jūsų sekėjų reaguoja į įprastą įrašą. Įveskite skaičius iš kelių paskutinių įrašų.",
        "engagement_result": "Jūsų įsitraukimo rodiklis yra {rate} %.",
        "engagement_note": "Rodiklis kyla, kai jus sekantiems žmonėms jūsų įrašai iš tiesų rūpi. Sekėjai, kurie niekada nereaguoja, jį mažina, kad ir kiek jų būtų.",
        "growth_title": "Kiek laiko iki jūsų tikslo?",
        "growth_lead": "Įveskite, kur esate dabar ir kur norite būti. Apskaičiuojame pagal kiekvieno paketo tipinį mėnesio intervalą.",
        "current": "Sekėjų šiandien",
        "goal": "Jūsų tikslas",
        "when_first": "paprastai jau per pirmąjį mėnesį",
        "when_range": "paprastai {low}–{high} mėn.",
        "when_about": "apie {n} mėn.",
        "reached": "Tikslas jau pasiektas.",
        "growth_note": "Tipiniai intervalai, o ne pažadas: tikri žmonės patys sprendžia, ar jus sekti.",
    },
    # Eyebrow above the headline of pages outside the platform x service grid (by "kind").
    "article_eyebrows": {
        "guide": "Gidas",
        "alternative": "Palyginimas",
        "payment": "Mokėjimai",
        "agency": "Augimo agentūra",
        "tool": "Įrankis",
        "intent": "Tiesus atsakymas",
    },
    "cta_title": "Pasiruošę augti platformoje {platform}?",
    "cta_text": "Pasirinkite paketą, ir mes pradėsime jūsų kampaniją. Visa kita nusprendžia tikri žmonės, o skydelis rodo, ką išmatavome.",

    # Platform hubs
    "services_title": "Ką auginame platformoje {platform}",
    "services_lead": "Vienas paketas atneša viską, iš tų pačių tikrų žmonių.",
    "teasers": {
        "audience": "Tikri žmonės, kurie atranda jūsų {profile} ir nusprendžia {follow}.",
        "likes": "Patiktukai iš žmonių, kuriems patinka žiūrėti jūsų {content}.",
        "views": "Peržiūros iš žmonių, kurie patys nusprendžia žiūrėti, niekada ne iš scenarijų.",
        "comments": "Komentarai, kuriuos tikri žmonės rašo savais žodžiais.",
    },
    "explore": "Peržiūrėti",
    "in_package": "Kiekviename pakete",
    "goals_title": "Daugiau būdų augti platformoje {platform}",
    "other_hubs_title": "Taip pat auginame",
}
