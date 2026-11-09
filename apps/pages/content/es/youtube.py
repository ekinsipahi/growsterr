"""Spanish (Spain) YouTube pages: the hub and subscribers. Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "youtube",
        "label": "YouTube",
        "title": "Paquetes de crecimiento para YouTube | Growsterr",
        "description": "Haz crecer tu canal de YouTube con personas reales: paquetes mensuales con suscriptores, likes y comentarios de espectadores reales. Desde {from_price} al mes.",
        "h1": ("Haz crecer tu canal de YouTube ", "con espectadores reales."),
        "intro": "Paquetes de crecimiento mensuales para creadores. Personas reales descubren tu canal, ven tus vídeos y se suscriben cuando les gusta lo que ven. Tu panel muestra lo que hemos medido, día a día.",
        "hero": {"image": "youtube-hub", "alt": "Un canal de YouTube ganando suscriptores, likes y comentarios de espectadores reales"},
        "sections": [
            {
                "h2": "Los suscriptores que ven tus vídeos son los que cuentan",
                "p": [
                    "YouTube recomienda los vídeos que la gente ve, a los que da like y a los que vuelve. Un suscriptor que nunca ve nada es peor que ninguno: reduce la parte de tu público que participa.",
                    "Cada suscriptor que traemos es una persona que encontró tu canal y decidió suscribirse. Los likes, las visualizaciones y los comentarios vienen de las mismas personas, dentro de tu paquete.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Espectadores ven el vídeo de YouTube de un creador y escriben comentarios"},
            },
            {
                "h2": "Para canales que publican con cuidado",
                "p": [
                    "Tutoriales, vlogs, música o gaming: si publicas con regularidad, los espectadores reales dan a cada nuevo vídeo un mejor arranque. Empieza con {starter_name} y sube de paquete cuando tu canal esté listo para más.",
                ],
                "ul": [
                    "Nos dices la ciudad, la región o el país del que debe venir tu público.",
                    "Suscriptores, likes y comentarios llegan juntos, de las mismas personas.",
                    "Tu canal sigue siendo tuyo: nunca te pedimos la contraseña.",
                ],
                "image": {"image": "youtube-channel", "alt": "Un creador edita un vídeo de YouTube en su estudio en casa"},
            },
        ],
        "faqs": [
            ("¿Los suscriptores son personas reales?", "Sí. Cada suscriptor es una persona real que encontró tu canal y decidió suscribirse. Sin bots, sin cuentas falsas, nada instantáneo."),
            ("¿Cuántos suscriptores trae un paquete?", "Normalmente {starter_audience} nuevos suscriptores al mes con {starter_name}, {rising_audience} con {rising_name} y {pro_audience} con {pro_name}. Rangos habituales, no una cifra fija."),
            ("¿Necesitáis mi contraseña de Google o YouTube?", "Nunca. Solo necesitamos el identificador de tu canal, y tu canal debe ser público."),
            ("¿Puedo comprar visualizaciones o likes por separado?", "No. Las visualizaciones, los likes y los comentarios vienen dentro de cada paquete, de las mismas personas reales que se suscriben."),
            ("¿Puedo cancelar cuando quiera?", "Sí. Los paquetes se renuevan cada mes y puedes cancelar desde tu cuenta. El mes que ya pagaste sigue hasta el final."),
        ],
    },
    {
        "service": "subscribers",
        "slug": "youtube/suscriptores",
        "label": "Suscriptores de YouTube",
        "title": "Suscriptores reales de YouTube que ven tus vídeos | Growsterr",
        "description": "Suscriptores de YouTube que son personas reales: espectadores que encontraron tu canal y decidieron suscribirse, con likes y comentarios. Desde {from_price} al mes.",
        "h1": ("Suscriptores de YouTube ", "que de verdad ven tus vídeos."),
        "intro": "Personas reales descubren tu canal, ven tus vídeos y se suscriben cuando les gusta lo que ven. Normalmente {starter_audience} nuevos suscriptores al mes con {starter_name}, con likes y comentarios de los mismos espectadores.",
        "hero": {"image": "youtube-subscribers", "alt": "La página de un canal de YouTube con nuevos suscriptores de espectadores reales"},
        "sections": [
            {
                "h2": "Un suscriptor debería ser un espectador",
                "p": [
                    "En YouTube, un suscriptor solo sirve si ve tus vídeos. Los suscriptores reales ven tu próxima subida, le dan like y a veces comentan, y eso es lo que YouTube mira para decidir qué recomendar.",
                    "Los suscriptores bot nunca ven nada. Hacen que un canal parezca más grande mientras sus vídeos llegan a menos gente.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Espectadores reales se suscriben a un canal de YouTube después de ver un vídeo"},
            },
            {
                "h2": "Cómo es un mes",
                "ul": [
                    "Primeros días: tu campaña arranca y llegan los primeros espectadores.",
                    "Cada semana: nuevos suscriptores, likes y comentarios, unos pocos cada día.",
                    "Al final del mes: normalmente {pick_audience} nuevos suscriptores con {pick_name}.",
                ],
            },
            {
                "h2": "De dónde vienen tus espectadores",
                "p": [
                    "Dinos la ciudad, la región o el país del que debe venir tu público. Mostramos tu canal primero a personas reales de allí; donde el público más afín es mayor en la zona cercana, pueden llegar más desde allí.",
                ],
            },
        ],
        "faqs": [
            ("¿Con qué rapidez llegan los suscriptores?", "Un poco cada día, durante todo el mes. Nunca todo de golpe: las personas reales se suscriben a su ritmo."),
            ("¿Verán mis vídeos?", "Son personas reales que decidieron suscribirse después de ver tu canal. Lo que vean después lo deciden ellas, como cualquier público, y precisamente por eso cuenta."),
            ("¿También recibo likes y comentarios?", "Sí, de los mismos espectadores: normalmente {pick_likes} likes y {pick_comments} comentarios al mes con {pick_name}."),
            ("¿Necesitáis mi contraseña?", "Nunca. Solo necesitamos el identificador de tu canal, y tu canal debe ser público."),
        ],
    },
]
