"""Catalan YouTube pages: the hub and subscribers ("subscriptors"). Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "youtube",
        "label": "YouTube",
        "title": "Paquets de creixement per a YouTube | Growsterr",
        "description": "Fes créixer el teu canal de YouTube amb persones reals: paquets mensuals amb subscriptors, m'agrades i comentaris d'espectadors reals. Des de {from_price} al mes.",
        "h1": ("Fes créixer el teu canal de YouTube ", "amb espectadors reals."),
        "intro": "Paquets de creixement mensuals per a creadors. Persones reals descobreixen el teu canal, miren els teus vídeos i s'hi subscriuen quan els agrada el que veuen. El teu tauler mostra el que hem mesurat, dia a dia.",
        "hero": {"image": "youtube-hub", "alt": "Un canal de YouTube que guanya subscriptors, m'agrades i comentaris d'espectadors reals"},
        "sections": [
            {
                "h2": "Els subscriptors que miren són els que compten",
                "p": [
                    "YouTube recomana els vídeos que la gent mira, als quals fa m'agrada i als quals torna. Un subscriptor que no mira mai res és pitjor que cap: redueix la part del teu públic que participa.",
                    "Cada subscriptor que portem és una persona que ha trobat el teu canal i ha decidit subscriure-s'hi. Els m'agrades, les visualitzacions i els comentaris arriben de les mateixes persones, dins del teu paquet.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Espectadors miren el vídeo de YouTube d'un creador i hi escriuen comentaris"},
            },
            {
                "h2": "Per a canals que publiquen amb cura",
                "p": [
                    "Tutorials, vlogs, música o gaming: si publiques amb regularitat, els espectadors reals donen a cada vídeo nou una millor arrencada. Comença amb {starter_name} i passa a un paquet superior quan el teu canal estigui a punt per a més.",
                ],
                "ul": [
                    "Ens dius la ciutat, la regió o el país d'on ha de venir el teu públic.",
                    "Subscriptors, m'agrades i comentaris arriben junts, de les mateixes persones.",
                    "El teu canal continua sent teu: mai et demanem la contrasenya.",
                ],
                "image": {"image": "youtube-channel", "alt": "Un creador edita un vídeo de YouTube al seu estudi de casa"},
            },
        ],
        "faqs": [
            ("Els subscriptors són persones reals?", "Sí. Cada subscriptor és una persona real que ha trobat el teu canal i ha decidit subscriure-s'hi. Sense bots, sense comptes falsos, res d'instantani."),
            ("Quants subscriptors porta un paquet?", "Normalment {starter_audience} subscriptors nous al mes amb {starter_name}, {rising_audience} amb {rising_name} i {pro_audience} amb {pro_name}. Intervals habituals, no una xifra fixa."),
            ("Necessiteu la meva contrasenya de Google o de YouTube?", "Mai. Només necessitem l'identificador del teu canal, i el canal ha de ser públic."),
            ("Puc comprar visualitzacions o m'agrades per separat?", "No. Les visualitzacions, els m'agrades i els comentaris arriben dins de cada paquet, de les mateixes persones reals que s'hi subscriuen."),
            ("Puc cancel·lar quan vulgui?", "Sí. Els paquets es renoven cada mes i pots cancel·lar des del teu compte. El mes que ja has pagat continua fins al final."),
        ],
    },
    {
        "service": "subscribers",
        "slug": "youtube/subscriptors",
        "label": "Subscriptors de YouTube",
        "title": "Subscriptors reals de YouTube que miren | Growsterr",
        "description": "Subscriptors de YouTube que són persones reals: espectadors que han trobat el teu canal i s'hi han subscrit, amb m'agrades i comentaris. Des de {from_price}.",
        "h1": ("Subscriptors de YouTube ", "que miren de debò."),
        "intro": "Persones reals descobreixen el teu canal, miren els teus vídeos i s'hi subscriuen quan els agrada el que veuen. Normalment {starter_audience} subscriptors nous al mes amb {starter_name}, amb m'agrades i comentaris dels mateixos espectadors.",
        "hero": {"image": "youtube-subscribers", "alt": "La pàgina d'un canal de YouTube amb subscriptors nous d'espectadors reals"},
        "sections": [
            {
                "h2": "Un subscriptor hauria de ser un espectador",
                "p": [
                    "A YouTube, un subscriptor només és útil si mira els teus vídeos. Els subscriptors reals veuen el teu proper vídeo, el miren, hi fan m'agrada i de vegades el comenten, i això és el que YouTube observa per decidir què recomana.",
                    "Els subscriptors bots no miren mai res. Fan que un canal sembli més gran mentre els seus vídeos arriben a menys gent.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Espectadors reals se subscriuen a un canal de YouTube després de mirar un vídeo"},
            },
            {
                "h2": "Com és un mes",
                "ul": [
                    "Primers dies: la campanya arrenca i arriben els primers espectadors.",
                    "Cada setmana: subscriptors nous, m'agrades i comentaris, uns quants cada dia.",
                    "A final de mes: normalment {pick_audience} subscriptors nous amb {pick_name}.",
                ],
            },
            {
                "h2": "D'on arriben els teus espectadors",
                "p": [
                    "Digues-nos la ciutat, la regió o el país d'on ha de venir el teu públic. Primer mostrem el teu canal a persones reals d'allà; on el públic més adequat és més nombrós a prop, en poden arribar més d'aquella zona.",
                ],
            },
        ],
        "faqs": [
            ("Amb quina rapidesa arriben els subscriptors?", "Una mica cada dia, durant tot el mes. Mai tot de cop: les persones reals se subscriuen al seu ritme."),
            ("Miraran els meus vídeos?", "Són persones reals que han decidit subscriure-s'hi després de veure el teu canal. El que mirin després ho decideixen elles, com qualsevol públic, i precisament per això compta."),
            ("També rebo m'agrades i comentaris?", "Sí, dels mateixos espectadors: normalment {pick_likes} m'agrades i {pick_comments} comentaris al mes amb {pick_name}."),
            ("Necessiteu la meva contrasenya?", "Mai. Només necessitem l'identificador del teu canal, i el canal ha de ser públic."),
        ],
    },
]
