"""European Portuguese UI of the money pages ("tu"). Mirrors en/ui.py key by key.

{follow} reads after "decidiu": "seguir-te" / "subscrever o teu canal". {content} is masculine
on every platform ("os teus conteúdos", "os teus vídeos"), so articles agree.
Likes are "gostos" (the word Instagram and Facebook use in Portugal).
"""

UI = {
    # Words that change with the platform or the service
    "audience": {"instagram": "seguidores", "tiktok": "seguidores", "youtube": "subscritores"},
    "follow": {"instagram": "seguir-te", "tiktok": "seguir-te", "youtube": "subscrever o teu canal"},
    "profile": {"instagram": "perfil", "tiktok": "perfil", "youtube": "canal"},
    "handle": {"instagram": "nome de utilizador", "tiktok": "nome de utilizador", "youtube": "identificador do canal"},
    "content": {"instagram": "conteúdos", "tiktok": "vídeos", "youtube": "vídeos"},
    "service_names": {"followers": "Seguidores", "subscribers": "Subscritores", "likes": "Gostos",
                      "views": "Visualizações", "comments": "Comentários"},
    "service_words": {"followers": "seguidores", "subscribers": "subscritores", "likes": "gostos",
                      "views": "visualizações", "comments": "comentários"},

    # Page chrome
    "home": "Início",
    "crumbs_label": "Navegação estrutural",
    "eyebrow": "{platform} · {service_name}",
    "eyebrow_hub": "Crescimento no {platform}",
    "cta": "Começa com o {pick_name}",
    "cta_more": "Ver todos os pacotes",
    "trust": ["Pessoas reais, nunca bots", "Nunca pedimos a tua palavra-passe", "Mensal, cancela quando quiseres"],
    "product_name": "Pacotes de crescimento para {platform}",
    "sticky_cta": "Começar",

    # Packages
    "packages_title": "Escolhe o teu pacote",
    "packages_lead": "Três pacotes mensais. Novos {audience}, gostos, visualizações e comentários chegam juntos, das mesmas pessoas reais.",
    "packages_note": "Intervalos mensais habituais, não uma quantidade fixa: cada um dos teus novos {audience} é uma pessoa real que decidiu {follow}, por isso cada mês é um pouco diferente.",

    # What's included: the page's own service comes first, then the rest in this order.
    "included_title": "O que está incluído",
    "included_lead": "Cada pacote traz o quadro completo, das mesmas pessoas reais.",
    "included_items": {
        "audience": ("Novos {audience}", "Pessoas reais que descobriram o teu {profile} e decidiram {follow}. Normalmente {starter_audience} por mês com o {starter_name}."),
        "likes": ("Gostos das mesmas pessoas", "Normalmente {starter_likes} por mês com o {starter_name}, nos {content} de que mais gostam."),
        "comments": ("Comentários com as suas palavras", "Normalmente {starter_comments} por mês com o {starter_name}. Escritos por pessoas, nunca por guião."),
        "views": ("Visualizações incluídas", "As mesmas pessoas veem os teus {content} por iniciativa própria. Não contamos visualizações antecipadamente: cada uma é uma pessoa."),
        "days": ("Distribuído por 30 dias", "Um pouco todos os dias, a partir da localização que escolheres. Nunca tudo de uma vez."),
        "dashboard": ("O teu painel", "O que medimos, dia a dia: as visitas vindas da tua campanha e os novos {audience} que trouxeram."),
    },

    # How it works: the subscription, step by step
    "steps_title": "Como funciona",
    "steps_lead": "Uma subscrição mensal: tu escolhes o pacote, nós gerimos a campanha, as pessoas reais decidem.",
    "steps": [
        ("Escolhe um pacote", "{starter_name}, {rising_name} ou {pro_name}, com faturação mensal. Cancela quando quiseres na tua conta."),
        ("Lançamos a tua campanha", "Diz-nos o teu {handle} do {platform} e de onde deve vir o teu público. Nunca pedimos a tua palavra-passe."),
        ("Pessoas reais descobrem o teu {profile}", "Todos os dias mostramos o teu {profile} a pessoas reais. Quem gosta do que vê decide, por si, {follow}, pôr gosto e comentar."),
        ("O teu painel mostra o que medimos", "As visitas vindas da tua campanha e os novos {audience} que trouxeram, dia a dia. Números medidos, nunca suposições."),
    ],

    # Real people vs bots / instant
    "compare_title": "Pessoas reais, não bots",
    "compare_lead": "Instantâneo significa bots: nenhuma pessoa real decide {follow} segundos depois de um pagamento.",
    "compare_cols": ("O que muda", "Serviços instantâneos e bots", "Growsterr"),
    "compare": [
        ("Quem são", "Bots e perfis falsos", "Pessoas reais que decidiram {follow}"),
        ("Velocidade", "Milhares em minutos", "Um pouco todos os dias, o mês inteiro"),
        ("Gostos e comentários", "Vendidos à parte, de mais bots", "Das mesmas pessoas, dentro do teu pacote"),
        ("O teu alcance", "Cai em silêncio: um público que nunca interage diz ao {platform} que os teus {content} não merecem ser mostrados", "Cresce com pessoas que veem, põem gosto e voltam"),
        ("A tua palavra-passe", "Pedida muitas vezes", "Nunca"),
        ("O que vês", "Um número que pode desaparecer na próxima limpeza", "Um painel com o que medimos"),
    ],

    # Quantity pages: how a monthly package gets you to the goal
    "quantity_title": "Como chegar a {quantity} {service}",
    "quantity_lead": "Não vendemos um lote fixo de {quantity}. As pessoas reais decidem por si, por isso um pacote mensal leva-te lá a um ritmo natural.",
    "pace_title": "Ritmo habitual com o {pick_name}",
    "pace_month": "Mês {n}",
    "pace_goal": "Objetivo: {quantity}",
    "pace_note": "Intervalos habituais com base no que pessoas reais fazem, nunca uma promessa. Alguns meses trazem mais, outros menos.",
    "by_plan_title": "Tempo até {quantity}, por pacote",
    "a_month": "{range} por mês",
    "when_first": "normalmente logo no primeiro mês",
    "when_about": "normalmente cerca de {n} meses",
    "when_range": "normalmente {low}–{high} meses",
    "views_pace": "As visualizações vêm das mesmas pessoas reais que descobrem o teu {profile}, por isso não as contamos antecipadamente. O {pick_name} é o pacote que melhor se ajusta a este objetivo.",

    # FAQ, related pages, closing
    "faq_title": "Perguntas e respostas",
    "related_title": "Continua a explorar",
    "related": {
        "platform": "Mais sobre o {platform}",
        "platforms": "Noutras plataformas",
        "quantities": "Outros objetivos",
        "modifiers": "Outras formas de crescer",
        "articles": "Lê também",
        "hubs": "Cresce com pessoas reais no",
    },
    # The tools a page can carry ("tool"): they run in the browser, nothing is sent.
    "tools": {
        "calculate": "Calcular",
        "followers": "Seguidores",
        "avg_likes": "Média de gostos por publicação",
        "avg_comments": "Média de comentários por publicação",
        "engagement_title": "A tua taxa de envolvimento",
        "engagement_lead": "Quantos dos teus seguidores reagem a uma publicação típica. Introduz os números das tuas últimas publicações.",
        "engagement_result": "A tua taxa de envolvimento é de {rate}%.",
        "engagement_note": "A taxa sobe quando as pessoas que te seguem se interessam mesmo pelas tuas publicações. Seguidores que nunca reagem fazem-na descer, sejam quantos forem.",
        "growth_title": "Quanto tempo até ao teu objetivo?",
        "growth_lead": "Introduz onde estás e onde queres chegar. Fazemos as contas com o intervalo mensal habitual de cada pacote.",
        "current": "Seguidores hoje",
        "goal": "O teu objetivo",
        "when_first": "normalmente logo no primeiro mês",
        "when_range": "normalmente {low}–{high} meses",
        "when_about": "cerca de {n} meses",
        "reached": "Já lá estás.",
        "growth_note": "Intervalos habituais, não uma promessa: as pessoas reais decidem por si se te seguem.",
    },
    # Eyebrow above the headline of pages outside the platform x service grid (by "kind").
    "article_eyebrows": {
        "guide": "Guia",
        "alternative": "Comparação",
        "payment": "Pagamentos",
        "agency": "Agência de crescimento",
        "tool": "Ferramenta",
        "intent": "Resposta direta",
    },
    "cta_title": "Pronto para crescer no {platform}?",
    "cta_text": "Escolhe um pacote e nós lançamos a tua campanha. As pessoas reais decidem o resto, e o teu painel mostra o que medimos.",

    # Platform hubs
    "services_title": "O que fazemos crescer no {platform}",
    "services_lead": "Um só pacote traz tudo, das mesmas pessoas reais.",
    "teasers": {
        "audience": "Pessoas reais que descobrem o teu {profile} e decidem {follow}.",
        "likes": "Gostos de pessoas que apreciam os teus {content}.",
        "views": "Visualizações de pessoas que escolhem ver, nunca de scripts.",
        "comments": "Comentários escritos por pessoas reais, com as suas próprias palavras.",
    },
    "explore": "Explorar",
    "in_package": "Incluído em todos os pacotes",
    "goals_title": "Mais formas de crescer no {platform}",
    "other_hubs_title": "Também te fazemos crescer no",
}
