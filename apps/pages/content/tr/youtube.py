"""Turkish YouTube pages: the hub and subscribers (mirrors en/youtube.py)."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "youtube",
        "label": "YouTube",
        "title": "İçerik Üreticileri İçin YouTube Büyüme Paketleri | Growsterr",
        "description": "YouTube kanalınızı gerçek insanlarla büyütün: aylık paketler, abone olmayı seçen izleyicilerden abone, beğeni ve yorum getirir. Başlangıç: ayda {from_price}.",
        "h1": ("YouTube kanalınızı ", "gerçek izleyicilerle büyütün."),
        "intro": "İçerik üreticileri için aylık büyüme paketleri. Gerçek insanlar kanalınızı keşfeder, videolarınızı izler ve gördüğünü beğenirse abone olur. Paneliniz ölçtüklerimizi gün gün gösterir.",
        "hero": {"image": "youtube-hub", "alt": "Gerçek izleyicilerden abone, beğeni ve yorum kazanan bir YouTube kanalı"},
        "sections": [
            {
                "h2": "Önemli olan, izleyen abonelerdir",
                "p": [
                    "YouTube, insanların izlediği, beğendiği ve geri döndüğü videoları önerir. Hiç izlemeyen bir abone, hiç olmamasından daha kötüdür: kitlenizin etkileşime giren kısmının oranını düşürür.",
                    "Getirdiğimiz her abone, kanalınızı bulup abone olmayı seçen bir insandır. Beğeni, izlenme ve yorumlar da paketinizin içinde, aynı insanlardan gelir.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Bir içerik üreticisinin YouTube videosunu izleyip yorum yazan izleyiciler"},
            },
            {
                "h2": "Özenle yayın yapan kanallar için",
                "p": [
                    "Eğitim, vlog, müzik ya da oyun: düzenli video yayınlıyorsanız, gerçek izleyiciler her yeni videonuza daha iyi bir başlangıç sağlar. {starter_name} ile başlayın, kanalınız daha fazlasına hazır olduğunda bir üst pakete geçin.",
                ],
                "ul": [
                    "Kitlenizin hangi şehir, bölge ya da ülkeden gelmesini istediğinizi siz söylersiniz.",
                    "Abone, beğeni ve yorumlar aynı insanlardan, birlikte gelir.",
                    "Kanalınız sizin kalır: şifrenizi asla istemiyoruz.",
                ],
                "image": {"image": "youtube-channel", "alt": "Ev stüdyosunda YouTube videosu düzenleyen bir içerik üreticisi"},
            },
        ],
        "faqs": [
            ("Aboneler gerçek insanlar mı?", "Evet. Her abone, kanalınızı bulup abone olmayı seçen gerçek bir insandır. Bot yok, sahte hesap yok, anında gelen hiçbir şey yok."),
            ("Bir paket kaç abone getirir?", "{starter_name} ile genellikle ayda {starter_audience}, {rising_name} ile {rising_audience}, {pro_name} ile {pro_audience} yeni abone. Bunlar sabit sayılar değil, tipik aralıklardır."),
            ("Google ya da YouTube şifremi istiyor musunuz?", "Asla. Yalnızca kanal kullanıcı adınız (@handle) yeterli; kanalınızın herkese açık olması gerekir."),
            ("İzlenme ya da beğeniyi tek başına satın alabilir miyim?", "Hayır. İzlenme, beğeni ve yorumlar her paketin içinde, kanalınıza abone olan aynı gerçek insanlardan gelir."),
            ("İstediğim zaman iptal edebilir miyim?", "Evet. Paketler her ay yenilenir ve hesabınızdan iptal edebilirsiniz. Ödemesini yaptığınız ay sonuna kadar devam eder."),
        ],
    },
    {
        "service": "subscribers",
        "slug": "youtube/abone",
        "label": "YouTube abone",
        "title": "Gerçekten İzleyen YouTube Aboneleri | Growsterr",
        "description": "Gerçek insanlardan YouTube abonesi: kanalınızı bulup abone olmayı seçen izleyiciler, beğeni ve yorumlarla birlikte. Başlangıç: ayda {from_price}.",
        "h1": ("YouTube'da ", "gerçekten izleyen aboneler."),
        "intro": "Gerçek insanlar kanalınızı keşfeder, videolarınızı izler ve gördüğünü beğenirse abone olur. {starter_name} ile genellikle ayda {starter_audience} yeni abone, aynı izleyicilerden gelen beğeni ve yorumlarla birlikte.",
        "hero": {"image": "youtube-subscribers", "alt": "Gerçek izleyicilerden yeni aboneler kazanan bir YouTube kanal sayfası"},
        "sections": [
            {
                "h2": "Abone, aynı zamanda izleyici olmalı",
                "p": [
                    "YouTube'da bir abone ancak izliyorsa işe yarar. Gerçek aboneler bir sonraki videonuzu görür, izler, beğenir ve bazen yorum yapar; YouTube da neyi önereceğine karar verirken buna bakar.",
                    "Bot aboneler hiç izlemez. Kanalı daha büyük gösterirler ama videoları daha az kişiye ulaşır.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Bir videoyu izledikten sonra YouTube kanalına abone olan gerçek izleyiciler"},
            },
            {
                "h2": "Bir ay nasıl geçer?",
                "ul": [
                    "İlk günler: kampanyanız başlar, ilk izleyiciler gelir.",
                    "Her hafta: yeni abone, beğeni ve yorumlar, her gün birkaç tane.",
                    "Ay sonunda: {pick_name} ile genellikle {pick_audience} yeni abone.",
                ],
            },
            {
                "h2": "İzleyicileriniz nereden gelir?",
                "p": [
                    "Kitlenizin hangi şehir, bölge ya da ülkeden gelmesini istediğinizi bize söyleyin. Kanalınızı önce oradaki gerçek insanlara gösteririz; en uygun kitle yakın bölgelerde daha büyükse, izleyicilerin bir kısmı oradan da gelebilir.",
                ],
            },
        ],
        "faqs": [
            ("Aboneler ne kadar hızlı gelir?", "Ayın tamamına yayılarak, her gün biraz. Asla hepsi birden değil: gerçek insanlar kendi hızında abone olur."),
            ("Videolarımı izleyecekler mi?", "Onlar kanalınızı gördükten sonra abone olmayı seçen gerçek insanlar. Sonra ne izleyecekleri, her kitlede olduğu gibi onlara kalmış; değerli olmasının nedeni de tam olarak bu."),
            ("Beğeni ve yorum da geliyor mu?", "Evet, aynı izleyicilerden: {pick_name} ile genellikle ayda {pick_likes} beğeni ve {pick_comments} yorum."),
            ("Şifremi istiyor musunuz?", "Asla. Yalnızca kanal kullanıcı adınız yeterli; kanalınızın herkese açık olması gerekir."),
        ],
    },
]
