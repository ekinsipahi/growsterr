"""Spanish (Spain) Instagram pages: comments, likes, and the ways people ask for followers and
likes (progresivos, orgánicos, locales, cuenta privada...). Keys and placeholders: docs/CONTENT.md.
Numbers come from the packages ({starter_likes}...), so they follow apps/growth/plan.py."""

UPDATED = "2026-11-08"

PAGES = [
    # --- Comentarios ----------------------------------------------------------------------
    {
        "service": "comments",
        "slug": "instagram/comentarios",
        "label": "Comentarios de Instagram",
        "title": "Comprar comentarios de Instagram de personas reales | Growsterr",
        "description": "¿Quieres comprar comentarios de Instagram? Los nuestros vienen en cada paquete mensual, escritos por personas reales. Normalmente {starter_comments} al mes.",
        "h1": ("Comprar comentarios de Instagram ", "de gente que lo dice en serio."),
        "intro": "Si has llegado aquí para comprar comentarios de Instagram, debes saber que solo los traemos de una forma: dentro de un paquete mensual, de personas reales que descubren tus publicaciones y tienen algo que decir. Normalmente {starter_comments} comentarios al mes con {starter_name} y {pick_comments} con {pick_name}.",
        "hero": {"image": "instagram-real-people", "alt": "Personas dejando sus propios comentarios, preguntas y emojis bajo una publicación de Instagram"},
        "sections": [
            {
                "h2": "Cómo es una sección de comentarios real",
                "p": [
                    "Los comentarios reales son desiguales. Alguien pregunta de dónde es la chaqueta, otra persona etiqueta a una amiga y otra escribe dos palabras y un emoji. Esa irregularidad es lo que hace creíble una sección de comentarios, y es justo lo que los comentarios con guion no pueden imitar.",
                    "Los comentarios comprados al por mayor suelen llegar como frases casi idénticas desde cuentas sin publicaciones propias. Cualquiera que haga scroll los detecta, también las marcas y los colaboradores a los que te gustaría impresionar.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "Un creador en su escritorio respondiendo a los comentarios de una publicación de Instagram"},
            },
            {
                "h2": "Cuántos comentarios trae cada paquete",
                "ul": [
                    "{starter_name}, por {starter_price} al mes, trae normalmente {starter_comments} comentarios, en las publicaciones que más gustan.",
                    "{rising_name}, por {rising_price}, trae normalmente {rising_comments}, y tú eliges las publicaciones que reciben la atención.",
                    "{pro_name}, por {pro_price}, trae normalmente {pro_comments}, además de posición prioritaria y una línea directa por WhatsApp.",
                ],
            },
            {
                "h2": "Por qué los comentarios solo vienen con un paquete",
                "p": [
                    "Una publicación con cuarenta comentarios y una docena de likes le cuenta a todo el mundo lo que pasó. Los comentarios solo encajan junto a los nuevos seguidores, los likes y las visualizaciones que trae la atención real, así que nosotros traemos la atención y dejamos que los comentarios surjan de ella.",
                ],
            },
        ],
        "faqs": [
            ("¿Puedo conseguir comentarios de Instagram sin un paquete?", "No. Los comentarios solo vienen dentro de nuestros paquetes mensuales, de personas que encontraron tu perfil a través de nuestras campañas. Nadie los escribe por encargo, y por eso se leen como una conversación."),
            ("¿Puedo elegir lo que dicen los comentarios?", "No. Las personas escriben con sus propias palabras, así que no hay nada que podamos guionizar, y un comentario escrito según unas instrucciones rara vez parece la reacción real de nadie. Lo que sí puedes elegir, con {rising_name} o {pro_name}, es adónde va la atención: las publicaciones que tú decidas."),
            ("¿Cuándo aparecen los comentarios?", "A lo largo del mes, unos pocos cada vez, a medida que la gente descubre tus publicaciones. Cien comentarios en diez minutos serían un script, no un público."),
            ("¿Los comentarios ayudan a que mis publicaciones lleguen a más gente?", "Los comentarios muestran que a la gente le importa una publicación, e Instagram se da cuenta. Los reales suman. No podemos prometer alcance, y nadie honesto puede, pero los comentarios con guion solo añaden ruido."),
            ("¿Necesitáis mi contraseña?", "No. Necesitamos tu nombre de usuario de Instagram y el lugar del que debe venir tu público. Mantén la cuenta pública para que la gente pueda leer tus publicaciones y participar."),
        ],
    },
    # --- Seguidores: las formas en que la gente los pide -----------------------------------
    {
        "service": "followers",
        "modifier": "gradual",
        "slug": "instagram/seguidores/progresivos",
        "label": "Seguidores de Instagram progresivos",
        "title": "Comprar seguidores de Instagram poco a poco | Growsterr",
        "description": "Compra seguidores de Instagram cada día, no de golpe: personas reales encuentran tu perfil durante 30 días, así que el crecimiento es progresivo por naturaleza.",
        "h1": ("Comprar seguidores de Instagram poco a poco, ", "como sigue la gente de verdad."),
        "intro": "Si prefieres comprar seguidores de Instagram poco a poco en lugar de todos de golpe, ya piensas como un público. Nuestras campañas muestran tu perfil a personas reales cada día durante 30 días, así que los seguidores llegan de forma progresiva, día tras día: normalmente {pick_audience} a lo largo del mes con {pick_name}.",
        "hero": {"image": "instagram-followers-1000", "alt": "Un contador de seguidores que sube un poco cada día a lo largo de un mes"},
        "sections": [
            {
                "h2": "El goteo es un ajuste. El crecimiento diario es una campaña.",
                "p": [
                    "Algunos servicios venden un goteo lento: un lote de cuentas que se suelta poco a poco para que la curva parezca natural. Las cuentas siguen siendo bots; lo único que se disimula es el ritmo.",
                    "Nuestro ritmo no es ningún ajuste. Tu perfil se muestra a personas cada día, y cada nuevo seguidor llega cuando alguien lo decide. La curva progresiva es simplemente lo que se ve desde fuera cuando son personas las que eligen.",
                ],
            },
            {
                "h2": "Por qué poco a poco es mejor que todo de golpe",
                "ul": [
                    "Una subida constante parece lo que es: una cuenta que la gente sigue descubriendo.",
                    "Los nuevos seguidores de cada día ven tu próxima publicación mientras su interés está fresco.",
                    "No hay un pico repentino que una marca, o un seguidor, pueda poner en duda.",
                    "Puedes ver qué funciona, porque cada día es un dato por sí mismo.",
                ],
            },
            {
                "h2": "Cómo leer tus cifras diarias",
                "p": [
                    "Tu panel muestra, para cada día, cuántas personas visitaron tu perfil a través de la campaña y cuántas de ellas te siguieron. Hay días con más movimiento que otros: una publicación fuerte, un fin de semana, un festivo. A lo largo del mes, esos días suman un rango habitual, no una cuota diaria fija.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "Un creador revisa un gráfico diario de visitas al perfil y nuevos seguidores"},
            },
        ],
        "faqs": [
            ("¿Cuántos seguidores tendré cada día?", "No hay una cifra diaria fija, porque las personas deciden por sí mismas. A lo largo del mes, {pick_name} trae normalmente {pick_audience}, así que un día medio trae una parte de eso: unos días más, otros menos."),
            ("¿Puedo ajustar yo la velocidad del goteo?", "No, y no te hace falta. La velocidad la marcan las personas, no un regulador: la campaña funciona cada día y los seguidores llegan cuando alguien decide seguirte."),
            ("¿Es menos arriesgado crecer poco a poco que de golpe?", "Cientos de seguidores en una hora es el rastro que dejan los bots. El crecimiento progresivo de personas reales no deja ese rastro, porque no es un patrón fabricado. No podemos hablar por Instagram sobre cómo trata cada cuenta; solo podemos asegurarnos de que cada seguidor que traemos es una persona."),
            ("¿Progresivo significa crecer menos?", "No. Progresivo describe la forma, no el total. El rango habitual del mes es el mismo tanto si alguien te sigue el día dos como el día veintinueve; simplemente llega como se construye un público."),
            ("¿Los likes y los comentarios también llegan poco a poco?", "Sí. Las mismas personas dan like y comentan a medida que encuentran tus publicaciones, así que ambos crecen junto a tus seguidores. Con {pick_name}, eso suma normalmente {pick_likes} likes y {pick_comments} comentarios a lo largo del mes."),
        ],
    },
    {
        "service": "followers",
        "modifier": "live",
        "slug": "instagram/seguidores/directo",
        "label": "Seguidores de Instagram: entrega y directos",
        "title": "Comprar seguidores de Instagram con entrega rápida | Growsterr",
        "description": "¿Cómo de rápida es la entrega si compras seguidores de Instagram reales? La campaña arranca enseguida, crece cada día y crea un público para tus directos.",
        "h1": ("¿Seguidores de Instagram con entrega rápida? ", "Esto es lo que significa rápido."),
        "intro": "Comprar seguidores de Instagram con entrega rápida suele significar una de dos cosas: un contador que se dispara en minutos o una campaña que arranca enseguida y no se detiene. Nosotros solo hacemos lo segundo. Tu campaña empieza pronto, las personas reales llegan desde los primeros días y tu panel muestra lo que trajo cada día.",
        "hero": {"image": "instagram-creator-studio", "alt": "Un creador se prepara en su escritorio para emitir en directo en Instagram"},
        "sections": [
            {
                "h2": "Rápido donde importa, nunca instantáneo",
                "p": [
                    "La parte rápida es el arranque. Ponemos en marcha tu campaña poco después del pedido, y la gente empieza a ver tu perfil desde los primeros días. Lo que no haremos es meter un mes de decisiones reales en una hora, porque la única forma de hacerlo es con cuentas que no usa nadie.",
                    "Así que, cuando compares plazos de entrega, fíjate en cuándo empieza el crecimiento real y en si continúa, no en lo rápido que salta una cifra.",
                ],
            },
            {
                "h2": "Seguidores para tus directos de Instagram",
                "p": [
                    "Los seguidores para directos son simplemente seguidores que aparecen cuando emites. Instagram puede avisar a tus seguidores cuando empieza una emisión, así que más personas que decidieron seguirte significa más personas que podrían entrar.",
                    "No vendemos espectadores para directos, y nadie puede prometer público a una hora concreta: la gente entra cuando le interesa y está conectada. Los seguidores que ganas durante el mes son los que más probabilidades tienen de hacerlo.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Seguidores se unen al directo de Instagram de un creador y comentan mientras emite"},
            },
            {
                "h2": "Entrega progresiva también para los likes",
                "p": [
                    "Los likes siguen el mismo ritmo. Vienen de las personas que descubren tu perfil, así que llegan a tus publicaciones poco a poco durante el mes, normalmente {pick_likes} con {pick_name}. No hay un pedido de likes aparte que programar ni un pico que explicar.",
                ],
            },
        ],
        "faqs": [
            ("¿Cuándo empieza la entrega?", "Enseguida. Una vez hecho el pedido, ponemos en marcha la campaña y la gente empieza a visitar tu perfil desde los primeros días. Los nuevos seguidores llegan con esas visitas y continúan todo el mes."),
            ("¿Puedo tener entrega instantánea?", "No. La entrega instantánea solo funciona con bots, porque ninguna persona sigue una cuenta segundos después de un pago. Nosotros empezamos rápido y crecemos cada día."),
            ("¿Tendré nuevos seguidores antes de mi directo de esta noche?", "Puede que algunos, si tu campaña ya está en marcha, pero no podemos hacer que las personas lleguen a la hora de una emisión. Si un directo te importa, empieza unas semanas antes para que tus nuevos seguidores hayan tenido tiempo de conocerte."),
            ("¿Vendéis espectadores para directos de Instagram?", "No. Los espectadores de un directo tendrían que ser personas mirando en un minuto concreto, y eso nadie lo puede entregar con honestidad. Los seguidores que traemos pueden unirse a tus directos por su cuenta."),
            ("¿Dónde puedo seguir la entrega?", "En tu panel, que cuenta las visitas al perfil que trajo nuestra campaña y los nuevos seguidores que salieron de ellas, día a día. El total de tu cuenta también se mueve con el resto de tu crecimiento y con quienes dejan de seguirte."),
        ],
    },
    {
        "service": "followers",
        "modifier": "no-drop",
        "slug": "instagram/seguidores/permanentes",
        "label": "Seguidores de Instagram que se quedan",
        "title": "Seguidores permanentes en Instagram: personas reales | Growsterr",
        "description": "¿Quieres seguidores de Instagram permanentes que no se caigan? Las cuentas bot desaparecen en las limpiezas. Las personas se quedan: seguirte fue idea suya.",
        "h1": ("Los seguidores de Instagram permanentes ", "empiezan por personas reales."),
        "intro": "Quien busca comprar seguidores de Instagram permanentes ya ha visto el otro tipo: un salto y después una fuga lenta hacia abajo. Los seguidores se caen cuando nunca fueron personas. Los nuestros son personas que decidieron seguirte, así que se quedan como se queda cualquier público real, y cuando alguien se va, es por los mismos motivos por los que se va cualquier seguidor.",
        "hero": {"image": "instagram-followers", "alt": "Un contador de seguidores de Instagram que se mantiene y sigue subiendo durante varios meses"},
        "sections": [
            {
                "h2": "Por qué se caen los seguidores comprados",
                "p": [
                    "Instagram elimina con regularidad cuentas falsas y de spam. Cuando tus seguidores son esas cuentas, cada limpieza le da un mordisco a tu cifra. Las reposiciones vuelven a subir el número con más de lo mismo, y el ciclo empieza otra vez.",
                    "A una persona no se la lleva una limpieza. Solo se va si decide dejar de seguirte, algo que pasa mucho menos y en lo que tus publicaciones pueden influir.",
                ],
            },
            {
                "h2": "Qué hace que los seguidores se queden",
                "ul": [
                    "Te eligieron, y quien empieza a seguirte por interés suele quedarse.",
                    "Vienen de donde vive tu público, así que tus publicaciones tienen sentido para ellos.",
                    "Ven tus próximas publicaciones, y cada una buena es un motivo para quedarse.",
                    "Tu ritmo importa más que cualquier cosa que hagamos nosotros: la gente se queda por publicaciones que espera con ganas.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Seguidores de hace tiempo siguen dando like y comentando la última publicación de un creador"},
            },
            {
                "h2": "Sin bajadas, dicho con honestidad",
                "p": [
                    "No te diremos que nadie dejará nunca de seguirte, porque las personas no funcionan así. Sí podemos decirte que no verás las oleadas de pérdidas que causan las cuentas falsas, y tu panel muestra los nuevos seguidores que trajo nuestra campaña, día a día, así que siempre sabes qué vino de nosotros.",
                ],
            },
        ],
        "faqs": [
            ("¿Vuestros seguidores son permanentes?", "Son personas reales, así que se quedan mientras quieran. Nadie puede prometer que una persona no deje nunca de seguirte; lo que sí podemos decir es que ninguna de ellas es una cuenta falsa esperando a que la borren."),
            ("¿Ofrecéis reposición si se caen seguidores?", "No, porque no hay nada que reponer. Las reposiciones existen para seguidores que desaparecen en las limpiezas. Los nuestros son personas, y que alguien deje de seguirte de vez en cuando forma parte de cualquier público real."),
            ("¿Por qué desaparecen los seguidores comprados?", "Normalmente no es que dejen de seguirte: es que eliminan las cuentas. Instagram borra perfiles falsos y de spam por oleadas, y tu cifra de seguidores cae con ellos."),
            ("¿Qué pasa con mis seguidores si cancelo?", "Se quedan. Te siguieron porque quisieron, no porque una suscripción se lo mandara. Cancelar solo significa que dejamos de traer personas nuevas cuando termina tu mes pagado; las que has ganado siguen siendo tus seguidores."),
            ("¿Cómo mantengo los seguidores que gano?", "Publica con regularidad, responde a los comentarios y dales a los nuevos seguidores un motivo para volver en sus primeras semanas. La gente se queda por las mismas razones por las que te siguió."),
        ],
    },
    {
        "service": "followers",
        "modifier": "organic",
        "slug": "instagram/seguidores/organicos",
        "label": "Seguidores orgánicos de Instagram",
        "title": "Seguidores orgánicos de Instagram: pagas por alcance | Growsterr",
        "description": "¿Se pueden comprar seguidores orgánicos de Instagram? Puedes pagar para que personas reales te vean cada día, donde elijas. Seguirte sigue siendo decisión suya.",
        "h1": ("¿Comprar seguidores orgánicos de Instagram? ", "Paga por alcance y deja que la gente elija."),
        "intro": "En sentido estricto, nadie puede comprar seguidores orgánicos de Instagram: un seguidor es orgánico porque una persona lo eligió. Lo que sí puedes comprar es alcance. Cada día, personas reales del lugar que elijas se encuentran con tu perfil a través de nuestras campañas, y cada nuevo seguidor que sale de ahí es una decisión que alguien tomó por su cuenta.",
        "hero": {"image": "instagram-real-people", "alt": "Personas se encuentran con el perfil de Instagram de un creador y deciden seguirlo"},
        "sections": [
            {
                "h2": "Dónde termina lo pagado y empieza lo orgánico",
                "p": [
                    "Nuestras campañas son promocionadas: pagamos para poner tu perfil delante de personas de nuestra red de socios. Esa parte es de pago, y lo decimos. Todo lo que viene después no lo es. A nadie se le pide que te siga, y nadie te sigue a cambio de nada.",
                    "Es el mismo trato que un anuncio o una mención en la página de otra persona: pagas por la presentación, y el público decide.",
                ],
            },
            {
                "h2": "Seguidores orgánicos, dirigidos a tu público",
                "p": [
                    "El crecimiento orgánico funciona mejor cuando las personas que te ven tienen motivos para interesarse. Indica la ciudad, la región o el país donde vive tu público, y ahí es donde mostramos tu perfil primero. Una panadería de Valencia y un creador de viajes con seguidores por toda Europa necesitan personas distintas, y apuntamos en consecuencia.",
                ],
            },
            {
                "h2": "Lo que deja fuera lo orgánico",
                "ul": [
                    "Intercambios de «sígueme y te sigo» y grupos de interacción.",
                    "Bots y perfiles falsos, por muy despacio que se suelten.",
                    "Accesos de cualquier tipo: tu contraseña se queda contigo.",
                    "Picos de seguidores más rápidos de lo que podría generar cualquier público real.",
                ],
            },
        ],
        "faqs": [
            ("¿Las campañas de pago son realmente orgánicas?", "El alcance es de pago; seguirte no. Cada nuevo seguidor vio tu perfil y decidió por su cuenta, que es justo lo que hace orgánico a un seguidor."),
            ("¿Tendré seguidores reales de Instagram cada día?", "Sí. La campaña funciona todos los días del mes y la gente te sigue a medida que te descubre. Unos días traen más que otros; a lo largo del mes suele sumar {pick_audience} con {pick_name}."),
            ("¿Es lo mismo que hacer yo anuncios en Instagram?", "Parecido en espíritu, distinto en la práctica. Nosotros llevamos las campañas en nuestra red de socios, nuestro equipo se ocupa de ellas y tú ves en un panel las visitas medidas y los nuevos seguidores. No necesitas una cuenta publicitaria ni un presupuesto que gestionar."),
            ("¿El crecimiento orgánico ayuda a que mis publicaciones lleguen a más gente?", "Más de lo que podrían las cifras compradas, porque los seguidores orgánicos ven tus publicaciones y reaccionan a ellas. Lo lejos que llegue una publicación concreta sigue dependiendo de la publicación."),
            ("¿El crecimiento orgánico es más lento?", "Es más constante. Un mes de crecimiento orgánico llega día a día en lugar de en una hora, y después no viene la caída que traen los picos de bots."),
        ],
    },
    {
        "service": "followers",
        "modifier": "private-account",
        "slug": "instagram/seguidores/cuenta-privada",
        "label": "Seguidores de Instagram para una cuenta privada",
        "title": "Seguidores para una cuenta privada de Instagram | Growsterr",
        "description": "¿Se pueden comprar seguidores de Instagram en una cuenta privada? Ahí solo se pueden enviar solicitudes, así que pedimos un perfil público durante la campaña.",
        "h1": ("¿Seguidores en una cuenta privada de Instagram? ", "Hazla pública mientras creces."),
        "intro": "Si quieres comprar o conseguir seguidores de Instagram en una cuenta privada, este es el inconveniente, dicho con honestidad: la gente no puede seguir una cuenta privada, solo puede pedirlo. Por eso te pedimos que mantengas tu perfil público mientras dura la campaña. Tú sigues decidiendo qué hay en él, y nunca necesitamos tu contraseña.",
        "hero": {"image": "instagram-followers", "alt": "Un perfil privado de Instagram con un candado junto al mismo perfil en modo público"},
        "sections": [
            {
                "h2": "Lo que una cuenta privada le hace a una campaña",
                "p": [
                    "Cuando alguien encuentra un perfil privado, ve un nombre, una biografía y un candado. Puede solicitar seguirlo, pero no puede ver ni una sola publicación, así que la mayoría pasa de largo. Los pocos que envían la solicitud tienen que esperar a que los apruebes, uno a uno.",
                    "Una campaña que manda gente a esa puerta cerrada desperdicia la mayor parte de su alcance. En un perfil público, esas mismas personas pueden ver tus publicaciones, decidirse y seguirte al momento.",
                ],
            },
            {
                "h2": "Si un servicio dice que las cuentas privadas no son un problema",
                "p": [
                    "En una cuenta privada, la cifra de seguidores solo sube cuando se aprueban solicitudes. Si alguien promete seguidores ahí sin que tú apruebes a nadie, tendría que aprobarlos él mismo, desde dentro de tu cuenta. Entregar tu contraseña para eso es lo único que nunca deberías hacer.",
                ],
            },
            {
                "h2": "Hacerte público sin perder el control",
                "ul": [
                    "Cambia a público durante la campaña y vuelve a privado cuando quieras.",
                    "Archiva las publicaciones que prefieras guardarte; no se borra nada.",
                    "Comparte las historias personales con Mejores amigos en lugar de con todo el mundo.",
                    "Quien te siga mientras eres público sigue siendo tu seguidor si vuelves a privado.",
                ],
            },
        ],
        "faqs": [
            ("¿Podéis hacer crecer una cuenta privada de Instagram?", "Solo un poco, así que no lo intentamos. La gente puede solicitar seguirte, pero no ve tus publicaciones, así que pocos lo hacen. Mantén la cuenta pública mientras dura la campaña y podrá hacer su trabajo."),
            ("¿Perderé seguidores si vuelvo a poner la cuenta privada?", "No. Quienes ya te siguen se quedan cuando cambias a privado. Los nuevos visitantes tendrían que enviar una solicitud, así que el crecimiento se frena mientras la cuenta sea privada."),
            ("¿Tengo que aprobar solicitudes de seguimiento?", "No mientras tu cuenta sea pública: la gente te sigue directamente. Si cambias a privado a mitad de mes, las nuevas solicitudes te esperan y la campaña trae muchos menos seguidores."),
            ("¿Necesitáis acceso a mi cuenta para hacerla crecer?", "No. Tus datos de acceso son tuyos; solo necesitamos tu nombre de usuario y un perfil público que puedan ver las personas que enviamos."),
            ("¿Funcionan los likes en una cuenta privada?", "Solo los de quienes ya te siguen, porque nadie más puede ver las publicaciones. Un motivo más por el que la campaña necesita el perfil público."),
        ],
    },
    {
        "service": "followers",
        "modifier": "real",
        "slug": "instagram/seguidores/reales",
        "label": "Seguidores de Instagram activos",
        "title": "Comprar seguidores reales y activos de Instagram | Growsterr",
        "description": "Los seguidores activos de Instagram son personas que dan like, comentan y miran. Los nuestros traen likes y comentarios: normalmente {pick_likes} likes al mes.",
        "h1": ("Comprar seguidores activos de Instagram ", "que de verdad interactúan."),
        "intro": "Cuando alguien quiere comprar seguidores de Instagram activos, se refiere a seguidores que dan like, comentan y miran, no a una cifra que se queda quieta. Eso solo pasa con personas reales, así que es lo único que traemos: personas que descubren tu perfil, deciden seguirte y reaccionan a las publicaciones que les gustan.",
        "hero": {"image": "instagram-real-people", "alt": "Nuevos seguidores de Instagram dan like a una publicación y empiezan una conversación en los comentarios"},
        "sections": [
            {
                "h2": "Parecer real frente a ser real",
                "p": [
                    "Algunos seguidores están hechos para parecer reales: una foto prestada, unas cuantas publicaciones, un nombre creíble. Superan un vistazo rápido y fallan en todo lo demás. Nunca dan like a tu nueva publicación, nunca ven un Reel hasta el final, nunca hacen una pregunta en los comentarios.",
                    "La alta calidad, en el único sentido que importa, significa una persona que podría hacer esas cosas. Las fotos de perfil y las biografías son cosmética; la interacción es la prueba.",
                ],
            },
            {
                "h2": "La actividad llega con los seguidores",
                "p": [
                    "Como nuestros seguidores son personas, la actividad llega con ellos, desde las mismas cuentas. Con {pick_name}, un mes habitual trae {pick_audience} nuevos seguidores junto con {pick_likes} likes y {pick_comments} comentarios.",
                ],
            },
            {
                "h2": "Cómo comprobar si tus seguidores son activos",
                "ul": [
                    "Compara likes y seguidores en tus últimas publicaciones: el crecimiento real mueve ambos.",
                    "Lee los comentarios: los reales hablan de la publicación; los de bots podrían estar debajo de cualquier cosa.",
                    "Abre unos cuantos perfiles de tus nuevos seguidores: los de personas reales son irregulares y concretos.",
                    "Observa el total durante unas semanas: los seguidores activos no desaparecen por oleadas.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "Un creador compara los likes y comentarios de sus últimas publicaciones de Instagram"},
            },
        ],
        "faqs": [
            ("¿Qué hace que un seguidor sea activo?", "Que sea una persona que ve tus publicaciones y a veces reacciona: un like, un comentario, un Reel visto, un envío a un amigo. Nadie reacciona a todas las publicaciones, y es normal."),
            ("¿Mis nuevos seguidores darán like a mis publicaciones?", "Muchos sí. Los likes vienen de las mismas personas que te siguen, y con {pick_name} suelen sumar {pick_likes} al mes. La gente da like a lo que le gusta, así que tus mejores publicaciones reúnen más."),
            ("¿Son seguidores de buena calidad?", "Son personas que decidieron seguirte, desde el lugar que indicaste. No clasificamos a los seguidores por lo pulidos que estén sus perfiles; nos importa que haya alguien detrás de cada uno."),
            ("¿Los seguidores parecen reales?", "Son reales, así que parecen usuarios normales de Instagram: sus propias fotos, amigos y costumbres. Algunos perfiles tienen mucho movimiento y otros son discretos, como en cualquier público."),
            ("¿Growsterr es una web real o un revendedor?", "Somos una agencia de crecimiento, parte de Sterr Agency (Sterr Technologies OÜ, Tallin, Estonia), y un equipo lleva cada campaña. Llevamos personas a tu perfil; no revendemos stock de seguidores."),
        ],
    },
    {
        "service": "followers",
        "modifier": "safe",
        "slug": "instagram/seguidores/pagina-fiable",
        "label": "Seguidores de Instagram en una web fiable",
        "title": "Comprar seguidores de Instagram en una web fiable | Growsterr",
        "description": "¿Buscas una web fiable para comprar seguidores de Instagram? Quiénes somos, cómo pagas, qué nunca te pedimos y qué revisar en cualquier servicio.",
        "h1": ("Comprar seguidores de Instagram en una web fiable: ", "así puedes saberlo."),
        "intro": "Antes de comprar seguidores de Instagram en una web que dice ser fiable, es justo preguntar quién hay detrás y qué podría salir mal. Esta es nuestra parte, sin rodeos: quiénes somos, cómo funciona el pago, qué hacemos con tu cuenta (nada) y las comprobaciones que haríamos en cualquier servicio de crecimiento, incluido el nuestro.",
        "hero": {"image": "instagram-hub", "alt": "Un creador de Instagram revisa los datos de un servicio de crecimiento antes de registrarse"},
        "sections": [
            {
                "h2": "A quién le pagas",
                "p": [
                    "Growsterr es un producto de Sterr Agency, gestionada por Sterr Technologies OÜ, una empresa registrada en Tallin (Estonia) con sede central en Turquía. Pagas con tarjeta en la pasarela de pago de Stripe, o con Apple Pay o Google Pay si tu dispositivo lo admite, y los datos de tu tarjeta van a Stripe, no a nosotros.",
                    "Es una suscripción mensual. Puedes cancelarla tú mismo cuando quieras, y la campaña sigue hasta que termina el mes pagado.",
                ],
            },
            {
                "h2": "Qué hacemos con tu cuenta: nada",
                "p": [
                    "Nunca iniciamos sesión, nunca publicamos, nunca seguimos a nadie en tu nombre y nunca tocamos un ajuste. La campaña ocurre fuera de tu cuenta: la gente ve tu perfil en nuestra red de socios y lo visita como visitaría cualquier perfil que alguien le recomendó.",
                ],
            },
            {
                "h2": "Cinco comprobaciones para cualquier servicio de crecimiento",
                "ul": [
                    "¿Te pide la contraseña? Un servicio legítimo nunca la necesita.",
                    "¿Promete miles de seguidores en minutos? Esa velocidad solo viene de bots.",
                    "¿Las cifras son rangos o promesas? A las personas no se las puede contar por adelantado.",
                    "¿Puedes cancelar por tu cuenta, sin escribir a nadie?",
                    "¿Hay un nombre de empresa y un país detrás de la web?",
                ],
            },
        ],
        "faqs": [
            ("¿Growsterr es de fiar?", "Sí. Somos una empresa registrada, el pago funciona solo a través de Stripe y cada campaña la lleva un equipo y se mide en tu panel. Puedes parar cuando quieras desde tu cuenta."),
            ("¿Es seguro para mi cuenta de Instagram?", "No podemos hablar por Instagram, y nadie honesto puede prometer cómo trata una cuenta. Lo que sí podemos decir es que no hacemos lo que pone en riesgo las cuentas: ni accesos, ni bots, ni avalanchas de seguidores."),
            ("¿Qué necesitáis de mí?", "Tu nombre de usuario de Instagram, de dónde deben ser tus nuevos seguidores y un perfil público. Esa es toda la lista."),
            ("¿Puedo fiarme de las cifras que mostráis?", "Son medidas, no estimadas: tu panel muestra las visitas que trajo nuestra campaña y los nuevos seguidores entre ellas, día a día. Antes del pedido damos rangos habituales, nunca promesas, porque las personas deciden por sí mismas."),
            ("¿Me cobraréis después de cancelar?", "No. Cancelar evita que la suscripción se renueve. Conservas el mes que has pagado, y después no se cobra nada."),
        ],
    },
    {
        "service": "followers",
        "modifier": "targeted",
        "slug": "instagram/seguidores/locales",
        "label": "Seguidores de Instagram locales",
        "title": "Comprar seguidores locales de Instagram, por zona | Growsterr",
        "description": "Compra seguidores de Instagram locales de la ciudad, la región o el país que indiques: personas reales que viven donde están tus clientes, cada día del mes.",
        "h1": ("Comprar seguidores de Instagram locales ", "del lugar que tú elijas."),
        "intro": "Una cafetería de Sevilla gana poco con seguidores del otro lado del mundo. Cuando compras seguidores de Instagram locales, el lugar lo es todo, así que es lo primero que preguntamos: ¿de qué ciudad, región o país deben venir tus nuevos seguidores? Después dirigimos tu campaña a las personas que viven allí.",
        "hero": {"image": "instagram-followers", "alt": "Nuevos seguidores de la misma ciudad aparecen en el perfil de Instagram de un negocio local"},
        "sections": [
            {
                "h2": "Por qué lo local importa más que el total",
                "p": [
                    "Para una tienda, un estudio, un restaurante o un creador que conoce a la gente en persona, un seguidor que puede venir vale por varios que no pueden. Los seguidores locales pueden entrar por la puerta, contárselo a un amigo y reconocer la calle en la que grabaste.",
                    "Además, mantiene tu público coherente. Cuando la mayoría de tus seguidores comparte un lugar y un idioma, más de ellos entienden cada publicación.",
                ],
            },
            {
                "h2": "Cómo funciona la segmentación por ubicación",
                "ul": [
                    "Indicas una ciudad, una región o un país entero al hacer el pedido.",
                    "Mostramos tu perfil primero a personas de allí, todos los días del mes.",
                    "Si el público afín allí es pequeño, algunos seguidores pueden venir de zonas cercanas en lugar de un sitio sin relación.",
                    "Tu contenido hace el resto: la gente te sigue cuando tus publicaciones le hablan.",
                ],
            },
            {
                "h2": "Seguidores del país al que te diriges",
                "p": [
                    "Los seguidores de un país para el que nunca publicas no te ayudan, sea cual sea ese país. Si tus clientes están en Francia, buscamos personas en Francia; si solo están en Madrid, dilo y empezamos por ahí.",
                ],
            },
        ],
        "faqs": [
            ("¿Puedo elegir una ciudad y no solo un país?", "Sí. Funcionan una ciudad, una región o un país entero. Una ciudad da el público más concreto; una región o un país dan a la campaña más personas a las que llegar."),
            ("¿Puedo tener seguidores solo de España y no de otros países?", "Sí. Tú eliges de dónde vienen tus seguidores, y nosotros apuntamos a ese lugar. No hay nada malo en los seguidores de ningún país; la cuestión es si son tu público. Si tus clientes están en España, buscamos personas en España."),
            ("¿Todos los seguidores serán de mi ciudad?", "Mostramos tu perfil allí primero. Cuando el público muy afín es mayor en los alrededores, algunos seguidores pueden venir de esa zona, así que piensa en una campaña apuntada a tu ciudad, no encerrada en ella."),
            ("¿La segmentación local cuesta más?", "No. Todos los paquetes la incluyen, desde {starter_name} por {starter_price} al mes."),
            ("¿Puedo segmentar por edad o intereses?", "Solo segmentamos por ubicación. Dentro de ese lugar, tu contenido decide quién te sigue, porque la gente sigue lo que le interesa."),
            ("¿La segmentación local sirve para un negocio online?", "Sí, si tu público vive en algún sitio concreto: una zona lingüística, un país, un mercado en el que estás entrando. Si tus compradores están repartidos por todo un país, indica el país."),
        ],
    },
    {
        "service": "followers",
        "modifier": "viral",
        "slug": "instagram/seguidores/viral",
        "label": "Seguidores de Instagram para hacerte viral",
        "title": "Seguidores de Instagram para ser viral: lo que ayuda | Growsterr",
        "description": "¿Se pueden comprar seguidores de Instagram para hacerte viral? Nadie puede prometerlo. Los seguidores reales dan a cada publicación más gente que la comparta.",
        "h1": ("¿Comprar seguidores de Instagram para hacerte viral? ", "Haz crecer a quienes comparten."),
        "intro": "Nadie puede venderte una publicación viral, diga lo que diga su web. Lo que hace que una publicación se extienda son las personas: la ven, se la envían a un amigo, la guardan, e Instagram la muestra a más gente como ellas. Si hacerte viral es el motivo para comprar seguidores de Instagram, compra la parte que puede ayudar: más personas reales que ven primero tu próxima publicación.",
        "hero": {"image": "instagram-followers-1000", "alt": "La línea de seguidores de un creador da un salto tras un Reel popular y luego se mantiene"},
        "sections": [
            {
                "h2": "Por qué una cifra grande no hace que una publicación se extienda",
                "p": [
                    "Una publicación llega lejos cuando quienes la ven primero reaccionan. Miles de seguidores que nunca reaccionan le dan peor arranque que unos cientos que sí lo hacen, porque Instagram ve una publicación que su primer público ignoró.",
                ],
            },
            {
                "h2": "Lo que aportan los seguidores reales a un momento viral",
                "ul": [
                    "Más primeros espectadores para cada publicación: las personas que deciden si llega lejos.",
                    "Compartidos y guardados, que solo pueden dar las personas.",
                    "Un perfil que merece la pena seguir cuando una publicación despega, para que el momento deje algo.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Personas comparten por mensaje la publicación de Instagram de un creador con sus amigos"},
            },
            {
                "h2": "Las probabilidades, con honestidad",
                "p": [
                    "La mayoría de las publicaciones no se hacen virales, ni las nuestras ni las de nadie. El crecimiento constante hace más probable que despeguen las que pueden hacerlo, y que las que no despeguen merezcan igualmente la pena. Ese es el trato que ofrecemos: ninguna promesa de un momento, y un mejor punto de partida para cada publicación.",
                ],
            },
        ],
        "faqs": [
            ("¿Podéis hacer que mi publicación se haga viral?", "No, y desconfía de quien diga que puede. La viralidad depende de la publicación, del momento y de las decisiones de miles de personas. Lo que sí podemos hacer es llevar cada día espectadores reales y nuevos a tu perfil, lo que da a cada publicación un mejor arranque."),
            ("¿Las publicaciones virales traen seguidores?", "A menudo, si el perfil que hay detrás da a la gente un motivo para quedarse. Por eso hacemos crecer el perfil y no una sola publicación: cuando algo despega, los recién llegados encuentran un público activo y un trabajo detrás."),
            ("¿Comprar seguidores ayuda al algoritmo?", "Los bots comprados juegan en tu contra, porque hacen que cada publicación parezca ignorada. Los seguidores reales que reaccionan ayudan a que cada publicación arranque mejor. Ninguna de las dos cosas es un interruptor que puedas pulsar."),
            ("¿Qué paquete encaja con una publicación que creo que puede despegar?", "{rising_name} o {pro_name}. Los dos te permiten indicar qué publicaciones deben recibir más miradas, así que más personas reales ven aquella en la que crees. {pro_name} añade posición prioritaria."),
            ("¿Cuándo notaría la diferencia?", "Tu campaña arranca enseguida y los nuevos seguidores llegan desde los primeros días. Que una publicación despegue nunca tiene fecha; tu crecimiento sí."),
        ],
    },
    # --- Likes ----------------------------------------------------------------------------
    {
        "service": "likes",
        "slug": "instagram/likes",
        "label": "Likes de Instagram",
        "title": "Comprar likes de Instagram de personas reales | Growsterr",
        "description": "Likes de Instagram de personas que vieron tu publicación y les gustó, dentro de cada paquete mensual: normalmente {starter_likes} al mes con {starter_name}.",
        "h1": ("Likes de Instagram ", "de personas a las que les gustó la publicación."),
        "intro": "¿Quieres comprar likes de Instagram para tus publicaciones? Con nosotros nunca se venden sueltos. Cada paquete lleva personas reales a tu perfil, y dan like a las publicaciones que les gustan: {starter_name} trae normalmente {starter_likes} likes al mes y {pick_name}, {pick_likes}, junto con nuevos seguidores y comentarios.",
        "hero": {"image": "instagram-hub", "alt": "Likes de personas reales se acumulan en una cuadrícula de publicaciones de Instagram"},
        "sections": [
            {
                "h2": "Un like es donde empieza todo",
                "p": [
                    "En Instagram, un like suele ser lo primero de varias cosas que hace una persona: abre tu perfil, mira unas cuantas publicaciones más, te sigue, vuelve la semana siguiente. Los likes comprados sueltos se quedan en el primer paso, y una publicación con muchos likes y nada más alrededor se lee justo así.",
                    "Los nuestros vienen de personas que están en ese camino. Por eso llegan junto con nuevos seguidores y comentarios, y no solos.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Una persona da like a una publicación de Instagram y después abre el perfil del creador"},
            },
            {
                "h2": "Likes en las publicaciones que elijas",
                "p": [
                    "Con {starter_name}, los likes llegan donde más gustan, normalmente a tus publicaciones más recientes. {rising_name} y {pro_name} te permiten elegir qué publicaciones reciben la atención, algo útil para un lanzamiento, una colaboración o una publicación que quieres que se vea.",
                ],
            },
            {
                "h2": "Dónde comprar likes de Instagram online en 2026",
                "ul": [
                    "Sin app que instalar ni acceso que compartir: una web que te pide cualquiera de las dos cosas busca el tipo de acceso equivocado.",
                    "Likes que llegan con visualizaciones y nuevos seguidores, no antes que ellos.",
                    "Rangos habituales en lugar de cifras exactas, porque deciden las personas.",
                    "Una empresa con nombre y un pago que reconoces: la nuestra es Sterr Technologies OÜ, y cobra con tarjeta a través de Stripe.",
                ],
            },
        ],
        "faqs": [
            ("¿Puedo comprar likes para una sola publicación?", "No como pedido suelto. Los likes vienen dentro de un paquete mensual, de personas que descubren tu perfil. Con {rising_name} o {pro_name} puedes dirigir esa atención a las publicaciones que elijas."),
            ("¿Hay una app para likes de Instagram?", "No tenemos ninguna, y no la necesitas. Haces el pedido en la web, pagas con Stripe y sigues tu campaña desde tu cuenta en cualquier dispositivo. Nunca necesitamos tus datos de acceso a Instagram."),
            ("¿Cuántos likes trae cada paquete?", "Normalmente {starter_likes} al mes con {starter_name}, {rising_likes} con {rising_name} y {pro_likes} con {pro_name}. Rangos, no recuentos: cada like es la elección de una persona."),
            ("¿Cuándo empiezan los likes?", "En cuanto tu campaña está en marcha y las primeras personas llegan a tu perfil, normalmente en los primeros días. Siguen llegando durante el mes, nunca de golpe."),
            ("¿Siguen importando los likes ahora que se pueden ocultar?", "Instagram permite ocultar el número de likes, así que la cifra en pantalla importa menos que antes. Lo que sigue importando es que la gente interactúe con tus publicaciones, y eso es lo que reflejan los likes reales."),
        ],
    },
    {
        "service": "likes",
        "modifier": "comment-likes",
        "slug": "instagram/likes/likes-en-comentarios",
        "label": "Likes en comentarios de Instagram",
        "title": "Likes para comentarios de Instagram: lo que funciona | Growsterr",
        "description": "¿Quieres comprar likes para comentarios de Instagram? No los vendemos. Quien llega a tus publicaciones lee el hilo y da like a las respuestas que comparte.",
        "h1": ("Los likes en comentarios de Instagram ", "vienen de quien lee el hilo."),
        "intro": "La gente compra likes para comentarios de Instagram por dos motivos: subir un comentario en la publicación de otra persona o hacer que su propia sección de comentarios parezca más animada. No vendemos ninguna de las dos cosas. Llevamos personas reales a tu perfil, y quienes leen tus comentarios pueden dar like, por su cuenta, a las respuestas con las que están de acuerdo.",
        "hero": {"image": "instagram-real-people", "alt": "Un hilo de comentarios animado bajo una publicación de Instagram, con likes en las mejores respuestas"},
        "sections": [
            {
                "h2": "Comentarios en publicaciones de otras personas",
                "p": [
                    "Un comentario con muchos likes cerca de lo alto de la publicación de una cuenta grande puede mandarte visitas, y por eso la gente busca likes para comentarios. Nosotros no hacemos campañas en publicaciones ajenas. Nuestro trabajo ocurre en tu propio perfil: lo mostramos a personas reales, y ellas deciden qué hacer allí.",
                ],
            },
            {
                "h2": "Likes en los comentarios de tus publicaciones",
                "p": [
                    "En tus publicaciones, los likes en comentarios surgen de forma natural en cuanto hay conversación. Las personas que llegan a través de tu campaña leen los comentarios, responden a algunos y dan like a los que comparten, incluidos los tuyos. No contamos esos likes ni los pronosticamos, porque nadie puede predecir a qué respuesta dará like una persona.",
                    "Lo que sí contamos: con {pick_name}, un mes trae normalmente {pick_likes} likes en tus publicaciones y {pick_comments} comentarios.",
                ],
            },
            {
                "h2": "Tres formas de ganar más likes en tus respuestas",
                "ul": [
                    "Responde rápido a los primeros comentarios, mientras la gente sigue en la publicación.",
                    "Responde con algo que merezca la pena leer: un consejo, un detalle, una pregunta de vuelta.",
                    "Fija un comentario que abra la conversación que quieres.",
                ],
            },
        ],
        "faqs": [
            ("¿Vendéis likes para comentarios de Instagram?", "No. Los likes en comentarios, como cualquier otro like, solo vienen de personas que deciden darlos. Nuestros paquetes llevan a esas personas a tus publicaciones; a qué dan like en el hilo es cosa suya."),
            ("¿Podéis subir mi comentario a lo alto de la publicación de otra cuenta?", "No. Solo hacemos crecer tu propio perfil, y no enviamos likes a comentarios en ningún otro sitio."),
            ("¿Mi sección de comentarios tendrá más movimiento?", "Normalmente sí, porque más gente ve tus publicaciones. Con {pick_name} llegan normalmente {pick_comments} comentarios al mes, y los comentarios suelen atraer sus propias respuestas y likes."),
            ("¿Los likes en comentarios cuentan en las cifras del paquete?", "No. Nuestros rangos habituales cuentan los likes en tus publicaciones. Los likes en comentarios concretos se suman a eso cuando la gente los da."),
            ("¿Vais a entrar en mi cuenta?", "No. Nadie de nuestro lado toca tu cuenta, y tu contraseña nunca sale de tus manos. Todo lo que ocurre en tus publicaciones lo hacen personas, desde sus propias cuentas."),
        ],
    },
    {
        "service": "likes",
        "modifier": "gradual",
        "slug": "instagram/likes/progresivos",
        "label": "Likes de Instagram lentos y progresivos",
        "title": "Likes de Instagram lentos que crecen durante días | Growsterr",
        "description": "¿Quieres comprar likes de Instagram lentos y no de golpe? Los nuestros vienen de personas reales que encuentran tus publicaciones a lo largo del mes.",
        "h1": ("Likes de Instagram lentos, ", "porque la gente se toma su tiempo."),
        "intro": "Si buscas comprar likes de Instagram lentos, ya sabes que cientos de likes en dos minutos no cuadran. Lento es lo correcto, pero la velocidad es solo la mitad. Nuestros likes llegan poco a poco porque vienen de personas reales que encuentran tus publicaciones a lo largo de días y semanas, no de una cola programada con un temporizador.",
        "hero": {"image": "instagram-followers-1000", "alt": "Los likes de una publicación de Instagram crecen con suavidad durante varios días"},
        "sections": [
            {
                "h2": "Cómo crecen los likes en una publicación real",
                "p": [
                    "Una publicación suma likes en forma de curva: una primera ola de personas que la ven poco después de que la compartas y luego una cola larga a medida que la encuentran en tu perfil, en un hashtag o en los mensajes de un amigo. Esa cola puede durar semanas.",
                    "Nuestras campañas añaden personas en todos los tramos de esa curva. Visitan tu perfil a lo largo del mes, recorren tus publicaciones y dan like a lo que les gusta, así que las publicaciones antiguas también ganan likes, no solo la más reciente.",
                ],
            },
            {
                "h2": "Por qué un temporizador no es lo mismo que el tiempo",
                "p": [
                    "Los likes de bots que se sueltan despacio resuelven el problema equivocado. El pico desaparece, pero las cuentas que dan los likes siguen sin mirar, seguir ni comentar nunca, y unos likes sin visualizaciones, seguidores ni comentarios alrededor resultan igual de raros a ritmo lento.",
                ],
            },
            {
                "h2": "Cuando lo lento no es lo que buscas",
                "p": [
                    "Si necesitas un muro de likes en una publicación en menos de una hora, somos el servicio equivocado, y preferimos decírtelo ya. Si quieres que cada publicación siga sumando likes de personas a las que les importa, para eso estamos hechos.",
                ],
            },
        ],
        "faqs": [
            ("¿Con qué lentitud llegan los likes?", "Al ritmo al que la gente encuentra tus publicaciones: algunos en los primeros días de tu campaña y más en las semanas siguientes. No hay temporizador ni lotes, así que no hay dos días iguales."),
            ("¿Puedo elegir la velocidad de los likes?", "No, y es a propósito. El ritmo lo marcan las personas que visitan tu perfil. Lo que sí puedes elegir, con {rising_name} o {pro_name}, es qué publicaciones reciben la atención."),
            ("¿Las publicaciones antiguas también recibirán likes?", "A menudo, sí. Quienes descubren tu perfil miran hacia atrás y dan like a lo que les gusta, así que los likes se reparten por tu feed en lugar de amontonarse en una sola publicación."),
            ("¿Los likes lentos parecen más naturales?", "Lo lento solo parece natural cuando hay personas detrás. Los nuestros lo parecen porque las hay: cada like viene con una persona que también puede seguirte o comentar."),
            ("¿Cuántos likes llegan en un mes?", "Con {pick_name}, normalmente {pick_likes} en 30 días. Es un rango, no una cuota, porque la gente da like a su ritmo."),
        ],
    },
    {
        "service": "likes",
        "modifier": "monthly",
        "slug": "instagram/likes/mensuales",
        "label": "Likes de Instagram mensuales",
        "title": "Likes mensuales de Instagram sin pedir post a post | Growsterr",
        "description": "Compra likes de Instagram al mes y no publicación a publicación: una suscripción, personas reales y likes todo el mes. Se renueva sola; cancela cuando quieras.",
        "h1": ("Likes automáticos de Instagram cada mes, ", "de personas, no de un script."),
        "intro": "Si quieres comprar likes automáticos de Instagram cada mes, seguramente quieres dejar de pensar en los likes publicación a publicación. Eso es lo que hace un paquete. Te suscribes una vez, llevamos tu campaña cada día y personas reales dan like a las publicaciones que les gustan durante todo el mes: normalmente {pick_likes} likes con {pick_name}. Se renueva cada mes hasta que canceles.",
        "hero": {"image": "instagram-creator-studio", "alt": "Un creador planifica un mes de publicaciones de Instagram en un calendario de pared"},
        "sections": [
            {
                "h2": "Automático, pero no automatizado",
                "p": [
                    "Los auto likes suelen ser un software que detecta cada nueva publicación y le lanza un número fijo de likes en minutos. Es automático, y cada uno de esos likes viene de una cuenta que no usa nadie.",
                    "Los nuestros son automáticos en otro sentido: no tienes que hacer nada con cada publicación. La campaña sigue funcionando, la gente sigue descubriendo tu perfil y los likes que deja son suyos.",
                ],
            },
            {
                "h2": "Qué cambia con un paquete mensual",
                "ul": [
                    "Un precio al mes, {pick_price} por {pick_name}, en lugar de un pedido por cada publicación.",
                    "Sin cifras que configurar ni horarios que programar.",
                    "Likes en publicaciones nuevas y antiguas por igual, a medida que la gente las encuentra.",
                    "Un mes de likes es un mes de opiniones: ves qué publicaciones gustan de verdad.",
                    "Puedes parar cuando quieras, sin plazo de preaviso.",
                ],
            },
        ],
        "faqs": [
            ("¿Las publicaciones nuevas reciben likes automáticamente?", "Deciden las personas, así que no hay un número fijo por publicación. Las publicaciones nuevas suelen ser por donde empieza la gente, y con {rising_name} o {pro_name} puedes decirnos qué publicaciones deben recibir la atención."),
            ("¿La suscripción se renueva automáticamente?", "Sí. Stripe la renueva cada mes con el método de pago que elegiste. Cancelar lleva un momento desde tu cuenta, y el mes que has pagado sigue hasta el final."),
            ("¿Cuántas publicaciones necesito?", "No hay mínimo, pero los likes vienen de personas que recorren tu perfil, así que unas cuantas publicaciones recientes les dan algo que disfrutar. Publicar durante el mes da a cada nuevo visitante más a lo que dar like."),
            ("¿Puedo cambiar de paquete de un mes a otro?", "Sí. Empieza con el paquete que encaja hoy y sube cuando tus publicaciones estén listas para más gente."),
            ("¿Es lo mismo que un software de auto likes?", "No. Un software que da like a cada publicación con un temporizador usa cuentas sin nadie detrás. Nuestros likes vienen de personas que visitaron tu perfil y disfrutaron de una publicación."),
        ],
    },
    {
        "service": "likes",
        "modifier": "no-drop",
        "slug": "instagram/likes/permanentes",
        "label": "Likes de Instagram que se quedan",
        "title": "Likes de Instagram permanentes que no se caen | Growsterr",
        "description": "¿Quieres likes de Instagram que no se caigan? Los likes desaparecen cuando se eliminan las cuentas que los dieron. Los nuestros son de personas y se quedan.",
        "h1": ("Likes de Instagram que se quedan, ", "porque los dio una persona."),
        "intro": "Los likes desaparecen por un motivo principal: se eliminan las cuentas que los dieron. Si quieres comprar likes de Instagram que se queden, los duraderos vienen de personas. Los nuestros también, así que un like en tu publicación se queda ahí salvo que la persona que lo dio cambie de opinión.",
        "hero": {"image": "instagram-hub", "alt": "Una publicación de Instagram cuyos likes se mantienen semanas después de compartirla"},
        "sections": [
            {
                "h2": "Adónde van los likes que desaparecen",
                "p": [
                    "Un like pertenece a la cuenta que lo dio. Cuando Instagram elimina cuentas falsas o de spam, todos los likes que dejaron se van con ellas, a menudo semanas después del pedido. Una publicación puede perder de la noche a la mañana buena parte de sus likes, y quien la viera antes nota el hueco.",
                ],
            },
            {
                "h2": "Por qué se mantienen los likes de personas",
                "p": [
                    "La cuenta de una persona no cae en una limpieza. Su like se queda en tu publicación mientras ella lo deje ahí, y la gente rara vez vuelve atrás para quitar el like a algo que le gustó.",
                    "Además, los likes reales siguen llegando. Las publicaciones antiguas reciben nuevos likes a medida que más gente encuentra tu perfil, así que la cifra de una publicación puede seguir subiendo mucho después de compartirla.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Nuevos visitantes dan like a una publicación antigua de Instagram semanas después"},
            },
        ],
        "faqs": [
            ("¿Bajarán los likes alguna vez?", "No como bajan los likes comprados. Cada like viene de la cuenta de una persona, así que solo se va si esa persona lo quita o cierra su cuenta, algo raro que ocurre de uno en uno."),
            ("¿Hay un periodo de reposición?", "No hay periodo de reposición porque no se espera ninguna caída. Las reposiciones arreglan un problema que nosotros no creamos."),
            ("¿Los likes en Reels también se quedan?", "Sí. Un like se queda en cualquier publicación, foto, carrusel o Reel, mientras la cuenta que lo dio siga ahí."),
            ("¿Cómo sé si mis likes anteriores venían de bots?", "Busca caídas repentinas tras una limpieza, likes muy por encima de tus visualizaciones y perfiles sin publicaciones propias entre quienes dieron like. Los likes de personas rara vez muestran nada de eso."),
            ("¿Cuántos likes trae un paquete?", "{pick_name} trae normalmente {pick_likes} al mes, repartidos entre las publicaciones que más gustan. Se quedan, y los del mes siguiente se suman."),
        ],
    },
    {
        "service": "likes",
        "modifier": "organic",
        "slug": "instagram/likes/organicos",
        "label": "Likes orgánicos de Instagram",
        "title": "Comprar likes orgánicos de Instagram | Growsterr",
        "description": "Likes orgánicos de Instagram que te dan una opinión honesta: personas reales ven tus publicaciones con nuestras campañas y solo dan like a lo que les gusta.",
        "h1": ("Likes orgánicos de Instagram ", "y lo que te cuentan."),
        "intro": "Cuando compras likes de Instagram orgánicos, recibes algo que los likes comprados no pueden darte: una opinión honesta. Nuestras campañas ponen tus publicaciones delante de personas reales, y solo dan like a lo que les gusta. Algunas publicaciones reunirán muchos más que otras, y esa diferencia te dice lo que quiere tu público.",
        "hero": {"image": "instagram-real-people", "alt": "Personas reaccionan de forma distinta a una fila de publicaciones de Instagram y dan like a unas más que a otras"},
        "sections": [
            {
                "h2": "Que los likes sean desiguales es buena señal",
                "p": [
                    "Los likes comprados son sospechosamente uniformes: cada publicación recibe más o menos la misma cifra, sea cual sea. Los likes orgánicos varían. Un Reel fuerte se adelanta, una foto discreta se queda atrás, y el patrón parece el de un público con opinión propia, porque lo es.",
                ],
            },
            {
                "h2": "Usa tus likes para publicar mejor",
                "ul": [
                    "Compara tus tres mejores publicaciones del mes: ¿qué tienen en común?",
                    "Fíjate en qué formato gusta más: Reels, carruseles o fotos.",
                    "Publica más de lo que funciona y comprueba si los likes acompañan.",
                    "Con {rising_name} o {pro_name}, pon más atención en una publicación que pruebe una idea nueva.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "Un creador ordena sus publicaciones de Instagram del mes pasado según los likes de cada una"},
            },
            {
                "h2": "Cómo llegan los likes orgánicos a tus publicaciones",
                "p": [
                    "Mostramos tu perfil a personas de nuestra red de socios, en la ciudad, la región o el país que elijas. Miran, te siguen si quieren y dan like a las publicaciones que les llaman la atención. A nadie se le pide que dé like a nada.",
                ],
            },
        ],
        "faqs": [
            ("¿Pagar por alcance hace que los likes dejen de ser orgánicos?", "No. Pagar para que te vean es como funciona cualquier anuncio o publicación promocionada. El like en sí sigue siendo la reacción de alguien a tu publicación."),
            ("¿Todas las publicaciones recibirán likes?", "La mayoría de las que gustan, sí, pero no por igual, y de eso se trata. Tus mejores publicaciones suelen reunir más."),
            ("¿Cuántos likes orgánicos puedo esperar?", "Un mes habitual con {pick_name} trae {pick_likes}. El total es un rango; cómo se reparte entre publicaciones depende de quienes las ven."),
            ("¿Los likes orgánicos vienen con seguidores?", "Sí. Quienes dan like a tus publicaciones a menudo también te siguen: normalmente {pick_audience} nuevos seguidores al mes con {pick_name}, y algunos dejan comentarios."),
            ("¿Por qué es mejor que un número fijo por publicación?", "Porque un número fijo no te dice nada. Los likes orgánicos suben y bajan con cada publicación, así que te muestran qué conecta y qué no."),
        ],
    },
    {
        "service": "likes",
        "modifier": "private-account",
        "slug": "instagram/likes/cuenta-privada",
        "label": "Likes de Instagram en una cuenta privada",
        "title": "¿Comprar likes de Instagram en una cuenta privada? | Growsterr",
        "description": "¿Se pueden comprar likes de Instagram en una cuenta privada? Solo tus seguidores aprobados ven sus publicaciones, así que nadie nuevo puede darles like.",
        "h1": ("Los likes en una cuenta privada de Instagram ", "solo pueden venir de tus seguidores."),
        "intro": "Antes de comprar likes de Instagram para una cuenta privada, conoce el límite: en un perfil privado, solo los seguidores aprobados pueden ver tus publicaciones, así que solo ellos pueden darles like. Cualquiera que una campaña lleve a tu perfil se encontraría con un candado. Por eso, mientras dura tu campaña, el perfil debe ser público, y hay buenas formas de mantener la privacidad donde importa.",
        "hero": {"image": "instagram-hub", "alt": "Una publicación de Instagram que solo los seguidores aprobados pueden ver y a la que solo ellos pueden dar like"},
        "sections": [
            {
                "h2": "Quién puede dar like en una cuenta privada",
                "p": [
                    "Solo las personas que has aprobado. Los demás ven tu nombre, tu biografía y tu número de seguidores, pero ni una sola publicación, así que no tienen nada a lo que dar like. Un servicio que prometa likes ahí necesitaría que sus cuentas estuvieran aprobadas antes como seguidoras tuyas, por ti o por alguien que haya iniciado sesión como tú.",
                ],
            },
            {
                "h2": "Mantener la privacidad de forma práctica",
                "ul": [
                    "Ten una segunda cuenta pública para tu trabajo y deja la personal en privado.",
                    "Oculta el número de likes en cualquier publicación si prefieres que la cifra no se vea.",
                    "Desactiva los comentarios en las publicaciones que quieras compartir sin conversación.",
                ],
            },
            {
                "h2": "Qué cambia cuando el perfil es público",
                "p": [
                    "La gente puede ver tus publicaciones y dar like a las que le gustan; con {pick_name}, eso suele suponer {pick_likes} likes al mes, junto con nuevos seguidores y comentarios. Tú sigues decidiendo qué publicas y con quién hablas.",
                ],
            },
        ],
        "faqs": [
            ("¿Pueden dar like en una cuenta privada quienes no me siguen?", "No. Instagram solo muestra las publicaciones de una cuenta privada a los seguidores aprobados, así que nadie más puede darles like."),
            ("¿Tengo que seguir en público después de la campaña?", "No, es tu decisión, y los likes que ya tienen tus publicaciones se quedan. Eso sí, mientras la cuenta sea privada, las personas nuevas no ven tus publicaciones, así que una campaña en marcha no puede traerte likes."),
            ("¿Puedo hacer crecer otra cuenta pública aparte?", "Sí. Una cuenta pública para tu trabajo y una privada para tus amigos funciona bien. Haríamos crecer la pública."),
            ("¿Necesitaréis acceso para aprobar solicitudes?", "No. Tu contraseña se queda contigo, y nunca iniciamos sesión en tu cuenta. En un perfil público no hay nada que aprobar: la gente te sigue y da like directamente."),
            ("¿Puedo ocultar el número de likes y seguir creciendo?", "Sí. Ocultar la cifra solo cambia lo que ven los visitantes en esa publicación. La gente puede seguir dándole like, y tú sigues viendo el número."),
        ],
    },
    {
        "service": "likes",
        "modifier": "real",
        "slug": "instagram/likes/reales",
        "label": "Likes de Instagram reales",
        "title": "Comprar likes reales de Instagram, sin bots | Growsterr",
        "description": "Likes reales de Instagram de personas con sus propias cuentas, nunca bots. Llegan con seguidores y comentarios de las mismas personas, en cada paquete.",
        "h1": ("Likes reales de Instagram, ", "cada uno de una persona que quiso darlo."),
        "intro": "¿Quieres comprar likes reales de Instagram? Un like real viene de alguien que miró tu publicación y le gustó lo que vio. Es el único tipo que traemos. Cada paquete muestra tu perfil a personas, y los likes que dejan llegan junto a nuevos seguidores, comentarios y visualizaciones de las mismas cuentas, así que tu interacción parece realista porque lo es.",
        "hero": {"image": "instagram-real-people", "alt": "Distintas personas, cada una con su propio perfil, dan like a la misma publicación de Instagram"},
        "sections": [
            {
                "h2": "Likes premium, likes de calidad y likes reales",
                "p": [
                    "Muchos vendedores dividen los likes en niveles: los baratos, de cuentas vacías; los premium o de alta calidad, de cuentas con fotos y publicaciones. Los dos niveles son lo mismo con distinta ropa: cuentas que dan like por encargo. Un disfraz mejor no hace que un like sea auténtico.",
                    "La calidad, en un like, significa una sola cosa: que una persona eligió darlo. Todo lo demás es presentación.",
                ],
            },
            {
                "h2": "Likes reales que van más allá del like",
                "p": [
                    "Un like real viene de alguien que también podría seguirte, comentar o ver tu próximo Reel. Por eso los likes reales hacen subir el resto de tus cifras en lugar de quedarse al lado: son un paso en lo que hace una persona, no toda la transacción.",
                ],
            },
            {
                "h2": "Cómo detectar likes que solo parecen reales",
                "ul": [
                    "Los likes se disparan mientras las visualizaciones, los seguidores y los comentarios no se mueven.",
                    "Los perfiles que dan like tienen fotos de stock, pocas publicaciones y miles de cuentas seguidas.",
                    "Llegan cientos a los pocos minutos de publicar y luego nada.",
                    "La cifra baja unas semanas después.",
                ],
            },
        ],
        "faqs": [
            ("¿Vuestros likes de Instagram son de cuentas reales?", "Sí. Cada like viene de la cuenta propia de una persona: alguien que descubrió tu perfil a través de nuestra campaña y disfrutó de la publicación. Sin bots y sin granjas de cuentas."),
            ("¿Vendéis likes premium?", "No vendemos likes por niveles ni sueltos. Cada like que traemos es de una persona, dentro de un paquete mensual; {starter_name}, el más pequeño, trae normalmente {starter_likes} al mes."),
            ("¿Los likes reales aumentarán mi alcance?", "Ayudan como solo puede ayudar la interacción real, porque las personas que hay detrás también pueden seguirte, comentar y compartir. Hasta dónde llega una publicación sigue dependiendo de la propia publicación, así que nunca prometemos alcance."),
            ("¿Por qué algunos likes comprados parecen reales?", "Porque están hechos para eso: fotos de perfil, unas cuantas publicaciones, nombres creíbles. Fíjate en lo que pasa alrededor. Los likes de personas llegan con visualizaciones y nuevos seguidores; los disfrazados llegan solos."),
            ("¿Puedo tener likes reales sin nuevos seguidores?", "No. Los likes llegan como parte del paquete, de personas que encuentran tu perfil, y muchas de ellas también te siguen. Eso es lo que mantiene los likes realistas."),
        ],
    },
    {
        "service": "likes",
        "modifier": "reels",
        "slug": "instagram/likes/reels",
        "label": "Likes para Reels de Instagram",
        "title": "Comprar likes para Reels de Instagram | Growsterr",
        "description": "Compra likes para Reels de Instagram de forma honesta: la gente ve tus vídeos y da like a los que le gustan, así que detrás de cada like hay una visualización.",
        "h1": ("Likes en tus Reels, ", "de personas que de verdad los vieron."),
        "intro": "Antes de comprar likes para Reels de Instagram, conviene saber cuánto vale un like en un Reel que nadie vio: poco. Nuestros likes en Reels vienen de personas reales que descubrieron tu perfil, vieron tus vídeos y dieron like a los que les engancharon, junto con nuevos seguidores y comentarios.",
        "hero": {"image": "instagram-creator-studio", "alt": "Un creador edita un Reel de Instagram con el móvil en su escritorio"},
        "sections": [
            {
                "h2": "En un Reel, primero se mira y después se da like",
                "p": [
                    "Los Reels viven de lo que hacen los espectadores: si lo ven hasta el final, si lo repiten, lo comparten o te siguen. Un like es una señal más entre esas, y significa más cuando llega después de una visualización real.",
                    "Los likes para vídeos comprados sueltos suelen llegar sin reproducciones que los acompañen. Un Reel con más likes que visualizaciones salta a la vista y no dice nada bueno de cómo los consiguió.",
                ],
            },
            {
                "h2": "Cómo conseguir que se vean más tus Reels",
                "ul": [
                    "La gente recorre tu perfil y ve los Reels que le llaman la atención, no solo el más reciente.",
                    "{rising_name} y {pro_name} te permiten poner un Reel concreto delante de más personas.",
                    "Los espectadores vienen del lugar que elijas, así que tu idioma y tus referencias conectan.",
                ],
            },
            {
                "h2": "Haz que cuenten los primeros segundos",
                "p": [
                    "Podemos llevar personas a tus Reels; retenerlas es trabajo del vídeo. Un gancho claro en el primer segundo o dos, subtítulos para quien lo ve sin sonido y un final que invite a volver a verlo ayudan a convertir una visualización en un like.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Espectadores ven un Reel de Instagram hasta el final y pulsan like"},
            },
        ],
        "faqs": [
            ("¿Puedo dirigir los likes a un Reel concreto?", "Sí, con {rising_name} o {pro_name}: eliges qué publicaciones y Reels reciben la atención, y las personas hacen el resto. Con {starter_name}, los espectadores encuentran por su cuenta los Reels que les gustan."),
            ("¿Los likes en Reels vienen con visualizaciones?", "Sí. La gente mira antes de dar like, así que detrás de cada like hay una visualización. No vendemos ni contamos las visualizaciones por separado, porque cada una es una persona que decide mirar."),
            ("¿Esto llevará mi Reel a Explorar?", "Nadie puede prometerlo, y nosotros no lo hacemos. Instagram decide qué aparece en Explorar y en el feed de Reels. Los espectadores que miran y reaccionan dan a un Reel un arranque justo; los likes comprados sin visualizaciones le dan uno extraño."),
            ("¿Mi cuenta tiene que ser pública?", "Sí, mientras dura tu campaña. Quienes no te siguen no pueden ver Reels en una cuenta privada, así que tampoco podrían darles like."),
            ("¿Cuántos likes recibirán mis Reels?", "Con {pick_name}, normalmente {pick_likes} likes al mes entre tus publicaciones y Reels. Cómo se reparten depende de lo que más guste."),
        ],
    },
    {
        "service": "likes",
        "modifier": "safe",
        "slug": "instagram/likes/legitimos",
        "label": "Likes de Instagram legítimos",
        "title": "Comprar likes de Instagram seguros y legítimos | Growsterr",
        "description": "¿Quieres comprar likes de Instagram legítimos? Un like legítimo viene de una persona que vio tu publicación. Cómo reconocerlos y de dónde salen los nuestros.",
        "h1": ("Los likes de Instagram legítimos ", "empiezan con una persona y una publicación."),
        "intro": "¿Buscas comprar likes de Instagram que sean legítimos? Un like legítimo tiene dos partes: una persona real y una publicación que de verdad vio. Todo lo que hacemos gira en torno a ambas. Mostramos tu perfil a personas, y quienes disfrutan de tus publicaciones les dan like, sin accesos, sin bots y sin likes vendidos sueltos.",
        "hero": {"image": "instagram-hub", "alt": "Una persona hace scroll en Instagram y se detiene a dar like a una publicación que le gustó"},
        "sections": [
            {
                "h2": "Señales de alarma en cualquier oferta de likes",
                "ul": [
                    "Un precio por cada mil likes: a las personas no se las compra por millares.",
                    "Entrega en minutos, o la promesa de cifras exactas.",
                    "Que te pidan la contraseña o que inicies sesión a través de una app.",
                    "Likes vendidos sin visualizaciones, seguidores ni comentarios que los acompañen.",
                ],
            },
            {
                "h2": "Por qué los likes falsos no son legítimos, los venda quien los venda",
                "p": [
                    "Las normas de Instagram piden no conseguir likes de forma artificial, y los likes de cuentas que dan like por encargo son exactamente eso. No podemos decir cómo trata Instagram a una cuenta concreta, y no vamos a adivinarlo. Simplemente, no llevamos nada artificial a la tuya.",
                ],
            },
            {
                "h2": "De dónde vienen nuestros likes",
                "p": [
                    "De las personas que nuestras campañas llevan a tu perfil: usuarios de nuestra red de socios, en el lugar que elijas, todos los días del mes. Dan like a lo que les gusta, normalmente {pick_likes} likes al mes con {pick_name}, y muchos también te siguen y comentan.",
                ],
            },
        ],
        "faqs": [
            ("¿Es legítimo comprar likes de Instagram?", "Comprar likes de cuentas que dan like por encargo va contra las normas de Instagram sobre interacción artificial. Lo que vendemos es distinto: alcance hacia personas reales, que deciden por sí mismas si dan like."),
            ("¿Puedo perder mi cuenta por comprar likes?", "No podemos hablar por Instagram, y quien prometa un resultado está adivinando. Lo que controlamos es que cada like que traemos venga de una persona y que nunca tocamos tus datos de acceso."),
            ("¿Cómo pago?", "Con tarjeta, Apple Pay o Google Pay, a través del pago seguro de Stripe. El cobro es mensual y se detiene cuando cancelas."),
            ("¿Me pedís los datos de acceso de Instagram?", "Nunca. Necesitamos tu nombre de usuario para empezar la campaña. Si un servicio de likes te pide la contraseña, vete."),
            ("¿Por qué no vendéis likes por publicación?", "Porque un número fijo de likes en una publicación fija solo puede venir de cuentas que dan like por encargo. Nosotros traemos personas; los likes son lo que hacen cuando les gusta una publicación."),
        ],
    },
    {
        "service": "likes",
        "modifier": "viral",
        "slug": "instagram/likes/viral",
        "label": "Likes de Instagram para hacerte viral",
        "title": "¿Los likes de Instagram te hacen viral? | Growsterr",
        "description": "¿Piensas comprar likes de Instagram para hacerte viral? Los likes solos no hacen que una publicación se extienda; la gente que mira, comparte y guarda, sí.",
        "h1": ("Los likes virales de Instagram ", "son un resultado, no un pistoletazo de salida."),
        "intro": "Mucha gente compra likes de Instagram para que una publicación se haga viral, con la esperanza de que una cifra grande convenza a Instagram, y a todo el mundo, de que merece más atención. Rara vez funciona así. Los likes de personas que vieron y disfrutaron una publicación son señal de impulso; los amontonados en una publicación tranquila no son señal de nada. Traemos los primeros, y no prometemos la parte viral.",
        "hero": {"image": "instagram-followers-1000", "alt": "Likes, compartidos y guardados suben juntos en una publicación de Instagram que empieza a extenderse"},
        "sections": [
            {
                "h2": "Los likes llegan después de que se extienda, no antes",
                "p": [
                    "Cuando una publicación despega, los likes son el rastro visible de miles de personas que la ven, se la envían a sus amigos y la guardan para después. Copia el rastro sin las personas y tendrás la cifra sin el movimiento.",
                ],
            },
            {
                "h2": "Lo que de verdad le da una oportunidad a una publicación",
                "ul": [
                    "Un primer público que reacciona: personas que ven la publicación pronto y le dan like, la comentan o la comparten.",
                    "Un gancho que hace que la gente se detenga, y un motivo para enviársela a alguien.",
                    "Publicar donde está tu público, en su idioma, cuando está haciendo scroll.",
                    "Enfoque: con {rising_name} o {pro_name}, más personas ven la publicación que crees que puede llegar lejos.",
                ],
            },
            {
                "h2": "Lo que prometemos y lo que no",
                "p": [
                    "Prometemos personas reales, cada día, y un panel con lo que hemos medido. No prometemos millones de visualizaciones, un hueco en Explorar ni una publicación que se extienda. Quien lo hace está vendiendo la apariencia de una publicación viral.",
                ],
            },
        ],
        "faqs": [
            ("¿Comprar likes hará que mi publicación se haga viral?", "No por sí solo. La cifra de likes es el resultado de la atención de la gente, y los likes comprados añaden la cifra sin la atención. Los likes de personas que miraron dan a una publicación un arranque honesto, que es lo máximo que alguien puede ofrecer."),
            ("¿Cuántos likes necesita una publicación viral?", "No hay número mágico. Una publicación con una cifra modesta puede llegar lejos si quienes la ven la comparten, y una con una cifra grande puede estancarse."),
            ("¿Enviáis likes en la primera hora después de publicar?", "No sincronizamos los likes con una publicación. La gente llega a lo largo del mes y da like a lo que le gusta. Si una publicación importa más, {rising_name} y {pro_name} te permiten elegir qué publicaciones reciben la atención."),
            ("¿Se incluyen compartidos y guardados?", "No los contamos ni los vendemos, pero ocurren: las personas que dan like a tus publicaciones también pueden compartirlas y guardarlas, algo que los bots nunca hacen."),
            ("¿Una cifra alta de likes hace que otros den más like?", "La gente sí se fija en una publicación con movimiento. Pero una cifra grande sin comentarios ni compartidos parece montada justo a ojos de las personas a las que quieres impresionar."),
        ],
    },
]
