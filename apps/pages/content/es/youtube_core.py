"""Spanish (Spain) YouTube pages beyond the hub and subscribers: likes, views and the ways people
ask for subscribers (reales, seguros, mensuales...). Keys and placeholders: docs/CONTENT.md. Brief:
docs/keywords/WRITING.md. Views are never counted in advance; we never promise monetization,
watch hours or retention."""

UPDATED = "2026-11-08"

PAGES = [
    # --- Likes ----------------------------------------------------------------------------
    {
        "service": "likes",
        "slug": "youtube/likes",
        "label": "Likes de YouTube",
        "title": "Comprar likes en YouTube de espectadores reales | Growsterr",
        "description": "¿Buscas comprar likes en YouTube? Cada like de nuestros paquetes viene de un espectador que miró, junto con suscriptores y comentarios. Desde {from_price} al mes.",
        "h1": ("¿Quieres comprar likes en YouTube? ", "Consíguelos de personas que vieron el vídeo."),
        "intro": "Si has venido a comprar likes en YouTube, primero una respuesta directa: no vendemos likes en lotes. Cada paquete lleva a tu canal personas reales que ven tus vídeos y dan like a los que les gustan, normalmente {starter_likes} likes al mes con {starter_name} y más con los paquetes mayores.",
        "hero": {"image": "youtube-viewers", "alt": "Espectadores dan like en el móvil a un vídeo de YouTube que acaban de ver"},
        "sections": [
            {
                "h2": "Lo que un like le dice a YouTube",
                "p": [
                    "Un like es un pequeño voto público de alguien que pulsó play. YouTube lo lee junto con todo lo demás que hizo ese espectador: cuánto tiempo miró, si se suscribió, si volvió para el siguiente vídeo.",
                    "Un like de una cuenta que nunca miró rompe ese patrón. El contador bajo tu vídeo sube mientras todo lo que lo rodea sigue plano, y YouTube trata como spam la interacción que considera artificial.",
                ],
            },
            {
                "h2": "Dónde caen los likes: vídeos, música y publicaciones",
                "p": [
                    "Los nuevos espectadores dan like a lo que les gusta, normalmente a tus últimos vídeos y al que los trajo a tu canal. Los músicos ven lo mismo en videoclips y vídeos con letra: likes de oyentes que reprodujeron el tema y querían más.",
                    "Las publicaciones de la comunidad funcionan distinto. Tus suscriptores las ven en su feed y pueden darles like por su cuenta, pero los rangos que damos son likes en tus vídeos.",
                ],
                "image": {"image": "youtube-channel", "alt": "Un músico graba una canción en su estudio en casa para un videoclip de YouTube"},
            },
            {
                "h2": "Por qué los likes llegan con suscriptores",
                "p": [
                    "Un like es lo más ligero que puede hacer un espectador. En un paquete llega con señales de más peso de las mismas personas: una suscripción, un comentario, una vuelta para el siguiente vídeo. Cuando esas cifras suben juntas, describen un canal que la gente disfruta, porque eso es lo que es.",
                ],
            },
        ],
        "faqs": [
            ("¿Puedo comprar likes de YouTube sin suscriptores?", "No. Los likes vienen dentro de cada paquete, junto con nuevos suscriptores y comentarios de las mismas personas reales. Un like sin nadie mirando detrás es el tipo de interacción que YouTube trata como spam."),
            ("¿Cuántos likes trae un mes habitual?", "Con {pick_name}, normalmente {pick_likes}, más o menos dos o tres likes por cada nuevo suscriptor. Las personas reales deciden a qué dar like, así que no hay dos meses iguales."),
            ("¿Puedo conseguir likes en una publicación de la comunidad de YouTube?", "No como pedido aparte. Tus nuevos suscriptores pueden ver tus publicaciones de la comunidad en su feed, y algunos les darán like porque quieren. Los rangos habituales de cada paquete cuentan likes en vídeos."),
            ("¿Los videoclips también reciben likes?", "Sí. Si tu canal es de música, las personas que traemos son oyentes que reprodujeron tus temas y dieron like a los que les gustaron. Puedes dirigir la campaña a la ciudad, la región o el país donde están tus oyentes."),
            ("¿Qué vídeos míos recibirán likes?", "Eligen los espectadores reales, así que suelen ser tus vídeos más recientes y el que los trajo primero a tu canal."),
            ("¿Cuándo aparecen los primeros likes?", "En los primeros días de tu campaña, cuando llegan los primeros espectadores, y después unos pocos cada día durante el resto del mes."),
        ],
    },
    {
        "service": "likes",
        "modifier": "comment-likes",
        "slug": "youtube/likes/likes-en-comentarios",
        "label": "Likes en comentarios de YouTube",
        "title": "¿Comprar likes para comentarios de YouTube? | Growsterr",
        "description": "¿Likes para comentarios de YouTube? No subimos un comentario concreto. Los espectadores reales leen los hilos de tus vídeos y dan like a lo que comparten.",
        "h1": ("¿Likes para comentarios de YouTube? ", "Crea una sección de comentarios que merezca likes."),
        "intro": "Quien compra likes para comentarios de YouTube suele querer subir un comentario a lo más alto. No vendemos eso. Llevamos espectadores reales a tu canal, y quienes leen los comentarios de tus vídeos dan like a las respuestas, preguntas y bromas que les llegan, incluido tu comentario fijado.",
        "hero": {"image": "youtube-viewers", "alt": "Un espectador recorre los comentarios de un vídeo de YouTube y da like a una respuesta"},
        "sections": [
            {
                "h2": "Un comentario en lo más alto no es el objetivo",
                "p": [
                    "Un comentario con cientos de likes bajo un vídeo que apenas se movió llama la atención de cualquiera que lea el hilo. Los likes en comentarios son interacción como cualquier otra, así que los likes de scripts también caen bajo las normas de spam de YouTube.",
                    "Y si el comentario está bajo el vídeo de otro creador, subirlo no es algo que hagamos en absoluto. Hacemos crecer tu propio canal, con personas que lo eligen.",
                ],
            },
            {
                "h2": "Cómo cobra vida una sección de comentarios",
                "p": [
                    "Los espectadores reales leen los comentarios después de ver el vídeo. Responden, dan like a los comentarios con los que están de acuerdo y dejan los suyos: normalmente {pick_comments} comentarios nuevos al mes con {pick_name}, escritos por personas y no por scripts.",
                ],
                "ul": [
                    "Fija un comentario que haga a los espectadores una pregunta de verdad. Las respuestas abren sus propios hilos.",
                    "Responde a los primeros comentarios de un vídeo nuevo. Un creador en el hilo atrae a más gente.",
                    "Marca con un corazón los comentarios que te gustan. Los espectadores se dan cuenta y vuelven a conversar.",
                ],
                "image": {"image": "youtube-channel", "alt": "Un creador fija una pregunta en los comentarios de un vídeo nuevo de YouTube"},
            },
            {
                "h2": "Lo que cuenta el paquete y lo que no",
                "p": [
                    "Los suscriptores, los likes en vídeos y los comentarios tienen rangos mensuales habituales. Los likes en comentarios no: ocurren cuando un espectador está de acuerdo con otro, y nadie puede programar eso.",
                ],
            },
        ],
        "faqs": [
            ("¿Podéis añadir likes a mi comentario en el vídeo de otro canal?", "No. Hacemos crecer tu propio canal con personas reales que lo eligen. Subir un comentario bajo el vídeo de otra persona no forma parte de lo que hacemos."),
            ("¿Los likes en comentarios vienen con el paquete?", "Vienen como en cualquier canal con vida: de espectadores reales que leen los hilos de tus vídeos. No los contamos por adelantado, porque cada uno es una persona que está de acuerdo con alguien."),
            ("¿Mis secciones de comentarios tendrán de verdad más movimiento?", "A medida que llega gente, sí: normalmente {starter_comments} comentarios nuevos al mes con {starter_name}, {rising_comments} con {rising_name} y {pro_comments} con {pro_name}, de las mismas personas que se suscriben."),
            ("¿Los comentarios los escriben bots o una IA?", "No. Cada comentario viene de una persona que vio tu vídeo y tenía algo que decir. Nunca guionizamos comentarios ni los escribimos por nadie."),
            ("¿Podéis enviar likes a un comentario de mi propio vídeo?", "No. Promocionamos tu canal, y los espectadores deciden qué comentarios merecen un like, incluidos los tuyos. Un comentario fijado que pregunta algo de verdad es el que más probabilidades tiene de reunirlos."),
            ("¿Es arriesgado comprar likes para comentarios de YouTube?", "A un servicio de bots, sí: los likes en comentarios son interacción, y YouTube trata la interacción artificial como spam. Los likes de personas que de verdad leen el hilo son la vida normal de un canal."),
        ],
    },
    {
        "service": "likes",
        "modifier": "live",
        "slug": "youtube/likes/directos",
        "label": "Likes en directos de YouTube",
        "title": "¿Comprar likes para directos de YouTube? | Growsterr",
        "description": "Antes de comprar likes para directos de YouTube: en una emisión vienen de quien está en el chat. Hacemos crecer los suscriptores reales que pueden entrar.",
        "h1": ("¿Comprar likes para directos de YouTube? ", "Vienen de la gente de tu chat."),
        "intro": "Antes de comprar likes para directos de YouTube, piensa en quién pulsa el botón: las personas que están viendo tu emisión. No podemos meter likes en una emisión en un minuto concreto, y no vamos a fingir que sí. Hacemos crecer los suscriptores reales que pueden ver que estás en directo y deciden entrar.",
        "hero": {"image": "youtube-channel", "alt": "Un creador emite en directo en YouTube desde un escritorio con cámara y micrófono"},
        "sections": [
            {
                "h2": "Un like en directo es una reacción, no una cifra",
                "p": [
                    "Durante una emisión, los likes llegan cuando pasa algo en pantalla: una jugada decisiva, una buena respuesta, la canción que pidió el chat. Son el público reaccionando en el momento.",
                    "Los likes de cuentas que no están mirando no reaccionan a nada. Caen en bloque junto a un chat callado, y cualquier persona real que entra ve que una cosa no encaja con la otra.",
                ],
            },
            {
                "h2": "Convertir los mejores momentos de una emisión en likes",
                "ul": [
                    "Pide likes una vez, en un momento álgido, no en el primer minuto.",
                    "Di en voz alta los nombres del chat: a la gente le gustan las emisiones de las que se siente parte.",
                    "Fija un comentario que explique a los que llegan tarde qué está pasando, para que se queden lo bastante para reaccionar.",
                    "Deja publicada la repetición, para que quien se perdió la emisión pueda verla y darle like.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Personas chatean y reaccionan en el chat en directo de YouTube mientras habla el creador"},
            },
            {
                "h2": "Haz crecer el público antes de la próxima emisión",
                "p": [
                    "Los suscriptores que traemos son personas reales que encontraron tu canal y decidieron quedarse. Algunas estarán en tu próximo chat, cuando les venga bien. Cuanto mayor sea ese grupo, más personas habrá para reaccionar cuando pase algo bueno en la emisión.",
                ],
            },
        ],
        "faqs": [
            ("¿Podéis enviar likes durante mi directo?", "No. Las personas reales tienen sus propios horarios, así que nadie honesto puede prometer reacciones a una hora concreta. Lo que hacemos crecer es el público que podría estar viéndote cuando emites."),
            ("¿Mis nuevos suscriptores verán mis directos?", "Algunos, los días que les venga bien. Eligieron tu canal después de verlo, así que tus emisiones pueden llegarles; que entren es decisión suya."),
            ("¿Se puede dar like a un directo después de que termine?", "Sí. La repetición se queda en tu canal como un vídeo, y cualquiera que la vea después puede darle like."),
            ("¿Por qué no comprar likes en directo a un servicio de bots?", "Porque una emisión es donde la interacción falsa se detecta con más facilidad. Cientos de likes junto a un chat en silencio le dicen a todo el que entra que la sala no es lo que parece."),
            ("¿Cuánto puede crecer el público de mis directos?", "Depende de tus emisiones, pero la base crece cada día: {pick_name} suma normalmente {pick_audience} suscriptores en un mes, y cada uno es alguien que podría estar en el chat la próxima vez."),
        ],
    },
    {
        "service": "likes",
        "modifier": "shorts",
        "slug": "youtube/likes/shorts",
        "label": "Likes en YouTube Shorts",
        "title": "Comprar likes en YouTube Shorts, de verdad | Growsterr",
        "description": "Likes en YouTube Shorts de personas reales que dejaron de deslizar, nunca de bots. Vienen en un paquete mensual con suscriptores y comentarios, desde {from_price}.",
        "h1": ("¿Comprar likes en YouTube Shorts? ", "Gánatelos de gente que dejó de deslizar."),
        "intro": "En el feed de Shorts, un like significa que alguien dejó de deslizar lo suficiente como para que le importara. Si quieres comprar likes en YouTube Shorts, ese es el único tipo que merece la pena: likes de personas reales que llevamos a tu canal cada día, que miran, dan like y a veces se suscriben.",
        "hero": {"image": "youtube-viewers", "alt": "Personas ven YouTube Shorts en el móvil y pulsan like"},
        "sections": [
            {
                "h2": "Lo que vale un like en Shorts",
                "p": [
                    "Los Shorts se reproducen en un feed por el que la gente pasa rápido. Un like ahí viene de un espectador que dejó correr tu Short, a menudo más de una vez, y decidió que se merecía un toque.",
                    "Los likes generados se saltan todo eso. Se amontonan en un Short que nadie siguió viendo, que es lo contrario de lo que se supone que dice un like.",
                ],
            },
            {
                "h2": "Qué hace que un Short merezca un like",
                "ul": [
                    "Empieza por lo mejor. El primer segundo decide si la gente se queda.",
                    "Haz que el final enlace con el principio, para que volver a verlo resulte natural.",
                    "Subtitula tus Shorts: mucha gente desliza sin sonido.",
                    "Termina con un motivo claro para visitar tu canal.",
                ],
                "image": {"image": "youtube-channel", "alt": "Un creador graba un Short vertical de YouTube con el móvil a la distancia del brazo"},
            },
            {
                "h2": "Lo que hace el paquete por tus Shorts",
                "ul": [
                    "Promocionamos tu canal; los espectadores que lo descubren eligen los Shorts y vídeos que quieren ver.",
                    "{pick_name} suma normalmente {pick_likes} likes en un mes, repartidos entre lo que la gente disfrutó.",
                    "Dinos la ciudad, la región o el país, para que tus Shorts lleguen a personas del lugar para el que los haces.",
                ],
            },
        ],
        "faqs": [
            ("¿Puedo tener likes en un solo Short?", "No como pedido suelto. Los likes llegan dentro de un paquete mensual, repartidos entre los Shorts y vídeos que gustan a la gente, junto con suscriptores y comentarios."),
            ("¿Los likes en Shorts ayudan a mis vídeos largos?", "De forma indirecta. Algunas personas que disfrutan de un Short abren el canal que hay detrás, y unas pocas acaban viendo tus vídeos más largos y suscribiéndose."),
            ("¿Con qué rapidez llegan los likes a mis Shorts?", "Desde los primeros días de tu campaña, y después unos pocos cada día a lo largo del mes. Miles de likes en Shorts en menos de una hora vienen de bots, no de espectadores."),
            ("¿Quién da like a mis Shorts?", "Personas que se encontraron con tu canal gracias a nuestra campaña, en la ubicación que elegiste. Decidieron mirar y decidieron dar like; nadie se lo pidió."),
            ("¿La gente también comentará mis Shorts?", "Algunos lo harán. En todo tu canal, {pick_name} trae normalmente {pick_comments} comentarios al mes, cada uno escrito por la persona que lo dejó."),
        ],
    },
    # --- Suscriptores ---------------------------------------------------------------------
    {
        "service": "subscribers",
        "modifier": "gradual",
        "slug": "youtube/suscriptores/progresivos",
        "label": "Suscriptores de YouTube progresivos",
        "title": "Comprar suscriptores de YouTube poco a poco | Growsterr",
        "description": "Suscriptores de YouTube poco a poco y sin parar: personas reales que se suscriben de pocas en pocas, cada día del mes, a su ritmo. Desde {from_price} al mes.",
        "h1": ("¿Comprar suscriptores de YouTube poco a poco? ", "Es el único ritmo que siguen las personas."),
        "intro": "Si quieres comprar suscriptores de YouTube poco a poco y de forma constante, pides lo correcto. Aquí, lo lento es simplemente lo que hace la gente: descubre tu canal el día que sea, ve un vídeo o dos y decide. Con {pick_name}, eso suma un habitual de {pick_audience} a lo largo del mes.",
        "hero": {"image": "youtube-subscribers", "alt": "La cifra de suscriptores de un canal de YouTube sube un poco cada día a lo largo de un mes"},
        "sections": [
            {
                "h2": "Los bots lentos siguen siendo bots",
                "p": [
                    "Algunos servicios venden una opción de goteo: los mismos suscriptores bot, soltados de pocos en pocos para que la curva parezca suave. Cambia el ritmo; lo que hay detrás, no. Las cuentas que nunca miran siguen reduciendo la parte de tus suscriptores que interactúa.",
                    "Progresivo significa algo cuando viene de personas que deciden una a una. Ningún ajuste puede imitarlo, y no hace falta ninguno.",
                ],
            },
            {
                "h2": "Cómo se ve lo constante en tu panel",
                "p": [
                    "Abre tu panel cualquier día y verás dos líneas: las personas que visitaron tu canal a través de la campaña y cuántas de ellas se suscribieron. Unos días tienen más movimiento que otros, como cualquier canal que la gente está descubriendo. Lo que no verás es un salto de miles de la noche a la mañana.",
                ],
            },
            {
                "h2": "Por qué en YouTube lo constante gana a lo repentino",
                "p": [
                    "Un canal que gana suscriptores cada semana, junto con visualizaciones y comentarios, es un canal que la gente está descubriendo. Cada nuevo vídeo llega a un grupo algo mayor de personas reales, y eso se va sumando con los meses.",
                ],
                "image": {"image": "youtube-channel", "alt": "Un creador de YouTube revisa en el portátil un mes de crecimiento constante del canal"},
            },
        ],
        "faqs": [
            ("¿Cómo de lento es lento?", "Repartido: un puñado de nuevos suscriptores casi todos los días, nunca un lote. En 30 días eso suma el rango habitual del paquete, y cada día es un poco distinto."),
            ("¿Puedo elegir con qué rapidez llegan los suscriptores?", "No por horas, porque eso lo marcan las personas reales. Tú eliges el paquete: uno mayor muestra tu canal a más gente cada día."),
            ("¿Un goteo lento es más seguro para mi canal?", "Solo si los suscriptores son reales. Un goteo lento de bots sigue siendo interacción falsa, mientras que personas reales que se suscriben a su ritmo son crecimiento normal."),
            ("¿Los suscriptores diarios parecerán sospechosos?", "No. Los canales que la gente descubre ganan suscriptores cada día; esa es la forma normal del crecimiento. Lo que llama la atención es que lleguen miles en una hora."),
            ("¿Qué pasa cuando termina el mes?", "El paquete se renueva y la campaña sigue al mismo ritmo constante, salvo que canceles. Cancelar detiene el siguiente pago; tu mes en curso sigue hasta el final."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "monthly",
        "slug": "youtube/suscriptores/mensuales",
        "label": "Suscriptores de YouTube mensuales",
        "title": "Comprar suscriptores de YouTube cada mes | Growsterr",
        "description": "Compra suscriptores de YouTube cada mes: un paquete que lleva personas reales a tu canal todo el mes, con pago con tarjeta y cancelable cuando quieras.",
        "h1": ("Comprar suscriptores de YouTube cada mes, ", "como crecen de verdad los canales."),
        "intro": "Un paquete mensual es exactamente como trabajamos. Cuando nos compras suscriptores de YouTube cada mes, tu canal se muestra a personas reales todos los días, quienes disfrutan de él se suscriben, y el paquete se renueva cada mes hasta que decidas parar.",
        "hero": {"image": "youtube-subscribers", "alt": "Un canal de YouTube gana nuevos suscriptores mes tras mes"},
        "sections": [
            {
                "h2": "Por qué una suscripción y no un lote único",
                "p": [
                    "Un canal no está terminado después de un empujón. Sigues subiendo vídeos, así que sigues necesitando que gente nueva te encuentre. Un paquete mensual sigue ese ritmo: cada vídeo nuevo llega a un público que todavía está creciendo.",
                    "Los lotes únicos hacen lo contrario. Entregan una cifra el primer día y nada después, y como ningún público real aparece por encargo, esa cifra casi siempre son bots.",
                ],
            },
            {
                "h2": "Pagar mes a mes",
                "ul": [
                    "El pago es con tarjeta en la pasarela segura de Stripe, o con Apple Pay y Google Pay en los dispositivos compatibles.",
                    "El paquete se renueva cada mes a partir del día en que empiezas.",
                    "Parar lleva un clic en tu cuenta, y no se cobra ningún pago más.",
                    "Puedes subir de paquete cuando tus vídeos estén listos para más gente.",
                ],
            },
            {
                "h2": "Lo que se va acumulando mes a mes",
                "p": [
                    "Cada mes suma suscriptores reales que se quedan mientras disfruten de tu canal. En varios meses eso se convierte en una base de personas que ven lo que subes, así que cada nuevo vídeo empieza con más de ellas.",
                ],
                "image": {"image": "youtube-channel", "alt": "Un creador planifica en un calendario de pared los vídeos de YouTube del mes siguiente"},
            },
        ],
        "faqs": [
            ("¿Es una suscripción?", "Sí. Cada paquete es una suscripción mensual, pagada con tarjeta, Apple Pay o Google Pay a través de Stripe. No hay lotes únicos."),
            ("¿Qué suele sumar cada mes?", "{starter_name} trae normalmente {starter_audience}, {rising_name} {rising_audience} y {pro_name} {pro_audience}. Cada mes varía un poco, porque cada suscriptor es una persona que toma una decisión."),
            ("¿Puedo cancelar después del primer mes?", "Sí. Cancela desde tu cuenta en cualquier momento; el mes que ya has pagado sigue hasta su último día, y después no se renueva nada."),
            ("¿Conservo mis suscriptores si cancelo?", "Nadie se va porque dejes de pagar: son personas, y siguen suscritas mientras tu canal les interese. Cancelar termina las nuevas campañas; no elimina a nadie."),
            ("¿Con qué puedo pagar?", "Con tarjeta, o con Apple Pay o Google Pay si tu móvil los ofrece. El método que elijas se vuelve a cobrar cada mes hasta que canceles."),
            ("¿Puedo empezar con poco y pasar a un paquete mayor?", "Sí. Empieza donde está hoy tu canal, a menudo con {starter_name}, y sube cuando publiques lo suficiente para recibir a más gente."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "no-drop",
        "slug": "youtube/suscriptores/permanentes",
        "label": "Suscriptores de YouTube sin bajadas",
        "title": "Suscriptores de YouTube sin bajadas y sin bots | Growsterr",
        "description": "Las cifras de suscriptores bajan cuando nunca fueron reales. Los nuestros son personas que eligieron tu canal, no cuentas a la espera de una limpieza.",
        "h1": ("¿Suscriptores de YouTube sin bajadas? ", "Empieza por personas que eligieron tu canal."),
        "intro": "Querer comprar suscriptores de YouTube sin bajadas suele significar que ya has visto caer una cifra. Los suscriptores se caen cuando nunca fueron personas: YouTube elimina el spam y las cuentas cerradas, y los suscriptores bot se van con ellos. Los nuestros son espectadores reales que decidieron suscribirse, justo el tipo de cuenta que una limpieza está hecha para dejar en paz.",
        "hero": {"image": "youtube-subscribers", "alt": "La cifra de suscriptores de YouTube se mantiene mientras llegan nuevos suscriptores reales"},
        "sections": [
            {
                "h2": "Por qué bajan las cifras de suscriptores",
                "p": [
                    "YouTube elimina los suscriptores que considera spam, junto con las cuentas que se han cerrado. Los canales que compraron suscriptores bot ven caer esas cifras por escalones, a veces meses después de la compra.",
                    "La bajada es la parte visible. La parte oculta es el tiempo que esas cuentas pasaron en tu canal sin ver nada, reduciendo la parte de tus suscriptores que interactúa.",
                ],
            },
            {
                "h2": "Por qué una reposición no es la solución",
                "p": [
                    "Algunos vendedores prometen reponer lo que se caiga. Eso significa sustituir bots eliminados por bots nuevos, lo que mantiene la cifra arriba y el problema en marcha. Un suscriptor real no necesita sustituto.",
                ],
            },
            {
                "h2": "Cómo es un «sin bajadas» honesto",
                "p": [
                    "Las personas reales pueden darse de baja, como en cualquier canal, y con el tiempo algunas lo harán. Es la rotación normal, y es pequeña al lado de las oleadas que dejan los bots. Lo que se queda es un público que sigue ahí cuando subes un vídeo.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Suscriptores de hace tiempo ven en el sofá el último vídeo de YouTube de un creador"},
            },
        ],
        "faqs": [
            ("¿Alguno de mis nuevos suscriptores se irá alguna vez?", "Puede que algunos, como pasa en todos los canales cuando cambian los gustos de la gente. Lo que no tendrás es un lote de cuentas falsas esperando a que las eliminen juntas."),
            ("¿Hay reposición si bajan los suscriptores?", "No, porque no hay ninguna cifra falsa que rellenar. Recibes un paquete mensual de personas reales; lo que hagan después es decisión suya, como con cualquier público."),
            ("¿Por qué bajó mi cifra después de otro servicio?", "Lo más probable es que YouTube eliminara cuentas que consideró spam, o cuentas que se habían cerrado. Los suscriptores bot suelen irse en grandes lotes durante esas limpiezas."),
            ("¿Los suscriptores bot pueden perjudicar mi canal incluso cuando ya no están?", "La eliminación es el problema menor. Mientras estuvieron, nunca vieron ni un solo vídeo, y eso hizo que tu público pareciera menos activo de lo que era en realidad."),
            ("¿Mi panel coincide con mi cifra de YouTube?", "No exactamente. Tu panel cuenta los nuevos suscriptores que trajo nuestra campaña; el total que muestra YouTube incluye también el crecimiento de otras fuentes y a quien se haya dado de baja."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "organic",
        "slug": "youtube/suscriptores/organicos",
        "label": "Suscriptores orgánicos de YouTube",
        "title": "Suscriptores orgánicos de YouTube: cómo funciona | Growsterr",
        "description": "¿Se pueden comprar suscriptores orgánicos de YouTube? Pagamos la presentación con campañas promocionadas; suscribirse es decisión del espectador.",
        "h1": ("¿Comprar suscriptores orgánicos de YouTube? ", "Pagamos la presentación. Ellos eligen."),
        "intro": "Esta es la respuesta honesta para quien quiere comprar suscriptores orgánicos de YouTube: nadie puede venderte una decisión. Lo que pagamos es la presentación. Tu canal se muestra a personas reales mediante campañas promocionadas en nuestra red de socios, y quien se suscribe lo hace porque quiere.",
        "hero": {"image": "youtube-subscribers", "alt": "Nuevos suscriptores se unen a un canal de YouTube después de descubrir sus vídeos"},
        "sections": [
            {
                "h2": "La línea entre lo pagado y lo orgánico",
                "p": [
                    "Todo canal que se anuncia paga por atención. Lo que pasa después es orgánico o no lo es: una persona mira, le gusta el vídeo o no, y se suscribe o sigue a lo suyo.",
                    "Mantenemos esa línea limpia. Pagamos para poner tu canal delante de personas cada día; nunca pagamos a nadie por suscribirse, nunca intercambiamos suscripciones y nunca usamos cuentas que actúan por encargo.",
                ],
            },
            {
                "h2": "Cómo distinguir a los suscriptores orgánicos del resto",
                "ul": [
                    "Sus nombres aparecen en los comentarios de tu próximo vídeo.",
                    "Sus comentarios suenan a personas: preguntas, bromas, algún desacuerdo.",
                    "Los nuevos suscriptores llegan junto con visitas al canal, nunca sin ellas.",
                    "Se quedan cuando termina la campaña, porque nada los retenía.",
                ],
            },
            {
                "h2": "Orgánico no tiene por qué significar esperar",
                "p": [
                    "A menudo se imagina el crecimiento orgánico como años esperando un vídeo con suerte. Una campaña promocionada acorta la espera: personas reales ven tu canal desde los primeros días. Lo único que no puede acortar es su decisión, y esa es la parte que merece la pena conservar.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Alguien pulsa suscribirse, café en mano, en un canal que descubrió esa mañana"},
            },
        ],
        "faqs": [
            ("Si promocionáis mi canal, ¿el crecimiento sigue siendo orgánico?", "Las suscripciones, sí. Pagamos para que se muestre tu canal; a nadie se le paga ni se le recompensa por suscribirse. Cada suscriptor decidió por su cuenta después de ver tus vídeos."),
            ("¿Usáis «sub por sub» o redes de intercambio?", "Nunca. Quien se suscribe para recibir una suscripción a cambio no está interesado en tus vídeos y rara vez los ve, y YouTube considera esos intercambios interacción falsa."),
            ("¿Cuánto suma el crecimiento orgánico en un mes?", "{pick_name} suele quedar en {pick_audience} al mes. Como cada uno es una persona que elige, es un rango y no un recuento."),
            ("¿Los suscriptores orgánicos verán mis vídeos?", "Eligieron tu canal después de verlo, que es el mejor comienzo que puede tener un suscriptor. Que vean cada vídeo depende del vídeo, como con todo el mundo."),
            ("¿Tengo que hacer algo durante la campaña?", "Mantén tu canal público y sigue subiendo vídeos. Cuanto más encajen tus vídeos con lo que promete la página de tu canal, más visitantes decidirán suscribirse."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "real",
        "slug": "youtube/suscriptores/reales",
        "label": "Suscriptores de YouTube reales",
        "title": "Suscriptores reales de YouTube que puedes comprobar | Growsterr",
        "description": "Reales, auténticos, de calidad: cuatro señales que puedes comprobar en cualquier suscriptor de YouTube, y cómo nuestros paquetes traen personas que las cumplen.",
        "h1": ("Comprar suscriptores de YouTube reales. ", "Así se distinguen."),
        "intro": "Cuando la gente compra suscriptores de YouTube, «reales» es la palabra que añade después de llevarse un chasco. Creemos que debería significar algo que puedas comprobar: una persona que se encontró con tu canal, decidió que merecía la pena suscribirse y después aparece en tus visualizaciones, tus likes y tus comentarios.",
        "hero": {"image": "youtube-subscribers", "alt": "La página de un canal de YouTube con suscriptores reales que llegan a lo largo de un mes"},
        "sections": [
            {
                "h2": "Cuatro señales de que un suscriptor es real",
                "p": [
                    "Alta calidad, auténticos, reales: todos los vendedores usan estas palabras. Estas son las comprobaciones que los distinguen.",
                ],
                "ul": [
                    "Hubo antes una visita: alguien abrió tu canal antes de suscribirse.",
                    "Miran: las visualizaciones de tu próximo vídeo suben junto con la cifra de suscriptores.",
                    "Hablan, en comentarios que ningún script escribiría.",
                    "Viven donde dirigiste la campaña, en el lugar que indicaste al hacer el pedido.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Un nuevo suscriptor comenta con sus propias palabras bajo un vídeo de YouTube"},
            },
            {
                "h2": "Compáranos con YouTube Studio",
                "p": [
                    "Nuestra versión de la historia es tu panel de Growsterr: las visitas de la campaña a tu canal y quiénes de ellas se suscribieron. YouTube Studio cuenta el mismo mes desde el lado de YouTube. Léelos juntos durante un mes: a medida que llegan suscriptores, tus vídeos también deberían ganar visualizaciones y comentarios de gente nueva.",
                ],
            },
            {
                "h2": "Lo que los suscriptores reales no pueden hacer",
                "p": [
                    "A las personas reales no se las puede pedir por horas, no se les puede decir qué comentar y no pueden prometer ver cada vídeo. Quien ofrece esas cosas está describiendo algo que no son personas. Preferimos contarte los límites a venderte una cifra.",
                ],
            },
        ],
        "faqs": [
            ("¿Qué significa «alta calidad» en suscriptores de YouTube?", "Para nosotros, una persona con su propia cuenta que eligió tu canal y puede mirar, dar like y comentar. Las fotos de perfil y la antigüedad de la cuenta son fáciles de falsificar; una decisión real de suscribirse, no."),
            ("¿Vuestros suscriptores son personas auténticas o cuentas que controláis?", "Personas auténticas. No tenemos, ni gestionamos, ni alquilamos ninguna cuenta. Mostramos tu canal mediante campañas promocionadas, y las personas que lo ven deciden."),
            ("¿Puedo comprar suscriptores reales de YouTube online sin compartir mis datos de acceso?", "Sí, y nunca deberías compartirlos con nadie. Necesitamos el identificador de tu canal y un canal público, nada más."),
            ("¿Los suscriptores reales harán que mi canal se monetice?", "Esa decisión es de YouTube, así que nunca prometemos monetización ni horas de visualización. Los suscriptores reales pueden ver tus vídeos, algo que los bots nunca hacen, pero son los requisitos y la revisión de YouTube los que deciden quién se monetiza."),
            ("¿Cómo es un mes de crecimiento real?", "Con {pick_name}, un habitual de {pick_audience} nuevos suscriptores, que llegan en pequeñas cantidades cada día. Un canal más pequeño puede empezar con {starter_name} por {starter_price} al mes."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "safe",
        "slug": "youtube/suscriptores/seguros",
        "label": "Suscriptores de YouTube seguros",
        "title": "Comprar suscriptores de YouTube legítimos y seguros | Growsterr",
        "description": "¿Es legítimo y seguro comprar suscriptores de YouTube? Comprueba quién lleva el servicio, qué te pide y cómo llegan los suscriptores. Así respondemos.",
        "h1": ("¿Comprar suscriptores de YouTube de forma legítima? ", "Comprueba primero quién hay detrás."),
        "intro": "¿Te preguntas si puedes comprar suscriptores de YouTube de forma legítima y segura? Para considerarse legítimo, un servicio debería superar tres comprobaciones: una empresa con nombre, nada que toque tus datos de acceso y suscriptores que sean personas reales. Growsterr es un producto de Sterr Agency, y así respondemos a cada una.",
        "hero": {"image": "youtube-subscribers", "alt": "El canal de YouTube de un creador crece de forma segura con suscriptores que son personas reales"},
        "sections": [
            {
                "h2": "A quién le pagas",
                "p": [
                    "Detrás de Growsterr está Sterr Agency, registrada como Sterr Technologies OÜ en Tallin (Estonia) y con sede central en Turquía. Pagas a través de la pasarela segura de Stripe, y la suscripción está en tu propia cuenta, desde donde puedes cancelarla.",
                ],
            },
            {
                "h2": "Cómo se mantiene protegido tu canal",
                "ul": [
                    "Tu contraseña de Google sigue siendo tuya: nunca te la pedimos, y nadie de nuestro equipo inicia sesión en tu canal.",
                    "A nadie se le paga por suscribirse, y no hay intercambios de suscripciones.",
                    "Los suscriptores llegan a lo largo del mes, nunca en un lote.",
                    "Los likes y los comentarios vienen de los propios suscriptores, así que todas las cifras se mueven a la par.",
                ],
                "image": {"image": "youtube-channel", "alt": "Un creador revisa en su escritorio los ajustes de su canal de YouTube, con la sesión iniciada solo en su dispositivo"},
            },
            {
                "h2": "Señales de alarma en cualquier servicio de crecimiento",
                "ul": [
                    "Te pide tus datos de acceso o acceso a tu cuenta de Google.",
                    "Promete un número exacto de suscriptores para una fecha concreta.",
                    "Vende suscriptores, visualizaciones y likes como lotes separados por millares.",
                    "No sabe decirte de dónde vienen los suscriptores ni mostrarte lo que ha medido.",
                ],
            },
        ],
        "faqs": [
            ("¿Es legítimo comprar suscriptores de YouTube?", "Pagar por promoción es lo normal; lo hace todo canal que se anuncia. Pagar por interacción falsa no lo es: los bots, los scripts y los intercambios de suscripciones son lo que YouTube trata como spam. Nosotros solo promocionamos tu canal ante personas reales que deciden por sí mismas."),
            ("¿YouTube puede cerrar mi canal por esto?", "YouTube actúa contra la interacción falsa, y por eso nunca la usamos. No podemos hablar por las decisiones de YouTube, pero que la gente elija tu canal después de verlo es como funciona la promoción en todas partes."),
            ("¿Qué tengo que daros para empezar?", "El identificador de tu canal, el lugar del que debe venir tu público y una tarjeta para el paquete mensual. Tu canal tiene que ser público para que la gente pueda suscribirse."),
            ("¿Mi pago es seguro?", "Stripe procesa todos los pagos, ya uses tarjeta, Apple Pay o Google Pay. Los datos de tu tarjeta se quedan en Stripe, no en nosotros."),
            ("¿Y si no es para mí?", "Cancela desde tu cuenta cuando quieras. A partir de ahí no se cobra ningún pago nuevo, y tu mes en curso sigue hasta que termine."),
        ],
    },
    # --- Visualizaciones ------------------------------------------------------------------
    {
        "service": "views",
        "slug": "youtube/visualizaciones",
        "label": "Visualizaciones de YouTube",
        "title": "Comprar visitas de YouTube de personas reales | Growsterr",
        "description": "¿Quieres comprar visualizaciones de YouTube? Las nuestras vienen de personas que deciden mirar, en un paquete mensual con suscriptores, likes y comentarios.",
        "h1": ("¿Comprar visitas en YouTube? ", "Cada una viene de una persona."),
        "intro": "Si has venido a comprar visualizaciones de YouTube, así funcionan las nuestras. Aquí no hay un menú de cifras de visitas. Cada paquete presenta tu canal a personas reales a diario; pulsan play en lo que les interesa, y muchas acaban dando like, comentando y suscribiéndose. Las visualizaciones vienen con el paquete, y cada una es una persona.",
        "hero": {"image": "youtube-viewers", "alt": "Personas reales pulsan play en el vídeo de YouTube de un creador"},
        "sections": [
            {
                "h2": "Por qué nuestros paquetes no tienen cifra de visualizaciones",
                "p": [
                    "Una visualización es una persona que decide mirar, y nadie puede prometer cuántas personas lo decidirán. Quien vende un número exacto de visualizaciones para una hora concreta vende reproducciones generadas por scripts o bots.",
                    "YouTube trata las visualizaciones infladas artificialmente como spam: puede eliminarlas, y nunca cuentan para la monetización. Así que vendemos lo que podemos defender: una campaña mensual que trae personas reales, con rangos habituales de los suscriptores, likes y comentarios que dejan.",
                ],
            },
            {
                "h2": "Videoclips, listas de reproducción y vídeos largos",
                "p": [
                    "Promocionamos tu canal, no un tema concreto. Los oyentes que lo descubren eligen las canciones que les enganchan, y quienes disfrutan de un tema pueden seguir por tus listas de reproducción; cada reproducción ahí es suya.",
                ],
                "image": {"image": "youtube-channel", "alt": "Un músico sube un nuevo videoclip a su canal de YouTube"},
            },
            {
                "h2": "Antes de elegir cualquier web para comprar visitas de YouTube",
                "ul": [
                    "Pregunta qué significa para ellos una visualización: una persona que eligió mirar o una reproducción que generaron.",
                    "Comprueba si las visualizaciones llegan solas o con suscriptores, likes y comentarios de las mismas personas.",
                    "Busca un nombre de empresa, una pasarela de pago real y una forma de cancelar.",
                    "Aléjate de quien te pida tu contraseña de Google.",
                ],
            },
        ],
        "faqs": [
            ("¿Puedo pedir visualizaciones sin un paquete?", "No. Cada visualización que traemos es de alguien que también podría suscribirse, dar like o comentar, y por eso solo vienen como parte de un paquete. Una cifra de visualizaciones que sube mientras nada más se mueve es el patrón del tráfico artificial."),
            ("¿Me diréis cuántas visualizaciones esperar?", "No ponemos cifra a las visualizaciones, porque cada una es la elección de una persona. Lo que sí damos son rangos mensuales habituales: con {pick_name}, {pick_audience} nuevos suscriptores y {pick_likes} likes, y esas personas miran antes de hacer cualquiera de las dos cosas."),
            ("¿Hay una app para comprar visitas de YouTube?", "No usamos ninguna app. Eliges un paquete en nuestra web, pagas a través de Stripe y sigues tu campaña en el panel de tu cuenta, desde cualquier navegador."),
            ("¿Qué son las visualizaciones «premium» de YouTube?", "Nada que YouTube reconozca. YouTube Premium es una suscripción para espectadores, no un tipo de visualización que nadie pueda venderte. Las únicas visualizaciones que merecen la pena son las de personas que pulsaron play por su cuenta."),
            ("¿Las visualizaciones compradas pueden hacer viral un vídeo?", "Nadie puede prometerlo. Los espectadores reales dan a un vídeo más personas que podrían compartirlo, que es la versión honesta de una oportunidad viral."),
            ("¿Las visualizaciones ayudan a monetizar mi canal?", "Ni la monetización ni las horas de visualización son algo que prometamos. Las visualizaciones artificiales no cuentan en absoluto; los espectadores reales pueden ver tus vídeos, pero es YouTube quien decide quién se monetiza."),
        ],
    },
    {
        "service": "views",
        "modifier": "gradual",
        "slug": "youtube/visualizaciones/progresivas",
        "label": "Visualizaciones de YouTube progresivas",
        "title": "Visitas de YouTube poco a poco, a ritmo humano | Growsterr",
        "description": "Visualizaciones de YouTube que crecen poco a poco durante el mes: espectadores reales encuentran tu canal de pocos en pocos, con suscriptores y likes.",
        "h1": ("¿Visitas de YouTube poco a poco? ", "Los espectadores reales nunca llegan de otra forma."),
        "intro": "Querer comprar visualizaciones de YouTube poco a poco es un buen instinto: un vídeo que gana visitas durante días es un vídeo que la gente está descubriendo. Aquí nadie tiene que activar ese ritmo. Personas reales descubren tu canal todos los días del mes y ven lo que les interesa, así que tus visualizaciones crecen como en cualquier canal que va a más.",
        "hero": {"image": "youtube-viewers", "alt": "Espectadores descubren un canal de YouTube uno a uno durante varias semanas"},
        "sections": [
            {
                "h2": "Un goteo programado no es lo mismo",
                "p": [
                    "Un goteo programado reparte reproducciones generadas a lo largo de una semana en vez de una hora. El contador sube con más calma, pero las reproducciones siguen llegando sin nadie mirando de verdad, sin likes y sin suscriptores. YouTube se fija en lo que hacen los espectadores, no solo en lo rápido que llegaron.",
                ],
            },
            {
                "h2": "Tus vídeos antiguos también se ven",
                "p": [
                    "Los espectadores que llegan a lo largo de semanas no solo ven tu último vídeo. Alguien que disfruta de uno puede abrir otro desde la página de tu canal, así que los vídeos antiguos también suman visitas al mismo ritmo pausado. Un goteo dirigido a un solo enlace no puede hacer eso.",
                ],
                "image": {"image": "youtube-channel", "alt": "La página de un canal de YouTube con una cuadrícula de vídeos antiguos que reciben nuevas visitas"},
            },
            {
                "h2": "Un ritmo que puedes seguir",
                "p": [
                    "El panel sigue a personas, no reproducciones: las visitas diarias de la campaña a tu canal y los suscriptores entre ellas. Las visualizaciones no aparecen, porque no las contamos por adelantado; las encontrarás en YouTube Studio, en los vídeos que eligió la gente.",
                ],
            },
        ],
        "faqs": [
            ("¿Hay una cifra diaria de visualizaciones con la que pueda contar?", "No hay cifra diaria que dar: cada visualización depende de que alguien decida mirar. Lo que puedes esperar son nuevos espectadores todos los días del mes, no un pico el primer día."),
            ("¿Puedo repartir las visualizaciones en un número de días concreto?", "Cada campaña dura 30 días y se renueva cada mes. Dentro de ese plazo, el ritmo lo marcan las personas reales, así que no programamos visualizaciones por días."),
            ("¿Las visualizaciones lentas parecen más naturales a YouTube?", "La velocidad es solo una parte. YouTube también ve si los espectadores siguen mirando, dan like al vídeo y vuelven. Las personas reales hacen esas cosas a cualquier ritmo; las reproducciones programadas, nunca."),
            ("¿Y los vídeos que publiqué el año pasado?", "Forman parte. Quien disfruta de un vídeo suele mirar qué más hay en tu canal, y los vídeos antiguos son a menudo donde acaba después."),
            ("¿Y si quiero visualizaciones más rápido?", "Elige un paquete mayor, para que más gente vea tu canal cada día. Lo que promete miles de visualizaciones en menos de una hora está generando reproducciones, no encontrando espectadores."),
        ],
    },
    {
        "service": "views",
        "modifier": "high-retention",
        "slug": "youtube/visualizaciones/alta-retencion",
        "label": "Visualizaciones de YouTube de alta retención",
        "title": "Visitas de YouTube de alta retención, con honestidad | Growsterr",
        "description": "Las visualizaciones de YouTube de alta retención no se compran: la retención la gana el vídeo. Traemos espectadores reales que eligen pulsar play.",
        "h1": ("¿Visitas de YouTube de alta retención? ", "Trae a personas que quieren mirar."),
        "intro": "Si quieres comprar visualizaciones de YouTube de alta retención, ya sabes que una cifra de reproducciones no es lo importante: quieres espectadores que se queden. Pero la retención no es algo que nadie pueda vender. Es cuánto tiempo deciden seguir mirando las personas reales. Nuestra parte es traer espectadores que pulsaron play por decisión propia; cuánto se quedan depende de tu vídeo.",
        "hero": {"image": "youtube-channel", "alt": "Un creador edita un vídeo largo de YouTube para que los espectadores sigan mirando"},
        "sections": [
            {
                "h2": "La retención que se compra es un temporizador",
                "p": [
                    "Cuando un vendedor ofrece visualizaciones con una retención fija, lo que hay detrás es un reproductor configurado para funcionar un número fijo de segundos. Mira igual sea lo que sea lo que hay en pantalla, y nunca da like, comenta ni se suscribe. Dure lo que dure, es interacción artificial, y YouTube la trata como spam.",
                ],
            },
            {
                "h2": "Por qué los espectadores reales dan sentido a la retención",
                "p": [
                    "La retención importa porque muestra que quienes empezaron un vídeo querían seguir viéndolo. Eso solo se cumple cuando eligieron el vídeo desde el principio. Los espectadores reales te dan datos de retención honestos: dónde se quedan, dónde se van y qué los hace volver.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Un espectador se acerca a la pantalla para ver hasta el final un vídeo largo de YouTube"},
            },
            {
                "h2": "Lo que sube la retención, por tu parte",
                "ul": [
                    "Cumple en los primeros segundos lo que prometen el título y la miniatura.",
                    "Quita la introducción lenta: muestra primero lo importante y luego explícalo.",
                    "Añade capítulos a los vídeos largos, para que los espectadores salten a lo que buscan en lugar de irse.",
                    "Busca en YouTube Studio dónde abandonan los espectadores y arregla ese momento en tu próximo vídeo.",
                ],
            },
        ],
        "faqs": [
            ("¿Prometéis un porcentaje de retención u horas de visualización?", "No. La retención y el tiempo de visualización dependen del vídeo y de cada espectador. Traemos personas reales que eligieron mirar, y nunca ponemos cifra a cuánto tiempo se quedan."),
            ("¿La gente verá mi vídeo entero?", "Unos sí y otros no, y eso es justo lo que hace útiles sus datos. YouTube Studio te muestra dónde se queda la gente y dónde se va."),
            ("¿Las visualizaciones de alta retención cuentan para la monetización?", "Las visualizaciones artificiales no cuentan en absoluto para la monetización, tengan la retención que tengan. El tiempo de visualización de los espectadores reales es auténtico, pero nunca prometemos monetización; eso lo decide YouTube."),
            ("¿La campaña puede llevar espectadores a un vídeo concreto?", "Puedes indicar un vídeo, al hacer el pedido o después desde tu cuenta, y los nuevos espectadores llegan a él: primero se suscriben y después miran. No prometemos visualizaciones ni tiempo de visualización en ese vídeo; cuánto se queda la gente depende de él."),
            ("¿Qué vídeos salen más beneficiados?", "Los que cumplen lo que prometen. Un gancho claro, una miniatura honesta y un ritmo constante convierten a los nuevos espectadores en visionados largos, y cuanta más gente lleva la campaña a tu canal, a más pueden retener esos vídeos."),
        ],
    },
    {
        "service": "views",
        "modifier": "live",
        "slug": "youtube/visualizaciones/directos",
        "label": "Visualizaciones de directos de YouTube",
        "title": "¿Visitas para tus directos de YouTube? | Growsterr",
        "description": "Nadie puede llenar un directo de YouTube con personas reales a una hora fija. Hacemos crecer los suscriptores que pueden entrar en el próximo.",
        "h1": ("¿Comprar visitas para directos de YouTube? ", "Crea el público que aparece."),
        "intro": "Si quieres comprar visitas para directos de YouTube, quieres una emisión que no parezca vacía cuando pulsas empezar. Nadie puede llevar personas reales a una emisión en un minuto concreto, y nosotros no lo decimos. Lo que hacemos es hacer crecer tu canal con suscriptores reales cada día, para que cada directo tenga más personas que podrían entrar.",
        "hero": {"image": "youtube-channel", "alt": "Un creador a punto de emitir en directo en YouTube con una emisión programada en pantalla"},
        "sections": [
            {
                "h2": "Por qué una cifra comprada en directo sale mal",
                "p": [
                    "La cifra de espectadores es lo primero que ve cualquiera en un directo. Cuando dice cientos y el chat está en silencio, todo visitante real lo nota. Los espectadores de directo comprados no escriben, no reaccionan y no vuelven para la repetición.",
                    "Las normas de YouTube sobre visualizaciones falsas no se detienen cuando emites en directo. Un contador en directo no es un lugar más seguro para falsificar.",
                ],
            },
            {
                "h2": "Quién entra en una emisión, y cuándo",
                "p": [
                    "Las personas con más probabilidades de entrar son suscriptores que ya conocen tu canal. Según sus ajustes, YouTube puede mostrarles tu emisión en su feed o enviarles una notificación.",
                ],
                "ul": [
                    "Programa la emisión con antelación, para que los suscriptores puedan poner un recordatorio.",
                    "Elige una ubicación de público en la que tu hora de emisión caiga por la tarde o la noche.",
                    "Emite un día fijo, para que los espectadores sepan cuándo volver.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Espectadores se unen desde el móvil a un directo programado de YouTube por la noche"},
            },
            {
                "h2": "La repetición sigue sumando visualizaciones",
                "p": [
                    "Cuando termina la emisión, se queda en tu canal como un vídeo. Los nuevos suscriptores que se la perdieron en directo pueden encontrar ahí la repetición y verla cuando les venga bien.",
                ],
            },
        ],
        "faqs": [
            ("¿Podéis llenar mi emisión mientras estoy en directo?", "No. Las personas reales miran cuando deciden, así que no podemos prometer a nadie a una hora concreta. Hacemos crecer la base de suscriptores de la que se nutren tus emisiones."),
            ("¿Importa la ubicación que elija para los directos?", "Más que para los vídeos normales. Elige el lugar donde vive tu público, y tu hora de emisión caerá en su día y no en mitad de su noche."),
            ("¿La repetición recibirá visualizaciones de la campaña?", "Puede. Una repetición es un vídeo de tu canal, así que los espectadores que te encuentran después de la emisión pueden verla como cualquier otro vídeo."),
            ("¿No podría comprar espectadores de directo solo para el contador?", "Podrías, pero sale mal. Los espectadores artificiales en una emisión son interacción falsa como cualquier otra, y un contador lleno sobre un chat vacío es fácil de detectar para los espectadores reales."),
            ("¿Qué paquete encaja con un canal que emite en directo?", "{pick_name} es el más popular, normalmente {pick_audience} nuevos suscriptores al mes; un canal más nuevo puede empezar con {starter_name}. Cada emisión a partir de ahí tiene más personas que podrían entrar."),
        ],
    },
    {
        "service": "views",
        "modifier": "monthly",
        "slug": "youtube/visualizaciones/mensuales",
        "label": "Visualizaciones de YouTube mensuales",
        "title": "Visitas de YouTube para varios vídeos, cada mes | Growsterr",
        "description": "Compra visualizaciones de YouTube para varios vídeos: un paquete mensual lleva espectadores reales a todo tu canal, donde eligen qué ver. Desde {from_price}.",
        "h1": ("Visualizaciones de YouTube para varios vídeos, ", "mes tras mes."),
        "intro": "Cuando compras visualizaciones de YouTube para varios vídeos, lo que de verdad quieres es un canal al que la gente vuelva. Un paquete mensual está hecho justo para eso: personas reales descubren tu canal cada día y ven los vídeos que les interesan, y la campaña se renueva cada mes, así que los nuevos vídeos siguen encontrando nuevos espectadores.",
        "hero": {"image": "youtube-viewers", "alt": "Un espectador pasa de un vídeo de YouTube al siguiente en el mismo canal"},
        "sections": [
            {
                "h2": "Un canal, muchos vídeos",
                "p": [
                    "Los espectadores interesados no se quedan en un vídeo. Alguien que te encuentra por un tutorial abre el siguiente, y después lo que sugiera la página de tu canal. Una campaña construida en torno a tu canal, y no a un solo enlace, sigue la forma en que la gente mira de verdad.",
                ],
            },
            {
                "h2": "Cómo orientar adónde van después los nuevos espectadores",
                "p": [
                    "Promocionamos tu canal en conjunto; los espectadores deciden qué vídeos abrir. Lo que controlas es el camino que tienen delante cuando llegan.",
                ],
                "ul": [
                    "Pon un tráiler del canal para los visitantes que aún no se han suscrito.",
                    "Destaca tu mejor vídeo en lo alto de la página de tu canal.",
                    "Agrupa vídeos relacionados en listas de reproducción, para que uno lleve al siguiente.",
                    "Añade pantallas finales que apunten al vídeo que un espectador debería ver después de este.",
                ],
            },
            {
                "h2": "Por qué poco a poco gana a todo de golpe",
                "p": [
                    "Las visualizaciones repartidas en un mes llegan a cada vídeo mientras es nuevo y mantienen vivos los antiguos. Un empujón único en varios vídeos hace lo contrario: un pico en cada uno y luego silencio.",
                ],
                "image": {"image": "youtube-channel", "alt": "Un creador prepara una serie de vídeos de YouTube para publicar a lo largo del mes"},
            },
        ],
        "faqs": [
            ("¿A cuántos vídeos pueden ir las visualizaciones?", "No hay lista ni límite. Promocionamos tu canal, y los espectadores ven lo que les interesa en cualquier parte de él."),
            ("¿Los vídeos que subo durante el mes reciben visualizaciones?", "Sí. La campaña funciona todos los días, así que un vídeo que publicas a mitad de mes sigue encontrando gente nueva, y tus nuevos suscriptores pueden verlo como cualquier suscriptor."),
            ("¿El precio es por vídeo?", "No, es por mes para todo tu canal: {starter_name} cuesta {starter_price} al mes, {rising_name} {rising_price} y {pro_name} {pro_price}, tengas los vídeos que tengas. Las visualizaciones vienen dentro, con suscriptores, likes y comentarios."),
            ("¿Puedo parar después de un mes?", "Sí. Cancela en tu cuenta; el mes pagado termina con normalidad y el siguiente no se cobra."),
            ("¿Las visualizaciones pueden venir de una sola ciudad?", "Sí. Sirve una sola ciudad, igual que una región o un país entero. Eso encaja con canales de público local, como una guía gastronómica de una ciudad o un canal de noticias locales."),
        ],
    },
    {
        "service": "views",
        "modifier": "no-drop",
        "slug": "youtube/visualizaciones/permanentes",
        "label": "Visualizaciones de YouTube sin bajadas",
        "title": "¿Visitas reales de YouTube sin bajadas? Por qué caen | Growsterr",
        "description": "Por qué bajan las visualizaciones de YouTube después de una compra, y en qué se diferencian las de personas que eligieron pulsar play. Desde {from_price} al mes.",
        "h1": ("¿Visitas reales de YouTube sin bajadas? ", "Empieza por visitas que nunca fueron falsas."),
        "intro": "Quien quiere comprar visualizaciones reales de YouTube sin bajadas normalmente ya ha visto caer una cifra. Las visualizaciones bajan cuando YouTube elimina reproducciones que considera artificiales. Las nuestras vienen de personas reales que eligieron pulsar play, dentro de un paquete mensual, así que no hay ningún lote de reproducciones falsas esperando a que lo retiren.",
        "hero": {"image": "youtube-channel", "alt": "Un creador comprueba en su estudio que la cifra de visualizaciones de un vídeo de YouTube se mantiene"},
        "sections": [
            {
                "h2": "Por qué bajan las cifras de visualizaciones",
                "p": [
                    "YouTube revisa las visualizaciones y elimina las que no considera auténticas: reproducciones de bots, scripts y otro tráfico artificial. Cuando eso pasa después de una compra, la cifra baja, a veces mucho después de la entrega, y el historial del vídeo muestra un pico seguido de una caída.",
                ],
            },
            {
                "h2": "Lo que podemos prometer y lo que no",
                "p": [
                    "No podemos prometer que YouTube nunca ajuste una cifra; revisa todo el tráfico, también el nuestro. Lo que sí podemos contarte es cómo ocurren nuestras visualizaciones: una persona real ve tu canal gracias a una campaña promocionada y decide mirar. Ese es el tipo de visualización que las revisiones de YouTube están para conservar.",
                ],
            },
            {
                "h2": "Cuando visualizaciones, likes y suscriptores suben juntos",
                "p": [
                    "Las visualizaciones reales rara vez van solas. En un paquete llegan con nuevos suscriptores, likes y comentarios de las mismas personas, así que tus cifras suben juntas y nada en ellas parece fuera de lugar, ni para YouTube ni para un espectador.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Unos amigos ven juntos un vídeo de YouTube y le dan like cuando termina"},
            },
        ],
        "faqs": [
            ("¿Bajarán alguna vez mis visualizaciones?", "YouTube puede ajustar la cifra de cualquier vídeo cuando revisa el tráfico, así que nadie puede prometer con honestidad una cifra que no se mueva nunca. Las visualizaciones de personas que eligieron mirar son el tipo que su revisión está pensada para conservar."),
            ("¿Repondréis visualizaciones si baja la cifra?", "No. Una reposición cambia reproducciones falsas eliminadas por otras nuevas. Nosotros vendemos un paquete mensual de personas reales, así que no hay nada artificial que sustituir."),
            ("¿Por qué bajaron mis visualizaciones después de una compra anterior?", "Casi siempre porque YouTube eliminó reproducciones que consideró artificiales. Eso puede ocurrir semanas después de la entrega, y por eso la bajada puede pillar por sorpresa."),
            ("¿Puedo comprar visualizaciones sin bajadas para un solo vídeo?", "No como pedido suelto. Las visualizaciones vienen dentro de un paquete mensual que hace crecer todo tu canal, así que cualquier vídeo puede beneficiarse."),
            ("¿Qué más viene con las visualizaciones?", "El resto lo traen los propios espectadores. Con {pick_name}, normalmente {pick_audience} suscriptores, {pick_likes} likes y {pick_comments} comentarios al mes."),
        ],
    },
    {
        "service": "views",
        "modifier": "organic",
        "slug": "youtube/visualizaciones/organicas",
        "label": "Visualizaciones de YouTube orgánicas y segmentadas",
        "title": "Visitas de YouTube segmentadas por ciudad o país | Growsterr",
        "description": "Compra visualizaciones de YouTube segmentadas en la ciudad, región o país de tu público: espectadores orgánicos que eligieron mirar, desde {from_price} al mes.",
        "h1": ("Visualizaciones de YouTube segmentadas, ", "del lugar donde vive tu público."),
        "intro": "Para comprar visualizaciones de YouTube segmentadas, dinos dónde deben estar tus espectadores: una ciudad, una región más amplia o un país entero. Mostramos tu canal a personas reales de allí mediante campañas promocionadas, y las visualizaciones son orgánicas en lo que importa: cada una es alguien que decidió mirar.",
        "hero": {"image": "youtube-channel", "alt": "Un creador graba un vídeo de YouTube en una calle de la ciudad para un público local"},
        "sections": [
            {
                "h2": "Por qué la ubicación es la segmentación que importa",
                "p": [
                    "Un canal de cocina en Lisboa, un canal inmobiliario en Dubái, un canal de videojuegos en turco: cada uno tiene un público que vive en algún sitio y habla un idioma. Los espectadores de ese lugar entienden tus vídeos, vuelven para el siguiente y pueden convertirse en clientes si vendes algo.",
                    "Dirigimos tu campaña primero al lugar que elijas. Si lo que mejor encaja con tu canal es un público mayor justo al otro lado de una frontera, parte de tus espectadores puede venir de allí.",
                ],
            },
            {
                "h2": "Segmentado no significa forzado",
                "p": [
                    "Apuntamos a donde está la gente y luego dejamos que decida. A nadie se le obliga a ver tu vídeo, y no se reproduce nada que no se haya elegido. Una visualización segmentada sigue siendo una elección, y eso es lo que la hace orgánica.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Espectadores locales en una cafetería ven un vídeo de YouTube grabado en su propia ciudad"},
            },
            {
                "h2": "Cómo elegir tu ubicación",
                "ul": [
                    "Elige el lugar para el que están hechos tus vídeos, no el lugar más grande que se te ocurra.",
                    "Para un negocio local o un canal de ciudad, elige la propia ciudad.",
                    "Para un idioma más que un lugar, elige el país donde vive la mayoría de quienes lo hablan.",
                    "Para un nicho internacional, empieza por el país cuyos espectadores más te interese alcanzar.",
                ],
            },
        ],
        "faqs": [
            ("¿Cómo de precisa es la segmentación?", "Tanto como una ciudad. Cuanto más pequeño es el lugar, más pequeño es su público, así que en un pueblo algunos espectadores pueden venir de la comarca."),
            ("¿La segmentación hace que las visualizaciones sean menos orgánicas?", "No: la decisión de mirar sigue siendo suya. Pagamos para mostrar tu canal en el lugar que elegiste; después cada espectador decide por sí mismo, y a nadie se le recompensa por mirar."),
            ("¿Los espectadores de mi ciudad se suscribirán?", "Algunos, si tu canal les habla. Con {pick_name}, normalmente {pick_audience} nuevos suscriptores al mes, del lugar que elegiste y de los alrededores."),
            ("¿Por qué no elegir la zona más amplia posible?", "Una zona mayor es una base mayor, pero los espectadores que no comparten tu idioma ni tu contexto rara vez se quedan. El lugar adecuado gana al más grande."),
            ("¿Necesitáis acceso a mi canal para segmentar a los espectadores?", "No. La segmentación ocurre en nuestras campañas, no en los ajustes de tu canal. Necesitamos tu identificador y una ubicación, nunca tu contraseña."),
        ],
    },
    {
        "service": "views",
        "modifier": "promote",
        "slug": "youtube/visualizaciones/promocionar",
        "label": "Promociona tus vídeos de YouTube",
        "title": "¿Visitas de YouTube con AdWords? Así promocionamos | Growsterr",
        "description": "¿Piensas comprar visitas de YouTube con AdWords? Promocionamos tu canal ante personas reales por ti, cada mes, con suscriptores, likes y comentarios.",
        "h1": ("¿Visitas de YouTube con AdWords? ", "O deja que llevemos la promoción."),
        "intro": "Quien quiere comprar visitas de YouTube con AdWords busca promocionar un vídeo con alcance pagado. Los anuncios de Google son una forma: una campaña que configuras, gestionas y pagas en las herramientas publicitarias de Google. Nosotros somos otra. Promocionamos tu canal ante personas reales mediante campañas en nuestra red de socios cada día, y tú sigues los resultados en tu panel.",
        "hero": {"image": "youtube-viewers", "alt": "Personas descubren en el móvil y la tableta un vídeo de YouTube promocionado"},
        "sections": [
            {
                "h2": "Hacer anuncios tú mismo o una campaña gestionada",
                "p": [
                    "Con Google Ads, la herramienta que sustituyó a AdWords, construyes tú la campaña: público, pujas, presupuesto y el propio anuncio. Pagas a medida que el sistema entrega, y vigilarlo es trabajo tuyo.",
                    "Un paquete de Growsterr es la opción en la que lo hacemos por ti. Nos das el identificador de tu canal y una ubicación; nuestro equipo lleva la promoción cada día, y tu panel muestra las visitas al canal y los nuevos suscriptores. Un precio mensual, sin pujas que gestionar.",
                ],
            },
            {
                "h2": "A qué debería llevar una visualización promocionada",
                "p": [
                    "Una visualización pagada solo compensa si el espectador hace algo después: ve otro vídeo, da like, se suscribe. Por eso nuestros paquetes giran en torno a los suscriptores, con likes, comentarios y visualizaciones de las mismas personas, y no en torno a un número de reproducciones.",
                ],
                "image": {"image": "youtube-channel", "alt": "Un creador revisa los nuevos suscriptores de un vídeo de YouTube después de empezar una promoción"},
            },
            {
                "h2": "Lo que no hacemos",
                "ul": [
                    "No configuramos ni gestionamos Google Ads, y nunca pedimos acceso a tu cuenta de Google.",
                    "No vendemos visualizaciones por millares ni con precio por visualización.",
                    "Puedes indicar un vídeo al que lleguen los nuevos espectadores, pero no hacemos coincidir la promoción con la hora de un lanzamiento.",
                    "No prometemos monetización, horas de visualización ni un hueco en las recomendaciones.",
                ],
            },
        ],
        "faqs": [
            ("¿Es lo mismo que hacer anuncios en YouTube?", "No. Los anuncios de YouTube funcionan en tu propia cuenta de Google Ads, con tu presupuesto y tus ajustes. Nosotros promocionamos tu canal a través de nuestra red de socios y llevamos la campaña por ti; nada funciona en tu cuenta."),
            ("¿Podéis gestionar mis campañas de Google Ads?", "No es algo que ofrezcamos. Nuestro trabajo son los paquetes de crecimiento mensuales; para algo mayor, háblanos por WhatsApp o por correo electrónico."),
            ("¿En qué se diferencia el coste de los anuncios?", "Los anuncios cobran a medida que entregan, así que lo que gastas se mueve con tus pujas y tu presupuesto. Nuestros paquetes tienen un precio mensual fijo, {starter_price}, {rising_price} o {pro_price}, con rangos habituales de suscriptores, likes y comentarios."),
            ("¿Puedo hacer mis propios anuncios a la vez?", "Sí. Tus anuncios funcionan en tu cuenta y nuestra campaña en nuestra red, así que una cosa no estorba a la otra."),
            ("¿Qué vídeos promocionáis?", "Tu canal en conjunto, y los espectadores eligen qué ver. Si quieres, puedes indicar un vídeo al que lleguen los nuevos espectadores; también ayuda poner un lanzamiento o una serie nueva en el espacio destacado de tu canal."),
        ],
    },
    {
        "service": "views",
        "modifier": "real",
        "slug": "youtube/visualizaciones/reales",
        "label": "Visualizaciones de YouTube reales",
        "title": "Visitas de YouTube de calidad: cada una, una persona | Growsterr",
        "description": "Compra visualizaciones de YouTube de calidad, de personas reales que eligieron mirar, con suscriptores, likes y comentarios de los mismos espectadores.",
        "h1": ("¿Visitas de YouTube de calidad? ", "Empieza por una persona detrás de cada reproducción."),
        "intro": "Antes de comprar visualizaciones de YouTube de calidad, conviene definir la calidad. Para nosotros, una visualización de calidad tiene una persona detrás: alguien que vio tu canal, eligió un vídeo y lo miró porque le interesaba. Es el único tipo que traen nuestros paquetes, y esas mismas personas también se suscriben, dan like y comentan.",
        "hero": {"image": "youtube-viewers", "alt": "Un espectador real elige un vídeo para ver en el canal de YouTube de un creador"},
        "sections": [
            {
                "h2": "Qué separa una visualización real de una reproducción",
                "ul": [
                    "La eligió una persona: a nadie se le pagó ni se le dio un guion para pulsar play.",
                    "Lleva a algo: algunos espectadores dan like, comentan o se suscriben.",
                    "Tiene un origen: el espectador vive donde dirigiste la campaña.",
                    "Aguanta: no tiene nada artificial que YouTube deba eliminar.",
                ],
            },
            {
                "h2": "Por qué las visualizaciones bot por niveles siguen sin ser de calidad",
                "p": [
                    "Algunos vendedores clasifican sus visualizaciones en estándar, alta calidad o premium. Sea cual sea la etiqueta, la pregunta que importa es la misma: ¿una persona eligió mirar? Si no, un nivel más alto solo significa un precio más alto por la misma reproducción vacía.",
                ],
            },
            {
                "h2": "Calidad que puedes leer en YouTube Studio",
                "p": [
                    "Las visualizaciones reales dejan huellas: tiempo de visualización que varía de un espectador a otro, comentarios que responden a tu vídeo y suscriptores ganados en los vídeos que la gente vio. Esas huellas son lo que hace que una visualización merezca la pena, y son las que las reproducciones generadas nunca dejan.",
                ],
                "image": {"image": "youtube-channel", "alt": "Un creador lee el tiempo de visualización y los comentarios de un vídeo de YouTube en sus estadísticas"},
            },
        ],
        "faqs": [
            ("¿En qué se diferencia una visualización de calidad de una barata?", "Una visualización barata suele ser una reproducción sin nada después. Una de calidad es una persona que podría dar like, comentar, suscribirse o volver, y solo ese tipo ayuda a tu canal."),
            ("¿Puedo ver quiénes son los espectadores?", "Tu panel muestra las visitas al canal y los nuevos suscriptores de tu campaña, y YouTube Studio muestra dónde están los espectadores y cuánto tiempo miran. Cada espectador sigue siendo anónimo, como en cualquier canal."),
            ("¿Las visualizaciones vienen sin suscriptores ni likes?", "No. Vienen en un paquete de las mismas personas, y eso es lo que las convierte en crecimiento y no en una cifra."),
            ("¿Por qué no hay lotes de mil visualizaciones?", "Porque mil visualizaciones por encargo significan mil reproducciones que alguien generó. Preferimos traer personas y dejar que elijan qué ver."),
            ("¿Puedo elegir dónde viven los espectadores?", "Sí: dinos el lugar al hacer el pedido, desde una sola ciudad hasta un país entero. Los espectadores locales entienden tus vídeos, y eso hace que sus visualizaciones valgan más que una cifra."),
        ],
    },
    {
        "service": "views",
        "modifier": "safe",
        "slug": "youtube/visualizaciones/seguras",
        "label": "Visualizaciones de YouTube seguras",
        "title": "Comprar visitas de YouTube legítimas y seguras | Growsterr",
        "description": "¿Comprar visitas de YouTube de forma legítima y segura? Qué considera falso YouTube, qué arriesga tu canal y cómo te llegan espectadores reales con nosotros.",
        "h1": ("¿Comprar visitas de YouTube de forma legítima? ", "Conoce lo que pone en riesgo un canal."),
        "intro": "Si quieres comprar visitas de YouTube de forma legítima y segura, empieza por aquello contra lo que actúa YouTube: visualizaciones de bots, scripts y cualquier tráfico que no sea una persona que decide mirar. Nos mantenemos en el lado correcto de esa línea promocionando tu canal solo ante personas reales, que miran si quieren.",
        "hero": {"image": "youtube-channel", "alt": "Un creador revisa el estado de su canal de YouTube en una tranquila oficina en casa"},
        "sections": [
            {
                "h2": "Lo que YouTube considera visualizaciones falsas",
                "p": [
                    "Las normas de YouTube sobre interacción falsa cubren todo lo siguiente. Puede eliminar las visualizaciones, y el contenido construido sobre ellas puede retirarse.",
                ],
                "ul": [
                    "Reproducciones de bots o scripts automáticos.",
                    "Visualizaciones de personas a las que se paga o recompensa por mirar.",
                    "Vídeos que se reproducen automáticamente sin que los espectadores los elijan.",
                    "Visualizaciones intercambiadas entre canales.",
                ],
            },
            {
                "h2": "Cómo llegan nuestras visualizaciones",
                "p": [
                    "Nuestra red de socios lleva campañas promocionadas que ponen tu canal delante de personas reales. A nadie se le paga por mirar, no se reproduce nada sin elegirlo y nada toca tu cuenta de YouTube. Quienes disfrutan de lo que ven miran más, dan like, comentan y se suscriben.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Un espectador elige en el móvil un vídeo de YouTube promocionado"},
            },
            {
                "h2": "Seguro también para tu cuenta",
                "ul": [
                    "Trabajamos con el identificador público de tu canal: sin datos de acceso ni solicitudes de acceso.",
                    "El cobro es una suscripción mensual de Stripe que controlas desde tu cuenta.",
                    "Terminarla depende de ti, en cualquier momento, sin preguntas.",
                ],
            },
        ],
        "faqs": [
            ("¿Comprar visualizaciones puede hacer que eliminen mi vídeo?", "Las visualizaciones falsas pueden: YouTube puede quitarlas de la cifra, y el contenido que incumple sus normas sobre interacción falsa puede retirarse. Las visualizaciones de personas que eligieron mirar no son interacción falsa."),
            ("¿Quién está detrás de Growsterr?", "Sterr Agency, cuya empresa registrada es Sterr Technologies OÜ, en Tallin (Estonia). La sede central del equipo está en Turquía."),
            ("¿Necesitáis mis datos de acceso de YouTube o Google?", "No, y un servicio que los pida ya es un riesgo en sí mismo. Solo necesitamos el identificador público de tu canal."),
            ("¿Está permitido promocionar un vídeo en YouTube?", "Promocionar un vídeo para que la gente lo descubra es lo normal; los canales lo hacen con anuncios todos los días. La línea que marca YouTube está en las visualizaciones artificiales o incentivadas, y nos quedamos en el lado correcto."),
            ("¿Y si no estoy contento?", "Detén la suscripción en tu cuenta y no se cobrará ningún mes más. Tu panel muestra lo que hemos medido, así que puedes juzgar la campaña con datos."),
        ],
    },
    {
        "service": "views",
        "modifier": "shorts",
        "slug": "youtube/visualizaciones/shorts",
        "label": "Visualizaciones de YouTube Shorts",
        "title": "¿Visitas para reels de YouTube? Allí se llaman Shorts | Growsterr",
        "description": "En YouTube, los reels se llaman Shorts. Traemos espectadores reales que siguen viendo tus Shorts, dentro de un paquete mensual con suscriptores. Desde {from_price}.",
        "h1": ("¿Visitas para reels de YouTube? ", "Consigue espectadores de Shorts que siguen mirando."),
        "intro": "Si quieres comprar visitas para reels de YouTube, te refieres a los Shorts: los vídeos cortos y verticales de YouTube. No vendemos visualizaciones de Shorts al por mayor. Llevamos personas reales a tu canal cada día, y quienes disfrutan de tus Shorts los ven, los repiten, les dan like y a veces se suscriben.",
        "hero": {"image": "youtube-viewers", "alt": "Alguien ve un YouTube Short en el móvil y lo deja repetirse"},
        "sections": [
            {
                "h2": "Las visualizaciones baratas de Shorts son fáciles de falsificar y fáciles de leer",
                "p": [
                    "Las visualizaciones baratas de Shorts están por todas partes porque una reproducción se genera en segundos. Lo difícil es lo que pasa después: ¿el espectador siguió mirando, lo repitió, dio like, abrió tu canal? Las reproducciones generadas responden que no a todo, y YouTube las trata como spam.",
                ],
            },
            {
                "h2": "Cómo un espectador de Shorts se convierte en suscriptor",
                "p": [
                    "Los Shorts son una puerta de entrada. Un espectador real al que le gusta uno puede tocar tu nombre, echar un vistazo a tu canal y suscribirse, y desde entonces tus vídeos más largos también pueden llegarle. Ese camino es la razón por la que una visualización de Shorts de una persona vale mucho más que una reproducción.",
                ],
                "image": {"image": "youtube-channel", "alt": "Un creador revisa en el móvil un Short vertical de YouTube antes de publicarlo"},
            },
            {
                "h2": "Cómo sacar más partido a los Shorts que publicas",
                "ul": [
                    "Haz que tus mejores Shorts sean fáciles de encontrar en la página de tu canal, donde llegan los curiosos.",
                    "Enlaza desde tu Short un vídeo largo relacionado, para que los espectadores interesados tengan adónde ir.",
                    "Publica con un ritmo constante, para que los nuevos suscriptores encuentren algo nuevo en cada visita.",
                ],
            },
        ],
        "faqs": [
            ("¿Los reels de YouTube son lo mismo que los Shorts?", "Sí. Reels es el nombre que usa Instagram; en YouTube, el mismo formato corto y vertical se llama Shorts. Todo lo que dice esta página se aplica a los Shorts."),
            ("¿Puedo comprar visualizaciones baratas para un solo Short?", "No hay precio por Short. Un paquete promociona tu canal, y los espectadores eligen los Shorts que quieren ver."),
            ("¿Podéis meter mis Shorts en el feed de Shorts?", "Es una promesa que nadie puede hacer con honestidad, así que no la hacemos. Traemos espectadores reales; cómo reparte YouTube un Short después es decisión suya."),
            ("¿Por qué no dais una cifra de visualizaciones de Shorts?", "Un Short puede repetirse, saltarse o verse en bucle, y una cifra de visualizaciones prometida por adelantado solo se puede cumplir generando reproducciones. Damos rangos mensuales habituales de lo que hace la gente después de mirar: suscribirse, dar like y comentar."),
            ("¿Es seguro comprar visualizaciones de YouTube Shorts?", "A un servicio de bots, no: una reproducción falsa es falsa tanto si el vídeo dura treinta segundos como una hora. Los espectadores reales que eligen tus Shorts son un público normal, publiques el formato que publiques."),
        ],
    },
]
