"""Spanish (Spain) UI of the money pages ("tú"). Mirrors en/ui.py key by key.

{follow} reads after "decidió": "seguirte" / "suscribirse". {content} is publicaciones (f) or
vídeos (m): write "tus {content}" and never an article or adjective that agrees with it.
"""

UI = {
    # Words that change with the platform or the service
    "audience": {"instagram": "seguidores", "tiktok": "seguidores", "youtube": "suscriptores"},
    "follow": {"instagram": "seguirte", "tiktok": "seguirte", "youtube": "suscribirse"},
    "profile": {"instagram": "perfil", "tiktok": "perfil", "youtube": "canal"},
    "handle": {"instagram": "nombre de usuario", "tiktok": "nombre de usuario", "youtube": "identificador del canal"},
    "content": {"instagram": "publicaciones", "tiktok": "vídeos", "youtube": "vídeos"},
    "service_names": {"followers": "Seguidores", "subscribers": "Suscriptores", "likes": "Likes",
                      "views": "Visualizaciones", "comments": "Comentarios"},
    "service_words": {"followers": "seguidores", "subscribers": "suscriptores", "likes": "likes",
                      "views": "visualizaciones", "comments": "comentarios"},

    # Page chrome
    "home": "Inicio",
    "crumbs_label": "Ruta de navegación",
    "eyebrow": "{platform} · {service_name}",
    "eyebrow_hub": "Crecimiento en {platform}",
    "cta": "Empieza con {pick_name}",
    "cta_more": "Ver todos los paquetes",
    "trust": ["Personas reales, nunca bots", "Nunca te pedimos la contraseña", "Mensual, cancela cuando quieras"],
    "product_name": "Paquetes de crecimiento para {platform}",
    "sticky_cta": "Empezar",

    # Packages
    "packages_title": "Elige tu paquete",
    "packages_lead": "Tres paquetes mensuales. Nuevos {audience}, likes, visualizaciones y comentarios llegan juntos, de las mismas personas reales.",
    "packages_note": "Rangos mensuales habituales, no una cifra fija: cada uno de tus nuevos {audience} es una persona real que decidió {follow}, así que cada mes es un poco distinto.",

    # What's included: the page's own service comes first, then the rest in this order.
    "included_title": "Qué incluye",
    "included_lead": "Cada paquete trae el conjunto completo, de las mismas personas reales.",
    "included_items": {
        "audience": ("Nuevos {audience}", "Personas reales que descubrieron tu {profile} y decidieron {follow}. Normalmente {starter_audience} al mes con {starter_name}."),
        "likes": ("Likes de las mismas personas", "Normalmente {starter_likes} al mes con {starter_name}: dan like a tus {content} cuando les gustan."),
        "comments": ("Comentarios con sus propias palabras", "Normalmente {starter_comments} al mes con {starter_name}. Escritos por personas, nunca con guion."),
        "views": ("Visualizaciones incluidas", "Las mismas personas ven tus {content} por su cuenta. No contamos las visualizaciones de antemano: detrás de cada una hay una persona."),
        "days": ("Repartido en 30 días", "Un poco cada día, desde la ubicación que elijas. Nunca todo de golpe."),
        "dashboard": ("Tu panel", "Lo que hemos medido, día a día: las visitas de tu campaña y los nuevos {audience} que trajeron."),
    },

    # How it works: the subscription, step by step
    "steps_title": "Cómo funciona",
    "steps_lead": "Una suscripción mensual: tú eliges el paquete, nosotros llevamos la campaña, las personas reales deciden.",
    "steps": [
        ("Elige un paquete", "{starter_name}, {rising_name} o {pro_name}, con cobro mensual. Cancela cuando quieras desde tu cuenta."),
        ("Ponemos en marcha tu campaña", "Dinos tu {handle} de {platform} y de dónde debe venir tu público. Nunca te pedimos la contraseña."),
        ("Personas reales descubren tu {profile}", "Cada día mostramos tu {profile} a personas reales. Quien disfruta de lo que ve decide por su cuenta {follow}, dar like y comentar."),
        ("Tu panel muestra lo que hemos medido", "Las visitas de tu campaña y los nuevos {audience} que trajeron, día a día. Cifras medidas, nunca suposiciones."),
    ],

    # Real people vs bots / instant
    "compare_title": "Personas reales, no bots",
    "compare_lead": "Instantáneo significa bots: ninguna persona real decide {follow} segundos después de un pago.",
    "compare_cols": ("Qué cambia", "Servicios instantáneos y bots", "Growsterr"),
    "compare": [
        ("Quiénes son", "Bots y perfiles falsos", "Personas reales que decidieron {follow}"),
        ("Velocidad", "Miles en minutos", "Un poco cada día, todo el mes"),
        ("Likes y comentarios", "Se venden aparte, de más bots", "De las mismas personas, dentro de tu paquete"),
        ("Tu alcance", "Cae sin avisar: un público que nunca interactúa le dice a {platform} que no merece la pena mostrar tus {content}", "Crece con personas que ven, dan like y vuelven"),
        ("Tu contraseña", "Te la suelen pedir", "Nunca"),
        ("Lo que ves", "Una cifra que puede desaparecer en la próxima limpieza", "Un panel con lo que hemos medido"),
    ],

    # Quantity pages: how a monthly package gets you to the goal
    "quantity_title": "Cómo llegar a {quantity} {service}",
    "quantity_lead": "No vendemos un lote fijo de {quantity}. Las personas reales deciden por sí mismas, así que un paquete mensual te lleva a tu meta a un ritmo natural.",
    "pace_title": "Ritmo habitual con {pick_name}",
    "pace_month": "Mes {n}",
    "pace_goal": "Meta: {quantity}",
    "pace_note": "Rangos habituales basados en lo que hacen personas reales, nunca una promesa. Algunos meses traen más y otros menos.",
    "by_plan_title": "Tiempo hasta {quantity}, por paquete",
    "a_month": "{range} al mes",
    "when_first": "normalmente en el primer mes",
    "when_about": "normalmente unos {n} meses",
    "when_range": "normalmente {low}–{high} meses",
    "views_pace": "Las visualizaciones vienen de las mismas personas reales que descubren tu {profile}, así que no las contamos de antemano. {pick_name} es el paquete que mejor encaja con esta meta.",

    # FAQ, related pages, closing
    "faq_title": "Preguntas frecuentes",
    "related_title": "Sigue explorando",
    "related": {
        "platform": "Más sobre {platform}",
        "platforms": "En otras plataformas",
        "quantities": "Otras metas",
        "modifiers": "Otras formas de crecer",
        "articles": "Sigue leyendo",
        "hubs": "Crece con personas reales en",
    },
    # The tools a page can carry ("tool"): they run in the browser, nothing is sent.
    "tools": {
        "calculate": "Calcular",
        "followers": "Seguidores",
        "avg_likes": "Likes medios por publicación",
        "avg_comments": "Comentarios medios por publicación",
        "engagement_title": "Tu tasa de interacción",
        "engagement_lead": "Cuántos de tus seguidores reaccionan a una publicación típica. Introduce las cifras de tus últimas publicaciones.",
        "engagement_result": "Tu tasa de interacción es del {rate} %.",
        "engagement_note": "La tasa sube cuando a las personas que te siguen les importan de verdad tus publicaciones. Los seguidores que nunca reaccionan la bajan, sean cuantos sean.",
        "growth_title": "¿Cuánto falta para tu meta?",
        "growth_lead": "Introduce dónde estás y adónde quieres llegar. Lo calculamos con el rango mensual habitual de cada paquete.",
        "current": "Seguidores hoy",
        "goal": "Tu meta",
        "when_first": "normalmente en el primer mes",
        "when_range": "normalmente {low}–{high} meses",
        "when_about": "unos {n} meses",
        "reached": "Ya has llegado.",
        "growth_note": "Rangos habituales, no una promesa: las personas reales deciden por sí mismas si te siguen.",
    },
    # Eyebrow above the headline of pages outside the platform x service grid (by "kind").
    "article_eyebrows": {
        "guide": "Guía",
        "alternative": "Comparativa",
        "payment": "Pagos",
        "agency": "Agencia de crecimiento",
        "tool": "Herramienta",
        "intent": "Respuesta clara",
    },
    "cta_title": "¿Listo para crecer en {platform}?",
    "cta_text": "Elige un paquete y ponemos en marcha tu campaña. Las personas reales deciden el resto, y tu panel muestra lo que hemos medido.",

    # Platform hubs
    "services_title": "Lo que hacemos crecer en {platform}",
    "services_lead": "Un solo paquete lo trae todo, de las mismas personas reales.",
    "teasers": {
        "audience": "Personas reales que descubren tu {profile} y deciden {follow}.",
        "likes": "Likes de personas a las que les gustan tus {content}.",
        "views": "Visualizaciones de personas que eligen ver, nunca de scripts.",
        "comments": "Comentarios escritos por personas reales, con sus propias palabras.",
    },
    "explore": "Explorar",
    "in_package": "Dentro de cada paquete",
    "goals_title": "Más formas de crecer en {platform}",
    "other_hubs_title": "También te hacemos crecer en",
}
