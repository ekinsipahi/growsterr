"""French YouTube pages beyond the hub and subscribers: likes, views and the ways people ask for
subscribers (real, safe, monthly...). Keys and placeholders: docs/CONTENT.md. Brief:
docs/keywords/WRITING.md. Views are never counted in advance; we never promise monetization,
watch hours or retention."""

UPDATED = "2026-11-09"

PAGES = [
    # --- Likes ---------------------------------------------------------------------------
    {
        "service": "likes",
        "slug": "youtube/likes",
        "label": "Likes YouTube",
        "title": "Acheter des likes YouTube ? De vrais spectateurs | Growsterr",
        "description": "Acheter des likes YouTube ? Dans nos packs, chaque like vient d'un spectateur qui a regardé, avec abonnés et commentaires. Dès {from_price} par mois.",
        "h1": ("Vous voulez acheter des likes YouTube ? ", "Recevez-les de gens qui ont regardé."),
        "intro": "Si vous êtes venu acheter des likes YouTube, une réponse franche d'abord : chez nous, les likes ne se vendent pas en lots. Chaque pack amène sur votre chaîne de vraies personnes qui regardent vos vidéos et aiment celles qui leur plaisent, en général {starter_likes} likes par mois avec {starter_name}, davantage avec les packs supérieurs.",
        "hero": {"image": "youtube-viewers", "alt": "Des spectateurs aiment sur leur téléphone une vidéo YouTube qu'ils viennent de regarder"},
        "sections": [
            {
                "h2": "Ce qu'un like dit à YouTube",
                "p": [
                    "Un like est un petit vote public de quelqu'un qui a appuyé sur lecture. YouTube le lit avec tout ce que ce spectateur a fait d'autre : combien de temps il a regardé, s'il s'est abonné, s'il est revenu pour la vidéo suivante.",
                    "Un like venant d'un compte qui n'a jamais regardé casse ce schéma. Le compteur sous votre vidéo monte pendant que tout le reste stagne, et YouTube traite l'engagement qu'il juge artificiel comme du spam.",
                ],
            },
            {
                "h2": "Où arrivent les likes : vidéos, musique et posts",
                "p": [
                    "Les nouveaux spectateurs aiment ce qui leur plaît, généralement vos dernières vidéos et celle qui les a amenés sur votre chaîne. Les musiciens voient la même chose sur leurs clips et leurs vidéos de paroles : des likes d'auditeurs qui ont écouté le morceau et en voulaient plus.",
                    "Les posts de la communauté fonctionnent autrement. Vos abonnés les voient dans leur fil et peuvent les aimer d'eux-mêmes, mais les fourchettes que nous annonçons concernent les likes sur vos vidéos.",
                ],
                "image": {"image": "youtube-channel", "alt": "Un musicien enregistre un morceau dans son home studio pour un clip YouTube"},
            },
            {
                "h2": "Pourquoi les likes arrivent avec les abonnés",
                "p": [
                    "Un like est le geste le plus léger qu'un spectateur puisse faire. Dans un pack, il s'accompagne de signaux plus forts venant des mêmes personnes : un abonnement, un commentaire, un retour pour la vidéo suivante. Quand ces chiffres montent ensemble, ils décrivent une chaîne que les gens apprécient, parce que c'est le cas.",
                ],
            },
        ],
        "faqs": [
            ("Puis-je acheter des likes YouTube sans abonnés ?", "Non. Les likes viennent dans chaque pack, avec de nouveaux abonnés et des commentaires des mêmes vraies personnes. Un like sans personne qui regarde derrière, c'est le genre d'engagement que YouTube traite comme du spam."),
            ("À quoi ressemble un mois habituel de likes ?", "Avec {pick_name}, en général {pick_likes}, soit environ deux à trois likes par nouvel abonné. Ce sont de vraies personnes qui décident quoi aimer, donc deux mois ne se ressemblent jamais."),
            ("Puis-je avoir des likes sur un post de la communauté YouTube ?", "Pas sous forme de commande séparée. Vos nouveaux abonnés peuvent voir vos posts dans leur fil, et certains les aimeront parce qu'ils en ont envie. Les fourchettes habituelles de chaque pack comptent les likes sur les vidéos."),
            ("Les clips musicaux reçoivent-ils aussi des likes ?", "Oui. Si votre chaîne est musicale, les personnes que nous amenons sont des auditeurs qui ont écouté vos morceaux et aimé ceux qui leur plaisaient. Vous pouvez viser la ville, la région ou le pays où se trouvent vos auditeurs."),
            ("Quelles vidéos vont recevoir des likes ?", "Ce sont les vrais spectateurs qui choisissent : généralement vos vidéos les plus récentes et celle qui les a amenés sur votre chaîne."),
            ("Quand apparaissent les premiers likes ?", "Dans les premiers jours de votre campagne, avec l'arrivée des premiers spectateurs, puis quelques-uns chaque jour jusqu'à la fin du mois."),
        ],
    },
    {
        "service": "likes",
        "modifier": "comment-likes",
        "slug": "youtube/likes/commentaires",
        "label": "Likes de commentaires YouTube",
        "title": "Acheter des likes de commentaires YouTube ? | Growsterr",
        "description": "Acheter des likes de commentaires YouTube ? Nous ne faisons pas remonter un commentaire : de vrais spectateurs lisent vos fils et aiment ce qui leur parle.",
        "h1": ("Acheter des likes de commentaires YouTube ? ", "Créez des fils qui méritent d'être aimés."),
        "intro": "Ceux qui achètent des likes de commentaires YouTube veulent généralement faire remonter un commentaire. Nous ne vendons pas cela. Nous amenons de vrais spectateurs sur votre chaîne, et ceux qui lisent les commentaires sous vos vidéos aiment les réponses, les questions et les blagues qui leur parlent, votre commentaire épinglé compris.",
        "hero": {"image": "youtube-viewers", "alt": "Un spectateur fait défiler les commentaires sous une vidéo YouTube et aime une réponse"},
        "sections": [
            {
                "h2": "Un commentaire en haut n'est pas l'objectif",
                "p": [
                    "Un commentaire avec des centaines de likes sous une vidéo qui a à peine bougé saute aux yeux de quiconque lit le fil. Les likes de commentaires sont un engagement comme un autre : ceux qui viennent de scripts tombent donc aussi sous les règles de YouTube contre le spam.",
                    "Et si le commentaire se trouve sous la vidéo d'un autre créateur, le faire remonter n'est pas du tout quelque chose que nous faisons. Nous faisons grandir votre propre chaîne, avec des gens qui la choisissent.",
                ],
            },
            {
                "h2": "Comment un fil de commentaires prend vie",
                "p": [
                    "Les vrais spectateurs lisent les commentaires après avoir regardé. Ils répondent, aiment les commentaires avec lesquels ils sont d'accord et laissent les leurs : en général {pick_comments} nouveaux commentaires par mois avec {pick_name}, écrits par des personnes et non par des scripts.",
                ],
                "ul": [
                    "Épinglez un commentaire qui pose une vraie question aux spectateurs. Les réponses lancent leurs propres fils.",
                    "Répondez aux premiers commentaires d'une nouvelle vidéo. Un créateur présent dans le fil y attire plus de monde.",
                    "Mettez un cœur aux commentaires que vous aimez. Les spectateurs le remarquent, et reviennent discuter.",
                ],
                "image": {"image": "youtube-channel", "alt": "Un créateur épingle une question dans les commentaires d'une nouvelle vidéo YouTube"},
            },
            {
                "h2": "Ce que le pack compte, et ce qu'il ne compte pas",
                "p": [
                    "Les abonnés, les likes sur les vidéos et les commentaires ont des fourchettes mensuelles habituelles. Les likes de commentaires, non : ils arrivent quand un spectateur est d'accord avec un autre, et personne ne peut programmer cela.",
                ],
            },
        ],
        "faqs": [
            ("Pouvez-vous ajouter des likes à mon commentaire sous la vidéo d'une autre chaîne ?", "Non. Nous faisons grandir votre propre chaîne avec de vraies personnes qui la choisissent. Faire remonter un commentaire sous la vidéo de quelqu'un d'autre ne fait pas partie de ce que nous faisons."),
            ("Les likes de commentaires viennent-ils avec le pack ?", "Ils viennent comme sur toute chaîne animée : de vrais spectateurs qui lisent les fils sous vos vidéos. Nous ne les comptons pas à l'avance, car chacun est une personne qui approuve quelqu'un."),
            ("Mes fils de commentaires seront-ils vraiment plus animés ?", "À mesure que les gens arrivent, oui : en général {starter_comments} nouveaux commentaires par mois avec {starter_name}, {rising_comments} avec {rising_name} et {pro_comments} avec {pro_name}, venant des mêmes personnes qui s'abonnent."),
            ("Les commentaires sont-ils écrits par des bots ou une IA ?", "Non. Chaque commentaire vient d'une personne qui a regardé votre vidéo et avait quelque chose à dire. Nous ne scriptons jamais de commentaires et n'en écrivons pour personne."),
            ("Pouvez-vous envoyer des likes sur un commentaire de ma propre vidéo ?", "Non. Nous faisons la promotion de votre chaîne, et ce sont les spectateurs qui décident quels commentaires méritent un like, le vôtre compris. Un commentaire épinglé qui pose une vraie question est celui qui a le plus de chances d'en récolter."),
            ("Est-ce risqué d'acheter des likes pour des commentaires YouTube ?", "Auprès d'un service de bots, oui : les likes de commentaires sont de l'engagement, et YouTube traite l'engagement artificiel comme du spam. Des likes de personnes qui ont vraiment lu le fil, c'est la vie normale d'une chaîne."),
        ],
    },
    {
        "service": "likes",
        "modifier": "live",
        "slug": "youtube/likes/live",
        "label": "Likes de live YouTube",
        "title": "Likes de live YouTube : un vrai chat, de vrais likes | Growsterr",
        "description": "Avant d'acheter des likes de live YouTube : en direct, ils viennent des gens présents dans le chat. Nous faisons grandir les abonnés qui peuvent venir.",
        "h1": ("Acheter des likes de live YouTube ? ", "Ils viennent des gens présents dans votre chat."),
        "intro": "Avant d'acheter des likes de live YouTube, pensez à qui appuie sur le bouton : les personnes qui regardent vraiment votre direct. Nous ne pouvons pas faire tomber des likes dans une diffusion à une minute précise, et nous ne ferons pas semblant. Nous faisons grandir les vrais abonnés qui peuvent voir que vous êtes en direct et choisir de vous rejoindre.",
        "hero": {"image": "youtube-channel", "alt": "Un créateur diffuse un live YouTube depuis son bureau, avec caméra et micro"},
        "sections": [
            {
                "h2": "Un like en direct est une réaction, pas un chiffre",
                "p": [
                    "Pendant un live, les likes arrivent quand quelque chose se passe à l'écran : une action décisive, une bonne réponse, le morceau que le chat réclamait. C'est l'audience qui réagit sur le moment.",
                    "Des likes de comptes qui ne regardent pas ne réagissent à rien. Ils tombent en bloc à côté d'un chat silencieux, et chaque vraie personne qui arrive voit que les deux ne collent pas.",
                ],
            },
            {
                "h2": "Transformer les meilleurs moments d'un live en likes",
                "ul": [
                    "Demandez des likes une seule fois, à un moment fort, pas dans la première minute.",
                    "Citez les pseudos du chat à voix haute : on aime les lives dont on se sent partie prenante.",
                    "Épinglez un commentaire qui explique aux retardataires ce qui se passe, pour qu'ils restent assez longtemps pour réagir.",
                    "Gardez la rediffusion en ligne, pour que ceux qui ont manqué le live puissent quand même le regarder et l'aimer.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Des gens discutent et réagissent dans le chat d'un live YouTube pendant que le créateur parle"},
            },
            {
                "h2": "Faites grandir l'audience avant le prochain live",
                "p": [
                    "Les abonnés que nous amenons sont de vraies personnes qui ont trouvé votre chaîne et décidé de rester. Certains seront dans votre prochain chat, selon leur propre emploi du temps. Plus ce groupe grandit, plus il y a de monde pour réagir quand quelque chose de bien se passe en direct.",
                ],
            },
        ],
        "faqs": [
            ("Pouvez-vous envoyer des likes pendant mon live ?", "Non. De vraies personnes ont leur propre emploi du temps, donc personne d'honnête ne peut promettre des réactions à une heure donnée. Ce que nous faisons grandir, c'est l'audience susceptible de regarder quand vous passez en direct."),
            ("Mes nouveaux abonnés regarderont-ils mes lives ?", "Certains, les jours où ça leur convient. Ils ont choisi votre chaîne après l'avoir vue, donc vos lives peuvent les toucher ; venir ou non leur appartient."),
            ("Peut-on aimer un live après sa fin ?", "Oui. La rediffusion reste sur votre chaîne sous forme de vidéo, et quiconque la regarde plus tard peut l'aimer."),
            ("Pourquoi ne pas acheter des likes de live à un service de bots ?", "Parce qu'un direct est l'endroit où le faux engagement se repère le plus facilement. Des centaines de likes à côté d'un chat muet disent à tous ceux qui arrivent que la salle n'est pas ce qu'elle paraît."),
            ("Jusqu'où peut grandir l'audience de mes lives ?", "Cela dépend de vos lives, mais le vivier grandit chaque jour : {pick_name} ajoute en général {pick_audience} abonnés sur un mois, et chacun est quelqu'un qui pourrait être dans le chat la prochaine fois."),
        ],
    },
    {
        "service": "likes",
        "modifier": "shorts",
        "slug": "youtube/likes/shorts",
        "label": "Likes YouTube Shorts",
        "title": "Acheter des likes sur YouTube Shorts, des vrais | Growsterr",
        "description": "Des likes YouTube Shorts de vraies personnes qui ont arrêté de faire défiler, jamais de bots. Dans un pack mensuel avec abonnés et commentaires, dès {from_price}.",
        "h1": ("Acheter des likes sur YouTube Shorts ? ", "Gagnez-les auprès de ceux qui s'arrêtent."),
        "intro": "Dans le fil des Shorts, un like veut dire que quelqu'un a cessé de faire défiler assez longtemps pour s'y intéresser. Si vous voulez acheter des likes sur YouTube Shorts, c'est le seul genre qui vaille : des likes de vraies personnes que nous amenons chaque jour sur votre chaîne, qui regardent, aiment et parfois s'abonnent.",
        "hero": {"image": "youtube-viewers", "alt": "Des gens regardent des YouTube Shorts sur leur téléphone et appuient sur j'aime"},
        "sections": [
            {
                "h2": "Ce que vaut un like sur un Short",
                "p": [
                    "Les Shorts défilent dans un fil que l'on parcourt vite. Un like y vient d'un spectateur qui a laissé tourner votre Short, souvent plus d'une fois, et a jugé qu'il méritait un geste.",
                    "Les likes générés sautent tout cela. Ils s'empilent sur un Short que personne n'a continué à regarder, ce qui est l'inverse de ce qu'un like est censé dire.",
                ],
            },
            {
                "h2": "Ce qui donne envie d'aimer un Short",
                "ul": [
                    "Commencez par le moment fort. La première seconde décide si les gens restent.",
                    "Faites en sorte que la fin ramène au début, pour que revoir paraisse naturel.",
                    "Sous-titrez vos Shorts : beaucoup de gens font défiler sans le son.",
                    "Terminez par une raison claire de visiter votre chaîne.",
                ],
                "image": {"image": "youtube-channel", "alt": "Un créateur filme un YouTube Short vertical avec son téléphone tenu à bout de bras"},
            },
            {
                "h2": "Ce que le pack fait pour vos Shorts",
                "ul": [
                    "Nous faisons la promotion de votre chaîne ; les spectateurs qui la découvrent choisissent les Shorts et les vidéos qu'ils veulent regarder.",
                    "{pick_name} ajoute en général {pick_likes} likes sur un mois, répartis sur ce que les gens ont apprécié.",
                    "Indiquez-nous la ville, la région ou le pays : vos Shorts toucheront les gens du lieu pour lequel vous les créez.",
                ],
            },
        ],
        "faqs": [
            ("Puis-je avoir des likes sur un seul Short ?", "Pas en commande ponctuelle. Les likes arrivent dans un pack mensuel, répartis sur les Shorts et vidéos que les gens apprécient, avec des abonnés et des commentaires."),
            ("Les likes sur les Shorts aident-ils mes vidéos longues ?", "Indirectement. Certaines personnes qui aiment un Short ouvrent la chaîne qui se trouve derrière, et quelques-unes regardent ensuite vos vidéos plus longues et s'abonnent."),
            ("À quelle vitesse les likes arrivent-ils sur mes Shorts ?", "Dès les premiers jours de votre campagne, puis quelques-uns chaque jour tout au long du mois. Des milliers de likes sur des Shorts en une heure viennent de bots, pas de spectateurs."),
            ("Qui aime mes Shorts ?", "Des personnes qui ont découvert votre chaîne grâce à notre campagne, dans le lieu que vous avez choisi. Elles ont décidé de regarder et décidé d'aimer ; personne ne le leur a demandé."),
            ("Les gens commenteront-ils aussi mes Shorts ?", "Certains, oui. Sur l'ensemble de votre chaîne, {pick_name} apporte en général {pick_comments} commentaires par mois, chacun tapé par la personne qui l'a laissé."),
        ],
    },
    # --- Subscribers ---------------------------------------------------------------------
    {
        "service": "subscribers",
        "modifier": "gradual",
        "slug": "youtube/abonnes/progressifs",
        "label": "Abonnés YouTube progressifs",
        "title": "Acheter des abonnés YouTube lentement et sûrement | Growsterr",
        "description": "Des abonnés YouTube lents et réguliers : de vraies personnes qui s'abonnent peu à peu, chaque jour du mois, à leur rythme. Dès {from_price} par mois.",
        "h1": ("Des abonnés YouTube lents et réguliers ? ", "Le seul rythme des vraies personnes."),
        "intro": "Si vous voulez acheter des abonnés YouTube lentement et sûrement, vous demandez la bonne chose. Ici, la lenteur, c'est simplement ce que font les gens : ils découvrent votre chaîne le jour qui leur convient, regardent une vidéo ou deux, et décident. Avec {pick_name}, cela représente en général {pick_audience} sur le mois.",
        "hero": {"image": "youtube-subscribers", "alt": "Le nombre d'abonnés d'une chaîne YouTube monte un peu chaque jour au fil d'un mois"},
        "sections": [
            {
                "h2": "Des bots lents restent des bots",
                "p": [
                    "Certains services vendent une option goutte-à-goutte : les mêmes abonnés bots, libérés quelques-uns à la fois pour que la courbe paraisse douce. Le rythme change ; ce qu'il y a derrière, non. Des comptes qui ne regardent jamais font toujours baisser la part de vos abonnés qui s'impliquent.",
                    "La progressivité a un sens quand elle vient de personnes qui décident une à une. Aucun réglage ne peut l'imiter, et aucun n'est nécessaire.",
                ],
            },
            {
                "h2": "À quoi ressemble la régularité dans votre tableau de bord",
                "p": [
                    "Ouvrez votre tableau de bord n'importe quel jour et vous verrez deux lignes : les personnes qui ont visité votre chaîne via la campagne, et combien d'entre elles se sont abonnées. Certains jours sont plus chargés que d'autres, comme pour toute chaîne que les gens découvrent. Ce que vous ne verrez pas, c'est un bond de milliers en une nuit.",
                ],
            },
            {
                "h2": "Pourquoi la régularité l'emporte sur YouTube",
                "p": [
                    "Une chaîne qui gagne des abonnés chaque semaine, avec des vues et des commentaires, est une chaîne que les gens découvrent. Chaque nouvelle vidéo touche un groupe de vraies personnes un peu plus grand, et cela s'additionne au fil des mois.",
                ],
                "image": {"image": "youtube-channel", "alt": "Un créateur YouTube passe en revue un mois de croissance régulière sur son ordinateur"},
            },
        ],
        "faqs": [
            ("Lent, c'est-à-dire ?", "Étalé : une poignée de nouveaux abonnés la plupart des jours, jamais un lot. Sur 30 jours, cela forme la fourchette habituelle du pack, et chaque jour est un peu différent."),
            ("Puis-je choisir la vitesse d'arrivée des abonnés ?", "Pas heure par heure, car ce sont de vraies personnes qui la fixent. Vous choisissez le pack : un pack plus grand montre votre chaîne à plus de monde chaque jour."),
            ("Un goutte-à-goutte lent est-il plus sûr pour ma chaîne ?", "Seulement si les abonnés sont réels. Un goutte-à-goutte de bots reste du faux engagement, alors que de vraies personnes qui s'abonnent à leur rythme, c'est une croissance ordinaire."),
            ("Des abonnés quotidiens auront-ils l'air suspects ?", "Non. Les chaînes que les gens découvrent gagnent des abonnés chaque jour : c'est la forme normale de la croissance. Ce qui détonne, ce sont des milliers d'abonnés en une heure."),
            ("Que se passe-t-il à la fin du mois ?", "Le pack se renouvelle et la campagne continue au même rythme régulier, sauf si vous résiliez. La résiliation arrête le prochain paiement ; votre mois en cours va jusqu'à son terme."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "monthly",
        "slug": "youtube/abonnes/mensuels",
        "label": "Abonnés YouTube mensuels",
        "title": "Abonnés YouTube au mois, sans engagement | Growsterr",
        "description": "Des abonnés YouTube au mois : un pack qui amène de vraies personnes sur votre chaîne, payé par carte, résiliable à tout moment. Dès {from_price}.",
        "h1": ("Acheter des abonnés YouTube au mois, ", "comme grandissent vraiment les chaînes."),
        "intro": "Un pack mensuel, c'est exactement notre façon de travailler. Quand vous achetez des abonnés YouTube au mois chez nous, votre chaîne est présentée chaque jour à de vraies personnes, celles qui l'aiment s'abonnent, et le pack se renouvelle chaque mois jusqu'à ce que vous décidiez d'arrêter.",
        "hero": {"image": "youtube-subscribers", "alt": "Une chaîne YouTube qui gagne de nouveaux abonnés mois après mois"},
        "sections": [
            {
                "h2": "Pourquoi un abonnement plutôt qu'un lot ponctuel",
                "p": [
                    "Une chaîne n'est pas terminée après une seule poussée. Vous continuez à publier, donc vous avez toujours besoin que de nouvelles personnes vous trouvent. Un pack mensuel suit ce rythme : chaque nouvelle vidéo arrive devant une audience qui grandit encore.",
                    "Les lots ponctuels font l'inverse. Ils livrent un chiffre le premier jour et plus rien ensuite, et comme aucune vraie audience n'apparaît sur commande, ce chiffre est presque toujours fait de bots.",
                ],
            },
            {
                "h2": "Payer mois par mois",
                "ul": [
                    "Le paiement se fait par carte via le paiement sécurisé de Stripe, ou par Apple Pay et Google Pay sur les appareils compatibles.",
                    "Le pack se renouvelle chaque mois à partir du jour où vous commencez.",
                    "Arrêter prend un clic dans votre compte, et aucun autre paiement n'est prélevé.",
                    "Vous pouvez passer au pack supérieur quand vos vidéos sont prêtes pour plus de monde.",
                ],
            },
            {
                "h2": "Ce qui se construit mois après mois",
                "p": [
                    "Chaque mois ajoute de vrais abonnés qui restent tant que votre chaîne leur plaît. Au bout de plusieurs mois, cela devient une base de personnes qui voient vos vidéos, si bien que chaque nouvelle vidéo démarre avec plus de monde.",
                ],
                "image": {"image": "youtube-channel", "alt": "Un créateur planifie les vidéos YouTube du mois prochain sur un calendrier mural"},
            },
        ],
        "faqs": [
            ("Est-ce un abonnement ?", "Oui. Chaque pack est un abonnement mensuel, payé par carte, Apple Pay ou Google Pay via Stripe. Il n'y a pas de lots ponctuels."),
            ("Qu'apporte habituellement chaque mois ?", "{starter_name} apporte en général {starter_audience}, {rising_name} {rising_audience} et {pro_name} {pro_audience}. Chaque mois diffère un peu, car chaque abonné est une personne qui fait un choix."),
            ("Puis-je résilier après le premier mois ?", "Oui. Résiliez depuis votre compte quand vous voulez ; le mois déjà payé continue jusqu'à son dernier jour, et rien ne se renouvelle ensuite."),
            ("Est-ce que je garde mes abonnés si je résilie ?", "Personne ne part parce que vous avez arrêté de payer : ce sont des personnes, et elles restent abonnées tant que votre chaîne les intéresse. La résiliation met fin aux nouvelles campagnes ; elle ne retire personne."),
            ("Avec quoi puis-je payer ?", "Une carte, ou Apple Pay ou Google Pay si votre téléphone les propose. Le moyen choisi est débité de nouveau chaque mois jusqu'à la résiliation."),
            ("Puis-je commencer petit et passer ensuite à un pack plus grand ?", "Oui. Commencez là où en est votre chaîne aujourd'hui, souvent avec {starter_name}, et montez quand vous publiez assez pour accueillir plus de monde."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "no-drop",
        "slug": "youtube/abonnes/sans-perte",
        "label": "Abonnés YouTube sans perte",
        "title": "Abonnés YouTube sans perte et sans bots | Growsterr",
        "description": "Un compteur d'abonnés baisse quand les abonnés n'ont jamais été réels. Les nôtres sont des personnes qui ont choisi votre chaîne. Dès {from_price} par mois.",
        "h1": ("Des abonnés YouTube sans perte ? ", "Commencez par des gens qui ont choisi votre chaîne."),
        "intro": "Vouloir acheter des abonnés YouTube sans perte veut généralement dire que vous avez déjà vu un compteur chuter. Les abonnés disparaissent quand ils n'ont jamais été des personnes : YouTube fait le ménage parmi le spam et les comptes fermés, et les abonnés bots partent avec. Les nôtres sont de vrais spectateurs qui ont choisi de s'abonner, le genre de compte qu'un nettoyage laisse tranquille.",
        "hero": {"image": "youtube-subscribers", "alt": "Un nombre d'abonnés YouTube qui tient bon pendant que de vrais abonnés arrivent"},
        "sections": [
            {
                "h2": "Pourquoi les compteurs d'abonnés baissent",
                "p": [
                    "YouTube retire les abonnés qu'il juge être du spam, ainsi que les comptes qui ont été fermés. Les chaînes qui ont acheté des abonnés bots voient ces chiffres baisser par paliers, parfois des mois après l'achat.",
                    "La baisse est la partie visible. La partie cachée, c'est le temps que ces comptes ont passé sur votre chaîne sans jamais regarder, en faisant baisser la part de vos abonnés qui s'impliquent.",
                ],
            },
            {
                "h2": "Pourquoi une recharge n'est pas la solution",
                "p": [
                    "Certains vendeurs promettent de recharger tout ce qui tombe. Cela revient à remplacer des bots supprimés par de nouveaux bots, ce qui maintient le chiffre et prolonge le problème. Un vrai abonné n'a pas besoin d'être remplacé.",
                ],
            },
            {
                "h2": "À quoi ressemble un vrai « sans perte »",
                "p": [
                    "De vraies personnes peuvent se désabonner, comme sur n'importe quelle chaîne, et avec le temps quelques-unes le feront. C'est une érosion normale, minime à côté des vagues que laissent les bots. Ce qui reste, c'est une audience encore là quand vous publiez.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Des abonnés de longue date regardent la dernière vidéo YouTube d'un créateur sur leur canapé"},
            },
        ],
        "faqs": [
            ("Certains de mes nouveaux abonnés partiront-ils un jour ?", "Certains peut-être, comme sur toute chaîne quand les goûts changent. Ce que vous n'aurez pas, c'est un lot de faux comptes en attente d'être supprimés ensemble."),
            ("Y a-t-il une recharge si des abonnés partent ?", "Non, car il n'y a pas de faux compteur à compléter. Vous avez un pack mensuel de vraies personnes ; ce qu'elles font ensuite leur appartient, comme pour toute audience."),
            ("Pourquoi mon compteur a-t-il baissé après un autre service ?", "Très probablement parce que YouTube a retiré des comptes qu'il jugeait être du spam, ou des comptes fermés. Les abonnés bots partent souvent par gros lots lors de ces nettoyages."),
            ("Des abonnés bots peuvent-ils nuire à ma chaîne même après leur départ ?", "La suppression est le moindre problème. Tant qu'ils étaient là, ils n'ont jamais regardé une seule vidéo, ce qui faisait paraître votre audience moins impliquée qu'elle ne l'était."),
            ("Mon tableau de bord correspond-il à mon compteur YouTube ?", "Pas exactement. Votre tableau de bord compte les nouveaux abonnés apportés par notre campagne ; le total affiché par YouTube inclut aussi la croissance venue d'ailleurs et les désabonnements."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "organic",
        "slug": "youtube/abonnes/organiques",
        "label": "Abonnés YouTube organiques",
        "title": "Abonnés YouTube organiques : comment ça marche | Growsterr",
        "description": "Peut-on acheter des abonnés YouTube organiques ? Nous payons la présentation ; s'abonner reste le choix du spectateur. Dès {from_price} par mois.",
        "h1": ("Acheter des abonnés YouTube organiques ? ", "Nous payons la présentation. Ils choisissent."),
        "intro": "Voici la réponse honnête pour qui veut acheter des abonnés YouTube organiques : personne ne peut vous vendre une décision. Ce que nous payons, c'est la présentation. Votre chaîne est montrée à de vraies personnes grâce à des campagnes sponsorisées dans notre réseau partenaire, et ceux qui s'abonnent le font parce qu'ils le veulent.",
        "hero": {"image": "youtube-subscribers", "alt": "De nouveaux abonnés rejoignent une chaîne YouTube après avoir découvert ses vidéos"},
        "sections": [
            {
                "h2": "La frontière entre payant et organique",
                "p": [
                    "Toute chaîne qui fait de la publicité paie pour de l'attention. Ce qui suit est organique ou ne l'est pas : une personne regarde, aime la vidéo ou non, s'abonne ou passe son chemin.",
                    "Nous gardons cette frontière nette. Nous payons pour placer votre chaîne devant des gens chaque jour ; nous ne payons jamais personne pour s'abonner, n'échangeons jamais d'abonnements et n'utilisons jamais de comptes qui agissent sur commande.",
                ],
            },
            {
                "h2": "Distinguer les abonnés organiques des autres",
                "ul": [
                    "Leurs noms apparaissent dans les commentaires de votre vidéo suivante.",
                    "Leurs commentaires ressemblent à des personnes : questions, blagues, désaccords de temps en temps.",
                    "Les nouveaux abonnés arrivent avec des visites de la chaîne, jamais sans.",
                    "Ils restent après la fin de la campagne, puisque rien ne les retenait.",
                ],
            },
            {
                "h2": "Organique ne veut pas forcément dire attendre",
                "p": [
                    "On imagine souvent la croissance organique comme des années d'attente pour une vidéo chanceuse. Une campagne sponsorisée raccourcit l'attente : de vraies personnes voient votre chaîne dès les premiers jours. La seule chose qu'elle ne peut pas raccourcir, c'est leur décision, et c'est la partie qui mérite d'être préservée.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Quelqu'un, café à la main, appuie sur S'abonner sur une chaîne découverte le matin même"},
            },
        ],
        "faqs": [
            ("Si vous faites la promotion de ma chaîne, la croissance reste-t-elle organique ?", "Les abonnements, oui. Nous payons pour que votre chaîne soit montrée ; personne n'est payé ni récompensé pour s'abonner. Chaque abonné a décidé seul après avoir vu vos vidéos."),
            ("Utilisez-vous le « sub4sub » ou des réseaux d'échange ?", "Jamais. Ceux qui s'abonnent pour obtenir un abonnement en retour ne s'intéressent pas à vos vidéos et les regardent rarement, et YouTube compte ces échanges comme du faux engagement."),
            ("Que représente la croissance organique en un mois ?", "{pick_name} se situe généralement dans une fourchette de {pick_audience} par mois. Comme chacun est une personne qui choisit, c'est une fourchette plutôt qu'un compte exact."),
            ("Les abonnés organiques regarderont-ils mes vidéos ?", "Ils ont choisi votre chaîne après l'avoir vue, ce qui est le meilleur départ possible pour un abonné. Qu'ils regardent chaque vidéo dépend de la vidéo, comme pour tout le monde."),
            ("Dois-je faire quelque chose pendant la campagne ?", "Gardez votre chaîne publique et continuez à publier. Plus vos vidéos correspondent à ce que promet la page de votre chaîne, plus les visiteurs décident de s'abonner."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "real",
        "slug": "youtube/abonnes/vrais",
        "label": "Vrais abonnés YouTube",
        "title": "Acheter de vrais abonnés YouTube, faciles à contrôler | Growsterr",
        "description": "Réels, authentiques, de qualité : quatre signes à contrôler chez un abonné YouTube, et comment nos packs amènent des gens qui y répondent.",
        "h1": ("Acheter de vrais abonnés YouTube. ", "Voici comment les reconnaître."),
        "intro": "Quand on achète des abonnés YouTube, « vrais » est le mot qu'on ajoute après s'être fait avoir une fois. Pour nous, il doit désigner quelque chose de contrôlable : une personne qui a découvert votre chaîne, a jugé qu'elle valait un abonnement, puis apparaît dans vos vues, vos likes et vos commentaires.",
        "hero": {"image": "youtube-subscribers", "alt": "La page d'une chaîne YouTube où de vrais abonnés arrivent au fil d'un mois"},
        "sections": [
            {
                "h2": "Quatre signes qu'un abonné est réel",
                "p": [
                    "Haute qualité, authentique, réel : tous les vendeurs emploient ces mots. Voici les contrôles qui permettent de les départager.",
                ],
                "ul": [
                    "Il y a eu une visite d'abord : quelqu'un a ouvert votre chaîne avant de s'abonner.",
                    "Ils regardent : les vues de votre vidéo suivante montent avec le nombre d'abonnés.",
                    "Ils parlent, dans des commentaires qu'aucun script n'écrirait.",
                    "Ils vivent là où vous avez dirigé la campagne, dans le lieu indiqué lors de la commande.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Un nouvel abonné commente une vidéo YouTube avec ses propres mots"},
            },
            {
                "h2": "Comparez-nous à YouTube Studio",
                "p": [
                    "Notre version des faits, c'est votre tableau de bord Growsterr : les visites de votre chaîne venues de la campagne, et qui parmi elles s'est abonné. YouTube Studio raconte le même mois du côté de YouTube. Lisez-les ensemble sur un mois : à mesure que les abonnés arrivent, vos vidéos devraient aussi gagner des vues et des commentaires de nouvelles personnes.",
                ],
            },
            {
                "h2": "Ce que de vrais abonnés ne peuvent pas faire",
                "p": [
                    "On ne commande pas de vraies personnes à l'heure, on ne leur dicte pas leurs commentaires et elles ne peuvent pas promettre de regarder chaque vidéo. Quiconque propose cela décrit autre chose que des personnes. Nous préférons vous dire les limites que vous vendre un compteur.",
                ],
            },
        ],
        "faqs": [
            ("Que veut dire « haute qualité » pour des abonnés YouTube ?", "Pour nous, une personne avec son propre compte, qui a choisi votre chaîne et peut regarder, aimer et commenter. Photos de profil et ancienneté du compte se falsifient facilement ; une vraie décision de s'abonner, non."),
            ("Vos abonnés sont-ils de vraies personnes ou des comptes que vous contrôlez ?", "De vraies personnes. Nous ne possédons, ne gérons ni ne louons aucun compte. Nous montrons votre chaîne grâce à des campagnes sponsorisées, et les gens qui la voient décident."),
            ("Puis-je acheter de vrais abonnés YouTube en ligne sans partager mes identifiants ?", "Oui, et vous ne devriez jamais les partager avec qui que ce soit. Il nous faut l'identifiant de votre chaîne et une chaîne publique, rien de plus."),
            ("De vrais abonnés permettront-ils de monétiser ma chaîne ?", "C'est la décision de YouTube, donc nous ne promettons jamais la monétisation ni des heures de visionnage. De vrais abonnés peuvent regarder vos vidéos, ce que les bots ne font jamais, mais ce sont les conditions et l'examen de YouTube qui décident qui est monétisé."),
            ("À quoi ressemble un mois de vraie croissance ?", "Avec {pick_name}, en général {pick_audience} nouveaux abonnés, qui arrivent en petit nombre chaque jour. Une petite chaîne peut commencer avec {starter_name} à {starter_price} par mois."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "safe",
        "slug": "youtube/abonnes/fiables",
        "label": "Abonnés YouTube fiables",
        "title": "Acheter des abonnés YouTube de façon fiable et sûre | Growsterr",
        "description": "Est-ce fiable et sûr d'acheter des abonnés YouTube ? Regardez qui gère le service, ce qu'il demande et comment arrivent les abonnés. Voici nos réponses.",
        "h1": ("Acheter des abonnés YouTube en toute confiance ? ", "Regardez d'abord qui est derrière."),
        "intro": "Vous vous demandez si l'on peut acheter des abonnés YouTube de façon fiable et sûre ? Pour être digne de confiance, un service doit passer trois contrôles : une société que l'on peut nommer, rien qui touche à vos identifiants, et des abonnés qui sont de vraies personnes. Growsterr est un produit de Sterr Agency, et voici comment nous répondons à chacun.",
        "hero": {"image": "youtube-subscribers", "alt": "La chaîne YouTube d'un créateur grandit sans risque avec des abonnés bien réels"},
        "sections": [
            {
                "h2": "Qui vous payez",
                "p": [
                    "Sterr Agency est derrière Growsterr, immatriculée sous le nom de Sterr Technologies OÜ à Tallinn, en Estonie, avec son siège en Turquie. Vous payez via le paiement sécurisé de Stripe, et l'abonnement se trouve dans votre propre compte, où vous pouvez le résilier.",
                ],
            },
            {
                "h2": "Comment votre chaîne reste protégée",
                "ul": [
                    "Votre mot de passe Google reste le vôtre : nous ne le demandons jamais, et personne chez nous ne se connecte à votre chaîne.",
                    "Personne n'est payé pour s'abonner, et il n'y a aucun échange d'abonnements.",
                    "Les abonnés arrivent au fil du mois, jamais en un lot.",
                    "Les likes et les commentaires viennent des abonnés eux-mêmes, donc tous les chiffres évoluent ensemble.",
                ],
                "image": {"image": "youtube-channel", "alt": "Un créateur consulte les paramètres de sa chaîne YouTube, connecté uniquement sur son propre appareil"},
            },
            {
                "h2": "Les signaux d'alerte de tout service de croissance",
                "ul": [
                    "Il demande vos identifiants, ou un accès à votre compte Google.",
                    "Il promet un nombre exact d'abonnés à une date fixe.",
                    "Il vend abonnés, vues et likes en lots séparés, par milliers.",
                    "Il ne peut pas vous dire d'où viennent les abonnés, ni vous montrer ce qu'il a mesuré.",
                ],
            },
        ],
        "faqs": [
            ("Est-ce légitime d'acheter des abonnés YouTube ?", "Payer pour de la promotion est banal : toute chaîne qui fait de la publicité le fait. Payer pour du faux engagement ne l'est pas : bots, scripts et échanges d'abonnements sont ce que YouTube traite comme du spam. Nous faisons uniquement la promotion de votre chaîne auprès de vraies personnes, qui décident elles-mêmes."),
            ("YouTube peut-il bannir ma chaîne pour cela ?", "YouTube sanctionne le faux engagement, c'est pourquoi nous n'en utilisons jamais. Nous ne pouvons pas parler des décisions de YouTube, mais des gens qui choisissent votre chaîne après l'avoir vue, c'est ainsi que fonctionne la promotion partout."),
            ("Que dois-je fournir pour commencer ?", "L'identifiant de votre chaîne, le lieu d'où doit venir votre audience et une carte de paiement pour le pack mensuel. Votre chaîne doit être publique pour que les gens puissent s'abonner."),
            ("Mon paiement est-il sécurisé ?", "Stripe traite chaque paiement, que vous utilisiez une carte, Apple Pay ou Google Pay. Vos données de carte restent chez Stripe, pas chez nous."),
            ("Et si ça ne me convient pas ?", "Résiliez depuis votre compte quand vous voulez. Aucun nouveau paiement n'est prélevé ensuite, et votre mois en cours continue jusqu'à son terme."),
        ],
    },
    # --- Views ---------------------------------------------------------------------------
    {
        "service": "views",
        "slug": "youtube/vues",
        "label": "Vues YouTube",
        "title": "Acheter des vues YouTube de vraies personnes | Growsterr",
        "description": "Acheter des vues YouTube ? Les nôtres viennent de vraies personnes qui choisissent de regarder, dans un pack avec abonnés, likes et commentaires.",
        "h1": ("Acheter des vues YouTube ? ", "Chacune vient d'une personne."),
        "intro": "Si vous êtes ici pour acheter des vues YouTube, voici comment fonctionnent les nôtres. Il n'y a pas de menu de nombres de vues. Chaque pack présente votre chaîne à de vraies personnes chaque jour ; elles lancent ce qui les intéresse, et beaucoup aiment, commentent et s'abonnent ensuite. Les vues viennent avec le pack, et chacune est une personne.",
        "hero": {"image": "youtube-viewers", "alt": "De vraies personnes lancent la lecture de la vidéo YouTube d'un créateur"},
        "sections": [
            {
                "h2": "Pourquoi nos packs n'affichent pas de nombre de vues",
                "p": [
                    "Une vue, c'est une personne qui décide de regarder, et personne ne peut promettre combien de personnes le décideront. Quiconque vend un nombre exact de vues pour une heure donnée vend des lectures générées par des scripts ou des bots.",
                    "YouTube traite les vues gonflées artificiellement comme du spam : il peut les supprimer, et elles ne comptent jamais pour la monétisation. Nous vendons donc ce que nous pouvons assumer : une campagne mensuelle qui amène de vraies personnes, avec des fourchettes habituelles pour les abonnés, likes et commentaires qu'elles laissent.",
                ],
            },
            {
                "h2": "Clips musicaux, playlists et vidéos longues",
                "p": [
                    "Nous faisons la promotion de votre chaîne, pas d'un seul morceau. Les auditeurs qui la découvrent choisissent les titres qui les accrochent, et ceux qui aiment un morceau peuvent poursuivre dans vos playlists ; chaque lecture y est la leur.",
                ],
                "image": {"image": "youtube-channel", "alt": "Un musicien met en ligne un nouveau clip sur sa chaîne YouTube"},
            },
            {
                "h2": "Avant de choisir un site pour acheter des vues YouTube",
                "ul": [
                    "Demandez ce qu'une vue signifie pour eux : une personne qui a choisi de regarder, ou une lecture qu'ils ont générée.",
                    "Regardez si les vues arrivent seules ou avec des abonnés, des likes et des commentaires des mêmes personnes.",
                    "Cherchez un nom de société, un vrai paiement en ligne et un moyen de résilier.",
                    "Fuyez quiconque demande votre mot de passe Google.",
                ],
            },
        ],
        "faqs": [
            ("Puis-je commander des vues sans pack ?", "Non. Chaque vue que nous amenons appartient à quelqu'un qui pourrait aussi s'abonner, aimer ou commenter, et c'est pourquoi elles ne viennent qu'avec un pack. Un compteur de vues qui grimpe pendant que rien d'autre ne bouge, c'est le schéma du trafic artificiel."),
            ("Me direz-vous combien de vues attendre ?", "Nous ne chiffrons pas les vues, car chacune est le choix d'une personne. Ce que nous annonçons, ce sont des fourchettes mensuelles habituelles : avec {pick_name}, {pick_audience} nouveaux abonnés et {pick_likes} likes, et ces personnes regardent avant de faire l'un ou l'autre."),
            ("Existe-t-il une appli pour acheter des vues YouTube ?", "Nous n'utilisons pas d'appli. Vous choisissez un pack sur notre site, payez via Stripe et suivez votre campagne dans le tableau de bord de votre compte, depuis n'importe quel navigateur."),
            ("Que sont les vues YouTube « premium » ?", "Rien que YouTube reconnaisse. YouTube Premium est un abonnement pour les spectateurs, pas un type de vue que quelqu'un pourrait vous vendre. Les seules vues qui valent la peine appartiennent à des personnes qui ont lancé la lecture elles-mêmes."),
            ("Des vues achetées peuvent-elles rendre une vidéo virale ?", "Personne ne peut le promettre. De vrais spectateurs donnent à une vidéo plus de personnes susceptibles de la partager : c'est la version honnête d'une chance de devenir viral."),
            ("Les vues aident-elles ma chaîne à être monétisée ?", "Nous ne promettons ni la monétisation ni des heures de visionnage. Les vues artificielles n'y comptent pas du tout ; de vrais spectateurs peuvent regarder vos vidéos, mais c'est YouTube qui décide qui est monétisé."),
        ],
    },
    {
        "service": "views",
        "modifier": "gradual",
        "slug": "youtube/vues/progressives",
        "label": "Vues YouTube progressives",
        "title": "Acheter des vues YouTube lentes et régulières | Growsterr",
        "description": "Des vues YouTube lentes qui montent au fil du mois : de vrais spectateurs trouvent votre chaîne peu à peu, avec abonnés et likes des mêmes personnes.",
        "h1": ("Acheter des vues YouTube lentes ? ", "De vrais spectateurs n'arrivent jamais autrement."),
        "intro": "Vouloir acheter des vues YouTube lentes, c'est un bon réflexe : une vidéo qui gagne des vues sur plusieurs jours est une vidéo que les gens découvrent. Ici, personne n'a besoin d'activer ce rythme. De vraies personnes découvrent votre chaîne chaque jour du mois et regardent ce qui les intéresse : vos vues montent comme sur toute chaîne qui grandit.",
        "hero": {"image": "youtube-viewers", "alt": "Des spectateurs découvrent une chaîne YouTube un par un pendant plusieurs semaines"},
        "sections": [
            {
                "h2": "Un goutte-à-goutte programmé, ce n'est pas la même chose",
                "p": [
                    "Un goutte-à-goutte programmé étale des lectures générées sur une semaine au lieu d'une heure. Le compteur monte plus calmement, mais les lectures arrivent toujours sans vrai visionnage, sans likes et sans abonnés. YouTube regarde ce que font les spectateurs, pas seulement la vitesse à laquelle ils sont arrivés.",
                ],
            },
            {
                "h2": "Vos anciennes vidéos sont regardées aussi",
                "p": [
                    "Des spectateurs qui arrivent au fil des semaines ne regardent pas que votre dernière vidéo. Quelqu'un qui en apprécie une peut en ouvrir une autre depuis la page de votre chaîne, si bien que les anciennes vidéos gagnent des vues au même rythme tranquille. Un goutte-à-goutte dirigé vers un seul lien ne peut pas faire cela.",
                ],
                "image": {"image": "youtube-channel", "alt": "La page d'une chaîne YouTube dont les anciennes vidéos gagnent de nouvelles vues"},
            },
            {
                "h2": "Un rythme que vous pouvez suivre",
                "p": [
                    "Le tableau de bord suit des personnes, pas des lectures : les visites quotidiennes de votre chaîne venues de la campagne et les abonnés parmi elles. Les vues n'y figurent pas, puisque nous ne les comptons pas à l'avance ; vous les trouverez dans YouTube Studio, sur les vidéos que les gens ont choisies.",
                ],
            },
        ],
        "faqs": [
            ("Y a-t-il un chiffre de vues quotidien sur lequel compter ?", "Il n'y a pas de chiffre quotidien à donner : chaque vue dépend de quelqu'un qui décide de regarder. Ce à quoi vous pouvez vous attendre, ce sont de nouveaux spectateurs chaque jour du mois, pas un pic le premier jour."),
            ("Puis-je étaler les vues sur un nombre de jours précis ?", "Chaque campagne court sur 30 jours et se renouvelle chaque mois. Dans cette fenêtre, ce sont de vraies personnes qui donnent le rythme, donc nous ne programmons pas les vues jour par jour."),
            ("Des vues lentes paraissent-elles plus naturelles à YouTube ?", "La vitesse n'est qu'une partie de la question. YouTube voit aussi si les spectateurs continuent de regarder, aiment la vidéo et reviennent. De vraies personnes font cela à n'importe quel rythme ; des lectures programmées, jamais."),
            ("Et les vidéos publiées l'an dernier ?", "Elles en font partie. Ceux qui aiment une vidéo regardent souvent ce qu'il y a d'autre sur votre chaîne, et les anciennes vidéos sont souvent là où ils atterrissent ensuite."),
            ("Et si je veux des vues plus vite ?", "Choisissez un pack plus grand, pour que plus de monde voie votre chaîne chaque jour. Tout ce qui promet des milliers de vues dans l'heure génère des lectures, sans trouver de spectateurs."),
        ],
    },
    {
        "service": "views",
        "modifier": "high-retention",
        "slug": "youtube/vues/haute-retention",
        "label": "Vues YouTube à haute rétention",
        "title": "Vues YouTube à haute rétention : la réponse honnête | Growsterr",
        "description": "Des vues YouTube à haute rétention ne s'achètent pas : la rétention se gagne par la vidéo. Nous amenons de vrais spectateurs qui ont choisi de regarder.",
        "h1": ("Acheter des vues YouTube à haute rétention ? ", "Amenez des gens qui veulent regarder."),
        "intro": "Si vous voulez acheter des vues YouTube à haute rétention, vous savez déjà que le nombre de lectures n'est pas l'essentiel : vous voulez des spectateurs qui restent. Mais la rétention ne se vend pas : c'est le temps que de vraies personnes choisissent de continuer à regarder. Notre part, c'est d'amener des spectateurs qui ont lancé la lecture par choix ; combien de temps ils restent dépend de votre vidéo.",
        "hero": {"image": "youtube-channel", "alt": "Un créateur monte une longue vidéo YouTube pour retenir ses spectateurs"},
        "sections": [
            {
                "h2": "La rétention qu'on achète est un minuteur",
                "p": [
                    "Quand un vendeur propose des vues avec une rétention fixée, il y a derrière un lecteur réglé pour tourner un nombre précis de secondes. Il regarde de la même façon quoi qu'il y ait à l'écran, et il n'aime, ne commente ni ne s'abonne jamais. Quelle que soit sa durée de lecture, c'est de l'engagement artificiel, et YouTube le traite comme du spam.",
                ],
            },
            {
                "h2": "Pourquoi de vrais spectateurs donnent du sens à la rétention",
                "p": [
                    "La rétention compte parce qu'elle montre que ceux qui ont commencé une vidéo voulaient continuer. Cela ne vaut que s'ils ont choisi la vidéo au départ. De vrais spectateurs vous donnent des données de rétention honnêtes : où ils restent, où ils décrochent et ce qui les fait revenir.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Un spectateur, penché vers l'écran, regarde une longue vidéo YouTube jusqu'au bout"},
            },
            {
                "h2": "Ce qui augmente la rétention, de votre côté",
                "ul": [
                    "Tenez dès les premières secondes ce que promettent le titre et la miniature.",
                    "Coupez l'introduction lente : montrez l'essentiel d'abord, expliquez ensuite.",
                    "Ajoutez des chapitres aux vidéos longues, pour que les spectateurs aillent à ce qu'ils cherchent au lieu de partir.",
                    "Repérez dans YouTube Studio où les spectateurs décrochent, et corrigez ce moment dans votre vidéo suivante.",
                ],
            },
        ],
        "faqs": [
            ("Promettez-vous un pourcentage de rétention ou des heures de visionnage ?", "Non. La rétention et la durée de visionnage dépendent de la vidéo et de chaque spectateur. Nous amenons de vraies personnes qui ont choisi de regarder, et ne chiffrons jamais combien de temps elles restent."),
            ("Les gens regarderont-ils toute ma vidéo ?", "Certains oui, d'autres non, et c'est exactement ce qui rend leurs données utiles. YouTube Studio vous montre où les gens restent et où ils partent."),
            ("Les vues à haute rétention comptent-elles pour la monétisation ?", "Les vues artificielles ne comptent pas du tout pour la monétisation, quelle que soit leur rétention. Le temps de visionnage de vrais spectateurs est authentique, mais nous ne promettons jamais la monétisation : c'est à YouTube d'en décider."),
            ("La campagne peut-elle pousser les spectateurs vers une seule vidéo ?", "Nous ne dirigeons pas les spectateurs vers des vidéos isolées : nous faisons la promotion de votre chaîne, et les gens choisissent quoi regarder. Vous pouvez quand même les orienter, car la vidéo mise en avant sur la page de votre chaîne est la première chose que voient les nouveaux visiteurs."),
            ("Quelles vidéos en profitent le plus ?", "Celles qui tiennent leur promesse. Une accroche claire, une miniature honnête et un rythme soutenu transforment de nouveaux spectateurs en longs visionnages, et plus la campagne amène de monde sur votre chaîne, plus ces vidéos peuvent en retenir."),
        ],
    },
    {
        "service": "views",
        "modifier": "live",
        "slug": "youtube/vues/live",
        "label": "Vues de live YouTube",
        "title": "Vues de live YouTube : construire une vraie audience | Growsterr",
        "description": "Personne ne peut remplir un live YouTube de vraies personnes à heure fixe. Nous faisons grandir les abonnés qui pourront rejoindre le prochain.",
        "h1": ("Acheter des vues pour un live YouTube ? ", "Construisez l'audience qui viendra."),
        "intro": "Si vous voulez acheter des vues pour un live YouTube, vous voulez un direct qui ne paraisse pas vide quand vous lancez la diffusion. Personne ne peut amener de vraies personnes sur une diffusion à une minute précise, et nous ne le prétendons pas. Ce que nous faisons, c'est faire grandir votre chaîne avec de vrais abonnés chaque jour, pour que chaque live compte plus de personnes susceptibles de venir.",
        "hero": {"image": "youtube-channel", "alt": "Un créateur s'apprête à passer en direct sur YouTube, avec un live programmé à l'écran"},
        "sections": [
            {
                "h2": "Pourquoi un compteur de live acheté se retourne contre vous",
                "p": [
                    "Le nombre de spectateurs est la première chose que l'on voit sur un live. Quand il affiche des centaines de personnes et que le chat est muet, chaque vrai visiteur le remarque. Les spectateurs de live achetés n'écrivent pas, ne réagissent pas et ne reviennent pas pour la rediffusion.",
                    "Les règles de YouTube sur les fausses vues ne s'arrêtent pas quand vous passez en direct. Un compteur de live n'est pas un endroit plus sûr pour tricher.",
                ],
            },
            {
                "h2": "Qui rejoint un live, et quand",
                "p": [
                    "Les personnes les plus susceptibles de venir sont des abonnés qui connaissent déjà votre chaîne. Selon leurs paramètres, YouTube peut leur montrer votre live dans leur fil ou leur envoyer une notification.",
                ],
                "ul": [
                    "Programmez le live à l'avance, pour que vos abonnés puissent activer un rappel.",
                    "Choisissez un lieu d'audience où l'heure de votre live tombe en soirée.",
                    "Passez en direct un jour fixe, pour que les spectateurs sachent quand revenir.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Des spectateurs rejoignent un live YouTube programmé depuis leur téléphone, en soirée"},
            },
            {
                "h2": "La rediffusion continue de gagner des vues",
                "p": [
                    "À la fin du live, il reste sur votre chaîne sous forme de vidéo. Les nouveaux abonnés qui l'ont manqué en direct peuvent y trouver la rediffusion et la regarder quand ça leur convient.",
                ],
            },
        ],
        "faqs": [
            ("Pouvez-vous remplir mon live pendant que je suis en direct ?", "Non. De vraies personnes regardent quand elles le choisissent, donc nous ne pouvons promettre personne à une heure donnée. Nous faisons grandir la base d'abonnés dans laquelle vos lives puisent."),
            ("Le lieu choisi compte-t-il pour les lives ?", "Plus que pour les vidéos classiques. Choisissez le lieu où vit votre audience : l'heure de votre live tombera dans sa journée plutôt qu'en pleine nuit."),
            ("La rediffusion recevra-t-elle des vues de la campagne ?", "C'est possible. Une rediffusion est une vidéo de votre chaîne, donc les spectateurs qui vous trouvent après le live peuvent la regarder comme n'importe quelle autre vidéo."),
            ("Ne pourrais-je pas simplement acheter des spectateurs de live pour le compteur ?", "Vous pourriez, mais cela se retourne contre vous. Des spectateurs artificiels sur un live sont du faux engagement comme un autre, et un compteur plein au-dessus d'un chat vide se repère facilement pour de vrais spectateurs."),
            ("Quel pack pour une chaîne qui fait des lives ?", "{pick_name} est notre pack le plus populaire, avec en général {pick_audience} nouveaux abonnés par mois ; une chaîne plus récente peut commencer avec {starter_name}. Chaque live suivant compte plus de personnes susceptibles de venir."),
        ],
    },
    {
        "service": "views",
        "modifier": "monthly",
        "slug": "youtube/vues/mensuelles",
        "label": "Vues YouTube mensuelles",
        "title": "Vues YouTube pour plusieurs vidéos, au mois | Growsterr",
        "description": "Des vues YouTube sur plusieurs vidéos : un pack mensuel amène de vrais spectateurs sur toute votre chaîne, et ils choisissent quoi regarder.",
        "h1": ("Acheter des vues YouTube pour plusieurs vidéos, ", "mois après mois."),
        "intro": "Quand vous achetez des vues YouTube pour plusieurs vidéos, ce que vous voulez vraiment, c'est une chaîne où les gens reviennent. Un pack mensuel est fait pour cela : de vraies personnes découvrent votre chaîne chaque jour et regardent les vidéos qui les intéressent, et la campagne se renouvelle chaque mois, donc vos nouvelles vidéos continuent de rencontrer de nouveaux spectateurs.",
        "hero": {"image": "youtube-viewers", "alt": "Un spectateur passe d'une vidéo YouTube à la suivante sur la même chaîne"},
        "sections": [
            {
                "h2": "Une chaîne, beaucoup de vidéos",
                "p": [
                    "Les spectateurs intéressés ne s'arrêtent pas à une vidéo. Quelqu'un qui vous trouve grâce à un tutoriel ouvre le suivant, puis ce que suggère la page de votre chaîne. Une campagne construite autour de votre chaîne, plutôt que d'un lien unique, suit la façon dont les gens regardent vraiment.",
                ],
            },
            {
                "h2": "Orienter la suite du parcours des nouveaux spectateurs",
                "p": [
                    "Nous faisons la promotion de votre chaîne dans son ensemble ; les spectateurs décident quelles vidéos ouvrir. Ce que vous maîtrisez, c'est le chemin qui s'offre à eux une fois arrivés.",
                ],
                "ul": [
                    "Ajoutez une bande-annonce de chaîne pour les visiteurs qui ne sont pas encore abonnés.",
                    "Mettez votre meilleure vidéo en avant en haut de la page de votre chaîne.",
                    "Regroupez les vidéos liées en playlists, pour que l'une mène à la suivante.",
                    "Ajoutez des écrans de fin qui indiquent la vidéo à regarder après celle-ci.",
                ],
            },
            {
                "h2": "Pourquoi la durée l'emporte sur l'immédiat",
                "p": [
                    "Des vues réparties sur un mois touchent chaque vidéo pendant qu'elle est récente et font vivre les plus anciennes. Une poussée ponctuelle sur plusieurs vidéos fait l'inverse : un pic sur chacune, puis le silence.",
                ],
                "image": {"image": "youtube-channel", "alt": "Un créateur prépare une série de vidéos YouTube à publier au fil du mois"},
            },
        ],
        "faqs": [
            ("Vers combien de vidéos peuvent aller les vues ?", "Il n'y a ni liste ni limite. Nous faisons la promotion de votre chaîne, et les spectateurs regardent ce qui les intéresse, n'importe où dessus."),
            ("Les vidéos publiées en cours de mois reçoivent-elles des vues ?", "Oui. La campagne tourne chaque jour, donc une vidéo publiée en milieu de mois rencontre quand même de nouvelles personnes, et vos nouveaux abonnés peuvent la voir comme tout abonné."),
            ("Le prix est-il par vidéo ?", "Non, il est mensuel, pour toute votre chaîne : {starter_name} coûte {starter_price} par mois, {rising_name} {rising_price} et {pro_name} {pro_price}, quel que soit votre nombre de vidéos. Les vues sont incluses, avec les abonnés, les likes et les commentaires."),
            ("Puis-je arrêter après un mois ?", "Oui. Résiliez dans votre compte ; le mois payé se termine normalement et le suivant n'est pas facturé."),
            ("Les vues peuvent-elles venir d'une seule ville ?", "Oui. Une ville fonctionne, tout comme une région ou un pays entier. Cela convient aux chaînes à audience locale, comme un guide gastronomique d'une ville ou une chaîne d'information locale."),
        ],
    },
    {
        "service": "views",
        "modifier": "no-drop",
        "slug": "youtube/vues/sans-perte",
        "label": "Vues YouTube sans perte",
        "title": "Vraies vues YouTube sans perte : pourquoi ça baisse | Growsterr",
        "description": "Pourquoi le compteur de vues YouTube baisse après un achat, et en quoi les vues de personnes qui ont choisi de regarder sont différentes.",
        "h1": ("De vraies vues YouTube sans perte ? ", "Partez de vues qui n'ont jamais été fausses."),
        "intro": "Quiconque veut acheter de vraies vues YouTube sans perte a généralement déjà vu un compteur chuter. Les vues baissent quand YouTube retire des lectures qu'il juge artificielles. Les nôtres viennent de vraies personnes qui ont choisi de lancer la lecture, dans un pack mensuel : aucun lot de fausses lectures n'attend d'être repris.",
        "hero": {"image": "youtube-channel", "alt": "Dans son studio, un créateur constate que le compteur de vues d'une vidéo YouTube tient bon"},
        "sections": [
            {
                "h2": "Pourquoi les compteurs de vues baissent",
                "p": [
                    "YouTube examine les vues et retire celles qu'il ne considère pas comme authentiques : lectures de bots, de scripts et autre trafic artificiel. Quand cela arrive après un achat, le compteur baisse, parfois longtemps après la livraison, et l'historique de la vidéo montre un pic suivi d'une chute.",
                ],
            },
            {
                "h2": "Ce que nous pouvons promettre, et ce que nous ne pouvons pas",
                "p": [
                    "Nous ne pouvons pas promettre que YouTube n'ajustera jamais un compteur : il contrôle tout le trafic, le nôtre compris. Ce que nous pouvons vous dire, c'est comment nos vues se produisent : une vraie personne voit votre chaîne grâce à une campagne sponsorisée et choisit de regarder. C'est le genre de vue que les contrôles de YouTube sont là pour conserver.",
                ],
            },
            {
                "h2": "Quand vues, likes et abonnés montent ensemble",
                "p": [
                    "Les vraies vues voyagent rarement seules. Dans un pack, elles arrivent avec de nouveaux abonnés, des likes et des commentaires des mêmes personnes : vos chiffres montent ensemble et rien n'y paraît déplacé, ni pour YouTube ni pour un spectateur.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Des amis regardent ensemble une vidéo YouTube et laissent un like à la fin"},
            },
        ],
        "faqs": [
            ("Mes vues baisseront-elles un jour ?", "YouTube peut ajuster le compteur de n'importe quelle vidéo lorsqu'il examine le trafic, donc personne ne peut honnêtement promettre un chiffre qui ne bouge jamais. Les vues de personnes qui ont choisi de regarder sont le genre que son examen est conçu pour garder."),
            ("Allez-vous recharger les vues si le compteur baisse ?", "Non. Une recharge remplace des lectures fausses supprimées par de nouvelles. Nous vendons à la place un pack mensuel de vraies personnes, il n'y a donc rien d'artificiel à remplacer."),
            ("Pourquoi mes vues ont-elles baissé après un achat précédent ?", "Le plus souvent parce que YouTube a retiré des lectures qu'il jugeait artificielles. Cela peut arriver des semaines après la livraison, d'où la surprise."),
            ("Puis-je acheter des vues sans perte pour une seule vidéo ?", "Pas en commande isolée. Les vues viennent dans un pack mensuel qui fait grandir toute votre chaîne, donc chaque vidéo peut en profiter."),
            ("Qu'est-ce qui vient avec les vues ?", "Les spectateurs apportent le reste eux-mêmes. Avec {pick_name}, en général {pick_audience} abonnés, {pick_likes} likes et {pick_comments} commentaires par mois."),
        ],
    },
    {
        "service": "views",
        "modifier": "organic",
        "slug": "youtube/vues/organiques",
        "label": "Vues YouTube organiques et ciblées",
        "title": "Vues YouTube ciblées : choisissez ville ou pays | Growsterr",
        "description": "Des vues YouTube ciblées depuis la ville, la région ou le pays de votre audience : des spectateurs organiques qui ont choisi de regarder.",
        "h1": ("Acheter des vues YouTube ciblées, ", "depuis le lieu où vit votre audience."),
        "intro": "Pour acheter des vues YouTube ciblées, dites-nous où doivent se trouver vos spectateurs : une ville, une région plus large ou un pays entier. Nous y montrons votre chaîne à de vraies personnes grâce à des campagnes sponsorisées, et les vues sont organiques au sens qui compte : chacune vient de quelqu'un qui a choisi de regarder.",
        "hero": {"image": "youtube-channel", "alt": "Un créateur filme une vidéo YouTube dans une rue de sa ville pour une audience locale"},
        "sections": [
            {
                "h2": "Pourquoi le lieu est le ciblage qui compte",
                "p": [
                    "Une chaîne de cuisine à Lisbonne, une chaîne immobilière à Dubaï, une chaîne de jeux vidéo en turc : chacune a une audience qui vit quelque part et parle une langue. Les spectateurs de ce lieu comprennent vos vidéos, reviennent pour la suivante et peuvent devenir clients si vous vendez quelque chose.",
                    "Nous dirigeons d'abord votre campagne vers le lieu choisi. Si l'audience la plus proche de votre chaîne est plus nombreuse juste de l'autre côté d'une frontière, une partie de vos spectateurs peut en venir.",
                ],
            },
            {
                "h2": "Ciblé ne veut pas dire forcé",
                "p": [
                    "Nous ciblons là où sont les gens, puis nous les laissons décider. Personne n'est obligé de regarder votre vidéo, et rien ne se lance sans avoir été choisi. Une vue ciblée reste un choix, et c'est ce qui la rend organique.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Des spectateurs dans un café regardent une vidéo YouTube tournée dans leur propre ville"},
            },
            {
                "h2": "Comment choisir votre lieu",
                "ul": [
                    "Choisissez le lieu pour lequel vos vidéos sont faites, pas le plus grand que vous puissiez nommer.",
                    "Pour un commerce local ou une chaîne de ville, choisissez la ville elle-même.",
                    "Pour une langue plutôt qu'un lieu, choisissez le pays où vivent la plupart de ses locuteurs.",
                    "Pour une niche internationale, commencez par le pays dont vous voulez le plus toucher les spectateurs.",
                ],
            },
        ],
        "faqs": [
            ("Quelle est la précision du ciblage ?", "Elle va jusqu'à la ville. Plus le lieu est petit, plus son audience l'est aussi : dans une petite ville, certains spectateurs peuvent venir de la région alentour."),
            ("Le ciblage rend-il les vues moins organiques ?", "Non : la décision de regarder leur appartient. Nous payons pour montrer votre chaîne dans le lieu choisi ; chaque spectateur décide ensuite seul, et personne n'est récompensé pour regarder."),
            ("Les spectateurs de ma ville vont-ils s'abonner ?", "Certains, si votre chaîne leur parle. Avec {pick_name}, en général {pick_audience} nouveaux abonnés par mois, du lieu choisi et des environs."),
            ("Pourquoi ne pas choisir la zone la plus large possible ?", "Une zone plus grande, c'est un vivier plus grand, mais les spectateurs qui ne partagent ni votre langue ni votre contexte restent rarement. Le bon lieu vaut mieux que le plus grand."),
            ("Avez-vous besoin d'accéder à ma chaîne pour cibler des spectateurs ?", "Non. Le ciblage se fait dans nos campagnes, pas dans les paramètres de votre chaîne. Il nous faut votre identifiant de chaîne et un lieu, jamais votre mot de passe."),
        ],
    },
    {
        "service": "views",
        "modifier": "promote",
        "slug": "youtube/vues/promouvoir",
        "label": "Promouvoir ses vidéos YouTube",
        "title": "Vues YouTube via AdWords ? Notre façon de promouvoir | Growsterr",
        "description": "Vous pensez acheter des vues YouTube via AdWords ? Nous promouvons votre chaîne auprès de vraies personnes, chaque mois, avec abonnés et likes inclus.",
        "h1": ("Acheter des vues YouTube via AdWords ? ", "Ou laissez-nous mener la promotion."),
        "intro": "Ceux qui veulent acheter des vues YouTube via AdWords cherchent à promouvoir une vidéo avec de la visibilité payante. Les publicités Google sont une option : une campagne que vous configurez, gérez et payez vous-même. Nous sommes une autre option : nous promouvons chaque jour votre chaîne auprès de vraies personnes via notre réseau partenaire, et vous suivez les résultats dans votre tableau de bord.",
        "hero": {"image": "youtube-viewers", "alt": "Des gens découvrent une vidéo YouTube sponsorisée sur leur téléphone et leur tablette"},
        "sections": [
            {
                "h2": "Gérer des publicités soi-même, ou une campagne gérée pour vous",
                "p": [
                    "Avec Google Ads, l'outil qui a remplacé AdWords, vous construisez la campagne vous-même : audience, enchères, budget et publicité. Vous payez au fil de la diffusion, et c'est à vous de la surveiller.",
                    "Un pack Growsterr, c'est l'option clé en main. Vous nous donnez l'identifiant de votre chaîne et un lieu cible ; notre équipe mène la promotion chaque jour, et votre tableau de bord montre les visites de la chaîne et les nouveaux abonnés. Un prix mensuel unique, aucune enchère à gérer.",
                ],
            },
            {
                "h2": "Ce à quoi une vue sponsorisée devrait mener",
                "p": [
                    "Une vue payée n'est rentable que si le spectateur fait quelque chose ensuite : regarder une autre vidéo, aimer, s'abonner. C'est pourquoi nos packs sont construits autour des abonnés, avec likes, commentaires et vues des mêmes personnes, plutôt qu'autour d'un nombre de lectures.",
                ],
                "image": {"image": "youtube-channel", "alt": "Un créateur regarde les nouveaux abonnés d'une vidéo YouTube après le début d'une promotion"},
            },
            {
                "h2": "Ce que nous ne faisons pas",
                "ul": [
                    "Nous ne configurons ni ne gérons de campagnes Google Ads, et nous ne demandons jamais d'accès à votre compte Google.",
                    "Nous ne vendons pas de vues par milliers ni à un prix par vue.",
                    "Vous pouvez désigner une vidéo sur laquelle arrivent les nouveaux spectateurs, mais nous ne calons pas la promotion sur l'heure d'un lancement.",
                    "Nous ne promettons ni la monétisation, ni des heures de visionnage, ni une place dans les recommandations.",
                ],
            },
        ],
        "faqs": [
            ("Est-ce la même chose que des publicités YouTube ?", "Non. Les publicités YouTube tournent dans votre propre compte Google Ads, avec votre budget et vos réglages. Nous faisons la promotion de votre chaîne via notre réseau partenaire et menons la campagne pour vous ; rien ne tourne dans votre compte."),
            ("Pouvez-vous gérer mes campagnes Google Ads ?", "Ce n'est pas un service que nous proposons. Notre travail, ce sont des packs de croissance mensuels ; pour tout projet plus large, écrivez-nous sur WhatsApp ou par e-mail."),
            ("En quoi le coût diffère-t-il de la publicité ?", "La publicité facture au fil de la diffusion, donc votre dépense varie avec vos enchères et votre budget. Nos packs ont un prix mensuel fixe, {starter_price}, {rising_price} ou {pro_price}, avec des fourchettes habituelles d'abonnés, de likes et de commentaires."),
            ("Puis-je lancer mes propres publicités en même temps ?", "Oui. Vos publicités tournent dans votre compte et notre campagne dans notre réseau : l'une ne gêne pas l'autre."),
            ("Quelles vidéos promouvez-vous ?", "Votre chaîne dans son ensemble, pas une vidéo isolée, et les spectateurs choisissent quoi regarder. Placer un lancement ou une nouvelle série en vidéo mise en avant sur votre chaîne aide les nouveaux visiteurs à la trouver."),
        ],
    },
    {
        "service": "views",
        "modifier": "real",
        "slug": "youtube/vues/vraies",
        "label": "Vraies vues YouTube",
        "title": "Vues YouTube de qualité : une personne par vue | Growsterr",
        "description": "Des vues YouTube de qualité, de vraies personnes qui ont choisi de regarder, avec abonnés, likes et commentaires des mêmes spectateurs, dans un pack.",
        "h1": ("Acheter des vues YouTube de qualité ? ", "Une personne derrière chaque lecture."),
        "intro": "Avant d'acheter des vues YouTube de qualité, mieux vaut définir la qualité. Pour nous, une vue de qualité a une personne derrière elle : quelqu'un qui a vu votre chaîne, choisi une vidéo et regardé parce que ça l'intéressait. C'est le seul genre que nos packs amènent, et ces mêmes personnes s'abonnent, aiment et commentent aussi.",
        "hero": {"image": "youtube-viewers", "alt": "Un vrai spectateur choisit une vidéo à regarder sur la chaîne YouTube d'un créateur"},
        "sections": [
            {
                "h2": "Ce qui distingue une vraie vue d'une lecture",
                "ul": [
                    "Une personne l'a choisie : personne n'a été payé ni scripté pour lancer la lecture.",
                    "Elle mène quelque part : certains spectateurs aiment, commentent ou s'abonnent.",
                    "Elle a une origine : le spectateur vit là où vous avez dirigé la campagne.",
                    "Elle tient : rien d'artificiel en elle que YouTube aurait à retirer.",
                ],
            },
            {
                "h2": "Pourquoi des vues de bots « haut de gamme » ne sont toujours pas de qualité",
                "p": [
                    "Certains vendeurs classent leurs vues en standard, haute qualité ou premium. Quelle que soit l'étiquette, la question qui compte reste la même : une personne a-t-elle choisi de regarder ? Sinon, une meilleure gamme signifie seulement un prix plus élevé pour la même lecture vide.",
                ],
            },
            {
                "h2": "Une qualité lisible dans YouTube Studio",
                "p": [
                    "Les vraies vues laissent des traces : une durée de visionnage qui varie d'un spectateur à l'autre, des commentaires qui répondent à votre vidéo et des abonnés gagnés sur les vidéos que les gens ont regardées. Ces traces sont ce qui donne de la valeur à une vue, et ce que des lectures générées ne laissent jamais.",
                ],
                "image": {"image": "youtube-channel", "alt": "Un créateur lit la durée de visionnage et les commentaires d'une vidéo YouTube dans ses statistiques"},
            },
        ],
        "faqs": [
            ("En quoi une vue de qualité diffère-t-elle d'une vue bon marché ?", "Une vue bon marché est généralement une lecture sans rien après. Une vue de qualité est une personne qui pourrait aimer, commenter, s'abonner ou revenir, et seul ce genre aide votre chaîne."),
            ("Puis-je voir qui sont les spectateurs ?", "Votre tableau de bord montre les visites de chaîne et les nouveaux abonnés de votre campagne, et YouTube Studio montre où se trouvent les spectateurs et combien de temps ils regardent. Les spectateurs individuels restent anonymes, comme sur toute chaîne."),
            ("Les vues viennent-elles sans abonnés ni likes ?", "Non. Elles viennent dans un seul pack, des mêmes personnes, et c'est ce qui en fait de la croissance plutôt qu'un chiffre."),
            ("Pourquoi pas de lots de mille vues ?", "Parce que mille vues sur commande, ce sont mille lectures que quelqu'un a générées. Nous préférons amener des personnes et les laisser choisir quoi regarder."),
            ("Puis-je choisir où vivent les spectateurs ?", "Oui : indiquez le lieu lors de la commande, d'une seule ville à un pays entier. Des spectateurs locaux comprennent vos vidéos, et c'est ce qui donne à leurs vues plus de valeur qu'un compteur."),
        ],
    },
    {
        "service": "views",
        "modifier": "safe",
        "slug": "youtube/vues/fiables",
        "label": "Vues YouTube sans risque",
        "title": "Acheter des vues YouTube sans risque pour sa chaîne | Growsterr",
        "description": "Acheter des vues YouTube de façon fiable ? Ce que YouTube considère comme faux, ce que risque votre chaîne, et comment nos vrais spectateurs arrivent.",
        "h1": ("Acheter des vues YouTube de façon fiable ? ", "Sachez ce qui met une chaîne en danger."),
        "intro": "Si vous voulez acheter des vues YouTube de façon fiable et sans risque, commencez par ce que YouTube sanctionne : les vues de bots, de scripts et tout trafic qui n'est pas une personne choisissant de regarder. Nous restons du bon côté de cette ligne en faisant uniquement la promotion de votre chaîne auprès de vraies personnes, qui regardent si elles en ont envie.",
        "hero": {"image": "youtube-channel", "alt": "Un créateur fait le point sur la santé de sa chaîne YouTube dans un bureau calme à la maison"},
        "sections": [
            {
                "h2": "Ce que YouTube considère comme de fausses vues",
                "p": [
                    "Les règles de YouTube sur le faux engagement couvrent tous les cas suivants. YouTube peut retirer ces vues, et les contenus qui en dépendent peuvent être supprimés.",
                ],
                "ul": [
                    "Les lectures de bots ou de scripts automatisés.",
                    "Les vues de personnes payées ou récompensées pour regarder.",
                    "Les vidéos lues automatiquement sans que les spectateurs les aient choisies.",
                    "Les vues échangées entre chaînes.",
                ],
            },
            {
                "h2": "Comment arrivent nos vues",
                "p": [
                    "Notre réseau partenaire mène des campagnes sponsorisées qui placent votre chaîne devant de vraies personnes. Personne n'est payé pour regarder, rien ne se lance sans avoir été choisi, et rien ne touche votre compte YouTube. Ceux qui aiment ce qu'ils voient regardent davantage, aiment, commentent et s'abonnent.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Un spectateur choisit sur son téléphone une vidéo YouTube sponsorisée à regarder"},
            },
            {
                "h2": "Sans risque pour votre compte aussi",
                "ul": [
                    "Nous travaillons à partir de l'identifiant public de votre chaîne : aucune connexion, aucune demande d'accès.",
                    "La facturation est un abonnement mensuel Stripe que vous gérez depuis votre compte.",
                    "Y mettre fin ne dépend que de vous, à tout moment, sans question à laquelle répondre.",
                ],
            },
        ],
        "faqs": [
            ("Acheter des vues peut-il faire supprimer ma vidéo ?", "De fausses vues, oui : YouTube peut les retirer du compteur, et un contenu qui enfreint ses règles sur le faux engagement peut être supprimé. Les vues de personnes qui ont choisi de regarder ne sont pas du faux engagement."),
            ("Qui est derrière Growsterr ?", "Sterr Agency, dont la société immatriculée est Sterr Technologies OÜ, à Tallinn, en Estonie. Le siège de l'équipe est en Turquie."),
            ("Avez-vous besoin de mes identifiants YouTube ou Google ?", "Non, et un service qui les demande est un risque en soi. Il nous faut seulement l'identifiant public de votre chaîne."),
            ("Promouvoir une vidéo est-il autorisé sur YouTube ?", "Promouvoir une vidéo pour que les gens la découvrent est banal ; des chaînes le font chaque jour avec la publicité. La limite que fixe YouTube concerne les vues artificielles ou incitées, et nous restons du bon côté."),
            ("Et si je ne suis pas satisfait ?", "Arrêtez l'abonnement dans votre compte et aucun autre mois ne sera facturé. Votre tableau de bord montre ce que nous avons mesuré : vous pouvez juger la campagne sur des faits."),
        ],
    },
    {
        "service": "views",
        "modifier": "shorts",
        "slug": "youtube/vues/shorts",
        "label": "Vues YouTube Shorts",
        "title": "Vues YouTube Shorts : les « reels » de YouTube | Growsterr",
        "description": "Sur YouTube, les reels s'appellent des Shorts. Nous amenons de vrais spectateurs qui regardent vos Shorts, dans un pack mensuel avec abonnés.",
        "h1": ("Acheter des vues de reels YouTube ? ", "Des spectateurs de Shorts qui continuent de regarder."),
        "intro": "Si vous voulez acheter des vues de reels YouTube, vous parlez des Shorts : les vidéos courtes et verticales de YouTube. Nous ne vendons pas de vues de Shorts en gros. Nous amenons chaque jour de vraies personnes sur votre chaîne, et celles qui aiment vos Shorts les regardent, les revoient, les aiment et parfois s'abonnent.",
        "hero": {"image": "youtube-viewers", "alt": "Quelqu'un regarde un YouTube Short sur son téléphone et le laisse tourner en boucle"},
        "sections": [
            {
                "h2": "Des vues de Shorts bon marché, faciles à truquer et faciles à repérer",
                "p": [
                    "Les vues de Shorts bon marché sont partout, parce qu'une lecture se génère en quelques secondes. Le plus dur, c'est ce qui se passe après : le spectateur a-t-il continué à regarder, revu la vidéo, aimé, ouvert votre chaîne ? Les lectures générées répondent non à tout, et YouTube les traite comme du spam.",
                ],
            },
            {
                "h2": "Comment un spectateur de Shorts devient un abonné",
                "p": [
                    "Les Shorts sont une porte d'entrée. Un vrai spectateur qui en aime un peut toucher votre nom, parcourir votre chaîne et s'abonner, et dès lors vos vidéos plus longues peuvent l'atteindre aussi. C'est ce chemin qui fait qu'une vue de Short venant d'une personne vaut bien plus qu'une lecture.",
                ],
                "image": {"image": "youtube-channel", "alt": "Un créateur relit un YouTube Short vertical sur son téléphone avant de le publier"},
            },
            {
                "h2": "Tirer davantage des Shorts que vous publiez",
                "ul": [
                    "Gardez vos meilleurs Shorts faciles à trouver sur la page de votre chaîne, là où arrivent les curieux.",
                    "Liez une vidéo longue en rapport depuis votre Short, pour que les spectateurs intéressés aient où aller.",
                    "Publiez à un rythme régulier, pour que les nouveaux abonnés trouvent du neuf à chaque visite.",
                ],
            },
        ],
        "faqs": [
            ("Les reels YouTube, est-ce la même chose que les Shorts ?", "Oui. Reels est le nom utilisé par Instagram ; sur YouTube, le même format court et vertical s'appelle Shorts. Tout ce qui figure sur cette page s'applique aux Shorts."),
            ("Puis-je acheter des vues bon marché pour un seul Short ?", "Il n'y a pas de prix par Short, et nous ne dirigeons pas de vues vers un Short isolé. Un pack fait la promotion de votre chaîne, et les spectateurs choisissent les Shorts qu'ils veulent."),
            ("Pouvez-vous faire entrer mes Shorts dans le fil des Shorts ?", "C'est une promesse que personne ne peut faire honnêtement, donc nous ne la faisons pas. Nous amenons de vrais spectateurs ; la façon dont YouTube diffuse ensuite un Short relève de sa propre décision."),
            ("Pourquoi n'annoncez-vous pas de nombre de vues de Shorts ?", "Un Short peut être revu, passé ou regardé en boucle, et un nombre de vues promis à l'avance ne peut être atteint qu'en générant des lectures. Nous annonçons des fourchettes mensuelles habituelles pour ce que les gens font après avoir regardé : s'abonner, aimer et commenter."),
            ("Est-ce sans risque d'acheter des vues YouTube Shorts ?", "Auprès d'un service de bots, non : une fausse lecture reste fausse, que la vidéo dure trente secondes ou une heure. De vrais spectateurs qui choisissent vos Shorts forment une audience ordinaire, quel que soit le format que vous publiez."),
        ],
    },
]
