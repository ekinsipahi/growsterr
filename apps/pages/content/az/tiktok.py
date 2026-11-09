"""Azerbaijani TikTok pages: the hub and likes (mirrors en/tiktok.py)."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "tiktok",
        "label": "TikTok",
        "title": "Kontent Yaradıcıları üçün TikTok Böyümə Paketləri | Growsterr",
        "description": "TikTok-da real insanlarla böyüyün: aylıq paketlər sizi izləməyi özü seçən insanlardan yeni izləyici, bəyənmə və şərh gətirir. Başlanğıc qiymət ayda {from_price}.",
        "h1": ("TikTok hesabınızı ", "real insanlarla böyüdün."),
        "intro": "Kontent yaradıcıları və influenserlər üçün aylıq böyümə paketləri. Real insanlar profilinizi kəşf edir, videolarınıza baxır və gördüyünü bəyənəndə sizi izləyir. Paneliniz ölçdüklərimizi gün-gün göstərir.",
        "hero": {"image": "tiktok-hub", "alt": "Yeni izləyicilər və bəyənmələr qazanan TikTok yaradıcısının profili"},
        "sections": [
            {
                "h2": "TikTok-da hər şey diqqətdən başlayır",
                "p": [
                    "TikTok videonu ilk tamaşaçılar ona baxanda, bəyənəndə, şərh yazanda və izləyəndə daha çox insana göstərir. Arxasında insan olmayan rəqəmlər bunların heç birini hərəkətə gətirmir.",
                    "Paketlərimiz hər gün profilinizə real insanlar gətirir. Onlar baxır, qərar verir; videolarınızı bəyənənlər izləyir və bəyənir. Videonun yayılmasına kömək edən diqqət məhz budur.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Kontent yaradıcısının TikTok videolarına baxan real tamaşaçılar"},
            },
            {
                "h2": "Deməyə sözü olan yaradıcılar üçün",
                "p": [
                    "Komediya, yemək, moda və ya dərslər: mütəmadi paylaşırsınızsa, real tamaşaçılar hər yeni videonuza daha yaxşı start verir. {starter_name} ilə başlayın, hazır olanda bir üst paketə keçin.",
                ],
                "ul": [
                    "Auditoriyanızın hansı şəhər, region və ya ölkədən gəlməsini siz deyirsiniz.",
                    "İzləyicilər, bəyənmələr və şərhlər eyni insanlardan, birlikdə gəlir.",
                    "Hesabınız sizin qalır: şifrənizi heç vaxt istəmirik.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Ştativdəki telefonla TikTok videosu çəkən yaradıcı"},
            },
        ],
        "faqs": [
            ("İzləyicilər real insanlardır?", "Bəli. Hər izləyici profilinizi görüb sizi izləməyi seçən real insandır. Heç vaxt bot, saxta hesab və ya ani çatdırılmadan istifadə etmirik."),
            ("Bir paket neçə izləyici gətirir?", "{starter_name} ilə adətən ayda {starter_audience}, {rising_name} ilə {rising_audience}, {pro_name} ilə {pro_audience} yeni izləyici. Bunlar sabit say deyil, adi aralıqlardır: real insanlar qərarı özləri verir."),
            ("TikTok şifrəmi istəyirsiniz?", "Heç vaxt. Bizə yalnız istifadəçi adınız lazımdır. Hesabınızı açıq saxlayın ki, onu kəşf edən insanlar sizi izləyə bilsin."),
            ("Baxış və ya bəyənməni ayrıca ala bilərəm?", "Xeyr. Baxış, bəyənmə və şərhlər hər paketin içində, sizi izləyən eyni real insanlardan gəlir."),
            ("İstənilən vaxt ləğv edə bilərəm?", "Bəli. Paketlər hər ay yenilənir və hesabınızdan ləğv edə bilərsiniz. Ödədiyiniz ay sonuna qədər davam edir."),
        ],
    },
    {
        "service": "likes",
        "slug": "tiktok/beyenme",
        "label": "TikTok bəyənmə",
        "title": "Real İnsanlardan TikTok Bəyənmələri, Hər Paketin İçində",
        "description": "Videolarınıza baxan real insanlardan TikTok bəyənmələri, heç vaxt bot yox. Bəyənmələr hər aylıq paketə izləyici və şərhlərlə birlikdə daxildir.",
        "h1": ("Real insanlardan TikTok bəyənmələri. ", "Hər paketin içində."),
        "intro": "Bəyənməni ayrıca satmırıq. Hər paket profilinizi kəşf edən, videolarınıza baxan və xoşuna gələni bəyənən real insanlar gətirir: {starter_name} ilə adətən ayda {starter_likes} bəyənmə.",
        "hero": {"image": "tiktok-likes", "alt": "TikTok videosuna real tamaşaçılardan gələn bəyənmələr"},
        "sections": [
            {
                "h2": "Bəyənmə yalnız arxasında insan olanda dəyərlidir",
                "p": [
                    "TikTok bəyənmənin ətrafında baş verənlərə baxır: tamaşaçı videoya baxmağa davam etdimi, izlədimi, geri qayıtdımı? Botlardan gələn bəyənmələr bunların hamısına yox cavabı verir: rəqəm əlavə edir, əhatənizdən isə alır.",
                    "Real insanlardan gələn bəyənmələr qalanını da gətirir: baxış müddəti, izləmə və şərh. Videonun yayılmasına kömək edən siqnal budur.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "TikTok videosuna sona qədər baxıb onu bəyənən tamaşaçılar"},
            },
            {
                "h2": "Hər paket neçə bəyənmə gətirir?",
                "ul": [
                    "{starter_name} (ayda {starter_price}): adətən {starter_likes} bəyənmə.",
                    "{rising_name} (ayda {rising_price}): adətən {rising_likes} bəyənmə, seçdiyiniz videolarda.",
                    "{pro_name} (ayda {pro_price}): adətən {pro_likes} bəyənmə, prioritet yerləşdirmə ilə.",
                ],
            },
            {
                "h2": "Bəyənməni niyə ayrıca satmırıq?",
                "p": [
                    "Baxış, izləmə və ya şərh olmadan gələn bəyənmələr olduğu kimi görünür. Paketin içində hər bəyənmə videoya baxmış birindən gəlir, beləliklə rəqəmləriniz real böyümədə olduğu kimi birlikdə hərəkət edir.",
                ],
            },
        ],
        "faqs": [
            ("Paketsiz TikTok bəyənməsi ala bilərəm?", "Xeyr. Bəyənmə, baxış və şərhlər yalnız aylıq paketlərimizin içində, eyni real insanlardan gəlir. Onları təbii saxlayan da budur."),
            ("Bəyənmələr hansı videolara gəlir?", "Real insanlar xoşuna gələni bəyənir, adətən ən yeni videolarınızı. {rising_name} və {pro_name} ilə diqqətin hansı videolara yönələcəyini siz seçə bilərsiniz."),
            ("Bəyənmələr nə qədər sürətlə gəlir?", "Ay boyu hər gün bir az. Heç vaxt dərhal yox: dərhal gələn bəyənmə botdur."),
            ("TikTok şifrəmi istəyirsiniz?", "Heç vaxt. Bizə yalnız istifadəçi adınız lazımdır, hesabınız isə açıq olmalıdır."),
        ],
    },
]
