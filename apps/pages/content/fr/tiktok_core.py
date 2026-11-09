"""French TikTok pages: followers, views and comments, and the ways people ask for them (real,
organic, progressive, monthly, no-drop, safe, private accounts, LIVE, the For You page...). The hub
and likes live in tiktok.py. Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-09"

PAGES = [
    # --- Followers ------------------------------------------------------------------------
    {
        "service": "followers",
        "slug": "tiktok/abonnes",
        "label": "Abonnés TikTok",
        "title": "Acheter des abonnés TikTok : de vraies personnes | Growsterr",
        "description": "Achetez des abonnés TikTok honnêtement : de vraies personnes découvrent vos vidéos et choisissent de vous suivre, chaque jour du mois. Packs dès {from_price}.",
        "h1": ("Acheter des abonnés TikTok ", "avec une vraie personne derrière chacun."),
        "intro": "Vous voulez acheter des abonnés TikTok sans remplir votre compte de bots ? Nos packs mensuels présentent votre profil à de nouvelles personnes chaque jour, et les spectateurs qui aiment votre style appuient sur S'abonner. Avec {starter_name}, cela représente en général {starter_audience} nouveaux abonnés par mois ; les packs supérieurs en apportent davantage.",
        "hero": {"image": "tiktok-creator", "alt": "Un créateur TikTok tourne une nouvelle vidéo pendant que de vraies personnes s'abonnent"},
        "sections": [
            {
                "h2": "Ce que vous payez vraiment",
                "p": [
                    "Quand vous achetez des abonnés TikTok chez nous, vous payez une campagne, pas un compteur. Grâce à des campagnes sponsorisées dans notre réseau partenaire, votre profil touche de vraies personnes chaque jour du mois. S'abonner ou non leur appartient, et c'est ce choix qui donne sa valeur à l'abonnement.",
                    "Sur TikTok, la valeur d'un abonné tient à ce qu'il fait ensuite : regarder votre nouvelle vidéo, rester jusqu'au bout, l'aimer, l'envoyer à un ami. Les personnes font tout cela. Un compte créé pour gonfler un chiffre n'en fait rien.",
                ],
            },
            {
                "h2": "Comment choisir un site pour acheter des abonnés TikTok",
                "p": ["Quel que soit le site ou l'appli que vous regardez, quelques questions distinguent vite les vrais services des boutiques de bots."],
                "ul": [
                    "Demande-t-il votre mot de passe, ou une connexion avec TikTok ? Un service d'abonnés n'a besoin ni de l'un ni de l'autre.",
                    "Parle-t-il de milliers d'abonnés en quelques minutes ? Seuls les bots arrivent aussi vite.",
                    "Montre-t-il ce qu'il a mesuré, jour après jour, ou juste un chiffre à la fin ?",
                    "Pouvez-vous arrêter l'abonnement vous-même, ou devez-vous écrire et attendre ?",
                    "Les likes et commentaires sont-ils vendus en option, ou viennent-ils des abonnés eux-mêmes ?",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "De nouveaux abonnés TikTok regardent les dernières vidéos d'un créateur sur leur téléphone"},
            },
            {
                "h2": "D'abord les abonnés, puis tout ce qu'ils apportent",
                "p": [
                    "Les nouveaux abonnés voient vos vidéos dans leur fil Abonnements, et leurs visionnages, likes et partages aident TikTok à comprendre à qui d'autre une vidéo pourrait plaire. Des abonnés bots laissent cette première audience muette, si bien que chaque nouvelle vidéo part d'une position plus faible.",
                ],
            },
        ],
        "faqs": [
            ("Comment obtenir des abonnés TikTok avec Growsterr ?", "Choisissez un pack, donnez-nous votre nom d'utilisateur TikTok, indiquez où doit vivre votre nouvelle audience et payez par carte via Stripe. Votre campagne démarre et les nouveaux abonnés commencent à arriver, un peu chaque jour."),
            ("Puis-je acheter des abonnés TikTok une seule fois, sans abonnement ?", "Non. Nous ne vendons pas de packs ponctuels. De vraies personnes arrivent sur plusieurs semaines plutôt qu'en une seule livraison, c'est pourquoi la croissance fonctionne en pack mensuel. Vous pouvez résilier quand vous voulez et garder le mois payé."),
            ("Dois-je installer une appli ?", "Non. Vous commandez sur ce site et suivez votre campagne dans votre compte Growsterr, depuis n'importe quel navigateur. Méfiez-vous des applis qui distribuent des abonnés en échange de suivre des inconnus : ces abonnements disparaissent souvent dès que l'échange prend fin."),
            ("Acheter des abonnés TikTok va-t-il me rendre viral ?", "Personne ne peut le promettre. De vrais abonnés donnent à chaque nouvelle vidéo plus de personnes susceptibles de la regarder jusqu'au bout et de la partager, ce qui améliore ses chances. Qu'elle décolle dépend toujours de la vidéo."),
            ("Que font les abonnés une fois abonnés ?", "Ce que font toujours de vraies personnes : certains regardent chaque vidéo, d'autres likent et commentent, quelques-uns s'éloignent. Sur un mois, {pick_name} apporte en général {pick_likes} likes et {pick_comments} commentaires de ces mêmes personnes."),
            ("Acheter des abonnés TikTok vaut-il encore le coup en 2026 ?", "Acheter des bots, non : TikTok supprime sans cesse les faux comptes, donc le compteur fond tandis que le tort fait à votre portée reste. Payer pour que de vraies personnes découvrent votre profil, c'est autre chose, car elles se comportent comme l'audience que vous gagneriez par vous-même."),
        ],
    },
    {
        "service": "followers",
        "modifier": "real",
        "slug": "tiktok/abonnes/vrais",
        "label": "Vrais abonnés TikTok",
        "title": "Acheter de vrais abonnés TikTok qui interagissent | Growsterr",
        "description": "Achetez de vrais abonnés TikTok : des personnes actives qui ont trouvé vos vidéos, choisi de vous suivre, et qui likent et commentent. Packs dès {from_price}.",
        "h1": ("Acheter de vrais abonnés TikTok : ", "actifs, authentiques et là par choix."),
        "intro": "Quand vous achetez de vrais abonnés TikTok chez nous, chacun est une personne : quelqu'un qui a vu votre profil grâce à notre campagne, regardé quelques vidéos et décidé de s'abonner. Ils sont actifs comme le sont de vraies personnes : ils likent et commentent quand quelque chose les touche, et restent discrets quand une vidéo n'est pas pour eux.",
        "hero": {"image": "tiktok-likes", "alt": "Des cœurs et de nouveaux abonnements de vraies personnes s'accumulent sur un profil TikTok"},
        "sections": [
            {
                "h2": "Ce qui fait un vrai abonné TikTok",
                "ul": [
                    "Une personne derrière le compte, avec ses propres vidéos, ses likes et son historique.",
                    "Une raison de s'abonner : elle a d'abord regardé vos vidéos.",
                    "Un choix personnel : personne ne l'a payée, et personne n'attend d'abonnement en retour.",
                    "Un rythme humain : les abonnés arrivent quelques-uns à la fois, comme on découvre tout ce qui vaut la peine d'être suivi.",
                ],
            },
            {
                "h2": "Des abonnés actifs, définis honnêtement",
                "p": [
                    "Personne ne peut rendre une personne active. Quand un service vend des abonnés actifs par milliers, il décrit des comptes qui likent selon un programme. Les vraies personnes interagissent quand quelque chose les accroche, ce qui est moins prévisible et vaut bien davantage.",
                    "Sur un mois, les personnes qu'apporte {pick_name} laissent en général {pick_likes} likes et {pick_comments} commentaires. Voilà à quoi ressemble l'interaction sincère de {pick_audience} nouveaux abonnés.",
                ],
            },
            {
                "h2": "Haute qualité veut dire bonne affinité",
                "p": [
                    "Un abonné de haute qualité est quelqu'un qui pourrait regarder votre prochaine vidéo. Tout tient à l'affinité : où il vit, la langue qu'il parle, ce qu'il aime regarder. Vous choisissez le lieu, et vos vidéos font le reste du tri, car les gens ne suivent que ce qui leur parle.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Un créateur lit les commentaires de nouveaux abonnés TikTok entre deux prises"},
            },
        ],
        "faqs": [
            ("Comment savoir si les abonnés sont réels ?", "Regardez-les. Parcourez quelques nouveaux abonnés : vous trouverez des profils avec leurs propres vidéos et leurs likes. Observez aussi vos vues et vos likes, car de vrais abonnés les font bouger. Votre tableau de bord montre les visites et abonnements apportés chaque jour par notre campagne."),
            ("Chaque abonné va-t-il liker et commenter ?", "Non, et c'est normal. Certaines personnes réagissent à presque tout, d'autres regardent surtout. Nos fourchettes mensuelles habituelles de likes et de commentaires viennent de ce que font de vraies audiences, pas d'un script."),
            ("De vrais abonnés coûtent-ils plus cher que des bots ?", "Oui, car toucher une vraie personne a un coût. {starter_name} coûte {starter_price} par mois pour, en général, {starter_audience} nouveaux abonnés. Les bots coûtent moins cher pour la raison la plus simple : il n'y a personne."),
            ("D'où viennent les vrais abonnés ?", "De l'endroit où vous dirigez la campagne, qu'il s'agisse d'une ville, d'une région plus large ou d'un pays entier. Ils découvrent votre profil grâce à nos campagnes sponsorisées, puis s'abonnent sur TikTok comme n'importe qui."),
            ("Puis-je acheter de vrais abonnés pour un compte tout neuf ?", "Oui, mais publiez d'abord quelques vidéos. Les gens décident selon ce qu'ils trouvent sur votre profil, et une grille vide ne leur donne rien à suivre."),
        ],
    },
    {
        "service": "followers",
        "modifier": "organic",
        "slug": "tiktok/abonnes/organiques",
        "label": "Abonnés TikTok organiques",
        "title": "Acheter des abonnés TikTok organiques | Growsterr",
        "description": "Des abonnés TikTok organiques, en toute transparence : nous payons pour montrer votre profil à de vraies personnes là où vous voulez. Elles décident seules.",
        "h1": ("Acheter des abonnés TikTok organiques : ", "visibilité payée, décision libre."),
        "intro": "Peut-on acheter des abonnés TikTok organiques ? Voici exactement ce que nous faisons. Nous payons des campagnes sponsorisées qui présentent votre profil à de vraies personnes, dans le lieu de votre choix, via notre réseau partenaire. Tout ce qui suit est organique : les gens regardent, se font un avis et s'abonnent s'ils en veulent plus.",
        "hero": {"image": "tiktok-creator", "alt": "Un créateur local filme une vidéo TikTok pour les spectateurs de sa propre ville"},
        "sections": [
            {
                "h2": "Ce qui est payé, et ce qui ne l'est pas",
                "p": [
                    "L'exposition est payée. La décision ne l'est pas. Personne n'est récompensé pour vous suivre, personne ne s'abonne dans le cadre d'un échange, et aucun compte ne s'abonne selon un script. C'est la frontière entre abonnés organiques et abonnés achetés.",
                    "En pratique, cela ressemble beaucoup à un créateur qui promeut son propre profil, avec une équipe qui mène la campagne et un tableau de bord qui montre ce qui a été mesuré.",
                ],
            },
            {
                "h2": "Des abonnés TikTok ciblés par lieu",
                "p": [
                    "Le ciblage se fait par lieu. Indiquez une ville, une région ou un pays entier : c'est là que votre profil est montré en premier. Une boulangerie à Nantes veut des gens à Nantes ; un professeur de langue veut les pays où vivent ses élèves. Quand les personnes les plus adaptées sont plus dispersées, certains abonnés peuvent venir des environs.",
                ],
            },
            {
                "h2": "De vrais abonnés TikTok, chaque jour",
                "ul": [
                    "Quelques nouvelles personnes trouvent votre profil chaque jour du mois.",
                    "Chacune arrive par vos vidéos : elle sait à quoi elle s'abonne.",
                    "Votre tableau de bord liste les visites et abonnements de chaque jour, pour que vous voyiez la progression.",
                ],
            },
        ],
        "faqs": [
            ("Est-ce organique si vous payez la campagne ?", "Vous payez la portée. L'abonnement lui-même est organique : les gens voient votre profil, regardent ce qui les intéresse et décident seuls, et personne ne reçoit rien pour s'abonner. C'est ce qui rend un abonnement organique."),
            ("En quoi est-ce différent du « follow pour follow » ?", "Le follow pour follow est un échange : on vous suit pour obtenir quelque chose en retour, et beaucoup se désabonnent une fois servis. Notre campagne ne demande rien à personne. Les gens s'abonnent parce qu'ils veulent en voir plus."),
            ("Que puis-je cibler en dehors du lieu ?", "Vous choisissez un lieu, d'une simple ville à un pays entier. À l'intérieur, vos vidéos font le tri. Les personnes qui s'arrêtent et s'abonnent sont celles que votre contenu attire, ce qu'aucun réglage ne saurait aussi bien repérer."),
            ("Les abonnés organiques vont-ils interagir avec mes vidéos ?", "Beaucoup, à leur façon : sur un mois avec {pick_name}, les personnes qui s'abonnent laissent généralement {pick_likes} likes et {pick_comments} commentaires à elles toutes."),
            ("À quel rythme arrivent les abonnés organiques ?", "Un peu chaque jour, des premiers jours de votre campagne jusqu'à la fin du mois. Organique ne veut jamais dire tout d'un coup."),
        ],
    },
    {
        "service": "followers",
        "modifier": "monthly",
        "slug": "tiktok/abonnes/mensuels",
        "label": "Abonnés TikTok mensuels",
        "title": "Abonnés TikTok chaque mois, sur abonnement | Growsterr",
        "description": "Achetez des abonnés TikTok chaque mois grâce à un abonnement qui amène de vraies personnes au quotidien. Payé par carte via Stripe, résiliable à tout moment.",
        "h1": ("Acheter des abonnés TikTok chaque mois. ", "Une croissance qui se renouvelle d'elle-même."),
        "intro": "Acheter des abonnés TikTok chaque mois, c'est exactement notre façon de travailler. Vous choisissez un pack, il tourne pendant 30 jours et se renouvelle jusqu'à ce que vous l'arrêtiez. Chaque jour de chaque mois, de nouvelles personnes tombent sur votre profil, et celles qui veulent voir plus de vos vidéos s'abonnent.",
        "hero": {"image": "tiktok-likes", "alt": "Un nombre d'abonnés TikTok qui grimpe mois après mois grâce à de vraies personnes"},
        "sections": [
            {
                "h2": "Pourquoi la croissance se vend au mois",
                "p": [
                    "De vraies personnes n'arrivent pas sur commande. Elles tombent sur un profil, regardent quelques vidéos et décident, et cela prend des jours. Un lot d'abonnés ponctuel ne peut donc être fait que de bots. Le mois est l'unité naturelle d'une vraie croissance : assez long pour qu'on vous trouve, assez court pour changer de cap.",
                    "Chaque mois s'appuie aussi sur le précédent. Les abonnés du premier mois voient vos nouvelles vidéos, et ceux qui les partagent peuvent attirer des personnes à qui nous n'avons jamais montré votre profil.",
                ],
            },
            {
                "h2": "Comment fonctionne la facturation mensuelle",
                "ul": [
                    "Vous payez par carte via Stripe ; Apple Pay et Google Pay fonctionnent aussi sur les appareils qui les proposent.",
                    "Votre compte indique la date du prochain renouvellement.",
                    "Résilier depuis votre compte arrête le prochain paiement ; le mois payé va jusqu'à son terme.",
                    "Vous ne payez que le pack choisi, sans rien d'ajouté.",
                ],
            },
            {
                "h2": "Le deuxième mois et la suite",
                "p": [
                    "Le premier mois lance la campagne. Au deuxième et au troisième, votre tableau de bord dessine une tendance lisible : quelles semaines ont apporté plus de visites, quelles vidéos ont transformé des visiteurs en abonnés. C'est le moment où il est le plus simple de décider de rester, de monter en gamme ou d'arrêter.",
                ],
            },
        ],
        "faqs": [
            ("Dois-je recommander chaque mois ?", "Non. Votre pack se renouvelle à sa date et la campagne continue sans interruption. Vous n'avez à agir que pour changer ou résilier."),
            ("Y a-t-il une durée minimale ?", "Non. Vous pouvez résilier après le premier mois ou rester aussi longtemps que cela vous aide. Résilier arrête le prochain paiement, et le mois déjà payé continue jusqu'à son dernier jour."),
            ("Recevrai-je le même nombre d'abonnés chaque mois ?", "Pas exactement. Chaque pack a une fourchette habituelle, comme {pick_audience} par mois avec {pick_name}, et de vraies personnes rendent chaque mois un peu différent."),
            ("Que montre mon tableau de bord chaque mois ?", "Les visites de profil apportées chaque jour par votre campagne, les nouveaux abonnés qu'elles ont amenés et votre nombre d'abonnés actuel. Mois après mois, c'est la trace de ce que le pack a fait."),
            ("Quels moyens de paiement pour un pack mensuel ?", "La carte via Stripe, et Apple Pay ou Google Pay sur les téléphones et navigateurs qui les proposent. Un abonnement exige un moyen de paiement renouvelable chaque mois, c'est pourquoi nous n'acceptons pas d'options ponctuelles comme le virement bancaire."),
        ],
    },
    {
        "service": "followers",
        "modifier": "gradual",
        "slug": "tiktok/abonnes/progressifs",
        "label": "Abonnés TikTok progressifs",
        "title": "Acheter des abonnés TikTok progressivement | Growsterr",
        "description": "Achetez des abonnés TikTok progressivement : de vraies personnes découvrent votre profil et s'abonnent peu à peu, chaque jour pendant 30 jours.",
        "h1": ("Acheter des abonnés TikTok progressivement, ", "au rythme où l'on s'abonne vraiment."),
        "intro": "Si vous voulez acheter des abonnés TikTok progressivement plutôt qu'en un bond suspect, un pack mensuel fonctionne ainsi par nature. Chaque jour, de vraies personnes tombent sur votre profil, et celles qui l'aiment s'abonnent. Rien n'est retenu ni libéré selon un minuteur : un rythme lent et quotidien, c'est simplement ainsi que les gens se comportent.",
        "hero": {"image": "tiktok-likes", "alt": "La courbe d'abonnés d'un compte TikTok monte doucement, quelques vraies personnes chaque jour"},
        "sections": [
            {
                "h2": "Goutte-à-goutte ou vrai rythme quotidien",
                "p": [
                    "Beaucoup de services proposent un goutte-à-goutte : les mêmes bots, libérés par petits lots pour que le bond paraisse plus petit. Les abonnés restent des comptes qui ne regardent jamais. Les étaler ne fait que masquer la livraison un moment.",
                    "Notre rythme quotidien n'est pas un réglage. Il vient de personnes qui voient votre profil ce jour-là et décident, une par une.",
                ],
            },
            {
                "h2": "À quoi ressemble la progression sur votre profil",
                "ul": [
                    "Votre nombre d'abonnés monte un peu presque chaque jour, avec des jours calmes et des jours plus chargés.",
                    "Les vues et les likes progressent en parallèle, car ce sont les mêmes personnes qui regardent.",
                    "Votre tableau de bord montre les visites de profil et les nouveaux abonnés de chaque jour : vous voyez la pente par vous-même.",
                ],
            },
            {
                "h2": "Pourquoi une croissance lente est celle qui dure",
                "p": [
                    "Les comptes qui grandissent régulièrement ont tendance à garder l'audience qu'ils gagnent. Chaque nouvel abonné arrive grâce à une vidéo qu'il a aimée, donc votre prochaine vidéo a déjà quelqu'un qui l'attend.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Un créateur publie son TikTok du jour pendant qu'une audience fidèle se construit"},
            },
        ],
        "faqs": [
            ("Combien de nouveaux abonnés apporte une seule journée ?", "Cela varie. Sur un mois entier, {pick_name} ajoute en général {pick_audience} nouveaux abonnés ; certains jours en apportent plus, d'autres moins, selon qui voit votre profil et ce que vous avez publié récemment."),
            ("Puis-je régler la vitesse de livraison ?", "Non, car il n'y a pas de livraison à freiner. Les gens s'abonnent quand ils le choisissent. Ce que vous choisissez, c'est le pack, et avec lui le nombre de personnes qui voient votre profil chaque mois."),
            ("Une livraison lente est-elle plus sûre pour mon compte ?", "Le rythme n'est qu'une partie de la question. Un filet lent de bots reste des bots. Ce qui garde un compte sain, c'est que chaque abonné soit une personne qui a choisi de s'abonner, et c'est le seul genre que nous apportons."),
            ("Quand arrivent les premiers abonnés ?", "Votre campagne démarre une fois la commande passée, et les premières visites de profil apparaissent généralement dans les premiers jours. Les abonnés naissent de ces visites, une personne après l'autre."),
            ("La croissance progressive s'arrête-t-elle après 30 jours ?", "Chaque pack tourne sur 30 jours et se renouvelle chaque mois : le rythme quotidien se poursuit donc le mois suivant, jusqu'à ce que vous résiliiez."),
        ],
    },
    {
        "service": "followers",
        "modifier": "no-drop",
        "slug": "tiktok/abonnes/sans-perte",
        "label": "Abonnés TikTok qui restent",
        "title": "Abonnés TikTok sans perte : les vrais restent | Growsterr",
        "description": "Des abonnés TikTok sans perte : de vraies personnes abonnées par choix ne disparaissent pas lors des purges de bots. Ce qui reste, ce qui part, et pourquoi.",
        "h1": ("Acheter des abonnés TikTok sans perte. ", "Commencez par des gens sincères."),
        "intro": "Ceux qui veulent acheter des abonnés TikTok sans perte en ont souvent assez de voir un chiffre fondre. Cela arrive quand les abonnés sont des bots et que TikTok fait le ménage. Nos abonnés sont de vraies personnes qui ont choisi de s'abonner : un nettoyage n'a rien à supprimer. Quelques-uns se désabonneront peut-être plus tard, comme évolue toute vraie audience.",
        "hero": {"image": "tiktok-likes", "alt": "Un nombre d'abonnés TikTok qui tient bon après un mois de vraie croissance"},
        "sections": [
            {
                "h2": "D'où viennent les chutes",
                "p": [
                    "Les chutes soudaines ont une cause habituelle : la suppression de faux comptes. TikTok les efface régulièrement, et chaque abonnement qu'ils portaient disparaît avec eux. Les services proposent alors des recharges, c'est-à-dire davantage de bots en attente du prochain nettoyage.",
                    "Les vrais abonnés ne partent pas par vagues. Certains s'éloignent avec le temps, un à un, pour les raisons habituelles : ils ont perdu l'intérêt, ou ils ont fait le tri dans leurs abonnements.",
                ],
            },
            {
                "h2": "Personne ne peut vous vendre des abonnés permanents",
                "p": [
                    "Méfiez-vous de quiconque vend des abonnés TikTok permanents. Une vraie personne peut toujours changer d'avis, donc une promesse de zéro désabonnement n'a de sens que pour des comptes qui ne pensent pas du tout. Ce que nous pouvons dire, c'est que les gens qui ont choisi de s'abonner ont tendance à rester, puisqu'ils l'ont fait pour vos vidéos.",
                ],
            },
            {
                "h2": "Comment garder les abonnés qui restent",
                "ul": [
                    "Continuez à publier le genre de vidéo qui les a fait s'abonner.",
                    "Répondez aux commentaires : on reste là où l'on se sent écouté.",
                    "Si vous changez de thématique, faites-le progressivement plutôt que du jour au lendemain.",
                    "Publiez assez souvent pour qu'ils n'oublient pas que vous êtes là.",
                ],
            },
        ],
        "faqs": [
            ("Vais-je perdre certains des abonnés que vous apportez ?", "Peut-être quelques-uns, comme évolue toute vraie audience. Ce que vous ne verrez pas, c'est une vague soudaine de pertes, car il n'y a pas de faux comptes que TikTok pourrait supprimer."),
            ("Proposez-vous des recharges ?", "Non. Les recharges servent à remplacer des bots supprimés, et il n'y en a aucun ici. Nos abonnés sont des personnes, et votre pack continue d'en amener de nouvelles chaque jour où il tourne."),
            ("Est-ce que je garde les abonnés après la résiliation ?", "Ils restent les vôtres. La résiliation met fin à la campagne à la fin de votre mois payé ; les personnes qui vous suivent continuent de le faire tant qu'elles aiment vos vidéos."),
            ("Vos abonnés TikTok sont-ils permanents ?", "Aucun vrai abonné n'est permanent par contrat, les nôtres compris. Ce sont des personnes, et une personne peut se désabonner. Ce sont aussi les seuls abonnés qui ne disparaissent pas lors d'un nettoyage."),
            ("Comment repérer des bots parmi mes abonnés actuels ?", "Ouvrez quelques profils. Les vrais abonnés ont leurs propres vidéos, des likes et un historique. Les bots n'ont souvent aucune vidéo, un nom aléatoire et des milliers d'abonnements. Vos vues vous renseignent aussi : de vrais abonnés les font bouger, pas les bots."),
        ],
    },
    {
        "service": "followers",
        "modifier": "safe",
        "slug": "tiktok/abonnes/fiables",
        "label": "Abonnés TikTok en toute sécurité",
        "title": "Abonnés TikTok sans risque : aucun mot de passe | Growsterr",
        "description": "Acheter des abonnés TikTok de façon fiable : aucun mot de passe, aucune connexion, que de vraies personnes, paiement via Stripe, résiliable à tout moment.",
        "h1": ("Acheter des abonnés TikTok en toute sécurité, ", "sans confier votre compte."),
        "intro": "Pour acheter des abonnés TikTok en toute sécurité, la première règle est simple : votre compte reste entre vos mains. Il nous faut seulement votre nom d'utilisateur. Nous ne demandons jamais de mot de passe, ne nous connectons jamais et ne faisons rien tourner sur votre compte. De vraies personnes découvrent votre profil et décident elles-mêmes.",
        "hero": {"image": "tiktok-creator", "alt": "Un créateur garde la main sur son compte TikTok pendant qu'il grandit avec de vrais abonnés"},
        "sections": [
            {
                "h2": "Sans risque pour votre compte",
                "p": [
                    "Le risque, avec la plupart des services d'abonnés, n'est pas le bouton S'abonner. C'est ce qui l'accompagne : des mots de passe confiés à des inconnus, des applis qui se connectent à votre place, des bots qui disparaissent et laissent votre engagement sonner creux. Rien de tout cela ici.",
                    "Côté TikTok, chaque nouvel abonné est une personne qui a visité votre profil et appuyé sur S'abonner. Rien ne se passe à l'intérieur de votre compte, il n'y a donc rien à nettoyer ensuite.",
                ],
            },
            {
                "h2": "Comment reconnaître un site fiable pour acheter des abonnés TikTok",
                "ul": [
                    "Il ne demande jamais votre mot de passe, ni de vous connecter avec TikTok.",
                    "Il ne promet pas des milliers d'abonnés en quelques minutes.",
                    "Il nomme la société qui se trouve derrière.",
                    "Il encaisse via un prestataire de paiement connu et vous laisse résilier vous-même.",
                    "Il parle en fourchettes habituelles, pas en chiffres exacts, car on ne compte pas de vraies personnes à l'avance.",
                ],
            },
            {
                "h2": "Qui est derrière Growsterr",
                "p": [
                    "Derrière Growsterr se trouve Sterr Agency : la société est Sterr Technologies OÜ, immatriculée à Tallinn, en Estonie, et notre siège est en Turquie. Les paiements passent par le paiement sécurisé de Stripe : carte, Apple Pay ou Google Pay. Quand vous avez une question, une personne vous répond sur WhatsApp ou par e-mail.",
                ],
            },
        ],
        "faqs": [
            ("Cela peut-il causer des ennuis à mon compte TikTok ?", "Nous ne touchons jamais à votre compte : pas de mot de passe, pas de connexion, pas d'automatisation. Ce qui arrive sur votre profil, ce sont des personnes qui visitent et s'abonnent, comme quand l'une de vos vidéos est partagée. Nous ne pouvons pas parler au nom de TikTok, mais de votre côté il n'y a rien d'autre que davantage de vrais visiteurs."),
            ("Growsterr est-il fiable ?", "Nous sommes une société immatriculée, Sterr Technologies OÜ à Tallinn, en Estonie, derrière la marque Sterr Agency. Vous payez via Stripe, suivez votre campagne sur un tableau de bord de chiffres mesurés et résiliez depuis votre compte quand vous voulez."),
            ("Mon paiement est-il sécurisé ?", "Le paiement passe par le paiement sécurisé de Stripe : votre numéro de carte complet ne nous parvient jamais. Vous pouvez payer par carte, Apple Pay ou Google Pay."),
            ("Quelles informations demandez-vous ?", "Votre nom d'utilisateur TikTok, l'endroit d'où doit venir votre audience, ainsi qu'un e-mail, un numéro de téléphone et un mot de passe pour votre compte Growsterr. Jamais votre mot de passe TikTok."),
            ("Et si je ne suis pas satisfait ?", "Résiliez depuis votre compte et le pack ne se renouvellera pas. Votre mois payé continue jusqu'à son dernier jour et n'est pas remboursé : vous gardez donc tout ce qu'il apporte."),
        ],
    },
    {
        "service": "followers",
        "modifier": "private-account",
        "slug": "tiktok/abonnes/compte-prive",
        "label": "Abonnés TikTok pour un compte privé",
        "title": "Acheter des abonnés TikTok pour un compte privé ? | Growsterr",
        "description": "Vous voulez acheter des abonnés TikTok pour un compte privé ? On ne peut qu'y envoyer des demandes : nous vous demandons de rester public pendant le pack.",
        "h1": ("Acheter des abonnés TikTok sur un compte privé ? ", "Voici comment ça marche."),
        "intro": "Vous pensez acheter des abonnés TikTok pour un compte privé ? De vraies personnes ne peuvent pas simplement suivre un profil privé : elles peuvent seulement envoyer une demande, et ne voient vos vidéos qu'après votre accord. C'est pourquoi nos campagnes fonctionnent sur des comptes publics, et pourquoi nous vous demandons de garder le vôtre public pendant votre pack.",
        "hero": {"image": "tiktok-creator", "alt": "Un créateur fait passer son compte TikTok de privé à public avant une campagne"},
        "sections": [
            {
                "h2": "Pourquoi compte privé et vraie croissance ne vont pas ensemble",
                "p": [
                    "Quand quelqu'un arrive sur un compte TikTok privé, il voit un nom, une photo et un cadenas. Aucune vidéo, rien sur quoi se décider : la plupart des visiteurs repartent. La poignée qui envoie une demande attend que vous l'acceptiez, et une pile de demandes qui grossit passe facilement inaperçue.",
                    "Un service qui prétend faire grandir un compte privé sans que vous acceptiez chaque demande se connecte à votre place pour les accepter, ou n'ajoute rien du tout.",
                ],
            },
            {
                "h2": "Vos options si la confidentialité compte",
                "ul": [
                    "Passez en public pendant les mois où votre pack tourne, puis décidez.",
                    "Gardez un compte privé séparé pour vos amis et votre famille, et faites grandir le compte public.",
                    "Rendez vos vidéos personnelles visibles par vos amis ou par vous seul, et laissez le reste ouvert aux nouvelles personnes.",
                ],
            },
        ],
        "faqs": [
            ("Pouvez-vous faire grandir un compte TikTok privé ?", "Pas bien, et nous ne prétendrons pas le contraire. De vraies personnes doivent voir vos vidéos avant de décider, et un profil privé les cache. Gardez-le public pendant que le pack tourne."),
            ("Dois-je accepter les demandes d'abonnement ?", "Seulement sur un compte privé, c'est pourquoi nous vous demandons de passer en public. Sur un compte public, les gens s'abonnent directement et vous n'avez rien à faire."),
            ("Puis-je repasser en privé après le mois ?", "Oui. Les abonnés déjà acquis restent. Les nouvelles personnes pourront de nouveau seulement envoyer des demandes, donc la croissance se limitera à ce que vous acceptez."),
            ("Avez-vous besoin de mes identifiants pour accepter les demandes à ma place ?", "Non, et personne ne devrait en avoir besoin. Nous ne demandons jamais votre mot de passe et ne nous connectons jamais à votre compte. Quiconque propose de gérer vos demandes depuis votre compte veut plus d'accès qu'un service de croissance n'en a besoin."),
            ("Certaines de mes vidéos peuvent-elles rester privées ?", "Oui. TikTok vous laisse choisir qui peut regarder chaque vidéo. Gardez votre profil public pour être découvert, et limitez les quelques vidéos personnelles."),
        ],
    },
    {
        "service": "followers",
        "modifier": "live",
        "plan": "starter",
        "slug": "tiktok/abonnes/live",
        "label": "Abonnés TikTok pour faire des LIVE",
        "title": "Acheter des abonnés TikTok pour faire des LIVE | Growsterr",
        "description": "Le LIVE TikTok demande 1 000 abonnés. Atteignez-les avec de vraies personnes : {starter_name} en apporte en général {starter_audience} par mois.",
        "h1": ("Acheter des abonnés TikTok pour faire des LIVE, ", "et avoir quelqu'un pour qui le faire."),
        "intro": "Acheter des abonnés TikTok pour faire des LIVE n'a de sens que si ces abonnés peuvent venir. TikTok demande 1 000 abonnés avant de débloquer le LIVE, et nos packs vous y amènent avec de vraies personnes qui ont trouvé vos vidéos et décidé de s'abonner. Un mois de {starter_name} en ajoute en général {starter_audience}.",
        "hero": {"image": "tiktok-creator", "alt": "Un créateur installe son téléphone et un anneau lumineux pour son premier LIVE TikTok"},
        "sections": [
            {
                "h2": "Le cap des 1 000 abonnés, et pourquoi les bots ne le débloquent pas vraiment",
                "p": [
                    "Des abonnés bots peuvent faire passer le chiffre au-dessus de 1 000, mais un LIVE est une salle, et les bots n'y entrent pas. Vous diffuseriez devant un compteur qui n'affiche personne. TikTok supprime aussi les faux comptes par vagues, et le compteur peut repasser sous la barre.",
                    "Les vrais abonnés, c'est différent. Ils se sont abonnés parce qu'ils aimaient vos vidéos, et quand vous lancez un LIVE, ce sont eux qui ont le plus de chances de le remarquer et de passer.",
                ],
            },
            {
                "h2": "Se préparer au LIVE pendant que vous grandissez",
                "ul": [
                    "Regardez l'option LIVE dans votre appli : TikTok impose aussi une condition d'âge et ses propres règles pour les diffusions.",
                    "Continuez à publier pendant que le pack tourne, pour que les nouveaux abonnés aient une raison de rester.",
                    "Annoncez dans vos vidéos qu'un premier LIVE arrive.",
                    "Construisez ce premier direct autour de quelque chose de concret : des questions-réponses, un tutoriel, des coulisses.",
                ],
            },
            {
                "h2": "Après le cap des 1 000",
                "p": [
                    "Votre pack continue de mois en mois jusqu'à ce que vous résiliiez, donc l'audience continue de grandir après le déblocage du LIVE. Nous n'envoyons pas de spectateurs sur un direct à heure fixe ; qui rejoint leur appartient. Ce qui grandit, c'est le nombre de personnes susceptibles de venir.",
                ],
            },
        ],
        "faqs": [
            ("Combien de temps avant de pouvoir faire un LIVE ?", "Cela dépend de votre point de départ. {starter_name} apporte en général {starter_audience} nouveaux abonnés par mois : pour un petit compte, le cap est souvent une affaire de semaines. Les gens décident quand s'abonner, donc nous ne pouvons pas donner de date."),
            ("Faut-il toujours 1 000 abonnés pour faire un LIVE ?", "C'est le seuil historique de TikTok, mais c'est TikTok qui fixe les règles et peut les changer ou les tester. L'option LIVE dans votre appli indique ce qui s'applique à votre compte."),
            ("Mes nouveaux abonnés regarderont-ils mon LIVE ?", "Certains, peut-être. Ce sont de vraies personnes abonnées pour vos vidéos, et leur présence dépend de leur journée, comme pour toute audience. Les bots, jamais."),
            ("Pouvez-vous envoyer des spectateurs à mon premier LIVE ?", "Non. Personne ne peut placer de vraies personnes dans un direct à l'heure de votre choix, et les comptes qui rejoignent sur commande restent là en silence. Ce que nous pouvons faire, c'est faire grandir l'audience susceptible de venir."),
            ("Quel pack pour faire des LIVE ?", "{starter_name} suffit généralement pour atteindre le cap. Si vous prévoyez des directs réguliers, {rising_name} fait grandir l'audience plus vite et vous permet de choisir les vidéos qui reçoivent l'attention."),
        ],
    },
    # --- Comments -------------------------------------------------------------------------
    {
        "service": "comments",
        "slug": "tiktok/commentaires",
        "label": "Commentaires TikTok",
        "title": "Acheter des commentaires TikTok, de vrais spectateurs | Growsterr",
        "description": "Acheter des commentaires TikTok, version honnête : de vraies personnes disent ce qu'elles pensent de vos vidéos, en général {starter_comments} par mois.",
        "h1": ("Acheter des commentaires TikTok ? ", "Recevez des gens qui ont quelque chose à dire."),
        "intro": "Si vous êtes venu acheter des commentaires TikTok, voici la version honnête : nous ne vendons pas de commentaires seuls. Chaque pack vous envoie de vraies personnes, et certaines commentent les vidéos qui leur plaisent, avec leurs propres mots. {starter_name} apporte en général {starter_comments} commentaires par mois, les packs supérieurs davantage.",
        "hero": {"image": "tiktok-watch-time", "alt": "Des spectateurs écrivent des commentaires sous une vidéo TikTok qu'ils viennent de regarder"},
        "sections": [
            {
                "h2": "Pourquoi un commentaire ne se commande pas comme un stock",
                "p": [
                    "Un commentaire, c'est quelqu'un qui vous dit ce qu'il a pensé. Dès qu'il est écrit sur commande, il cesse de l'être : la même poignée de phrases, les mêmes emojis, postés par des comptes sans vidéos à eux. Les spectateurs les repèrent et passent leur chemin.",
                    "Les vrais commentaires sont plus désordonnés et bien plus utiles. Ils posent des questions, contredisent, vous resservent votre chute et identifient l'ami qui doit absolument voir ça.",
                ],
            },
            {
                "h2": "Ce que chaque pack apporte en commentaires",
                "ul": [
                    "{starter_name} : en général {starter_comments} commentaires par mois, avec {starter_audience} nouveaux abonnés.",
                    "{rising_name} : en général {rising_comments}, et vous décidez quelles vidéos reçoivent l'attention.",
                    "{pro_name} : en général {pro_comments}, avec une mise en avant prioritaire et une ligne WhatsApp directe avec nous.",
                ],
            },
            {
                "h2": "Faites de vrais commentaires votre prochaine vidéo",
                "p": [
                    "TikTok permet de répondre à un commentaire par une vidéo, et une vraie question d'un spectateur est l'une des idées les plus faciles que vous aurez jamais. Les commentaires scriptés ne posent jamais de question qui mérite une réponse.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Un créateur filme une réponse vidéo à la question d'un spectateur sur TikTok"},
            },
        ],
        "faqs": [
            ("Puis-je avoir des commentaires TikTok sans abonnés ?", "Non. Les commentaires font partie de chaque pack mensuel et viennent des personnes qui vous suivent et vous likent aussi. Ils ne sont pas vendus séparément."),
            ("Puis-je décider de ce que les gens écrivent ?", "Non, et c'est tout l'intérêt : les gens écrivent ce qu'ils pensent vraiment. Pour lancer une conversation, posez une question dans votre légende ou à la fin de la vidéo. Les vrais spectateurs répondent aux questions."),
            ("Quelles vidéos reçoivent des commentaires ?", "Surtout les plus récentes, puisque c'est ce que les gens voient d'abord sur votre profil. Si vous voulez qu'une vidéo concentre la conversation, {rising_name} et {pro_name} vous permettent d'y diriger la campagne."),
            ("Les commentaires seront-ils dans ma langue ?", "Les gens commentent dans la langue qu'ils parlent. Ciblez un lieu où l'on parle votre langue, et c'est généralement ce que vous lirez."),
            ("Les commentaires arrivent-ils tous d'un coup ?", "Non. Ils arrivent au fil du mois, à mesure que les gens découvrent vos vidéos. Une rafale de commentaires dans la première minute sur une vidéo que presque personne n'a vue paraît suspecte à tous ceux qui la voient."),
        ],
    },
    # --- Views ----------------------------------------------------------------------------
    {
        "service": "views",
        "slug": "tiktok/vues",
        "label": "Vues TikTok",
        "title": "Acheter des vues TikTok de gens qui regardent | Growsterr",
        "description": "Des vues TikTok avec de vrais visionnages : des gens découvrent votre profil et regardent vos vidéos, dans un pack qui apporte aussi abonnés et likes.",
        "h1": ("Acheter des vues TikTok ", "de gens qui regardent vraiment."),
        "intro": "Vous cherchez à acheter des vues TikTok ? Nous ne vendons pas de lectures par milliers. Chaque pack envoie de nouveaux spectateurs sur votre profil : ils regardent les vidéos qui les accrochent, aiment ce qui leur plaît et s'abonnent quand ils en veulent plus. Leurs vues font partie du pack, jamais d'un compteur à part.",
        "hero": {"image": "tiktok-watch-time", "alt": "De vraies personnes regardent des vidéos TikTok sur leur téléphone, une vue à la fois"},
        "sections": [
            {
                "h2": "Une vue ne vaut que par le visionnage",
                "p": [
                    "TikTok compte une vue dès qu'une vidéo commence à se lire. Ce qui compte, c'est la suite : le spectateur est-il resté, a-t-il revu la vidéo, l'a-t-il partagée, a-t-il ouvert votre profil ? Des milliers de lectures qui s'arrêtent au bout d'une seconde disent à TikTok l'inverse de ce que vous espériez.",
                    "Les vues de vraies personnes portent le reste de l'histoire, car celui qui a regardé est aussi celui qui pourrait liker, s'abonner ou faire suivre la vidéo.",
                ],
            },
            {
                "h2": "Pourquoi nous ne chiffrons pas les vues",
                "p": [
                    "Les abonnés, les likes et les commentaires ont des fourchettes mensuelles habituelles. Les vues, non, car elles dépendent autant de la vidéo que du spectateur : l'un regarde un clip une fois et passe à autre chose, l'autre le regarde en boucle et en ouvre trois autres. Nous ne vendons donc pas de nombre de vues. Nous amenons les personnes, et vos vidéos font le reste.",
                ],
            },
            {
                "h2": "Où acheter des vues TikTok",
                "ul": [
                    "Une vraie vue vient avec un spectateur : regardez si les likes, les abonnements et les commentaires bougent avec elle.",
                    "Des vues bon marché par milliers sont des lectures, pas des personnes.",
                    "Un site qui a besoin de vos identifiants TikTok pour livrer des vues est un site à quitter.",
                    "Si un service vous montre un tableau de bord, regardez ce qu'il a réellement mesuré.",
                ],
            },
        ],
        "faqs": [
            ("Combien de vues mes vidéos auront-elles ?", "Nous ne comptons pas les vues à l'avance. Elles viennent des vraies personnes qui découvrent votre profil chaque jour, et ce qu'elles regardent dépend de vos vidéos. Ce que nous mesurons et vous montrons, ce sont les visites de profil apportées par votre campagne et les nouveaux abonnés qu'elles ont amenés."),
            ("Puis-je acheter des vues pour une vidéo TikTok précise ?", "Pas seules. Avec {rising_name} et {pro_name}, vous choisissez les vidéos qui reçoivent l'attention : une vidéo qui vous tient à cœur est vue par davantage des personnes que nous amenons."),
            ("Les vues TikTok bon marché font-elles du tort ?", "Elles le peuvent. Les vues de bots sont des lectures sans personne derrière : elles font baisser le temps moyen passé sur votre vidéo, et ce temps fait partie de ce que TikTok pèse pour décider qui verra la vidéo ensuite."),
            ("Faut-il une appli pour acheter des vues TikTok ?", "Non. Tout se passe depuis votre compte Growsterr, dans le navigateur : vous commandez, payez par carte ou avec un portefeuille mobile comme Apple Pay, et consultez votre tableau de bord. Évitez les applis qui veulent que vous vous connectiez avec TikTok pour débloquer des vues."),
            ("Les vues viennent-elles avec des abonnés et des likes ?", "Oui. Les personnes qui regardent vos vidéos sont les mêmes qui s'abonnent et likent : en général {pick_audience} nouveaux abonnés et {pick_likes} likes par mois avec {pick_name}."),
        ],
    },
    # --- Likes (the likes page itself is in tiktok.py) ----------------------------------------
    {
        "service": "likes",
        "modifier": "real",
        "slug": "tiktok/likes/vrais",
        "label": "Vrais likes TikTok",
        "title": "Acheter de vrais likes TikTok, sans aucun bot | Growsterr",
        "description": "Achetez de vrais likes TikTok, sans bots : des spectateurs qui ont regardé votre vidéo et l'ont aimée, dans un pack mensuel avec abonnés et commentaires.",
        "h1": ("Acheter de vrais likes TikTok. ", "Chacun d'une personne qui a regardé."),
        "intro": "Quand vous achetez de vrais likes TikTok via Growsterr, chaque like vient d'une personne, jamais d'un bot : quelqu'un qui a trouvé votre profil grâce à notre campagne, lancé une vidéo et l'a aimée. Les likes viennent dans chaque pack avec abonnés et commentaires, en général {starter_likes} par mois avec {starter_name}.",
        "hero": {"image": "tiktok-likes", "alt": "Un cœur touché par un vrai spectateur à la fin d'une vidéo TikTok"},
        "sections": [
            {
                "h2": "Distinguer les vrais likes des likes de bots",
                "ul": [
                    "Regardez qui a liké : votre activité montre les comptes, et les vrais ont leurs propres photos, vidéos et abonnés.",
                    "Comparez likes et vues : les vrais likes sont une part des personnes qui ont regardé, jamais plus que toutes.",
                    "Observez le moment : les vrais likes arrivent au compte-gouttes sur plusieurs jours, ceux des bots tombent en bloc.",
                    "Voyez ce qui les accompagne : ceux qui likent vraiment commentent, s'abonnent ou partagent parfois.",
                ],
            },
            {
                "h2": "Des likes de haute qualité, définis",
                "p": [
                    "Un like de haute qualité a une vraie vue derrière lui, venant de quelqu'un qui pourrait revenir regarder. Peu importe que le compte paraisse soigné. Ce qui compte, c'est qu'une personne ait choisi votre vidéo et l'ait regardée assez longtemps pour toucher le cœur.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Un spectateur s'arrête sur un clip TikTok qui lui plaît, le pouce au-dessus du cœur"},
            },
            {
                "h2": "Les vrais likes arrivent avec le reste du pack",
                "p": [
                    "Les likes ne sont qu'une partie de ce que font ces mêmes personnes : elles s'abonnent et commentent aussi. Un mois avec {pick_name} représente en général {pick_likes} likes, {pick_audience} nouveaux abonnés et {pick_comments} commentaires, tous de vraies personnes.",
                ],
            },
        ],
        "faqs": [
            ("Les likes viennent-ils de vraies personnes, sans aucun bot ?", "Oui. Nous n'utilisons ni bots, ni faux comptes, ni automatisation, nulle part. Chaque like est laissé par quelqu'un qui a atteint votre vidéo grâce à notre campagne et a décidé de toucher le cœur."),
            ("Puis-je acheter de vrais likes sans abonnés ?", "Non. Les vrais likes ne viennent que de vrais spectateurs, et les vrais spectateurs s'abonnent, commentent et partagent aussi quand ils en ont envie. C'est pourquoi tout vient dans un seul pack."),
            ("Pourquoi ne pouvez-vous pas me dire exactement combien de likes j'aurai ?", "Parce que ce sont les gens qui décident. Nous savons ce que font habituellement de vraies audiences, alors nous donnons des fourchettes, comme {pick_likes} par mois avec {pick_name}. Un chiffre fixe voudrait dire qu'on a demandé à quelqu'un de liker."),
            ("De vrais likes aident-ils mes vidéos à toucher plus de monde ?", "Ils viennent avec ce que les likes de bots n'ont jamais : un vrai temps de visionnage, et parfois un partage ou un abonnement. C'est cet ensemble qui aide une vidéo à voyager ; un simple compteur, non."),
            ("D'où viennent les personnes qui likent mes vidéos ?", "Du lieu que vous nous indiquez lors de la commande, qu'il s'agisse d'une ville, d'une région plus large ou d'un pays entier. Si l'audience la plus proche de la vôtre déborde un peu, certains likes viennent des environs."),
        ],
    },
    {
        "service": "likes",
        "modifier": "organic",
        "slug": "tiktok/likes/organiques",
        "label": "Likes TikTok organiques",
        "title": "Likes TikTok organiques, gagnés par vos vidéos | Growsterr",
        "description": "Achetez des likes TikTok organiques : de vraies personnes arrivent sur votre profil grâce à notre campagne et aiment les vidéos qui le méritent.",
        "h1": ("Acheter des likes TikTok organiques, ", "gagnés vidéo après vidéo."),
        "intro": "Peut-on acheter des likes TikTok organiques ? Vous pouvez payer pour que des gens voient vos vidéos, et c'est ce que font nos packs. Les likes restent organiques parce que chacun est la réaction d'une vraie personne à une vidéo qu'elle a regardée. Personne ne se voit dire quoi aimer, et rien n'est réparti uniformément pour avoir l'air naturel.",
        "hero": {"image": "tiktok-likes", "alt": "Des likes répartis de façon inégale sur les vidéos TikTok d'un créateur, surtout sur la meilleure"},
        "sections": [
            {
                "h2": "À quoi ressemblent des likes organiques",
                "p": [
                    "Les likes organiques sont inégaux. Votre meilleure vidéo en reçoit bien plus que la plus faible, les likes continuent d'arriver sur les anciennes vidéos, et un succès peut entraîner des likes sur tout le reste de votre profil. Les likes achetés sont plats : le même nombre sur chaque vidéo, tous arrivés d'un coup.",
                ],
            },
            {
                "h2": "Vos vidéos décident où vont les likes",
                "ul": [
                    "Les premières secondes décident si quelqu'un reste assez longtemps pour liker.",
                    "Un son que les gens reconnaissent peut suffire à les arrêter dans leur défilement.",
                    "Les sous-titres et le texte à l'écran aident ceux qui regardent sans le son.",
                    "Une fin nette, ou une boucle sans couture, donne envie de revoir.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Un créateur choisit un son pour une vidéo TikTok avant de la publier"},
            },
            {
                "h2": "Ce que le pack ajoute",
                "p": [
                    "Ce que nous ajoutons, ce sont des personnes : un flux régulier de vrais spectateurs venant du lieu de votre choix, chaque jour du mois. Avec {pick_name}, ils laissent en général {pick_likes} likes, avec de nouveaux abonnés et des commentaires.",
                ],
            },
        ],
        "faqs": [
            ("Les likes sont-ils vraiment organiques si je paie ?", "Votre argent achète la possibilité d'être vu. Chaque like reste une décision prise par quelqu'un qui regarde votre vidéo, et c'est ce que veut dire organique. Si une vidéo ne plaît pas, elle en reçoit moins, ce qui est utile à savoir aussi."),
            ("Toutes mes vidéos auront-elles le même nombre de likes ?", "Non. Les likes organiques suivent la qualité, le moment et un peu de chance. Cette irrégularité fait partie de ce qui les rend crédibles."),
            ("Les likes organiques peuvent-ils venir d'un pays précis ?", "Oui. Choisissez une ville, une région ou un pays, et les personnes qui voient votre profil viennent d'abord de là. Leurs likes viennent du même endroit."),
            ("Les likes organiques aident-ils une vidéo à être davantage montrée ?", "TikTok regarde les likes avec le temps de visionnage, les partages et les abonnements. Les likes de personnes qui ont regardé portent ces autres signaux avec eux ; les likes de bots n'en portent aucun."),
            ("En quoi est-ce différent des groupes d'engagement ?", "Les groupes d'engagement échangent des likes : vous aimez les leurs, ils aiment les vôtres. Les comptes sont réels, mais pas l'intérêt. Nos spectateurs ne vous doivent rien : quand ils aiment une vidéo, ils le pensent."),
        ],
    },
    {
        "service": "likes",
        "modifier": "monthly",
        "slug": "tiktok/likes/mensuels",
        "label": "Likes TikTok mensuels",
        "title": "Likes TikTok au mois, pas des auto-likes | Growsterr",
        "description": "Achetez des likes TikTok chaque mois, de vraies personnes : un pack renouvelé chaque mois qui amène des spectateurs sur chaque nouvelle vidéo. Aucun script.",
        "h1": ("Acheter des likes TikTok chaque mois. ", "De vraies personnes, pas un auto-liker."),
        "intro": "Vous voulez acheter des likes TikTok chaque mois pour donner un départ à chaque nouvelle vidéo ? C'est ce que font nos packs, avec une différence par rapport aux auto-likes : il n'y a pas de script. Le pack se renouvelle seul chaque mois, et chaque jour de vraies personnes découvrent votre profil, regardent et aiment les vidéos qui leur plaisent.",
        "hero": {"image": "tiktok-likes", "alt": "Des likes de vrais spectateurs arrivent sur les dernières vidéos TikTok d'un créateur"},
        "sections": [
            {
                "h2": "Auto-likes ou pack mensuel",
                "p": [
                    "Les auto-likes TikTok surveillent votre compte et envoient un nombre fixe de likes sur chaque nouvelle vidéo en quelques minutes. Chaque publication reçoit le même nombre, de comptes qui ne l'ont jamais regardée. Ça a l'air automatique parce que ça l'est.",
                    "Un pack mensuel n'est automatique qu'au seul endroit où il doit l'être : la facturation. Vous ne recommandez pas, et votre campagne ne s'interrompt pas entre deux mois. Les likes, eux, restent humains : une excellente vidéo en reçoit plus, une vidéo discrète moins.",
                ],
            },
            {
                "h2": "À quoi ressemble un mois de likes",
                "ul": [
                    "Des likes répartis sur 30 jours et sur les vidéos que les gens choisissent de regarder.",
                    "Vos vidéos les plus fortes en récoltent le plus, comme il se doit.",
                    "Les nouvelles vidéos rencontrent une audience fraîche, car de nouvelles personnes trouvent votre profil chaque jour.",
                    "{rising_name} et {pro_name} vous laissent choisir les vidéos qui comptent le plus ce mois-ci.",
                ],
            },
            {
                "h2": "Pourquoi un rythme mensuel convient à TikTok",
                "p": [
                    "Sur TikTok, les créateurs travaillent par cycles : une série, un format hebdomadaire, un lancement. Un pack mensuel s'y adapte. Chaque mois, vous voyez ce que votre tableau de bord a mesuré, regardez quelles vidéos les gens ont aimées et décidez sur quoi le mois suivant doit porter.",
                ],
            },
        ],
        "faqs": [
            ("Chaque nouvelle vidéo recevra-t-elle des likes automatiquement ?", "Pas selon un calendrier. Les nouvelles vidéos sont vues par les personnes qui découvrent votre profil ce jour-là, et elles aiment ce qui leur plaît. Certaines vidéos en récoltent beaucoup, d'autres moins : c'est ainsi que se comporte une vraie audience."),
            ("Combien de likes vais-je recevoir chaque mois ?", "{starter_name} en apporte en général {starter_likes} par mois, {rising_name} {rising_likes} et {pro_name} {pro_likes}, tous de personnes qui vous suivent."),
            ("Dois-je vous prévenir quand je publie ?", "Non. La campagne montre votre profil, et les gens voient ce qu'il y a de plus récent. Si une vidéo compte plus que les autres, {rising_name} et {pro_name} vous permettent d'y diriger l'attention."),
            ("Qu'est-ce qui ne va pas avec les auto-likes ?", "Ils tombent quelques minutes après la publication, toujours au même nombre, venant de comptes qui n'ont jamais regardé. Des likes sans temps de visionnage derrière eux et un nombre identique sur chaque vidéo forment un schéma que n'importe qui sait lire."),
            ("Puis-je arrêter les likes mensuels ?", "Oui. Résilier depuis votre compte met fin aux renouvellements ; le mois en cours va quand même jusqu'à son dernier jour."),
        ],
    },
    {
        "service": "likes",
        "modifier": "gradual",
        "slug": "tiktok/likes/progressifs",
        "label": "Likes TikTok progressifs",
        "title": "Acheter des likes TikTok lents et naturels | Growsterr",
        "description": "Des likes TikTok lents et naturels : de vraies personnes aiment vos vidéos en petit nombre, jour après jour, dans un pack avec abonnés et commentaires.",
        "h1": ("Acheter des likes TikTok lentement, ", "comme les donnent de vrais spectateurs."),
        "intro": "Ceux qui achètent des likes TikTok lentement veulent qu'ils aient l'air naturels. Le plus simple, c'est qu'ils le soient. Chaque jour du mois, notre campagne amène de nouveaux spectateurs sur votre profil ; ils regardent et aiment ce qui leur plaît, quelques-uns à la fois. {pick_name} représente en général {pick_likes} likes sur le mois.",
        "hero": {"image": "tiktok-likes", "alt": "Quelques likes à la fois apparaissent sur une vidéo TikTok pendant plusieurs jours"},
        "sections": [
            {
                "h2": "Comment les vrais likes s'étalent sur la vie d'une vidéo",
                "p": [
                    "Une vraie vidéo ne reçoit pas tous ses likes dans la première heure. Les gens la trouvent sur votre profil des jours plus tard, remontent vers les anciennes vidéos et aiment celles qu'ils avaient ratées. Cette longue traîne, c'est à cela que ressemble une attention sincère, et c'est exactement ce qui manque à un lot soudain de likes.",
                ],
            },
            {
                "h2": "Pourquoi la livraison progressive n'est pas le sujet",
                "p": [
                    "Certains services vendent une livraison progressive : les mêmes likes de bots, libérés sur quelques heures. Le rythme change, pas les likes. Un like sans vue derrière lui reste vide, aussi lentement qu'il arrive.",
                    "Chez nous, il n'y a rien à libérer. Les likes viennent des personnes qui ont regardé, le jour où elles ont regardé.",
                ],
            },
            {
                "h2": "À quoi s'attendre, semaine après semaine",
                "ul": [
                    "Première semaine : les premiers visiteurs et leurs premiers likes, généralement sur vos vidéos les plus récentes.",
                    "Deuxième et troisième semaines : un flux régulier, à mesure que d'autres personnes trouvent votre profil et remontent le fil.",
                    "Quatrième semaine : un mois de likes répartis sur de nombreuses vidéos plutôt qu'entassés sur une seule.",
                ],
            },
        ],
        "faqs": [
            ("Combien de likes par jour vais-je recevoir ?", "Cela change d'un jour à l'autre. Sur le mois, {starter_name} apporte en général {starter_likes} likes et {rising_name} {rising_likes}, répartis sur 30 jours et sur les vidéos que les gens choisissent de regarder."),
            ("Puis-je choisir à quelle lenteur arrivent les likes ?", "Il n'y a pas de réglage de vitesse, puisque personne ne libère de likes selon un minuteur. Ils arrivent quand les gens regardent. Si vous voulez plus d'attention sur certaines vidéos, {rising_name} et {pro_name} vous permettent de les choisir."),
            ("Pourquoi certaines de mes anciennes vidéos reçoivent-elles aussi des likes ?", "Parce que les vraies personnes explorent. Quelqu'un qui aime une vidéo ouvre souvent votre profil et en regarde quelques autres. Ces likes sont bon signe : ils veulent dire qu'on veut plus de vous."),
            ("Les likes viennent-ils avec des vues ?", "Toujours. Ici, un like signifie qu'une personne a d'abord regardé la vidéo, donc vos vues montent avec. Des likes plus nombreux que les vues d'une vidéo trahissent la présence de bots."),
            ("Les likes continuent-ils après le premier mois ?", "Oui, tant que votre pack se renouvelle. Chaque mois apporte un nouveau flux de spectateurs, et les personnes abonnées les mois précédents continuent souvent d'aimer vos nouvelles vidéos."),
        ],
    },
    {
        "service": "likes",
        "modifier": "no-drop",
        "slug": "tiktok/likes/sans-perte",
        "label": "Likes TikTok qui restent",
        "title": "Des likes TikTok qui restent, de vraies personnes | Growsterr",
        "description": "Des likes TikTok qui restent sur vos vidéos : les likes de vraies personnes ne disparaissent pas quand TikTok supprime les faux comptes. Jamais vendus seuls.",
        "h1": ("Acheter des likes TikTok qui restent, ", "parce qu'une personne les pensait."),
        "intro": "Pour acheter des likes TikTok qui restent, il faut des likes qu'aucun nettoyage ne peut toucher. Quand un faux compte est supprimé, chaque like qu'il a laissé disparaît avec lui. Nos likes viennent de vraies personnes qui ont regardé vos vidéos, dans un pack mensuel, et on retire rarement un like une fois qu'on l'a donné.",
        "hero": {"image": "tiktok-likes", "alt": "Un nombre de likes TikTok qui tient bon semaine après semaine"},
        "sections": [
            {
                "h2": "Pourquoi les likes achetés disparaissent",
                "p": [
                    "Les compteurs de likes baissent pour une raison principale : les comptes derrière eux n'existent plus. TikTok supprime les faux comptes et le faux engagement, et leurs likes partent avec. Une vidéo peut afficher un gros chiffre une semaine et bien moins la suivante, sans que vous ayez rien fait entre-temps.",
                ],
            },
            {
                "h2": "Des likes qui restent, et pourquoi",
                "ul": [
                    "Ils viennent de vrais comptes avec leur propre historique, qu'un nettoyage n'a aucune raison de supprimer.",
                    "Ils viennent de personnes qui ont regardé, donc les vues derrière eux sont réelles aussi.",
                    "Ils sont répartis sur plusieurs jours et plusieurs vidéos, jamais empilés sur une seule.",
                    "Ils appartiennent à des personnes qui s'abonnent souvent aussi : ils sont liés à une vraie audience.",
                ],
            },
            {
                "h2": "Si vous avez déjà acheté des likes",
                "p": [
                    "Vous ne pouvez pas retirer des likes vous-même, et vous n'en avez pas besoin. Les likes de bots s'effacent à mesure que TikTok supprime les comptes derrière eux. Le mieux à faire est d'amener de vrais spectateurs sur vos prochaines vidéos, pour que ce soient les chiffres récents qui parlent pour votre compte.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Un créateur repart de zéro avec une nouvelle vidéo TikTok pour de vrais spectateurs"},
            },
        ],
        "faqs": [
            ("Les likes disparaîtront-ils un jour ?", "Seulement si la personne derrière un like le retire ou supprime son compte, ce qui est rare. Aucune vague de suppressions ne vous attend, car il n'y a pas de faux comptes derrière eux."),
            ("Puis-je avoir des likes qui restent sans abonnés ?", "Non. Les likes font partie de chaque pack et arrivent avec les abonnements et commentaires de ces mêmes spectateurs. Nous ne les vendons pas séparément, et c'est en partie pour cela qu'ils restent : ils sont liés à des personnes qui ont choisi de s'abonner."),
            ("Pourquoi les likes achetés ailleurs ont-ils baissé ?", "Très probablement parce que les comptes derrière eux ont été supprimés. C'est ce qui arrive tôt ou tard au faux engagement sur TikTok, quoi qu'ait promis le vendeur."),
            ("Combien de likes restent chaque mois ?", "Tous nos likes sont laissés par de vraies personnes : la vraie question est donc de savoir combien de personnes aiment vos vidéos, en général {pick_likes} par mois avec {pick_name}."),
            ("Mieux vaut-il moins de vrais likes qu'un gros chiffre acheté ?", "Oui. Un like qui vient avec un visionnage complet, un abonnement ou un commentaire fait partie d'un ensemble qui se lit comme un intérêt sincère. Un gros chiffre sans rien autour se lit exactement pour ce qu'il est."),
        ],
    },
    {
        "service": "likes",
        "modifier": "safe",
        "slug": "tiktok/likes/fiables",
        "label": "Likes TikTok fiables",
        "title": "Acheter des likes TikTok en toute fiabilité | Growsterr",
        "description": "Une façon fiable d'acheter des likes TikTok : de vrais spectateurs, aucune connexion, paiement par carte via Stripe et un pack que vous résiliez vous-même.",
        "h1": ("Une façon fiable d'acheter des likes TikTok : ", "de vraies personnes, sans raccourci."),
        "intro": "Se demander s'il est fiable d'acheter des likes TikTok, c'est le bon réflexe. La plupart des vendeurs de likes livrent des bots, et certains veulent aussi vos identifiants. Voici ce que nous faisons à la place : de vraies personnes découvrent votre profil et aiment les vidéos qui leur plaisent, dans un pack mensuel payé via Stripe et résiliable depuis votre compte.",
        "hero": {"image": "tiktok-likes", "alt": "Des likes de vrais spectateurs sur une vidéo TikTok, sans aucun raccourci"},
        "sections": [
            {
                "h2": "Les signaux d'alerte chez un vendeur de likes TikTok",
                "ul": [
                    "Des milliers de likes promis dans l'heure.",
                    "Un prix pour mille likes inférieur à celui d'un café.",
                    "Une demande de mot de passe TikTok, ou de connexion avec TikTok.",
                    "Aucun nom de société, aucune adresse, aucunes conditions générales.",
                    "Des likes vendus pour n'importe quel lien, sans un mot sur qui regarderait.",
                ],
            },
            {
                "h2": "Ce qui nous rend fiables",
                "p": [
                    "Nous sommes Growsterr, conçu par l'équipe de Sterr Agency (Sterr Technologies OÜ, Tallinn, Estonie). Nous faisons grandir des comptes grâce à des campagnes sponsorisées dans notre réseau partenaire, qui les montrent à de vraies personnes, et nous disons clairement ce que nous ne pouvons pas faire : nous ne promettons pas de chiffres, et les likes ne sont jamais vendus seuls.",
                    "Votre tableau de bord montre ce que nous avons mesuré : les visites de profil de chaque jour et combien se sont transformées en abonnements.",
                ],
            },
            {
                "h2": "Sans risque pour vos vidéos aussi",
                "p": [
                    "Les likes de bots ne font pas que disparaître plus tard. Tant qu'ils sont là, ils faussent le tableau : beaucoup de cœurs, peu de temps de visionnage, aucun commentaire. Les vrais likes sont laissés par ceux qui ont regardé, donc les chiffres sous votre vidéo concordent entre eux.",
                ],
            },
        ],
        "faqs": [
            ("Comment savoir que Growsterr n'est pas une arnaque ?", "Regardez ce que nous demandons et ce que nous promettons. Nous demandons votre nom d'utilisateur, jamais votre mot de passe. Nous donnons des fourchettes habituelles, jamais des chiffres exacts. Le paiement passe par Stripe, et la résiliation se fait dans votre compte, sans rien demander à personne."),
            ("Puis-je être remboursé pour des likes ?", "Les packs sont des abonnements mensuels. Si vous résiliez, le mois payé continue et n'est pas remboursé, et rien n'est prélevé ensuite."),
            ("Des likes fiables auront-ils l'air différents de ceux que j'ai achetés avant ?", "En général, oui. Ils arrivent sur plusieurs jours, répartis sur vos vidéos, et s'accompagnent de vues, d'abonnements et de commentaires des mêmes personnes. Les likes de bots tombent souvent en un bloc sur une seule vidéo."),
            ("À qui parler si quelque chose semble anormal ?", "À une personne de notre équipe, par e-mail ou sur WhatsApp. {pro_name} inclut aussi une ligne WhatsApp directe."),
            ("Payer pour des likes TikTok, est-ce vraiment sérieux ?", "Payer pour des bots, non : vous obtenez un chiffre sans personne derrière. Payer pour que de vraies personnes voient vos vidéos, c'est autre chose, comme une entreprise qui paie pour être vue. C'est ce type de croissance que nous vendons."),
        ],
    },
    {
        "service": "likes",
        "modifier": "comment-likes",
        "slug": "tiktok/likes/commentaires",
        "label": "Likes de commentaires TikTok",
        "title": "Acheter des likes de commentaires TikTok ? | Growsterr",
        "description": "Vous cherchez à acheter des likes de commentaires TikTok ? Nous n'en vendons pas. Les vrais spectateurs aiment les réponses qui sonnent juste.",
        "h1": ("Acheter des likes de commentaires TikTok ? ", "Laissez les vrais spectateurs juger."),
        "intro": "Si vous vouliez acheter des likes de commentaires TikTok pour faire remonter un commentaire épinglé ou une réponse, voici la réponse franche : nous ne vendons pas de likes sur des commentaires précis. Nos campagnes amènent de vraies personnes sur votre profil, et celles qui lisent vos commentaires aiment ceux avec lesquels elles sont d'accord, les vôtres compris.",
        "hero": {"image": "tiktok-watch-time", "alt": "Un spectateur lit les commentaires d'une vidéo TikTok et aime une réponse"},
        "sections": [
            {
                "h2": "Pourquoi nous ne vendons pas de likes sur les commentaires",
                "p": [
                    "Un commentaire avec des centaines de likes et aucune réponse paraît étrange à quiconque passe par là. Les likes de commentaires venant de bots ne mènent à rien d'utile non plus : ils tombent, restent là et ne disent rien de la qualité du commentaire.",
                    "Nous ne pouvons pas non plus faire remonter un commentaire sous la vidéo de quelqu'un d'autre. Nos campagnes montrent votre profil à des gens ; ce qui se passe dans les commentaires des autres créateurs dépend de leurs spectateurs.",
                ],
            },
            {
                "h2": "Des commentaires que les gens aiment vraiment",
                "ul": [
                    "Épinglez un commentaire qui apporte quelque chose : un lien vers la partie deux, la réponse à la question que tout le monde pose.",
                    "Répondez tant qu'une vidéo est récente, quand les commentaires sont les plus animés.",
                    "Posez une question dans la légende pour que les spectateurs aient de quoi parler.",
                    "Gardez des réponses courtes et à votre façon : on aime les commentaires qui vous ressemblent.",
                ],
            },
            {
                "h2": "D'où viennent les likes de commentaires dans un pack",
                "p": [
                    "Chaque pack apporte des likes et des commentaires sur vos vidéos, venant des mêmes personnes ; sur un mois, {pick_name} représente en général {pick_likes} likes et {pick_comments} commentaires. Ces personnes aiment souvent d'autres commentaires en lisant, mais nous ne comptons ni n'orientons cela.",
                ],
            },
        ],
        "faqs": [
            ("Pouvez-vous obtenir des likes sur mon commentaire sous la vidéo d'un gros créateur ?", "Non. Nos campagnes ne font grandir que votre propre profil. Faire remonter un commentaire chez quelqu'un d'autre voudrait dire y envoyer des comptes pour le liker, et c'est exactement le travail pour lequel les bots sont faits."),
            ("Vos packs incluent-ils des likes de commentaires ?", "Pas sous forme de chiffre. Les packs incluent des likes sur vos vidéos et des commentaires écrits par de vraies personnes. Ces mêmes personnes aiment parfois les commentaires qu'elles lisent ; c'est leur choix, et nous ne le mesurons pas."),
            ("Comment faire liker mon commentaire épinglé ?", "Un commentaire épinglé est déjà en haut. Ce qui lui vaut des likes, c'est de valoir la lecture : une suite, une réponse, une chute. Les vrais spectateurs l'aiment quand il ajoute quelque chose à la vidéo."),
            ("Des likes de commentaires achetés aideraient-ils ma vidéo ?", "Pas d'une manière qui compte. Un like sur un commentaire, venant d'un compte qui n'a jamais regardé la vidéo, ne change rien à ses résultats, et une rafale de likes sur un seul commentaire se repère facilement."),
            ("Quel pack apporte le plus d'activité dans mes commentaires ?", "{pro_name}, avec en général {pro_comments} commentaires par mois, puis {rising_name} avec {rising_comments}. Plus de commentaires, c'est une section plus animée, et une section animée se lit."),
        ],
    },
    {
        "service": "likes",
        "modifier": "private-account",
        "slug": "tiktok/likes/compte-prive",
        "label": "Likes TikTok sur un compte privé",
        "title": "Acheter des likes TikTok sur un compte privé ? | Growsterr",
        "description": "Peut-on acheter des likes TikTok sur un compte privé ? Les vidéos privées ne sont visibles que par vos abonnés acceptés : personne de nouveau ne peut les liker.",
        "h1": ("Acheter des likes TikTok sur un compte privé ? ", "Il faut d'abord qu'on voie les vidéos."),
        "intro": "Si vous voulez acheter des likes TikTok sur un compte privé, il y a une limite à connaître d'abord : sur un compte privé, seuls les abonnés que vous avez acceptés peuvent regarder vos vidéos. Les nouvelles personnes ne les voient pas, donc ne peuvent pas les aimer. Nos packs amènent de vrais spectateurs, c'est pourquoi ils ont besoin d'un profil public pendant qu'ils tournent.",
        "hero": {"image": "tiktok-watch-time", "alt": "Une vidéo TikTok rendue publique pour que de nouveaux spectateurs puissent la regarder et l'aimer"},
        "sections": [
            {
                "h2": "Qui peut aimer une vidéo privée",
                "p": [
                    "Sur un compte TikTok privé, vos vidéos n'atteignent que les abonnés acceptés. Tous les autres voient un profil verrouillé. Un like demande une vue, une vue demande un accès : les likes ne peuvent venir que de personnes que vous avez déjà laissées entrer.",
                    "C'est l'inverse de ce à quoi sert un pack de croissance. Nos campagnes existent pour toucher des gens qui ne vous connaissent pas encore, et ils ne peuvent aimer que ce qu'ils ont le droit de regarder.",
                ],
            },
            {
                "h2": "Un compte public avec des moments privés",
                "ul": [
                    "Passez le compte en public pour que de nouvelles personnes vous trouvent et aiment ce qu'elles voient.",
                    "Limitez vos vidéos personnelles à vos amis ou à vous seul : les visiteurs de la campagne ne les verront pas.",
                    "Désactivez les duos, les collages ou les téléchargements sur certaines vidéos si vous voulez plus de contrôle.",
                    "Utilisez les filtres de commentaires de TikTok pour garder la conversation comme vous l'aimez.",
                ],
            },
            {
                "h2": "Ce qu'apporte un mois en public",
                "p": [
                    "Avec un compte public, les personnes amenées par notre campagne peuvent regarder tout ce que vous avez partagé avec tout le monde. Avec {pick_name}, cela représente en général {pick_likes} likes par mois, avec {pick_audience} nouveaux abonnés.",
                ],
            },
        ],
        "faqs": [
            ("Les likes atteindront-ils les vidéos que j'ai mises en privé ?", "Non. Les vidéos réservées à vos amis ou à vous seul ne sont vues que par ces personnes, donc les visiteurs de la campagne ne peuvent ni les regarder ni les aimer. Seules les vidéos visibles par tous reçoivent des likes de nouveaux spectateurs."),
            ("Puis-je repasser en privé à la fin du mois ?", "Oui, une fois votre pack terminé. Les likes déjà présents sur vos vidéos restent, mais les nouvelles personnes ne pourront plus les regarder."),
            ("Puis-je rester en privé et recevoir des likes de mes seuls abonnés ?", "Vos abonnés actuels peuvent aimer ce qu'ils veulent ; nous ne pouvons pas les y pousser. Nos campagnes fonctionnent en montrant votre profil à de nouvelles personnes, et cela n'aide que si elles peuvent voir vos vidéos."),
            ("Passer de privé à public est-il risqué ?", "C'est un réglage que vous maîtrisez et pouvez annuler. Avant de basculer, regardez quelles vidéos sont visibles par tous et réservez tout ce qui est personnel à vos amis ou à vous seul."),
            ("Quelqu'un a-t-il besoin d'accéder à mon compte pour envoyer des likes ?", "Personne ne devrait. Nous travaillons à partir de votre seul nom d'utilisateur et ne nous connectons jamais à votre compte. Si un service a besoin de vos identifiants pour obtenir des likes sur un compte privé, gardez-les pour vous."),
        ],
    },
    {
        "service": "likes",
        "modifier": "live",
        "slug": "tiktok/likes/live",
        "label": "Likes de LIVE TikTok",
        "title": "Acheter des likes de LIVE TikTok ? Ce qui marche | Growsterr",
        "description": "Vous voulez acheter des likes de LIVE TikTok ? Ils viennent des gens présents dans le direct. Nous faisons grandir les abonnés qui pourraient venir.",
        "h1": ("Acheter des likes de LIVE TikTok ? ", "Remplissez la salle, les cœurs suivront."),
        "intro": "Si vous cherchez à acheter des likes de LIVE TikTok, mieux vaut savoir ce qu'ils sont : des tapotements sur l'écran de la part de personnes qui regardent votre direct à cet instant. Nous n'envoyons pas de likes sur un LIVE, et personne ne peut en envoyer de vrais. Ce que nous faisons grandir, c'est l'audience susceptible de venir : de vrais abonnés qui ont découvert vos vidéos et les ont assez aimées pour rester.",
        "hero": {"image": "tiktok-likes", "alt": "Des cœurs montent sur l'écran pendant un LIVE TikTok avec de vrais spectateurs"},
        "sections": [
            {
                "h2": "Ce que mesurent vraiment les likes d'un LIVE TikTok",
                "p": [
                    "Les likes d'un LIVE sont le pouls de la salle. Un spectateur peut tapoter autant qu'il veut, donc un direct avec quelques personnes impliquées peut en récolter beaucoup. Ce que montrent ces cœurs, à vous comme à ceux qui arrivent, c'est que les personnes présentes apprécient.",
                    "Des tapotements envoyés par des comptes qui ne regardent pas ne montrent rien de tel. Le chat reste muet, les cœurs ne correspondent pas à ce qui se passe à l'écran, et quiconque arrive le sent.",
                ],
            },
            {
                "h2": "Comment un pack aide vos LIVE",
                "p": [
                    "Vous ne pouvez pas acheter la salle, mais vous pouvez faire grandir la liste des personnes susceptibles d'entrer. Chaque abonné amené par nos campagnes est quelqu'un qui a choisi vos vidéos, et vos abonnés sont l'audience de départ de chaque LIVE.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Un créateur parle à ses spectateurs pendant un LIVE TikTok depuis son studio à la maison"},
            },
            {
                "h2": "Obtenir plus de cœurs des personnes présentes",
                "ul": [
                    "Affichez un objectif à l'écran, ou lancez un vote par cœurs, pour donner aux spectateurs une raison de tapoter.",
                    "Réagissez à voix haute quand les cœurs grimpent : on tapote davantage quand on voit que ça fait mouche.",
                    "Gardez des premières minutes animées, car c'est là que les nouveaux venus décident de rester.",
                    "Remerciez les habitués par leur nom : une salle qui se sent comme une communauté tapote comme une communauté.",
                ],
            },
        ],
        "faqs": [
            ("Puis-je acheter des likes pour un LIVE TikTok en cours ?", "Non. Nous n'envoyons ni likes, ni spectateurs, ni commentaires sur un direct. De vraies personnes rejoignent un LIVE quand elles le voient et en ont envie, et personne ne peut programmer cela."),
            ("Vos packs apportent-ils des likes sur les LIVE ?", "Pas directement. Les packs apportent des abonnés, ainsi que des likes et des commentaires sur vos vidéos. Certains de ces abonnés peuvent rejoindre vos LIVE et tapoter ; cela leur appartient, et nous ne le comptons pas."),
            ("Faut-il 1 000 abonnés avant que les likes de LIVE comptent ?", "Le LIVE lui-même reste verrouillé tant qu'un compte n'a pas 1 000 abonnés. Si vous n'y êtes pas encore, faites d'abord grandir vos abonnés ; les likes de LIVE viendront ensuite, des personnes qui restent."),
            ("Pourquoi mes likes de LIVE sont-ils faibles malgré beaucoup d'abonnés ?", "Des abonnés qui ne regardent jamais ne rejoignent pas les directs. Si un compteur a été construit avec des bots, le LIVE paraîtra vide. De vrais abonnés, des directs réguliers et un début animé, voilà ce qui apporte des cœurs."),
            ("Les likes de LIVE influencent-ils qui voit mon direct ?", "TikTok ne publie pas exactement comment il choisit les LIVE à montrer, mais une salle où les gens restent, discutent et tapotent lui donne de quoi travailler. Une salle de comptes muets, non."),
        ],
    },
    # --- Views: the ways people ask for them --------------------------------------------------
    {
        "service": "views",
        "modifier": "real",
        "slug": "tiktok/vues/vraies",
        "label": "Vraies vues TikTok",
        "title": "Acheter de vraies vues TikTok, de qualité | Growsterr",
        "description": "Achetez de vraies vues TikTok, de personnes et non de scripts : des spectateurs qui regardent, ouvrent votre profil et s'abonnent quand ils en veulent plus.",
        "h1": ("Acheter de vraies vues TikTok, ", "de gens qui appuient eux-mêmes sur lecture."),
        "intro": "Quand vous achetez de vraies vues TikTok via un pack Growsterr, vous payez pour des personnes : de vrais spectateurs qui découvrent votre profil, lancent la lecture eux-mêmes et regardent aussi longtemps que votre vidéo les retient. La qualité n'est pas une gamme à choisir. C'est ce que vous obtenez quand chaque vue a une personne derrière elle.",
        "hero": {"image": "tiktok-watch-time", "alt": "Un vrai spectateur lance la lecture de la vidéo TikTok d'un créateur"},
        "sections": [
            {
                "h2": "Comment juger la qualité des vues TikTok",
                "ul": [
                    "Le temps de visionnage : de vrais spectateurs restent quand une vidéo est bonne et partent quand elle ne l'est pas.",
                    "Les visites de profil : ceux qui aiment une vidéo ouvrent votre profil pour en voir plus.",
                    "Les abonnements et les likes : certains spectateurs en veulent plus, et le montrent.",
                    "Les commentaires : une vraie audience répond, avec ses propres mots.",
                    "Les partages : le signe le plus clair de tous, et seules des personnes le donnent.",
                ],
            },
            {
                "h2": "Les vraies vues commencent sur votre profil",
                "p": [
                    "Nos campagnes présentent votre profil à de vrais spectateurs de notre réseau partenaire. Les curieux l'ouvrent sur TikTok et commencent à regarder : c'est de là que viennent vos vues. C'est aussi pourquoi nous mesurons les visites de profil : une visite, c'est une personne qui arrive, et les vues suivent.",
                    "Les vues en gros volume sautent cette étape. Elles visent un seul lien de vidéo, sont lues par un logiciel et disparaissent en une seconde.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Le profil TikTok d'un créateur ouvert par de nouveaux spectateurs qui parcourent ses vidéos"},
            },
        ],
        "faqs": [
            ("Quelle différence entre vraies vues et vues de haute qualité ?", "Pour nous, aucune. Une vraie vue vient d'une personne qui a choisi de regarder, et c'est la seule qualité qui compte. Les mentions de qualité sur les lots de vues signifient généralement juste que les comptes ont une photo de profil."),
            ("Pouvez-vous me montrer les vues que vous avez apportées ?", "Nous montrons ce que nous mesurons : les visites quotidiennes de votre profil venues de la campagne, et la part qui s'est transformée en abonnements. Vos vues apparaissent dans les statistiques de TikTok, avec le temps de visionnage."),
            ("Les vraies vues comptent-elles comme les autres ?", "Dans le compteur, une vue reste une vue. La différence, c'est tout ce qui l'entoure : de vrais spectateurs regardent, réagissent et s'abonnent parfois, et c'est ce qui aide une vidéo à toucher plus de monde."),
            ("Pourquoi ne vendez-vous pas de vues sans abonnés ?", "Parce que de vrais spectateurs ne viennent pas en pièces détachées. La même personne qui regarde peut liker, commenter ou s'abonner : nous amenons donc des personnes plutôt qu'un nombre de lectures, et tout vient dans un seul pack."),
            ("Les vraies vues sont-elles plus lentes que les vues achetées ?", "Oui. Les gens arrivent tout au long de la journée, chaque jour du mois. Tout ce qui arrive plus vite que des personnes ne peuvent trouver une vidéo n'est pas fait de personnes."),
        ],
    },
    {
        "service": "views",
        "modifier": "organic",
        "slug": "tiktok/vues/organiques",
        "label": "Vues TikTok organiques",
        "title": "Vues TikTok organiques, du lieu de votre choix | Growsterr",
        "description": "Des vues TikTok organiques venues de là où vit votre audience : ville, région ou pays. De vrais spectateurs regardent parce qu'ils en ont envie.",
        "h1": ("Acheter des vues TikTok organiques, ", "là où vit votre audience."),
        "intro": "Pour acheter des vues TikTok organiques qui ont du sens, deux choses comptent : une vraie personne a choisi de regarder, et c'est la bonne personne. Nos packs s'occupent des deux. Nous présentons votre profil à de vraies personnes dans le lieu de votre choix, et les vues viennent de celles qui s'arrêtent pour regarder.",
        "hero": {"image": "tiktok-watch-time", "alt": "Des habitants d'une même ville regardent les vidéos TikTok d'un créateur local"},
        "sections": [
            {
                "h2": "Des vues TikTok ciblées par lieu",
                "p": [
                    "Un restaurant à Lisbonne a besoin de vues de Lisbonne. Un créateur hispanophone veut des spectateurs qui comprennent l'espagnol. Une boutique qui ne livre qu'en France gagne peu à des vues d'un autre continent. Choisir le lieu est le moyen le plus simple de faire compter les vues.",
                    "Indiquez une ville, une région ou un pays dans votre commande, et la campagne commence là.",
                ],
            },
            {
                "h2": "Ce qui rend une vue organique",
                "ul": [
                    "Le spectateur n'a été ni payé, ni sollicité, ni scripté pour regarder.",
                    "Il a atteint votre vidéo depuis votre profil et lancé la lecture lui-même.",
                    "Il aurait pu faire défiler, et ne l'a pas fait.",
                    "Ce qu'il fait ensuite, un like, un abonnement, un partage ou rien du tout, lui appartient.",
                ],
            },
            {
                "h2": "Pourquoi les vues du bon endroit vont plus loin",
                "p": [
                    "Les vues du bon endroit viennent avec le reste : des commentaires dans une langue à laquelle vous pouvez répondre, des abonnements de personnes qui pourraient vraiment passer votre porte, des partages à des amis qui habitent tout près. Une vue de l'autre bout du monde, sans raison de s'y intéresser, n'apporte rien de tout cela.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Le gérant d'un petit commerce filme un TikTok pour les clients de sa ville"},
            },
        ],
        "faqs": [
            ("Puis-je cibler des vues TikTok par pays ?", "Oui, ou par ville ou région. Indiquez le lieu lors de la commande ; les personnes qui y vivent voient votre profil en premier, et quand l'audience la plus adaptée déborde un peu, certains spectateurs peuvent venir des alentours."),
            ("Des vues ciblées restent-elles organiques ?", "Oui. Choisir qui voit votre profil ne choisit pas qui regarde. Chaque personne dans ce lieu décide elle-même si votre vidéo vaut son temps."),
            ("Et si mon audience est répartie sur plusieurs pays ?", "Indiquez la région qui les couvre, ou le pays qui compte le plus. S'il vous faut quelque chose de plus précis, écrivez-nous avant de commander."),
            ("Les vues suivront-elles le fuseau horaire de mon audience ?", "De vraies personnes naviguent quand elles sont éveillées, donc les vues du lieu choisi suivent généralement ses heures de journée. Les vues de bots se moquent de l'heure qu'il est chez vous."),
            ("Les vues organiques viennent-elles avec des abonnés ?", "Oui. Les spectateurs qui regardent sont les mêmes personnes qui s'abonnent : avec {pick_name}, cela représente en général {pick_audience} nouveaux abonnés par mois, avec leurs likes et leurs commentaires."),
        ],
    },
    {
        "service": "views",
        "modifier": "monthly",
        "slug": "tiktok/vues/mensuelles",
        "label": "Vues TikTok pour chaque vidéo",
        "title": "Vues TikTok sur toutes vos vidéos, chaque mois | Growsterr",
        "description": "Des vues TikTok pour toutes vos vidéos avec un seul pack mensuel : de vraies personnes parcourent votre profil et regardent ce qui les accroche.",
        "h1": ("Acheter des vues TikTok pour plusieurs vidéos, ", "tout le mois, de vraies personnes."),
        "intro": "Vous voulez acheter des vues TikTok pour plusieurs vidéos sans commander pour chacune ? Un pack mensuel couvre tout votre profil. De vraies personnes vous découvrent chaque jour, et une fois sur votre profil, elles regardent plus d'une vidéo : la plus récente, les épinglées, ce qui les accroche. Les vues s'accumulent au fil du temps, sur tout ce que vous publiez.",
        "hero": {"image": "tiktok-watch-time", "alt": "Un spectateur fait défiler plusieurs vidéos sur le profil TikTok d'un créateur"},
        "sections": [
            {
                "h2": "Un pack, toutes vos vidéos",
                "p": [
                    "Les lots de vues par vidéo vous obligent à choisir : celle-ci est aidée, celle-là non, et la semaine suivante vous recommandez. Un pack mensuel agit au niveau de votre profil. Chaque vidéo publiée dans le mois est là pour les personnes que nous amenons, tout comme tout ce que vous avez publié avant.",
                    "{rising_name} et {pro_name} vous permettent aussi d'indiquer les vidéos qui doivent recevoir le plus d'attention.",
                ],
            },
            {
                "h2": "Les vues automatiques TikTok, et pourquoi nous n'en faisons pas",
                "p": [
                    "Les vues automatiques envoient un nombre fixe de lectures sur chaque nouvelle vidéo dès sa mise en ligne. Chaque vidéo reçoit le même coup de pouce, que ce soit la meilleure ou la plus faible, et aucune de ces lectures ne vient avec un spectateur. C'est un schéma facile à repérer.",
                ],
            },
            {
                "h2": "Gagner plus de vues au fil du temps",
                "ul": [
                    "Épinglez vos trois vidéos les plus fortes : les vidéos épinglées apparaissent en premier sur votre profil.",
                    "Faites une série, pour que les gens aient une raison de regarder l'épisode suivant et le précédent.",
                    "Soignez votre profil, avec une bio claire, pour que les visiteurs sachent ce qui les attend.",
                    "Les anciennes vidéos continuent de gagner des vues tant que de nouvelles personnes arrivent.",
                ],
            },
        ],
        "faqs": [
            ("Le pack couvre-t-il chaque vidéo que je publie ?", "Oui. La campagne amène des gens sur votre profil, pas sur un lien unique, donc tout ce qui y est public peut être regardé. Les nouvelles vidéos en reçoivent souvent le plus, car elles sont en haut de ce que voient les visiteurs."),
            ("Comment les vues se répartissent-elles entre mes vidéos ?", "Ce sont les spectateurs qui décident. Ils regardent ce qui les intéresse, donc vos vidéos les plus fortes en récoltent davantage. Nous ne répartissons pas de chiffre entre elles, puisqu'il n'y en a pas."),
            ("Les anciennes vidéos continueront-elles d'avoir des vues ?", "Oui, tant que de nouvelles personnes découvrent votre profil. Chaque mois apporte une audience fraîche qui peut remonter vers ce que vous avez déjà publié."),
            ("Est-ce la même chose que les vues automatiques TikTok ?", "Non. Les vues automatiques envoient d'elles-mêmes des lectures sur chaque nouvelle publication. Notre pack se renouvelle de lui-même, mais les vues viennent de personnes qui ont choisi de regarder."),
            ("Puis-je avoir des vues pour plusieurs comptes TikTok ?", "Chaque pack fait grandir un compte. Si vous en gérez plusieurs, prenez un pack pour chacun ; ils se retrouvent tous dans le même compte Growsterr."),
        ],
    },
    {
        "service": "views",
        "modifier": "gradual",
        "slug": "tiktok/vues/progressives",
        "label": "Vues TikTok progressives",
        "title": "Vues TikTok progressives, au rythme des gens | Growsterr",
        "description": "Achetez des vues TikTok lentement, sans minuteur de goutte-à-goutte : de vraies personnes découvrent votre profil chaque jour et regardent à leur rythme.",
        "h1": ("Acheter des vues TikTok lentement, ", "un vrai spectateur à la fois."),
        "intro": "Vous voulez acheter des vues TikTok lentement pour qu'elles aient l'air naturelles ? Oubliez le goutte-à-goutte. Des vues qui ont l'air naturelles, ce sont des vues de personnes. Nos packs amènent de vrais spectateurs sur votre profil chaque jour du mois, et ils regardent vos vidéos quand ils les trouvent, au rythme où l'on navigue vraiment.",
        "hero": {"image": "tiktok-watch-time", "alt": "Des vues TikTok qui s'accumulent jour après jour à mesure que de vraies personnes trouvent les vidéos d'un créateur"},
        "sections": [
            {
                "h2": "La forme des vraies vues",
                "p": [
                    "Les vraies vues n'arrivent pas en ligne droite. Une vidéo reçoit une première vague des personnes qui la voient tôt, puis une longue traîne de spectateurs qui la trouvent sur votre profil des jours ou des semaines plus tard. Chaque nouvel abonné est un nouveau spectateur pour tout votre catalogue.",
                    "Les vues au goutte-à-goutte aplatissent cette forme en une rampe bien nette : un nombre fixe par heure, venant de comptes qui partent au bout d'une seconde. C'est lent, mais ça n'a pas l'air vrai.",
                ],
            },
            {
                "h2": "Des vues qui bougent avec tout le reste",
                "ul": [
                    "Quand les vues montent, les likes et les abonnements montent avec elles, car ce sont les mêmes personnes qui font les trois.",
                    "Vos anciennes vidéos continuent d'être regardées à mesure que de nouvelles personnes explorent votre profil.",
                    "Jours chargés et jours calmes alternent, comme pour tout créateur.",
                ],
            },
            {
                "h2": "Ce que nous mesurons, et ce que mesure TikTok",
                "p": [
                    "Nous ne comptons pas les vues à l'avance, et nous ne prétendons pas le faire. Votre tableau de bord montre ce que notre système a mesuré : les visites de profil venues de la campagne et les abonnés qu'elles ont donnés, jour après jour. Les statistiques de TikTok montrent vos vues, et avec de vraies personnes derrière, les deux racontent la même histoire.",
                ],
            },
        ],
        "faqs": [
            ("Combien de vues par jour auront mes vidéos ?", "Cela dépend davantage de vos vidéos que de nous. Nous amenons un flux régulier de vraies personnes sur votre profil ; combien de vidéos elles regardent, et à quelle fréquence, leur appartient."),
            ("Pourquoi mes vues arrivent-elles par vagues et pas régulièrement ?", "Parce que les gens ne naviguent pas de façon régulière. Les soirées, les week-ends et une nouvelle vidéo rendent les journées plus chargées. Un flux de vues identique chaque heure, c'est ce que produit une machine."),
            ("Les anciennes vidéos reçoivent-elles aussi des vues ?", "Souvent. Ceux qui aiment une vidéo ont tendance à ouvrir votre profil et à en regarder d'autres. C'est l'un des meilleurs signes que laisse une vraie audience."),
            ("Puis-je répartir les vues sur des vidéos précises ?", "Avec {rising_name} ou {pro_name}, vous décidez quelles vidéos la campagne met en avant ; les personnes que nous amenons regardent quand même à leur rythme."),
            ("Le rythme change-t-il d'un mois à l'autre ?", "Un peu. Chaque mois apporte de nouvelles personnes, et ce que vous publiez influence ce qu'elles regardent. Un mois de vidéos fortes paraît généralement plus animé."),
        ],
    },
    {
        "service": "views",
        "modifier": "no-drop",
        "slug": "tiktok/vues/sans-perte",
        "label": "Vues TikTok qui ne baissent pas",
        "title": "Vues TikTok sans perte : les vraies lectures restent | Growsterr",
        "description": "Des vues TikTok sans perte : les vues de vraies personnes sont des lectures ordinaires, qui restent comptées. Pas besoin de promesse de recharge.",
        "h1": ("Des vues TikTok qui ne baissent pas : ", "commencez par des gens qui ont regardé."),
        "intro": "Si vous voulez acheter des vues TikTok sans perte, regardez d'abord pourquoi des vues baissent : ce n'étaient jamais de vraies lectures, et TikTok les a retirées. Nos packs amènent de vraies personnes qui regardent vos vidéos, et leurs vues sont des vues ordinaires de spectateurs ordinaires. Il n'y a rien à retirer.",
        "hero": {"image": "tiktok-watch-time", "alt": "Un compteur de vues TikTok qui garde ses chiffres parce que de vraies personnes ont regardé"},
        "sections": [
            {
                "h2": "Pourquoi certains compteurs de vues baissent",
                "p": [
                    "TikTok s'efforce de tenir le faux engagement à l'écart, et quand il supprime des lectures non authentiques ou les comptes qui les ont produites, le compteur s'ajuste. C'est pourquoi une vidéo peut afficher plus de vues un jour que le lendemain. Une étiquette « sans perte » sur un lot de lectures ne change pas la nature de ces lectures.",
                ],
            },
            {
                "h2": "Ce qui fait qu'une vue reste",
                "ul": [
                    "Une vraie personne a appuyé sur lecture, sur son propre téléphone, par son propre choix.",
                    "Elle a trouvé votre vidéo depuis votre profil, pas via un lien donné à un script.",
                    "Sa vue arrive avec des likes, des abonnements et des commentaires cohérents entre eux.",
                ],
            },
            {
                "h2": "De vraies vues sans perte, en version honnête",
                "p": [
                    "Nous ne promettrons pas qu'un chiffre ne bougera jamais, car TikTok tient ses propres comptes. Ce que nous pouvons dire, c'est que chaque vue que nous apportons est la décision personnelle de quelqu'un de regarder, le seul type de vue qu'un nettoyage n'a aucune raison de toucher.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Un créateur consulte ses statistiques TikTok après un mois de vues de vraies personnes"},
            },
        ],
        "faqs": [
            ("Mes vues vont-elles baisser après la campagne ?", "Les vues de vraies personnes sont comptées comme toutes les autres, donc il n'y a aucune raison qu'elles disparaissent à la fin de votre pack. Vos vues progressent simplement plus lentement une fois que de nouvelles personnes cessent d'arriver."),
            ("Pourquoi les vues « sans perte » d'autres sites baissent-elles quand même ?", "Parce que « sans perte » décrit un espoir, pas les vues. Si les lectures venaient de bots ou de scripts, elles peuvent être supprimées quoi que dise l'étiquette."),
            ("Combien de mes vues resteront ?", "Toutes celles que de vraies personnes vous donnent. Nous ne comptons pas les vues à l'avance, puisqu'elles dépendent du nombre de vidéos que chacun regarde, mais chacune vient d'une vraie personne."),
            ("Les vues restent-elles si je supprime et republie une vidéo ?", "Non. Une vidéo supprimée emporte ses vues, quelle qu'en soit l'origine. Une republication repart de zéro : mieux vaut généralement laisser une vidéo en ligne et laisser les gens continuer à la trouver."),
            ("Les vraies vues viennent-elles aussi avec des likes ?", "Oui. Les mêmes spectateurs likent, commentent et s'abonnent quand ils le veulent, ce qui avec {pick_name} représente en général {pick_likes} likes et {pick_comments} commentaires par mois."),
        ],
    },
    {
        "service": "views",
        "modifier": "safe",
        "slug": "tiktok/vues/fiables",
        "label": "Vues TikTok sans risque",
        "title": "Acheter des vues TikTok sans bots ni connexion | Growsterr",
        "description": "Est-ce sûr d'acheter des vues TikTok ? Les vues de bots brouillent vos statistiques et peuvent disparaître. Nous : de vrais spectateurs, aucune connexion.",
        "h1": ("Acheter des vues TikTok sans risque : ", "un compte et des statistiques propres."),
        "intro": "Pour acheter des vues TikTok en toute sécurité, pensez à plus que votre mot de passe. Les vues de bots faussent aussi vos statistiques, si bien que vous ne savez plus quelles vidéos marchent. Nos packs amènent de vraies personnes qui découvrent votre profil et regardent d'elles-mêmes. Aucune connexion, aucun script, rien qui touche votre compte, et vos statistiques restent honnêtes.",
        "hero": {"image": "tiktok-watch-time", "alt": "Des statistiques TikTok propres, avec des vues et un temps de visionnage venus de vraies personnes"},
        "sections": [
            {
                "h2": "Le coût caché des vues à risque",
                "p": [
                    "Vos statistiques TikTok sont votre façon d'apprendre : quelles accroches retiennent, quels sons fonctionnent, quels sujets amènent des abonnés. Les vues de bots y déversent du bruit. Le temps de visionnage moyen s'effondre, les sources de trafic n'ont plus de sens, et vous finissez par copier la vidéo qui avait seulement l'air de marcher.",
                ],
            },
            {
                "h2": "Est-ce une façon sérieuse d'acheter des vues TikTok ?",
                "p": [
                    "Nous ne vendons pas de vues comme produit. Nous vendons un pack de croissance mensuel, mené sous forme de campagnes sponsorisées où de vraies personnes découvrent votre profil. Les vues, c'est ce que font ces personnes quand vos vidéos leur plaisent. Voilà la version sérieuse : vous payez pour être vu, et les gens décident du reste.",
                ],
            },
            {
                "h2": "Ce qui reste protégé",
                "ul": [
                    "Vos identifiants : ils ne quittent jamais vos mains, car un nom d'utilisateur suffit.",
                    "Votre paiement : le paiement sécurisé de Stripe, par carte, Apple Pay ou Google Pay.",
                    "Votre sortie : résiliez depuis votre compte quand vous voulez, et gardez le reste du mois payé.",
                    "Vos données : des vues et un temps de visionnage venus de personnes, donc ce que vous en apprenez est vrai.",
                ],
            },
        ],
        "faqs": [
            ("Acheter des vues pourrait-il mettre mes vidéos en danger ?", "Nous amenons des personnes qui regardent d'elles-mêmes, et nous n'agissons jamais dans votre compte ni n'envoyons de lectures scriptées. TikTok prend ses propres décisions, mais de vrais spectateurs qui regardent des vidéos publiques, c'est exactement ce à quoi sert l'appli."),
            ("Avez-vous besoin d'accéder à mon TikTok pour envoyer des vues ?", "Non. Les vues viennent de personnes qui ouvrent votre profil et lancent la lecture, ce qui ne demande rien d'autre qu'un compte public et votre nom d'utilisateur."),
            ("Pourquoi les lots de vues bon marché sont-ils risqués ?", "Ils sont bon marché parce que personne ne regarde. Ces lectures peuvent être supprimées, elles font baisser votre temps de visionnage moyen et rendent vos statistiques inutilisables pour décider quoi publier ensuite."),
            ("Comment savoir que les vues sont réelles ?", "Regardez ce qui les accompagne. De vraies vues amènent des visites de profil, des likes, des abonnements et quelques commentaires, et vos statistiques montrent des spectateurs qui restent plus ou moins longtemps, pas qui partent tous à la même seconde."),
            ("Puis-je arrêter si je ne suis pas à l'aise ?", "Oui, quand vous voulez, depuis votre compte. Aucun autre paiement n'est prélevé, et votre mois en cours se poursuit jusqu'à son dernier jour."),
        ],
    },
    {
        "service": "views",
        "modifier": "fyp",
        "slug": "tiktok/vues/pour-toi",
        "label": "Vues TikTok et page Pour toi",
        "title": "Vues TikTok et page Pour toi : ce qui y mène | Growsterr",
        "description": "Des vues TikTok pour le Pour toi (FYP) ? Personne ne peut acheter ni promettre cette place. Ce qui compte, c'est ce qu'en font de vrais spectateurs.",
        "h1": ("Vues TikTok et page Pour toi : ", "ce qui fait vraiment avancer une vidéo."),
        "intro": "Chercher à acheter des vues TikTok pour la FYP veut généralement dire une chose : vous voulez qu'une vidéo arrive sur la page Pour toi. Personne ne peut vous vendre cette place, nous compris. Ce que nous pouvons faire, c'est envoyer de vraies personnes sur votre profil jour après jour, et ce qu'elles font de vos vidéos (regarder, partager, s'abonner) est le genre de signal que TikTok dit utiliser.",
        "hero": {"image": "tiktok-watch-time", "alt": "Des spectateurs regardent une vidéo TikTok jusqu'au bout et la partagent"},
        "sections": [
            {
                "h2": "Pourquoi personne ne peut vous vendre la page Pour toi",
                "p": [
                    "La page Pour toi n'est pas un endroit où l'on place une vidéo. Elle est différente pour chaque personne, construite à partir de ce que chacun a regardé, aimé, partagé et passé. TikTok choisit pour eux, vidéo par vidéo, et il n'y a pas de place à acheter.",
                    "Quand un service vend des vues « FYP », il vend donc des lectures, généralement de bots. Des lectures que personne ne regarde ne peuvent pas convaincre TikTok que quelqu'un veut en voir plus.",
                ],
            },
            {
                "h2": "Ce que TikTok dit regarder",
                "p": [
                    "TikTok a décrit ce qui alimente ses recommandations, et rien de cela n'est un chiffre qu'on peut acheter :",
                ],
                "ul": [
                    "Les interactions des gens : ce qu'ils regardent, aiment, partagent, commentent et suivent.",
                    "Les éléments de la vidéo elle-même : légendes, sons et hashtags.",
                    "Des paramètres comme la langue et la localisation.",
                ],
            },
            {
                "h2": "Devenir viral sur TikTok, honnêtement",
                "p": [
                    "Personne ne peut promettre une vidéo virale. Les partages et les enregistrements arrivent quand un spectateur veut montrer quelque chose à un ami, ou le revoir, et personne ne peut commander cela à de vraies personnes. Ce qu'une croissance régulière vous donne, ce sont plus de chances : plus de vraies personnes qui voient chaque vidéo, plus de gens susceptibles de la partager au bon moment. La vidéo doit encore le mériter. Une accroche forte, un son adapté et une fin qui donne envie de revoir font plus que n'importe quel chiffre acheté.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Un créateur teste différents sons pour une vidéo TikTok avant de la publier"},
            },
        ],
        "faqs": [
            ("Votre pack mettra-t-il ma vidéo sur la page Pour toi ?", "Nous ne pouvons pas le promettre, et personne ne le peut honnêtement. Nous amenons de vrais spectateurs sur votre profil ; s'ils regardent, partagent et s'abonnent, TikTok a des raisons de montrer votre vidéo à d'autres personnes comme eux."),
            ("Les vues aident-elles une vidéo à atteindre le Pour toi ?", "Les vues seules, non. Une lecture qui s'arrête au bout d'une seconde dit à TikTok que la vidéo n'a pas retenu l'attention. Regarder jusqu'au bout, revoir, partager et enregistrer comptent bien davantage, et seules des personnes le font."),
            ("Puis-je acheter des partages ou des enregistrements ?", "Non. Les partages et les enregistrements viennent de vrais spectateurs qui ont assez aimé une vidéo pour l'envoyer à quelqu'un ou la garder. Ils viennent avec le pack quand vos vidéos les méritent, et nous ne les comptons ni ne les vendons séparément."),
            ("Comment devenir viral sur TikTok ?", "Il n'y a pas d'interrupteur. Publiez souvent, accrochez les spectateurs dès les premières secondes, utilisez des sons adaptés à la vidéo et faites des choses qu'on a envie d'envoyer à un ami. De vrais spectateurs donnent plus de chances à chaque vidéo ; le reste, c'est la vidéo et un peu de chance."),
            ("Le hashtag #fyp aide-t-il ?", "TikTok lit bien les hashtags, mais #fyp ne dit rien du contenu de votre vidéo. Un hashtag qui décrit votre sujet aide les bonnes personnes à la trouver."),
            ("Quel pack aide le plus une vidéo précise ?", "Avec {rising_name} ou {pro_name}, vous pouvez désigner les vidéos qui comptent, pour que celle en laquelle vous croyez passe devant davantage de nos visiteurs. Jusqu'où elle va ensuite dépend des personnes qui la regardent."),
        ],
    },
    {
        "service": "views",
        "modifier": "high-retention",
        "slug": "tiktok/vues/haute-retention",
        "label": "Vues TikTok à haute rétention",
        "title": "Vues TikTok à haute rétention, honnêtement | Growsterr",
        "description": "Acheter des vues TikTok à haute rétention ? La rétention vient de gens qui continuent à regarder. Nous amenons de vrais spectateurs ; votre vidéo les retient.",
        "h1": ("Des vues TikTok à haute rétention ? ", "De vrais spectateurs, puis une vidéo qu'on finit."),
        "intro": "Vouloir acheter des vues TikTok à haute rétention, c'est déjà connaître le secret : sur TikTok, la durée de visionnage compte, pas seulement le nombre de lancements. Mais la rétention ne se vend pas : c'est une personne qui décide de continuer à regarder. Notre travail est d'amener de vraies personnes sur votre profil ; les garder jusqu'au bout, c'est le travail de votre vidéo.",
        "hero": {"image": "tiktok-watch-time", "alt": "Un spectateur regarde encore une vidéo TikTok alors qu'elle arrive à ses dernières secondes"},
        "sections": [
            {
                "h2": "Ce que sont généralement les vues « haute rétention »",
                "p": [
                    "Quand quelqu'un vend des vues à haute rétention, il parle de lectures programmées pour durer un nombre fixe de secondes avant de passer à autre chose. Le temps de visionnage n'est réel qu'au sens où un écran l'a lu. Personne ne l'a vu, personne n'a ri, personne ne l'a partagé, et le reste de vos chiffres le montre.",
                ],
            },
            {
                "h2": "Une rétention que vous pouvez vraiment augmenter",
                "ul": [
                    "Allez droit au but dans la première ou la deuxième seconde, quand la plupart des spectateurs décident.",
                    "Adaptez la durée à l'idée : une blague rapide ne doit pas durer une minute.",
                    "Choisissez un son qui colle à l'ambiance, sans qu'il couvre votre voix.",
                    "Ajoutez des sous-titres pour ceux qui regardent sans le son.",
                    "Terminez d'une façon qui rend le revisionnage naturel.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Un créateur raccourcit les premières secondes d'une vidéo TikTok pour retenir les spectateurs"},
            },
            {
                "h2": "Lisez votre propre rétention",
                "p": [
                    "Les statistiques de TikTok montrent votre temps de visionnage moyen et combien de spectateurs ont regardé la vidéo en entier. Consultez-les après chaque publication. Avec de vraies personnes qui trouvent vos vidéos grâce à notre campagne, ces chiffres sont honnêtes, et vous verrez quelles vidéos retiennent des inconnus et lesquelles non.",
                ],
            },
        ],
        "faqs": [
            ("Pouvez-vous livrer des vues avec un temps de visionnage fixe ?", "Non. Chaque vue vient d'une vraie personne, qui regarde aussi longtemps que la vidéo la retient. Un temps de visionnage fixe voudrait dire que personne ne regardait vraiment."),
            ("De vrais spectateurs regarderont-ils toute ma vidéo ?", "Certains oui, d'autres non, selon la vidéo. C'est justement pour cela que leur rétention vaut quelque chose : elle vous dit, à vous comme à TikTok, ce qui marche."),
            ("Les vidéos longues ont-elles une moins bonne rétention ?", "Pas forcément. Une vidéo longue qui justifie sa durée peut très bien retenir les gens. Ce qui fait du tort, c'est une longueur que l'idée ne peut pas porter."),
            ("La rétention compte-t-elle plus que les likes ?", "Les deux sont liés. Ceux qui regardent jusqu'au bout sont les plus susceptibles de liker, commenter et partager : de vrais spectateurs vous donnent tout cela à la fois."),
            ("Quel pack amène le plus de spectateurs sur mes vidéos ?", "{pro_name} amène le plus de personnes sur votre profil, en général {pro_audience} nouveaux abonnés par mois, et ajoute une mise en avant prioritaire ainsi que le choix des vidéos qui reçoivent l'attention."),
        ],
    },
    {
        "service": "views",
        "modifier": "live",
        "slug": "tiktok/vues/live",
        "label": "Spectateurs de LIVE TikTok",
        "title": "Spectateurs LIVE TikTok : une salle ne s'achète pas | Growsterr",
        "description": "Vous cherchez à acheter des spectateurs de LIVE TikTok ? On ne réserve pas de vraies personnes pour un direct. Nous faisons grandir votre audience, sans bots.",
        "h1": ("Les spectateurs de LIVE TikTok ", "viennent d'abonnés qui tiennent à vous."),
        "intro": "Les spectateurs d'un LIVE TikTok sont des personnes présentes dans la salle à cet instant, et personne ne peut en fournir de vrais sur commande. C'est pourquoi nous ne vendons ni vues ni spectateurs de LIVE. Nous faisons grandir l'audience susceptible de venir : de vraies personnes qui ont découvert vos vidéos et se sont abonnées, chaque jour du mois. Quand vous lancez un direct, ce sont elles qui peuvent venir.",
        "hero": {"image": "tiktok-creator", "alt": "Un créateur anime un LIVE TikTok pendant que de vrais spectateurs arrivent et discutent"},
        "sections": [
            {
                "h2": "Pourquoi des spectateurs de LIVE achetés dégradent un direct",
                "p": [
                    "Un nombre de spectateurs élevé avec un chat vide dit à tous ceux qui arrivent que quelque chose cloche. Les spectateurs achetés restent dans la salle sans parler, sans envoyer de cadeaux ni partager le direct. Ils gonflent le seul chiffre que tout le monde voit et affament ceux qui font vivre un LIVE.",
                ],
            },
            {
                "h2": "Transformer vos abonnés en spectateurs de LIVE",
                "ul": [
                    "Programmez le direct à l'avance en tant qu'événement LIVE, pour que vos abonnés puissent activer un rappel.",
                    "Annoncez l'horaire dans vos vidéos la veille.",
                    "Lancez vos LIVE au même créneau chaque semaine pour que cela devienne une habitude pour vos abonnés.",
                    "Passez en LIVE peu après une vidéo qui a bien marché, tant que ses spectateurs sont encore curieux de vous.",
                ],
            },
            {
                "h2": "Ce que nous pouvons faire pour un LIVE, et ce que nous ne pouvons pas",
                "p": [
                    "Nous ne pouvons pas remplir votre direct un vendredi à 20 h, et nous ne pouvons pas promettre un nombre de spectateurs. Ce que nous pouvons faire, c'est veiller à ce que, chaque mois, davantage de vraies personnes connaissent vos vidéos et vous suivent, pour que chaque LIVE démarre avec un groupe plus grand de personnes susceptibles de venir.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Des abonnés ouvrent le LIVE TikTok d'un créateur depuis leur téléphone"},
            },
        ],
        "faqs": [
            ("Puis-je acheter de vrais spectateurs pour mon LIVE TikTok ?", "Personne ne le peut. De vraies personnes rejoignent un direct parce qu'elles l'ont vu et en ont eu envie, à ce moment-là. Des spectateurs livrés sur demande sont des comptes qui ne regardent pas, et ils rendent un LIVE plus vide, pas plus plein."),
            ("Comment vos packs aident-ils les vues de mes LIVE ?", "Ils font grandir vos abonnés avec de vraies personnes. Vos abonnés sont votre audience de LIVE en puissance : certains viendront quand vous serez en direct, d'autres non, comme avec toute audience."),
            ("Comptez-vous les vues de LIVE dans le tableau de bord ?", "Non. Le tableau de bord montre ce que notre campagne a mesuré, c'est-à-dire les visites de profil et les abonnements qu'elles ont entraînés, jour par jour. Les statistiques LIVE de TikTok montrent qui a rejoint vos directs."),
            ("Puis-je faire un LIVE sans 1 000 abonnés ?", "En général non : TikTok demande d'abord 1 000 abonnés, et votre appli vous indique si le LIVE vous est ouvert. Atteindre ce cap avec de vrais abonnés signifie que votre premier direct a des gens susceptibles de venir."),
            ("Des spectateurs de LIVE achetés feront-ils recommander mon direct ?", "Il n'y a aucune raison de s'y attendre. Une salle pleine de comptes qui ne discutent jamais, n'offrent rien et ne restent pas ne donne à TikTok rien qui vaille d'être recommandé."),
        ],
    },
    {
        "service": "views",
        "modifier": "promote",
        "slug": "tiktok/vues/promouvoir",
        "label": "Promouvoir ses vidéos TikTok",
        "title": "Vues TikTok Promote, ou une campagne menée pour vous | Growsterr",
        "description": "Vous pensez à l'outil Promouvoir de TikTok pour des vues ou des abonnés ? Nous menons des campagnes sponsorisées pour votre profil, tout le mois.",
        "h1": ("Promouvoir vos vues TikTok, ", "ou une campagne de croissance menée pour vous."),
        "intro": "Vous hésitez entre acheter des vues via l'outil Promouvoir de TikTok et autre chose ? Voici où nous nous situons. Nous ne gérons pas de publicités TikTok pour vous. Nous menons nos propres campagnes sponsorisées dans notre réseau partenaire, qui montrent votre profil à de vraies personnes chaque jour, tout le mois, dans le lieu de votre choix. Celles qui aiment ce qu'elles voient regardent, s'abonnent, reviennent.",
        "hero": {"image": "tiktok-creator", "alt": "Un créateur réfléchit à la façon de montrer une vidéo TikTok à davantage de vraies personnes"},
        "sections": [
            {
                "h2": "Deux façons de promouvoir une vidéo TikTok",
                "p": [
                    "L'outil Promouvoir de TikTok vous permet de payer TikTok pour montrer une vidéo à plus de monde tant que votre budget dure : vous choisissez la vidéo, un objectif et la dépense, et vous gérez le tout vous-même.",
                    "Un pack Growsterr met en avant votre profil plutôt qu'une seule publication, pendant un mois entier, avec une équipe qui mène la campagne. Les gens arrivent sur votre profil, regardent ce qui attire leur œil et décident de s'abonner ou non.",
                ],
            },
            {
                "h2": "Ce qu'apporte un mois de promotion",
                "ul": [
                    "De nouveaux abonnés : en général {pick_audience} avec {pick_name}.",
                    "Des likes et des commentaires de ces mêmes abonnés : en général {pick_likes} et {pick_comments}.",
                    "Des vues sur tout votre profil, que nous ne comptons pas à l'avance.",
                    "Un tableau de bord des visites de profil et des nouveaux abonnés, jour après jour.",
                ],
            },
            {
                "h2": "Peut-on utiliser les deux ?",
                "p": [
                    "Oui. Les outils de TikTok conviennent à un coup de pouce ponctuel derrière une seule vidéo ; un pack mensuel continue d'amener des gens sur votre profil entre deux coups de pouce. Rien dans l'un ne gêne l'autre.",
                ],
            },
        ],
        "faqs": [
            ("Utilisez-vous Promouvoir ou les publicités TikTok ?", "Non. Nos campagnes tournent dans notre réseau partenaire, en dehors des outils publicitaires de TikTok. Nous n'avons jamais besoin d'accéder à votre compte ou à votre budget publicitaire, seulement à votre nom d'utilisateur."),
            ("En quoi le prix diffère-t-il de publicités que je gérerais moi-même ?", "Un pack a un prix mensuel fixe : {starter_price} pour {starter_name}, {rising_price} pour {rising_name}, {pro_price} pour {pro_name}. Avec la publicité, vous fixez et gérez votre propre budget. Nous ne pouvons pas vous dire ce qui coûtera le moins pour votre compte, mais nous pouvons vous dire exactement ce que coûte chaque pack."),
            ("Puis-je promouvoir une vidéo TikTok précise ?", "Avec {rising_name} et {pro_name}, oui : vous choisissez les vidéos qui reçoivent l'attention. {starter_name} met en avant votre profil dans son ensemble."),
            ("La promotion m'apportera-t-elle aussi des abonnés TikTok ?", "Oui, c'est même l'essentiel. Les personnes qui aiment ce qu'elles regardent s'abonnent, en général {pick_audience} par mois avec {pick_name}, et leurs likes et commentaires viennent avec."),
            ("Ai-je besoin d'un compte professionnel ?", "Non. Les comptes personnels comme professionnels fonctionnent, tant que le compte est public, et votre nom d'utilisateur est tout ce que nous demandons."),
        ],
    },
]
