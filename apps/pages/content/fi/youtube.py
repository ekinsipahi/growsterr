"""Finnish YouTube pages: the hub and subscribers (mirrors en/youtube.py)."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "youtube",
        "label": "YouTube",
        "title": "YouTube-kasvupaketit sisällöntuottajille | Growsterr",
        "description": "Kasvata YouTube-kanavaasi: kuukausipaketit tuovat tilaajia, tykkäyksiä ja kommentteja oikeilta katsojilta, jotka päättivät tilata. Alkaen {from_price}/kk.",
        "h1": ("Kasvata YouTube-kanavaasi ", "oikeiden katsojien avulla."),
        "intro": "Kuukausittaiset kasvupaketit sisällöntuottajille. Oikeat ihmiset löytävät kanavasi, katsovat videoitasi ja tilaavat, kun pitävät näkemästään. Hallintapaneelisi näyttää, mitä mittasimme, päivä päivältä.",
        "hero": {"image": "youtube-hub", "alt": "YouTube-kanava saa tilaajia, tykkäyksiä ja kommentteja oikeilta katsojilta"},
        "sections": [
            {
                "h2": "Merkitystä on tilaajilla, jotka katsovat",
                "p": [
                    "YouTube suosittelee videoita, joita ihmiset katsovat, joista he tykkäävät ja joihin he palaavat. Tilaaja, joka ei koskaan katso, on huonompi kuin ei tilaajaa lainkaan: hän pienentää sitä osaa yleisöstäsi, joka on aktiivinen.",
                    "Jokainen tuomamme tilaaja on ihminen, joka löysi kanavasi ja päätti tilata sen. Tykkäykset, katselukerrat ja kommentit tulevat samoilta ihmisiltä, osana pakettiasi.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Katsojat katsovat sisällöntuottajan YouTube-videota ja kirjoittavat kommentteja"},
            },
            {
                "h2": "Kanaville, jotka julkaisevat huolella",
                "p": [
                    "Opetusvideot, vlogit, musiikki tai pelaaminen: jos julkaiset säännöllisesti, oikeat katsojat antavat jokaiselle uudelle videolle paremman alun. Aloita {starter_name} -paketilla ja siirry isompaan, kun kanavasi on valmis enempään.",
                ],
                "ul": [
                    "Kerrot itse, mistä kaupungista, alueelta tai maasta yleisösi pitäisi tulla.",
                    "Tilaajat, tykkäykset ja kommentit tulevat yhdessä, samoilta ihmisiltä.",
                    "Kanavasi pysyy sinun: emme koskaan kysy salasanaasi.",
                ],
                "image": {"image": "youtube-channel", "alt": "Sisällöntuottaja editoi YouTube-videota kotistudiossa"},
            },
        ],
        "faqs": [
            ("Ovatko tilaajat oikeita ihmisiä?", "Kyllä. Jokainen tilaaja on oikea ihminen, joka löysi kanavasi ja päätti tilata sen. Ei botteja, ei valetilejä, ei mitään hetkessä."),
            ("Kuinka monta tilaajaa paketti tuo?", "Tyypillisesti {starter_audience} uutta tilaajaa kuukaudessa {starter_name} -paketilla, {rising_audience} {rising_name} -paketilla ja {pro_audience} {pro_name} -paketilla. Tyypillisiä vaihteluvälejä, ei kiinteä määrä."),
            ("Tarvitsetteko Google- tai YouTube-salasanani?", "Ei koskaan. Tarvitsemme vain kanavasi kahvan (@handle), ja kanavasi pitää olla julkinen."),
            ("Voinko ostaa katselukertoja tai tykkäyksiä erikseen?", "Et. Katselukerrat, tykkäykset ja kommentit kuuluvat jokaiseen pakettiin, ja ne tulevat samoilta oikeilta ihmisiltä, jotka tilaavat kanavasi."),
            ("Voinko perua milloin tahansa?", "Kyllä. Paketit uusiutuvat kuukausittain, ja voit perua ne tililtäsi. Maksamasi kuukausi jatkuu loppuun asti."),
        ],
    },
    {
        "service": "subscribers",
        "slug": "youtube/tilaajat",
        "label": "YouTube-tilaajat",
        "title": "Aidot YouTube-tilaajat, jotka katsovat | Growsterr",
        "description": "YouTube-tilaajia, jotka ovat oikeita ihmisiä: katsojia, jotka löysivät kanavasi ja päättivät tilata sen, tykkäysten ja kommenttien kera. Alkaen {from_price}/kk.",
        "h1": ("YouTube-tilaajia, ", "jotka oikeasti katsovat."),
        "intro": "Oikeat ihmiset löytävät kanavasi, katsovat videoitasi ja tilaavat, kun pitävät näkemästään. Tyypillisesti {starter_audience} uutta tilaajaa kuukaudessa {starter_name} -paketilla, ja tykkäykset ja kommentit samoilta katsojilta.",
        "hero": {"image": "youtube-subscribers", "alt": "YouTube-kanavasivu saa uusia tilaajia oikeilta katsojilta"},
        "sections": [
            {
                "h2": "Tilaajan pitäisi olla katsoja",
                "p": [
                    "YouTubessa tilaajasta on hyötyä vain, jos hän katsoo. Aidot tilaajat näkevät seuraavan latauksesi, katsovat sen, tykkäävät siitä ja joskus kommentoivat, ja juuri tätä YouTube katsoo päättäessään, mitä suositella.",
                    "Bottitilaajat eivät koskaan katso. Ne saavat kanavan näyttämään isommalta, vaikka sen videot tavoittavat vähemmän ihmisiä.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Oikeat katsojat tilaavat YouTube-kanavan katsottuaan videon"},
            },
            {
                "h2": "Tältä kuukausi näyttää",
                "ul": [
                    "Ensimmäiset päivät: kampanjasi alkaa ja ensimmäiset katsojat saapuvat.",
                    "Joka viikko: uusia tilaajia, tykkäyksiä ja kommentteja, muutama joka päivä.",
                    "Kuukauden lopussa: tyypillisesti {pick_audience} uutta tilaajaa {pick_name} -paketilla.",
                ],
            },
            {
                "h2": "Mistä katsojasi tulevat",
                "p": [
                    "Kerro meille, mistä kaupungista, alueelta tai maasta yleisösi pitäisi tulla. Näytämme kanavaasi ensin siellä oleville oikeille ihmisille; jos parhaiten sopiva yleisö on lähialueella suurempi, osa voi tulla sieltä.",
                ],
            },
        ],
        "faqs": [
            ("Kuinka nopeasti tilaajat tulevat?", "Vähän joka päivä, koko kuukauden ajan. Ei koskaan kaikkea kerralla: oikeat ihmiset tilaavat omaan tahtiinsa."),
            ("Katsovatko he videoitani?", "He ovat oikeita ihmisiä, jotka päättivät tilata kanavasi nähtyään sen. Mitä he katsovat seuraavaksi, on heidän päätöksensä, kuten minkä tahansa yleisön, ja juuri siksi sillä on merkitystä."),
            ("Saanko myös tykkäyksiä ja kommentteja?", "Kyllä, samoilta katsojilta: tyypillisesti {pick_likes} tykkäystä ja {pick_comments} kommenttia kuukaudessa {pick_name} -paketilla."),
            ("Tarvitsetteko salasanani?", "Ei koskaan. Tarvitsemme vain kanavasi kahvan, ja kanavasi pitää olla julkinen."),
        ],
    },
]
