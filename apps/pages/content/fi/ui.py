"""Finnish UI of the money pages (mirrors en/ui.py key by key).

The word placeholders are chosen so every sentence stays grammatical on every platform:
{audience} nominative plural (seuraajat/tilaajat), {follow} infinitive with its object
(seurata sinua/tilata kanavasi), {profile} and {content} possessive forms (profiilisi,
julkaisusi), {handle} joins {platform} as a compound ({platform}-käyttäjänimesi), {service}
is the partitive that follows a number (1 000 seuraajaa). Package names take " -paketilla".
"""

UI = {
    # Words that change with the platform or the service
    "audience": {"instagram": "seuraajat", "tiktok": "seuraajat", "youtube": "tilaajat"},
    "follow": {"instagram": "seurata sinua", "tiktok": "seurata sinua", "youtube": "tilata kanavasi"},
    "profile": {"instagram": "profiilisi", "tiktok": "profiilisi", "youtube": "kanavasi"},
    "handle": {"instagram": "käyttäjänimesi", "tiktok": "käyttäjänimesi", "youtube": "kahvasi"},
    "content": {"instagram": "julkaisusi", "tiktok": "videosi", "youtube": "videosi"},
    "service_names": {"followers": "Seuraajat", "subscribers": "Tilaajat", "likes": "Tykkäykset",
                      "views": "Katselukerrat", "comments": "Kommentit"},
    "service_words": {"followers": "seuraajaa", "subscribers": "tilaajaa", "likes": "tykkäystä",
                      "views": "katselukertaa", "comments": "kommenttia"},

    # Page chrome
    "home": "Etusivu",
    "crumbs_label": "Murupolku",
    "eyebrow": "{platform} · {service_name}",
    "eyebrow_hub": "{platform}-kasvu",
    "cta": "Aloita {pick_name} -paketilla",
    "cta_more": "Katso kaikki paketit",
    "trust": ["Oikeita ihmisiä, ei koskaan botteja", "Emme koskaan kysy salasanaasi", "Kuukausittain, peru milloin tahansa"],
    "product_name": "{platform}-kasvupaketit",
    "sticky_cta": "Aloita",

    # Packages
    "packages_title": "Valitse pakettisi",
    "packages_lead": "Kolme kuukausipakettia. Uudet {audience}, tykkäykset, katselukerrat ja kommentit tulevat yhdessä, samoilta oikeilta ihmisiltä.",
    "packages_note": "Tyypillisiä kuukausivaihteluvälejä, ei kiinteä määrä: uudet {audience} ovat kaikki oikeita ihmisiä, jotka ovat päättäneet {follow}, joten jokainen kuukausi on vähän erilainen.",

    # What's included: the page's own service comes first, then the rest in this order.
    "included_title": "Mitä pakettiin kuuluu",
    "included_lead": "Jokainen paketti tuo koko kokonaisuuden, samoilta oikeilta ihmisiltä.",
    "included_items": {
        "audience": ("Uudet {audience}", "Oikeita ihmisiä, jotka löysivät {profile} ja päättivät {follow}. Tyypillisesti {starter_audience} kuukaudessa {starter_name} -paketilla."),
        "likes": ("Tykkäykset samoilta ihmisiltä", "Tyypillisesti {starter_likes} kuukaudessa {starter_name} -paketilla, kun samat ihmiset näkevät {content} ja pitävät niistä."),
        "comments": ("Kommentit omin sanoin", "Tyypillisesti {starter_comments} kuukaudessa {starter_name} -paketilla. Ihmisten kirjoittamia, ei koskaan valmiita tekstejä."),
        "views": ("Katselukerrat tulevat mukana", "Samat ihmiset katsovat {content} omasta halustaan. Emme laske katselukertoja etukäteen: jokainen niistä on ihminen."),
        "days": ("Jaettuna 30 päivälle", "Vähän joka päivä, valitsemaltasi alueelta. Ei koskaan kaikkea kerralla."),
        "dashboard": ("Hallintapaneelisi", "Mitä mittasimme, päivä päivältä: kampanjasi tuomat käynnit ja niiden tuomat uudet {audience}."),
    },

    # How it works: the subscription, step by step
    "steps_title": "Näin se toimii",
    "steps_lead": "Kuukausitilaus: sinä valitset paketin, me hoidamme kampanjan, oikeat ihmiset päättävät.",
    "steps": [
        ("Valitse paketti", "{starter_name}, {rising_name} tai {pro_name}, laskutus kuukausittain. Peru milloin tahansa tililtäsi."),
        ("Aloitamme kampanjasi", "Kerro meille {platform}-{handle} ja mistä yleisösi pitäisi tulla. Emme koskaan kysy salasanaasi."),
        ("Oikeat ihmiset löytävät {profile}", "Joka päivä {profile} näytetään oikeille ihmisille. Ne, jotka pitävät näkemästään, päättävät itse {follow}, tykätä ja kommentoida."),
        ("Hallintapaneeli näyttää, mitä mittasimme", "Kampanjasi tuomat käynnit ja niiden tuomat uudet {audience}, päivä päivältä. Mitattuja lukuja, ei koskaan arvauksia."),
    ],

    # Real people vs bots / instant
    "compare_title": "Oikeita ihmisiä, ei botteja",
    "compare_lead": "Hetkessä tarkoittaa botteja: yksikään oikea ihminen ei päätä {follow} sekunteja maksun jälkeen.",
    "compare_cols": ("Mikä muuttuu", "Pikapalvelut ja botit", "Growsterr"),
    "compare": [
        ("Keitä he ovat", "Botteja ja valeprofiileja", "Oikeita ihmisiä, jotka päättivät {follow}"),
        ("Tahti", "Tuhansia minuuteissa", "Vähän joka päivä, koko kuukauden"),
        ("Tykkäykset ja kommentit", "Myydään erikseen, lisää botteja", "Samoilta ihmisiltä, osana pakettiasi"),
        ("Näkyvyytesi", "Laskee hiljaa: yleisö, joka ei koskaan reagoi, kertoo {platform}-algoritmille, etteivät {content} ole näyttämisen arvoisia", "Kasvaa ihmisten kanssa, jotka katsovat, tykkäävät ja palaavat"),
        ("Salasanasi", "Usein kysytään", "Ei koskaan"),
        ("Mitä näet", "Luku, joka voi kadota seuraavassa siivouksessa", "Hallintapaneeli siitä, mitä mittasimme"),
    ],

    # Quantity pages: how a monthly package gets you to the goal
    "quantity_title": "Näin saavutat {quantity} {service}",
    "quantity_lead": "Emme myy kiinteää pakettia, jossa on {quantity} {service}. Oikeat ihmiset päättävät itse, joten kuukausipaketti vie sinut perille luonnollisessa tahdissa.",
    "pace_title": "Tyypillinen tahti {pick_name} -paketilla",
    "pace_month": "{n}. kuukausi",
    "pace_goal": "Tavoite: {quantity}",
    "pace_note": "Tyypillisiä vaihteluvälejä sen perusteella, mitä oikeat ihmiset tekevät, ei koskaan lupaus. Jotkin kuukaudet tuovat enemmän, toiset vähemmän.",
    "by_plan_title": "Aika tavoitteeseen {quantity}, paketeittain",
    "a_month": "{range} kuukaudessa",
    "when_first": "yleensä ensimmäisen kuukauden aikana",
    "when_about": "yleensä noin {n} kuukautta",
    "when_range": "yleensä {low}–{high} kuukautta",
    "views_pace": "Katselukerrat tulevat samoilta oikeilta ihmisiltä, jotka löytävät {profile}, joten emme laske niitä etukäteen. {pick_name} on tähän tavoitteeseen parhaiten sopiva paketti.",

    # FAQ, related pages, closing
    "faq_title": "Kysymyksiä ja vastauksia",
    "related_title": "Tutustu lisää",
    "related": {
        "platform": "Lisää {platform}-kasvusta",
        "platforms": "Muilla alustoilla",
        "quantities": "Muita tavoitteita",
        "modifiers": "Muita tapoja kasvaa",
        "articles": "Lue seuraavaksi",
        "hubs": "Kasva oikeiden ihmisten kanssa:",
    },
    # The tools a page can carry ("tool"): they run in the browser, nothing is sent.
    "tools": {
        "calculate": "Laske",
        "followers": "Seuraajat",
        "avg_likes": "Tykkäyksiä keskimäärin julkaisua kohden",
        "avg_comments": "Kommentteja keskimäärin julkaisua kohden",
        "engagement_title": "Sitoutumisasteesi",
        "engagement_lead": "Kuinka moni seuraajistasi reagoi tavalliseen julkaisuun? Syötä luvut muutamasta viimeisimmästä julkaisustasi.",
        "engagement_result": "Sitoutumisasteesi on {rate} %.",
        "engagement_note": "Aste nousee, kun sinua seuraavat ihmiset todella välittävät julkaisuistasi. Seuraajat, jotka eivät koskaan reagoi, laskevat sitä, oli heitä kuinka paljon tahansa.",
        "growth_title": "Kuinka kauan tavoitteeseesi?",
        "growth_lead": "Syötä, missä olet nyt ja mihin haluat päästä. Laskemme sen kunkin paketin tyypillisestä kuukausivaihteluvälistä.",
        "current": "Seuraajat nyt",
        "goal": "Tavoitteesi",
        "when_first": "yleensä ensimmäisen kuukauden aikana",
        "when_range": "yleensä {low}–{high} kuukautta",
        "when_about": "noin {n} kuukautta",
        "reached": "Olet jo perillä.",
        "growth_note": "Tyypillisiä vaihteluvälejä, ei lupaus: oikeat ihmiset päättävät itse, seuraavatko he sinua.",
    },
    # Eyebrow above the headline of pages outside the platform x service grid (by "kind").
    "article_eyebrows": {
        "guide": "Opas",
        "alternative": "Vertailu",
        "payment": "Maksaminen",
        "agency": "Kasvutoimisto",
        "tool": "Työkalu",
        "intent": "Suora vastaus",
    },
    "cta_title": "Valmiina {platform}-kasvuun?",
    "cta_text": "Valitse paketti, niin aloitamme kampanjasi. Oikeat ihmiset päättävät loput, ja hallintapaneelisi näyttää, mitä mittasimme.",

    # Platform hubs
    "services_title": "Mitä kasvatamme {platform}-palvelussa",
    "services_lead": "Yksi paketti tuo kaiken tämän, samoilta oikeilta ihmisiltä.",
    "teasers": {
        "audience": "Oikeita ihmisiä, jotka löytävät {profile} ja päättävät {follow}.",
        "likes": "Tykkäyksiä ihmisiltä, jotka näkevät {content} ja pitävät niistä.",
        "views": "Katselukertoja ihmisiltä, jotka päättävät katsoa, ei koskaan skripteiltä.",
        "comments": "Oikeiden ihmisten kirjoittamia kommentteja, omin sanoin.",
    },
    "explore": "Tutustu",
    "in_package": "Osana jokaista pakettia",
    "goals_title": "Lisää tapoja {platform}-kasvuun",
    "other_hubs_title": "Kasvatamme myös",
}
