"""Turkish UI of the money pages (mirrors en/ui.py key by key).

The word placeholders carry their case ending, so the sentences stay grammatical on every
platform: {profile} profilinizi/kanalınızı, {content} gönderilerinizi/videolarınızı,
{handle} kullanıcı adınızı, {follow} takip etmeyi/abone olmayı. {audience} takipçi/abone
takes -ler and -niz on both words (takipçiler, aboneler; takipçiniz, aboneniz).
"""

UI = {
    # Words that change with the platform or the service
    "audience": {"instagram": "takipçi", "tiktok": "takipçi", "youtube": "abone"},
    "follow": {"instagram": "takip etmeyi", "tiktok": "takip etmeyi", "youtube": "abone olmayı"},
    "profile": {"instagram": "profilinizi", "tiktok": "profilinizi", "youtube": "kanalınızı"},
    "handle": {"instagram": "kullanıcı adınızı", "tiktok": "kullanıcı adınızı", "youtube": "kanal kullanıcı adınızı"},
    "content": {"instagram": "gönderilerinizi", "tiktok": "videolarınızı", "youtube": "videolarınızı"},
    "service_names": {"followers": "Takipçi", "subscribers": "Abone", "likes": "Beğeni",
                      "views": "İzlenme", "comments": "Yorum"},
    "service_words": {"followers": "takipçi", "subscribers": "abone", "likes": "beğeni",
                      "views": "izlenme", "comments": "yorum"},

    # Page chrome
    "home": "Ana sayfa",
    "crumbs_label": "Sayfa yolu",
    "eyebrow": "{platform} · {service_name}",
    "eyebrow_hub": "{platform} büyümesi",
    "cta": "{pick_name} ile başlayın",
    "cta_more": "Tüm paketleri görün",
    "trust": ["Gerçek insanlar, asla bot değil", "Şifrenizi asla istemiyoruz", "Aylık, istediğiniz zaman iptal"],
    "product_name": "{platform} büyüme paketleri",
    "sticky_cta": "Başlayın",

    # Packages
    "packages_title": "Paketinizi seçin",
    "packages_lead": "Üç paket, hepsi aylık. Yeni {audience}ler, beğeniler, izlenmeler ve yorumlar aynı gerçek insanlardan, birlikte gelir.",
    "packages_note": "Sabit bir sayı değil, tipik aylık aralıklar: her yeni {audience}niz, {follow} kendisi seçen gerçek bir insan. Bu yüzden her ay biraz farklı geçer.",

    # What's included: the page's own service comes first, then the rest in this order.
    "included_title": "Pakete neler dahil",
    "included_lead": "Her paket büyümenin tamamını getirir, hepsi aynı gerçek insanlardan.",
    "included_items": {
        "audience": ("Yeni {audience}ler", "{profile} keşfedip {follow} seçen gerçek insanlar. {starter_name} ile genellikle ayda {starter_audience}."),
        "likes": ("Aynı insanlardan beğeniler", "Aynı insanlar {content} beğendikçe gelir: {starter_name} ile genellikle ayda {starter_likes}."),
        "comments": ("Kendi cümleleriyle yorumlar", "{starter_name} ile genellikle ayda {starter_comments}. Hazır metin değil, insanların kendi yazdığı yorumlar."),
        "views": ("Beraberinde gelen izlenmeler", "Aynı insanlar {content} kendi istekleriyle izler. İzlenmeyi önceden saymıyoruz: her biri bir insan."),
        "days": ("30 güne yayılır", "Her gün biraz, seçtiğiniz konumdan. Asla hepsi birden değil."),
        "dashboard": ("Paneliniz", "Gün gün ölçtüklerimiz: kampanyanızdan gelen ziyaretler ve getirdiği yeni {audience}ler."),
    },

    # How it works: the subscription, step by step
    "steps_title": "Nasıl çalışır?",
    "steps_lead": "Aylık bir abonelik: paketi siz seçersiniz, kampanyayı biz yürütürüz, kararı gerçek insanlar verir.",
    "steps": [
        ("Paketinizi seçin", "{starter_name}, {rising_name} ya da {pro_name}; aylık faturalandırılır. Hesabınızdan istediğiniz zaman iptal edebilirsiniz."),
        ("Kampanyanızı başlatıyoruz", "{platform} {handle} ve kitlenizin nereden gelmesini istediğinizi bize iletin. Şifrenizi asla istemiyoruz."),
        ("Gerçek insanlar {profile} keşfeder", "Her gün {profile} gerçek insanlara gösteriyoruz. Gördüğünü beğenenler kendi istekleriyle {audience}niz olur, beğenir ve yorum yapar."),
        ("Paneliniz ölçtüklerimizi gösterir", "Kampanyanızdan gelen ziyaretler ve getirdiği yeni {audience}ler, gün gün. Tahmin değil, ölçülmüş rakamlar."),
    ],

    # Real people vs bots / instant
    "compare_title": "Bot değil, gerçek insanlar",
    "compare_lead": "Anında demek bot demek: hiçbir gerçek insan, bir ödemeden saniyeler sonra {follow} seçmez.",
    "compare_cols": ("Ne değişir?", "Anında ve bot hizmetleri", "Growsterr"),
    "compare": [
        ("Kimler", "Botlar ve sahte profiller", "{follow} kendisi seçen gerçek insanlar"),
        ("Hız", "Dakikalar içinde binlerce", "Ay boyunca her gün biraz"),
        ("Beğeni ve yorum", "Ayrıca satılır, yine botlardan", "Aynı insanlardan, paketinizin içinde"),
        ("Erişiminiz", "Sessizce düşer: hiç etkileşime girmeyen bir kitle, {platform} algoritmasına {content} göstermeye değmediğini söyler", "İzleyen, beğenen ve geri gelen insanlarla büyür"),
        ("Şifreniz", "Çoğu zaman istenir", "Asla istenmez"),
        ("Gördüğünüz", "Bir sonraki temizlikte silinebilecek bir sayı", "Ölçtüklerimizi gösteren bir panel"),
    ],

    # Quantity pages: how a monthly package gets you to the goal
    "quantity_title": "{quantity} {service} hedefine nasıl ulaşırsınız?",
    "quantity_lead": "Sabit bir {quantity} {service} paketi satmıyoruz. Gerçek insanlar kendi kararını verir; aylık bir paket sizi oraya doğal bir hızla götürür.",
    "pace_title": "{pick_name} ile tipik hız",
    "pace_month": "{n}. ay",
    "pace_goal": "Hedef: {quantity}",
    "pace_note": "Gerçek insanların davranışından çıkan tipik aralıklar, asla söz değil. Bazı aylar daha fazla, bazıları daha az getirir.",
    "by_plan_title": "Pakete göre {quantity} için gereken süre",
    "a_month": "ayda {range}",
    "when_first": "genellikle ilk ay içinde",
    "when_about": "genellikle yaklaşık {n} ay",
    "when_range": "genellikle {low}–{high} ay",
    "views_pace": "İzlenmeler {profile} keşfeden aynı gerçek insanlardan gelir, bu yüzden onları önceden saymıyoruz. Bu hedefe en uygun paket {pick_name}.",

    # FAQ, related pages, closing
    "faq_title": "Sıkça sorulan sorular",
    "related_title": "Keşfetmeye devam edin",
    "related": {
        "platform": "{platform} için daha fazlası",
        "platforms": "Diğer platformlarda",
        "quantities": "Diğer hedefler",
        "modifiers": "Büyümenin diğer yolları",
        "articles": "Sıradaki yazı",
        "hubs": "Gerçek insanlarla büyüyün:",
    },
    # The tools a page can carry ("tool"): they run in the browser, nothing is sent.
    "tools": {
        "calculate": "Hesapla",
        "followers": "Takipçi sayısı",
        "avg_likes": "Gönderi başına ortalama beğeni",
        "avg_comments": "Gönderi başına ortalama yorum",
        "engagement_title": "Etkileşim oranınız",
        "engagement_lead": "Takipçilerinizin ne kadarı sıradan bir gönderinize tepki veriyor? Son birkaç gönderinizin rakamlarını girin.",
        "engagement_result": "Etkileşim oranınız: %{rate}.",
        "engagement_note": "Sizi takip eden insanlar gönderilerinizi gerçekten önemsediğinde oran yükselir. Hiç tepki vermeyen takipçiler, sayıları ne olursa olsun oranı düşürür.",
        "growth_title": "Hedefinize ne kadar sürede ulaşırsınız?",
        "growth_lead": "Şu an nerede olduğunuzu ve nereye ulaşmak istediğinizi girin. Hesabı her paketin tipik aylık aralığına göre yapıyoruz.",
        "current": "Bugünkü takipçi sayınız",
        "goal": "Hedefiniz",
        "when_first": "genellikle ilk ay içinde",
        "when_range": "genellikle {low}–{high} ay",
        "when_about": "yaklaşık {n} ay",
        "reached": "Hedefinize zaten ulaşmışsınız.",
        "growth_note": "Tipik aralıklar, söz değil: takip edip etmemeye gerçek insanlar kendisi karar verir.",
    },
    # Eyebrow above the headline of pages outside the platform x service grid (by "kind").
    "article_eyebrows": {
        "guide": "Rehber",
        "alternative": "Karşılaştırma",
        "payment": "Ödeme",
        "agency": "Büyüme ajansı",
        "tool": "Araç",
        "intent": "Açık cevap",
    },
    "cta_title": "{platform} büyümenizi başlatmaya hazır mısınız?",
    "cta_text": "Paketinizi seçin, kampanyanızı başlatalım. Gerisine gerçek insanlar karar verir; paneliniz de ölçtüklerimizi gösterir.",

    # Platform hubs
    "services_title": "{platform} üzerinde büyüttüklerimiz",
    "services_lead": "Tek paket hepsini getirir, aynı gerçek insanlardan.",
    "teasers": {
        "audience": "{profile} keşfedip {follow} seçen gerçek insanlar.",
        "likes": "{content} beğenen insanlardan gelen beğeniler.",
        "views": "Script'ten değil, izlemeyi kendisi seçen insanlardan gelen izlenmeler.",
        "comments": "Gerçek insanların kendi cümleleriyle yazdığı yorumlar.",
    },
    "explore": "Keşfedin",
    "in_package": "Her pakete dahil",
    "goals_title": "{platform} için daha fazla büyüme yolu",
    "other_hubs_title": "Diğer platformlarda da büyütüyoruz",
}
