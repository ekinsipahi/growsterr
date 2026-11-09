"""European Portuguese YouTube pages: the hub and subscribers ("subscritores"). Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "youtube",
        "label": "YouTube",
        "title": "Pacotes de crescimento para YouTube | Growsterr",
        "description": "Faz crescer o teu canal de YouTube com pessoas reais: pacotes mensais com subscritores, gostos e comentários de espectadores reais. Desde {from_price} por mês.",
        "h1": ("Faz crescer o teu canal de YouTube ", "com espectadores reais."),
        "intro": "Pacotes de crescimento mensais para criadores. Pessoas reais descobrem o teu canal, veem os teus vídeos e subscrevem-no quando gostam do que veem. O teu painel mostra o que medimos, dia a dia.",
        "hero": {"image": "youtube-hub", "alt": "Um canal de YouTube a ganhar subscritores, gostos e comentários de espectadores reais"},
        "sections": [
            {
                "h2": "Os subscritores que veem são os que contam",
                "p": [
                    "O YouTube recomenda os vídeos que as pessoas veem, de que gostam e a que voltam. Um subscritor que nunca vê nada é pior do que nenhum: reduz a parte do teu público que participa.",
                    "Cada subscritor que trazemos é uma pessoa que encontrou o teu canal e decidiu subscrevê-lo. Os gostos, as visualizações e os comentários vêm das mesmas pessoas, dentro do teu pacote.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Espectadores veem o vídeo de YouTube de um criador e escrevem comentários"},
            },
            {
                "h2": "Para canais que publicam com cuidado",
                "p": [
                    "Tutoriais, vlogs, música ou gaming: se publicas com regularidade, espectadores reais dão a cada novo vídeo um melhor arranque. Começa com o {starter_name} e sobe de pacote quando o teu canal estiver pronto para mais.",
                ],
                "ul": [
                    "Dizes-nos a cidade, a região ou o país de onde deve vir o teu público.",
                    "Subscritores, gostos e comentários chegam juntos, das mesmas pessoas.",
                    "O teu canal continua a ser teu: nunca pedimos a tua palavra-passe.",
                ],
                "image": {"image": "youtube-channel", "alt": "Um criador a editar um vídeo de YouTube no seu estúdio em casa"},
            },
        ],
        "faqs": [
            ("Os subscritores são pessoas reais?", "Sim. Cada subscritor é uma pessoa real que encontrou o teu canal e decidiu subscrevê-lo. Sem bots, sem contas falsas, nada instantâneo."),
            ("Quantos subscritores traz um pacote?", "Normalmente {starter_audience} novos subscritores por mês com o {starter_name}, {rising_audience} com o {rising_name} e {pro_audience} com o {pro_name}. Intervalos habituais, não uma quantidade fixa."),
            ("Precisam da minha palavra-passe do Google ou do YouTube?", "Nunca. Só precisamos do identificador do teu canal, e o teu canal deve ser público."),
            ("Posso comprar visualizações ou gostos à parte?", "Não. As visualizações, os gostos e os comentários vêm em todos os pacotes, das mesmas pessoas reais que subscrevem o teu canal."),
            ("Posso cancelar quando quiser?", "Sim. Os pacotes renovam-se todos os meses e podes cancelar na tua conta. O mês que já pagaste continua até ao fim."),
        ],
    },
    {
        "service": "subscribers",
        "slug": "youtube/subscritores",
        "label": "Subscritores no YouTube",
        "title": "Subscritores reais no YouTube que veem mesmo | Growsterr",
        "description": "Subscritores no YouTube que são pessoas reais: espectadores que encontraram o teu canal e decidiram subscrevê-lo, com gostos e comentários. Desde {from_price}.",
        "h1": ("Subscritores no YouTube ", "que veem mesmo os teus vídeos."),
        "intro": "Pessoas reais descobrem o teu canal, veem os teus vídeos e subscrevem-no quando gostam do que veem. Normalmente {starter_audience} novos subscritores por mês com o {starter_name}, com gostos e comentários dos mesmos espectadores.",
        "hero": {"image": "youtube-subscribers", "alt": "A página de um canal de YouTube com novos subscritores vindos de espectadores reais"},
        "sections": [
            {
                "h2": "Um subscritor devia ser um espectador",
                "p": [
                    "No YouTube, um subscritor só é útil se vir os teus vídeos. Os subscritores reais veem o teu próximo vídeo, põem gosto e às vezes comentam, e é isso que o YouTube observa quando decide o que recomendar.",
                    "Os subscritores bots nunca veem nada. Fazem um canal parecer maior enquanto os seus vídeos chegam a menos pessoas.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Espectadores reais subscrevem um canal de YouTube depois de verem um vídeo"},
            },
            {
                "h2": "Como é um mês",
                "ul": [
                    "Primeiros dias: a tua campanha arranca e chegam os primeiros espectadores.",
                    "Todas as semanas: novos subscritores, gostos e comentários, alguns por dia.",
                    "No fim do mês: normalmente {pick_audience} novos subscritores com o {pick_name}.",
                ],
            },
            {
                "h2": "De onde vêm os teus espectadores",
                "p": [
                    "Diz-nos a cidade, a região ou o país de onde deve vir o teu público. Mostramos o teu canal primeiro a pessoas reais nesse local; onde o público mais adequado for maior nas proximidades, podem vir mais de lá.",
                ],
            },
        ],
        "faqs": [
            ("Com que rapidez chegam os subscritores?", "Um pouco todos os dias, ao longo do mês inteiro. Nunca tudo de uma vez: as pessoas reais subscrevem ao seu ritmo."),
            ("Vão ver os meus vídeos?", "São pessoas reais que decidiram subscrever o teu canal depois de o verem. O que veem a seguir é decisão delas, como acontece com qualquer público, e é precisamente por isso que conta."),
            ("Também recebo gostos e comentários?", "Sim, dos mesmos espectadores: normalmente {pick_likes} gostos e {pick_comments} comentários por mês com o {pick_name}."),
            ("Precisam da minha palavra-passe?", "Nunca. Só precisamos do identificador do teu canal, e o teu canal deve ser público."),
        ],
    },
]
