"""Turkish TikTok pages: the hub and likes (mirrors en/tiktok.py)."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "tiktok",
        "label": "TikTok",
        "title": "İçerik Üreticileri İçin TikTok Büyüme Paketleri | Growsterr",
        "description": "TikTok'ta gerçek insanlarla büyüyün: aylık paketler, takip etmeyi kendisi seçen insanlardan yeni takipçi, beğeni ve yorum getirir. Başlangıç: ayda {from_price}.",
        "h1": ("TikTok hesabınızı ", "gerçek insanlarla büyütün."),
        "intro": "İçerik üreticileri ve influencer'lar için aylık büyüme paketleri. Gerçek insanlar profilinizi keşfeder, videolarınızı izler ve gördüğünü beğenirse sizi takip eder. Paneliniz ölçtüklerimizi gün gün gösterir.",
        "hero": {"image": "tiktok-hub", "alt": "Yeni takipçi ve beğeniler kazanan bir TikTok içerik üreticisinin profili"},
        "sections": [
            {
                "h2": "TikTok'ta asıl mesele ilgi",
                "p": [
                    "TikTok bir videoyu, ilk izleyenler onu izleyip beğendiğinde, yorum yaptığında ve takip ettiğinde daha çok kişiye gösterir. Arkasında insan olmayan sayılar bunların hiçbirini harekete geçirmez.",
                    "Paketlerimiz her gün profilinize gerçek insanlar getirir. İzlerler, karar verirler; videolarınızdan keyif alanlar takip eder ve beğenir. Bir videonun yayılmasına yardım eden ilgi tam olarak budur.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Bir içerik üreticisinin TikTok videolarını izleyen gerçek izleyiciler"},
            },
            {
                "h2": "Söyleyecek sözü olan içerik üreticileri için",
                "p": [
                    "Komedi, yemek, moda ya da eğitim videoları: düzenli paylaşım yapıyorsanız, gerçek izleyiciler her yeni videonuza daha iyi bir başlangıç sağlar. {starter_name} ile başlayın, hazır olduğunuzda bir üst pakete geçin.",
                ],
                "ul": [
                    "Kitlenizin hangi şehir, bölge ya da ülkeden gelmesini istediğinizi siz söylersiniz.",
                    "Takipçi, beğeni ve yorumlar aynı insanlardan, birlikte gelir.",
                    "Hesabınız sizin kalır: şifrenizi asla istemiyoruz.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Tripoda takılı telefonla TikTok videosu çeken bir içerik üreticisi"},
            },
        ],
        "faqs": [
            ("Takipçiler gerçek insanlar mı?", "Evet. Her takipçi, profilinizi görüp sizi takip etmeyi seçen gerçek bir insandır. Asla bot, sahte hesap ya da anında teslimat kullanmıyoruz."),
            ("Bir paket kaç takipçi getirir?", "{starter_name} ile genellikle ayda {starter_audience}, {rising_name} ile {rising_audience}, {pro_name} ile {pro_audience} yeni takipçi. Bunlar sabit sayılar değil, tipik aralıklardır: gerçek insanlar kendi kararını verir."),
            ("TikTok şifremi istiyor musunuz?", "Asla. Yalnızca kullanıcı adınız yeterli. Hesabınızı herkese açık tutun ki onu keşfeden insanlar sizi takip edebilsin."),
            ("İzlenme ya da beğeniyi tek başına satın alabilir miyim?", "Hayır. İzlenme, beğeni ve yorumlar her paketin içinde, sizi takip eden aynı gerçek insanlardan gelir."),
            ("İstediğim zaman iptal edebilir miyim?", "Evet. Paketler her ay yenilenir ve hesabınızdan iptal edebilirsiniz. Ödemesini yaptığınız ay sonuna kadar devam eder."),
        ],
    },
    {
        "service": "likes",
        "slug": "tiktok/begeni",
        "label": "TikTok beğeni",
        "title": "Gerçek İnsanlardan TikTok Beğenisi, Her Paketin İçinde",
        "description": "Videolarınızı izleyen gerçek insanlardan TikTok beğenisi, asla bot değil. Beğeniler her aylık pakette takipçi ve yorumla gelir. Başlangıç: ayda {from_price}.",
        "h1": ("Gerçek insanlardan TikTok beğenisi. ", "Her paketin içinde."),
        "intro": "Beğeniyi tek başına satmıyoruz. Her paket, profilinizi keşfeden, videolarınızı izleyen ve keyif aldığını beğenen gerçek insanlar getirir: {starter_name} ile genellikle ayda {starter_likes} beğeni.",
        "hero": {"image": "tiktok-likes", "alt": "Bir TikTok videosuna gerçek izleyicilerden gelen beğeniler"},
        "sections": [
            {
                "h2": "Beğeni, arkasında bir insan varsa değerlidir",
                "p": [
                    "TikTok bir beğeninin çevresinde olanlara bakar: izleyen videoyu izlemeye devam etti mi, takip etti mi, geri geldi mi? Botlardan gelen beğeniler bunların hepsine hayır der; bir sayı ekler ama erişiminizden götürür.",
                    "Gerçek insanlardan gelen beğeniler gerisini de getirir: izlenme süresi, takip ve yorum. Bir videonun yayılmasına yardım eden sinyal budur.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Bir TikTok videosunu sonuna kadar izleyip beğenen izleyiciler"},
            },
            {
                "h2": "Her paket kaç beğeni getirir?",
                "ul": [
                    "{starter_name} (ayda {starter_price}): genellikle {starter_likes} beğeni.",
                    "{rising_name} (ayda {rising_price}): genellikle {rising_likes} beğeni, seçtiğiniz videolarda.",
                    "{pro_name} (ayda {pro_price}): genellikle {pro_likes} beğeni, öncelikli yerleşimle.",
                ],
            },
            {
                "h2": "Beğeniyi neden tek başına satmıyoruz?",
                "p": [
                    "İzlenme, takip ya da yorum olmadan gelen beğeniler tam olarak neyse öyle görünür. Paketin içinde her beğeni videoyu izlemiş birinden gelir; böylece rakamlarınız, gerçek büyümede olduğu gibi birlikte hareket eder.",
                ],
            },
        ],
        "faqs": [
            ("Paket olmadan TikTok beğenisi alabilir miyim?", "Hayır. Beğeni, izlenme ve yorumlar yalnızca aylık paketlerimizin içinde, aynı gerçek insanlardan gelir. Onları doğal tutan da budur."),
            ("Beğeniler hangi videolara gelir?", "Gerçek insanlar keyif aldığını beğenir; genellikle en yeni videolarınızı. {rising_name} ve {pro_name} ile ilginin hangi videolara yöneleceğini siz seçebilirsiniz."),
            ("Beğeniler ne kadar hızlı gelir?", "Ay boyunca her gün biraz. Asla anında değil: anında gelen beğeni bottur."),
            ("TikTok şifremi istiyor musunuz?", "Asla. Yalnızca kullanıcı adınız yeterli; hesabınızın herkese açık olması gerekir."),
        ],
    },
]
