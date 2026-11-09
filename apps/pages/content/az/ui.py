"""Azerbaijani UI of the money pages (mirrors en/ui.py key by key).

The word placeholders carry their case ending, so the sentences stay grammatical on every
platform: {profile} profilinizi/kanalınızı, {content} paylaşımlarınızı/videolarınızı,
{handle} istifadəçi adınızı/kanal adınızı, {follow} izləməyi/abunə olmağı. {audience}
izləyici/abunəçi takes -lər and -niz on both words (izləyicilər, abunəçiniz).
"""

UI = {
    # Words that change with the platform or the service
    "audience": {"instagram": "izləyici", "tiktok": "izləyici", "youtube": "abunəçi"},
    "follow": {"instagram": "izləməyi", "tiktok": "izləməyi", "youtube": "abunə olmağı"},
    "profile": {"instagram": "profilinizi", "tiktok": "profilinizi", "youtube": "kanalınızı"},
    "handle": {"instagram": "istifadəçi adınızı", "tiktok": "istifadəçi adınızı", "youtube": "kanal adınızı"},
    "content": {"instagram": "paylaşımlarınızı", "tiktok": "videolarınızı", "youtube": "videolarınızı"},
    "service_names": {"followers": "İzləyici", "subscribers": "Abunəçi", "likes": "Bəyənmə",
                      "views": "Baxış", "comments": "Şərh"},
    "service_words": {"followers": "izləyici", "subscribers": "abunəçi", "likes": "bəyənmə",
                      "views": "baxış", "comments": "şərh"},

    # Page chrome
    "home": "Ana səhifə",
    "crumbs_label": "Səhifə yolu",
    "eyebrow": "{platform} · {service_name}",
    "eyebrow_hub": "{platform} böyüməsi",
    "cta": "{pick_name} ilə başlayın",
    "cta_more": "Bütün paketlərə baxın",
    "trust": ["Real insanlar, heç vaxt bot yox", "Şifrənizi heç vaxt istəmirik", "Aylıq, istənilən vaxt ləğv edin"],
    "product_name": "{platform} böyümə paketləri",
    "sticky_cta": "Başlayın",

    # Packages
    "packages_title": "Paketinizi seçin",
    "packages_lead": "Üç paket, hamısı aylıq. Yeni {audience}lər, bəyənmələr, baxışlar və şərhlər eyni real insanlardan, birlikdə gəlir.",
    "packages_note": "Sabit say deyil, adi aylıq aralıqlar: hər yeni {audience}niz {follow} özü seçən real insandır, ona görə hər ay bir az fərqli olur.",

    # What's included: the page's own service comes first, then the rest in this order.
    "included_title": "Paketə nələr daxildir",
    "included_lead": "Hər paket böyümənin bütün tərəflərini gətirir, hamısı eyni real insanlardan.",
    "included_items": {
        "audience": ("Yeni {audience}lər", "{profile} kəşf edib {follow} seçən real insanlar. {starter_name} ilə adətən ayda {starter_audience}."),
        "likes": ("Eyni insanlardan bəyənmələr", "Eyni insanlar {content} bəyəndikcə gəlir: {starter_name} ilə adətən ayda {starter_likes}."),
        "comments": ("Öz sözləri ilə şərhlər", "{starter_name} ilə adətən ayda {starter_comments}. Hazır mətn yox, insanların özünün yazdığı şərhlər."),
        "views": ("Birlikdə gələn baxışlar", "Eyni insanlar {content} öz istəkləri ilə açıb baxır. Baxışları əvvəlcədən saymırıq: hər biri bir insandır."),
        "days": ("30 günə yayılır", "Hər gün bir az, seçdiyiniz məkandan. Heç vaxt hamısı birdən yox."),
        "dashboard": ("Paneliniz", "Gün-gün ölçdüklərimiz: kampaniyanızdan gələn ziyarətlər və onların gətirdiyi yeni {audience}lər."),
    },

    # How it works: the subscription, step by step
    "steps_title": "Necə işləyir?",
    "steps_lead": "Aylıq abunəlik: paketi siz seçirsiniz, kampaniyanı biz aparırıq, qərarı real insanlar verir.",
    "steps": [
        ("Paket seçin", "{starter_name}, {rising_name} və ya {pro_name}, aylıq ödənişlə. Hesabınızdan istənilən vaxt ləğv edə bilərsiniz."),
        ("Kampaniyanızı başladırıq", "{platform} {handle} və auditoriyanızın haradan gəlməsini istədiyinizi bizə bildirin. Şifrənizi heç vaxt istəmirik."),
        ("Real insanlar {profile} kəşf edir", "Hər gün {profile} real insanlara göstəririk. Gördüyünü bəyənənlər öz istəkləri ilə {audience}niz olur, bəyənir və şərh yazır."),
        ("Paneliniz ölçdüklərimizi göstərir", "Kampaniyanızdan gələn ziyarətlər və onların gətirdiyi yeni {audience}lər, gün-gün. Təxmin yox, ölçülmüş rəqəmlər."),
    ],

    # Real people vs bots / instant
    "compare_title": "Bot yox, real insanlar",
    "compare_lead": "Ani bot deməkdir: heç bir real insan ödənişdən saniyələr sonra {follow} seçmir.",
    "compare_cols": ("Nə dəyişir", "Ani və bot xidmətləri", "Growsterr"),
    "compare": [
        ("Kimlərdir", "Botlar və saxta profillər", "{follow} özü seçən real insanlar"),
        ("Sürət", "Dəqiqələr ərzində minlərlə", "Bütün ay boyu hər gün bir az"),
        ("Bəyənmə və şərhlər", "Ayrıca satılır, yenə botlardan", "Eyni insanlardan, paketinizin içində"),
        ("Əhatəniz", "Səssizcə düşür: heç aktivlik göstərməyən auditoriya {platform} alqoritminə {content} göstərməyə dəymədiyini deyir", "Baxan, bəyənən və geri qayıdan insanlarla böyüyür"),
        ("Şifrəniz", "Çox vaxt istənilir", "Heç vaxt"),
        ("Gördüyünüz", "Növbəti təmizləmədə yox ola bilən bir rəqəm", "Ölçdüklərimizi göstərən panel"),
    ],

    # Quantity pages: how a monthly package gets you to the goal
    "quantity_title": "{quantity} {service} hədəfinə necə çatırsınız",
    "quantity_lead": "Sabit {quantity} {service} paketi satmırıq. Real insanlar qərarı özləri verir, ona görə aylıq paket sizi ora təbii sürətlə aparır.",
    "pace_title": "{pick_name} ilə adi temp",
    "pace_month": "Ay {n}",
    "pace_goal": "Hədəf: {quantity}",
    "pace_note": "Real insanların davranışından çıxan adi aralıqlar, heç vaxt vəd deyil. Bəzi aylar daha çox, bəziləri daha az gətirir.",
    "by_plan_title": "Paketə görə {quantity} hədəfinə qədər vaxt",
    "a_month": "ayda {range}",
    "when_first": "adətən ilk ay ərzində",
    "when_about": "adətən təxminən {n} ay",
    "when_range": "adətən {low}–{high} ay",
    "views_pace": "Baxışlar {profile} kəşf edən eyni real insanlardan gəlir, ona görə onları əvvəlcədən saymırıq. Bu hədəfə ən uyğun paket: {pick_name}.",

    # FAQ, related pages, closing
    "faq_title": "Suallar və cavablar",
    "related_title": "Kəşf etməyə davam edin",
    "related": {
        "platform": "{platform} üzrə daha çox",
        "platforms": "Digər platformalarda",
        "quantities": "Digər hədəflər",
        "modifiers": "Böyümənin digər yolları",
        "articles": "Növbəti oxu",
        "hubs": "Real insanlarla böyüyün:",
    },
    # The tools a page can carry ("tool"): they run in the browser, nothing is sent.
    "tools": {
        "calculate": "Hesabla",
        "followers": "İzləyicilər",
        "avg_likes": "Paylaşım başına orta bəyənmə",
        "avg_comments": "Paylaşım başına orta şərh",
        "engagement_title": "Aktivlik dərəcəniz",
        "engagement_lead": "İzləyicilərinizin nə qədəri adi bir paylaşımınıza reaksiya verir? Son bir neçə paylaşımınızın rəqəmlərini daxil edin.",
        "engagement_result": "Aktivlik dərəcəniz: {rate}%.",
        "engagement_note": "Sizi izləyən insanlar paylaşımlarınıza həqiqətən maraq göstərəndə dərəcə yüksəlir. Heç reaksiya verməyən izləyicilər, sayından asılı olmayaraq, onu aşağı salır.",
        "growth_title": "Hədəfinizə nə qədər qalıb?",
        "growth_lead": "İndi harada olduğunuzu və harada olmaq istədiyinizi daxil edin. Hesablamanı hər paketin adi aylıq aralığına görə edirik.",
        "current": "Bugünkü izləyici sayı",
        "goal": "Hədəfiniz",
        "when_first": "adətən ilk ay ərzində",
        "when_range": "adətən {low}–{high} ay",
        "when_about": "təxminən {n} ay",
        "reached": "Artıq hədəfinizə çatmısınız.",
        "growth_note": "Adi aralıqlar, vəd deyil: izləyib-izləməmək qərarını real insanlar özləri verir.",
    },
    # Eyebrow above the headline of pages outside the platform x service grid (by "kind").
    "article_eyebrows": {
        "guide": "Bələdçi",
        "alternative": "Müqayisə",
        "payment": "Ödəniş",
        "agency": "Böyümə agentliyi",
        "tool": "Alət",
        "intent": "Açıq cavab",
    },
    "cta_title": "{platform} böyüməsinə hazırsınız?",
    "cta_text": "Paketi seçin, kampaniyanızı başladaq. Qalanına real insanlar qərar verir, paneliniz isə ölçdüklərimizi göstərir.",

    # Platform hubs
    "services_title": "{platform} üzrə nələri böyüdürük",
    "services_lead": "Bir paket hamısını gətirir, eyni real insanlardan.",
    "teasers": {
        "audience": "{profile} kəşf edib {follow} seçən real insanlar.",
        "likes": "{content} bəyənən insanlardan gələn bəyənmələr.",
        "views": "Skriptdən yox, baxmağı özü seçən insanlardan gələn baxışlar.",
        "comments": "Real insanların öz sözləri ilə yazdığı şərhlər.",
    },
    "explore": "Kəşf edin",
    "in_package": "Hər paketə daxildir",
    "goals_title": "{platform} üzrə böyümənin daha çox yolu",
    "other_hubs_title": "Digər platformalarda da böyüdürük",
}
