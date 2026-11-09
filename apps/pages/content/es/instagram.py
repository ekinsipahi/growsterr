"""Spanish (Spain) Instagram pages: the hub, followers, and the 1,000-followers goal.
Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "instagram",
        "label": "Instagram",
        "title": "Paquetes de crecimiento para Instagram | Growsterr",
        "description": "Crece en Instagram con personas reales: paquetes mensuales con nuevos seguidores, likes y comentarios de gente que decidió seguirte. Desde {from_price} al mes.",
        "h1": ("Haz crecer tu Instagram ", "con personas reales."),
        "intro": "Paquetes de crecimiento mensuales para creadores e influencers. Mostramos tu perfil a personas reales, y quienes disfrutan de lo que ven te siguen, dan like y comentan. Tu panel muestra lo que hemos medido, día a día.",
        "hero": {"image": "instagram-hub", "alt": "El perfil de Instagram de un creador recibiendo nuevos seguidores, likes y comentarios"},
        "sections": [
            {
                "h2": "Un crecimiento que parece merecido, porque lo es",
                "p": [
                    "Instagram premia las cuentas con las que la gente interactúa de verdad. Los bots hacen lo contrario: se quedan en tu número de seguidores, nunca dan like, nunca miran y le enseñan al algoritmo que no merece la pena mostrar tus publicaciones.",
                    "Nosotros lo hacemos al revés. Cada día mostramos tu perfil a personas reales, y cada nuevo seguidor es una decisión. Por eso los likes, las visualizaciones y los comentarios llegan con tus seguidores, no como una compra aparte.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Personas reales descubren las publicaciones de Instagram de un creador y dejan comentarios"},
            },
            {
                "h2": "Para creadores que publican con intención",
                "p": [
                    "Marca personal, página de nicho o pequeño negocio: los paquetes crecen contigo. Empieza con {starter_name} y sube de paquete cuando tu contenido esté listo para más.",
                ],
                "ul": [
                    "Reels, carruseles y fotos se benefician por igual.",
                    "Nos dices la ciudad, la región o el país del que debe venir tu público.",
                    "Tu cuenta sigue siendo tuya: nunca te pedimos la contraseña.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "Un creador planifica contenido de Instagram en su escritorio"},
            },
        ],
        "faqs": [
            ("¿Los seguidores son personas reales?", "Sí. Cada seguidor es una persona real que vio tu perfil y decidió seguirte. Nunca usamos bots, perfiles falsos ni entregas instantáneas."),
            ("¿Cuántos seguidores trae un paquete?", "Normalmente {starter_audience} nuevos seguidores al mes con {starter_name}, {rising_audience} con {rising_name} y {pro_audience} con {pro_name}. Son rangos habituales, no una cifra fija: las personas reales deciden por sí mismas."),
            ("¿Necesitáis mi contraseña de Instagram?", "Nunca. Solo necesitamos tu nombre de usuario. Mantén tu cuenta pública para que quienes la descubran puedan seguirte."),
            ("¿Puedo comprar likes o comentarios por separado?", "No. Los likes, las visualizaciones y los comentarios vienen dentro de cada paquete, de las mismas personas reales que te siguen. Eso es lo que mantiene tus cifras naturales."),
            ("¿Puedo cancelar cuando quiera?", "Sí. Los paquetes se renuevan cada mes y puedes cancelar desde tu cuenta. El mes que ya pagaste sigue hasta el final."),
        ],
    },
    {
        "service": "followers",
        "slug": "instagram/seguidores",
        "label": "Seguidores de Instagram",
        "title": "Seguidores reales de Instagram, cada mes | Growsterr",
        "description": "Seguidores de Instagram que son personas reales y decidieron seguirte, con likes y comentarios de las mismas personas. Paquetes mensuales desde {from_price}.",
        "h1": ("Seguidores de Instagram ", "que decidieron seguirte."),
        "intro": "Cada día, personas reales descubren tu perfil, y quienes disfrutan de lo que ven te siguen. Normalmente {starter_audience} nuevos seguidores al mes con {starter_name}, con likes y comentarios de las mismas personas.",
        "hero": {"image": "instagram-followers", "alt": "Un perfil de Instagram ganando nuevos seguidores de personas reales"},
        "sections": [
            {
                "h2": "Por qué los seguidores reales valen más",
                "p": [
                    "Un seguidor solo cuenta si hay una persona detrás. Los seguidores reales ven tu próxima publicación, le dan like, la comentan y la comparten, y esa interacción es lo que Instagram mira para decidir a quién más mostrar tu contenido.",
                    "Los bots no hacen nada de eso. Inflan una cifra unos días, desaparecen en la siguiente limpieza y los que se quedan reducen tu alcance sin hacer ruido.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Personas reales dan like y comentan una publicación de Instagram de un creador"},
            },
            {
                "h2": "De dónde vienen tus nuevos seguidores",
                "p": [
                    "Dinos la ciudad, la región o el país del que debe venir tu público. Mostramos tu perfil primero a personas reales de allí; donde el público más afín es mayor en la zona cercana, pueden llegar más desde allí.",
                ],
            },
            {
                "h2": "Cómo es un mes",
                "ul": [
                    "Primeros días: tu campaña arranca y llegan las primeras visitas.",
                    "Cada semana: nuevos seguidores, likes y comentarios, unos pocos cada día.",
                    "Al final del mes: normalmente {pick_audience} nuevos seguidores con {pick_name}.",
                ],
            },
        ],
        "faqs": [
            ("¿Con qué rapidez llegan los seguidores?", "Un poco cada día, durante todo el mes. Nunca todo de golpe: las personas reales siguen a su ritmo, y todo lo instantáneo es un bot."),
            ("¿Dejarán de seguirme mis nuevos seguidores?", "Algunos puede que sí, igual que cambia cualquier público real. Los seguidores reales se quedan mucho más que los bots, que desaparecen en oleadas."),
            ("¿También recibo likes y comentarios?", "Sí, de las mismas personas: normalmente {pick_likes} likes y {pick_comments} comentarios al mes con {pick_name}."),
            ("¿Es seguro para mi cuenta?", "Nunca te pedimos la contraseña ni entramos en tu cuenta. Las personas encuentran tu perfil y deciden por sí mismas, igual que te encuentra cualquier seguidor."),
            ("¿Puedo elegir de dónde son mis seguidores?", "Sí. Indica la ciudad, la región o el país al hacer el pedido. Apuntamos primero allí; si cerca hay un público muy afín y más grande, parte de tus seguidores puede venir de esa zona."),
        ],
    },
    {
        "service": "followers",
        "quantity": 1000,
        "slug": "instagram/seguidores/1000",
        "label": "{quantity} seguidores de Instagram",
        "title": "{quantity} seguidores de Instagram, personas reales | Growsterr",
        "description": "Llega a {quantity} seguidores de Instagram con personas reales, no bots. {pick_name} trae normalmente {pick_audience} al mes, con likes y comentarios.",
        "h1": ("{quantity} seguidores de Instagram, ", "todos reales."),
        "intro": "No vendemos un lote de {quantity} bots. Hacemos crecer tu cuenta con personas reales: {pick_name} trae normalmente {pick_audience} nuevos seguidores al mes, así que {quantity} suele estar a tu alcance en el primer mes.",
        "hero": {"image": "instagram-followers-1000", "alt": "Una línea ascendente de nuevos seguidores de Instagram que alcanza un primer hito"},
        "sections": [
            {
                "h2": "¿Por qué no {quantity} seguidores en una hora?",
                "p": [
                    "Porque ninguna persona real sigue una cuenta segundos después de un pago. Los servicios que entregan {quantity} seguidores en una hora entregan bots: no dan like, no comentan y desaparecen en oleadas.",
                    "Los que se quedan hacen aún más daño. Cada seguidor que nunca interactúa reduce la parte de tu público que sí lo hace, y tus publicaciones llegan a menos gente sin que lo notes.",
                ],
            },
            {
                "h2": "Tus primeros mil, bien hechos",
                "p": [
                    "Tus primeros mil seguidores reales cambian cómo te ven los nuevos visitantes. Son personas que pueden ver tus Reels, dar like a tus publicaciones y volver, y eso es justo lo que ayuda a que los siguientes mil te encuentren.",
                ],
                "ul": [
                    "Personas reales que decidieron seguirte, desde la ubicación que elijas.",
                    "Likes y comentarios de las mismas personas, dentro del paquete.",
                    "Un panel que muestra lo que hemos medido, día a día.",
                ],
            },
        ],
        "faqs": [
            ("¿Cuánto se tarda en llegar a {quantity} seguidores reales?", "A un ritmo habitual, {pick_name} trae {pick_audience} nuevos seguidores al mes, así que {quantity} suele alcanzarse en el primer mes. Las personas reales siguen a su ritmo, así que cada mes es un poco distinto."),
            ("¿Es un lote único de {quantity}?", "No. Vendemos crecimiento en paquetes mensuales. {pick_name} cuesta {pick_price} al mes y puedes cancelar cuando quieras desde tu cuenta."),
            ("¿Recibo likes y comentarios con ellos?", "Sí, de las mismas personas reales: normalmente {pick_likes} likes y {pick_comments} comentarios al mes con {pick_name}."),
            ("¿Qué pasa después de {quantity}?", "Tu paquete sigue activo hasta que lo canceles, así que tu crecimiento continúa mes a mes. Cuando tu contenido esté listo para más, puedes subir de paquete."),
        ],
    },
]
