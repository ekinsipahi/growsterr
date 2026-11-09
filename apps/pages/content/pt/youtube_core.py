"""European Portuguese YouTube pages beyond the hub and subscribers: likes, views and the ways people
ask for subscribers (real, safe, monthly...). Keys and placeholders: docs/CONTENT.md. Brief:
docs/keywords/WRITING.md. Views are never counted in advance; we never promise monetization,
watch hours or retention."""

UPDATED = "2026-11-09"

PAGES = [
    # --- Gostos ---------------------------------------------------------------------------
    {
        "service": "likes",
        "slug": "youtube/gostos",
        "label": "Gostos no YouTube",
        "title": "Comprar gostos no YouTube de espectadores reais | Growsterr",
        "description": "Queres comprar gostos no YouTube? Nos nossos pacotes, cada gosto vem de quem viu o vídeo, com novos subscritores e comentários. Desde {from_price} por mês.",
        "h1": ("Queres comprar gostos no YouTube? ", "Recebe-os de quem viu o vídeo."),
        "intro": "Se vieste comprar gostos no YouTube, primeiro uma resposta direta: não vendemos gostos em lotes. Cada pacote traz ao teu canal pessoas reais que veem os teus vídeos e põem gosto nos que lhes agradam, normalmente {starter_likes} gostos por mês com o {starter_name} e mais com os pacotes maiores.",
        "hero": {"image": "youtube-viewers", "alt": "Espectadores no telemóvel a pôr gosto num vídeo de YouTube que acabaram de ver"},
        "sections": [
            {
                "h2": "O que um gosto diz ao YouTube",
                "p": [
                    "Um gosto é um pequeno voto público de alguém que carregou no play. O YouTube lê-o a par de tudo o resto que esse espectador fez: quanto tempo viu, se subscreveu, se voltou para o vídeo seguinte.",
                    "Um gosto de uma conta que nunca viu nada quebra esse padrão. O contador debaixo do teu vídeo sobe enquanto tudo à volta fica parado, e o YouTube trata como spam a interação que considera artificial.",
                ],
            },
            {
                "h2": "Onde caem os gostos: vídeos, música e publicações",
                "p": [
                    "Os novos espectadores põem gosto no que lhes agrada, normalmente nos teus vídeos mais recentes e no vídeo que os trouxe ao teu canal. Os músicos veem o mesmo em videoclipes e vídeos com letra: gostos de ouvintes que tocaram a faixa e quiseram mais.",
                    "As publicações da comunidade funcionam de outra forma. Os teus subscritores veem-nas no feed e podem pôr-lhes gosto por si, mas os intervalos que indicamos são gostos nos teus vídeos.",
                ],
                "image": {"image": "youtube-channel", "alt": "Um músico a gravar uma canção num estúdio caseiro para um videoclipe no YouTube"},
            },
            {
                "h2": "Porque é que os gostos chegam com subscritores",
                "p": [
                    "Um gosto é a coisa mais leve que um espectador pode fazer. Num pacote, vem com sinais mais fortes das mesmas pessoas: uma subscrição, um comentário, um regresso para o vídeo seguinte. Quando esses números sobem juntos, descrevem um canal de que as pessoas gostam, porque é isso que ele é.",
                ],
            },
        ],
        "faqs": [
            ("Posso comprar gostos no YouTube sem subscritores?", "Não. Os gostos vêm em todos os pacotes, juntamente com novos subscritores e comentários das mesmas pessoas reais. Um gosto sem ninguém a ver por trás é o tipo de interação que o YouTube trata como spam."),
            ("Quantos gostos tem um mês habitual?", "Com o {pick_name}, normalmente {pick_likes}, o que dá mais ou menos dois a três gostos por cada novo subscritor. São as pessoas reais que decidem em que põem gosto, por isso não há dois meses iguais."),
            ("Posso ter gostos numa publicação da comunidade?", "Não como encomenda à parte. Os teus novos subscritores podem ver as tuas publicações da comunidade no feed, e alguns vão pôr-lhes gosto porque querem. Os intervalos habituais de cada pacote contam gostos em vídeos."),
            ("Os videoclipes também recebem gostos?", "Sim. Se o teu canal é de música, as pessoas que trazemos são ouvintes que tocaram as tuas faixas e puseram gosto nas que lhes agradaram. Podes apontar a campanha à cidade, região ou país onde estão os teus ouvintes."),
            ("Que vídeos vão receber gostos?", "São os espectadores reais que escolhem, por isso costumam ser os teus vídeos mais recentes e aquele que primeiro os trouxe ao teu canal."),
            ("Quando aparecem os primeiros gostos?", "Nos primeiros dias da campanha, à medida que chegam os primeiros espectadores, e depois alguns todos os dias durante o resto do mês."),
        ],
    },
    {
        "service": "likes",
        "modifier": "comment-likes",
        "slug": "youtube/gostos/em-comentarios",
        "label": "Gostos em comentários no YouTube",
        "title": "Gostos em comentários no YouTube: como surgem | Growsterr",
        "description": "A pensar comprar gostos para comentários no YouTube? Não pomos um comentário no topo. Espectadores reais leem as conversas e põem gosto no que lhes diz algo.",
        "h1": ("Comprar gostos em comentários no YouTube? ", "Cria uma secção de comentários que os mereça."),
        "intro": "Quem compra gostos para comentários no YouTube quer normalmente pôr um comentário no topo. Não vendemos isso. Trazemos espectadores reais ao teu canal, e quem lê os comentários dos teus vídeos põe gosto nas respostas, perguntas e piadas que lhe dizem alguma coisa, incluindo o teu comentário fixado.",
        "hero": {"image": "youtube-viewers", "alt": "Um espectador a percorrer os comentários de um vídeo de YouTube e a pôr gosto numa resposta"},
        "sections": [
            {
                "h2": "Um comentário no topo não é o objetivo",
                "p": [
                    "Um comentário com centenas de gostos debaixo de um vídeo que mal mexeu salta à vista de quem lê a conversa. Os gostos em comentários são interação como outra qualquer, por isso os gostos de scripts também caem nas regras de spam do YouTube.",
                    "E se o comentário estiver no vídeo de outro criador, fazê-lo subir não é coisa que façamos. Fazemos crescer o teu próprio canal, com pessoas que o escolhem.",
                ],
            },
            {
                "h2": "Como uma secção de comentários ganha vida",
                "p": [
                    "Os espectadores reais leem os comentários depois de verem. Respondem, põem gosto nos comentários com que concordam e deixam os seus: normalmente {pick_comments} comentários novos por mês com o {pick_name}, escritos por pessoas e não por scripts.",
                ],
                "ul": [
                    "Fixa um comentário que faça uma pergunta a sério aos espectadores. As respostas abrem conversas próprias.",
                    "Responde aos primeiros comentários de um vídeo novo. Um criador na conversa puxa mais gente para ela.",
                    "Dá coração aos comentários de que gostas. Os espectadores reparam e voltam para conversar.",
                ],
                "image": {"image": "youtube-channel", "alt": "Um criador a fixar uma pergunta nos comentários de um vídeo novo no YouTube"},
            },
            {
                "h2": "O que o pacote conta, e o que não conta",
                "p": [
                    "Os subscritores, os gostos em vídeos e os comentários vêm com intervalos mensais habituais. Os gostos em comentários não: acontecem quando um espectador concorda com outro, e ninguém consegue agendar isso.",
                ],
            },
        ],
        "faqs": [
            ("Podem pôr gostos no meu comentário no vídeo de outro canal?", "Não. Fazemos crescer o teu próprio canal com pessoas reais que o escolhem. Fazer subir um comentário no vídeo de outra pessoa não faz parte do que fazemos."),
            ("Os gostos em comentários vêm com o pacote?", "Vêm como vêm em qualquer canal animado: de espectadores reais que leem as conversas dos teus vídeos. Não os contamos antecipadamente, porque cada um é uma pessoa a concordar com alguém."),
            ("As minhas secções de comentários vão mesmo ter mais movimento?", "À medida que as pessoas chegam, sim: normalmente {starter_comments} comentários novos por mês com o {starter_name}, {rising_comments} com o {rising_name} e {pro_comments} com o {pro_name}, das mesmas pessoas que subscrevem."),
            ("Os comentários são escritos por bots ou por IA?", "Não. Cada comentário vem de uma pessoa que viu o teu vídeo e tinha algo a dizer. Nunca fazemos guiões de comentários nem os escrevemos por ninguém."),
            ("Podem mandar gostos para um comentário no meu próprio vídeo?", "Não. Promovemos o teu canal, e são os espectadores que decidem que comentários merecem um gosto, incluindo os teus. Um comentário fixado que pergunta algo a sério é o que tem mais probabilidade de os juntar."),
            ("É arriscado comprar gostos para comentários no YouTube?", "A um serviço de bots, sim: os gostos em comentários são interação, e o YouTube trata a interação artificial como spam. Os gostos de pessoas que leram mesmo a conversa são a vida normal de um canal."),
        ],
    },
    {
        "service": "likes",
        "modifier": "live",
        "slug": "youtube/gostos/em-direto",
        "label": "Gostos em diretos no YouTube",
        "title": "Gostos em diretos no YouTube: chat real, gostos reais | Growsterr",
        "description": "Antes de comprares gostos para diretos no YouTube: numa transmissão, vêm de quem está no chat. Trazemos subscritores reais que podem entrar. Desde {from_price}.",
        "h1": ("Comprar gostos para diretos no YouTube? ", "Vêm das pessoas que estão no teu chat."),
        "intro": "Antes de comprares gostos para diretos no YouTube, pensa em quem carrega no botão: as pessoas que estão mesmo a ver a tua transmissão. Não conseguimos pôr gostos num direto a um minuto marcado, e não vamos fingir que sim. Fazemos crescer os subscritores reais que podem ver que estás em direto e decidir entrar.",
        "hero": {"image": "youtube-channel", "alt": "Um criador em direto no YouTube a partir de uma secretária com câmara e microfone"},
        "sections": [
            {
                "h2": "Um gosto em direto é uma reação, não um número",
                "p": [
                    "Durante uma transmissão, os gostos chegam quando acontece alguma coisa no ecrã: uma jogada decisiva, uma boa resposta, a música que o chat pediu. São o público a reagir no momento.",
                    "Os gostos de contas que não estão a ver não reagem a nada. Caem em bloco ao lado de um chat calado, e qualquer pessoa real que entre vê que as duas coisas não batem certo.",
                ],
            },
            {
                "h2": "Transformar os melhores momentos de um direto em gostos",
                "ul": [
                    "Pede gostos uma vez, num momento alto, não no primeiro minuto.",
                    "Diz em voz alta os nomes do chat: as pessoas gostam de transmissões de que se sentem parte.",
                    "Fixa um comentário que explique a quem chega tarde o que está a acontecer, para ficarem o suficiente para reagir.",
                    "Deixa a gravação disponível, para que quem perdeu o direto ainda o possa ver e pôr gosto.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Pessoas a conversar e a reagir no chat de um direto no YouTube enquanto o criador fala"},
            },
            {
                "h2": "Faz crescer o público antes do próximo direto",
                "p": [
                    "Os subscritores que trazemos são pessoas reais que encontraram o teu canal e decidiram ficar. Alguns vão estar no teu próximo chat, quando lhes der jeito. Quanto maior for esse grupo, mais pessoas há para reagir quando acontece algo de bom no direto.",
                ],
            },
        ],
        "faqs": [
            ("Podem mandar gostos durante o meu direto?", "Não. As pessoas reais têm os seus horários, por isso ninguém honesto pode prometer reações a uma dada hora. O que fazemos crescer é o público que pode estar a ver quando entras em direto."),
            ("Os meus novos subscritores vão ver os meus diretos?", "Alguns, nos dias em que lhes der jeito. Escolheram o teu canal depois de o verem, por isso os teus diretos podem chegar-lhes; se entram ou não é com eles."),
            ("As pessoas podem pôr gosto num direto depois de acabar?", "Sim. A gravação fica no teu canal como vídeo, e quem a vir mais tarde pode pôr-lhe gosto."),
            ("Porque não comprar gostos para diretos a um serviço de bots?", "Porque um direto é onde a interação falsa se nota mais facilmente. Centenas de gostos ao lado de um chat em silêncio dizem a quem entra que a sala não é o que parece."),
            ("Até onde pode crescer o público dos meus diretos?", "Depende das tuas transmissões, mas a base cresce todos os dias: o {pick_name} junta normalmente {pick_audience} subscritores ao longo de um mês, e cada um é alguém que pode estar no chat da próxima vez."),
        ],
    },
    {
        "service": "likes",
        "modifier": "shorts",
        "slug": "youtube/gostos/shorts",
        "label": "Gostos em YouTube Shorts",
        "title": "Comprar gostos em YouTube Shorts de pessoas reais | Growsterr",
        "description": "Gostos em YouTube Shorts de pessoas reais que pararam de deslizar, nunca de bots. Vêm num pacote mensal com subscritores e comentários, desde {from_price}.",
        "h1": ("Comprar gostos em YouTube Shorts? ", "Conquista-os de quem parou de deslizar."),
        "intro": "No feed de Shorts, um gosto quer dizer que alguém parou de deslizar o tempo suficiente para se importar. Se queres comprar gostos em YouTube Shorts, esse é o único tipo que vale a pena: gostos de pessoas reais que trazemos ao teu canal todos os dias, que veem, põem gosto e às vezes subscrevem.",
        "hero": {"image": "youtube-viewers", "alt": "Pessoas a ver YouTube Shorts no telemóvel e a tocar em gosto"},
        "sections": [
            {
                "h2": "Quanto vale um gosto num Short",
                "p": [
                    "Os Shorts passam num feed que as pessoas percorrem depressa. Um gosto aí vem de um espectador que deixou o teu Short correr, muitas vezes mais do que uma vez, e decidiu que merecia um toque.",
                    "Os gostos gerados saltam tudo isso. Amontoam-se num Short que ninguém continuou a ver, o que é o contrário do que um gosto devia dizer.",
                ],
            },
            {
                "h2": "O que faz um Short merecer um gosto",
                "ul": [
                    "Começa pelo melhor momento. O primeiro segundo decide se as pessoas ficam.",
                    "Faz o final ligar ao início, para que voltar a ver pareça natural.",
                    "Põe legendas nos teus Shorts: muita gente vê sem som.",
                    "Termina com uma razão clara para visitar o teu canal.",
                ],
                "image": {"image": "youtube-channel", "alt": "Um criador a filmar um YouTube Short na vertical com o telemóvel de braço esticado"},
            },
            {
                "h2": "O que o pacote faz pelos teus Shorts",
                "ul": [
                    "Promovemos o teu canal; os espectadores que o descobrem escolhem os Shorts e vídeos que querem ver.",
                    "O {pick_name} junta normalmente {pick_likes} gostos ao longo de um mês, repartidos pelo que agradou às pessoas.",
                    "Diz-nos a cidade, a região ou o país, para que os teus Shorts cheguem às pessoas do sítio para onde os fazes.",
                ],
            },
        ],
        "faqs": [
            ("Posso ter gostos só num Short?", "Não como encomenda avulsa. Os gostos chegam dentro de um pacote mensal, repartidos pelos Shorts e vídeos de que as pessoas gostam, com subscritores e comentários."),
            ("Os gostos nos Shorts ajudam os meus vídeos longos?", "Indiretamente. Algumas pessoas que gostam de um Short abrem o canal por trás dele, e algumas acabam por ver os teus vídeos mais longos e subscrever."),
            ("Com que rapidez chegam os gostos aos meus Shorts?", "Desde os primeiros dias da campanha, e depois alguns por dia ao longo do mês. Milhares de gostos em Shorts numa hora vêm de bots, não de espectadores."),
            ("Quem está a pôr gosto nos meus Shorts?", "Pessoas que deram com o teu canal através da nossa campanha, no local que escolheste. Decidiram ver e decidiram pôr gosto; ninguém lhes pediu."),
            ("As pessoas também vão comentar os meus Shorts?", "Algumas vão. No conjunto do teu canal, o {pick_name} traz normalmente {pick_comments} comentários por mês, cada um escrito pela pessoa que o deixou."),
        ],
    },
    # --- Subscritores ---------------------------------------------------------------------
    {
        "service": "subscribers",
        "modifier": "gradual",
        "slug": "youtube/subscritores/entrega-gradual",
        "label": "Subscritores no YouTube com entrega gradual",
        "title": "Comprar subscritores no YouTube aos poucos | Growsterr",
        "description": "Subscritores no YouTube devagar e com constância: pessoas reais que subscrevem algumas de cada vez, todos os dias do mês, ao seu ritmo. Desde {from_price} por mês.",
        "h1": ("Comprar subscritores no YouTube devagar? ", "É o único ritmo que as pessoas reais conhecem."),
        "intro": "Se queres comprar subscritores no YouTube devagar e com constância, estás a pedir a coisa certa. Aqui, devagar é simplesmente o que as pessoas fazem: descobrem o teu canal no dia delas, veem um ou dois vídeos e decidem. Com o {pick_name}, isso soma normalmente {pick_audience} ao longo do mês.",
        "hero": {"image": "youtube-subscribers", "alt": "O número de subscritores de um canal de YouTube a subir um pouco todos os dias ao longo de um mês"},
        "sections": [
            {
                "h2": "Bots lentos continuam a ser bots",
                "p": [
                    "Há serviços que vendem uma opção a conta-gotas: os mesmos subscritores bots, libertados aos poucos para que a curva pareça suave. O ritmo muda; o que está por trás não. Contas que nunca veem nada continuam a reduzir a parte dos teus subscritores que interage.",
                    "Gradual só significa alguma coisa quando vem de pessoas a decidir uma a uma. Nenhuma definição consegue imitar isso, e nenhuma é precisa.",
                ],
            },
            {
                "h2": "Como é a constância no teu painel",
                "p": [
                    "Abre o teu painel num dia qualquer e vês duas linhas: as pessoas que visitaram o teu canal através da campanha e quantas delas subscreveram. Há dias mais movimentados do que outros, como em qualquer canal que as pessoas estão a descobrir. O que não vais ver é um salto de milhares de um dia para o outro.",
                ],
            },
            {
                "h2": "Porque é que constante é melhor do que repentino no YouTube",
                "p": [
                    "Um canal que ganha subscritores todas as semanas, a par de visualizações e comentários, é um canal que as pessoas estão a encontrar. Cada vídeo novo chega a um grupo um pouco maior de pessoas reais, e isso soma ao longo dos meses.",
                ],
                "image": {"image": "youtube-channel", "alt": "Um criador de YouTube a rever num portátil um mês de crescimento constante do canal"},
            },
        ],
        "faqs": [
            ("Quão devagar é devagar?", "Bem espalhado: um punhado de novos subscritores na maioria dos dias, nunca um lote. Ao longo de 30 dias, isso soma o intervalo habitual do pacote, e cada dia é um pouco diferente."),
            ("Posso escolher a que velocidade chegam os subscritores?", "Não à hora, porque são as pessoas reais que a definem. Escolhes o pacote: um maior mostra o teu canal a mais pessoas por dia."),
            ("Um conta-gotas é mais seguro para o meu canal?", "Só se os subscritores forem reais. Um conta-gotas de bots continua a ser interação falsa, enquanto pessoas reais a subscrever ao seu ritmo é crescimento normal."),
            ("Subscritores todos os dias vão parecer suspeitos?", "Não. Os canais que as pessoas estão a descobrir ganham subscritores todos os dias; é essa a forma normal do crescimento. O que dá nas vistas são milhares a chegar numa hora."),
            ("O que acontece quando o mês acaba?", "O pacote renova-se e a campanha continua ao mesmo ritmo constante, a não ser que canceles. Cancelar trava o pagamento seguinte; o mês em curso continua até ao fim."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "monthly",
        "slug": "youtube/subscritores/mensais",
        "label": "Subscritores mensais no YouTube",
        "title": "Subscritores no YouTube ao mês, sem fidelização | Growsterr",
        "description": "Compra subscritores no YouTube ao mês: um pacote que traz pessoas reais ao teu canal, pago com cartão e que cancelas quando quiseres. Desde {from_price}.",
        "h1": ("Comprar subscritores no YouTube ao mês, ", "como os canais crescem de facto."),
        "intro": "Um pacote mensal é exatamente a forma como trabalhamos. Quando compras subscritores no YouTube ao mês connosco, o teu canal é mostrado a pessoas reais todos os dias, quem gosta dele subscreve, e o pacote renova-se todos os meses até decidires parar.",
        "hero": {"image": "youtube-subscribers", "alt": "Um canal de YouTube a ganhar novos subscritores mês após mês"},
        "sections": [
            {
                "h2": "Porquê uma subscrição e não um pacote único",
                "p": [
                    "Um canal não fica feito depois de uma rajada. Continuas a carregar vídeos, por isso continuas a precisar de que pessoas novas te encontrem. Um pacote mensal acompanha esse ritmo: cada vídeo novo chega a um público que ainda está a crescer.",
                    "Os pacotes únicos fazem o contrário. Entregam um número no primeiro dia e nada depois, e como nenhum público real aparece por encomenda, esse número é quase sempre de bots.",
                ],
            },
            {
                "h2": "Pagar mês a mês",
                "ul": [
                    "O pagamento é feito com cartão no checkout seguro da Stripe, ou com Apple Pay e Google Pay nos dispositivos compatíveis.",
                    "O pacote renova-se todos os meses a partir do dia em que começas.",
                    "Parar leva um clique na tua conta, e não é feito mais nenhum pagamento.",
                    "Podes subir de pacote quando os teus vídeos estiverem prontos para mais pessoas.",
                ],
            },
            {
                "h2": "O que se acumula mês após mês",
                "p": [
                    "Cada mês junta subscritores reais que ficam enquanto gostarem do teu canal. Ao fim de vários meses, isso torna-se uma base de pessoas que veem os teus vídeos, por isso cada vídeo novo começa com mais gente.",
                ],
                "image": {"image": "youtube-channel", "alt": "Um criador a planear os vídeos de YouTube do próximo mês num calendário de parede"},
            },
        ],
        "faqs": [
            ("É uma subscrição?", "Sim. Todos os pacotes são uma subscrição mensal, paga com cartão, Apple Pay ou Google Pay através da Stripe. Não há pacotes únicos."),
            ("Quanto junta cada mês, normalmente?", "O {starter_name} traz normalmente {starter_audience}, o {rising_name} {rising_audience} e o {pro_name} {pro_audience}. Cada mês varia um pouco, porque cada subscritor é uma pessoa a fazer uma escolha."),
            ("Posso cancelar depois do primeiro mês?", "Sim. Cancela na tua conta quando quiseres; o mês que já pagaste continua até ao último dia, e nada se renova depois disso."),
            ("Fico com os subscritores se cancelar?", "Ninguém sai por deixares de pagar: são pessoas, e continuam subscritas enquanto o teu canal lhes interessar. Cancelar acaba com as novas campanhas; não remove ninguém."),
            ("Com que posso pagar?", "Com cartão, ou com Apple Pay ou Google Pay quando o teu telemóvel os oferece. O meio que escolheres é cobrado de novo todos os meses até cancelares."),
            ("Posso começar pequeno e passar a um pacote maior?", "Sim. Começa onde o teu canal está hoje, muitas vezes com o {starter_name}, e sobe quando estiveres a publicar o suficiente para receber mais pessoas."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "no-drop",
        "slug": "youtube/subscritores/sem-quedas",
        "label": "Subscritores no YouTube sem quedas",
        "title": "Comprar subscritores YouTube sem quedas e sem bots | Growsterr",
        "description": "O número de subscritores cai quando eles nunca foram reais. Os nossos são pessoas que escolheram o teu canal, não contas à espera de limpeza. Desde {from_price}.",
        "h1": ("Comprar subscritores no YouTube sem quedas? ", "Começa com pessoas que escolheram o teu canal."),
        "intro": "Querer comprar subscritores no YouTube sem quedas costuma querer dizer que já viste um número cair. Os subscritores caem quando nunca foram pessoas: o YouTube limpa contas de spam e contas encerradas, e os subscritores bots vão com elas. Os nossos são espectadores reais que decidiram subscrever, o tipo de conta que uma limpeza deixa em paz.",
        "hero": {"image": "youtube-subscribers", "alt": "O número de subscritores de um canal de YouTube estável enquanto chegam novos subscritores reais"},
        "sections": [
            {
                "h2": "Porque cai o número de subscritores",
                "p": [
                    "O YouTube remove os subscritores que considera spam, além das contas que foram encerradas. Os canais que compraram subscritores bots veem esses números cair aos degraus, às vezes meses depois da compra.",
                    "A queda é a parte visível. A parte escondida é o tempo que essas contas passaram no teu canal sem nunca ver nada, a baixar a parte dos teus subscritores que interage.",
                ],
            },
            {
                "h2": "Porque é que uma reposição não é a solução",
                "p": [
                    "Alguns vendedores prometem repor tudo o que cair. Isso quer dizer substituir bots removidos por bots novos, o que mantém o número em cima e o problema vivo. Um subscritor real não precisa de ser substituído.",
                ],
            },
            {
                "h2": "Como é um \"sem quedas\" honesto",
                "p": [
                    "As pessoas reais podem cancelar a subscrição, como em qualquer canal, e com o tempo algumas vão fazê-lo. É a rotação normal, e é pequena ao lado das vagas que os bots deixam. O que fica é um público que ainda lá está quando publicas.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Subscritores de longa data a ver no sofá o vídeo mais recente de um criador"},
            },
        ],
        "faqs": [
            ("Algum dos meus novos subscritores vai sair?", "Alguns talvez, como acontece em todos os canais quando os gostos das pessoas mudam. O que não vais ter é um lote de contas falsas à espera de serem removidas todas juntas."),
            ("Há reposição se os subscritores caírem?", "Não, porque não há número falso para completar. Recebes um pacote mensal de pessoas reais; o que elas fazem depois é escolha delas, como em qualquer público."),
            ("Porque caiu o meu número depois de outro serviço?", "O mais provável é o YouTube ter removido contas que considerou spam, ou contas que tinham sido encerradas. Os subscritores bots tendem a ir em grandes lotes nessas limpezas."),
            ("Os subscritores bots podem prejudicar o canal mesmo depois de saírem?", "A remoção é o problema menor. Enquanto lá estiveram, nunca viram um único vídeo, o que fez o teu público parecer menos envolvido do que realmente era."),
            ("O meu painel bate certo com o número do YouTube?", "Não exatamente. O teu painel conta os novos subscritores que a nossa campanha trouxe; o total que o YouTube mostra inclui também o crescimento vindo de outros lados e quem cancelou a subscrição."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "organic",
        "slug": "youtube/subscritores/organicos",
        "label": "Subscritores orgânicos no YouTube",
        "title": "Subscritores orgânicos no YouTube: como funciona | Growsterr",
        "description": "Dá para comprar subscritores orgânicos no YouTube? Pagamos a apresentação com campanhas promovidas; a decisão de subscrever é do espectador. Desde {from_price}.",
        "h1": ("Comprar subscritores orgânicos no YouTube? ", "Pagamos a apresentação. Eles escolhem."),
        "intro": "Eis a resposta honesta para quem quer comprar subscritores orgânicos no YouTube: ninguém te pode vender uma decisão. O que pagamos é a apresentação. O teu canal é mostrado a pessoas reais através de campanhas promovidas na nossa rede de parceiros, e quem subscreve fá-lo porque quer.",
        "hero": {"image": "youtube-subscribers", "alt": "Novos subscritores a juntar-se a um canal de YouTube depois de descobrirem os seus vídeos"},
        "sections": [
            {
                "h2": "A linha entre o pago e o orgânico",
                "p": [
                    "Qualquer canal que faz publicidade paga pela atenção. O que acontece a seguir é orgânico ou não: uma pessoa vê, gosta do vídeo ou não, e subscreve ou segue em frente.",
                    "Mantemos essa linha limpa. Pagamos para pôr o teu canal à frente de pessoas todos os dias; nunca pagamos a ninguém para subscrever, nunca trocamos subscrições e nunca usamos contas que agem por encomenda.",
                ],
            },
            {
                "h2": "Como distinguir subscritores orgânicos dos outros",
                "ul": [
                    "Os nomes deles aparecem nos comentários do teu vídeo seguinte.",
                    "Os comentários deles soam a pessoas: perguntas, piadas, uma ou outra discordância.",
                    "Os novos subscritores chegam a par de visitas ao canal, nunca sem elas.",
                    "Ficam depois de a campanha acabar, porque nada os prendia lá.",
                ],
            },
            {
                "h2": "Orgânico não tem de querer dizer esperar",
                "p": [
                    "O crescimento orgânico é muitas vezes imaginado como anos à espera de um vídeo com sorte. Uma campanha promovida encurta a espera: pessoas reais veem o teu canal desde os primeiros dias. A única coisa que não pode encurtar é a decisão delas, e é essa a parte que vale a pena manter.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Alguém a tocar em subscrever num canal que encontrou nessa manhã, de café na mão"},
            },
        ],
        "faqs": [
            ("Se promovem o meu canal, o crescimento continua a ser orgânico?", "As subscrições são. Pagamos para que o teu canal seja mostrado; ninguém é pago nem recompensado por subscrever. Cada subscritor decidiu por si depois de ver os teus vídeos."),
            ("Usam redes de sub4sub ou de troca?", "Nunca. Quem subscreve para receber uma subscrição de volta não tem interesse nos teus vídeos e raramente os vê, e o YouTube conta essas trocas como interação falsa."),
            ("Quanto dá o crescimento orgânico num mês?", "O {pick_name} fica normalmente no intervalo de {pick_audience} por mês. Como cada subscritor é uma pessoa a escolher, isso é um intervalo e não uma contagem."),
            ("Os subscritores orgânicos vão ver os meus vídeos?", "Escolheram o teu canal depois de o verem, que é o melhor começo que um subscritor pode ter. Se veem cada vídeo depende do vídeo, como com toda a gente."),
            ("Tenho de fazer alguma coisa durante a campanha?", "Mantém o canal público e continua a publicar. Quanto mais os teus vídeos corresponderem ao que a página do canal promete, mais pessoas das que visitam decidem subscrever."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "real",
        "slug": "youtube/subscritores/reais",
        "label": "Subscritores reais no YouTube",
        "title": "Comprar subscritores reais no YouTube: como confirmar | Growsterr",
        "description": "Reais, genuínos, de alta qualidade: quatro sinais que podes confirmar em qualquer subscritor do YouTube, e como os nossos pacotes trazem quem os cumpre.",
        "h1": ("Comprar subscritores no YouTube, mas reais. ", "Eis como os reconhecer."),
        "intro": "Quando se compram subscritores no YouTube, \"reais\" é a palavra que se acrescenta depois de uma má experiência. Achamos que devia querer dizer algo que podes confirmar: uma pessoa que deu com o teu canal, decidiu que valia a pena subscrevê-lo e depois aparece nas tuas visualizações, gostos e comentários.",
        "hero": {"image": "youtube-subscribers", "alt": "A página de um canal de YouTube com subscritores reais e genuínos a chegar ao longo de um mês"},
        "sections": [
            {
                "h2": "Quatro sinais de que um subscritor é real",
                "p": [
                    "Alta qualidade, genuínos, reais: todos os vendedores usam estas palavras. Estes são os testes que os distinguem.",
                ],
                "ul": [
                    "Houve uma visita primeiro: alguém abriu o teu canal antes de subscrever.",
                    "Veem: as visualizações do teu vídeo seguinte sobem a par do número de subscritores.",
                    "Falam, em comentários que nenhum guião escreveria.",
                    "Vivem onde apontaste a campanha, no local que indicaste na encomenda.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Um novo subscritor a comentar com as suas palavras um vídeo de YouTube"},
            },
            {
                "h2": "Compara-nos com o YouTube Studio",
                "p": [
                    "A nossa versão da história é o teu painel Growsterr: visitas ao canal vindas da campanha e quem, entre essas pessoas, subscreveu. O YouTube Studio conta o mesmo mês do lado do YouTube. Lê os dois juntos ao longo de um mês: à medida que os subscritores chegam, os teus vídeos devem também ganhar visualizações e comentários de pessoas novas.",
                ],
            },
            {
                "h2": "O que os subscritores reais não podem fazer",
                "p": [
                    "As pessoas reais não se encomendam à hora, não se lhes diz o que comentar e não podem prometer ver todos os vídeos. Quem oferece essas coisas está a descrever algo que não são pessoas. Preferimos dizer-te os limites a vender-te um número.",
                ],
            },
        ],
        "faqs": [
            ("O que quer dizer \"alta qualidade\" nos subscritores do YouTube?", "Para nós, uma pessoa com conta própria que escolheu o teu canal e pode ver, pôr gosto e comentar. Fotos de perfil e antiguidade da conta falsificam-se facilmente; uma decisão real de subscrever, não."),
            ("Os vossos subscritores são pessoas genuínas ou contas que controlam?", "Pessoas genuínas. Não temos, não gerimos nem alugamos conta nenhuma. Mostramos o teu canal através de campanhas promovidas, e quem o vê decide."),
            ("Posso comprar subscritores reais no YouTube sem partilhar o meu acesso?", "Sim, e nunca o devias partilhar com ninguém. Precisamos do identificador do teu canal e de um canal público, mais nada."),
            ("Os subscritores reais vão pôr o meu canal a monetizar?", "Essa decisão é do YouTube, por isso nunca prometemos monetização nem horas de visualização. Os subscritores reais podem ver os teus vídeos, o que os bots nunca fazem, mas são os requisitos e a análise do próprio YouTube que decidem quem é monetizado."),
            ("Como é um mês de crescimento real?", "Com o {pick_name}, normalmente {pick_audience} novos subscritores, a chegar em pequenos números todos os dias. Um canal mais pequeno pode começar com o {starter_name}, a {starter_price} por mês."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "safe",
        "slug": "youtube/subscritores/seguros",
        "label": "Subscritores no YouTube de forma segura",
        "title": "Comprar subscritores YouTube, seguro e legítimo | Growsterr",
        "description": "É legítimo e seguro comprar subscritores no YouTube? Vê quem está por trás do serviço, o que pede e como chegam os subscritores. Eis as nossas respostas.",
        "h1": ("Comprar subscritores no YouTube de forma legítima? ", "Vê primeiro quem está por trás."),
        "intro": "Perguntas-te se dá para comprar subscritores no YouTube de forma legítima e segura? Para ser legítimo, um serviço deve passar três testes: uma empresa com nome, nada que toque no teu acesso e subscritores que sejam pessoas reais. A Growsterr é um produto da Sterr Agency, e eis como respondemos a cada um.",
        "hero": {"image": "youtube-subscribers", "alt": "O canal de YouTube de um criador a crescer em segurança com subscritores que são pessoas reais"},
        "sections": [
            {
                "h2": "A quem estás a pagar",
                "p": [
                    "Por trás da Growsterr está a Sterr Agency, registada como Sterr Technologies OÜ em Tallinn, na Estónia, com sede na Turquia. Pagas através do checkout seguro da Stripe, e a subscrição fica na tua própria conta, onde a podes cancelar.",
                ],
            },
            {
                "h2": "Como o teu canal fica protegido",
                "ul": [
                    "A tua palavra-passe do Google continua a ser só tua: nunca a pedimos, e ninguém da nossa parte inicia sessão no teu canal.",
                    "Ninguém é pago para subscrever, e não há trocas de subscrições.",
                    "Os subscritores chegam ao longo do mês, nunca num lote.",
                    "Os gostos e os comentários vêm dos próprios subscritores, por isso todos os números andam a par.",
                ],
                "image": {"image": "youtube-channel", "alt": "Um criador à secretária a ver as definições do seu canal de YouTube, com sessão iniciada só no seu dispositivo"},
            },
            {
                "h2": "Sinais de alarme em qualquer serviço de crescimento",
                "ul": [
                    "Pede o teu acesso, ou acesso à tua conta Google.",
                    "Promete um número exato de subscritores até uma data.",
                    "Vende subscritores, visualizações e gostos como pacotes separados ao milhar.",
                    "Não te sabe dizer de onde vêm os subscritores, nem mostrar o que mediu.",
                ],
            },
        ],
        "faqs": [
            ("É legítimo comprar subscritores no YouTube?", "Pagar por promoção é normal; qualquer canal que faz anúncios fá-lo. Pagar por interação falsa não é: bots, scripts e trocas de subscrições são o que o YouTube trata como spam. Nós só promovemos o teu canal a pessoas reais que decidem por si."),
            ("O YouTube pode banir o meu canal por isto?", "O YouTube atua contra a interação falsa, e é por isso que nunca a usamos. Não podemos falar pelas decisões do YouTube, mas pessoas a escolher o teu canal depois de o verem é como a promoção funciona em todo o lado."),
            ("O que tenho de entregar para começar?", "O identificador do teu canal, o local de onde deve vir o teu público e um cartão de pagamento para o pacote mensal. O teu canal tem de ser público para que as pessoas possam subscrever."),
            ("O meu pagamento está seguro?", "A Stripe processa todos os pagamentos, quer uses cartão, Apple Pay ou Google Pay. Os dados do teu cartão ficam com a Stripe, não connosco."),
            ("E se não for para mim?", "Cancela na tua conta quando quiseres. Não é feito nenhum pagamento novo depois disso, e o mês em curso continua até ao fim."),
        ],
    },
    # --- Visualizações --------------------------------------------------------------------
    {
        "service": "views",
        "slug": "youtube/visualizacoes",
        "label": "Visualizações no YouTube",
        "title": "Comprar visualizações no YouTube de pessoas reais | Growsterr",
        "description": "Queres comprar visualizações no YouTube? As nossas vêm de pessoas reais que decidem ver, num pacote mensal com subscritores, gostos e comentários. Desde {from_price}.",
        "h1": ("Comprar visualizações no YouTube? ", "Cada uma vem de uma pessoa."),
        "intro": "Se vieste comprar visualizações no YouTube, é assim que as nossas funcionam. Aqui não há um menu de quantidades de visualizações. Cada pacote apresenta o teu canal a pessoas reais todos os dias; elas carregam no play no que lhes interessa, e muitas acabam por pôr gosto, comentar e subscrever. As visualizações vêm com o pacote, e cada uma é uma pessoa.",
        "hero": {"image": "youtube-viewers", "alt": "Pessoas reais a carregar no play num vídeo de YouTube de um criador"},
        "sections": [
            {
                "h2": "Porque não há uma quantidade de visualizações nos nossos pacotes",
                "p": [
                    "Uma visualização é uma pessoa a decidir ver, e ninguém pode prometer quantas pessoas vão decidir isso. Quem vende um número exato de visualizações até uma hora marcada está a vender reproduções geradas por scripts ou bots.",
                    "O YouTube trata as visualizações inflacionadas artificialmente como spam: pode removê-las, e nunca contam para a monetização. Por isso vendemos aquilo por que podemos responder: uma campanha mensal que traz pessoas reais, com intervalos habituais para os subscritores, gostos e comentários que deixam.",
                ],
            },
            {
                "h2": "Videoclipes, playlists e vídeos longos",
                "p": [
                    "Promovemos o teu canal, não uma faixa. Os ouvintes que o descobrem escolhem as músicas que os prendem, e quem gosta de uma faixa pode continuar pelas tuas playlists; cada reprodução aí é deles.",
                ],
                "image": {"image": "youtube-channel", "alt": "Um músico a carregar um novo videoclipe no seu canal de YouTube"},
            },
            {
                "h2": "Antes de escolheres um site para comprar visualizações no YouTube",
                "ul": [
                    "Pergunta o que é para eles uma visualização: uma pessoa que decidiu ver, ou uma reprodução que geraram.",
                    "Confirma se as visualizações vêm sozinhas ou com subscritores, gostos e comentários das mesmas pessoas.",
                    "Procura um nome de empresa, um checkout a sério e uma forma de cancelar.",
                    "Afasta-te de quem te pedir a palavra-passe do Google.",
                ],
            },
        ],
        "faqs": [
            ("Posso encomendar visualizações sem um pacote?", "Não. Cada visualização que trazemos pertence a alguém que também pode subscrever, pôr gosto ou comentar, e é por isso que só vêm como parte de um pacote. Um número de visualizações que sobe enquanto nada mais mexe é o padrão do tráfego artificial."),
            ("Dizem-me quantas visualizações devo esperar?", "Não pomos número nas visualizações, porque cada uma é a escolha de uma pessoa. O que indicamos são intervalos mensais habituais: com o {pick_name}, {pick_audience} novos subscritores e {pick_likes} gostos, e essas pessoas veem antes de fazer uma coisa ou outra."),
            ("Há uma app para comprar visualizações no YouTube?", "Não usamos app. Escolhes um pacote no nosso site, pagas pela Stripe e acompanhas a campanha no painel da tua conta, a partir de qualquer navegador."),
            ("O que são visualizações \"premium\" no YouTube?", "Nada que o YouTube reconheça. O YouTube Premium é uma subscrição para espectadores, não um tipo de visualização que alguém te possa vender. As únicas visualizações que valem a pena são as de pessoas que carregaram no play por si."),
            ("Visualizações compradas podem pôr um vídeo viral?", "Ninguém pode prometer isso. Os espectadores reais dão a um vídeo mais gente que o pode partilhar, que é a versão honesta de uma hipótese de ficar viral."),
            ("As visualizações ajudam o meu canal a ser monetizado?", "Nem a monetização nem as horas de visualização são coisas que prometamos. As visualizações artificiais não contam de todo; os espectadores reais podem ver os teus vídeos, mas é o YouTube que decide quem é monetizado."),
        ],
    },
    {
        "service": "views",
        "modifier": "gradual",
        "slug": "youtube/visualizacoes/entrega-gradual",
        "label": "Visualizações no YouTube aos poucos",
        "title": "Visualizações lentas no YouTube, ao ritmo real | Growsterr",
        "description": "Visualizações no YouTube que crescem ao longo do mês: espectadores reais encontram o teu canal aos poucos, com subscritores e gostos. Desde {from_price}.",
        "h1": ("Comprar visualizações no YouTube devagar? ", "Os espectadores reais só chegam assim."),
        "intro": "Querer comprar visualizações no YouTube devagar é um bom instinto: um vídeo que ganha visualizações ao longo de dias é um vídeo que as pessoas estão a encontrar. Aqui ninguém precisa de ligar esse ritmo. Pessoas reais descobrem o teu canal todos os dias do mês e veem o que lhes interessa, por isso as tuas visualizações crescem como em qualquer canal em crescimento.",
        "hero": {"image": "youtube-viewers", "alt": "Espectadores a descobrir um canal de YouTube um a um ao longo de várias semanas"},
        "sections": [
            {
                "h2": "Um conta-gotas agendado não é a mesma coisa",
                "p": [
                    "Um conta-gotas agendado espalha reproduções geradas por uma semana em vez de uma hora. O contador sobe com mais calma, mas as reproduções continuam a vir sem ninguém a ver de verdade, sem gostos e sem subscritores. O YouTube olha para o que os espectadores fazem, não só para a velocidade a que apareceram.",
                ],
            },
            {
                "h2": "Os teus vídeos mais antigos também são vistos",
                "p": [
                    "Os espectadores que chegam ao longo de semanas não veem só o teu vídeo mais recente. Quem gosta de um vídeo pode abrir outro a partir da página do teu canal, por isso os vídeos antigos ganham visualizações ao mesmo ritmo tranquilo. Um conta-gotas apontado a um link não consegue isso.",
                ],
                "image": {"image": "youtube-channel", "alt": "A página de um canal de YouTube com uma grelha de vídeos antigos a ganhar novas visualizações"},
            },
            {
                "h2": "Um ritmo que podes acompanhar",
                "p": [
                    "O painel acompanha pessoas, não reproduções: visitas diárias ao teu canal vindas da campanha e os subscritores entre elas. As visualizações não estão lá, porque não as contamos antecipadamente; encontra-las no YouTube Studio, nos vídeos que as pessoas escolheram.",
                ],
            },
        ],
        "faqs": [
            ("Há um número diário de visualizações com que possa contar?", "Não há número diário para dar: cada visualização depende de alguém decidir ver. O que podes esperar são espectadores novos em todos os dias do mês, não um pico no primeiro dia."),
            ("Posso espalhar as visualizações por um número de dias à escolha?", "Cada campanha corre durante 30 dias e renova-se todos os meses. Dentro dessa janela, são as pessoas reais que definem o ritmo, por isso não agendamos visualizações por dia."),
            ("As visualizações lentas parecem mais naturais ao YouTube?", "A velocidade é só uma parte. O YouTube também vê se os espectadores continuam a ver, põem gosto no vídeo e voltam. As pessoas reais fazem isso a qualquer ritmo; as reproduções agendadas nunca."),
            ("E os vídeos que publiquei no ano passado?", "Também entram. Quem gosta de um vídeo tende a ver o que mais há no teu canal, e os vídeos antigos são muitas vezes onde vai parar a seguir."),
            ("E se quiser visualizações mais depressa?", "Escolhe um pacote maior, para que mais pessoas vejam o teu canal todos os dias. Tudo o que promete milhares de visualizações numa hora está a gerar reproduções, não a encontrar espectadores."),
        ],
    },
    {
        "service": "views",
        "modifier": "high-retention",
        "slug": "youtube/visualizacoes/alta-retencao",
        "label": "Visualizações no YouTube com alta retenção",
        "title": "Visualizações com alta retenção no YouTube? | Growsterr",
        "description": "Visualizações no YouTube com alta retenção não se compram: a retenção conquista-se com o vídeo. Trazemos espectadores reais que escolhem ver. Desde {from_price}.",
        "h1": ("Comprar visualizações no YouTube com alta retenção? ", "Traz pessoas que querem ver."),
        "intro": "Se queres comprar visualizações no YouTube com alta retenção, já sabes que o número de reproduções não é o que importa: queres espectadores que ficam. Mas a retenção não é algo que alguém possa vender. É o tempo que as pessoas reais decidem continuar a ver. A nossa parte é trazer espectadores que carregaram no play por escolha; quanto tempo ficam depende do teu vídeo.",
        "hero": {"image": "youtube-channel", "alt": "Um criador a editar um vídeo longo de YouTube para manter os espectadores a ver"},
        "sections": [
            {
                "h2": "A retenção que se compra é um temporizador",
                "p": [
                    "Quando um vendedor oferece visualizações com uma retenção definida, o que está por trás é um leitor programado para correr um número fixo de segundos. Vê da mesma forma, esteja o que estiver no ecrã, e nunca põe gosto, comenta ou subscreve. Por mais tempo que corra, é interação artificial, e o YouTube trata-a como spam.",
                ],
            },
            {
                "h2": "Porque é que os espectadores reais dão sentido à retenção",
                "p": [
                    "A retenção importa porque mostra que as pessoas que começaram um vídeo quiseram continuar a ver. Isso só vale quando foram elas a escolher o vídeo. Os espectadores reais dão-te dados de retenção honestos: onde ficam, onde desistem e o que os faz voltar.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Um espectador inclinado para a frente a ver um vídeo longo de YouTube até ao fim"},
            },
            {
                "h2": "O que faz subir a retenção, do teu lado",
                "ul": [
                    "Cumpre nos primeiros segundos o que o título e a miniatura prometem.",
                    "Corta a introdução lenta: mostra primeiro o essencial e explica depois.",
                    "Acrescenta capítulos aos vídeos longos, para que os espectadores saltem para o que procuram em vez de saírem.",
                    "Descobre no YouTube Studio onde os espectadores desistem e corrige esse momento no vídeo seguinte.",
                ],
            },
        ],
        "faqs": [
            ("Prometem uma percentagem de retenção ou horas de visualização?", "Não. A retenção e o tempo de visualização dependem do vídeo e de cada espectador. Trazemos pessoas reais que decidiram ver, e nunca pomos número no tempo que ficam."),
            ("As pessoas vão ver o meu vídeo inteiro?", "Algumas sim e outras não, e é exatamente isso que torna os dados delas úteis. O YouTube Studio mostra-te onde as pessoas ficam e onde saem."),
            ("Visualizações de alta retenção contam para a monetização?", "As visualizações artificiais não contam para a monetização de todo, seja qual for a retenção. O tempo de visualização dos espectadores reais é genuíno, mas nunca prometemos monetização; essa decisão é do YouTube."),
            ("A campanha pode levar espectadores a um vídeo?", "Podes indicar um vídeo, na encomenda ou mais tarde na tua conta, e é para lá que enviamos os novos espectadores. Não prometemos quanto tempo o veem: isso depende do vídeo, e o resto do teu canal fica à distância de um toque."),
            ("Que vídeos beneficiam mais?", "Os vídeos que cumprem a promessa. Um gancho claro, uma miniatura honesta e um ritmo constante transformam novos espectadores em visualizações longas, e quanto mais pessoas a campanha trouxer ao teu canal, mais delas esses vídeos podem prender."),
        ],
    },
    {
        "service": "views",
        "modifier": "live",
        "slug": "youtube/visualizacoes/em-direto",
        "label": "Visualizações em diretos no YouTube",
        "title": "Visualizações em direto no YouTube: um público real | Growsterr",
        "description": "Ninguém consegue encher um direto no YouTube com pessoas reais a uma hora marcada. Fazemos crescer os subscritores que podem entrar no próximo. Desde {from_price}.",
        "h1": ("Comprar visualizações para diretos no YouTube? ", "Cria o público que aparece."),
        "intro": "Se queres comprar visualizações para diretos no YouTube, queres uma transmissão que não pareça vazia quando carregas em começar. Ninguém consegue levar pessoas reais a um direto a um minuto marcado, e não dizemos que conseguimos. O que fazemos é fazer crescer o teu canal com subscritores reais todos os dias, para que cada direto tenha mais pessoas que possam entrar.",
        "hero": {"image": "youtube-channel", "alt": "Um criador prestes a entrar em direto no YouTube, com uma transmissão agendada no ecrã"},
        "sections": [
            {
                "h2": "Porque um contador de direto comprado sai pela culatra",
                "p": [
                    "O número de espectadores é a primeira coisa que qualquer pessoa vê num direto. Quando diz centenas e o chat está calado, todos os visitantes reais reparam. Os espectadores de direto comprados não escrevem, não reagem e não voltam para a gravação.",
                    "As regras do YouTube sobre visualizações falsas não fazem pausa quando entras em direto. Um contador em direto não é um sítio mais seguro para fingir.",
                ],
            },
            {
                "h2": "Quem entra num direto, e quando",
                "p": [
                    "As pessoas com mais probabilidade de entrar são subscritores que já conhecem o teu canal. Conforme as definições de cada um, o YouTube pode mostrar-lhes o teu direto no feed ou enviar uma notificação.",
                ],
                "ul": [
                    "Agenda o direto com antecedência, para que os subscritores possam ativar um lembrete.",
                    "Escolhe para o público um local onde a hora do teu direto calhe à noite.",
                    "Entra em direto num dia fixo, para que os espectadores saibam quando voltar.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Espectadores a entrar à noite, pelo telemóvel, num direto agendado no YouTube"},
            },
            {
                "h2": "A gravação continua a ganhar visualizações",
                "p": [
                    "Quando o direto acaba, fica no teu canal como vídeo. Os novos subscritores que o perderam em direto podem encontrar lá a gravação e vê-la quando lhes der jeito.",
                ],
            },
        ],
        "faqs": [
            ("Conseguem encher a minha transmissão enquanto estou em direto?", "Não. As pessoas reais veem quando escolhem, por isso não podemos prometer ninguém a uma dada hora. Fazemos crescer a base de subscritores de onde vêm os espectadores dos teus diretos."),
            ("O local que escolho importa para os diretos?", "Mais do que para os vídeos normais. Escolhe o sítio onde vive o teu público, e a hora do teu direto cai no dia deles e não a meio da noite."),
            ("A gravação vai ter visualizações da campanha?", "Pode ter. Uma gravação é um vídeo no teu canal, por isso os espectadores que te encontram depois do direto podem vê-la como qualquer outro vídeo."),
            ("Não podia simplesmente comprar espectadores de direto para o contador?", "Podias, mas sai pela culatra. Espectadores artificiais num direto são interação falsa como outra qualquer, e um contador cheio por cima de um chat vazio é fácil de detetar para os espectadores reais."),
            ("Que pacote serve um canal que faz diretos?", "O {pick_name} é o nosso mais popular, com normalmente {pick_audience} novos subscritores por mês; um canal mais recente pode começar com o {starter_name}. Cada direto a partir daí tem mais pessoas que podem entrar."),
        ],
    },
    {
        "service": "views",
        "modifier": "monthly",
        "slug": "youtube/visualizacoes/mensais",
        "label": "Visualizações mensais no YouTube",
        "title": "Visualizações para vários vídeos do YouTube, ao mês | Growsterr",
        "description": "Compra visualizações no YouTube para vários vídeos: um pacote mensal traz espectadores reais a todo o teu canal, e eles escolhem o que ver. Desde {from_price}.",
        "h1": ("Comprar visualizações no YouTube para vários vídeos, ", "mês após mês."),
        "intro": "Quando compras visualizações no YouTube para vários vídeos, o que queres mesmo é um canal ao qual as pessoas voltam. Um pacote mensal é feito exatamente para isso: pessoas reais descobrem o teu canal todos os dias e veem os vídeos que lhes interessam, e a campanha renova-se todos os meses, para que os novos vídeos continuem a encontrar novos espectadores.",
        "hero": {"image": "youtube-viewers", "alt": "Um espectador a passar de um vídeo de YouTube para o seguinte no mesmo canal"},
        "sections": [
            {
                "h2": "Um canal, muitos vídeos",
                "p": [
                    "Os espectadores interessados não ficam por um vídeo. Quem te encontra através de um tutorial abre o seguinte, e depois o que a página do teu canal sugerir. Uma campanha construída à volta do teu canal, e não de um único link, acompanha a forma como as pessoas veem de facto.",
                ],
            },
            {
                "h2": "Orientar para onde vão a seguir os novos espectadores",
                "p": [
                    "Promovemos o teu canal no seu todo; os espectadores decidem que vídeos abrem. O que controlas é o caminho que têm à frente quando chegam.",
                ],
                "ul": [
                    "Define um trailer do canal para os visitantes que ainda não subscreveram.",
                    "Põe o teu melhor vídeo em destaque no topo da página do canal.",
                    "Agrupa vídeos relacionados em playlists, para que um leve ao seguinte.",
                    "Acrescenta ecrãs finais que apontem para o vídeo que um espectador deve ver a seguir.",
                ],
            },
            {
                "h2": "Porque ao longo do tempo é melhor do que tudo de uma vez",
                "p": [
                    "As visualizações espalhadas por um mês chegam a cada vídeo enquanto é novo e mantêm vivos os mais antigos. Uma rajada única em vários vídeos faz o contrário: um pico em cada um, e depois silêncio.",
                ],
                "image": {"image": "youtube-channel", "alt": "Um criador a preparar uma série de vídeos de YouTube para publicar ao longo do mês"},
            },
        ],
        "faqs": [
            ("Para quantos vídeos podem ir as visualizações?", "Não há lista nem limite. Promovemos o teu canal, e os espectadores veem o que lhes interessar em qualquer parte dele."),
            ("Os vídeos novos publicados durante o mês têm visualizações?", "Sim. A campanha corre todos os dias, por isso um vídeo que publiques a meio do mês continua a encontrar pessoas novas, e os teus novos subscritores podem vê-lo como qualquer subscritor."),
            ("O preço é por vídeo?", "Não, é por mês para todo o teu canal: o {starter_name} custa {starter_price} por mês, o {rising_name} {rising_price} e o {pro_name} {pro_price}, tenhas os vídeos que tiveres. As visualizações vêm incluídas, com subscritores, gostos e comentários."),
            ("Posso parar ao fim de um mês?", "Sim. Cancela na tua conta; o mês pago termina normalmente e o seguinte não é cobrado."),
            ("As visualizações podem vir de uma só cidade?", "Sim. Uma só cidade funciona, tal como uma região ou um país inteiro. Isso serve canais com público local, como um guia gastronómico de uma cidade ou um canal de notícias locais."),
        ],
    },
    {
        "service": "views",
        "modifier": "no-drop",
        "slug": "youtube/visualizacoes/sem-quedas",
        "label": "Visualizações no YouTube sem quedas",
        "title": "Visualizações no YouTube sem quedas: porque caem | Growsterr",
        "description": "Porque é que as visualizações no YouTube caem depois de uma compra, e porque é diferente com pessoas que decidiram carregar no play. Desde {from_price} por mês.",
        "h1": ("Visualizações sem quedas no YouTube? ", "Começa por visualizações que nunca foram falsas."),
        "intro": "Quem quer comprar visualizações reais no YouTube sem quedas já viu, normalmente, um número cair. As visualizações caem quando o YouTube remove reproduções que considera artificiais. As nossas vêm de pessoas reais que decidiram carregar no play, dentro de um pacote mensal, por isso não há nenhum lote de reproduções falsas à espera de ser retirado.",
        "hero": {"image": "youtube-channel", "alt": "Um criador no estúdio a confirmar que o número de visualizações de um vídeo de YouTube se mantém"},
        "sections": [
            {
                "h2": "Porque cai o número de visualizações",
                "p": [
                    "O YouTube analisa as visualizações e remove as que não considera genuínas: reproduções de bots, scripts e outro tráfego artificial. Quando isso acontece depois de uma compra, o número cai, às vezes muito depois da entrega, e o histórico do vídeo mostra um pico seguido de uma queda.",
                ],
            },
            {
                "h2": "O que podemos e não podemos prometer",
                "p": [
                    "Não podemos prometer que o YouTube nunca vai ajustar um número; ele verifica todo o tráfego, incluindo o nosso. O que te podemos dizer é como as nossas visualizações acontecem: uma pessoa real vê o teu canal através de uma campanha promovida e decide ver. É esse o tipo de visualização que as verificações do YouTube existem para manter.",
                ],
            },
            {
                "h2": "Quando visualizações, gostos e subscritores sobem juntos",
                "p": [
                    "As visualizações reais raramente viajam sozinhas. Num pacote, vêm com novos subscritores, gostos e comentários das mesmas pessoas, por isso os teus números sobem juntos e nada neles parece fora do sítio, nem para o YouTube nem para um espectador.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Amigos a ver juntos um vídeo de YouTube e a pôr gosto quando acaba"},
            },
        ],
        "faqs": [
            ("As minhas visualizações vão alguma vez descer?", "O YouTube pode ajustar o número de qualquer vídeo quando analisa o tráfego, por isso ninguém pode prometer com honestidade um número que nunca mexe. As visualizações de pessoas que decidiram ver são o tipo que essa análise foi feita para manter."),
            ("Repõem as visualizações se o número cair?", "Não. Uma reposição troca reproduções falsas removidas por outras novas. Vendemos antes um pacote mensal de pessoas reais, por isso não há nada de artificial para substituir."),
            ("Porque caíram as minhas visualizações depois de uma compra anterior?", "Na maioria dos casos, porque o YouTube removeu reproduções que considerou artificiais. Isso pode acontecer semanas depois da entrega, e é por isso que uma queda pode apanhar-te de surpresa."),
            ("Posso comprar visualizações sem quedas para um só vídeo?", "Não como encomenda única. As visualizações vêm dentro de um pacote mensal que faz crescer todo o teu canal, por isso todos os vídeos podem beneficiar."),
            ("O que mais vem com as visualizações?", "São os próprios espectadores que trazem o resto. Com o {pick_name}, normalmente {pick_audience} subscritores, {pick_likes} gostos e {pick_comments} comentários por mês."),
        ],
    },
    {
        "service": "views",
        "modifier": "organic",
        "slug": "youtube/visualizacoes/organicas",
        "label": "Visualizações orgânicas e segmentadas no YouTube",
        "title": "Visualizações segmentadas no YouTube, por cidade | Growsterr",
        "description": "Compra visualizações segmentadas no YouTube na cidade, região ou país do teu público: espectadores orgânicos que decidiram ver, num pacote desde {from_price}.",
        "h1": ("Comprar visualizações segmentadas no YouTube, ", "do sítio onde vive o teu público."),
        "intro": "Para comprar visualizações segmentadas no YouTube, diz-nos onde devem estar os teus espectadores: uma cidade, uma região mais alargada ou um país inteiro. Mostramos o teu canal a pessoas reais lá através de campanhas promovidas, e as visualizações são orgânicas no sentido que importa: cada uma é alguém que decidiu ver.",
        "hero": {"image": "youtube-channel", "alt": "Um criador a filmar um vídeo de YouTube numa rua da cidade para um público local"},
        "sections": [
            {
                "h2": "Porque é que o local é a segmentação que conta",
                "p": [
                    "Um canal de culinária em Lisboa, um canal de imobiliário no Dubai, um canal de gaming em turco: cada um tem um público que vive num sítio e fala uma língua. Os espectadores desse sítio percebem os teus vídeos, voltam para o seguinte e podem tornar-se clientes se venderes alguma coisa.",
                    "Apontamos primeiro a tua campanha ao local que escolheres. Se o público mais parecido com o teu canal for um público maior logo do outro lado de uma fronteira, parte dos teus espectadores pode vir de lá.",
                ],
            },
            {
                "h2": "Segmentado não quer dizer forçado",
                "p": [
                    "Segmentamos onde as pessoas estão e depois deixamo-las decidir. Ninguém é obrigado a ver o teu vídeo, e nada é reproduzido sem ter sido escolhido. Uma visualização segmentada continua a ser uma escolha, e é isso que a torna orgânica.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Espectadores locais num café a ver um vídeo de YouTube feito na sua própria cidade"},
            },
            {
                "h2": "Como escolher o teu local",
                "ul": [
                    "Escolhe o sítio para onde os teus vídeos são feitos, não o maior sítio que consigas nomear.",
                    "Para um negócio local ou um canal de cidade, escolhe a própria cidade.",
                    "Para uma língua em vez de um sítio, escolhe o país onde vive a maioria de quem a fala.",
                    "Para um nicho internacional, começa pelo país cujos espectadores mais queres alcançar.",
                ],
            },
        ],
        "faqs": [
            ("Quão precisa é a segmentação?", "Tão precisa como uma cidade. Quanto mais pequeno o sítio, mais pequeno o público, por isso numa vila alguns espectadores podem vir da região à volta."),
            ("A segmentação torna as visualizações menos orgânicas?", "Não: a decisão de ver continua a ser deles. Pagamos para mostrar o teu canal no local que escolheste; cada espectador decide depois por si, e ninguém é recompensado por ver."),
            ("Os espectadores da minha cidade vão subscrever?", "Alguns vão, se o teu canal lhes falar. Com o {pick_name}, normalmente {pick_audience} novos subscritores por mês, do local que escolheste e arredores."),
            ("Porque não escolher a maior área possível?", "Uma área maior é uma base maior, mas os espectadores que não partilham a tua língua ou o teu contexto raramente ficam. O sítio certo é melhor do que o maior."),
            ("Precisam de acesso ao meu canal para segmentar espectadores?", "Não. A segmentação acontece nas nossas campanhas, não nas definições do teu canal. Precisamos do teu identificador e de um local, nunca da tua palavra-passe."),
        ],
    },
    {
        "service": "views",
        "modifier": "promote",
        "slug": "youtube/visualizacoes/promover",
        "label": "Promover os teus vídeos no YouTube",
        "title": "Visualizações no YouTube com AdWords? Como promovemos | Growsterr",
        "description": "A pensar em visualizações no YouTube com AdWords? Promovemos o teu canal a pessoas reais por ti, ao mês, com subscritores, gostos e comentários. Desde {from_price}.",
        "h1": ("Comprar visualizações no YouTube com AdWords? ", "Ou deixa-nos tratar da promoção."),
        "intro": "Quem quer comprar visualizações no YouTube com AdWords procura promover um vídeo com alcance pago. Os anúncios do próprio Google são uma forma: uma campanha que configuras, geres e pagas nas ferramentas de anúncios do Google. Nós somos outra. Promovemos o teu canal a pessoas reais todos os dias, através de campanhas na nossa rede de parceiros, e acompanhas os resultados no teu painel.",
        "hero": {"image": "youtube-viewers", "alt": "Pessoas a descobrir um vídeo de YouTube promovido no telemóvel e no tablet"},
        "sections": [
            {
                "h2": "Fazer anúncios tu mesmo, ou uma campanha gerida",
                "p": [
                    "Com o Google Ads, a ferramenta que substituiu o AdWords, és tu que montas a campanha: público, licitações, orçamento e o próprio anúncio. Pagas à medida que o sistema entrega, e acompanhá-lo é trabalho teu.",
                    "Um pacote Growsterr é a versão feita por nós. Dás-nos o identificador do teu canal e um local-alvo; a nossa equipa trata da promoção todos os dias, e o teu painel mostra as visitas ao canal e os novos subscritores. Um preço mensal, nenhuma licitação para gerir.",
                ],
            },
            {
                "h2": "Ao que uma visualização promovida deve levar",
                "p": [
                    "Uma visualização paga só compensa se o espectador fizer alguma coisa a seguir: ver outro vídeo, pôr gosto, subscrever. É por isso que os nossos pacotes giram à volta de subscritores, com gostos, comentários e visualizações das mesmas pessoas, e não de um número de reproduções.",
                ],
                "image": {"image": "youtube-channel", "alt": "Um criador a ver os novos subscritores de um vídeo de YouTube depois de uma promoção começar"},
            },
            {
                "h2": "O que não fazemos",
                "ul": [
                    "Não configuramos nem gerimos Google Ads, e nunca pedimos acesso à tua conta Google.",
                    "Não vendemos visualizações ao milhar nem a um preço por visualização.",
                    "Podes indicar um vídeo onde os novos espectadores chegam, mas não acertamos a promoção com a hora de um lançamento.",
                    "Não prometemos monetização, horas de visualização nem um lugar nas recomendações.",
                ],
            },
        ],
        "faqs": [
            ("É o mesmo que fazer anúncios no YouTube?", "Não. Os anúncios do YouTube correm na tua própria conta Google Ads, com o teu orçamento e as tuas definições. Nós promovemos o teu canal através da nossa rede de parceiros e gerimos a campanha por ti; nada corre na tua conta."),
            ("Podem gerir as minhas campanhas de Google Ads?", "Não é algo que ofereçamos. O nosso trabalho são pacotes mensais de crescimento; para algo maior, fala connosco por WhatsApp ou por email."),
            ("Em que é que o custo difere dos anúncios?", "Os anúncios cobram à medida que entregam, por isso o que gastas mexe com as tuas licitações e o teu orçamento. Os nossos pacotes têm um preço mensal fixo, {starter_price}, {rising_price} ou {pro_price}, com intervalos habituais de subscritores, gostos e comentários."),
            ("Posso fazer os meus próprios anúncios ao mesmo tempo?", "Sim. Os teus anúncios correm na tua conta e a nossa campanha corre na nossa rede, por isso uma coisa não atrapalha a outra."),
            ("Que vídeos promovem?", "O teu canal no seu todo, e os espectadores escolhem o que ver; podes indicar um vídeo para onde enviar quem chega. Pôr um lançamento ou uma nova série em destaque no teu canal ajuda os novos visitantes a encontrá-lo."),
        ],
    },
    {
        "service": "views",
        "modifier": "real",
        "slug": "youtube/visualizacoes/reais",
        "label": "Visualizações reais no YouTube",
        "title": "Comprar visualizações de qualidade no YouTube | Growsterr",
        "description": "Compra visualizações de qualidade no YouTube, de pessoas reais que decidiram ver, com subscritores, gostos e comentários dos mesmos espectadores. Desde {from_price}.",
        "h1": ("Comprar visualizações de qualidade no YouTube? ", "Uma pessoa por trás de cada play."),
        "intro": "Antes de comprares visualizações de qualidade no YouTube, convém definir qualidade. Para nós, uma visualização de qualidade tem uma pessoa por trás: alguém que viu o teu canal, escolheu um vídeo e o viu porque lhe interessava. É o único tipo que os nossos pacotes trazem, e as mesmas pessoas também subscrevem, põem gosto e comentam.",
        "hero": {"image": "youtube-viewers", "alt": "Um espectador real a escolher que vídeo ver no canal de YouTube de um criador"},
        "sections": [
            {
                "h2": "O que separa uma visualização real de uma reprodução",
                "ul": [
                    "Uma pessoa escolheu-a: ninguém foi pago nem programado para carregar no play.",
                    "Leva a algum lado: alguns espectadores põem gosto, comentam ou subscrevem.",
                    "Tem uma origem: o espectador vive onde apontaste a campanha.",
                    "Aguenta-se: não há nada de artificial nela que o YouTube tenha de remover.",
                ],
            },
            {
                "h2": "Porque é que visualizações de bots por escalões continuam sem qualidade",
                "p": [
                    "Alguns vendedores classificam as visualizações como padrão, alta qualidade ou premium. Seja qual for o rótulo, a pergunta que importa é a mesma: uma pessoa decidiu ver? Se não, um escalão mais alto só quer dizer um preço mais alto pela mesma reprodução vazia.",
                ],
            },
            {
                "h2": "Qualidade que se lê no YouTube Studio",
                "p": [
                    "As visualizações reais deixam rasto: tempo de visualização que varia de espectador para espectador, comentários que respondem ao teu vídeo e subscritores ganhos nos vídeos que as pessoas viram. Esse rasto é o que faz uma visualização valer a pena, e é o que as reproduções geradas nunca deixam.",
                ],
                "image": {"image": "youtube-channel", "alt": "Um criador a ler o tempo de visualização e os comentários de um vídeo de YouTube nas estatísticas"},
            },
        ],
        "faqs": [
            ("Em que é que uma visualização de qualidade difere de uma barata?", "Uma visualização barata é normalmente uma reprodução sem nada depois. Uma visualização de qualidade é uma pessoa que pode pôr gosto, comentar, subscrever ou voltar, e só esse tipo ajuda o teu canal."),
            ("Posso ver quem são os espectadores?", "O teu painel mostra as visitas ao canal e os novos subscritores da campanha, e o YouTube Studio mostra onde estão os espectadores e quanto tempo veem. Cada espectador, individualmente, continua privado, como em qualquer canal."),
            ("As visualizações vêm sem subscritores ou gostos?", "Não. Vêm num só pacote, das mesmas pessoas, e é isso que as torna crescimento e não um número."),
            ("Porque não há pacotes de mil visualizações?", "Porque mil visualizações por encomenda são mil reproduções que alguém gerou. Preferimos trazer pessoas e deixá-las escolher o que ver."),
            ("Posso escolher onde vivem os espectadores?", "Sim: diz-nos o local quando fizeres a encomenda, de uma só cidade a um país inteiro. Os espectadores locais percebem os teus vídeos, e é isso que faz as visualizações deles valerem mais do que um número."),
        ],
    },
    {
        "service": "views",
        "modifier": "safe",
        "slug": "youtube/visualizacoes/seguras",
        "label": "Visualizações no YouTube de forma segura",
        "title": "Comprar visualizações YouTube de forma segura | Growsterr",
        "description": "Queres comprar visualizações no YouTube de forma segura? O que o YouTube trata como falso, o que isso arrisca para o teu canal e como chegam espectadores reais.",
        "h1": ("Comprar visualizações no YouTube de forma legítima? ", "Sabe o que põe um canal em risco."),
        "intro": "Se queres comprar visualizações no YouTube de forma legítima e segura, começa pelo que o YouTube combate: visualizações de bots, scripts e qualquer tráfego que não seja uma pessoa a decidir ver. Ficamos do lado certo dessa linha porque só promovemos o teu canal a pessoas reais, que veem se quiserem.",
        "hero": {"image": "youtube-channel", "alt": "Um criador num escritório tranquilo em casa a rever o estado do seu canal de YouTube"},
        "sections": [
            {
                "h2": "O que o YouTube trata como visualizações falsas",
                "p": [
                    "As regras do YouTube sobre interação falsa abrangem tudo o que se segue. O YouTube pode remover as visualizações, e o conteúdo construído sobre elas pode ser retirado.",
                ],
                "ul": [
                    "Reproduções de bots ou scripts automáticos.",
                    "Visualizações de pessoas pagas ou recompensadas para ver.",
                    "Vídeos reproduzidos automaticamente sem que os espectadores os tenham escolhido.",
                    "Visualizações trocadas entre canais.",
                ],
            },
            {
                "h2": "Como chegam as nossas visualizações",
                "p": [
                    "A nossa rede de parceiros faz campanhas promovidas que põem o teu canal à frente de pessoas reais. Ninguém é pago para ver, nada é reproduzido sem ser escolhido e nada toca na tua conta do YouTube. Quem gosta do que encontra vê mais, põe gosto, comenta e subscreve.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Um espectador a escolher no telemóvel um vídeo de YouTube promovido"},
            },
            {
                "h2": "Seguro também para a tua conta",
                "ul": [
                    "Trabalhamos a partir do identificador público do teu canal: sem acessos, sem pedidos de permissão.",
                    "A faturação é uma subscrição mensal da Stripe que controlas na tua conta.",
                    "Terminá-la depende só de ti, a qualquer momento, sem perguntas.",
                ],
            },
        ],
        "faqs": [
            ("Comprar visualizações pode levar à remoção do meu vídeo?", "As visualizações falsas podem: o YouTube pode tirá-las do número, e o conteúdo que viola as regras sobre interação falsa pode ser retirado. As visualizações de pessoas que decidiram ver não são interação falsa."),
            ("Quem gere a Growsterr?", "A Sterr Agency, cuja empresa registada é a Sterr Technologies OÜ, em Tallinn, na Estónia. A sede da equipa fica na Turquia."),
            ("Precisam do meu acesso ao YouTube ou ao Google?", "Não, e um serviço que o peça já é um risco em si. Só precisamos do identificador público do teu canal."),
            ("Promover um vídeo é permitido no YouTube?", "Promover um vídeo para que as pessoas o descubram é normal; os canais fazem-no com anúncios todos os dias. A linha que o YouTube traça está nas visualizações artificiais ou incentivadas, e ficamos do lado certo dela."),
            ("E se não ficar satisfeito?", "Para a subscrição na tua conta e nenhum mês seguinte é cobrado. O teu painel mostra o que medimos, por isso podes avaliar a campanha com factos."),
        ],
    },
    {
        "service": "views",
        "modifier": "shorts",
        "slug": "youtube/visualizacoes/shorts",
        "label": "Visualizações em YouTube Shorts",
        "title": "Visualizações de reels no YouTube? São Shorts | Growsterr",
        "description": "No YouTube, os reels chamam-se Shorts. Trazemos espectadores reais que continuam a ver os teus Shorts, num pacote mensal com subscritores. Desde {from_price}.",
        "h1": ("Comprar visualizações de reels no YouTube? ", "Espectadores de Shorts que continuam a ver."),
        "intro": "Se queres comprar visualizações de reels no YouTube, estás a falar de Shorts: os vídeos curtos e verticais do YouTube. Não vendemos visualizações de Shorts em massa. Trazemos pessoas reais ao teu canal todos os dias, e quem gosta dos teus Shorts vê, volta a ver, põe gosto e às vezes subscreve.",
        "hero": {"image": "youtube-viewers", "alt": "Alguém a ver um YouTube Short no telemóvel e a deixá-lo repetir"},
        "sections": [
            {
                "h2": "Visualizações baratas de Shorts falsificam-se e detetam-se facilmente",
                "p": [
                    "Há visualizações baratas de Shorts em todo o lado porque uma reprodução se gera em segundos. O difícil é o que acontece depois da reprodução: o espectador continuou a ver, voltou a ver, pôs gosto, abriu o teu canal? As reproduções geradas respondem não a tudo, e o YouTube trata-as como spam.",
                ],
            },
            {
                "h2": "Como um espectador de Shorts se torna subscritor",
                "p": [
                    "Os Shorts são uma porta de entrada. Um espectador real que gosta de um pode tocar no teu nome, explorar o teu canal e subscrever, e a partir daí os teus vídeos mais longos também lhe podem chegar. É por esse caminho que uma visualização de Shorts de uma pessoa vale muito mais do que uma reprodução.",
                ],
                "image": {"image": "youtube-channel", "alt": "Um criador a rever no telemóvel um YouTube Short vertical antes de o publicar"},
            },
            {
                "h2": "Tirar mais partido dos Shorts que publicas",
                "ul": [
                    "Deixa os teus melhores Shorts fáceis de encontrar na página do canal, onde chegam os espectadores curiosos.",
                    "Liga um vídeo longo relacionado a partir do teu Short, para que quem se interessa tenha para onde ir.",
                    "Publica a um ritmo regular, para que os novos subscritores encontrem algo novo a cada visita.",
                ],
            },
        ],
        "faqs": [
            ("Os reels do YouTube são o mesmo que os Shorts?", "Sim. Reels é o nome do Instagram; no YouTube, o mesmo formato curto e vertical chama-se Shorts. Tudo o que está nesta página se aplica aos Shorts."),
            ("Posso comprar visualizações baratas para um Short?", "Não há preço por Short, e não vendemos visualizações para um Short em particular. Um pacote promove o teu canal, e os espectadores escolhem os Shorts que querem."),
            ("Conseguem pôr os meus Shorts no feed de Shorts?", "É uma promessa que ninguém pode fazer com honestidade, por isso não a fazemos. Trazemos espectadores reais; a forma como o YouTube espalha um Short depois disso é decisão dele."),
            ("Porque não indicam um número de visualizações de Shorts?", "Um Short pode ser repetido, saltado ou posto em ciclo, e um número de visualizações prometido antecipadamente só se cumpre gerando reproduções. Indicamos intervalos mensais habituais para o que as pessoas fazem depois de ver: subscrever, pôr gosto e comentar."),
            ("É seguro comprar visualizações em YouTube Shorts?", "A um serviço de bots, não: uma reprodução falsa é falsa quer o vídeo dure trinta segundos quer uma hora. Espectadores reais a escolher os teus Shorts são um público normal, seja qual for o formato que publicas."),
        ],
    },
]
