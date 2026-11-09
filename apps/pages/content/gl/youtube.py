"""Galician YouTube pages: the hub and subscribers ("subscritores"). Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "youtube",
        "label": "YouTube",
        "title": "Paquetes de crecemento para YouTube | Growsterr",
        "description": "Fai medrar a túa canle de YouTube con persoas reais: paquetes mensuais con subscritores, gústames e comentarios de espectadores reais. Desde {from_price} ao mes.",
        "h1": ("Fai medrar a túa canle de YouTube ", "con espectadores reais."),
        "intro": "Paquetes de crecemento mensuais para creadores. Persoas reais descobren a túa canle, miran os teus vídeos e subscríbense cando lles gusta o que ven. O teu panel amosa o que medimos, día a día.",
        "hero": {"image": "youtube-hub", "alt": "Unha canle de YouTube que gaña subscritores, gústames e comentarios de espectadores reais"},
        "sections": [
            {
                "h2": "Os subscritores que miran son os que contan",
                "p": [
                    "YouTube recomenda os vídeos que a xente mira, aos que lles dá gústame e aos que volve. Un subscritor que nunca mira nada é peor ca ningún: reduce a parte do teu público que participa.",
                    "Cada subscritor que traemos é unha persoa que atopou a túa canle e decidiu subscribirse. Os gústames, as visualizacións e os comentarios veñen das mesmas persoas, dentro do teu paquete.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Espectadores miran o vídeo de YouTube dun creador e escriben comentarios"},
            },
            {
                "h2": "Para canles que publican con coidado",
                "p": [
                    "Titoriais, vlogs, música ou gaming: se publicas con regularidade, os espectadores reais dan a cada vídeo novo un mellor arranque. Comeza con {starter_name} e pasa a un paquete superior cando a túa canle estea lista para máis.",
                ],
                "ul": [
                    "Dinos a cidade, a rexión ou o país de onde debe vir o teu público.",
                    "Subscritores, gústames e comentarios chegan xuntos, das mesmas persoas.",
                    "A túa canle segue sendo túa: nunca che pedimos o contrasinal.",
                ],
                "image": {"image": "youtube-channel", "alt": "Un creador edita un vídeo de YouTube no seu estudio da casa"},
            },
        ],
        "faqs": [
            ("Os subscritores son persoas reais?", "Si. Cada subscritor é unha persoa real que atopou a túa canle e decidiu subscribirse. Sen bots, sen contas falsas, nada instantáneo."),
            ("Cantos subscritores trae un paquete?", "Normalmente {starter_audience} subscritores novos ao mes con {starter_name}, {rising_audience} con {rising_name} e {pro_audience} con {pro_name}. Intervalos habituais, non unha cifra fixa."),
            ("Necesitades o meu contrasinal de Google ou de YouTube?", "Nunca. Só necesitamos o identificador da túa canle, e a canle debe ser pública."),
            ("Podo mercar visualizacións ou gústames por separado?", "Non. As visualizacións, os gústames e os comentarios veñen dentro de cada paquete, das mesmas persoas reais que se subscriben."),
            ("Podo cancelar cando queira?", "Si. Os paquetes renóvanse cada mes e podes cancelar desde a túa conta. O mes que xa pagaches segue ata o final."),
        ],
    },
    {
        "service": "subscribers",
        "slug": "youtube/subscritores",
        "label": "Subscritores de YouTube",
        "title": "Subscritores reais de YouTube que miran | Growsterr",
        "description": "Subscritores de YouTube que son persoas reais: espectadores que atoparon a túa canle e decidiron subscribirse, con gústames e comentarios. Desde {from_price}.",
        "h1": ("Subscritores de YouTube ", "que miran de verdade."),
        "intro": "Persoas reais descobren a túa canle, miran os teus vídeos e subscríbense cando lles gusta o que ven. Normalmente {starter_audience} subscritores novos ao mes con {starter_name}, con gústames e comentarios dos mesmos espectadores.",
        "hero": {"image": "youtube-subscribers", "alt": "A páxina dunha canle de YouTube con subscritores novos de espectadores reais"},
        "sections": [
            {
                "h2": "Un subscritor debería ser un espectador",
                "p": [
                    "En YouTube, un subscritor só é útil se mira os teus vídeos. Os subscritores reais ven o teu próximo vídeo, mírano, danlle gústame e ás veces coméntano, e iso é o que YouTube observa para decidir que recomenda.",
                    "Os subscritores bots nunca miran nada. Fan que unha canle pareza máis grande mentres os seus vídeos chegan a menos xente.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Espectadores reais subscríbense a unha canle de YouTube despois de mirar un vídeo"},
            },
            {
                "h2": "Como é un mes",
                "ul": [
                    "Primeiros días: a campaña arrinca e chegan os primeiros espectadores.",
                    "Cada semana: subscritores novos, gústames e comentarios, uns poucos cada día.",
                    "Ao final do mes: normalmente {pick_audience} subscritores novos con {pick_name}.",
                ],
            },
            {
                "h2": "De onde veñen os teus espectadores",
                "p": [
                    "Dinos a cidade, a rexión ou o país de onde debe vir o teu público. Amosamos a túa canle primeiro a persoas reais de alí; onde o público máis afín é maior nas proximidades, poden chegar máis desa zona.",
                ],
            },
        ],
        "faqs": [
            ("Con que rapidez chegan os subscritores?", "Un pouco cada día, ao longo de todo o mes. Nunca todo de vez: as persoas reais subscríbense ao seu ritmo."),
            ("Mirarán os meus vídeos?", "Son persoas reais que decidiron subscribirse despois de ver a túa canle. O que miren despois decídeno elas, como calquera público, e precisamente por iso conta."),
            ("Tamén recibo gústames e comentarios?", "Si, dos mesmos espectadores: normalmente {pick_likes} gústames e {pick_comments} comentarios ao mes con {pick_name}."),
            ("Necesitades o meu contrasinal?", "Nunca. Só necesitamos o identificador da túa canle, e a canle debe ser pública."),
        ],
    },
]
