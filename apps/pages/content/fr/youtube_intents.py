UPDATED = "2026-11-09"

# French YouTube intent pages: searches for things we don't sell (cheap, instant, free, free
# trial, panels). Each answers honestly, then leads to the monthly package. Keys and placeholders:
# docs/CONTENT.md; angles: docs/keywords/WRITING.md.

PAGES = [
    # --- Subscribers ----------------------------------------------------------------------
    {
        "service": "subscribers",
        "modifier": "cheap",
        "slug": "youtube/abonnes/pas-cher",
        "label": "Abonnés YouTube pas chers ?",
        "plan": "starter",
        "title": "Abonnés YouTube pas chers à 1 € ? Le vrai coût | Growsterr",
        "description": "Les abonnés YouTube à 1 € ne regardent jamais et finissent supprimés. Pour {starter_price} par mois, {starter_name} amène en général {starter_audience} vrais abonnés.",
        "h1": ("Les abonnés YouTube à 1 € ", "ne regardent jamais une seule vidéo."),
        "intro": "Vous pensez acheter des abonnés YouTube pas cher, à 1 € ? À ce prix, vous obtenez des comptes qui ne regarderont jamais rien, et YouTube retire régulièrement les comptes de spam des compteurs. Nous facturons davantage et amenons des spectateurs : {starter_audience} nouveaux abonnés dans un mois habituel avec {starter_name}, à {starter_price}, chacun étant une personne qui a trouvé votre chaîne et décidé de s'abonner.",
        "hero": {"image": "youtube-subscribers", "alt": "Le nombre d'abonnés d'une chaîne YouTube qui grandit avec de vrais spectateurs"},
        "sections": [
            {
                "h2": "Le coût d'un abonné qui ne regarde jamais",
                "p": [
                    "Sur YouTube, ce que font les abonnés compte plus que leur nombre. Une liste remplie de comptes qui n'appuient jamais sur lecture fait paraître chaque nouvelle vidéo moins intéressante qu'elle ne l'est.",
                    "Un abonné bon marché n'est donc pas bon marché. Vous payez une fois en argent, et une seconde fois en vues que vous n'obtenez pas.",
                ],
            },
            {
                "h2": "Ce que coûte un vrai abonné",
                "p": [
                    "Prenez {starter_name} : {starter_price} par mois, et en général {starter_audience} abonnés qui sont de vrais spectateurs, du lieu de votre choix. Par personne, c'est une affaire de centimes, et leurs likes et commentaires sont compris dans le prix.",
                ],
            },
            {
                "h2": "Un petit prix sans le risque",
                "ul": [
                    "Aucun mot de passe ni accès à votre compte Google : seulement l'identifiant de votre chaîne.",
                    "Facturation mensuelle par carte via Stripe, résiliable depuis votre compte.",
                    "Abonnés, likes et commentaires pour un seul prix, venant des mêmes personnes.",
                ],
            },
        ],
        "faqs": [
            ("Combien coûtent de vrais abonnés YouTube ?", "Nos packs commencent à {starter_price} par mois. {starter_name} apporte en général {starter_audience} nouveaux abonnés ; {rising_name}, à {rising_price}, en apporte {rising_audience} ; {pro_name}, à {pro_price}, en apporte {pro_audience}."),
            ("Pourquoi certains sites vendent-ils des abonnés si peu cher ?", "Parce qu'ils vendent des comptes, pas des spectateurs. Créer ou louer des comptes en masse ne coûte presque rien ; trouver des gens qui veulent regarder votre chaîne, si."),
            ("Y a-t-il une option très bon marché pour une petite chaîne ?", "{starter_name} est conçu pour les chaînes nouvelles et petites, et c'est notre prix le plus bas."),
            ("Des abonnés pas chers peuvent-ils causer des ennuis à ma chaîne ?", "Oui. La politique de YouTube sur le faux engagement couvre les abonnés achetés, et les chaînes qui en utilisent risquent la suppression de vidéos ou des sanctions."),
            ("Les vues sont-elles comprises dans le prix ?", "Oui. Vos nouveaux abonnés regardent, aiment et commentent d'eux-mêmes, le tout dans le pack. Nous ne chiffrons pas les vues, puisque chacune est quelqu'un qui choisit d'appuyer sur lecture."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "fast",
        "slug": "youtube/abonnes/rapides",
        "label": "Abonnés YouTube rapides ?",
        "title": "Abonnés YouTube rapides : réels, pas instantanés | Growsterr",
        "description": "Des abonnés YouTube réels, instantanés et actifs à la fois, c'est impossible. Les nôtres sont réels et actifs : la campagne démarre en quelques jours.",
        "h1": ("Réels, actifs et instantanés ? ", "Seules deux de ces promesses peuvent être vraies."),
        "intro": "Vous voulez acheter des abonnés YouTube rapides, réels, instantanés et actifs à la fois ? Seules deux de ces promesses peuvent être vraies ensemble. Des abonnés instantanés ne sont pas des personnes, et de vraies personnes ne s'abonnent pas à la seconde où vous payez. Nous amenons vite de vrais abonnés actifs : la campagne démarre en quelques jours, puis {pick_name} en ajoute en général {pick_audience} par mois.",
        "hero": {"image": "youtube-subscribers", "alt": "De nouveaux abonnés rejoignent une chaîne YouTube jour après jour"},
        "sections": [
            {
                "h2": "Pourquoi instantané veut dire faux sur YouTube",
                "p": [
                    "Une vraie personne s'abonne après avoir regardé quelque chose : une vidéo, un Short, une bande-annonce de chaîne. Cela prend au moins quelques minutes, et ça arrive quand elle en a le temps. Des abonnés qui apparaissent par centaines juste après un paiement ont sauté l'étape du visionnage : ce n'étaient pas des personnes.",
                ],
            },
            {
                "h2": "À quelle vitesse arrivent de vrais abonnés",
                "p": [
                    "La mise en place prend les premiers jours après la commande. Ensuite, de nouveaux spectateurs trouvent votre chaîne chaque jour, et ceux qui aiment ce qu'ils regardent s'abonnent. Le tableau de bord montre chaque jour tel que nous le mesurons : vous voyez le rythme dès la première semaine.",
                ],
            },
            {
                "h2": "Une vitesse utile",
                "ul": [
                    "Publiez pendant la campagne, pour que les nouveaux abonnés aient quelque chose à regarder ensuite.",
                    "Soignez la page de votre chaîne : une bannière claire, une bande-annonce et des playlists dans un ordre logique.",
                    "Choisissez {pro_name} pour la plus grande fourchette mensuelle : en général {pro_audience} nouveaux abonnés.",
                ],
            },
        ],
        "faqs": [
            ("À quelle vitesse mon nombre d'abonnés va-t-il augmenter ?", "Dès les premiers jours de votre campagne : quelques-uns à la fois au début, puis chaque jour tout au long du mois."),
            ("Pouvez-vous ajouter 1 000 abonnés instantanément ?", "Non, et personne ne le peut avec de vraies personnes. Mille en une heure, ce sont mille comptes qui ne regarderont jamais, et ce sont ceux que YouTube supprime."),
            ("Vos abonnés sont-ils actifs ?", "Ce sont de vraies personnes qui se sont abonnées après avoir vu votre chaîne, donc elles sont aussi actives que n'importe quel spectateur : elles regardent, aiment et commentent quand une vidéo les intéresse."),
            ("Quel pack est le plus rapide ?", "{pro_name} apporte le plus chaque mois : en général {pro_audience} nouveaux abonnés. {starter_name} et {rising_name} apportent des fourchettes plus petites, réparties de la même façon sur le mois."),
            ("Une croissance rapide nuira-t-elle à ma chaîne ?", "Pas à ce rythme. Les abonnés arrivent chaque jour, de vrais spectateurs, comme sur toute chaîne qui grandit."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "free",
        "slug": "youtube/abonnes/gratuits",
        "label": "Abonnés YouTube gratuits ?",
        "plan": "starter",
        "tool": "growth-calculator",
        "title": "Abonnés YouTube gratuits ? Un meilleur plan | Growsterr",
        "description": "Les abonnés YouTube gratuits viennent d'échanges sub4sub ou de bots. Nous n'en offrons pas, mais notre calculateur gratuit estime une vraie croissance.",
        "h1": ("Des abonnés YouTube gratuits ? ", "Planifiez plutôt de vrais abonnés."),
        "intro": "Vous cherchez des abonnés YouTube gratuits, ou 1 000 abonnés pour 5 € ? Ni l'un ni l'autre n'amène des gens qui regardent : les offres gratuites reposent sur des échanges « sub4sub » ou des comptes bots. Nous ne donnons pas d'abonnés. Ce qui est gratuit ici, c'est le calculateur de croissance : indiquez où en est votre chaîne et votre objectif, il estime les mois nécessaires avec chaque pack.",
        "hero": {"image": "youtube-channel", "alt": "Un youtubeur fixe un objectif d'abonnés pour les mois à venir"},
        "sections": [
            {
                "h2": "Le sub4sub et autres astuces gratuites",
                "ul": [
                    "Les groupes sub4sub : vous vous abonnez à des inconnus, ils s'abonnent en retour, et personne ne regarde personne.",
                    "Les sites d'abonnés gratuits qui vous demandent de vous connecter avec Google, puis utilisent votre compte pour s'abonner à d'autres chaînes.",
                    "De minuscules lots gratuits de comptes bots, offerts pour que vous en achetiez un plus gros.",
                ],
                "p": [
                    "Tous remplissent votre compteur de gens qui ne s'intéressent pas à vos vidéos, ce qui est pire que d'avoir moins d'abonnés.",
                ],
            },
            {
                "h2": "À propos de ces 1 000",
                "p": [
                    "Mille abonnés, c'est un cap pour beaucoup de chaînes, souvent à cause du Programme Partenaire YouTube. Des abonnés achetés ou échangés n'apportent aucune durée de visionnage, et YouTube les traite comme du faux engagement. Nous ne promettons pas non plus la monétisation : nous amenons de vrais spectateurs, et le reste dépend de vos vidéos et de YouTube.",
                ],
            },
            {
                "h2": "Planifiez avec le calculateur de croissance",
                "p": [
                    "Le calculateur en haut de page est gratuit et fonctionne dans votre navigateur. Saisissez votre nombre d'abonnés à la ligne « Abonnés aujourd'hui », et votre cible comme objectif. Il calcule combien de mois chaque pack demande habituellement, à partir de sa fourchette mensuelle habituelle.",
                ],
            },
        ],
        "faqs": [
            ("Puis-je obtenir des abonnés YouTube gratuitement ?", "Pas de vrais abonnés chez nous. Chaque abonné que nous apportons est un spectateur touché par une campagne payante. Le calculateur est la partie gratuite, sans limite d'utilisation."),
            ("1 000 abonnés YouTube pour 5 €, c'est réel ?", "Aucune vraie campagne ne peut trouver mille personnes qui veulent votre chaîne pour cinq euros. À ce prix, les abonnés sont des comptes, pas des spectateurs."),
            ("Combien de temps pour atteindre 1 000 vrais abonnés ?", "Cela dépend de votre point de départ. {starter_name} apporte en général {starter_audience} nouveaux abonnés par mois ; saisissez vos propres chiffres dans le calculateur ci-dessus pour voir le nombre de mois pour votre chaîne."),
            ("Le sub4sub est-il contraire aux règles de YouTube ?", "Oui. La politique de YouTube sur le faux engagement couvre l'échange d'abonnements, ce qui peut mettre une chaîne en danger. Cela amène aussi des abonnés qui ne regardent jamais."),
            ("Par où une petite chaîne devrait-elle commencer ?", "Par {starter_name}, à {starter_price} par mois, sans engagement au-delà du mois en cours."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "free-trial",
        "slug": "youtube/abonnes/essai-gratuit",
        "label": "Essai gratuit d'abonnés YouTube ?",
        "plan": "starter",
        "title": "Acheter des abonnés YouTube avec un essai gratuit ? | Growsterr",
        "description": "Pas d'essai gratuit d'abonnés YouTube ici : un échantillon d'un jour ne prouve rien. Votre premier mois montre de vrais spectateurs, mesurés, sans engagement.",
        "h1": ("Un essai gratuit d'abonnés YouTube ", "ne prouverait rien. Un mois, si."),
        "intro": "Si vous voulez acheter des abonnés YouTube après un essai gratuit, soyons francs : nous n'en proposons pas. Un essai de 100 abonnés en une journée montrerait seulement qu'un vendeur a des comptes en réserve. C'est votre premier mois qui permet de nous juger : {starter_name} à {starter_price}, de vrais spectateurs dès les premiers jours, un tableau de bord de ce que nous avons mesuré, et aucun engagement au-delà du mois.",
        "hero": {"image": "youtube-hub", "alt": "Les statistiques d'une chaîne YouTube pendant un premier mois de vraie croissance"},
        "sections": [
            {
                "h2": "Ce qu'un essai ne peut pas vous montrer",
                "p": [
                    "La question n'est pas de savoir si un chiffre peut monter. C'est de savoir si de vraies personnes regardent, aiment et restent, et cela prend des semaines à voir. Un échantillon d'un jour est un argument de vente, pas un test.",
                ],
            },
            {
                "h2": "Comment nous contrôler pendant le mois",
                "ul": [
                    "Ouvrez le tableau de bord tous les quelques jours : visites venues de la campagne et nouveaux abonnés, tels que mesurés.",
                    "Regardez les statistiques de vos vidéos : les nouveaux spectateurs regardent-ils ?",
                    "Lisez les commentaires : des gens qui parlent de vos vidéos avec leurs propres mots.",
                    "Décidez avant la date de renouvellement ; vous pouvez résilier depuis votre compte à tout moment.",
                ],
            },
        ],
        "faqs": [
            ("Avez-vous un essai gratuit pour YouTube ?", "Non. Nous ne faisons d'essai sur aucune plateforme. Un mois est le pack le plus court, et vous pouvez résilier avant que le suivant commence."),
            ("Pourquoi pas d'essai alors que d'autres sites en proposent ?", "Chaque abonné que nous apportons vient d'une vraie campagne qui coûte de l'argent dès le premier jour. Les vendeurs qui peuvent se permettre des échantillons gratuits envoient généralement des comptes, pas des spectateurs."),
            ("Que se passe-t-il si je résilie après un mois ?", "Rien de plus n'est prélevé, et le mois payé va jusqu'à son terme. Les vrais abonnés ne sont pas repris ; ils restent, sauf s'ils décident de partir."),
            ("Verrai-je des résultats dès le premier mois ?", "Vous verrez le rythme : de nouveaux abonnés chaque jour, en général {starter_audience} sur le mois avec {starter_name}. Habituel, pas fixe, car chacun est une personne qui décide pour elle-même."),
            ("Puis-je d'abord essayer un pack plus petit ?", "{starter_name} est notre plus petit pack, et le point de départ naturel. Vous pourrez monter en gamme plus tard si votre chaîne en a besoin."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "smm-panel",
        "slug": "youtube/abonnes/panel-smm",
        "label": "Abonnés YouTube via un panel SMM ?",
        "title": "Acheter des abonnés YouTube sur un panel SMM ? | Growsterr",
        "description": "Les panels SMM vendent abonnés et vues YouTube au mille, avec recharges, car tout baisse. Nous sommes une agence : vrais spectateurs, chiffres mesurés.",
        "h1": ("Les abonnés de panel ont un bouton de recharge. ", "Les nôtres n'en ont pas besoin."),
        "intro": "Avant d'acheter des abonnés ou des vues YouTube sur un panel SMM, remarquez l'option de recharge souvent affichée à côté : le panel s'attend à ce que les chiffres baissent. Les panels revendent du trafic de bots en gros. Nous travaillons comme une agence : notre équipe s'occupe de votre campagne, de vrais spectateurs trouvent votre chaîne et s'abonnent, et le tableau de bord rapporte ce que nous avons mesuré.",
        "hero": {"image": "youtube-channel", "alt": "Un créateur consulte un tableau de bord de nouveaux abonnés YouTube mesurés"},
        "sections": [
            {
                "h2": "Des abonnés et des vues au mille",
                "p": [
                    "Sur un panel, abonnés, vues et durée de visionnage YouTube figurent dans une même liste, au prix du mille, avec des notes sur les délais de démarrage et les recharges. Personne ne regarde votre chaîne. La commande rejoint une file d'attente, et des comptes exécutent ce que dit la file.",
                    "Les vues de panel fonctionnent de la même façon : des lectures sans que personne ne décide de regarder, le genre que YouTube s'efforce de retirer des compteurs.",
                ],
            },
            {
                "h2": "Ce qui change avec une agence",
                "ul": [
                    "Des personnes au lieu de files d'attente : votre chaîne est montrée chaque jour à de vrais spectateurs.",
                    "Chaque abonné, like, vue et commentaire remonte à une personne.",
                    "Une équipe derrière votre campagne, et un moyen de nous joindre quand vous avez des questions.",
                    "Un tableau de bord de ce que nous avons mesuré, pas un compteur qu'il faut sans cesse recharger.",
                ],
            },
        ],
        "faqs": [
            ("Les abonnés de panel sont-ils de vraies personnes ?", "Non. Les panels revendent du trafic en gros venant de comptes qui s'abonnent sur instruction, et c'est pourquoi les recharges font partie de l'offre."),
            ("Vendez-vous des vues YouTube seules ?", "Non. Les vues ne sont pas une ligne à part. Elles viennent des personnes que notre campagne touche, les mêmes qui s'abonnent, aiment et commentent."),
            ("Les vues de panel peuvent-elles causer des ennuis à ma chaîne ?", "Oui. Les vues artificielles enfreignent les règles de YouTube sur le faux engagement ; elles peuvent être retirées de votre compteur, et un usage répété met la chaîne en danger."),
            ("Proposez-vous un panel revendeur ?", "Non. Nous ne vendons ni en gros ni via des revendeurs : chaque pack est une campagne construite autour d'une chaîne. Les agences qui gèrent plusieurs chaînes peuvent nous contacter pour en parler."),
            ("Qu'apporte un pack chaque mois ?", "{pick_name} apporte en général {pick_audience} nouveaux abonnés par mois, de vrais spectateurs qui arrivent sur les 30 jours."),
        ],
    },
    # --- Views ----------------------------------------------------------------------------
    {
        "service": "views",
        "modifier": "cheap",
        "slug": "youtube/vues/pas-cher",
        "label": "Vues YouTube pas chères ?",
        "plan": "starter",
        "title": "Acheter des vues YouTube pas cher : ce que vaut 1 € | Growsterr",
        "description": "Les vues YouTube à un euro les mille sont des lectures, pas des spectateurs. Notre pack mensuel amène de vraies personnes qui regardent et s'abonnent.",
        "h1": ("Des vues YouTube pas chères ", "sont des lectures, pas des spectateurs."),
        "intro": "Si vous comptez acheter des vues YouTube pas cher, disons mille pour un euro, sachez ce qui arrive : des lectures de scripts ou de comptes en masse qui regardent quelques secondes au plus, et que YouTube peut retirer de votre compteur. Nous ne vendons pas de vues séparément. Notre pack mensuel amène de vraies personnes sur votre chaîne, et elles regardent, aiment, commentent et s'abonnent par choix.",
        "hero": {"image": "youtube-viewers", "alt": "De vrais spectateurs regardent une vidéo YouTube jusqu'au bout"},
        "sections": [
            {
                "h2": "Ce que vaut une vue",
                "p": [
                    "Une vue aide quand une personne regarde. Combien de temps elle reste, si elle aime la vidéo et sur quelle vidéo elle clique ensuite, voilà ce qui montre à YouTube qu'une vidéo mérite plus de spectateurs. Une vue bon marché ajoute un au compteur et ne donne rien à YouTube.",
                    "Un gros nombre de vues avec presque aucune durée de visionnage envoie aussi un signal contradictoire, et les lectures achetées peuvent de toute façon être retirées.",
                ],
            },
            {
                "h2": "Un pack de vues YouTube, version honnête",
                "p": [
                    "Nous vendons bien un pack, mais pas un lot de vues. {starter_name} coûte {starter_price} par mois : en général {starter_audience} nouveaux abonnés, {starter_likes} likes et {starter_comments} commentaires de vrais spectateurs, plus les vues que ces mêmes personnes donnent à vos vidéos.",
                    "Les vues ne sont pas comptées à l'avance. Elles suivent votre contenu plutôt qu'un quota, car chacune est le choix de quelqu'un.",
                ],
            },
            {
                "h2": "Prix par vue ou prix par spectateur",
                "p": [
                    "Comptez les spectateurs, pas les vues. Un vrai abonné peut regarder des dizaines de vos vidéos pendant les mois où il reste. Un euro de lectures scriptées ne regarde plus rien après aujourd'hui.",
                ],
            },
        ],
        "faqs": [
            ("Combien coûtent les vues YouTube chez vous ?", "Les vues n'ont pas de prix à part. Le plus petit pack, {starter_name}, coûte {starter_price} par mois et apporte abonnés, likes et commentaires, avec les vues de ces mêmes personnes."),
            ("Pourquoi les vues à 1 € sont-elles si bon marché ?", "Parce que personne ne les regarde. Des scripts et des comptes en masse produisent des lectures pour presque rien, et c'est tout ce qu'ils produisent."),
            ("Des vues pas chères m'amèneront-elles de vrais spectateurs ?", "Peu probable. YouTube regarde comment les gens réagissent à une vidéo, pas seulement le compteur, et les vues achetées ne réagissent pas."),
            ("Puis-je choisir quelles vidéos reçoivent des spectateurs ?", "Non. La campagne fait la promotion de votre chaîne dans son ensemble, et les spectateurs choisissent quoi regarder. De bons titres et de bonnes miniatures les aident à trouver vos meilleures vidéos."),
            ("Existe-t-il un pack très bon marché rien que pour les vues ?", "Il n'existe pas d'option « vues seules » en dessous de {starter_name} à {starter_price} par mois, car les vues viennent des personnes qu'un pack amène."),
        ],
    },
    {
        "service": "views",
        "modifier": "fast",
        "slug": "youtube/vues/rapides",
        "label": "Vues YouTube rapides ?",
        "title": "Vues YouTube rapides ? Ce qui arrive vraiment | Growsterr",
        "description": "Les vues YouTube instantanées, y compris pour les premières, viennent de scripts. De vrais spectateurs trouvent votre chaîne dès les premiers jours.",
        "h1": ("Des vues YouTube rapides ? ", "Les spectateurs ne se livrent pas."),
        "intro": "Vous voulez acheter des vues YouTube rapidement, avec livraison instantanée ? Des vues livrées selon un minuteur viennent de scripts, pas de personnes : un vrai spectateur clique quand une vidéo attire son regard. Nous ne vendons ni ne livrons de vues. Nous amenons de vraies personnes sur votre chaîne chaque jour dès les premiers jours de votre campagne, et elles regardent, aiment et s'abonnent d'elles-mêmes.",
        "hero": {"image": "youtube-viewers", "alt": "Des spectateurs découvrent la nouvelle vidéo YouTube d'un créateur"},
        "sections": [
            {
                "h2": "La livraison rapide, c'est pour les colis",
                "p": [
                    "Les délais de livraison ont du sens pour ce qui arrive en carton. Pour des vues, une vitesse de livraison signifie qu'une machine appuie sur lecture, et ces lectures ne s'accompagnent d'aucune durée de visionnage digne de ce nom.",
                ],
            },
            {
                "h2": "Les premières ont besoin de vraies personnes",
                "p": [
                    "Une première est un moment : des gens qui attendent, discutent et regardent ensemble. Des vues de première achetées peuvent remplir un compteur, jamais le chat. Nous ne pouvons pas non plus amener une audience à une minute précise, et nous ne ferons pas semblant.",
                    "Ce qui aide, c'est une base plus large de vrais abonnés, qui peuvent voir la première sur leur page d'accueil ou dans leur fil d'abonnements et activer un rappel.",
                ],
            },
            {
                "h2": "À quelle vitesse se construisent de vraies vues",
                "ul": [
                    "Dans les premiers jours, votre campagne démarre et de nouveaux spectateurs arrivent sur votre chaîne.",
                    "Chaque vidéo publiée ce mois-ci est là pour les personnes abonnées la semaine précédente.",
                    "Les vues continuent de venir de ces abonnés tant qu'ils apprécient vos vidéos.",
                ],
            },
        ],
        "faqs": [
            ("À quelle vitesse mes vues vont-elles monter ?", "Une fois la campagne lancée, ce qui se fait dans ses premiers jours, les vues montent à mesure que de nouvelles personnes trouvent votre chaîne. Elles grandissent avec votre audience au lieu de bondir sur une seule vidéo."),
            ("Pouvez-vous envoyer des vues instantanées sur une nouvelle vidéo ?", "Non. Les vues instantanées viennent de scripts. Les vraies vues d'une nouvelle vidéo viennent de personnes qui la voient dans leur fil ou leurs recommandations, et notre travail est de faire grandir ce groupe."),
            ("Pouvez-vous remplir ma première de spectateurs en direct ?", "Personne ne peut promettre de vraies personnes à une minute précise. Faire grandir vos vrais abonnés avant une première vous donne plus de gens susceptibles de venir."),
            ("Les vues sont-elles comptées dans mon pack ?", "Elles y sont incluses, sans nombre fixe. Les mêmes personnes qui s'abonnent, aiment et commentent regardent aussi, donc les vues suivent votre audience."),
            ("Quel pack apporte le plus de vues ?", "Nous ne dimensionnons pas les packs en vues. Un pack plus grand touche plus de monde : {pro_name}, avec en général {pro_audience} nouveaux abonnés par mois, signifie généralement plus de personnes qui regardent."),
        ],
    },
    {
        "service": "views",
        "modifier": "free",
        "slug": "youtube/vues/gratuites",
        "label": "Vues YouTube gratuites ?",
        "plan": "starter",
        "tool": "engagement-calculator",
        "title": "1 000 vues YouTube gratuites ? Pourquoi ça n'aide pas | Growsterr",
        "description": "Les vues YouTube gratuites, Shorts compris, viennent d'échanges et de scripts. Nous n'en donnons pas ; mesurez plutôt votre engagement, gratuitement.",
        "h1": ("1 000 vues YouTube gratuites ", "ne regarderont pas votre vidéo. De vraies personnes, si."),
        "intro": "Les offres de 1 000 vues YouTube gratuites, ou de vues gratuites sur les Shorts, reposent sur des échanges de vues, des astuces de lecture automatique ou des lectures de bots, et aucune n'amène quelqu'un qui regarde. Nous ne donnons pas de vues. Le calculateur d'engagement de cette page est gratuit : il montre quelle part de vos abonnés réagit à une vidéo typique. Pour plus de vraies personnes, nos packs les amènent.",
        "hero": {"image": "youtube-channel", "alt": "Un youtubeur consulte les likes et les commentaires de ses vidéos récentes"},
        "sections": [
            {
                "h2": "D'où viennent les vues gratuites",
                "ul": [
                    "Les échanges de vues : vous regardez les vidéos d'inconnus contre des crédits, et ils lisent les vôtres sans le son.",
                    "Les intégrations et astuces de lecture automatique qui comptent une lecture que personne n'a choisie.",
                    "Des lectures de bots distribuées par petits lots pour vous en vendre de plus gros.",
                    "Des vues gratuites sur les Shorts, venant de scripts qui passent à la suite au bout d'une seconde.",
                ],
            },
            {
                "h2": "Mesurez votre engagement avec le calculateur",
                "p": [
                    "Ce calculateur fonctionne entièrement dans votre navigateur, gratuitement. À la ligne « Abonnés », saisissez vos abonnés ; ajoutez ensuite la moyenne de likes et de commentaires de vos vidéos récentes. Le résultat est la part de votre audience qui réagit, un bien meilleur indicateur de santé qu'un nombre de vues.",
                ],
            },
            {
                "h2": "Des façons gratuites d'obtenir plus de vues",
                "ul": [
                    "Passez autant de temps sur le titre et la miniature que sur le montage ; ce sont eux qui décident du clic.",
                    "Allez droit au but dans les premières secondes d'une vidéo ou d'un Short.",
                    "Ajoutez des écrans de fin et des playlists pour qu'une vue en amène une autre.",
                    "Répondez aux commentaires ; les gens reviennent vers les conversations.",
                ],
            },
        ],
        "faqs": [
            ("Puis-je obtenir 1 000 vues YouTube gratuitement ?", "Pas de vraies personnes, et pas chez nous. Un millier gratuit vient d'échanges ou de scripts. Le calculateur de cette page est la partie vraiment gratuite."),
            ("Les vues gratuites sur les Shorts sont-elles différentes ?", "Non. Elles viennent des mêmes astuces. Un Short ne circule que lorsque de vraies personnes le regardent jusqu'au bout, donc des lectures de scripts ne l'aident pas."),
            ("Des vues gratuites peuvent-elles faire sanctionner ma chaîne ?", "C'est un vrai risque. Les vues issues de systèmes automatisés ou d'échanges relèvent de la politique de YouTube sur le faux engagement, qui permet à YouTube de les retirer ou d'agir contre la chaîne."),
            ("Avez-vous un pack de vues gratuit ?", "Non. Le plus petit pack est {starter_name} à {starter_price} par mois, et les vues y sont incluses, venant des vraies personnes qui s'abonnent."),
            ("Que m'apprend le taux d'engagement ?", "Quelle part de votre audience est vraiment là. Un taux faible avec beaucoup d'abonnés signifie généralement que beaucoup d'abonnés ont cessé de regarder, ou n'ont jamais regardé."),
        ],
    },
    {
        "service": "views",
        "modifier": "free-trial",
        "slug": "youtube/vues/essai-gratuit",
        "label": "Essai gratuit de vues YouTube ?",
        "plan": "starter",
        "title": "Vues YouTube en essai gratuit ? Testez-nous vraiment | Growsterr",
        "description": "Pas d'essai gratuit de vues YouTube, et pas de vues vendues seules. Testez-nous sur un mois de vrais spectateurs, avec les statistiques de YouTube.",
        "h1": ("Un essai de vues YouTube ", "prouve seulement qu'un compteur peut bouger."),
        "intro": "Vous espérez acheter des vues YouTube après un essai gratuit, avant de payer quoi que ce soit ? Il n'y a pas d'essai ici, et les vues ne sont jamais vendues seules non plus. Un essai de quelques milliers de vues en une heure montrerait seulement que quelqu'un a des scripts. Nous proposons un pack mensuel qui amène de vraies personnes sur votre chaîne, vues comprises, résiliable à tout moment.",
        "hero": {"image": "youtube-hub", "alt": "Un créateur compare les statistiques YouTube avec un tableau de bord de croissance"},
        "sections": [
            {
                "h2": "Ce que mesure un essai de vues",
                "p": [
                    "Une seule chose : si le chiffre bouge. Il ne dit rien de qui a regardé, combien de temps, ni si quelqu'un est revenu. Ce sont pourtant les questions qui comptent, et seuls de vrais spectateurs peuvent y répondre.",
                ],
            },
            {
                "h2": "Testez-nous avec les chiffres de YouTube",
                "p": [
                    "Pendant votre premier mois, ouvrez YouTube Studio à côté de notre tableau de bord. Regardez les spectateurs réguliers, la durée moyenne de visionnage et les nouveaux abonnés. De vraies personnes laissent dans ces chiffres une trace que des lectures achetées ne laissent jamais.",
                ],
            },
        ],
        "faqs": [
            ("Y a-t-il un essai pour les vues YouTube ?", "Aucun essai, ni pour les vues ni pour le reste. L'engagement le plus court est un mois de pack, et vous pouvez résilier avant le renouvellement."),
            ("Puis-je acheter un petit pack de vues pour tester ?", "Nous ne vendons pas de vues en pack séparé, petit ou grand. {starter_name}, à {starter_price} par mois, est la façon la plus légère de commencer."),
            ("Comment distinguer de vraies vues de vues achetées ?", "Regardez au-delà du compteur : la durée de visionnage, les spectateurs réguliers et les commentaires que les gens écrivent vous disent qui est vraiment là."),
            ("Et si je résilie après le premier mois ?", "Votre pack s'arrête à la fin du mois payé. Les spectateurs qui se sont abonnés restent abonnés, sauf s'ils choisissent de partir."),
            ("Les vues viennent-elles avec des abonnés ?", "Oui. Chaque pack apporte de nouveaux abonnés, des likes et des commentaires, et ces mêmes personnes regardent vos vidéos."),
        ],
    },
]
