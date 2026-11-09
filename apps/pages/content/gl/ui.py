"""Galician UI of the money pages ("ti"). Mirrors en/ui.py key by key.

{profile} carries its own possessive ("o teu perfil" / "a túa canle", since canle is feminine):
use it only where no preposition precedes it (Galician contracts "a/de/en" with the article).
{content} is masculine on every platform ("os teus contidos", "os teus vídeos").
{follow} reads after "decidiu": "seguirte" / "subscribirse". Likes are "gústames".
"""

UI = {
    # Words that change with the platform or the service
    "audience": {"instagram": "seguidores", "tiktok": "seguidores", "youtube": "subscritores"},
    "follow": {"instagram": "seguirte", "tiktok": "seguirte", "youtube": "subscribirse"},
    "profile": {"instagram": "o teu perfil", "tiktok": "o teu perfil", "youtube": "a túa canle"},
    "handle": {"instagram": "nome de usuario", "tiktok": "nome de usuario", "youtube": "identificador da canle"},
    "content": {"instagram": "contidos", "tiktok": "vídeos", "youtube": "vídeos"},
    "service_names": {"followers": "Seguidores", "subscribers": "Subscritores", "likes": "Gústames",
                      "views": "Visualizacións", "comments": "Comentarios"},
    "service_words": {"followers": "seguidores", "subscribers": "subscritores", "likes": "gústames",
                      "views": "visualizacións", "comments": "comentarios"},

    # Page chrome
    "home": "Inicio",
    "crumbs_label": "Ruta de navegación",
    "eyebrow": "{platform} · {service_name}",
    "eyebrow_hub": "Crecemento en {platform}",
    "cta": "Comeza con {pick_name}",
    "cta_more": "Ver todos os paquetes",
    "trust": ["Persoas reais, nunca bots", "Nunca che pedimos o contrasinal", "Mensual, cancela cando queiras"],
    "product_name": "Paquetes de crecemento para {platform}",
    "sticky_cta": "Comezar",

    # Packages
    "packages_title": "Escolle o teu paquete",
    "packages_lead": "Tres paquetes mensuais. Novos {audience}, gústames, visualizacións e comentarios chegan xuntos, das mesmas persoas reais.",
    "packages_note": "Intervalos mensuais habituais, non unha cifra fixa: cada un dos teus novos {audience} é unha persoa real que decidiu {follow}, así que cada mes é un pouco diferente.",

    # What's included: the page's own service comes first, then the rest in this order.
    "included_title": "Que inclúe",
    "included_lead": "Cada paquete trae o conxunto completo, das mesmas persoas reais.",
    "included_items": {
        "audience": ("Novos {audience}", "Persoas reais que descubriron {profile} e decidiron {follow}. Normalmente {starter_audience} ao mes con {starter_name}."),
        "likes": ("Gústames das mesmas persoas", "Normalmente {starter_likes} ao mes con {starter_name}, nos {content} que máis lles gustan."),
        "comments": ("Comentarios coas súas palabras", "Normalmente {starter_comments} ao mes con {starter_name}. Escritos por persoas, nunca cun guión."),
        "views": ("Visualizacións incluídas", "As mesmas persoas miran os teus {content} pola súa conta. Non contamos as visualizacións por adiantado: detrás de cada unha hai unha persoa."),
        "days": ("Repartido en 30 días", "Un pouco cada día, desde a localización que escollas. Nunca todo de vez."),
        "dashboard": ("O teu panel", "O que medimos, día a día: as visitas da túa campaña e os novos {audience} que trouxeron."),
    },

    # How it works: the subscription, step by step
    "steps_title": "Como funciona",
    "steps_lead": "Unha subscrición mensual: ti escolles o paquete, nós levamos a campaña, as persoas reais deciden.",
    "steps": [
        ("Escolle un paquete", "{starter_name}, {rising_name} ou {pro_name}, con cobro mensual. Cancela cando queiras desde a túa conta."),
        ("Poñemos en marcha a túa campaña", "Dinos o teu {handle} de {platform} e de onde debe vir o teu público. Nunca che pedimos o contrasinal."),
        ("Persoas reais descobren {profile}", "Cada día amosamos {profile} a persoas reais. Quen goza do que ve decide pola súa conta {follow}, dar gústame e comentar."),
        ("O teu panel amosa o que medimos", "As visitas da túa campaña e os novos {audience} que trouxeron, día a día. Cifras medidas, nunca suposicións."),
    ],

    # Real people vs bots / instant
    "compare_title": "Persoas reais, non bots",
    "compare_lead": "Instantáneo significa bots: ningunha persoa real decide {follow} segundos despois dun pagamento.",
    "compare_cols": ("Que cambia", "Servizos instantáneos e bots", "Growsterr"),
    "compare": [
        ("Quen son", "Bots e perfís falsos", "Persoas reais que decidiron {follow}"),
        ("Velocidade", "Miles en minutos", "Un pouco cada día, todo o mes"),
        ("Gústames e comentarios", "Véndense á parte, de máis bots", "Das mesmas persoas, dentro do teu paquete"),
        ("O teu alcance", "Cae en silencio: un público que nunca interactúa dille a {platform} que non paga a pena amosar os teus {content}", "Medra con persoas que miran, dan gústame e volven"),
        ("O teu contrasinal", "Pídeno a miúdo", "Nunca"),
        ("O que ves", "Un número que pode desaparecer na próxima limpeza", "Un panel co que medimos"),
    ],

    # Quantity pages: how a monthly package gets you to the goal
    "quantity_title": "Como chegar a {quantity} {service}",
    "quantity_lead": "Non vendemos un lote fixo de {quantity}. As persoas reais deciden por si mesmas, así que un paquete mensual lévate ata alí a un ritmo natural.",
    "pace_title": "Ritmo habitual con {pick_name}",
    "pace_month": "Mes {n}",
    "pace_goal": "Obxectivo: {quantity}",
    "pace_note": "Intervalos habituais baseados no que fan persoas reais, nunca unha promesa. Algúns meses traen máis e outros menos.",
    "by_plan_title": "Tempo ata {quantity}, por paquete",
    "a_month": "{range} ao mes",
    "when_first": "normalmente xa no primeiro mes",
    "when_about": "normalmente uns {n} meses",
    "when_range": "normalmente {low}–{high} meses",
    "views_pace": "As visualizacións veñen das mesmas persoas reais que descobren {profile}, así que non as contamos por adiantado. {pick_name} é o paquete que mellor encaixa con este obxectivo.",

    # FAQ, related pages, closing
    "faq_title": "Preguntas e respostas",
    "related_title": "Segue explorando",
    "related": {
        "platform": "Máis sobre {platform}",
        "platforms": "Noutras plataformas",
        "quantities": "Outros obxectivos",
        "modifiers": "Outras formas de medrar",
        "articles": "Segue lendo",
        "hubs": "Medra con persoas reais en",
    },
    # The tools a page can carry ("tool"): they run in the browser, nothing is sent.
    "tools": {
        "calculate": "Calcular",
        "followers": "Seguidores",
        "avg_likes": "Gústames de media por publicación",
        "avg_comments": "Comentarios de media por publicación",
        "engagement_title": "A túa taxa de interacción",
        "engagement_lead": "Cantos dos teus seguidores reaccionan a unha publicación típica. Escribe as cifras das túas últimas publicacións.",
        "engagement_result": "A túa taxa de interacción é do {rate} %.",
        "engagement_note": "A taxa sobe cando ás persoas que te seguen lles importan de verdade as túas publicacións. Os seguidores que nunca reaccionan báixana, sexan cantos sexan.",
        "growth_title": "Canto falta para o teu obxectivo?",
        "growth_lead": "Escribe onde estás e onde queres chegar. Calculámolo co intervalo mensual habitual de cada paquete.",
        "current": "Seguidores hoxe",
        "goal": "O teu obxectivo",
        "when_first": "normalmente xa no primeiro mes",
        "when_range": "normalmente {low}–{high} meses",
        "when_about": "uns {n} meses",
        "reached": "Xa chegaches.",
        "growth_note": "Intervalos habituais, non unha promesa: as persoas reais deciden por si mesmas se te seguen.",
    },
    # Eyebrow above the headline of pages outside the platform x service grid (by "kind").
    "article_eyebrows": {
        "guide": "Guía",
        "alternative": "Comparativa",
        "payment": "Pagamentos",
        "agency": "Axencia de crecemento",
        "tool": "Ferramenta",
        "intent": "Resposta clara",
    },
    "cta_title": "Listo para medrar en {platform}?",
    "cta_text": "Escolle un paquete e poñemos en marcha a túa campaña. As persoas reais deciden o resto, e o teu panel amosa o que medimos.",

    # Platform hubs
    "services_title": "O que facemos medrar en {platform}",
    "services_lead": "Un só paquete tráeo todo, das mesmas persoas reais.",
    "teasers": {
        "audience": "Persoas reais que descobren {profile} e deciden {follow}.",
        "likes": "Gústames de persoas que gozan dos teus {content}.",
        "views": "Visualizacións de persoas que escollen mirar, nunca de scripts.",
        "comments": "Comentarios escritos por persoas reais, coas súas propias palabras.",
    },
    "explore": "Explorar",
    "in_package": "Incluído en cada paquete",
    "goals_title": "Máis formas de medrar en {platform}",
    "other_hubs_title": "Tamén te facemos medrar en",
}
