"""French YouTube pages: the hub and subscribers ("abonnés"). Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "youtube",
        "label": "YouTube",
        "title": "Packs de croissance YouTube pour créateurs | Growsterr",
        "description": "Développez votre chaîne YouTube avec de vrais spectateurs : abonnés, likes et commentaires chaque mois, jamais de bots. Packs dès {from_price} par mois.",
        "h1": ("Développez votre chaîne YouTube ", "avec de vrais spectateurs."),
        "intro": "Des packs de croissance mensuels pour les créateurs. De vraies personnes découvrent votre chaîne, regardent vos vidéos et s'abonnent quand elles aiment ce qu'elles voient. Votre tableau de bord montre ce que nous avons mesuré, jour après jour.",
        "hero": {"image": "youtube-hub", "alt": "Une chaîne YouTube qui gagne des abonnés, des likes et des commentaires de vrais spectateurs"},
        "sections": [
            {
                "h2": "Les abonnés qui regardent sont ceux qui comptent",
                "p": [
                    "YouTube recommande les vidéos que les gens regardent, aiment et reviennent voir. Un abonné qui ne regarde jamais est pire que pas d'abonné du tout : il fait baisser la part de votre audience qui s'implique.",
                    "Chaque abonné que nous apportons est une personne qui a trouvé votre chaîne et a choisi de s'abonner. Likes, vues et commentaires viennent des mêmes personnes, inclus dans votre pack.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Des spectateurs regardent la vidéo YouTube d'un créateur et écrivent des commentaires"},
            },
            {
                "h2": "Pour les chaînes qui publient avec soin",
                "p": [
                    "Tutoriels, vlogs, musique ou gaming : si vous publiez régulièrement, de vrais spectateurs donnent un meilleur départ à chaque nouvelle vidéo. Commencez avec {starter_name} et passez au pack supérieur quand votre chaîne est prête.",
                ],
                "ul": [
                    "Vous nous indiquez la ville, la région ou le pays d'où doit venir votre audience.",
                    "Abonnés, likes et commentaires arrivent ensemble, des mêmes personnes.",
                    "Votre chaîne reste la vôtre : nous ne demandons jamais votre mot de passe.",
                ],
                "image": {"image": "youtube-channel", "alt": "Un créateur monte une vidéo YouTube dans son studio à la maison"},
            },
        ],
        "faqs": [
            ("Les abonnés sont-ils de vraies personnes ?", "Oui. Chaque abonné est une vraie personne qui a trouvé votre chaîne et a choisi de s'abonner. Pas de bots, pas de faux comptes, rien d'instantané."),
            ("Combien d'abonnés un pack apporte-t-il ?", "En général {starter_audience} nouveaux abonnés par mois avec {starter_name}, {rising_audience} avec {rising_name} et {pro_audience} avec {pro_name}. Des fourchettes habituelles, pas un nombre fixe."),
            ("Avez-vous besoin de mon mot de passe Google ou YouTube ?", "Jamais. Nous avons seulement besoin de l'identifiant de votre chaîne, et votre chaîne doit être publique."),
            ("Puis-je acheter des vues ou des likes seuls ?", "Non. Vues, likes et commentaires sont inclus dans chaque pack, venant des mêmes vraies personnes qui s'abonnent."),
            ("Puis-je résilier à tout moment ?", "Oui. Les packs se renouvellent chaque mois et vous pouvez résilier depuis votre compte. Le mois payé se poursuit jusqu'à son terme."),
        ],
    },
    {
        "service": "subscribers",
        "slug": "youtube/abonnes",
        "label": "Abonnés YouTube",
        "title": "De vrais abonnés YouTube qui regardent | Growsterr",
        "description": "Des abonnés YouTube qui sont de vraies personnes : des spectateurs qui ont trouvé votre chaîne et choisi de s'abonner, avec likes et commentaires. Dès {from_price}.",
        "h1": ("Des abonnés YouTube ", "qui regardent vraiment."),
        "intro": "De vraies personnes découvrent votre chaîne, regardent vos vidéos et s'abonnent quand elles aiment ce qu'elles voient. En général {starter_audience} nouveaux abonnés par mois avec {starter_name}, avec les likes et commentaires des mêmes spectateurs.",
        "hero": {"image": "youtube-subscribers", "alt": "La page d'une chaîne YouTube avec de nouveaux abonnés venus de vrais spectateurs"},
        "sections": [
            {
                "h2": "Un abonné devrait être un spectateur",
                "p": [
                    "Sur YouTube, un abonné n'est utile que s'il regarde. De vrais abonnés voient votre prochaine vidéo, la regardent, l'aiment et parfois la commentent, et c'est ce que YouTube observe pour décider quoi recommander.",
                    "Les abonnés bots ne regardent jamais. Ils font paraître une chaîne plus grande pendant que ses vidéos touchent moins de monde.",
                ],
                "image": {"image": "youtube-viewers", "alt": "De vrais spectateurs s'abonnent à une chaîne YouTube après avoir regardé une vidéo"},
            },
            {
                "h2": "À quoi ressemble un mois",
                "ul": [
                    "Premiers jours : votre campagne démarre et les premiers spectateurs arrivent.",
                    "Chaque semaine : nouveaux abonnés, likes et commentaires, un peu chaque jour.",
                    "En fin de mois : en général {pick_audience} nouveaux abonnés avec {pick_name}.",
                ],
            },
            {
                "h2": "D'où viennent vos spectateurs",
                "p": [
                    "Indiquez-nous la ville, la région ou le pays d'où doit venir votre audience. Nous montrons d'abord votre chaîne à de vraies personnes là-bas ; là où le public le plus adapté est plus nombreux, davantage peuvent venir des environs.",
                ],
            },
        ],
        "faqs": [
            ("À quelle vitesse arrivent les abonnés ?", "Un peu chaque jour, sur tout le mois. Jamais tout d'un coup : de vraies personnes s'abonnent à leur rythme."),
            ("Vont-ils regarder mes vidéos ?", "Ce sont de vraies personnes qui ont choisi de s'abonner après avoir vu votre chaîne. Ce qu'elles regardent ensuite leur appartient, comme pour toute audience, et c'est justement pour cela que ça compte."),
            ("Est-ce que je reçois aussi des likes et des commentaires ?", "Oui, des mêmes spectateurs : en général {pick_likes} likes et {pick_comments} commentaires par mois avec {pick_name}."),
            ("Avez-vous besoin de mon mot de passe ?", "Jamais. Nous avons seulement besoin de l'identifiant de votre chaîne, et votre chaîne doit être publique."),
        ],
    },
]
