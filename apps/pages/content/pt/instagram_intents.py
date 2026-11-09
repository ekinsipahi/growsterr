UPDATED = "2026-11-09"

# European Portuguese Instagram intent pages: searches for things we don't sell (cheap, instant,
# free, free trial, panels, verified, female, AI or custom comments). Each answers honestly, then
# leads to the monthly package. Keys and placeholders: docs/CONTENT.md; angles: docs/keywords/WRITING.md.

PAGES = [
    # --- Comentários ----------------------------------------------------------------------
    {
        "service": "comments",
        "modifier": "ai",
        "slug": "instagram/comentarios/ia",
        "label": "Comentários de IA no Instagram?",
        "title": "Comentários de IA no Instagram? Nós usamos pessoas | Growsterr",
        "description": "Não vendemos comentários escritos por IA no Instagram. Nos nossos pacotes, cada um é escrito por uma pessoa real: {starter_comments} num mês habitual.",
        "h1": ("Comentários de IA no Instagram? ", "Os nossos são escritos por pessoas."),
        "intro": "Procuras comprar comentários de IA para o Instagram? Não os vendemos. O texto gerado por software tem sempre de ser publicado a partir de uma conta, e uma conta que ninguém usa é um bot, por mais inteligente que seja a frase. Nos nossos pacotes, cada comentário é escrito por uma pessoa real que viu a tua publicação, normalmente {starter_comments} por mês com o {starter_name}.",
        "hero": {"image": "instagram-real-people", "alt": "Pessoas a escrever os seus próprios comentários na publicação de Instagram de um criador"},
        "sections": [
            {
                "h2": "O que é, na verdade, um comentário de IA",
                "p": [
                    "Um software consegue escrever num segundo uma frase sobre a tua roupa ou a tua receita. O que não consegue é ser alguém. Para aparecer na tua publicação, essa frase tem de vir de uma conta, e uma conta que só existe para publicar texto gerado é um perfil falso com um guião melhor.",
                    "O teu público também lê os comentários. Uma série de respostas polidas e um pouco genéricas a chegar todas juntas parece encenada, e enterra a conversa verdadeira debaixo da tua publicação.",
                ],
            },
            {
                "h2": "Porque é que o comentário de uma pessoa vale mais",
                "ul": [
                    "É escrito por alguém que pode voltar para a tua próxima publicação.",
                    "Diz-te o que as pessoas pensam mesmo, por isso sabes do que deves fazer mais.",
                    "Abre uma conversa a que podes responder, e as respostas trazem as pessoas de volta.",
                    "Vem com um novo seguidor e gostos da mesma pessoa, dentro do pacote.",
                ],
            },
            {
                "h2": "Põe antes a IA a trabalhar do teu lado",
                "p": [
                    "Se gostas de ferramentas de IA, usa-as onde ajudam: a pensar em legendas, a esboçar um carrossel, a planear um mês de publicações. Depois deixa as pessoas reais reagir ao que fizeste. Essa divisão mantém a tua conta honesta e a tua secção de comentários viva.",
                ],
            },
        ],
        "faqs": [
            ("Podem pôr comentários gerados por IA nas minhas publicações?", "Não. Não geramos comentários nem publicamos nada a partir de contas que controlamos. Cada comentário de um pacote é escrito por uma pessoa real que decidiu dizer alguma coisa."),
            ("Dão um guião a essas pessoas?", "Não. Escrevem com as suas palavras sobre o que viram. É por isso que alguns comentários são um único emoji e outros te fazem uma pergunta."),
            ("Quantos comentários traz cada pacote?", "Normalmente {starter_comments} por mês com o {starter_name}, {rising_comments} com o {rising_name} e {pro_comments} com o {pro_name}. Intervalos e não contagens, porque são as pessoas que decidem se têm algo a dizer."),
            ("Os comentários vão parecer naturais?", "Vão, porque são. As pessoas reais comentam a horas diferentes, em estilos diferentes, nas publicações de que gostaram mesmo."),
            ("Posso ter comentários sem seguidores?", "Os comentários não se vendem à parte. Quem gosta de uma publicação é quem segue, põe gosto e escreve, por isso os três vêm juntos em todos os pacotes."),
        ],
    },
    {
        "service": "comments",
        "modifier": "custom",
        "slug": "instagram/comentarios/personalizados",
        "label": "Comentários personalizados no Instagram?",
        "title": "Comprar comentários personalizados no Instagram? | Growsterr",
        "description": "Comentários personalizados no Instagram, escritos por ti, são publicados por contas que ninguém usa. Trazemos comentários que pessoas reais escrevem por si.",
        "h1": ("Comentários personalizados no Instagram, ", "ou comentários sentidos?"),
        "intro": "Se queres comprar comentários no Instagram com texto personalizado, as palavras seriam tuas e as contas que as publicam não seriam reais. Não oferecemos isso. A nossa campanha apresenta o teu perfil a pessoas reais, e quem tem algo a dizer escreve-o por si: normalmente {pick_comments} comentários por mês com o {pick_name}.",
        "hero": {"image": "instagram-creator-studio", "alt": "Um criador a escrever uma legenda de Instagram que termina com uma pergunta aos seguidores"},
        "sections": [
            {
                "h2": "Porque não publicamos as tuas palavras",
                "p": [
                    "Um serviço de comentários personalizados pega na tua lista de frases e publica-as debaixo da tua foto a partir de um conjunto de contas. Por muito bem que as escrevas, as contas denunciam-nas: não há ninguém por trás, nunca voltam, e a secção de comentários transforma-se num espetáculo.",
                    "Os seguidores reparam quando os comentários de uma publicação soam à pessoa que a publicou.",
                ],
            },
            {
                "h2": "O que podes influenciar",
                "p": [
                    "Não podes escolher o que as pessoas reais dizem. Podes tornar mais fácil que digam alguma coisa.",
                ],
                "ul": [
                    "Termina a legenda com uma pergunta a que se responda em poucas palavras.",
                    "Responde depressa aos primeiros comentários; uma resposta convida muitas vezes outra.",
                    "Fixa um comentário que lance a conversa que gostavas de ter.",
                    "Escolhe a cidade ou o país de onde devem vir as pessoas que comentam.",
                ],
            },
            {
                "h2": "Comentários que te dizem alguma coisa",
                "p": [
                    "Os comentários reais são feedback. Quando te perguntam onde é o casaco ou que receita experimentar a seguir, ficas a saber o que o teu público quer. Os comentários pré-escritos só conseguem repetir o que já pensas.",
                ],
            },
        ],
        "faqs": [
            ("Posso escrever eu os comentários?", "Não. Nunca publicamos comentários por ti, e não temos contas a partir das quais os publicar. As pessoas reais escrevem os seus, e é o único tipo que trazemos."),
            ("Os comentários podem ser numa língua específica?", "Indiretamente. Escolhe o país ou a cidade de onde vem o teu público, e as pessoas de lá tendem a comentar na língua que falam. As palavras são sempre delas."),
            ("Posso escolher que publicações recebem comentários?", "Não diretamente. Com o {rising_name} ou o {pro_name} escolhes que publicações recebem mais atenção, mas o que as pessoas comentam, e onde, é com elas. As tuas publicações mais fortes costumam juntar mais."),
            ("Vou receber comentários negativos?", "As pessoas reais dizem o que pensam. A maioria comenta porque gostou do que viu, mas não filtramos opiniões, e as ferramentas habituais do Instagram para ocultar ou apagar comentários continuam nas tuas mãos."),
            ("Os comentários vão ficar espalhados pelas minhas publicações?", "Ao longo do mês, sim: o {pick_name} traz normalmente {pick_comments}, escritos ao longo de 30 dias e não de uma vez. As publicações sobre as quais as pessoas têm mais a dizer juntam mais."),
        ],
    },
    {
        "service": "comments",
        "modifier": "fast",
        "slug": "instagram/comentarios/rapidos",
        "label": "Comentários instantâneos no Instagram?",
        "title": "Comentários instantâneos no Instagram? Só de bots | Growsterr",
        "description": "Comentários instantâneos no Instagram vêm de scripts. Os nossos vêm de pessoas reais que encontraram o teu perfil, aos poucos: normalmente {pick_comments} por mês.",
        "h1": ("Comentários instantâneos no Instagram vêm de scripts. ", "Os nossos vêm de pessoas."),
        "intro": "Comentários no Instagram instantâneos só se compram a scripts: nenhuma pessoa real lê uma publicação e responde segundos depois de um pagamento. Não fazemos nada instantâneo. A tua campanha mostra o teu perfil a pessoas reais todos os dias, e os comentários chegam à medida que elas descobrem as tuas publicações, normalmente {pick_comments} por mês com o {pick_name}.",
        "hero": {"image": "instagram-hub", "alt": "Comentários a aparecer em publicações de Instagram, alguns de cada vez, ao longo de um mês"},
        "sections": [
            {
                "h2": "Como é a rapidez com pessoas reais",
                "p": [
                    "A rapidez no Instagram não é a velocidade a que um número salta. É o tempo que as tuas publicações levam a pôr uma conversa a andar. Quem comenta a sério continua a chegar ao longo do mês, por isso uma publicação que lances na terceira semana também encontra pessoas novas.",
                ],
            },
            {
                "h2": "Porque uma parede de comentários num minuto sai pela culatra",
                "p": [
                    "Trinta comentários no mesmo minuto numa publicação com meia dúzia de gostos não parece popular. Parece comprado, aos olhos dos teus seguidores e de qualquer marca que pense trabalhar contigo.",
                    "Depois para. Os comentários pré-escritos chegam numa rajada e nunca mais voltam, por isso a tua publicação seguinte parece parada em comparação.",
                ],
            },
            {
                "h2": "O calendário, com honestidade",
                "ul": [
                    "Depois da encomenda: a tua campanha arranca e as primeiras pessoas chegam ao teu perfil em poucos dias.",
                    "Ao longo do mês: os comentários chegam alguns de cada vez, nas publicações de que as pessoas mais gostam.",
                    "Em cada nova publicação: as pessoas que te seguiram entretanto estão lá para a ver e responder.",
                ],
            },
        ],
        "faqs": [
            ("Quando aparecem os primeiros comentários?", "Normalmente nos primeiros dias da campanha, quando pessoas reais começam a encontrar as tuas publicações. Depois disso chegam alguns de cada vez, não numa rajada."),
            ("Podem mandar comentários para uma publicação no momento em que sai?", "Não. Não prometemos comentários numa publicação nem os acertamos com um momento. A campanha promove o teu perfil, e as pessoas comentam as publicações que escolhem, quando as veem."),
            ("Porque não pôr todos os comentários logo no primeiro dia?", "Porque teriam de vir de contas que não são pessoas. Quem comenta a sério tem os seus horários, e é exatamente por isso que os comentários parecem naturais."),
            ("Os gostos vêm com os comentários?", "Sim. Quem comenta costuma também pôr gosto: o {pick_name} traz normalmente {pick_likes} gostos por mês, além dos novos seguidores."),
            ("Posso parar se o ritmo não for para mim?", "Sim. Cancela na tua conta quando quiseres; não voltas a ser cobrado, e o mês pago continua até ao fim."),
        ],
    },
    {
        "service": "comments",
        "modifier": "female",
        "slug": "instagram/comentarios/de-mulheres",
        "label": "Comentários de mulheres no Instagram?",
        "title": "Comprar comentários de mulheres no Instagram? | Growsterr",
        "description": "Não segmentamos por género, e ninguém pode prometer só comentários de mulheres com pessoas reais. Porquê, e como chegam comentários reais ao teu Instagram.",
        "h1": ("Comentários só de mulheres no Instagram? ", "Ninguém o pode prometer com honestidade."),
        "intro": "Queres comprar comentários de mulheres no Instagram? A resposta direta: não segmentamos por género, e um serviço que promete comentários só de contas femininas não consegue cumprir essa promessa com pessoas reais. Essas ofertas assentam em perfis montados para parecerem de mulheres. Nós escolhemos onde o teu perfil é mostrado; quem comenta depende de quem o vê.",
        "hero": {"image": "instagram-real-people", "alt": "Um grupo variado de pessoas a ler e a comentar uma publicação de Instagram"},
        "sections": [
            {
                "h2": "Porque é que prometer quem comenta exige contas falsas",
                "p": [
                    "Uma pessoa real decide por si se comenta. Por isso, nenhum serviço honesto pode prometer ao mesmo tempo um número de comentários e quem os escreve. Quando uma oferta promete as duas coisas, as contas são do vendedor, e as fotos nelas são escolhidas para bater certo com a encomenda.",
                    "Não oferecemos segmentação por género de todo. Decidimos onde o teu perfil é mostrado, e deixamos às próprias pessoas a decisão de responder.",
                ],
            },
            {
                "h2": "O teu conteúdo decide quem participa",
                "p": [
                    "Se hoje a maior parte do teu público são mulheres, é por causa do que publicas e de a quem isso fala. As pessoas que uma campanha traz funcionam da mesma forma: comentam quando uma publicação lhes diz respeito.",
                ],
                "ul": [
                    "Escolhe a cidade ou o país onde vive o teu público ideal.",
                    "Publica com regularidade sobre o que interessa a esse público.",
                    "Responde aos comentários, para que quem participou se sinta ouvido.",
                ],
            },
        ],
        "faqs": [
            ("Posso escolher comentários femininos ou masculinos?", "Não. Não oferecemos segmentação por género. Escolhes um local, e quem comenta são as pessoas que gostaram da tua publicação."),
            ("Porque é que algumas ofertas prometem comentários de mulheres?", "Porque quem comenta são contas que elas controlam. Um nome e uma foto de perfil arranjam-se facilmente; uma pessoa real que decide escrever, não."),
            ("As mulheres vão comentar as minhas publicações?", "Claro, se as tuas publicações lhes falarem. Os públicos reais são mistos, e quem entra na conversa depende do que publicas e de onde isso é mostrado."),
            ("Então quem vai comentar?", "Quem gostar das tuas publicações. O {pick_name} traz normalmente {pick_comments} comentários por mês de todo o tipo de pessoas que decidiram escrever, com novos seguidores e gostos dessas mesmas pessoas."),
            ("Precisam da minha palavra-passe?", "Não. O teu nome de utilizador do Instagram é tudo o que precisamos, e o teu perfil deve ficar público enquanto a campanha corre."),
        ],
    },
    {
        "service": "comments",
        "modifier": "free",
        "slug": "instagram/comentarios/gratis",
        "label": "Comentários grátis no Instagram?",
        "plan": "starter",
        "tool": "engagement-calculator",
        "title": "Comentários grátis no Instagram? O que resulta mesmo | Growsterr",
        "description": "Não damos comentários grátis no Instagram. O que custam as apps que os dão, uma calculadora de envolvimento gratuita e hábitos que trazem comentários reais.",
        "h1": ("Comentários grátis no Instagram? ", "Eis o que os conquista de verdade."),
        "intro": "Queres ter ou comprar comentários grátis no Instagram? Não os damos, e as apps que os dão cobram-se com a tua palavra-passe, horas em grupos de comentários ou contas que não são pessoas. O que é grátis aqui: a calculadora de envolvimento desta página, que mostra que parte do teu público reage a uma publicação, e hábitos que conquistam comentários reais. Os nossos pacotes trazem comentários de pessoas reais.",
        "hero": {"image": "instagram-creator-studio", "alt": "Um criador a analisar as reações às suas últimas publicações de Instagram"},
        "sections": [
            {
                "h2": "De onde vêm os comentários grátis",
                "ul": [
                    "Apps de comentários que pedem o teu acesso e depois usam a tua conta para comentar publicações de outras pessoas em troca.",
                    "Grupos de interação onde prometes dezenas de comentários por dia para receber uns quantos de volta.",
                    "Amostras grátis de redes de bots, enviadas para que pagues um lote maior.",
                ],
                "p": [
                    "Nenhuma delas traz alguém que se interesse pelas tuas publicações, e entregar o teu acesso põe em risco a conta que estás a fazer crescer.",
                ],
            },
            {
                "h2": "O que é mesmo grátis: a tua taxa de envolvimento",
                "p": [
                    "Usa a calculadora desta página: introduz os teus seguidores e a média de gostos e comentários das tuas últimas publicações. Funciona no teu navegador e não envia nada para lado nenhum.",
                    "Os comentários costumam ser uma pequena parte das tuas reações. É normal: comentar dá mais trabalho do que tocar no ecrã, e é por isso que um comentário é o sinal mais claro de que uma publicação acertou.",
                ],
            },
            {
                "h2": "Hábitos grátis que trazem mais comentários",
                "ul": [
                    "Faz uma pergunta concreta na legenda em vez de uma vaga.",
                    "Responde aos comentários pouco depois de publicares; as respostas trazem as pessoas de volta.",
                    "Publica quando os teus seguidores estão online; as estatísticas da tua conta mostram quando.",
                    "Partilha a publicação nas tuas histórias e encaminha as pessoas para a conversa.",
                ],
            },
        ],
        "faqs": [
            ("Oferecem comentários grátis no Instagram?", "Não. Cada comentário que trazemos vem de uma pessoa real que a nossa campanha alcançou, e esse trabalho custa dinheiro. O que é grátis nesta página é a calculadora e os conselhos."),
            ("É seguro ter comentários grátis através de uma app?", "A maioria dessas apps pede o teu acesso ao Instagram, e é essa a parte a evitar. Quem tem a tua palavra-passe pode publicar, seguir e comentar como se fosse tu. Nós nunca a pedimos."),
            ("Posso comprar só comentários por menos?", "Os comentários nunca se vendem à parte. Vêm dentro de cada pacote, com seguidores e gostos das mesmas pessoas: normalmente {starter_comments} comentários por mês com o {starter_name}."),
            ("O que é uma boa taxa de envolvimento?", "Depende do teu nicho e da tua dimensão, por isso compara-te contigo próprio. Calcula a tua taxa hoje e outra vez daqui a um mês: uma taxa a subir quer dizer que mais gente do teu público se interessa."),
            ("Posso cancelar se não for para mim?", "Sim, a qualquer momento na tua conta. Não é cobrado mais nada, e ficas com o mês que pagaste."),
        ],
    },
    {
        "service": "comments",
        "modifier": "verified",
        "slug": "instagram/comentarios/verificados",
        "label": "Comentários de contas verificadas?",
        "title": "Comentários de contas verificadas no Instagram? | Growsterr",
        "description": "Ninguém consegue pôr contas verificadas ou celebridades a comentar as tuas publicações a pedido. Trazemos comentários de pessoas reais que viram a publicação.",
        "h1": ("Comentários de contas verificadas ou celebridades? ", "Ninguém os pode vender."),
        "intro": "Querer comprar comentários no Instagram de contas verificadas ou de celebridades faz sentido: um visto azul na tua publicação parece uma aprovação. Não os vendemos, e nenhum serviço de crescimento consegue pôr uma conta verificada ou uma pessoa conhecida a comentar por encomenda. As ofertas que o prometem usam perfis de imitação ou scripts. Os nossos comentários vêm de pessoas reais que viram a tua publicação.",
        "hero": {"image": "instagram-real-people", "alt": "Utilizadores comuns do Instagram a deixar comentários na foto de um criador"},
        "sections": [
            {
                "h2": "Como teria de funcionar um comentário verificado",
                "p": [
                    "As contas verificadas pertencem a pessoas e marcas que decidem por si o que comentam. Um vendedor não lhes pode fazer uma encomenda. Por isso, quando uma tabela de preços inclui comentários de perfis verificados ou de celebridades, está a oferecer contas disfarçadas para parecerem oficiais.",
                    "Os perfis de imitação são denunciados e removidos, e um comentário de um deles pode tornar a tua publicação menos credível, não mais.",
                ],
            },
            {
                "h2": "Os comentários que ajudam mesmo uma publicação",
                "p": [
                    "Um comentário ajuda quando vem de alguém que pode voltar: uma pessoa que gostou da publicação, o diz com as suas palavras e pode tornar-se presença habitual. É isso que os nossos pacotes trazem: com o {pick_name}, um mês habitual tem {pick_comments} comentários assim, com novos seguidores e gostos.",
                ],
            },
            {
                "h2": "Se queres que contas maiores reparem em ti",
                "p": [
                    "O reconhecimento de contas maiores conquista-se em público. Identifica as marcas que usas de verdade, convida criadores do teu nicho para publicações em colaboração e deixa comentários pensados no trabalho deles. É mais lento do que um formulário de encomenda, e é real.",
                ],
            },
        ],
        "faqs": [
            ("Conseguem pôr celebridades a comentar as minhas publicações?", "Não. Nós não conseguimos, nem ninguém que o venda como pacote. As pessoas conhecidas escolhem por si onde comentam."),
            ("Quem comenta são contas verificadas?", "Não escolhemos pessoas pelo selo. Quem comenta são utilizadores reais do Instagram que encontraram a tua publicação; se algum tem visto azul não é algo que escolhamos ou prometamos."),
            ("Comentários reais ajudam-me a ser verificado?", "A verificação é tratada pelo Instagram, com o seu próprio processo, e não temos qualquer papel nela. A interação real torna a tua conta um sítio mais vivo e credível, decida o Instagram o que decidir."),
            ("Que tipo de comentários vou receber?", "Comentários de utilizadores comuns do Instagram, com as suas palavras. Meses habituais: {starter_comments} com o {starter_name}, {pro_comments} com o {pro_name}, e o {rising_name} entre os dois."),
            ("A minha conta está segura convosco?", "Sim. Nunca iniciamos sessão nem pedimos a tua palavra-passe. Só precisamos do teu nome de utilizador, e os comentários vêm de pessoas que agem por iniciativa própria."),
        ],
    },
    # --- Seguidores -----------------------------------------------------------------------
    {
        "service": "followers",
        "modifier": "cheap",
        "slug": "instagram/seguidores/baratos",
        "label": "Seguidores baratos no Instagram?",
        "plan": "starter",
        "title": "Comprar seguidores baratos no Instagram: o custo real | Growsterr",
        "description": "Seguidores baratos no Instagram a 1 € por mil são bots. O {starter_name} custa {starter_price} por mês e traz normalmente {starter_audience} seguidores reais.",
        "h1": ("Seguidores baratos no Instagram? ", "Faz as contas por pessoa real."),
        "intro": "Antes de comprares seguidores baratos no Instagram, compara o que cada seguidor custa e o que faz. Um euro por mil compra bots que desaparecem e puxam o teu alcance para baixo. O {starter_name} custa {starter_price} por mês e traz normalmente {starter_audience} novos seguidores, pessoas reais que decidiram seguir-te, com gostos e comentários incluídos. São cêntimos por pessoa real.",
        "hero": {"image": "instagram-followers", "alt": "Um número de seguidores no Instagram a crescer com pessoas reais vindas de um pacote mensal"},
        "sections": [
            {
                "h2": "O que o preço mais baixo compra realmente",
                "p": [
                    "Ao preço mais baixo, um seguidor é uma conta criada em massa, sem publicações e, quando muito, com uma foto emprestada. Custa quase nada porque não há ninguém por trás.",
                    "Essas contas nunca põem gosto nem comentam. Vão-se embora quando o Instagram limpa perfis falsos, e enquanto ficam, cada publicação chega a uma parte menor das pessoas que se interessam.",
                ],
            },
            {
                "h2": "As contas dos seguidores reais",
                "p": [
                    "Divide {starter_price} pelos {starter_audience} seguidores que o {starter_name} traz normalmente num mês, e cada pessoa real custa uns cêntimos. Depois soma o que vem com elas: normalmente {starter_likes} gostos e {starter_comments} comentários dessas mesmas pessoas, sem custo extra.",
                ],
            },
            {
                "h2": "Preço baixo, nada escondido",
                "ul": [
                    "Um preço mensal cobre seguidores, gostos e comentários.",
                    "Pagamento com cartão através da Stripe, com Apple Pay ou Google Pay quando o teu dispositivo os aceita.",
                    "Cancela quando quiseres e fica com o resto do mês que pagaste.",
                    "Começa com o {starter_name}, o nosso preço mais baixo, e sobe só se quiseres mais.",
                ],
            },
        ],
        "faqs": [
            ("Quanto custam seguidores reais no Instagram?", "O nosso preço mais baixo é {starter_price} por mês pelo {starter_name}, que traz normalmente {starter_audience} novos seguidores. O {rising_name} custa {rising_price} e o {pro_name} {pro_price}, com intervalos maiores."),
            ("Porque não comprar seguidores no Instagram por 1 € ou 1 dólar?", "Porque a esse preço ninguém é real. Um euro ou um dólar por mil só paga contas criadas por software, e são as primeiras a ir numa limpeza."),
            ("Posso ter seguidores baratos e rápidos?", "Barato e instantâneo ao mesmo tempo quer sempre dizer bots. Os seguidores reais chegam alguns por dia quando a tua campanha estiver a correr."),
            ("Há alguma coisa mais barata do que o {starter_name}?", "Não. O {starter_name}, a {starter_price} por mês, é o nosso pacote mais pequeno. Não vendemos pacotinhos avulsos: uma campanha real precisa de um mês para chegar às pessoas, e os pacotes baratíssimos são onde vivem os bots."),
            ("Pago à parte pelos gostos e comentários?", "Não. Vêm dentro do pacote, das pessoas que te seguem: normalmente {starter_likes} gostos e {starter_comments} comentários por mês com o {starter_name}."),
        ],
    },
    {
        "service": "followers",
        "modifier": "fast",
        "slug": "instagram/seguidores/rapidos",
        "label": "Seguidores rápidos no Instagram?",
        "title": "Comprar seguidores Instagram rápido, de pessoas reais | Growsterr",
        "description": "Seguidores no Instagram rápidos e reais: a campanha arranca nos primeiros dias e os novos seguidores chegam diariamente. Nunca instantâneos: instantâneo é bot.",
        "h1": ("Seguidores rápidos no Instagram, ", "à velocidade a que as pessoas reais se mexem."),
        "intro": "Queres comprar seguidores no Instagram rápido? A campanha pode arrancar depressa, mas os seguidores reais não podem ser instantâneos: ninguém decide seguir uma conta segundos depois de pagares. Connosco, pessoas reais começam a chegar nos primeiros dias e continuam a chegar diariamente, normalmente {pick_audience} por mês com o {pick_name}. A rapidez que conta é crescer de semana para semana.",
        "hero": {"image": "instagram-followers-1000", "alt": "Uma linha de seguidores no Instagram a subir um pouco mais todos os dias"},
        "sections": [
            {
                "h2": "Arranque rápido, subida constante",
                "p": [
                    "Depois da encomenda, configuramos a tua campanha e o teu perfil começa a ser mostrado a pessoas reais. As primeiras visitas e os primeiros seguidores aparecem normalmente no teu painel em poucos dias, e a linha continua a subir a partir daí.",
                ],
            },
            {
                "h2": "Porque as ofertas mais rápidas são as que deves evitar",
                "p": [
                    "Milhares de seguidores numa hora são um sinal de alarme, não uma vantagem. Para andar tão depressa, um vendedor precisa de contas que fazem o que lhes mandam, e o Instagram remove-as em vagas.",
                    "Um salto desses também parece estranho a quem visita: um número de seguidores que duplicou de um dia para o outro, por cima de publicações com os poucos gostos da semana passada.",
                ],
            },
            {
                "h2": "Formas de acelerar o crescimento real",
                "ul": [
                    "Escolhe um pacote maior: o {pro_name} traz normalmente {pro_audience} seguidores por mês.",
                    "Continua a publicar enquanto a campanha corre, para que quem visita encontre algo novo.",
                    "Deixa a biografia clara e o perfil público; um visitante decide em segundos.",
                    "Escolhe um local onde o teu conteúdo encaixe, para que mais visitantes se tornem seguidores.",
                ],
            },
        ],
        "faqs": [
            ("Em quanto tempo vejo novos seguidores?", "Nos primeiros dias da campanha, quando pessoas reais começam a visitar o teu perfil. O teu painel mostra as visitas e os novos seguidores de cada dia, tal como os medimos."),
            ("Conseguem entregar seguidores numa hora?", "Não, e ninguém consegue com pessoas reais. Tudo o que chega assim tão depressa vem de contas que não são pessoas, e elas tendem a desaparecer outra vez."),
            ("Que pacote faz crescer mais depressa?", "O {pro_name}: normalmente {pro_audience} novos seguidores por mês, contra {rising_audience} com o {rising_name} e {starter_audience} com o {starter_name}."),
            ("O crescimento rápido vai parecer suspeito?", "Não ao nosso ritmo. As pessoas seguem algumas de cada vez, todos os dias, como acontece com qualquer conta que está a crescer."),
            ("Posso subir de pacote mais tarde para crescer mais depressa?", "Sim. Quando quiseres mais pessoas a ver o teu perfil, podes mudar para um pacote maior."),
        ],
    },
    {
        "service": "followers",
        "modifier": "free",
        "slug": "instagram/seguidores/gratis",
        "label": "Seguidores grátis no Instagram?",
        "plan": "starter",
        "tool": "growth-calculator",
        "title": "Seguidores grátis no Instagram? O que recebes mesmo | Growsterr",
        "description": "Seguidores grátis no Instagram, 30 ou 50 de cada vez ou sem login, são bots ou trocas de seguir por seguir. Não os damos. Usa antes a calculadora gratuita.",
        "h1": ("30 ou 50 seguidores grátis no Instagram? ", "Eis o que são na verdade."),
        "intro": "Os sites que te dão 30 seguidores grátis no Instagram, ou 50 sem login, estão a distribuir amostras de redes de bots ou trocas de seguir por seguir. Não oferecemos seguidores grátis. O que é grátis nesta página é a calculadora de crescimento: introduz os teus seguidores de hoje e o teu objetivo, e vê quanto tempo o crescimento real costuma levar com cada pacote.",
        "hero": {"image": "instagram-followers", "alt": "Um criador a planear quantos seguidores reais quer atingir no Instagram"},
        "sections": [
            {
                "h2": "Quanto te custa um seguidor grátis",
                "ul": [
                    "Uma amostra de 30 ou 50 contas de uma rede de bots, enviada para que pagues mais.",
                    "Apps de seguir por seguir: segues desconhecidos, eles seguem-te de volta e vão-se embora quando paras.",
                    "Apps que querem a tua palavra-passe e usam a tua conta para seguir outras pessoas.",
                ],
                "p": [
                    "Quanto a 100 mil seguidores grátis, isso não existe em lado nenhum. A essa escala até os bots custam dinheiro, por isso, seja o que for que está a ser oferecido, não são seguidores.",
                ],
            },
            {
                "h2": "Sem login: o instinto certo",
                "p": [
                    "Querer seguidores sem login quer dizer que já sabes que não deves entregar a tua palavra-passe. Continua assim. Nós também nunca a pedimos: o teu nome de utilizador é tudo o que precisamos para mostrar o teu perfil a pessoas reais.",
                ],
            },
            {
                "h2": "Planeia o crescimento real com a calculadora",
                "p": [
                    "A calculadora de crescimento desta página é grátis e funciona no teu navegador. Introduz os teus seguidores de hoje e o número que queres atingir, e ela mostra quantos meses cada pacote costuma levar a chegar lá. Assim decides com números reais à frente.",
                ],
            },
        ],
        "faqs": [
            ("Oferecem seguidores grátis no Instagram?", "Não. Cada seguidor que trazemos é uma pessoa real alcançada por uma campanha paga, por isso não há nada grátis para distribuir. A calculadora desta página não custa nada, por muitas vezes que a uses."),
            ("É seguro ter seguidores sem login?", "Guardar a tua palavra-passe é sempre mais seguro. Os seguidores oferecidos são outra conversa: sem login, os serviços grátis costumam mandar contas de bots ou pedir-te que sigas desconhecidos."),
            ("Posso ter 100 mil seguidores no Instagram grátis?", "Ninguém te pode dar tantos seguidores reais a troco de nada. O crescimento real até aos 100 mil leva meses; a calculadora mostra mais ou menos quantos com cada pacote."),
            ("Qual é a forma mais barata de começar?", "O {starter_name}, a {starter_price} por mês, traz normalmente {starter_audience} seguidores reais. Cancelas quando quiseres; o mês que pagaste continua até ao fim."),
            ("Seguidores grátis podem prejudicar a minha conta?", "Podem. Contas que nunca interagem baixam a parte dos teus seguidores que reage às tuas publicações, e tendem a desaparecer quando o Instagram remove perfis falsos."),
        ],
    },
    {
        "service": "followers",
        "modifier": "free-trial",
        "slug": "instagram/seguidores/teste-gratis",
        "label": "Teste grátis de seguidores no Instagram?",
        "plan": "starter",
        "title": "Teste grátis de seguidores no Instagram? O que temos | Growsterr",
        "description": "Não oferecemos um teste grátis de seguidores no Instagram. O teu primeiro mês é o teste: pessoas reais, um painel com o que medimos, e cancelas quando quiseres.",
        "h1": ("Sem teste grátis de seguidores no Instagram. ", "O teu primeiro mês é o teste."),
        "intro": "Queres comprar seguidores no Instagram com um teste grátis primeiro? Não temos, e um teste de 50 seguidores numa hora só provaria que o vendedor tem bots. O teu primeiro mês é o teste a sério: o {starter_name} custa {starter_price}, pessoas reais começam a chegar nos primeiros dias, o teu painel mostra o que medimos, e podes cancelar quando quiseres.",
        "hero": {"image": "instagram-hub", "alt": "Um perfil de Instagram no primeiro mês de crescimento com seguidores reais"},
        "sections": [
            {
                "h2": "Porque não fazemos testes",
                "p": [
                    "Cada dia de campanha significa mostrar o teu perfil a pessoas reais através de campanhas promovidas na nossa rede de parceiros, e isso custa o mesmo no primeiro dia e no trigésimo. Não há forma barata de fazer uma versão curta com pessoas reais.",
                    "De qualquer forma, um teste pequeno não te diria muito. O crescimento real é um ritmo ao longo de um mês, não um número na primeira tarde.",
                ],
            },
            {
                "h2": "Como nos avaliar no primeiro mês",
                "ul": [
                    "Acompanha o painel: visitas ao perfil e novos seguidores, dia a dia.",
                    "Vê quem te segue: perfis reais, com publicações e vidas próprias.",
                    "Repara nos teus gostos e comentários, que vêm dessas mesmas pessoas.",
                    "Não ficaste convencido? Cancela na tua conta antes da renovação seguinte.",
                ],
            },
        ],
        "faqs": [
            ("Há um teste grátis?", "Não. Não fazemos testes nem oferecemos seguidores. O mais parecido é um mês do {starter_name}: cancela antes da renovação e não voltas a pagar."),
            ("E se não ficar satisfeito depois do primeiro mês?", "Cancela na tua conta, e não há renovação. As pessoas reais que te seguiram nesse mês não desaparecem quando cancelas."),
            ("Há um compromisso mínimo?", "Um mês. Não há contrato além disso: cada mês só se renova se deixares o pacote ativo."),
            ("Em quanto tempo posso avaliar os resultados?", "Nas primeiras semanas. O painel mostra visitas e novos seguidores todos os dias, por isso vês o ritmo a ganhar forma muito antes do fim do mês."),
            ("Porque é que outros sites oferecem um teste?", "Um teste de umas dezenas de seguidores sai barato quando os seguidores são bots. Com pessoas reais, cada seguidor vem de uma campanha paga, por isso não sai."),
        ],
    },
    {
        "service": "followers",
        "modifier": "smm-panel",
        "slug": "instagram/seguidores/painel-smm",
        "label": "Seguidores no Instagram de painéis SMM?",
        "title": "Seguidores no Instagram de um painel SMM barato? | Growsterr",
        "description": "Painéis SMM, servidores de Discord e vendedores no Telegram revendem bots em massa. A Growsterr é uma agência: pessoas reais, uma equipa e dados medidos.",
        "h1": ("Os painéis SMM vendem números. ", "Somos uma agência que traz pessoas."),
        "intro": "Se estás prestes a comprar seguidores no Instagram num painel SMM barato, num servidor de Discord ou num canal de Telegram, sabe o que está à venda: os painéis SMM revendem tráfego de bots em massa, ao preço por mil, sem ninguém responsável. A Growsterr é uma agência de crescimento. Uma equipa gere a tua campanha, pessoas reais decidem seguir-te e vês os resultados medidos no teu painel.",
        "hero": {"image": "instagram-creator-studio", "alt": "Um criador a rever uma campanha de crescimento no Instagram gerida por uma equipa real"},
        "sections": [
            {
                "h2": "Como funciona um painel SMM",
                "p": [
                    "Um painel SMM é uma tabela de preços. Seguidores, gostos e visualizações para o Instagram aparecem lado a lado, vendidos ao milhar e muitas vezes revendidos de um painel para o seguinte. Colas um link, pagas com um saldo e vês um contador mexer.",
                    "Num painel SMM, ninguém olha para o teu perfil nem para o teu público. É assim que se mantém barato, e é por isso que o que chega é tráfego de bots.",
                ],
            },
            {
                "h2": "Discord, Telegram e vendedores em marketplaces",
                "p": [
                    "Os seguidores e gostos vendidos em servidores de Discord, canais de Telegram ou anúncios em marketplaces vêm normalmente dos mesmos painéis grossistas, com um revendedor pelo meio. Pagas adiantado, muitas vezes a um nome anónimo, sem conta, sem registo e sem ninguém a quem perguntar quando os números caem.",
                ],
            },
            {
                "h2": "O que uma agência faz de diferente",
                "ul": [
                    "Uma equipa configura e acompanha a tua campanha.",
                    "Pessoas reais veem o teu perfil e escolhem se te seguem.",
                    "Os gostos e os comentários vêm dessas mesmas pessoas, dentro do pacote.",
                    "O teu painel mostra as visitas ao perfil que medimos e os seguidores que trouxeram.",
                    "Geres a tua subscrição mensal na tua própria conta.",
                ],
            },
        ],
        "faqs": [
            ("Os seguidores de painéis SMM são reais?", "Os seguidores de painel são tráfego de bots vendido em massa. Algumas contas têm fotos e nomes, mas nenhuma decidiu seguir-te, e não interagem."),
            ("Vendem gostos no Instagram num painel?", "Não. Não temos um painel SMM, e aqui os gostos nunca se vendem à parte. Vêm dentro de cada pacote, das pessoas reais que te seguem: o {pick_name} traz normalmente {pick_likes} por mês."),
            ("Posso revender os vossos pacotes no meu painel?", "Não oferecemos acesso para painéis ou revenda. Cada pacote é uma campanha para uma conta. Se geres várias contas de clientes, escreve-nos e falamos sobre isso."),
            ("Porque são tão baratos os vendedores de Discord e Telegram?", "Passam tráfego de bots em massa com uma margem por cima. Não há campanha por trás nem ninguém a chegar a pessoas reais."),
            ("Como encomendo convosco?", "Escolhe um pacote, dá-nos o teu nome de utilizador do Instagram e o local de onde deve vir o teu público, e paga com cartão. A tua palavra-passe nunca entra na conversa."),
        ],
    },
    {
        "service": "followers",
        "modifier": "verified",
        "slug": "instagram/seguidores/verificados",
        "label": "Seguidores verificados no Instagram?",
        "title": "Comprar seguidores verificados no Instagram? | Growsterr",
        "description": "Ninguém pode vender seguidores verificados no Instagram, nem a própria verificação. Trazemos pessoas reais que decidiram seguir-te, com gostos e comentários.",
        "h1": ("Seguidores verificados no Instagram? ", "Ninguém os pode vender com honestidade."),
        "intro": "Se esperavas comprar seguidores no Instagram que sejam verificados, ou seguidores que te deem o selo de verificação, a resposta às duas é não. As contas verificadas seguem quem escolhem, e nenhum serviço lhes pode dar ordens. A verificação é tratada pelo próprio Instagram e não se vende. O que trazemos são pessoas reais que decidiram seguir-te, normalmente {pick_audience} por mês com o {pick_name}.",
        "hero": {"image": "instagram-followers-1000", "alt": "Utilizadores comuns do Instagram a seguir o perfil de um criador"},
        "sections": [
            {
                "h2": "Seguidores com visto azul",
                "p": [
                    "Uma conta verificada pertence a uma figura pública, criador ou marca que confirmou a sua identidade junto do Instagram. Essas pessoas seguem as contas que acham interessantes, como toda a gente. Um vendedor não as pode pôr a seguir-te, por isso \"seguidores verificados\" numa tabela de preços quer dizer perfis feitos para parecer importantes.",
                ],
            },
            {
                "h2": "Seguidores para ser verificado",
                "p": [
                    "Um número maior não dá, por si só, um visto azul, e um salto repentino de seguidores falsos tem mais probabilidade de levantar dúvidas do que de ajudar. A verificação passa pelo processo do próprio Instagram, nunca por um serviço de crescimento.",
                    "O que torna qualquer conta credível é o contrário de um salto: um público real, a crescer de forma constante e ativo nas tuas publicações.",
                ],
            },
            {
                "h2": "O que podemos fazer",
                "ul": [
                    "Mostrar o teu perfil a pessoas novas todos os dias, no local que escolheres.",
                    "Trazer seguidores que te escolheram, com os seus gostos e comentários.",
                    "Mostrar-te no painel exatamente o que medimos.",
                ],
            },
        ],
        "faqs": [
            ("Conseguem pôr contas verificadas a seguir-me?", "Não. Os utilizadores verificados decidem quem seguem, e nenhum pacote muda isso. Entre as pessoas reais que trazemos, o visto azul não é escolhido nem prometido."),
            ("Comprar seguidores vai dar-me a verificação?", "Não. Um número de seguidores, sozinho, não dá a verificação, e não oferecemos verificação de forma nenhuma."),
            ("Os vossos seguidores são contas reais?", "Sim. Cada um é uma pessoa com uma conta própria, que deu com o teu perfil e decidiu seguir-te."),
            ("As celebridades seguem de volta através dos vossos pacotes?", "Não. As nossas campanhas chegam a utilizadores comuns do Instagram. Quem promete seguidores famosos está a usar contas de imitação."),
            ("Quantos seguidores traz um mês?", "De {starter_audience} com o {starter_name} a {pro_audience} com o {pro_name}, como intervalos mensais habituais. Cada um deles é uma pessoa que decidiu seguir-te."),
        ],
    },
    # --- Gostos ---------------------------------------------------------------------------
    {
        "service": "likes",
        "modifier": "cheap",
        "slug": "instagram/gostos/baratos",
        "label": "Gostos baratos no Instagram?",
        "plan": "starter",
        "title": "Gostos baratos no Instagram? Compara o que recebes | Growsterr",
        "description": "Gostos baratos no Instagram caem numa publicação e acabam ali. Os nossos vêm num pacote mensal, de seguidores reais: normalmente {starter_likes} gostos por mês.",
        "h1": ("Gostos baratos no Instagram ", "custam mais do que parece."),
        "intro": "Antes de comprares gostos baratos no Instagram, vê o que é um pacote de 1 €: toques de contas que nunca vão ver a tua próxima publicação. Os gostos não são algo que vendamos à parte. Vêm em cada pacote, de pessoas reais que te seguem: normalmente {starter_likes} gostos por mês com o {starter_name}, por {starter_price}, com novos seguidores e comentários.",
        "hero": {"image": "instagram-hub", "alt": "Gostos de seguidores reais espalhados pela grelha de Instagram de um criador"},
        "sections": [
            {
                "h2": "Uma publicação contra todas as publicações",
                "p": [
                    "Um pacote barato de gostos cai numa publicação e fica por ali. A publicação seguinte começa do zero, por isso terias de continuar a comprar só para manter as aparências.",
                    "Os gostos de pessoas que te seguem funcionam ao contrário. Veem as tuas novas publicações e põem gosto nas de que gostam, por isso tudo o que publicas este mês recebe a sua parte.",
                ],
            },
            {
                "h2": "Onde um orçamento pequeno rende mais",
                "p": [
                    "Se o preço é o que mais importa, põe o dinheiro onde ele continua a trabalhar: seguidores reais que continuam a pôr gosto. O {starter_name} é o nosso preço mais baixo, e um único pagamento mensal cobre os seguidores, os gostos e os comentários.",
                ],
            },
            {
                "h2": "Gostos que não parecem comprados",
                "p": [
                    "Centenas de gostos numa publicação com três comentários e nenhum seguidor novo parecem comprados a quem estiver atento, marcas incluídas. Quando os gostos, os seguidores e os comentários vêm das mesmas pessoas, os números fazem sentido juntos.",
                ],
            },
        ],
        "faqs": [
            ("Quanto custam os gostos no Instagram convosco?", "Os gostos não têm preço à parte. O {starter_name} custa {starter_price} por mês e traz normalmente {starter_likes} gostos, com {starter_audience} novos seguidores e {starter_comments} comentários das mesmas pessoas."),
            ("Posso comprar poucos gostos para uma publicação?", "Não. Não vendemos gostos para publicações soltas. A campanha promove o teu perfil, e as pessoas que alcança escolhem em que publicações põem gosto, por isso tudo o que partilhas tem a sua oportunidade."),
            ("Porque são tão baratos os gostos a 1 €?", "Porque não há ninguém por trás. São produzidos em massa por software, e podem desaparecer quando o Instagram limpa a atividade falsa."),
            ("Qual é o pacote mais barato?", "O {starter_name}, a {starter_price} por mês. É o preço mais baixo que temos, e podes cancelar quando quiseres."),
            ("Os gostos reais ajudam o meu alcance?", "Os gostos reais vêm de pessoas que olham mesmo para as tuas publicações, e esse tipo de atenção ajuda uma publicação a ir longe de uma forma que um contador comprado nunca consegue."),
        ],
    },
    {
        "service": "likes",
        "modifier": "fast",
        "slug": "instagram/gostos/rapidos",
        "label": "Gostos rápidos no Instagram?",
        "title": "Gostos rápidos no Instagram? Começa pelos seguidores | Growsterr",
        "description": "Gostos instantâneos no Instagram são gostos de bots. Os rápidos vêm de seguidores reais que veem as tuas publicações logo que saem. Criamos esse público.",
        "h1": ("Gostos rápidos no Instagram ", "de quem viu mesmo a publicação."),
        "intro": "Queres comprar gostos no Instagram rápidos, até instantâneos? Gostos instantâneos são gostos de bots: ninguém toca no coração de uma publicação que ainda não viu. O que faz os gostos chegarem depressa é um público de pessoas reais que veem as tuas publicações pouco depois de as publicares. Os nossos pacotes constroem esse público, gostos incluídos, normalmente {pick_likes} por mês com o {pick_name}.",
        "hero": {"image": "instagram-real-people", "alt": "Seguidores a pôr gosto numa nova publicação de Instagram pouco depois de ter saído"},
        "sections": [
            {
                "h2": "A forma real de ter gostos rápidos",
                "p": [
                    "As primeiras horas depois de publicares são quando os teus seguidores veem a publicação. Quantos mais seguidores reais tiveres, mais gostos chegam cedo, e um arranque cedo ajuda uma publicação a ir mais longe.",
                    "É essa a rapidez que vale a pena pagar: não uma publicação escorada uma vez, mas cada nova publicação a arrancar mais depressa do que a anterior.",
                ],
            },
            {
                "h2": "Porque os gostos instantâneos vêm e vão",
                "p": [
                    "Os gostos que aparecem segundos depois de um pagamento vêm de contas que funcionam com horário marcado, não por curiosidade. Chegam todos de uma vez, não acrescentam nada aos comentários nem aos seguidores, e podem desaparecer com a mesma rapidez.",
                ],
            },
            {
                "h2": "O que podes esperar de nós",
                "ul": [
                    "A tua campanha arranca nos primeiros dias depois da encomenda.",
                    "Os gostos chegam ao longo do mês, nas publicações de que as pessoas mais gostam.",
                    "Cada novo seguidor é alguém que também pode pôr gosto nas tuas próximas publicações.",
                ],
            },
        ],
        "faqs": [
            ("A que velocidade começam a chegar os gostos?", "Pouco depois de a campanha arrancar, nos primeiros dias. Continuam a chegar ao longo do mês, à medida que mais pessoas encontram o teu perfil."),
            ("Podem mandar gostos no momento em que publico?", "Não a pedido. As pessoas reais põem gosto nas publicações quando as veem, e à medida que o teu público cresce, mais delas veem cada nova publicação pouco depois de sair."),
            ("Os gostos instantâneos prejudicam a minha conta?", "Podem fazer os teus números parecer estranhos: uma rajada de gostos sem comentários nem novos seguidores. E não fazem nada pelas publicações seguintes."),
            ("É possível ter gostos rápidos de pessoas reais?", "Sim, dos teus próprios seguidores. É por isso que fazemos crescer primeiro o teu público: pôr gosto é o que os seguidores reais fazem."),
            ("Quantos gostos vêm com um pacote?", "O {pick_name} traz normalmente {pick_likes} gostos por mês, das mesmas pessoas que te seguem e comentam."),
        ],
    },
    {
        "service": "likes",
        "modifier": "female",
        "slug": "instagram/gostos/de-mulheres",
        "label": "Gostos de mulheres no Instagram?",
        "title": "Gostos femininos no Instagram? Porque não os vendemos | Growsterr",
        "description": "Não vendemos gostos femininos no Instagram nem segmentamos por género. Os pacotes de gostos de mulheres usam perfis falsos. Os reais vêm de pessoas.",
        "h1": ("Gostos femininos no Instagram? ", "Os gostos reais não vêm separados por género."),
        "intro": "Procuras comprar gostos no Instagram de contas femininas? Não segmentamos por género, e não podemos prometer quem toca no coração: cada pessoa decide por si. Os pacotes de gostos femininos são preenchidos com contas montadas para parecerem de mulheres. O que oferecemos são gostos de pessoas reais no local que escolheres, dentro de um pacote mensal com seguidores e comentários.",
        "hero": {"image": "instagram-real-people", "alt": "Pessoas de todo o tipo a pôr gosto na foto de Instagram de um criador"},
        "sections": [
            {
                "h2": "Porque é que os gostos femininos são fabricados, não encontrados",
                "p": [
                    "Uma pessoa real põe gosto no que lhe agrada, seja quem for. Para cumprir uma encomenda de gostos só de mulheres, um vendedor precisa de contas que põem gosto por encomenda e de fotos à medida da encomenda. Isso é um perfil falso, tenha o aspeto que tiver.",
                ],
            },
            {
                "h2": "O que as marcas analisam de facto",
                "p": [
                    "Se queres mostrar a uma marca que o teu público inclui muitas mulheres, ela vai pedir as estatísticas da tua conta, não percorrer os nomes debaixo de uma publicação. Os perfis falsos só baralham esse retrato. Pessoas reais, alcançadas no sítio certo com conteúdo que lhes fala, é que o tornam fiel.",
                ],
            },
            {
                "h2": "Molda o teu público com conteúdo e local",
                "ul": [
                    "Indica a cidade ou o país onde vivem as pessoas que queres alcançar.",
                    "Publica com regularidade sobre o que lhes interessa.",
                    "Repara nas publicações com mais gostos e faz mais como essas.",
                ],
            },
        ],
        "faqs": [
            ("Posso ter gostos só de mulheres?", "Não. Não oferecemos segmentação por género, nem para gostos nem para mais nada. Pessoas de todo o tipo veem as tuas publicações, e quem gosta delas põe-lhes gosto."),
            ("E posso antes escolher gostos masculinos?", "Não, aplica-se o mesmo. A única segmentação que oferecemos é por local: uma cidade, uma região ou um país."),
            ("Como chego a mais mulheres no Instagram?", "Através do que publicas. O conteúdo que fala às pessoas que queres tende a atraí-las, e o local certo ajuda a tua campanha a chegar até elas."),
            ("Os gostos estão incluídos em todos os pacotes?", "Sim. Todos os pacotes os incluem: com o {pick_name}, um mês habitual traz {pick_likes}, de pessoas que também te seguem e comentam."),
            ("Os gostos femininos ajudam a fechar parcerias com marcas?", "Dificilmente. As marcas olham para quem te segue e interage de verdade, e gostos de perfis inventados não resistem a essa análise."),
        ],
    },
    {
        "service": "likes",
        "modifier": "free",
        "slug": "instagram/gostos/gratis",
        "label": "Gostos grátis no Instagram?",
        "plan": "starter",
        "tool": "engagement-calculator",
        "title": "Gostos grátis no Instagram? O que vale o teu tempo | Growsterr",
        "description": "Gostos grátis no Instagram, de 10 a 100 a cada 24 horas, vêm de bots ou de apps de gosto por gosto. Usa a calculadora gratuita e conquista gostos reais.",
        "h1": ("Gostos grátis no Instagram ", "custam sempre alguma coisa. Isto não."),
        "intro": "Queres ter gostos grátis no Instagram, 10, 50 ou 100 de cada vez, a cada 24 horas? Essas ofertas funcionam com contas de bots ou apps de gosto por gosto que te levam o acesso ou o tempo. Não damos gostos. O que é grátis aqui é a calculadora de envolvimento desta página e formas honestas de ter mais gostos. Os nossos pacotes trazem gostos de pessoas reais: compras um mês de crescimento, não um monte de gostos.",
        "hero": {"image": "instagram-creator-studio", "alt": "Um criador a calcular a taxa de envolvimento das publicações recentes no Instagram"},
        "sections": [
            {
                "h2": "Como funcionam as apps de gostos grátis",
                "ul": [
                    "Doses diárias de 10 a 100 gostos de contas de bots, para te venderem um pacote maior.",
                    "Apps de gosto por gosto onde percorres publicações de desconhecidos para ganhar créditos.",
                    "Ferramentas que querem o teu acesso ao Instagram e usam a tua conta para pôr gosto noutras publicações.",
                    "Gostos grátis nos teus comentários, do mesmo tipo de contas de bots.",
                ],
                "p": [
                    "Todas custam alguma coisa: a tua palavra-passe, as tuas horas, ou um público inchado com contas que nunca voltam.",
                ],
            },
            {
                "h2": "Mede primeiro com a calculadora de envolvimento",
                "p": [
                    "A calculadora desta página é grátis, e nada do que introduzes sai do teu navegador. Preenche o teu número de seguidores e depois o que uma publicação recente típica recebe em gostos e comentários, para veres que parte do teu público reage. Volta a calcular daqui a umas semanas para ver se o que estás a experimentar está a resultar.",
                ],
            },
            {
                "h2": "Formas grátis de conquistar mais gostos numa publicação",
                "ul": [
                    "Abre com a tua imagem mais forte ou com o primeiro segundo do vídeo; as pessoas decidem depressa.",
                    "Publica Reels: o Instagram mostra-os a pessoas que ainda não te seguem.",
                    "Mantém um ritmo regular para que os seguidores esperem as tuas publicações.",
                    "Escreve legendas que deem às pessoas uma razão para parar, guardar ou partilhar.",
                ],
            },
        ],
        "faqs": [
            ("Posso ter gostos grátis a cada 24 horas?", "Não connosco, nem de pessoas reais em lado nenhum. Os gostos grátis diários são uma amostra de contas de bots, pensada para te levar a um pacote pago."),
            ("Como tenho gostos numa publicação sem pagar?", "O caminho lento resulta: publica algo que as pessoas queiram ver, quando os teus seguidores estão online, e partilha-o nas tuas histórias. Não custa nada, e resulta melhor à medida que o teu público real cresce."),
            ("E os gostos grátis nos meus comentários?", "Os gostos em comentários das apps grátis vêm das mesmas contas de bots. Os reais chegam quando as pessoas leem a conversa de uma publicação e concordam com alguma coisa."),
            ("Têm um plano grátis?", "Não. Os pacotes pagos começam no {starter_name}, a {starter_price} por mês, que traz normalmente {starter_likes} gostos de pessoas reais, mais seguidores e comentários. Cancelas quando quiseres."),
            ("A calculadora é mesmo grátis?", "Sim. Usa-a as vezes que quiseres. Faz as contas no teu navegador e não nos envia nada."),
        ],
    },
    {
        "service": "likes",
        "modifier": "verified",
        "slug": "instagram/gostos/verificados",
        "label": "Gostos de contas verificadas no Instagram?",
        "title": "Gostos de contas verificadas no Instagram? A resposta | Growsterr",
        "description": "Ninguém pode vender gostos de contas verificadas no Instagram. Trazemos gostos de pessoas reais que viram a tua publicação, num pacote mensal com seguidores.",
        "h1": ("Gostos de contas verificadas no Instagram ", "não são coisa que se venda."),
        "intro": "Se queres comprar gostos verificados no Instagram, ou seja, gostos de contas com visto azul, a resposta honesta é esta: não os podemos vender, nem ninguém que trabalhe com pessoas reais. Os utilizadores verificados põem gosto no que escolhem. Os nossos pacotes trazem gostos de utilizadores reais do Instagram que viram a tua publicação, dentro de um pacote que também traz seguidores e comentários.",
        "hero": {"image": "instagram-hub", "alt": "Gostos de utilizadores comuns do Instagram na publicação mais recente de um criador"},
        "sections": [
            {
                "h2": "O que acrescentaria um gosto verificado",
                "p": [
                    "Muito pouco que alguém veja. Um gosto conta o mesmo seja quem for que o dê, e um visto azul só aparece se alguém abrir a lista de gostos. O valor que as pessoas imaginam é reconhecimento, e o reconhecimento de uma conta de imitação não vale a pena.",
                ],
            },
            {
                "h2": "Porque é que estas ofertas existem",
                "p": [
                    "Os vendedores sabem que um visto azul tem peso, por isso disfarçam contas para parecerem oficiais, às vezes com um selo desenhado na própria foto de perfil. Um selo verdadeiro não pode ser acrescentado a uma conta a partir de fora, e isso diz-te o que está realmente à venda.",
                ],
            },
            {
                "h2": "Gostos que continuam a chegar",
                "p": [
                    "Os gostos reais vêm de pessoas que te seguem e veem o que publicas a seguir. Com o {pick_name}, isso dá normalmente {pick_likes} gostos por mês nas tuas publicações, das mesmas pessoas que te seguem e comentam.",
                ],
            },
        ],
        "faqs": [
            ("Algum dos vossos gostos vem de contas verificadas?", "Não escolhemos pessoas pelo selo, e nunca prometemos gostos verificados. As pessoas a quem chegamos são utilizadores comuns do Instagram que viram a tua publicação e gostaram."),
            ("Gostos verificados ajudam-me a ser verificado?", "Não. O Instagram decide a verificação com o seu próprio processo, e nenhum vendedor de gostos tem influência nisso."),
            ("Vale a pena pagar por um gosto de uma celebridade?", "Só um verdadeiro significaria alguma coisa, e os verdadeiros não se compram. Um gosto de uma conta de imitação é só mais um gosto de bot com um nome emprestado."),
            ("Como tenho mais gostos no Instagram?", "Faz crescer o número de pessoas reais que veem as tuas publicações e querem ver mais. É isso que os nossos pacotes fazem, com gostos, seguidores e comentários a vir das mesmas pessoas."),
            ("Precisam de acesso à minha conta?", "Não. O teu nome de utilizador chega, e nunca pedimos a tua palavra-passe."),
        ],
    },
]
