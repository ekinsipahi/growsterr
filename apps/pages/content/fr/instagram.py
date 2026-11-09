"""French Instagram pages: the hub, followers ("abonnés"), and the 1,000-followers goal.
Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "instagram",
        "label": "Instagram",
        "title": "Packs de croissance Instagram pour créateurs | Growsterr",
        "description": "Développez votre Instagram avec de vraies personnes : nouveaux abonnés, likes et commentaires chaque mois, jamais de bots. Packs dès {from_price} par mois.",
        "h1": ("Développez votre Instagram ", "avec de vraies personnes."),
        "intro": "Des packs de croissance mensuels pour les créateurs et les influenceurs. Nous montrons votre profil à de vraies personnes, et celles qui aiment ce qu'elles voient vous suivent, likent et commentent. Votre tableau de bord montre ce que nous avons mesuré, jour après jour.",
        "hero": {"image": "instagram-hub", "alt": "Le profil Instagram d'un créateur qui reçoit de nouveaux abonnés, des likes et des commentaires"},
        "sections": [
            {
                "h2": "Une croissance qui a l'air méritée, parce qu'elle l'est",
                "p": [
                    "Instagram récompense les comptes avec lesquels les gens interagissent vraiment. Les bots font le contraire : ils gonflent votre nombre d'abonnés, n'aiment jamais, ne regardent jamais et apprennent à l'algorithme que vos publications ne valent pas la peine d'être montrées.",
                    "Nous faisons l'inverse. Votre profil est présenté chaque jour à de vraies personnes, et chaque abonnement est un choix. C'est pour cela que likes, vues et commentaires arrivent avec vos abonnés, et non comme un achat à part.",
                ],
                "image": {"image": "instagram-real-people", "alt": "De vraies personnes découvrent les publications Instagram d'un créateur et laissent des commentaires"},
            },
            {
                "h2": "Pour les créateurs qui publient avec une intention",
                "p": [
                    "Marque personnelle, page de niche ou petite entreprise : les packs grandissent avec vous. Commencez avec {starter_name} et passez au pack supérieur quand votre contenu est prêt pour plus.",
                ],
                "ul": [
                    "Reels, carrousels et photos en profitent tous.",
                    "Vous nous indiquez la ville, la région ou le pays d'où doit venir votre audience.",
                    "Votre compte reste le vôtre : nous ne demandons jamais votre mot de passe.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "Un créateur prépare ses contenus Instagram à son bureau"},
            },
        ],
        "faqs": [
            ("Les abonnés sont-ils de vraies personnes ?", "Oui. Chaque abonné est une vraie personne qui a vu votre profil et a choisi de vous suivre. Nous n'utilisons jamais de bots, de faux profils ni de livraison instantanée."),
            ("Combien d'abonnés un pack apporte-t-il ?", "En général {starter_audience} nouveaux abonnés par mois avec {starter_name}, {rising_audience} avec {rising_name} et {pro_audience} avec {pro_name}. Ce sont des fourchettes habituelles, pas un nombre fixe : de vraies personnes décident elles-mêmes."),
            ("Avez-vous besoin de mon mot de passe Instagram ?", "Jamais. Nous avons seulement besoin de votre nom d'utilisateur. Gardez votre compte public pour que les personnes qui le découvrent puissent vous suivre."),
            ("Puis-je acheter des likes ou des commentaires seuls ?", "Non. Likes, vues et commentaires sont inclus dans chaque pack, venant des mêmes vraies personnes qui vous suivent. C'est ce qui garde vos chiffres naturels."),
            ("Puis-je résilier à tout moment ?", "Oui. Les packs se renouvellent chaque mois et vous pouvez résilier depuis votre compte. Le mois payé se poursuit jusqu'à son terme."),
        ],
    },
    {
        "service": "followers",
        "slug": "instagram/abonnes",
        "label": "Abonnés Instagram",
        "title": "De vrais abonnés Instagram, chaque mois | Growsterr",
        "description": "Des abonnés Instagram qui sont de vraies personnes et ont choisi de vous suivre, avec likes et commentaires des mêmes personnes. Packs mensuels dès {from_price}.",
        "h1": ("Des abonnés Instagram ", "qui ont choisi de vous suivre."),
        "intro": "De vraies personnes découvrent votre profil chaque jour, et celles qui aiment ce qu'elles voient vous suivent. En général {starter_audience} nouveaux abonnés par mois avec {starter_name}, avec les likes et commentaires des mêmes personnes.",
        "hero": {"image": "instagram-followers", "alt": "Un profil Instagram qui gagne de nouveaux abonnés, tous de vraies personnes"},
        "sections": [
            {
                "h2": "Pourquoi de vrais abonnés valent plus",
                "p": [
                    "Un abonné ne compte que si une personne se trouve derrière. De vrais abonnés voient votre prochaine publication, l'aiment, la commentent et la partagent, et c'est cet engagement qu'Instagram regarde pour décider à qui montrer votre contenu.",
                    "Les bots ne font rien de tout cela. Ils gonflent un chiffre quelques jours, disparaissent au prochain nettoyage, et ceux qui restent font baisser votre portée en silence.",
                ],
                "image": {"image": "instagram-real-people", "alt": "De vraies personnes aiment et commentent la publication Instagram d'un créateur"},
            },
            {
                "h2": "D'où viennent vos nouveaux abonnés",
                "p": [
                    "Indiquez-nous la ville, la région ou le pays d'où doit venir votre audience. Nous montrons d'abord votre profil à de vraies personnes là-bas ; là où le public le plus adapté est plus nombreux, davantage peuvent venir des environs.",
                ],
            },
            {
                "h2": "À quoi ressemble un mois",
                "ul": [
                    "Premiers jours : votre campagne démarre et les premières visites arrivent.",
                    "Chaque semaine : nouveaux abonnés, likes et commentaires, un peu chaque jour.",
                    "En fin de mois : en général {pick_audience} nouveaux abonnés avec {pick_name}.",
                ],
            },
        ],
        "faqs": [
            ("À quelle vitesse arrivent les abonnés ?", "Un peu chaque jour, sur tout le mois. Jamais tout d'un coup : de vraies personnes suivent à leur rythme, et tout ce qui est instantané est un bot."),
            ("Mes nouveaux abonnés vont-ils se désabonner ?", "Certains peut-être, comme dans toute audience réelle. De vrais abonnés restent bien plus souvent que les bots, qui disparaissent par vagues."),
            ("Est-ce que je reçois aussi des likes et des commentaires ?", "Oui, des mêmes personnes : en général {pick_likes} likes et {pick_comments} commentaires par mois avec {pick_name}."),
            ("Est-ce sans risque pour mon compte ?", "Nous ne demandons jamais votre mot de passe et ne nous connectons jamais à votre compte. Les gens trouvent votre profil et décident eux-mêmes, comme n'importe quel abonné vous trouve."),
            ("Puis-je choisir d'où viennent mes abonnés ?", "Oui. Indiquez la ville, la région ou le pays lors de la commande. Nous visons d'abord cet endroit ; quand un public très proche est plus nombreux aux alentours, une partie de vos abonnés peut en venir."),
        ],
    },
    {
        "service": "followers",
        "quantity": 1000,
        "slug": "instagram/abonnes/1000",
        "label": "{quantity} abonnés Instagram",
        "title": "{quantity} abonnés Instagram, de vraies personnes | Growsterr",
        "description": "Atteignez {quantity} abonnés Instagram avec de vraies personnes, pas des bots. {pick_name} en apporte en général {pick_audience} par mois, avec des likes.",
        "h1": ("{quantity} abonnés Instagram, ", "tous bien réels."),
        "intro": "Nous ne vendons pas un lot de {quantity} bots. Nous faisons grandir votre compte avec de vraies personnes : {pick_name} apporte en général {pick_audience} nouveaux abonnés par mois, donc {quantity} est souvent à portée dès le premier mois.",
        "hero": {"image": "instagram-followers-1000", "alt": "Une courbe de nouveaux abonnés Instagram qui atteint un premier palier"},
        "sections": [
            {
                "h2": "Pourquoi pas {quantity} abonnés en une heure ?",
                "p": [
                    "Parce qu'aucune vraie personne ne suit un compte quelques secondes après un paiement. Les services qui livrent {quantity} abonnés en une heure livrent des bots : ils n'aiment pas, ne commentent pas et disparaissent par vagues.",
                    "Ceux qui restent font encore plus de dégâts. Chaque abonné qui n'interagit jamais fait baisser la part de votre audience qui interagit, et vos publications touchent moins de monde, en silence.",
                ],
            },
            {
                "h2": "Vos mille premiers, dans les règles de l'art",
                "p": [
                    "Mille premiers abonnés réels changent la façon dont les nouveaux visiteurs vous perçoivent. Ce sont des personnes qui peuvent regarder vos Reels, aimer vos publications et revenir, et c'est exactement ce qui aide les mille suivants à vous trouver.",
                ],
                "ul": [
                    "De vraies personnes qui ont choisi de vous suivre, depuis le lieu de votre choix.",
                    "Les likes et commentaires des mêmes personnes, inclus dans le pack.",
                    "Un tableau de bord qui montre ce que nous avons mesuré, jour après jour.",
                ],
            },
        ],
        "faqs": [
            ("Combien de temps pour {quantity} vrais abonnés ?", "À un rythme habituel, {pick_name} apporte {pick_audience} nouveaux abonnés par mois, donc {quantity} est souvent atteint dès le premier mois. De vraies personnes suivent à leur rythme, donc chaque mois est un peu différent."),
            ("Est-ce un lot unique de {quantity} ?", "Non. Nous vendons la croissance sous forme de packs mensuels. {pick_name} coûte {pick_price} par mois, résiliable à tout moment depuis votre compte."),
            ("Est-ce que je reçois des likes et des commentaires avec ?", "Oui, des mêmes vraies personnes : en général {pick_likes} likes et {pick_comments} commentaires par mois avec {pick_name}."),
            ("Que se passe-t-il après {quantity} ?", "Votre pack continue jusqu'à ce que vous le résiliiez, donc votre croissance se poursuit mois après mois. Quand votre contenu est prêt pour plus, vous pouvez passer au pack supérieur."),
        ],
    },
]
