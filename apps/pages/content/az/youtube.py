"""Azerbaijani YouTube pages: the hub and subscribers (mirrors en/youtube.py)."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "youtube",
        "label": "YouTube",
        "title": "Kontent Yaradıcıları üçün YouTube Böyümə Paketləri | Growsterr",
        "description": "YouTube kanalınızı real insanlarla böyüdün: aylıq paketlər abunə olmağı seçən tamaşaçılardan abunəçi, bəyənmə və şərh gətirir. Başlanğıc qiymət ayda {from_price}.",
        "h1": ("YouTube kanalınızı ", "real tamaşaçılarla böyüdün."),
        "intro": "Kontent yaradıcıları üçün aylıq böyümə paketləri. Real insanlar kanalınızı kəşf edir, videolarınıza baxır və gördüyünü bəyənəndə abunə olur. Paneliniz ölçdüklərimizi gün-gün göstərir.",
        "hero": {"image": "youtube-hub", "alt": "Real tamaşaçılardan abunəçi, bəyənmə və şərh qazanan YouTube kanalı"},
        "sections": [
            {
                "h2": "Dəyərli olan baxan abunəçilərdir",
                "p": [
                    "YouTube insanların baxdığı, bəyəndiyi və geri qayıtdığı videoları tövsiyə edir. Heç vaxt baxmayan abunəçi heç olmamasından da pisdir: auditoriyanızın aktiv hissəsinin payını aşağı salır.",
                    "Gətirdiyimiz hər abunəçi kanalınızı tapıb abunə olmağı seçən insandır. Bəyənmə, baxış və şərhlər də paketinizin içində, eyni insanlardan gəlir.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Kontent yaradıcısının YouTube videosuna baxıb şərh yazan tamaşaçılar"},
            },
            {
                "h2": "Diqqətlə video yayımlayan kanallar üçün",
                "p": [
                    "Dərslər, vloq, musiqi və ya oyun: mütəmadi yayımlayırsınızsa, real tamaşaçılar hər yeni videonuza daha yaxşı start verir. {starter_name} ilə başlayın, kanalınız daha çoxuna hazır olanda bir üst paketə keçin.",
                ],
                "ul": [
                    "Auditoriyanızın hansı şəhər, region və ya ölkədən gəlməsini siz deyirsiniz.",
                    "Abunəçilər, bəyənmələr və şərhlər eyni insanlardan, birlikdə gəlir.",
                    "Kanalınız sizin qalır: şifrənizi heç vaxt istəmirik.",
                ],
                "image": {"image": "youtube-channel", "alt": "Ev studiyasında YouTube videosunu montaj edən yaradıcı"},
            },
        ],
        "faqs": [
            ("Abunəçilər real insanlardır?", "Bəli. Hər abunəçi kanalınızı tapıb abunə olmağı seçən real insandır. Bot yox, saxta hesab yox, ani heç nə yox."),
            ("Bir paket neçə abunəçi gətirir?", "{starter_name} ilə adətən ayda {starter_audience}, {rising_name} ilə {rising_audience}, {pro_name} ilə {pro_audience} yeni abunəçi. Bunlar sabit say deyil, adi aralıqlardır."),
            ("Google və ya YouTube şifrəmi istəyirsiniz?", "Heç vaxt. Bizə yalnız kanal adınız (@handle) lazımdır, kanalınız isə açıq olmalıdır."),
            ("Baxış və ya bəyənməni ayrıca ala bilərəm?", "Xeyr. Baxış, bəyənmə və şərhlər hər paketin içində, kanalınıza abunə olan eyni real insanlardan gəlir."),
            ("İstənilən vaxt ləğv edə bilərəm?", "Bəli. Paketlər hər ay yenilənir və hesabınızdan ləğv edə bilərsiniz. Ödədiyiniz ay sonuna qədər davam edir."),
        ],
    },
    {
        "service": "subscribers",
        "slug": "youtube/abuneci",
        "label": "YouTube abunəçi",
        "title": "Həqiqətən Baxan Real YouTube Abunəçiləri | Growsterr",
        "description": "Real insanlardan YouTube abunəçiləri: kanalınızı tapıb abunə olmağı seçən tamaşaçılar, bəyənmə və şərhlərlə birlikdə. Başlanğıc qiymət ayda {from_price}.",
        "h1": ("YouTube-da ", "həqiqətən baxan abunəçilər."),
        "intro": "Real insanlar kanalınızı kəşf edir, videolarınıza baxır və gördüyünü bəyənəndə abunə olur. {starter_name} ilə adətən ayda {starter_audience} yeni abunəçi, eyni tamaşaçılardan bəyənmə və şərhlərlə birlikdə.",
        "hero": {"image": "youtube-subscribers", "alt": "Real tamaşaçılardan yeni abunəçilər qazanan YouTube kanal səhifəsi"},
        "sections": [
            {
                "h2": "Abunəçi həm də tamaşaçı olmalıdır",
                "p": [
                    "YouTube-da abunəçi yalnız baxanda faydalıdır. Real abunəçilər növbəti videonuzu görür, baxır, bəyənir və bəzən şərh yazır; YouTube da nəyi tövsiyə edəcəyinə qərar verəndə buna baxır.",
                    "Bot abunəçilər heç vaxt baxmır. Kanalı daha böyük göstərirlər, amma videoları daha az insana çatır.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Videoya baxdıqdan sonra YouTube kanalına abunə olan real tamaşaçılar"},
            },
            {
                "h2": "Bir ay necə keçir?",
                "ul": [
                    "İlk günlər: kampaniyanız başlayır və ilk tamaşaçılar gəlir.",
                    "Hər həftə: yeni abunəçilər, bəyənmələr və şərhlər, hər gün bir neçəsi.",
                    "Ayın sonunda: {pick_name} ilə adətən {pick_audience} yeni abunəçi.",
                ],
            },
            {
                "h2": "Tamaşaçılarınız haradan gəlir?",
                "p": [
                    "Auditoriyanızın hansı şəhər, region və ya ölkədən gəlməsini bizə deyin. Kanalınızı əvvəlcə oradakı real insanlara göstəririk; ən uyğun auditoriya yaxınlıqda daha böyükdürsə, tamaşaçıların bir hissəsi oradan da gələ bilər.",
                ],
            },
        ],
        "faqs": [
            ("Abunəçilər nə qədər sürətlə gəlir?", "Bütün aya yayılaraq, hər gün bir az. Heç vaxt hamısı birdən yox: real insanlar öz tempində abunə olur."),
            ("Videolarıma baxacaqlar?", "Onlar kanalınızı gördükdən sonra abunə olmağı seçən real insanlardır. Sonra nəyə baxacaqları, hər auditoriyada olduğu kimi, onların öz seçimidir; dəyərli olmasının səbəbi də məhz budur."),
            ("Bəyənmə və şərh də gəlir?", "Bəli, eyni tamaşaçılardan: {pick_name} ilə adətən ayda {pick_likes} bəyənmə və {pick_comments} şərh."),
            ("Şifrəmi istəyirsiniz?", "Heç vaxt. Bizə yalnız kanal adınız lazımdır, kanalınız isə açıq olmalıdır."),
        ],
    },
]
