"""Hungarian UI of the money pages (mirrors en/ui.py key by key).

Hungarian suffixes follow vowel harmony, so no placeholder ever takes a suffix: the word tables hold
complete forms, and every sentence uses each one in exactly that form.
    {audience} nominative plural (követők / feliratkozók) · {follow} a noun used with "a … mellett"
    (követés / feliratkozás) · {profile} {handle} {content} accusative, "your" (profilodat, videóidat...)
    {service} accusative singular, right after {quantity} ("1 000 követőt")
{platform} never follows a bare a/az: it stands alone or opens a hyphenated compound ("{platform}-növekedés").
"""

UI = {
    # Words that change with the platform or the service
    "audience": {"instagram": "követők", "tiktok": "követők", "youtube": "feliratkozók"},
    "follow": {"instagram": "követés", "tiktok": "követés", "youtube": "feliratkozás"},
    "profile": {"instagram": "profilodat", "tiktok": "profilodat", "youtube": "csatornádat"},
    "handle": {"instagram": "felhasználónevedet", "tiktok": "felhasználónevedet", "youtube": "csatornád azonosítóját"},
    "content": {"instagram": "posztjaidat", "tiktok": "videóidat", "youtube": "videóidat"},
    "service_names": {"followers": "Követők", "subscribers": "Feliratkozók", "likes": "Lájkok",
                      "views": "Megtekintések", "comments": "Kommentek"},
    "service_words": {"followers": "követőt", "subscribers": "feliratkozót", "likes": "lájkot",
                      "views": "megtekintést", "comments": "kommentet"},

    # Page chrome
    "home": "Főoldal",
    "crumbs_label": "Navigációs útvonal",
    "eyebrow": "{platform} · {service_name}",
    "eyebrow_hub": "{platform}-növekedés",
    "cta": "Kezdd a {pick_name} csomaggal",
    "cta_more": "Az összes csomag",
    "trust": ["Valódi emberek, soha nem botok", "A jelszavadat soha nem kérjük el", "Havi díj, bármikor lemondható"],
    "product_name": "{platform}-növekedési csomagok",
    "sticky_cta": "Kezdés",

    # Packages
    "packages_title": "Válaszd ki a csomagod",
    "packages_lead": "Három havi csomag. Új {audience}, lájkok, megtekintések és kommentek együtt, ugyanazoktól a valódi emberektől.",
    "packages_note": "Jellemző havi tartományok, nem fix mennyiség: az új {audience} mindegyike valódi ember, aki maga döntött a {follow} mellett, így minden hónap kicsit más.",

    # What's included: the page's own service comes first, then the rest in this order.
    "included_title": "Ami benne van",
    "included_lead": "Minden csomag a teljes képet adja, ugyanazoktól a valódi emberektől.",
    "included_items": {
        "audience": ("Új {audience}", "Valódi emberek, akik felfedezték a {profile}, és a {follow} mellett döntöttek. A {starter_name} csomaggal havonta jellemzően {starter_audience}."),
        "likes": ("Lájkok ugyanazoktól az emberektől", "A {starter_name} csomaggal havonta jellemzően {starter_likes}, olyanoktól, akik szívesen nézik a {content}."),
        "comments": ("Kommentek a saját szavaikkal", "A {starter_name} csomaggal havonta jellemzően {starter_comments}. Emberek írják, soha nem előre megírt szöveg."),
        "views": ("Megtekintések, amelyek vele járnak", "Ugyanezek az emberek maguktól nézik meg a {content}. A megtekintéseket nem számoljuk előre: mindegyik mögött egy ember áll."),
        "days": ("30 napra elosztva", "Minden nap egy kicsit, az általad választott helyről. Soha nem egyszerre."),
        "dashboard": ("A te irányítópultod", "Amit mértünk, napról napra: a kampányodból érkező látogatások és az általuk hozott új {audience}."),
    },

    # How it works: the subscription, step by step
    "steps_title": "Így működik",
    "steps_lead": "Havi előfizetés: te választod a csomagot, mi futtatjuk a kampányt, valódi emberek döntenek.",
    "steps": [
        ("Válassz csomagot", "{starter_name}, {rising_name} vagy {pro_name}, havi számlázással. A fiókodból bármikor lemondhatod."),
        ("Elindítjuk a kampányodat", "Add meg a {handle}, és azt, hogy honnan érkezzen a közönséged. A jelszavadat soha nem kérjük el."),
        ("Valódi emberek fedezik fel a {profile}", "Minden nap megmutatjuk a {profile} valódi embereknek. Akinek tetszik, amit lát, magától dönt a {follow} mellett, lájkol és kommentel."),
        ("Az irányítópult megmutatja, mit mértünk", "A kampányodból érkező látogatások és az általuk hozott új {audience}, napról napra. Mért számok, soha nem találgatás."),
    ],

    # Real people vs bots / instant
    "compare_title": "Valódi emberek, nem botok",
    "compare_lead": "Az „azonnali” botokat jelent: egyetlen valódi ember sem dönt a {follow} mellett másodpercekkel a fizetés után.",
    "compare_cols": ("Miben más", "Azonnali és bot szolgáltatások", "Growsterr"),
    "compare": [
        ("Kik ők", "Botok és hamis profilok", "Valódi emberek, akik a {follow} mellett döntöttek"),
        ("Tempó", "Ezrek percek alatt", "Minden nap egy kicsit, egész hónapban"),
        ("Lájkok és kommentek", "Külön árulják, még több bottól", "Ugyanazoktól az emberektől, a csomagod részeként"),
        ("Az elérésed", "Csendben csökken: a soha nem reagáló közönség azt jelzi az algoritmusnak, hogy a {content} nem érdemes megmutatni", "Nő, mert olyan emberek jönnek, akik néznek, lájkolnak és visszatérnek"),
        ("A jelszavad", "Gyakran elkérik", "Soha"),
        ("Amit látsz", "Egy szám, amely a következő tisztításnál eltűnhet", "Irányítópult arról, amit mértünk"),
    ],

    # Quantity pages: how a monthly package gets you to the goal
    "quantity_title": "Így gyűjtesz össze {quantity} {service}",
    "quantity_lead": "Nem árulunk fix, {quantity} darabos csomagot. Valódi emberek döntenek maguktól, ezért egy havi csomag természetes tempóban visz el a célig.",
    "pace_title": "Jellemző tempó a {pick_name} csomaggal",
    "pace_month": "{n}. hónap",
    "pace_goal": "Cél: {quantity}",
    "pace_note": "Jellemző tartományok abból, amit valódi emberek tesznek, soha nem ígéret. Van hónap, amely többet hoz, és van, amely kevesebbet.",
    "by_plan_title": "Idő a célig ({quantity}), csomagonként",
    "a_month": "havonta {range}",
    "when_first": "általában már az első hónapban",
    "when_about": "általában kb. {n} hónap",
    "when_range": "általában {low}–{high} hónap",
    "views_pace": "A megtekintések ugyanazoktól a valódi emberektől jönnek, akik felfedezik a {profile}, ezért előre nem számoljuk őket. Ehhez a célhoz a {pick_name} csomag illik a legjobban.",

    # FAQ, related pages, closing
    "faq_title": "Kérdések és válaszok",
    "related_title": "Fedezz fel még többet",
    "related": {
        "platform": "Még több: {platform}",
        "platforms": "Más platformokon",
        "quantities": "Más célok",
        "modifiers": "További utak a növekedéshez",
        "articles": "Olvasd tovább",
        "hubs": "Növekedj valódi emberekkel itt:",
    },
    # The tools a page can carry ("tool"): they run in the browser, nothing is sent.
    "tools": {
        "calculate": "Számold ki",
        "followers": "Követők",
        "avg_likes": "Átlagos lájkszám posztonként",
        "avg_comments": "Átlagos kommentszám posztonként",
        "engagement_title": "Az interakciós arányod",
        "engagement_lead": "A követőid közül hányan reagálnak egy átlagos posztra. Add meg az utolsó néhány posztod számait.",
        "engagement_result": "Az interakciós arányod: {rate}%.",
        "engagement_note": "Az arány akkor nő, ha a követőidet tényleg érdeklik a posztjaid. A soha nem reagáló követők lehúzzák, bármennyien is vannak.",
        "growth_title": "Mennyi idő a célodig?",
        "growth_lead": "Add meg, hol tartasz most, és hová szeretnél eljutni. Az egyes csomagok jellemző havi tartományából számoljuk ki.",
        "current": "Követők ma",
        "goal": "A célod",
        "when_first": "általában már az első hónapban",
        "when_range": "általában {low}–{high} hónap",
        "when_about": "kb. {n} hónap",
        "reached": "Már el is érted.",
        "growth_note": "Jellemző tartományok, nem ígéret: valódi emberek maguk döntenek a követésről.",
    },
    # Eyebrow above the headline of pages outside the platform x service grid (by "kind").
    "article_eyebrows": {
        "guide": "Útmutató",
        "alternative": "Összehasonlítás",
        "payment": "Fizetés",
        "agency": "Növekedési ügynökség",
        "tool": "Eszköz",
        "intent": "Egyenes válasz",
    },
    "cta_title": "Indulhat a valódi {platform}-növekedés?",
    "cta_text": "Válassz csomagot, és elindítjuk a kampányodat. A többit valódi emberek döntik el, az irányítópultod pedig megmutatja, mit mértünk.",

    # Platform hubs
    "services_title": "{platform}-növekedés: ezt kapod",
    "services_lead": "Egyetlen csomag mindezt elhozza, ugyanazoktól a valódi emberektől.",
    "teasers": {
        "audience": "Valódi emberek, akik felfedezik a {profile}, és a {follow} mellett döntenek.",
        "likes": "Lájkok azoktól, akik szívesen nézik a {content}.",
        "views": "Megtekintések olyanoktól, akik maguk döntenek a nézés mellett, soha nem szkriptektől.",
        "comments": "Kommentek valódi emberektől, a saját szavaikkal.",
    },
    "explore": "Felfedezem",
    "in_package": "Minden csomagban benne van",
    "goals_title": "Még több út a valódi {platform}-növekedéshez",
    "other_hubs_title": "Máshol is segítünk",
}
