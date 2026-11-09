"""European Portuguese Instagram pages: comments, likes, and the ways people ask for followers and
likes (gradual, organic, local, private accounts...). Keys and placeholders: docs/CONTENT.md. Numbers
come from the packages ({starter_likes}...), so they follow apps/growth/plan.py."""

UPDATED = "2026-11-09"

PAGES = [
    # --- Comentários ----------------------------------------------------------------------
    {
        "service": "comments",
        "slug": "instagram/comentarios",
        "label": "Comentários no Instagram",
        "title": "Comprar comentários no Instagram de pessoas reais | Growsterr",
        "description": "Queres comprar comentários no Instagram? Os nossos vêm em cada pacote mensal, escritos por pessoas reais. Normalmente {starter_comments} por mês.",
        "h1": ("Comprar comentários no Instagram ", "de quem tem mesmo algo a dizer."),
        "intro": "Se vieste comprar comentários no Instagram, fica a saber que só os trazemos de uma forma: dentro de um pacote mensal, de pessoas reais que descobrem as tuas publicações e têm algo a dizer. Normalmente {starter_comments} comentários por mês com o {starter_name}, {pick_comments} com o {pick_name}.",
        "hero": {"image": "instagram-real-people", "alt": "Pessoas a deixar os seus próprios comentários, perguntas e emojis numa publicação de Instagram"},
        "sections": [
            {
                "h2": "Como é uma secção de comentários verdadeira",
                "p": [
                    "Os comentários reais são irregulares. Uma pessoa pergunta onde é o casaco, outra identifica um amigo, outra escreve duas palavras e um emoji. É essa irregularidade que torna uma secção de comentários credível, e é exatamente o que os comentários pré-escritos não conseguem imitar.",
                    "Os comentários comprados em massa costumam chegar como frases quase iguais, de contas sem publicações próprias. Qualquer pessoa que faça scroll os deteta, incluindo as marcas e os parceiros que gostarias de impressionar.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "Um criador à secretária a responder a comentários numa publicação de Instagram"},
            },
            {
                "h2": "Quantos comentários traz cada pacote",
                "ul": [
                    "{starter_name}, a {starter_price} por mês, traz normalmente {starter_comments} comentários, nas publicações de que as pessoas mais gostam.",
                    "{rising_name}, a {rising_price}, traz normalmente {rising_comments}, e és tu que escolhes as publicações que recebem a atenção.",
                    "{pro_name}, a {pro_price}, traz normalmente {pro_comments}, com destaque prioritário e uma linha direta por WhatsApp.",
                ],
            },
            {
                "h2": "Porque é que os comentários só vêm com um pacote",
                "p": [
                    "Uma publicação com quarenta comentários e uma dúzia de gostos diz a toda a gente o que aconteceu. Os comentários só parecem certos ao lado dos seguidores, gostos e visualizações que a atenção real traz, por isso trazemos a atenção e deixamos que os comentários nasçam dela.",
                ],
            },
        ],
        "faqs": [
            ("Posso ter comentários no Instagram sem um pacote?", "Não. Os comentários só vêm dentro dos nossos pacotes mensais, de pessoas que encontraram o teu perfil através das nossas campanhas. Ninguém os escreve por encomenda, e é por isso que soam a conversa."),
            ("Posso escolher o que dizem os comentários?", "Não. As pessoas escrevem com as suas palavras, por isso não há nada para escrevermos por elas, e comentários feitos por encomenda raramente parecem a reação verdadeira de alguém. O que podes escolher, com o {rising_name} ou o {pro_name}, é para onde vai a atenção: as publicações que indicares."),
            ("Quando aparecem os comentários?", "Ao longo do mês, alguns de cada vez, à medida que as pessoas descobrem as tuas publicações. Cem comentários em dez minutos seriam um guião, não um público."),
            ("Os comentários ajudam as minhas publicações a chegar a mais pessoas?", "Os comentários mostram que as pessoas se interessam por uma publicação, e o Instagram repara nisso. Os reais somam. Não podemos prometer alcance, e ninguém honesto pode, mas os comentários pré-escritos só acrescentam ruído."),
            ("Precisam da minha palavra-passe?", "Não. Precisamos do teu nome de utilizador do Instagram e do local de onde deve vir o teu público. Mantém a conta pública para que as pessoas possam ler as tuas publicações e participar."),
        ],
    },
    # --- Seguidores: as formas como as pessoas os procuram -------------------------------------
    {
        "service": "followers",
        "modifier": "gradual",
        "slug": "instagram/seguidores/entrega-gradual",
        "label": "Seguidores no Instagram com entrega gradual",
        "title": "Comprar seguidores Instagram com entrega gradual | Growsterr",
        "description": "Compra seguidores no Instagram que chegam todos os dias, não de uma vez: pessoas reais encontram o teu perfil durante 30 dias, num crescimento gradual.",
        "h1": ("Seguidores no Instagram todos os dias, ", "ao ritmo a que as pessoas seguem."),
        "intro": "Se preferes comprar seguidores no Instagram que cheguem dia a dia em vez de tudo de uma vez, já estás a pensar como um público. As nossas campanhas mostram o teu perfil a pessoas reais todos os dias durante 30 dias, por isso os seguidores chegam aos poucos: normalmente {pick_audience} ao longo do mês com o {pick_name}.",
        "hero": {"image": "instagram-followers-1000", "alt": "Um número de seguidores a subir um pouco todos os dias ao longo de um mês"},
        "sections": [
            {
                "h2": "Conta-gotas é uma definição. Crescer todos os dias é uma campanha.",
                "p": [
                    "Há serviços que vendem entrega a conta-gotas: um lote de contas libertado aos poucos para que a curva pareça natural. As contas continuam a ser bots; só o ritmo vem disfarçado.",
                    "O nosso ritmo não é definição nenhuma. O teu perfil é mostrado a pessoas todos os dias, e cada novo seguidor chega quando alguém decide seguir-te. A curva gradual é simplesmente o aspeto que a escolha das pessoas tem, vista de fora.",
                ],
            },
            {
                "h2": "Porque devagar é melhor do que tudo de uma vez",
                "ul": [
                    "Uma subida constante parece o que é: uma conta que as pessoas continuam a descobrir.",
                    "Os novos seguidores de cada dia encontram a tua próxima publicação com o interesse ainda fresco.",
                    "Não há nenhum pico repentino que uma marca, ou um seguidor, possa pôr em causa.",
                    "Percebes o que está a resultar, porque cada dia é um dado à parte.",
                ],
            },
            {
                "h2": "Como ler os teus números diários",
                "p": [
                    "O teu painel mostra, para cada dia, quantas pessoas visitaram o teu perfil através da campanha e quantas te seguiram. Há dias mais movimentados do que outros: uma publicação forte, um fim de semana, um feriado. Ao longo do mês, esses dias somam um intervalo habitual, não uma quota diária fixa.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "Um criador a consultar um gráfico diário de visitas ao perfil e novos seguidores"},
            },
        ],
        "faqs": [
            ("Quantos seguidores vou ter por dia?", "Não há um número diário fixo, porque as pessoas decidem por si. Ao longo do mês, o {pick_name} traz normalmente {pick_audience}, por isso um dia médio traz uma parte disso, uns dias mais, outros menos."),
            ("Posso escolher eu a velocidade de entrega?", "Não, nem precisas. A velocidade vem das pessoas, não de um botão: a campanha corre todos os dias e os seguidores chegam sempre que alguém decide."),
            ("O crescimento gradual é menos arriscado do que um lote grande?", "Centenas de seguidores numa hora é um padrão que os bots deixam. O crescimento gradual com pessoas reais não deixa esse padrão, porque não é um. Não podemos falar pela forma como o Instagram trata cada conta; só podemos assegurar que cada seguidor que trazemos é uma pessoa."),
            ("Gradual significa crescer menos?", "Não. Gradual descreve a forma, não o total. O intervalo habitual do mês é o mesmo quer alguém te siga ao segundo dia quer ao vigésimo nono; simplesmente chega da forma como um público se constrói."),
            ("Os gostos e os comentários também chegam aos poucos?", "Sim. As mesmas pessoas põem gosto e comentam à medida que encontram as tuas publicações, por isso ambos crescem a par dos teus seguidores. Com o {pick_name}, isso dá normalmente {pick_likes} gostos e {pick_comments} comentários ao longo do mês."),
        ],
    },
    {
        "service": "followers",
        "modifier": "live",
        "slug": "instagram/seguidores/em-direto",
        "label": "Seguidores no Instagram: entrega e diretos",
        "title": "Entrega rápida de seguidores no Instagram, explicada | Growsterr",
        "description": "Com que rapidez chegam seguidores do Instagram que são pessoas reais? A campanha arranca depressa, cresce todos os dias e prepara público para os teus diretos.",
        "h1": ("Comprar seguidores no Instagram com entrega rápida? ", "Eis o que rápido quer dizer."),
        "intro": "Comprar seguidores no Instagram com entrega rápida costuma querer dizer uma de duas coisas: um contador que dispara em minutos, ou uma campanha que arranca logo e não para. Nós só fazemos a segunda. A tua campanha arranca depressa, pessoas reais chegam desde os primeiros dias, e o teu painel mostra o que cada dia trouxe.",
        "hero": {"image": "instagram-creator-studio", "alt": "Um criador a preparar-se à secretária para entrar em direto no Instagram"},
        "sections": [
            {
                "h2": "Rápido onde conta, nunca instantâneo",
                "p": [
                    "A parte rápida é o arranque. Configuramos a tua campanha pouco depois da encomenda, e as pessoas começam a ver o teu perfil desde os primeiros dias. O que não fazemos é meter um mês de decisões reais numa hora, porque a única forma de o fazer é com contas que ninguém usa.",
                    "Por isso, quando comparares prazos de entrega, olha para quando começa o crescimento real e se ele continua, não para a rapidez com que um número salta.",
                ],
            },
            {
                "h2": "Seguidores para os teus diretos no Instagram",
                "p": [
                    "Os seguidores para diretos são simplesmente seguidores que aparecem quando entras em direto. O Instagram pode avisar os teus seguidores quando uma transmissão começa, por isso mais pessoas que decidiram seguir-te significa mais pessoas que podem entrar.",
                    "Não vendemos espectadores para diretos, e ninguém pode prometer uma plateia a uma hora marcada: as pessoas entram quando têm interesse e estão por perto. Os seguidores que ganhas ao longo do mês são os que têm mais probabilidade de o fazer.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Seguidores a entrar no direto de Instagram de um criador e a comentar durante a transmissão"},
            },
            {
                "h2": "Entrega gradual também para os gostos",
                "p": [
                    "Os gostos seguem o mesmo ritmo. Vêm das pessoas que descobrem o teu perfil, por isso vão caindo nas tuas publicações ao longo do mês, normalmente {pick_likes} com o {pick_name}. Não há uma encomenda de gostos à parte para agendar nem um pico para explicar.",
                ],
            },
        ],
        "faqs": [
            ("Quando começa a entrega?", "Depressa. Assim que a encomenda entra, configuramos a campanha e as pessoas começam a visitar o teu perfil desde os primeiros dias. Os novos seguidores começam com essas visitas e continuam o mês inteiro."),
            ("Posso ter entrega instantânea?", "Não. A entrega instantânea só funciona com bots, porque nenhuma pessoa segue alguém segundos depois de um pagamento. Em vez disso, arrancamos depressa e crescemos todos os dias."),
            ("Vou ter novos seguidores antes do meu direto desta noite?", "Talvez alguns, se a tua campanha já estiver a correr, mas não conseguimos fazer as pessoas chegar à hora de uma transmissão. Se um direto é importante para ti, começa umas semanas antes, para que os novos seguidores tenham tempo de te conhecer."),
            ("Vendem espectadores para diretos no Instagram?", "Não. Os espectadores de um direto teriam de ser pessoas a ver num minuto concreto, e ninguém pode entregar isso de forma honesta. Os seguidores que trazemos podem entrar nos teus diretos por iniciativa própria."),
            ("Onde posso acompanhar a entrega?", "No teu painel, que conta as visitas ao perfil trazidas pela nossa campanha e os seguidores que vieram delas, dia a dia. O total da tua conta também mexe com o resto do teu crescimento e com quem deixa de te seguir."),
        ],
    },
    {
        "service": "followers",
        "modifier": "no-drop",
        "slug": "instagram/seguidores/sem-quedas",
        "label": "Seguidores no Instagram que ficam",
        "title": "Seguidores permanentes no Instagram: os reais ficam | Growsterr",
        "description": "Queres comprar seguidores permanentes no Instagram? As contas falsas somem nas limpezas. As pessoas reais ficam, porque seguir-te foi ideia delas.",
        "h1": ("Seguidores permanentes no Instagram ", "começam com pessoas reais."),
        "intro": "Quem procura comprar seguidores permanentes no Instagram já viu o outro tipo: um salto, depois uma fuga lenta de volta ao ponto de partida. Os seguidores caem quando nunca foram pessoas. Os nossos são pessoas que decidiram seguir-te, por isso ficam como fica qualquer público real, e quando alguém sai, é pelas razões por que qualquer seguidor sai.",
        "hero": {"image": "instagram-followers", "alt": "Um número de seguidores no Instagram estável e a subir ao longo de vários meses"},
        "sections": [
            {
                "h2": "Porque caem os seguidores comprados",
                "p": [
                    "O Instagram remove regularmente contas falsas e de spam. Quando os teus seguidores são essas contas, cada limpeza leva um pedaço do teu número. As reposições voltam a encher o contador com mais do mesmo, e o ciclo recomeça.",
                    "Uma pessoa não é removida numa limpeza. Só sai se decidir deixar de te seguir, o que acontece muito menos vezes e é algo em que as tuas publicações podem pesar.",
                ],
            },
            {
                "h2": "O que faz os seguidores ficar",
                "ul": [
                    "Escolheram-te, e quem começa a seguir por interesse tende a ficar.",
                    "Vêm de onde vive o teu público, por isso as tuas publicações fazem sentido para eles.",
                    "Veem as tuas próximas publicações, e cada uma boa é mais uma razão para ficar.",
                    "O teu ritmo conta mais do que qualquer coisa que façamos: as pessoas ficam pelas publicações que esperam com vontade.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Seguidores de longa data ainda a pôr gosto e a comentar a publicação mais recente de um criador"},
            },
            {
                "h2": "Sem quedas, definido com honestidade",
                "p": [
                    "Não te vamos dizer que ninguém vai deixar de te seguir, porque as pessoas não funcionam assim. Podemos dizer-te que não vais ver as vagas de perdas que as contas falsas causam, e o teu painel mostra os novos seguidores que a nossa campanha trouxe, dia a dia, para saberes sempre o que veio de nós.",
                ],
            },
        ],
        "faqs": [
            ("Os vossos seguidores são permanentes?", "São pessoas reais, por isso ficam enquanto quiserem. Ninguém pode prometer que uma pessoa nunca deixará de te seguir; o que podemos dizer é que nenhuma delas é uma conta falsa à espera de ser apagada."),
            ("Fazem reposição se os seguidores caírem?", "Não, porque não há nada para repor. As reposições existem para seguidores que desaparecem nas limpezas. Os nossos são pessoas, e um ou outro que deixa de seguir faz parte de qualquer público real."),
            ("Porque desaparecem os seguidores comprados?", "Normalmente nem deixam de seguir: as contas é que são removidas. O Instagram apaga perfis falsos e de spam em vagas, e o número de seguidores cai com eles."),
            ("O que acontece aos meus seguidores se cancelar?", "Ficam. Seguiram-te porque quiseram, não porque uma subscrição os obrigou. Cancelar só significa que deixamos de trazer pessoas novas quando o mês pago terminar; as que já ganhaste continuam a seguir-te."),
            ("Como mantenho os seguidores que ganho?", "Publica com regularidade, responde aos comentários e dá aos novos seguidores uma razão para voltar nas primeiras semanas. As pessoas ficam pelas mesmas razões por que te seguiram."),
        ],
    },
    {
        "service": "followers",
        "modifier": "organic",
        "slug": "instagram/seguidores/organicos",
        "label": "Seguidores orgânicos no Instagram",
        "title": "Seguidores orgânicos no Instagram: pagas o alcance | Growsterr",
        "description": "Dá para comprar seguidores orgânicos no Instagram? Podes pagar para seres visto por pessoas reais, no local que escolheres. Seguir-te é decisão delas.",
        "h1": ("Comprar seguidores orgânicos no Instagram? ", "Paga o alcance, deixa as pessoas escolher."),
        "intro": "Em rigor, ninguém pode comprar seguidores orgânicos no Instagram: um seguidor é orgânico porque uma pessoa o decidiu. O que podes comprar é alcance. Todos os dias, pessoas reais no local que escolheres dão com o teu perfil através das nossas campanhas, e cada seguidor que daí vem é uma decisão que alguém tomou por si.",
        "hero": {"image": "instagram-real-people", "alt": "Pessoas a dar com o perfil de Instagram de um criador e a decidir segui-lo"},
        "sections": [
            {
                "h2": "Onde acaba o pago e começa o orgânico",
                "p": [
                    "As nossas campanhas são promovidas: pagamos para pôr o teu perfil à frente de pessoas na nossa rede de parceiros. Essa parte é paga, e dizemo-lo. Tudo o que vem depois não é. Ninguém é convidado a seguir-te, e ninguém te segue de volta como parte de uma troca.",
                    "É o mesmo acordo de um anúncio ou de uma menção na página de outra pessoa: pagas a apresentação, e o público decide.",
                ],
            },
            {
                "h2": "Seguidores orgânicos, dirigidos ao teu público",
                "p": [
                    "O crescimento orgânico resulta melhor quando quem te vê tem boas probabilidades de se interessar. Indica a cidade, a região ou o país onde vive o teu público, e é aí que mostramos primeiro o teu perfil. Uma pastelaria em Braga e um criador de viagens com leitores por toda a Europa precisam de pessoas diferentes, e apontamos em conformidade.",
                ],
            },
            {
                "h2": "O que o orgânico deixa de fora",
                "ul": [
                    "Trocas de seguir por seguir e grupos de interação.",
                    "Bots e perfis falsos, por mais devagar que sejam libertados.",
                    "Acessos de qualquer tipo: a tua palavra-passe fica contigo.",
                    "Picos de seguidores mais rápidos do que qualquer público real conseguiria.",
                ],
            },
        ],
        "faqs": [
            ("As campanhas pagas são mesmo orgânicas?", "O alcance é pago; o seguimento não. Cada novo seguidor viu o teu perfil e decidiu por si, e é isso que torna um seguidor orgânico."),
            ("Vou ter seguidores reais no Instagram todos os dias?", "Sim. A campanha corre todos os dias do mês e as pessoas seguem-te à medida que te descobrem. Há dias que trazem mais do que outros; ao longo do mês, somam normalmente {pick_audience} com o {pick_name}."),
            ("É o mesmo que fazer eu próprio anúncios no Instagram?", "Parecido no espírito, diferente na prática. Nós corremos as campanhas na nossa rede de parceiros, a nossa equipa acompanha-as e tu vês visitas medidas e novos seguidores num painel. Não precisas de uma conta de anúncios nem de um orçamento para gerir."),
            ("O crescimento orgânico ajuda as minhas publicações a chegar a mais pessoas?", "Mais do que números comprados alguma vez poderiam, porque os seguidores orgânicos veem mesmo e reagem ao que publicas. Até onde chega cada publicação continua a depender da publicação."),
            ("O crescimento orgânico é mais lento?", "É mais constante. Um mês de crescimento orgânico chega dia a dia em vez de numa hora, e não vem seguido da queda que os picos de bots trazem."),
        ],
    },
    {
        "service": "followers",
        "modifier": "private-account",
        "slug": "instagram/seguidores/conta-privada",
        "label": "Seguidores no Instagram para conta privada",
        "title": "Seguidores no Instagram com conta privada | Growsterr",
        "description": "Dá para comprar seguidores no Instagram com a conta privada? Aí as pessoas só podem pedir para seguir, por isso pedimos um perfil público durante a campanha.",
        "h1": ("Seguidores numa conta privada do Instagram? ", "Passa a público enquanto cresces."),
        "intro": "Se queres comprar ou ganhar seguidores no Instagram com a conta privada, eis o senão, com toda a honestidade: ninguém consegue seguir uma conta privada, só pode pedir para seguir. Por isso pedimos-te que mantenhas o perfil público enquanto a campanha corre. Continuas a decidir o que lá está, e nunca precisamos da tua palavra-passe.",
        "hero": {"image": "instagram-followers", "alt": "Um perfil privado de Instagram com cadeado ao lado do mesmo perfil já público"},
        "sections": [
            {
                "h2": "O que uma conta privada faz a uma campanha",
                "p": [
                    "Quem encontra um perfil privado vê um nome, uma biografia e um cadeado. Pode pedir para seguir, mas não vê uma única publicação, por isso a maioria segue em frente. Os poucos que pedem ficam à espera de que os aproves, um a um.",
                    "Uma campanha que manda pessoas para essa porta fechada desperdiça a maior parte do alcance. Num perfil público, as mesmas pessoas podem percorrer as tuas publicações, decidir e seguir-te de imediato.",
                ],
            },
            {
                "h2": "Se um serviço diz que contas privadas não são problema",
                "p": [
                    "Numa conta privada, o número de seguidores só sobe quando os pedidos são aprovados. Se alguém promete seguidores aí sem que aproves ninguém, teria de ser essa pessoa a aprovar, de dentro da tua conta. Entregar a tua palavra-passe para isso é a única coisa que nunca deves fazer.",
                ],
            },
            {
                "h2": "Ficar público sem perder o controlo",
                "ul": [
                    "Muda para público durante a campanha e volta a privado quando quiseres.",
                    "Arquiva as publicações que preferes guardar para ti; nada é apagado.",
                    "Partilha as histórias mais pessoais só com os Amigos chegados, em vez de com toda a gente.",
                    "Quem te seguir enquanto és público continua a seguir-te se voltares a privado.",
                ],
            },
        ],
        "faqs": [
            ("Dá para fazer crescer uma conta privada no Instagram?", "Só um pouco, por isso nem tentamos. As pessoas podem pedir para seguir, mas não veem as tuas publicações, e poucas o fazem. Mantém a conta pública enquanto a campanha corre e ela pode fazer o seu trabalho."),
            ("Perco seguidores se voltar a pôr a conta privada?", "Não. Quem já te segue continua a seguir-te quando mudas para privado. Os novos visitantes teriam de enviar um pedido, por isso o crescimento abranda enquanto a conta estiver privada."),
            ("Tenho de aprovar os pedidos para seguir?", "Não enquanto a tua conta for pública: as pessoas seguem diretamente. Se mudares para privado a meio do mês, os novos pedidos ficam à tua espera e a campanha traz muito menos seguidores."),
            ("Precisam de acesso à minha conta para a fazer crescer?", "Não. O teu acesso continua a ser só teu; precisamos apenas do teu nome de utilizador e de um perfil público que as pessoas que enviamos possam ver."),
            ("Os gostos funcionam numa conta privada?", "Só de quem já te segue, porque mais ninguém consegue ver as publicações. Mais uma razão para a campanha precisar do perfil público."),
        ],
    },
    {
        "service": "followers",
        "modifier": "real",
        "slug": "instagram/seguidores/reais",
        "label": "Seguidores ativos no Instagram",
        "title": "Comprar seguidores reais e ativos no Instagram | Growsterr",
        "description": "Seguidores ativos no Instagram põem gosto, comentam e veem. Os nossos trazem gostos e comentários das mesmas contas: normalmente {pick_likes} por mês.",
        "h1": ("Comprar seguidores ativos no Instagram ", "que interagem mesmo."),
        "intro": "Quem quer comprar seguidores reais e ativos no Instagram quer seguidores que põem gosto, comentam e veem, não um número parado. Isso só acontece com pessoas reais, por isso é só isso que trazemos: pessoas que descobrem o teu perfil, decidem seguir-te e reagem às publicações de que gostam.",
        "hero": {"image": "instagram-real-people", "alt": "Novos seguidores do Instagram a pôr gosto numa publicação e a começar uma conversa nos comentários"},
        "sections": [
            {
                "h2": "Parecer real e ser real",
                "p": [
                    "Há seguidores feitos para parecer reais: uma foto emprestada, umas quantas publicações, um nome credível. Passam num olhar rápido e falham em tudo o resto. Nunca põem gosto na tua nova publicação, nunca veem um Reel até ao fim, nunca fazem uma pergunta nos comentários.",
                    "Alta qualidade, no único sentido que importa, quer dizer uma pessoa que pode fazer essas coisas. Fotos de perfil e biografias são cosmética; o teste é a interação.",
                ],
            },
            {
                "h2": "A atividade chega com os seguidores",
                "p": [
                    "Como os nossos seguidores são pessoas, a atividade vem com eles, das mesmas contas. Com o {pick_name}, um mês habitual traz {pick_audience} novos seguidores, com {pick_likes} gostos e {pick_comments} comentários.",
                ],
            },
            {
                "h2": "Como perceber se os seguidores são ativos",
                "ul": [
                    "Compara os gostos com os seguidores nas tuas últimas publicações: o crescimento real mexe com os dois.",
                    "Lê os comentários: os reais falam da publicação, os de bots podiam estar debaixo de qualquer uma.",
                    "Abre alguns perfis de novos seguidores: os de pessoas reais são irregulares e concretos.",
                    "Acompanha o total durante umas semanas: os seguidores ativos não desaparecem em vagas.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "Um criador a comparar gostos e comentários das publicações recentes no Instagram"},
            },
        ],
        "faqs": [
            ("O que faz de alguém um seguidor ativo?", "Ser uma pessoa que vê as tuas publicações e de vez em quando reage: um gosto, um comentário, um Reel visto, uma partilha. Ninguém reage a todas as publicações, e isso é normal."),
            ("Os meus novos seguidores vão pôr gosto nas minhas publicações?", "Muitos vão. Os gostos vêm das mesmas pessoas que te seguem, e com o {pick_name} somam normalmente {pick_likes} por mês. As pessoas põem gosto no que lhes agrada, por isso as tuas melhores publicações recolhem mais."),
            ("São seguidores de qualidade?", "São pessoas que decidiram seguir-te, a partir do local que indicaste. Não avaliamos seguidores pelo aspeto cuidado dos perfis; o que nos importa é que haja alguém por trás de cada um."),
            ("Os seguidores parecem reais?", "São reais, por isso parecem utilizadores normais do Instagram: fotos próprias, amigos e hábitos. Há perfis muito ativos e outros mais calados, como em qualquer público."),
            ("A Growsterr é um site sério ou um revendedor?", "Somos uma agência de crescimento, parte da Sterr Agency (Sterr Technologies OÜ, Tallinn, Estónia), e há uma equipa por trás de cada campanha. Trazemos pessoas ao teu perfil; não revendemos stock de seguidores."),
        ],
    },
    {
        "service": "followers",
        "modifier": "safe",
        "slug": "instagram/seguidores/seguros",
        "label": "Seguidores no Instagram de forma segura",
        "title": "Comprar seguidores Instagram num site fiável | Growsterr",
        "description": "Procuras um site fiável para comprar seguidores no Instagram? Quem somos, como pagas, o que nunca pedimos e o que confirmar em qualquer serviço de crescimento.",
        "h1": ("Comprar seguidores no Instagram num site fiável: ", "como saber se é."),
        "intro": "Antes de comprares seguidores no Instagram num site que se diz fiável, é justo perguntar quem está por trás e o que pode correr mal. Eis a nossa parte, sem rodeios: quem somos, como funciona o pagamento, o que fazemos com a tua conta (nada) e o que confirmaríamos em qualquer serviço de crescimento, incluindo o nosso.",
        "hero": {"image": "instagram-hub", "alt": "Um criador de Instagram a analisar os dados de um serviço de crescimento antes de se inscrever"},
        "sections": [
            {
                "h2": "A quem estás a pagar",
                "p": [
                    "A Growsterr é um produto da Sterr Agency, gerida pela Sterr Technologies OÜ, uma empresa registada em Tallinn, na Estónia, com sede na Turquia. Pagas com cartão no checkout da Stripe, ou com Apple Pay ou Google Pay quando o teu dispositivo os aceita, e os dados do cartão vão para a Stripe, não para nós.",
                    "É uma subscrição mensal. Podes cancelá-la tu mesmo quando quiseres, e a campanha continua até ao fim do mês pago.",
                ],
            },
            {
                "h2": "O que fazemos com a tua conta: nada",
                "p": [
                    "Nunca iniciamos sessão, nunca publicamos, nunca seguimos ninguém em teu nome e nunca mexemos numa definição. A campanha acontece fora da tua conta: as pessoas veem o teu perfil na nossa rede de parceiros e visitam-no como visitariam qualquer perfil que alguém lhes recomendasse.",
                ],
            },
            {
                "h2": "Cinco perguntas a fazer a qualquer serviço de crescimento",
                "ul": [
                    "Pede a tua palavra-passe? Um serviço legítimo nunca precisa dela.",
                    "Promete milhares de seguidores em minutos? Essa velocidade só vem de bots.",
                    "Os números são intervalos ou promessas? As pessoas não se contam antecipadamente.",
                    "Consegues cancelar sozinho, sem teres de escrever a ninguém?",
                    "Há um nome de empresa e um país por trás do site?",
                ],
            },
        ],
        "faqs": [
            ("A Growsterr é legítima?", "Sim. Somos uma empresa registada, o pagamento passa só pela Stripe e cada campanha é gerida por uma equipa e medida no teu painel. Podes parar quando quiseres na tua conta."),
            ("É seguro para a minha conta de Instagram?", "Não podemos falar pelo Instagram, e ninguém honesto pode prometer como trata uma conta. O que podemos dizer é que não fazemos nada do que põe contas em risco: nada de acessos, nada de bots, nada de picos de seguidores."),
            ("De que precisam da minha parte?", "Do teu nome de utilizador do Instagram, de saber de onde devem vir os novos seguidores e de um perfil público. A lista é só esta."),
            ("Posso confiar nos números que mostram?", "São medidos, não estimados: o teu painel mostra as visitas que a nossa campanha trouxe e os novos seguidores entre elas, dia a dia. Antes da encomenda, indicamos intervalos habituais, nunca promessas, porque as pessoas decidem por si."),
            ("Vou ser cobrado depois de cancelar?", "Não. Cancelar impede que a subscrição se renove. Ficas com o mês que pagaste, e nada é cobrado depois disso."),
        ],
    },
    {
        "service": "followers",
        "modifier": "targeted",
        "slug": "instagram/seguidores/locais",
        "label": "Seguidores locais no Instagram",
        "title": "Comprar seguidores locais no Instagram, por cidade | Growsterr",
        "description": "Compra seguidores locais no Instagram vindos da cidade, região ou país que indicares: pessoas reais que vivem onde estão os teus clientes, todos os dias do mês.",
        "h1": ("Comprar seguidores locais no Instagram ", "do sítio que escolheres."),
        "intro": "Um café no Porto ganha pouco com seguidores do outro lado do mundo. Quando compras seguidores locais no Instagram, o local é tudo, por isso é a primeira coisa que perguntamos: de que cidade, região ou país devem vir os teus novos seguidores? Depois apontamos a campanha às pessoas que vivem lá.",
        "hero": {"image": "instagram-followers", "alt": "Novos seguidores da mesma cidade a aparecer no perfil de Instagram de um negócio local"},
        "sections": [
            {
                "h2": "Porque é que o local conta mais do que o total",
                "p": [
                    "Para uma loja, um estúdio, um restaurante ou um criador que conhece pessoas ao vivo, um seguidor que pode mesmo aparecer vale vários que não podem. Os seguidores locais podem entrar pela porta, falar de ti a um amigo e reconhecer a rua onde filmaste.",
                    "Também mantém o teu público coerente. Quando a maioria dos teus seguidores partilha um lugar e uma língua, mais deles percebem cada publicação.",
                ],
            },
            {
                "h2": "Como funciona a segmentação por local",
                "ul": [
                    "Indicas uma cidade, uma região ou um país inteiro quando fazes a encomenda.",
                    "Mostramos o teu perfil primeiro às pessoas de lá, todos os dias do mês.",
                    "Se o público adequado for pequeno, alguns seguidores podem vir das zonas próximas, e não de um sítio sem relação nenhuma.",
                    "O teu conteúdo faz o resto: as pessoas seguem quando as tuas publicações lhes dizem alguma coisa.",
                ],
            },
            {
                "h2": "Seguidores do país onde trabalhas",
                "p": [
                    "Seguidores de um país para o qual nunca publicas não te ajudam, seja ele qual for. Se os teus clientes estão em Portugal, procuramos pessoas em Portugal; se estão só em Lisboa, diz-nos, e começamos por aí.",
                ],
            },
        ],
        "faqs": [
            ("Posso escolher uma cidade, e não só um país?", "Sim. Uma cidade, uma região ou um país inteiro, tudo funciona. Uma cidade dá o público mais concentrado; uma região ou um país dão à campanha mais pessoas a quem chegar."),
            ("Posso evitar seguidores do Brasil ou de outro país onde não trabalho?", "Sim. Escolhes de onde vêm os teus seguidores, e é esse local que segmentamos. Não há nada de errado com seguidores de país nenhum; a questão é se são o teu público. Se os teus clientes estão em Portugal, procuramos pessoas em Portugal."),
            ("Todos os seguidores vão ser da minha cidade?", "Mostramos o teu perfil primeiro aí. Quando o público mais parecido é maior nos arredores, alguns seguidores podem vir de lá, por isso pensa nisto como apontado à tua cidade, não vedado a ela."),
            ("A segmentação local custa mais?", "Não. Está incluída em todos os pacotes, a partir do {starter_name} a {starter_price} por mês."),
            ("Posso segmentar por idade ou interesses?", "Segmentamos só por local. Dentro desse local, é o teu conteúdo que decide quem segue, porque as pessoas seguem o que lhes interessa."),
            ("A segmentação local serve um negócio online?", "Serve, se o teu público vive num sítio concreto: uma zona de língua, um país, um mercado onde estás a entrar. Se os teus compradores estão espalhados por um país inteiro, indica o país."),
        ],
    },
    {
        "service": "followers",
        "modifier": "viral",
        "slug": "instagram/seguidores/viral",
        "label": "Seguidores no Instagram para ficar viral",
        "title": "Seguidores para ficar viral no Instagram? O que ajuda | Growsterr",
        "description": "Dá para comprar seguidores no Instagram para ficar viral? Ninguém pode prometer viralidade. Seguidores reais dão a cada publicação mais gente que a partilhe.",
        "h1": ("Comprar seguidores no Instagram para ficar viral? ", "Faz crescer quem partilha."),
        "intro": "Ninguém te pode vender uma publicação viral, diga a página o que disser. O que faz uma publicação espalhar-se são pessoas: veem, enviam a um amigo, guardam, e o Instagram mostra-a a mais pessoas parecidas. Se ficar viral é a razão para comprares seguidores no Instagram, compra a parte que pode ajudar: mais pessoas reais que veem primeiro a tua próxima publicação.",
        "hero": {"image": "instagram-followers-1000", "alt": "A linha de seguidores de um criador a saltar depois de um Reel popular e depois a manter-se"},
        "sections": [
            {
                "h2": "Porque é que um número grande não faz uma publicação espalhar-se",
                "p": [
                    "Uma publicação vai longe quando as pessoas que a veem primeiro reagem a ela. Milhares de seguidores que nunca reagem dão-lhe um arranque pior do que umas centenas que reagem, porque o Instagram vê uma publicação que o primeiro público ignorou.",
                ],
            },
            {
                "h2": "O que os seguidores reais dão a um momento viral",
                "ul": [
                    "Mais primeiros espectadores para cada publicação: as pessoas que decidem se ela vai longe.",
                    "Partilhas e publicações guardadas, que só pessoas podem dar.",
                    "Um perfil que vale a pena seguir quando uma publicação descola, para que o momento deixe alguma coisa.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Pessoas a partilhar a publicação de Instagram de um criador com amigos por mensagem"},
            },
            {
                "h2": "As probabilidades, com honestidade",
                "p": [
                    "A maioria das publicações não fica viral, nem as nossas nem as de ninguém. O crescimento constante torna mais provável que descolem as publicações que podem descolar, e faz com que as que não descolam continuem a valer a pena. É essa a troca que propomos: nenhuma promessa de um momento, uma melhor posição de partida para cada publicação.",
                ],
            },
        ],
        "faqs": [
            ("Conseguem pôr a minha publicação viral?", "Não, e desconfia de quem diga que consegue. A viralidade depende da publicação, do momento e das escolhas de milhares de pessoas. O que podemos fazer é trazer todos os dias espectadores novos e reais ao teu perfil, o que dá a cada publicação um melhor arranque."),
            ("As publicações virais trazem seguidores?", "Muitas vezes, se o perfil por trás der às pessoas uma razão para ficar. É por isso que fazemos crescer o perfil e não uma publicação só: quando algo descola, quem chega encontra um público ativo e trabalho feito."),
            ("Comprar seguidores ajuda o algoritmo?", "Os bots comprados jogam contra ti, porque fazem todas as publicações parecer ignoradas. Seguidores reais que reagem ajudam cada publicação a arrancar melhor. Nenhum dos dois é um interruptor que se liga."),
            ("Que pacote serve para uma publicação que acho que pode descolar?", "O {rising_name} ou o {pro_name}. Ambos te deixam indicar as publicações que devem ter mais olhos, para que mais pessoas reais vejam aquela em que acreditas. O {pro_name} junta destaque prioritário."),
            ("Em quanto tempo noto diferença?", "A tua campanha arranca depressa e os novos seguidores chegam desde os primeiros dias. Se uma publicação descola nunca tem data marcada; o teu crescimento tem."),
        ],
    },
    # --- Gostos ---------------------------------------------------------------------------
    {
        "service": "likes",
        "slug": "instagram/gostos",
        "label": "Gostos no Instagram",
        "title": "Comprar gostos no Instagram de pessoas reais | Growsterr",
        "description": "Gostos no Instagram de pessoas que viram a tua publicação e gostaram, dentro de cada pacote mensal: normalmente {starter_likes} por mês com o {starter_name}.",
        "h1": ("Gostos no Instagram ", "de quem gostou mesmo da publicação."),
        "intro": "Queres comprar gostos no Instagram para as tuas publicações? Connosco, nunca são vendidos à parte. Cada pacote leva pessoas reais ao teu perfil, e elas põem gosto nas publicações de que gostam: o {starter_name} traz normalmente {starter_likes} gostos por mês, o {pick_name} {pick_likes}, com novos seguidores e comentários.",
        "hero": {"image": "instagram-hub", "alt": "Gostos de pessoas reais a juntar-se numa grelha de publicações de Instagram"},
        "sections": [
            {
                "h2": "Um gosto é só o começo",
                "p": [
                    "No Instagram, um gosto é muitas vezes a primeira de várias coisas que uma pessoa faz: abre o teu perfil, vê mais umas publicações, segue-te, volta na semana seguinte. Os gostos comprados à parte ficam pelo primeiro passo, e uma publicação cheia de gostos e sem mais nada à volta lê-se exatamente assim.",
                    "Os nossos vêm de pessoas que estão nesse caminho. É por isso que chegam com seguidores e comentários, e não sozinhos.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Uma pessoa a pôr gosto numa publicação de Instagram e depois a abrir o perfil do criador"},
            },
            {
                "h2": "Gostos nas publicações que escolheres",
                "p": [
                    "Com o {starter_name}, os gostos caem onde as pessoas mais gostam, normalmente nas tuas publicações mais recentes. O {rising_name} e o {pro_name} deixam-te escolher que publicações recebem a atenção, o que dá jeito para um lançamento, uma colaboração ou uma publicação que queres mesmo que seja vista.",
                ],
            },
            {
                "h2": "Onde comprar gostos no Instagram online em 2026",
                "ul": [
                    "Nenhuma app para instalar e nenhum acesso para partilhar: um site que queira uma das duas coisas está a pedir o tipo de acesso errado.",
                    "Gostos que chegam com visualizações e seguidores, não antes deles.",
                    "Intervalos habituais em vez de quantidades exatas, porque são as pessoas que decidem.",
                    "Uma empresa com nome e um checkout que reconheces: a nossa é a Sterr Technologies OÜ, com pagamentos por cartão através da Stripe.",
                ],
            },
        ],
        "faqs": [
            ("Posso comprar gostos para uma só publicação?", "Não como encomenda avulsa. Os gostos vêm dentro de um pacote mensal, de pessoas que descobrem o teu perfil. Com o {rising_name} ou o {pro_name} podes apontar essa atenção às publicações que escolheres."),
            ("Há uma app para gostos no Instagram?", "Não temos, e não precisas. Encomendas no site, pagas pela Stripe e acompanhas a campanha na tua conta em qualquer dispositivo. Nunca precisamos do teu acesso ao Instagram."),
            ("Quantos gostos traz cada pacote?", "Normalmente {starter_likes} por mês com o {starter_name}, {rising_likes} com o {rising_name} e {pro_likes} com o {pro_name}. Intervalos, não contagens: cada gosto é a escolha de uma pessoa."),
            ("Quando começam os gostos?", "Assim que a campanha estiver a correr e as primeiras pessoas chegarem ao teu perfil, normalmente nos primeiros dias. Continuam a chegar ao longo do mês, nunca de uma só vez."),
            ("Os gostos ainda importam agora que se podem esconder?", "O Instagram deixa esconder o número de gostos, por isso o número no ecrã pesa menos do que antes. O que continua a importar é que as pessoas interajam com as tuas publicações, e é isso que os gostos reais refletem."),
        ],
    },
    {
        "service": "likes",
        "modifier": "comment-likes",
        "slug": "instagram/gostos/em-comentarios",
        "label": "Gostos em comentários no Instagram",
        "title": "Gostos em comentários no Instagram: o que resulta | Growsterr",
        "description": "Queres comprar gostos para comentários no Instagram? Não os vendemos. Quem chega às tuas publicações lê a conversa e põe gosto nas respostas com que concorda.",
        "h1": ("Gostos em comentários no Instagram ", "vêm de quem lê a conversa."),
        "intro": "Há duas razões para comprar gostos em comentários no Instagram: fazer subir um comentário na publicação de outra pessoa, ou dar mais movimento à tua própria secção de comentários. Não vendemos nenhuma das duas coisas. Trazemos pessoas reais ao teu perfil, e quem lê os teus comentários pode pôr gosto nas respostas com que concorda, por iniciativa própria.",
        "hero": {"image": "instagram-real-people", "alt": "Uma conversa animada nos comentários de uma publicação de Instagram, com gostos nas melhores respostas"},
        "sections": [
            {
                "h2": "Comentários nas publicações de outras pessoas",
                "p": [
                    "Um comentário com muitos gostos no topo da publicação de uma conta grande pode trazer-te visitas, e é por isso que há quem procure gostos para comentários. Não fazemos campanhas nas publicações de outras pessoas. O nosso trabalho acontece no teu próprio perfil: mostramo-lo a pessoas reais, e elas decidem o que fazer lá.",
                ],
            },
            {
                "h2": "Gostos em comentários nas tuas publicações",
                "p": [
                    "Nas tuas publicações, os gostos em comentários surgem naturalmente quando há conversa. Quem chega através da campanha lê os comentários, responde a alguns e põe gosto naqueles com que concorda, incluindo os teus. Não contamos nem prevemos esses gostos, porque ninguém consegue adivinhar em que resposta uma pessoa vai pôr gosto.",
                    "O que contamos: com o {pick_name}, um mês traz normalmente {pick_likes} gostos nas tuas publicações e {pick_comments} comentários.",
                ],
            },
            {
                "h2": "Três formas de ganhar mais gostos nas tuas respostas",
                "ul": [
                    "Responde depressa aos primeiros comentários, enquanto as pessoas ainda estão na publicação.",
                    "Responde com algo que valha a pena ler: uma dica, um pormenor, uma pergunta de volta.",
                    "Fixa um comentário que lance a conversa que queres.",
                ],
            },
        ],
        "faqs": [
            ("Vendem gostos para comentários no Instagram?", "Não. Os gostos em comentários, como qualquer outro gosto, só vêm de quem decide dá-los. Os nossos pacotes trazem essas pessoas às tuas publicações; aquilo em que põem gosto na conversa é com elas."),
            ("Conseguem pôr o meu comentário no topo da publicação de outra conta?", "Não. Só fazemos crescer o teu próprio perfil, e não enviamos gostos para comentários em mais lado nenhum."),
            ("A minha secção de comentários vai ter mais movimento?", "Normalmente sim, porque mais pessoas veem as tuas publicações. Com o {pick_name} vêm normalmente {pick_comments} comentários por mês, e os comentários tendem a atrair respostas e gostos próprios."),
            ("Os gostos em comentários contam para os números do pacote?", "Não. Os nossos intervalos habituais contam os gostos nas tuas publicações. Os gostos em comentários vêm por cima disso, sempre que as pessoas os dão."),
            ("Vão iniciar sessão na minha conta?", "Não. Ninguém do nosso lado mexe na tua conta, e a tua palavra-passe nunca sai das tuas mãos. Tudo o que acontece nas tuas publicações é feito por pessoas, a partir das contas delas."),
        ],
    },
    {
        "service": "likes",
        "modifier": "gradual",
        "slug": "instagram/gostos/entrega-gradual",
        "label": "Gostos no Instagram aos poucos",
        "title": "Gostos no Instagram aos poucos, ao longo de dias | Growsterr",
        "description": "Queres comprar gostos no Instagram devagar, e não num pico? Os nossos vêm de pessoas reais que encontram as tuas publicações ao longo do mês, como é natural.",
        "h1": ("Gostos no Instagram devagar, ", "porque as pessoas não têm pressa."),
        "intro": "Se procuras comprar gostos no Instagram devagar, já sabes que centenas de gostos em dois minutos parecem estranhos. Devagar está certo, mas a velocidade é só metade da questão. Os nossos gostos chegam aos poucos porque vêm de pessoas reais que encontram as tuas publicações ao longo de dias e semanas, não de uma fila com temporizador.",
        "hero": {"image": "instagram-followers-1000", "alt": "Gostos numa publicação de Instagram a crescer suavemente ao longo de vários dias"},
        "sections": [
            {
                "h2": "Como crescem os gostos numa publicação real",
                "p": [
                    "Uma publicação ganha gostos em curva: uma primeira vaga de quem a vê pouco depois de a partilhares, e depois uma cauda longa à medida que é encontrada no teu perfil, através de uma hashtag ou nas mensagens de um amigo. Essa cauda pode durar semanas.",
                    "As nossas campanhas acrescentam pessoas a cada parte dessa curva. Visitam o teu perfil ao longo do mês, percorrem as tuas publicações e põem gosto no que lhes agrada, por isso as publicações mais antigas também ganham gostos, e não só a mais recente.",
                ],
            },
            {
                "h2": "Porque um temporizador não é o mesmo que tempo",
                "p": [
                    "Os gostos de bots libertados devagar resolvem o problema errado. O pico desaparece, mas as contas por trás dos gostos continuam a nunca ver, seguir ou comentar, e gostos sem as visualizações, os seguidores ou os comentários à volta parecem igualmente estranhos a um ritmo lento.",
                ],
            },
            {
                "h2": "Quando devagar não é o que queres",
                "p": [
                    "Se precisas de uma parede de gostos numa publicação dentro de uma hora, somos o serviço errado, e preferimos dizê-lo já. Se queres que cada publicação continue a juntar gostos de pessoas que se interessam, é exatamente para isso que existimos.",
                ],
            },
        ],
        "faqs": [
            ("A que ritmo chegam os gostos?", "Ao ritmo a que as pessoas encontram as tuas publicações: alguns nos primeiros dias da campanha, mais nas semanas seguintes. Não há temporizador nem lotes, por isso não há dois dias iguais."),
            ("Posso escolher a velocidade dos gostos?", "Não, e é de propósito. O ritmo vem das pessoas que visitam o teu perfil. O que podes escolher, com o {rising_name} ou o {pro_name}, é que publicações recebem a atenção."),
            ("As publicações mais antigas também recebem gostos?", "Muitas vezes, sim. Quem descobre o teu perfil vai ver publicações anteriores e põe gosto no que lhe agrada, por isso os gostos espalham-se pelo teu feed em vez de se acumularem numa só publicação."),
            ("Os gostos lentos parecem mais naturais?", "Lento só parece natural quando há pessoas por trás. Os nossos parecem porque há: cada gosto vem com uma pessoa que também pode seguir-te ou comentar."),
            ("Quantos gostos chegam num mês?", "Com o {pick_name}, normalmente {pick_likes} ao longo de 30 dias. É um intervalo, não uma quota, porque as pessoas põem gosto ao seu ritmo."),
        ],
    },
    {
        "service": "likes",
        "modifier": "monthly",
        "slug": "instagram/gostos/mensais",
        "label": "Gostos mensais no Instagram",
        "title": "Gostos automáticos no Instagram, todos os meses | Growsterr",
        "description": "Compra gostos no Instagram ao mês, não por publicação: uma subscrição, pessoas reais, gostos o mês inteiro. Renova-se sozinha e cancelas quando quiseres.",
        "h1": ("Gostos automáticos no Instagram todos os meses, ", "de pessoas, não de um script."),
        "intro": "Se queres comprar gostos automáticos no Instagram todos os meses, provavelmente queres deixar de pensar em gostos publicação a publicação. É isso que um pacote faz. Subscreves uma vez, nós corremos a tua campanha todos os dias, e pessoas reais põem gosto nas publicações de que gostam o mês inteiro: normalmente {pick_likes} gostos com o {pick_name}. Renova-se todos os meses até cancelares.",
        "hero": {"image": "instagram-creator-studio", "alt": "Um criador a planear um mês de publicações de Instagram num calendário de parede"},
        "sections": [
            {
                "h2": "Automático, mas não automatizado",
                "p": [
                    "Gostos automáticos costumam ser software que deteta cada nova publicação e lhe dispara um número fixo de gostos em minutos. É automático, e cada um desses gostos vem de uma conta que ninguém usa.",
                    "Os nossos são automáticos noutro sentido: não tens de fazer nada por cada publicação. A campanha continua a correr, as pessoas continuam a descobrir o teu perfil e os gostos que deixam são delas.",
                ],
            },
            {
                "h2": "O que muda com um pacote mensal",
                "ul": [
                    "Um preço por mês, {pick_price} pelo {pick_name}, em vez de uma encomenda por publicação.",
                    "Nenhuma quantidade para definir e nenhum horário para agendar.",
                    "Gostos em publicações novas e antigas, à medida que as pessoas as encontram.",
                    "Um mês de gostos é um mês de feedback: vês de que publicações as pessoas gostam mesmo.",
                    "Podes parar quando quiseres, sem pré-aviso.",
                ],
            },
        ],
        "faqs": [
            ("As novas publicações recebem gostos automaticamente?", "Quem decide são as pessoas, por isso não há um número fixo por publicação. As publicações novas costumam ser por onde as pessoas começam, e com o {rising_name} ou o {pro_name} podes dizer-nos que publicações devem receber a atenção."),
            ("A subscrição renova-se automaticamente?", "Sim. A Stripe renova-a todos os meses no meio de pagamento que escolheste. Cancelar leva um instante na tua conta, e o mês que já pagaste continua até ao fim."),
            ("De quantas publicações preciso?", "Não há mínimo, mas os gostos vêm de pessoas que percorrem o teu perfil, por isso algumas publicações recentes dão-lhes alguma coisa de que gostar. Publicar ao longo do mês dá a cada novo visitante mais em que pôr gosto."),
            ("Posso mudar de pacote de um mês para o outro?", "Sim. Começa com o pacote que te serve hoje e sobe quando as tuas publicações estiverem prontas para mais pessoas."),
            ("É o mesmo que software de gostos automáticos?", "Não. O software que põe gosto em todas as publicações com temporizador usa contas sem ninguém por trás. Os nossos gostos vêm de pessoas que visitaram o teu perfil e gostaram de uma publicação."),
        ],
    },
    {
        "service": "likes",
        "modifier": "no-drop",
        "slug": "instagram/gostos/sem-quedas",
        "label": "Gostos no Instagram que ficam",
        "title": "Gostos no Instagram que ficam nas tuas publicações | Growsterr",
        "description": "Queres comprar gostos no Instagram que não desapareçam? Os gostos somem quando as contas por trás são removidas. Os nossos vêm de pessoas reais, por isso ficam.",
        "h1": ("Gostos no Instagram que ficam, ", "porque foi uma pessoa que os deu."),
        "intro": "Os gostos desaparecem sobretudo por uma razão: as contas que os deram são removidas. Se queres comprar gostos no Instagram que fiquem, os duradouros vêm de pessoas. Os nossos vêm, por isso um gosto na tua publicação fica lá a não ser que quem o deu mude de ideias.",
        "hero": {"image": "instagram-hub", "alt": "Uma publicação de Instagram cujos gostos se mantêm semanas depois de ter sido partilhada"},
        "sections": [
            {
                "h2": "Para onde vão os gostos que desaparecem",
                "p": [
                    "Um gosto pertence à conta que o deu. Quando o Instagram remove contas falsas ou de spam, todos os gostos que elas deixaram vão com elas, muitas vezes semanas depois da encomenda. Uma publicação pode perder uma grande parte dos gostos de um dia para o outro, e quem a viu antes nota a diferença.",
                ],
            },
            {
                "h2": "Porque é que os gostos de pessoas se mantêm",
                "p": [
                    "A conta de uma pessoa não é varrida numa limpeza. O gosto dela fica na tua publicação enquanto ela o deixar lá, e as pessoas raramente voltam atrás para retirar o gosto a algo de que gostaram.",
                    "Os gostos reais também continuam a chegar. As publicações mais antigas ganham novos gostos à medida que mais pessoas encontram o teu perfil, por isso o número de uma publicação pode continuar a subir muito depois de a partilhares.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Novos visitantes a pôr gosto numa publicação de Instagram antiga, semanas depois de ter sido publicada"},
            },
        ],
        "faqs": [
            ("Os gostos vão cair algum dia?", "Não da forma como caem os gostos comprados. Cada gosto vem da conta de uma pessoa, por isso só desaparece se essa pessoa retirar o gosto ou fechar a conta, o que é raro e acontece um de cada vez."),
            ("Há um período de reposição?", "Não há período de reposição porque não há uma queda prevista. As reposições resolvem um problema que não criamos."),
            ("Os gostos nos Reels também ficam?", "Sim. Um gosto fica em qualquer publicação, fotografia, carrossel ou Reel, enquanto a conta que o deu existir."),
            ("Como sei se os gostos que tive antes vieram de bots?", "Procura quedas repentinas depois de uma limpeza, gostos muito acima das visualizações e, entre quem pôs gosto, perfis sem publicações próprias. Os gostos de pessoas raramente mostram algum destes sinais."),
            ("Quantos gostos traz um pacote?", "O {pick_name} traz normalmente {pick_likes} por mês, distribuídos pelas publicações de que as pessoas gostam. Ficam, e os gostos do mês seguinte somam-se a eles."),
        ],
    },
    {
        "service": "likes",
        "modifier": "organic",
        "slug": "instagram/gostos/organicos",
        "label": "Gostos orgânicos no Instagram",
        "title": "Gostos orgânicos no Instagram de quem te encontrou | Growsterr",
        "description": "Compra gostos orgânicos no Instagram e recebe feedback honesto: pessoas reais veem as tuas publicações nas nossas campanhas e só põem gosto no que lhes agrada.",
        "h1": ("Gostos orgânicos no Instagram, ", "e o que te dizem."),
        "intro": "Quando compras gostos orgânicos no Instagram, recebes algo que os gostos comprados não dão: feedback honesto. As nossas campanhas põem as tuas publicações à frente de pessoas reais, e elas só põem gosto no que lhes agrada. Algumas publicações vão juntar muito mais do que outras, e essa diferença diz-te o que o teu público quer.",
        "hero": {"image": "instagram-real-people", "alt": "Pessoas a reagir de forma diferente a uma fila de publicações de Instagram, gostando mais de umas do que de outras"},
        "sections": [
            {
                "h2": "Gostos desiguais são bom sinal",
                "p": [
                    "Os gostos comprados são suspeitamente iguais: cada publicação recebe mais ou menos o mesmo número, seja ela qual for. Os gostos orgânicos variam. Um Reel forte dispara, uma foto mais discreta fica para trás, e o padrão parece o de um público com opinião, porque é.",
                ],
            },
            {
                "h2": "Usar os gostos para publicar melhor",
                "ul": [
                    "Compara as tuas três melhores publicações do mês: o que têm em comum?",
                    "Repara no formato de que as pessoas mais gostam: Reels, carrosséis ou fotografias.",
                    "Publica mais do que resulta e vê se os gostos acompanham.",
                    "Com o {rising_name} ou o {pro_name}, dá atenção extra a uma publicação que testa uma ideia nova.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "Um criador a ordenar as publicações de Instagram do mês passado pelo número de gostos"},
            },
            {
                "h2": "Como os gostos orgânicos chegam às tuas publicações",
                "p": [
                    "Mostramos o teu perfil a pessoas na nossa rede de parceiros, na cidade, região ou país que escolheres. Elas exploram, seguem-te se quiserem e põem gosto nas publicações que lhes chamam a atenção. Ninguém é convidado a pôr gosto em nada.",
                ],
            },
        ],
        "faqs": [
            ("Pagar pelo alcance torna os gostos menos orgânicos?", "Não. Pagar para ser visto é como funciona qualquer anúncio ou publicação promovida. O gosto em si continua a ser a reação de alguém à tua publicação."),
            ("Todas as publicações vão receber gostos?", "A maioria das publicações de que as pessoas gostam vai receber, mas não por igual, e é essa a ideia. As tuas melhores publicações costumam juntar mais."),
            ("Quantos gostos orgânicos posso esperar?", "Um mês habitual com o {pick_name} traz {pick_likes}. O total é um intervalo; a forma como se reparte pelas publicações depende de quem as vê."),
            ("Os gostos orgânicos vêm com seguidores?", "Sim. Quem põe gosto nas tuas publicações muitas vezes também te segue: normalmente {pick_audience} novos seguidores por mês com o {pick_name}, e alguns deixam comentários."),
            ("Porque é melhor do que um número fixo por publicação?", "Porque um número fixo não te diz nada. Os gostos orgânicos sobem e descem com cada publicação, por isso mostram-te o que está a resultar e o que não está."),
        ],
    },
    {
        "service": "likes",
        "modifier": "private-account",
        "slug": "instagram/gostos/conta-privada",
        "label": "Gostos no Instagram numa conta privada",
        "title": "Comprar gostos no Instagram com conta privada? | Growsterr",
        "description": "Dá para comprar gostos no Instagram numa conta privada? Só os seguidores aprovados veem as publicações, e ninguém novo lhes pode pôr gosto. Eis o que funciona.",
        "h1": ("Gostos numa conta privada do Instagram ", "só podem vir de seguidores."),
        "intro": "Antes de comprares gostos no Instagram para uma conta privada, conhece o limite: num perfil privado, só os seguidores aprovados veem as tuas publicações, por isso só eles lhes podem pôr gosto. Quem uma campanha trouxesse ao teu perfil encontraria um cadeado. Por isso, enquanto a campanha corre, o perfil tem de ser público, e há boas formas de manter a privacidade onde ela importa.",
        "hero": {"image": "instagram-hub", "alt": "Uma publicação de Instagram visível apenas para os seguidores aprovados"},
        "sections": [
            {
                "h2": "Quem pode pôr gosto numa publicação de uma conta privada",
                "p": [
                    "Só as pessoas que aprovaste. Todas as outras veem o teu nome, a biografia e o número de seguidores, mas nem uma publicação, por isso não há nada em que pôr gosto. Um serviço que prometa gostos aí precisaria primeiro que as suas contas fossem aprovadas como teus seguidores, por ti ou por alguém com sessão iniciada como tu.",
                ],
            },
            {
                "h2": "Manter a privacidade, de forma prática",
                "ul": [
                    "Tem uma segunda conta, pública, para o teu trabalho e mantém a pessoal privada.",
                    "Esconde o número de gostos em qualquer publicação, se preferires que não se veja.",
                    "Desativa os comentários nas publicações que queres partilhar sem conversa.",
                ],
            },
            {
                "h2": "O que muda quando o perfil é público",
                "p": [
                    "As pessoas podem ver as tuas publicações e pôr gosto nas de que gostam; com o {pick_name}, isso dá normalmente {pick_likes} gostos por mês, com novos seguidores e comentários. Continuas a decidir o que publicas e com quem falas.",
                ],
            },
        ],
        "faqs": [
            ("Quem não me segue pode pôr gosto em publicações de uma conta privada?", "Não. O Instagram só mostra as publicações de uma conta privada aos seguidores aprovados, por isso mais ninguém lhes pode pôr gosto."),
            ("Tenho de ficar público depois da campanha?", "Não, a escolha é tua, e os gostos que já tens nas publicações ficam. Mas enquanto a conta estiver privada, pessoas novas não veem as tuas publicações, por isso uma campanha a decorrer não te pode trazer gostos."),
            ("Posso antes fazer crescer uma conta pública à parte?", "Sim. Uma conta pública para o teu trabalho e uma privada para os amigos funciona bem. Faríamos crescer a pública."),
            ("Vão precisar de acesso para aprovar pedidos?", "Não. A tua palavra-passe fica contigo, e nunca iniciamos sessão na tua conta. Num perfil público não há nada para aprovar: as pessoas seguem e põem gosto diretamente."),
            ("Posso esconder o número de gostos e continuar a crescer?", "Sim. Esconder o número só muda o que os visitantes veem nessa publicação. As pessoas continuam a poder pôr gosto, e tu continuas a ver o número."),
        ],
    },
    {
        "service": "likes",
        "modifier": "real",
        "slug": "instagram/gostos/reais",
        "label": "Gostos reais no Instagram",
        "title": "Comprar gostos reais no Instagram, sem bots | Growsterr",
        "description": "Gostos reais no Instagram de pessoas genuínas com contas próprias, nunca de bots. Chegam com seguidores e comentários das mesmas pessoas, em todos os pacotes.",
        "h1": ("Gostos reais no Instagram, ", "cada um de alguém que gostou mesmo."),
        "intro": "Queres comprar gostos reais no Instagram? Um gosto real vem de alguém que olhou para a tua publicação e gostou do que viu. É o único tipo que trazemos. Cada pacote mostra o teu perfil a pessoas, e os gostos que deixam aparecem ao lado de seguidores, comentários e visualizações das mesmas contas, por isso a tua interação parece realista porque é.",
        "hero": {"image": "instagram-real-people", "alt": "Pessoas diferentes, cada uma com o seu perfil, a pôr gosto na mesma publicação de Instagram"},
        "sections": [
            {
                "h2": "Gostos premium, gostos de qualidade e gostos reais",
                "p": [
                    "Muitos vendedores dividem os gostos em escalões: baratos, de contas vazias; premium ou de alta qualidade, de contas com fotos e publicações. Os dois escalões são a mesma coisa com roupa diferente: contas que põem gosto por encomenda. Um disfarce melhor não torna um gosto genuíno.",
                    "Qualidade, num gosto, quer dizer uma coisa: uma pessoa decidiu dá-lo. Tudo o resto é apresentação.",
                ],
            },
            {
                "h2": "Gostos reais que vão além do gosto",
                "p": [
                    "Um gosto real vem de alguém que também pode seguir-te, comentar ou ver o teu próximo Reel. É por isso que os gostos reais fazem subir o resto dos teus números em vez de ficarem ao lado deles: são um passo naquilo que uma pessoa faz, não a transação toda.",
                ],
            },
            {
                "h2": "Como detetar gostos que só parecem reais",
                "ul": [
                    "Os gostos disparam enquanto as visualizações, os seguidores e os comentários ficam parados.",
                    "Os perfis de quem pôs gosto têm fotos de banco de imagens, poucas publicações e milhares de contas seguidas.",
                    "Chegam centenas nos minutos a seguir a publicares, e depois nada.",
                    "O número cai umas semanas mais tarde.",
                ],
            },
        ],
        "faqs": [
            ("Os vossos gostos no Instagram vêm de contas reais?", "Sim. Cada gosto vem da conta de uma pessoa: alguém que descobriu o teu perfil através da nossa campanha e gostou da publicação. Sem bots e sem quintas de contas."),
            ("Vendem gostos premium?", "Não vendemos gostos por escalões nem à parte. Cada gosto que trazemos vem de uma pessoa, dentro de um pacote mensal; o {starter_name}, o mais pequeno, traz normalmente {starter_likes} por mês."),
            ("Os gostos reais aumentam o meu alcance?", "Ajudam como só a interação real consegue, porque as pessoas por trás deles também podem seguir, comentar e partilhar. Até onde vai uma publicação continua a depender da própria publicação, por isso nunca prometemos alcance."),
            ("Porque é que alguns gostos comprados parecem reais?", "Porque são feitos para isso: fotos de perfil, umas quantas publicações, nomes credíveis. Olha para o que acontece à volta deles. Os gostos de pessoas vêm com visualizações e seguidores; os disfarçados chegam sozinhos."),
            ("Posso ter gostos reais sem novos seguidores?", "Não. Os gostos chegam como parte do pacote, de pessoas que encontram o teu perfil, e muitas delas também te seguem. É isso que mantém os gostos realistas."),
        ],
    },
    {
        "service": "likes",
        "modifier": "reels",
        "slug": "instagram/gostos/reels",
        "label": "Gostos em Reels do Instagram",
        "title": "Comprar gostos para Reels do Instagram, de quem viu | Growsterr",
        "description": "Gostos para Reels do Instagram, da forma honesta: as pessoas veem os teus vídeos e põem gosto nos que lhes agradam. Cada gosto tem uma visualização por trás.",
        "h1": ("Gostos nos teus Reels, ", "de quem os viu mesmo."),
        "intro": "Antes de comprares gostos para Reels no Instagram, convém saber quanto vale um gosto num Reel que ninguém viu: pouco. Os nossos gostos em Reels vêm de pessoas reais que descobriram o teu perfil, viram os teus vídeos e puseram gosto nos que as prenderam, a par de novos seguidores e comentários.",
        "hero": {"image": "instagram-creator-studio", "alt": "Um criador a editar um Reel de Instagram no telemóvel, à secretária"},
        "sections": [
            {
                "h2": "Num Reel, ver vem antes de pôr gosto",
                "p": [
                    "Os Reels vivem do que os espectadores fazem: se veem até ao fim, se voltam a ver, se partilham, se seguem. Um gosto é um sinal entre esses, e vale mais quando vem depois de uma visualização real.",
                    "Os gostos em vídeos comprados à parte costumam chegar sem reproduções que batam certo. Um Reel com mais gostos do que visualizações é fácil de detetar e não diz nada de bom sobre a forma como os conseguiu.",
                ],
            },
            {
                "h2": "Pôr mais pessoas a ver os teus Reels",
                "ul": [
                    "As pessoas exploram o teu perfil e veem os Reels que lhes chamam a atenção, não só os mais recentes.",
                    "O {rising_name} e o {pro_name} deixam-te pôr um Reel concreto à frente de mais pessoas.",
                    "Os espectadores vêm do local que escolheres, por isso a tua língua e as tuas referências chegam lá.",
                ],
            },
            {
                "h2": "Faz contar os primeiros segundos",
                "p": [
                    "Podemos levar pessoas aos teus Reels; mantê-las lá é trabalho do vídeo. Um gancho claro logo no primeiro segundo, legendas para quem vê sem som e um final que dê vontade de voltar a ver ajudam a transformar uma visualização num gosto.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Espectadores a ver um Reel de Instagram até ao fim e a tocar em gosto"},
            },
        ],
        "faqs": [
            ("Posso apontar os gostos a um Reel específico?", "Sim, com o {rising_name} ou o {pro_name}: escolhes que publicações e Reels recebem a atenção, e as pessoas fazem o resto. Com o {starter_name}, os espectadores encontram sozinhos os Reels de que gostam."),
            ("Os gostos nos Reels vêm com visualizações?", "Sim. As pessoas veem antes de pôr gosto, por isso há uma visualização por trás de cada gosto. Não vendemos nem contamos visualizações à parte, porque cada uma é uma pessoa que decide ver."),
            ("Isto põe o meu Reel no Explorar?", "Ninguém pode prometer isso, e nós não prometemos. É o Instagram que decide o que vai para o Explorar e para o feed de Reels. Espectadores que veem e reagem dão a um Reel um arranque justo; gostos comprados sem visualizações dão-lhe um arranque estranho."),
            ("A minha conta tem de ser pública?", "Sim, enquanto a campanha corre. Quem não te segue não consegue ver Reels numa conta privada, por isso também não lhes poderia pôr gosto."),
            ("Quantos gostos vão ter os meus Reels?", "Com o {pick_name}, normalmente {pick_likes} gostos por mês entre publicações e Reels. A forma como se repartem depende daquilo de que as pessoas mais gostam."),
        ],
    },
    {
        "service": "likes",
        "modifier": "safe",
        "slug": "instagram/gostos/seguros",
        "label": "Gostos legítimos no Instagram",
        "title": "Gostos legítimos no Instagram: como os reconhecer | Growsterr",
        "description": "Queres comprar gostos no Instagram de forma segura? Um gosto legítimo vem de quem viu a tua publicação. Como o reconhecer e como os nossos pacotes o trazem.",
        "h1": ("Gostos legítimos no Instagram ", "começam com uma pessoa e uma publicação."),
        "intro": "Procuras comprar gostos no Instagram de forma segura e legítima? Um gosto legítimo tem duas partes: uma pessoa real e uma publicação que ela viu mesmo. Tudo o que fazemos assenta nas duas. Mostramos o teu perfil a pessoas, e quem gosta das tuas publicações põe-lhes gosto, sem acessos à tua conta, sem bots e sem gostos vendidos à parte.",
        "hero": {"image": "instagram-hub", "alt": "Uma pessoa a percorrer o Instagram e a parar para pôr gosto numa publicação de que gostou"},
        "sections": [
            {
                "h2": "Sinais de alarme em qualquer oferta de gostos",
                "ul": [
                    "Um preço por cada mil gostos: as pessoas não se compram ao milhar.",
                    "Entrega em minutos, ou a promessa de números exatos.",
                    "Um pedido da tua palavra-passe, ou um início de sessão através de uma app.",
                    "Gostos vendidos sem visualizações, seguidores ou comentários a acompanhar.",
                ],
            },
            {
                "h2": "Porque é que os gostos falsos nunca são legítimos, venda-os quem os vender",
                "p": [
                    "As regras do Instagram pedem às pessoas que não juntem gostos de forma artificial, e os gostos de contas que põem gosto por encomenda são exatamente isso. Não podemos dizer como o Instagram trata uma conta em particular, e não vamos adivinhar. Simplesmente não levamos nada de artificial à tua.",
                ],
            },
            {
                "h2": "De onde vêm os nossos gostos",
                "p": [
                    "Das pessoas que as nossas campanhas levam ao teu perfil: utilizadores da nossa rede de parceiros, no local que escolheres, todos os dias do mês. Põem gosto no que lhes agrada, normalmente {pick_likes} gostos por mês com o {pick_name}, e muitos também te seguem e comentam.",
                ],
            },
        ],
        "faqs": [
            ("É legítimo comprar gostos no Instagram?", "Comprar gostos a contas que os dão por encomenda vai contra as regras do Instagram sobre interação artificial. O que vendemos é diferente: alcance junto de pessoas reais, que decidem por si se põem gosto."),
            ("Posso perder a conta por causa de gostos comprados?", "Não podemos falar pelo Instagram, e quem prometer um resultado está a adivinhar. O que controlamos é que cada gosto que trazemos vem de uma pessoa, e que nunca mexemos no teu acesso."),
            ("Como pago?", "Com cartão, Apple Pay ou Google Pay, através do checkout seguro da Stripe. A faturação é mensal e para quando cancelares."),
            ("Pedem o meu acesso ao Instagram?", "Nunca. Precisamos do teu nome de utilizador para arrancar a campanha. Se um serviço de gostos te pedir a palavra-passe, afasta-te."),
            ("Porque não vendem gostos por publicação?", "Porque um número fixo de gostos numa publicação fixa só pode vir de contas que põem gosto por encomenda. Nós trazemos pessoas; os gostos são o que elas fazem quando gostam de uma publicação."),
        ],
    },
    {
        "service": "likes",
        "modifier": "viral",
        "slug": "instagram/gostos/viral",
        "label": "Gostos no Instagram para ficar viral",
        "title": "Gostos virais no Instagram: espalham uma publicação? | Growsterr",
        "description": "Pensas comprar gostos no Instagram para ficar viral? Sozinhos, não espalham nada: quem espalha é quem vê, partilha e guarda. O que os gostos reais podem fazer.",
        "h1": ("Gostos virais no Instagram ", "são um resultado, não um tiro de partida."),
        "intro": "Muita gente compra gostos no Instagram para pôr uma publicação viral, na esperança de que um número grande convença o Instagram, e toda a gente, de que ela merece mais atenção. Raramente funciona assim. Gostos de pessoas que viram e gostaram de uma publicação são sinal de embalo; gostos empilhados numa publicação parada não são sinal de nada. Trazemos os primeiros, e não prometemos a parte viral.",
        "hero": {"image": "instagram-followers-1000", "alt": "Gostos, partilhas e publicações guardadas a subir juntos numa publicação de Instagram que começa a espalhar-se"},
        "sections": [
            {
                "h2": "Os gostos vêm depois de a publicação se espalhar, não antes",
                "p": [
                    "Quando uma publicação descola, os gostos são o rasto visível de milhares de pessoas a vê-la, a enviá-la a amigos e a guardá-la para mais tarde. Copia o rasto sem as pessoas e ficas com o número sem o movimento.",
                ],
            },
            {
                "h2": "O que dá mesmo uma oportunidade a uma publicação",
                "ul": [
                    "Um primeiro público que reage: pessoas que veem a publicação cedo e põem gosto, comentam ou partilham.",
                    "Um gancho que faz as pessoas parar, e uma razão para a enviar a alguém.",
                    "Publicar onde está o teu público, na língua dele, quando está a fazer scroll.",
                    "Foco: com o {rising_name} ou o {pro_name}, mais pessoas veem a publicação que achas que pode ir longe.",
                ],
            },
            {
                "h2": "O que prometemos, e o que não prometemos",
                "p": [
                    "Prometemos pessoas reais, todos os dias, e um painel com o que medimos. Não prometemos milhões de visualizações, um lugar no Explorar nem uma publicação que se espalhe. Quem o promete está a vender a aparência de uma publicação viral.",
                ],
            },
        ],
        "faqs": [
            ("Comprar gostos vai pôr a minha publicação viral?", "Não por si só. O número de gostos é o resultado da atenção das pessoas, e os gostos comprados acrescentam o número sem a atenção. Gostos de quem viu dão a uma publicação um arranque honesto, que é o máximo que alguém pode oferecer."),
            ("De quantos gostos precisa uma publicação viral?", "Não há número mágico. Uma publicação com um número modesto pode ir longe se quem a vê a partilhar, e uma publicação com um número grande pode estagnar."),
            ("Mandam gostos na primeira hora depois de eu publicar?", "Não acertamos gostos pela hora de uma publicação. As pessoas chegam ao longo do mês e põem gosto no que lhes agrada. Se uma publicação importa mais, o {rising_name} e o {pro_name} deixam-te escolher que publicações recebem a atenção."),
            ("As partilhas e as publicações guardadas estão incluídas?", "Não as contamos nem as vendemos, mas acontecem: quem põe gosto nas tuas publicações também as pode partilhar e guardar, coisa que os bots nunca fazem."),
            ("Um número alto de gostos leva outros a pôr gosto?", "As pessoas reparam numa publicação movimentada. Mas um número grande sem comentários nem partilhas parece encenado precisamente aos olhos de quem queres impressionar."),
        ],
    },
]
