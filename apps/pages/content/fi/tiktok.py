"""Finnish TikTok pages: the hub and likes (mirrors en/tiktok.py)."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "tiktok",
        "label": "TikTok",
        "title": "TikTok-kasvupaketit sisällöntuottajille | Growsterr",
        "description": "Kasva TikTokissa aidosti: kuukausipaketit tuovat seuraajia, tykkäyksiä ja kommentteja oikeilta ihmisiltä, jotka päättivät seurata. Alkaen {from_price}/kk.",
        "h1": ("Kasvata TikTokiasi ", "oikeiden ihmisten avulla."),
        "intro": "Kuukausittaiset kasvupaketit sisällöntuottajille ja vaikuttajille. Oikeat ihmiset löytävät profiilisi, katsovat videoitasi ja seuraavat sinua, kun pitävät näkemästään. Hallintapaneelisi näyttää, mitä mittasimme, päivä päivältä.",
        "hero": {"image": "tiktok-hub", "alt": "TikTok-sisällöntuottajan profiili, johon tulee uusia seuraajia ja tykkäyksiä"},
        "sections": [
            {
                "h2": "TikTokissa huomio on kaikki kaikessa",
                "p": [
                    "TikTok näyttää videon useammille, kun sen ensimmäiset katsojat katsovat, tykkäävät, kommentoivat ja seuraavat. Luvut, joiden takana ei ole ihmisiä, eivät liikuta mitään näistä.",
                    "Pakettimme tuovat oikeita ihmisiä profiiliisi joka päivä. He katsovat, he päättävät, ja ne, jotka pitävät videoistasi, seuraavat ja tykkäävät. Juuri sellainen huomio auttaa videota leviämään.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Oikeat katsojat katsovat sisällöntuottajan TikTok-videoita"},
            },
            {
                "h2": "Sisällöntuottajille, joilla on sanottavaa",
                "p": [
                    "Komiikka, ruoanlaitto, muoti tai opetusvideot: jos julkaiset säännöllisesti, oikeat katsojat antavat jokaiselle uudelle videolle paremman alun. Aloita {starter_name} -paketilla ja siirry isompaan, kun olet valmis.",
                ],
                "ul": [
                    "Kerrot itse, mistä kaupungista, alueelta tai maasta yleisösi pitäisi tulla.",
                    "Seuraajat, tykkäykset ja kommentit tulevat yhdessä, samoilta ihmisiltä.",
                    "Tilisi pysyy sinun: emme koskaan kysy salasanaasi.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Sisällöntuottaja kuvaa TikTok-videota jalustalla olevalla puhelimella"},
            },
        ],
        "faqs": [
            ("Ovatko seuraajat oikeita ihmisiä?", "Kyllä. Jokainen seuraaja on oikea ihminen, joka näki profiilisi ja päätti seurata sinua. Emme koskaan käytä botteja, valetilejä emmekä välitöntä toimitusta."),
            ("Kuinka monta seuraajaa paketti tuo?", "Tyypillisesti {starter_audience} uutta seuraajaa kuukaudessa {starter_name} -paketilla, {rising_audience} {rising_name} -paketilla ja {pro_audience} {pro_name} -paketilla. Tyypillisiä vaihteluvälejä, ei kiinteä määrä: oikeat ihmiset päättävät itse."),
            ("Tarvitsetteko TikTok-salasanani?", "Ei koskaan. Tarvitsemme vain käyttäjänimesi. Pidä tilisi julkisena, jotta sen löytävät ihmiset voivat seurata sinua."),
            ("Voinko ostaa katselukertoja tai tykkäyksiä erikseen?", "Et. Katselukerrat, tykkäykset ja kommentit kuuluvat jokaiseen pakettiin, ja ne tulevat samoilta oikeilta ihmisiltä, jotka seuraavat sinua."),
            ("Voinko perua milloin tahansa?", "Kyllä. Paketit uusiutuvat kuukausittain, ja voit perua ne tililtäsi. Maksamasi kuukausi jatkuu loppuun asti."),
        ],
    },
    {
        "service": "likes",
        "slug": "tiktok/tykkaykset",
        "label": "TikTok-tykkäykset",
        "title": "TikTok-tykkäykset oikeilta ihmisiltä, osana pakettia",
        "description": "TikTok-tykkäyksiä oikeilta ihmisiltä, jotka katsovat videoitasi, ei koskaan boteilta. Tykkäykset kuuluvat jokaiseen kuukausipakettiin. Alkaen {from_price}/kk.",
        "h1": ("TikTok-tykkäykset oikeilta ihmisiltä. ", "Osana jokaista pakettia."),
        "intro": "Emme myy tykkäyksiä erikseen. Jokainen paketti tuo oikeita ihmisiä, jotka löytävät profiilisi, katsovat videoitasi ja tykkäävät siitä, mistä pitävät: tyypillisesti {starter_likes} tykkäystä kuukaudessa {starter_name} -paketilla.",
        "hero": {"image": "tiktok-likes", "alt": "Oikeiden katsojien tykkäyksiä nousee TikTok-videosta"},
        "sections": [
            {
                "h2": "Tykkäys merkitsee vain, kun sen takana on ihminen",
                "p": [
                    "TikTok seuraa, mitä tykkäyksen ympärillä tapahtuu: jatkoiko katsoja katsomista, seurasiko hän, palasiko hän? Bottien tykkäykset vastaavat kaikkeen ei, joten ne lisäävät luvun ja vievät näkyvyyttä.",
                    "Oikeiden ihmisten tykkäykset tuovat mukanaan muunkin: katseluajan, seuraamiset ja kommentit. Juuri se signaali auttaa videota leviämään.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Katsojat katsovat TikTok-videon loppuun ja tykkäävät siitä"},
            },
            {
                "h2": "Näin monta tykkäystä kukin paketti tuo",
                "ul": [
                    "{starter_name} ({starter_price} kuukaudessa): tyypillisesti {starter_likes} tykkäystä.",
                    "{rising_name} ({rising_price} kuukaudessa): tyypillisesti {rising_likes} tykkäystä valitsemiisi videoihin.",
                    "{pro_name} ({pro_price} kuukaudessa): tyypillisesti {pro_likes} tykkäystä ja etusija näkyvyydessä.",
                ],
            },
            {
                "h2": "Miksi emme myy tykkäyksiä erikseen",
                "p": [
                    "Tykkäykset, jotka tulevat ilman katselukertoja, seuraamisia tai kommentteja, näyttävät juuri siltä, mitä ne ovat. Paketissa jokainen tykkäys tulee joltakulta, joka katsoi videon, joten lukusi liikkuvat yhdessä niin kuin aidossa kasvussa.",
                ],
            },
        ],
        "faqs": [
            ("Saanko TikTok-tykkäyksiä ilman pakettia?", "Et. Tykkäykset, katselukerrat ja kommentit tulevat vain kuukausipakettiemme mukana, samoilta oikeilta ihmisiltä. Juuri se pitää ne luonnollisina."),
            ("Mitkä videot saavat tykkäykset?", "Oikeat ihmiset tykkäävät siitä, mistä pitävät, yleensä uusimmista videoistasi. {rising_name}- ja {pro_name} -paketeilla voit valita, mitkä videot saavat huomion."),
            ("Kuinka nopeasti tykkäykset tulevat?", "Vähän joka päivä, kuukauden aikana. Ei koskaan hetkessä: hetkessä tuleva tykkäys on botti."),
            ("Tarvitsetteko TikTok-salasanani?", "Ei koskaan. Tarvitsemme vain käyttäjänimesi, ja tilisi pitää olla julkinen."),
        ],
    },
]
