UPDATED = "2026-11-09"

# Turkish YouTube intent pages: searches for things we don't sell (cheap, instant, free, free
# trial, panels). Each answers honestly, then leads to the monthly package. Mirrors
# en/youtube_intents.py; keys and placeholders: docs/CONTENT.md.

PAGES = [
    # --- Subscribers ----------------------------------------------------------------------
    {
        "service": "subscribers",
        "modifier": "cheap",
        "slug": "youtube/abone/ucuz",
        "label": "Ucuz YouTube abone?",
        "plan": "starter",
        "title": "Ucuz YouTube Abone mi? Size Gerçek Maliyeti Bu | Growsterr",
        "description": "Birkaç liralık YouTube aboneleri hiç izlemez ve temizlenip gider. {starter_name} ayda {starter_price} ile genellikle {starter_audience} gerçek izleyici getirir.",
        "h1": ("Birkaç liralık YouTube aboneleri ", "tek bir video bile izlemez."),
        "intro": "YouTube aboneyi birkaç liraya satın almayı mı düşünüyorsunuz? O fiyata asla izlemeyecek, beğenmeyecek ya da yorum yapmayacak hesaplar alırsınız; YouTube da spam hesapları abone sayılarından düzenli olarak siler. Biz daha fazla ücret alırız ve izleyici getiririz: {starter_name} ile ayda {starter_price} karşılığında tipik bir ayda {starter_audience} yeni abone; her biri kanalınızı bulup abone olmaya karar veren bir insan.",
        "hero": {"image": "youtube-subscribers", "alt": "Gerçek izleyicilerle büyüyen bir YouTube kanalının abone sayısı"},
        "sections": [
            {
                "h2": "Hiç izlemeyen bir abonenin maliyeti",
                "p": [
                    "YouTube'da abonelerin ne yaptığı, kaç tane olduklarından daha önemlidir. Oynat tuşuna hiç basmayan hesaplarla dolu bir liste, her yeni videoyu olduğundan daha az ilginç gösterir.",
                    "Yani ucuz bir abone ucuz değildir. Bir kez parayla, bir kez de alamadığınız izlenmelerle ödersiniz.",
                ],
            },
            {
                "h2": "Gerçek bir abonenin maliyeti",
                "p": [
                    "{starter_name} paketine bakın: ayda {starter_price} ve genellikle seçtiğiniz yerden gelen, gerçek izleyici olan {starter_audience} abone. Kişi başına birkaç sent eder; beğenileri ve yorumları da fiyatın içindedir.",
                ],
            },
            {
                "h2": "Risk olmadan düşük fiyat",
                "ul": [
                    "Şifre yok, Google hesabınıza erişim yok: yalnızca kanal kullanıcı adınız.",
                    "Stripe üzerinden kartla aylık ödeme, hesabınızdan iptal edilebilir.",
                    "Abone, beğeni ve yorum tek fiyatta, aynı insanlardan.",
                ],
            },
        ],
        "faqs": [
            ("Gerçek YouTube aboneleri ne kadar tutar?", "Paketlerimiz ayda {starter_price} ile başlar. {starter_name} genellikle {starter_audience} yeni abone getirir; {rising_price} olan {rising_name} {rising_audience}, {pro_price} olan {pro_name} {pro_audience} getirir."),
            ("Bazı siteler neden aboneyi bu kadar ucuza satıyor?", "Çünkü izleyici değil hesap satıyorlar. Toplu hesap açmak ya da kiralamak çok ucuzdur; kanalınızı izlemek isteyen insanları bulmak değildir."),
            ("Küçük bir kanal için çok ucuz bir seçenek var mı?", "{starter_name} yeni ve küçük kanallar için yapıldı ve en düşük fiyatımız."),
            ("Ucuz aboneler kanalımı sıkıntıya sokabilir mi?", "Sokabilir. YouTube'un sahte etkileşim politikası satın alınan aboneleri kapsar; bunları kullanan kanallar videolarının kaldırılması ya da kanalın yaptırımla karşılaşması riskini alır."),
            ("İzlenmeler fiyata dahil mi?", "Evet. Yeni aboneleriniz kendi istekleriyle izler, beğenir ve yorum yapar; hepsi paketin içinde. İzlenmelere bir sayı koymayız, çünkü her biri oynat tuşuna basmayı seçen biridir."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "fast",
        "slug": "youtube/abone/hizli",
        "label": "Hızlı YouTube abone?",
        "title": "Hızlı YouTube Abone Satın Al: Gerçek, Anında Değil | Growsterr",
        "description": "Gerçek, aktif ve anında YouTube abonesi bir arada olamaz. Bizimkiler gerçek ve aktif: kampanyanız birkaç günde başlar, aboneler her gün gelir.",
        "h1": ("Gerçek, aktif ve anında mı? ", "Bunların ancak ikisi doğru olabilir."),
        "intro": "YouTube aboneyi hızlı, gerçek, anında ve aktif, hepsi bir arada mı satın almak istiyorsunuz? Bunların ancak ikisi birlikte doğru olabilir. Anında gelen aboneler insan değildir; gerçek insanlar da siz ödeme yaptığınız saniye abone olmaz. Biz gerçek ve aktif aboneleri çabuk getiririz: kampanya ilk günler içinde başlar ve oradan itibaren {pick_name} genellikle ayda {pick_audience} abone ekler, her gün birkaç tane.",
        "hero": {"image": "youtube-subscribers", "alt": "Gün be gün bir YouTube kanalına katılan yeni aboneler"},
        "sections": [
            {
                "h2": "YouTube'da anında neden sahte demektir?",
                "p": [
                    "Gerçek bir insan bir şey izledikten sonra abone olur: bir video, bir Shorts, bir kanal fragmanı. Bu en az birkaç dakika sürer ve onlar fırsat bulduğunda olur. Bir ödemenin hemen ardından yüzlercesi beliren aboneler izleme kısmını atlamıştır; bu da size insan olmadıklarını söyler.",
                ],
            },
            {
                "h2": "Gerçek aboneler ne kadar hızlı gelir?",
                "p": [
                    "Kurulum, sipariş verdikten sonraki ilk günleri alır. Ondan sonra yeni izleyiciler her gün kanalınızı bulur, izlediğini beğenenler de abone olur. Panel her günü ölçtüğümüz gibi gösterir; hızı ilk haftadan görürsünüz.",
                ],
            },
            {
                "h2": "İşinize yarayan hız",
                "ul": [
                    "Kampanya sürerken video yükleyin ki yeni abonelerin izleyecek bir sonraki şeyi olsun.",
                    "Kanal sayfanızı toparlayın: net bir kapak, bir fragman ve mantıklı sıralanmış oynatma listeleri.",
                    "En büyük aylık aralık için {pro_name} seçin: genellikle {pro_audience} yeni abone.",
                ],
            },
        ],
        "faqs": [
            ("Abone sayım ne kadar hızlı artar?", "Kampanyanızın ilk günleri içinde: önce birkaç birkaç, sonra ay boyunca her gün."),
            ("Anında 1.000 abone ekleyebilir misiniz?", "Hayır; gerçek insanlarla kimse ekleyemez. Bir saatte bin abone, asla izlemeyecek bin hesap demektir; YouTube'un temizlediği de tam olarak bunlardır."),
            ("Aboneleriniz aktif mi?", "Kanalınızı gördükten sonra abone olan gerçek insanlar; yani her izleyici kadar aktifler: bir video ilgilerini çektiğinde izler, beğenir ve yorum yaparlar."),
            ("Hangi paket en hızlı?", "{pro_name} her ay en çoğunu getirir: genellikle {pro_audience} yeni abone. {starter_name} ve {rising_name} daha küçük aralıklar getirir; onlar da aynı şekilde aya yayılır."),
            ("Hızlı büyüme kanalıma zarar verir mi?", "Bu hızda hayır. Aboneler gerçek izleyicilerden her gün gelir; büyüyen kanallar da aboneyi zaten böyle kazanır."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "free",
        "slug": "youtube/abone/ucretsiz",
        "label": "Ücretsiz YouTube abone?",
        "plan": "starter",
        "tool": "growth-calculator",
        "title": "Ücretsiz YouTube Abone mi? Daha İyi Bir Plan Var | Growsterr",
        "description": "Ücretsiz YouTube aboneleri abone takasından ya da botlardan gelir. Vermiyoruz; ücretsiz büyüme hesaplayıcımız gerçek büyümenin ne kadar sürdüğünü gösterir.",
        "h1": ("Ücretsiz YouTube abone mi? ", "Bunun yerine gerçeklerini planlayın."),
        "intro": "YouTube aboneyi ücretsiz ya da birkaç dolara 1.000 tane mi almak istiyorsunuz? İkisi de izleyen insan getirmez: bedava teklifler abone takasına ya da bot hesaplara dayanır. Biz abone dağıtmıyoruz. Bu sayfanın ücretsiz kısmı büyüme hesaplayıcısı: kanalınızın bugün nerede olduğunu ve nereye gitmek istediğinizi girin, her paketin genellikle kaç ay gerektirdiğini tahmin etsin.",
        "hero": {"image": "youtube-channel", "alt": "Önümüzdeki aylar için bir abone hedefi planlayan bir YouTuber"},
        "sections": [
            {
                "h2": "Abone takası ve diğer bedava numaralar",
                "ul": [
                    "Abone takası grupları: yabancılara abone olursunuz, onlar da size; kimse kimseyi izlemez.",
                    "Google ile giriş yapmanızı isteyip sonra hesabınızı başkalarına abone olmak için kullanan bedava abone siteleri.",
                    "Daha büyüğünü alasınız diye bot hesaplardan verilen küçük ücretsiz partiler.",
                ],
                "p": [
                    "Hepsi sayınızı videolarınızla hiç ilgilenmeyen insanlarla doldurur; bu da daha az aboneye sahip olmaktan kötüdür.",
                ],
            },
            {
                "h2": "Şu 1.000 meselesi",
                "p": [
                    "Bin abone, çoğu zaman YouTube İş Ortağı Programı yüzünden birçok kanal için bir dönüm noktasıdır. Satın alınan ya da takasla gelen aboneler hiç izlenme süresi eklemez ve YouTube onları sahte etkileşim sayar. Biz de para kazanma sözü vermeyiz: gerçek izleyiciler getiririz, gerisi videolarınıza ve YouTube'a bağlıdır.",
                ],
            },
            {
                "h2": "Büyüme hesaplayıcısıyla planlayın",
                "p": [
                    "Üst kısımdaki hesaplayıcı ücretsizdir ve tarayıcınızda çalışır. Bugünkü takipçi sayısını sorduğu yere abone sayınızı, hedef olarak da ulaşmak istediğiniz sayıyı girin. Her paketin tipik aylık aralığından yola çıkarak kaç ay gerektiğini hesaplar.",
                ],
            },
        ],
        "faqs": [
            ("YouTube abonesini ücretsiz alabilir miyim?", "Bizden gerçek olanını hayır. Getirdiğimiz her abone, ücretli bir kampanyanın ulaştığı bir izleyicidir. Buradaki hesaplayıcı ücretsiz kısımdır ve ne sıklıkla kullandığınızın sınırı yoktur."),
            ("Birkaç dolara 1.000 YouTube abonesi gerçek mi?", "Hiçbir gerçek kampanya birkaç dolara kanalınızı isteyen bin insan bulamaz. O fiyatta aboneler izleyici değil, hesaptır."),
            ("1.000 gerçek aboneye ulaşmak ne kadar sürer?", "Başlangıç noktanıza bağlı. {starter_name} genellikle ayda {starter_audience} yeni abone getirir; kanalınız için kaç ay süreceğini görmek için kendi rakamlarınızı yukarıdaki hesaplayıcıya girin."),
            ("Abone takası YouTube kurallarına aykırı mı?", "Evet. YouTube'un sahte etkileşim politikası abonelik takasını kapsar; bu yüzden bir kanalı riske atabilir. Üstelik hiç izlemeyen aboneler getirir."),
            ("Küçük bir kanal nereden başlamalı?", "Ayda {starter_price} olan {starter_name} ile; içinde bulunduğunuz ayın ötesinde sözleşme olmadan."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "free-trial",
        "slug": "youtube/abone/ucretsiz-deneme",
        "label": "YouTube abone ücretsiz deneme?",
        "plan": "starter",
        "title": "Ücretsiz Denemeyle YouTube Abone mi? | Growsterr",
        "description": "Burada ücretsiz YouTube abone denemesi yok: bir günlük numune hiçbir şey kanıtlamaz. İlk ayınız ölçülmüş gerçek izleyicileri sözleşmesiz gösterir.",
        "h1": ("Ücretsiz bir YouTube abone denemesi ", "hiçbir şey kanıtlamaz. Bir ay kanıtlar."),
        "intro": "YouTube aboneyi ücretsiz bir denemeden sonra satın almak istiyorsanız size açık olalım: deneme sunmuyoruz. Bir günde 100 abonelik bir deneme, yalnızca satıcının harcayacak hesabı olduğunu gösterirdi. Bizi ilk ayınızda değerlendirirsiniz: ayda {starter_price} ile {starter_name}, ilk günlerden gelen gerçek izleyiciler, ölçtüklerimizi gösteren bir panel ve ayın ötesinde sözleşme yok.",
        "hero": {"image": "youtube-hub", "alt": "Gerçek büyümenin ilk ayında bir YouTube kanalının analizleri"},
        "sections": [
            {
                "h2": "Bir denemenin size gösteremeyeceği",
                "p": [
                    "Soru bir sayının artıp artamayacağı değil. Gerçek insanların izleyip izlemediği, beğenip beğenmediği ve kalıp kalmadığı; bunu görmek de haftalar alır. Bir günlük numune bir test değil, bir satış numarasıdır.",
                ],
            },
            {
                "h2": "Ay boyunca bizi nasıl kontrol edersiniz?",
                "ul": [
                    "Panele birkaç günde bir bakın: kampanyadan gelen ziyaretler ve yeni aboneler, ölçüldüğü gibi.",
                    "Video analizlerinize bakın: yeni izleyiciler izliyor mu?",
                    "Yorumları okuyun: videolarınız hakkında kendi cümleleriyle yazan insanlar.",
                    "Yenileme tarihinden önce karar verin; hesabınızdan istediğiniz an iptal edebilirsiniz.",
                ],
            },
        ],
        "faqs": [
            ("YouTube için ücretsiz denemeniz var mı?", "Hayır. Hiçbir platformda deneme yapmıyoruz. En kısa paket bir aydır ve bir sonraki başlamadan iptal edebilirsiniz."),
            ("Diğer siteler sunarken siz neden deneme sunmuyorsunuz?", "Getirdiğimiz her abone, ilk günden para tutan gerçek bir kampanyadan gelir. Bedava numune dağıtabilen satıcılar genellikle izleyici değil hesap gönderiyordur."),
            ("Bir aydan sonra iptal edersem ne olur?", "Başka ödeme alınmaz ve ödenen ay sonuna kadar sürer. Gerçek aboneler geri alınmaz; ayrılmaya kendileri karar vermedikçe kalırlar."),
            ("İlk ay içinde sonuç görür müyüm?", "Hızı görürsünüz: her gün gelen yeni aboneler, {starter_name} ile ay boyunca genellikle {starter_audience}. Tipik, sabit değil; çünkü her biri kendi kararını veren biridir."),
            ("Önce daha küçük bir paketi deneyebilir miyim?", "{starter_name} en küçük paketimiz ve başlamak için doğal yer. Kanalınız daha fazlasına ihtiyaç duyarsa sonra yükseltebilirsiniz."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "smm-panel",
        "slug": "youtube/abone/smm-panel",
        "label": "SMM panelinden YouTube abone?",
        "title": "SMM Panelden YouTube Abone Almadan Önce | Growsterr",
        "description": "SMM panelleri YouTube abone ve izlenmesini binlik satar, düştüğü için telafiyle. Biz bir ajansız: gerçek izleyiciler ve ölçüm gösteren bir hesap paneli.",
        "h1": ("Panel abonelerinin bir telafi düğmesi vardır. ", "Bizimkilerin buna ihtiyacı yok."),
        "intro": "Bir SMM panelinden YouTube abone ya da izlenme almadan önce, panellerin yanına çoğu zaman koyduğu telafi seçeneğine dikkat edin: sayıların düşmesini bekliyorlar. Paneller bot trafiğini toptan yeniden satar. Biz bunun yerine bir ajans olarak çalışırız: ekibimizden insanlar kampanyanızla ilgilenir, gerçek izleyiciler kanalınızı bulup abone olur ve hesap paneliniz ölçtüklerimizi raporlar.",
        "hero": {"image": "youtube-channel", "alt": "Ölçülmüş yeni YouTube abonelerini gösteren bir paneli kontrol eden bir içerik üreticisi"},
        "sections": [
            {
                "h2": "Biner biner abone ve izlenme",
                "p": [
                    "Bir panelde YouTube abonesi, izlenmesi ve izlenme süresi binlik fiyatla, başlangıç süreleri ve telafi notlarıyla tek bir listede durur. Kimse kanalınıza bakmaz. Sipariş bir kuyruğa girer ve hesaplar kuyruğun söylediğini yapar.",
                    "Panel izlenmeleri de aynı şekilde işler: kimsenin izlemeye karar vermediği oynatmalar; YouTube'un izlenme sayılarından ayıklamaya çalıştığı türden.",
                ],
            },
            {
                "h2": "Bir ajansla ne değişir?",
                "ul": [
                    "Kuyruk yerine insanlar: kanalınız her gün gerçek izleyicilere gösterilir.",
                    "Her abone, beğeni, izlenme ve yorum bir insana dayanır.",
                    "Kampanyanızın arkasında bir ekip ve sorularınız olduğunda bize ulaşmanın bir yolu.",
                    "Doldurulması gereken bir sayaç değil, ölçtüklerimizi gösteren bir panel.",
                ],
            },
        ],
        "faqs": [
            ("Panel aboneleri gerçek insanlar mı?", "Hayır. Paneller talimatla abone olan hesaplardan gelen toptan trafiği yeniden satar; telafinin teklifin parçası olmasının nedeni de bu."),
            ("YouTube izlenmesini tek başına satıyor musunuz?", "Hayır. İzlenmeler ayrı bir kalem değil. Kampanyamızın ulaştığı, abone olan, beğenen ve yorum yapan aynı insanlardan gelirler."),
            ("Panel izlenmeleri kanalımı sıkıntıya sokabilir mi?", "Evet. Yapay izlenmeler YouTube'un sahte etkileşim kurallarını çiğner; sayınızdan silinebilirler ve tekrarlanan kullanım kanalı riske atar."),
            ("Bayi paneli sunuyor musunuz?", "Hayır. Toptan ya da bayiler üzerinden satmıyoruz: her paket tek bir kanalın etrafında kurulan bir kampanyadır. Birkaç kanalı olan ajanslar konuşmak için bize ulaşabilir."),
            ("Bir paket her ay ne getirir?", "{pick_name} genellikle ayda {pick_audience} yeni abone getirir; 30 güne yayılarak gelen gerçek izleyiciler."),
        ],
    },
    # --- Views ----------------------------------------------------------------------------
    {
        "service": "views",
        "modifier": "cheap",
        "slug": "youtube/izlenme/ucuz",
        "label": "Ucuz YouTube izlenme?",
        "plan": "starter",
        "title": "Ucuz YouTube İzlenme mi? Birkaç Lira Ne Getirir | Growsterr",
        "description": "Binliği birkaç liraya satılan ucuz YouTube izlenmeleri izleyici değil, oynatmadır. Aylık paketimiz izleyen, abone olan ve yorum yapan gerçek insanlar getirir.",
        "h1": ("Ucuz YouTube izlenmeleri ", "izleyici değil, oynatmadır."),
        "intro": "YouTube izlenmesini ucuza, diyelim binini birkaç liraya almayı planlıyorsanız ne geldiğini bilin: en fazla birkaç saniye izleyen yazılımlardan ya da toplu hesaplardan oynatmalar; YouTube da onları sayınızdan silebilir. İzlenmeyi ayrıca satmıyoruz. Aylık paketimiz kanalınıza gerçek insanlar getirir; onlar da kendi seçimleriyle izler, beğenir, yorum yapar ve abone olur.",
        "hero": {"image": "youtube-viewers", "alt": "Bir YouTube videosunu sonuna kadar izleyen gerçek izleyiciler"},
        "sections": [
            {
                "h2": "Bir izlenmenin değeri",
                "p": [
                    "Bir izlenme, bir insan izlediğinde işe yarar. Ne kadar kaldıkları, beğenip beğenmedikleri ve sonra hangi videoya tıkladıkları, YouTube'a bir videonun daha çok izleyiciyi hak ettiğini gösteren şeylerdir. Ucuz bir izlenme sayaca bir ekler ve YouTube'a üzerinde çalışacak hiçbir şey vermez.",
                    "Neredeyse hiç izlenme süresi olmayan büyük bir izlenme sayısı da karışık bir sinyal verir; satın alınan oynatmalar zaten silinebilir.",
                ],
            },
            {
                "h2": "Dürüst türden bir YouTube izlenme paketi",
                "p": [
                    "Bir paket satıyoruz, yalnızca bir izlenme paketi değil. {starter_name} ayda {starter_price}: gerçek izleyicilerden genellikle {starter_audience} yeni abone, {starter_likes} beğeni ve {starter_comments} yorum; artı aynı insanların videolarınıza verdiği izlenmeler.",
                    "İzlenmeler önceden sayılmaz. Bir kotayı değil içeriğinizi izlerler, çünkü her biri birinin seçimidir.",
                ],
            },
            {
                "h2": "İzlenme başına fiyat mı, izleyici başına fiyat mı?",
                "p": [
                    "İzlenmeleri değil izleyicileri sayın. Gerçek bir abone, kaldığı aylar boyunca onlarca videonuzu izleyebilir. Birkaç liralık yazılım oynatması ise bugünden sonra hiçbir şey izlemez.",
                ],
            },
        ],
        "faqs": [
            ("Sizde YouTube izlenmesi ne kadar tutar?", "İzlenmelerin tek başına bir fiyatı yok. En düşük paket olan {starter_name} ayda {starter_price}; abone, beğeni ve yorum getirir, izlenmeler de aynı insanlardan gelir."),
            ("Birkaç liralık izlenmeler neden bu kadar ucuz?", "Çünkü kimse izlemiyor. Yazılımlar ve toplu hesaplar neredeyse hiçbir maliyet olmadan oynatma üretebilir; ürettikleri de yalnızca oynatmadır."),
            ("Ucuz izlenmeler bana gerçek izleyici getirir mi?", "Pek olası değil. YouTube yalnızca sayıya değil, insanların bir videoya nasıl tepki verdiğine bakar; satın alınan izlenmeler tepki vermez."),
            ("Hangi videoların izleyici alacağını seçebilir miyim?", "Yeni izleyicilerin varacağı bir videoyu sipariş verirken ya da sonra hesabınızdan belirtebilirsiniz. Gerisinde kanalınızı bir bütün olarak tanıtırız ve izleyiciler ne izleyeceklerini seçer; güçlü başlıklar ve küçük resimler en iyi işlerinizi bulmalarına yardım eder."),
            ("Yalnızca izlenme için çok ucuz bir paket var mı?", "Ayda {starter_price} olan {starter_name} paketinin altında yalnızca izlenmeye yönelik bir seçenek yok; çünkü izlenmeler bir paketin getirdiği insanlardan gelir."),
        ],
    },
    {
        "service": "views",
        "modifier": "fast",
        "slug": "youtube/izlenme/hizli",
        "label": "Hızlı YouTube izlenme?",
        "title": "Hızlı YouTube İzlenme: Gerçek İzleyici Nasıl Gelir? | Growsterr",
        "description": "Prömiyer dahil anında YouTube izlenmeleri yazılımdan gelir. Gerçek izleyiciler kampanyanızın ilk günlerinden itibaren kanalınızı bulur ve gelmeye devam eder.",
        "h1": ("Hızlı YouTube izlenme mi? ", "İzleyiciler kargoyla gelmez."),
        "intro": "YouTube izlenmeyi hızlı, anında teslimatla mı satın almak istiyorsunuz? Bir zamanlayıcıyla teslim edilen izlenmeler insanlardan değil yazılımlardan gelir: gerçek bir izleyici, bir video gözüne çarptığında tıklar. İzlenme satmıyor ya da teslim etmiyoruz. Kampanyanızın ilk günlerinden itibaren her gün kanalınıza gerçek insanlar getiririz; onlar da kendi istekleriyle izler, beğenir ve abone olur.",
        "hero": {"image": "youtube-viewers", "alt": "Bir içerik üreticisinin yeni YouTube videosunu keşfeden izleyiciler"},
        "sections": [
            {
                "h2": "Hızlı teslimat bir kargo kelimesidir",
                "p": [
                    "Teslimat süreleri kutudaki şeyler için anlamlıdır. İzlenmelerde bir teslimat hızı, oynat tuşuna bir makinenin bastığı anlamına gelir; o oynatmalar da sahip olmaya değer hiçbir izlenme süresi getirmez.",
                ],
            },
            {
                "h2": "Prömiyer izlenmeleri gerçek insanlar ister",
                "p": [
                    "Prömiyer bir andır: bekleyen, sohbet eden ve birlikte izleyen insanlar. Satın alınan prömiyer izlenmeleri bir sayacı doldurabilir ama sohbeti asla. Biz de belirli bir dakikaya kitle getiremeyiz ve getirebiliyormuş gibi yapmayız.",
                    "Yardım eden şey, prömiyeri ana sayfalarında ya da abonelik akışlarında görüp hatırlatıcı kurabilecek daha büyük bir gerçek abone tabanıdır.",
                ],
            },
            {
                "h2": "Gerçek izlenmeler ne kadar hızlı birikir?",
                "ul": [
                    "İlk günlerde kampanyanız başlar ve yeni izleyiciler kanalınıza ulaşır.",
                    "Bu ay yüklediğiniz her video, geçen hafta abone olan insanlar için oradadır.",
                    "Bu aboneler videolarınızdan keyif aldıkları sürece izlenme gelmeye devam eder.",
                ],
            },
        ],
        "faqs": [
            ("İzlenmelerim ne kadar hızlı artar?", "Kampanya başladığında, yani ilk günlerinde, yeni insanlar kanalınızı buldukça izlenmeler yükselir. Tek bir videoda sıçramak yerine kitlenizle birlikte büyür."),
            ("Yeni bir videoya anında izlenme gönderebilir misiniz?", "Hayır. Anında izlenmeler yazılımdan gelir. Yeni bir videodaki gerçek izlenmeler, onu akışında ya da önerilerde gören insanlardan gelir; bizim işimiz o grubu büyütmek."),
            ("Prömiyerimi canlı izleyicilerle doldurabilir misiniz?", "Kimse belirli bir dakikada gerçek insan vaat edemez. Bir prömiyerden önce gerçek aboneleri büyütmek, katılabilecek daha çok insanınız olmasını sağlar."),
            ("İzlenmeler paketimde sayılıyor mu?", "Paketin içinde gelirler, belirli bir sayı olmadan. Abone olan, beğenen ve yorum yapan aynı insanlar izler de; yani izlenmeler kitlenizi izler."),
            ("En çok izlenmeyi hangi paket getirir?", "Paketleri izlenmeye göre boyutlandırmıyoruz. Daha büyük bir paket daha çok insana ulaşır; bu yüzden genellikle ayda {pro_audience} yeni aboneyle {pro_name}, çoğu zaman daha çok izleyen insan demektir."),
        ],
    },
    {
        "service": "views",
        "modifier": "free",
        "slug": "youtube/izlenme/ucretsiz",
        "label": "Ücretsiz YouTube izlenme?",
        "plan": "starter",
        "tool": "engagement-calculator",
        "title": "Ücretsiz YouTube İzlenme Neden İşe Yaramaz? | Growsterr",
        "description": "Shorts dahil ücretsiz YouTube izlenmeleri takas sitelerinden ve yazılımlardan gelir. İzlenme dağıtmıyoruz; etkileşiminizi ücretsiz hesaplayıcımızla ölçün.",
        "h1": ("1.000 ücretsiz YouTube izlenmesi ", "videonuzu izlemez. Gerçek insanlar izler."),
        "intro": "1.000 ücretsiz YouTube izlenmesi ya da bedava Shorts izlenmesi teklifleri izlenme takaslarıyla, otomatik oynatma hileleriyle ya da bot oynatmalarıyla çalışır; hiçbiri izleyen birini getirmez. Biz izlenme dağıtmıyoruz. Aşağıdaki etkileşim hesaplayıcı ücretsizdir ve abonelerinizin ne kadarının tipik bir videoya tepki verdiğini söyler. Daha çok gerçek insanın izlemesini istediğinizde paketlerimiz onları getirir.",
        "hero": {"image": "youtube-channel", "alt": "Son videolarındaki beğeni ve yorumlara bakan bir YouTuber"},
        "sections": [
            {
                "h2": "Ücretsiz izlenmeler nereden gelir?",
                "ul": [
                    "İzlenme takasları: kredi için yabancıların videolarını izlersiniz, onlar da sizinkini sessizde oynatır.",
                    "Kimsenin seçmediği bir oynatmayı sayan yerleştirmeler ve otomatik oynatma hileleri.",
                    "Daha büyüklerini satmak için küçük partiler halinde dağıtılan bot oynatmaları.",
                    "Bir saniye sonra kaydırıp geçen yazılımlardan bedava Shorts izlenmeleri.",
                ],
            },
            {
                "h2": "Etkileşiminizi hesaplayıcıyla kontrol edin",
                "p": [
                    "Bu hesaplayıcı tamamen tarayıcınızda, ücretsiz çalışır. Takipçi sayısını sorduğu yere abone sayınızı girin; sonra son videolarınızdaki ortalama beğeni ve yorumu ekleyin. Sonuç, kitlenizin tepki veren kısmıdır; bir izlenme sayısından çok daha iyi bir sağlık kontrolü.",
                ],
            },
            {
                "h2": "Daha çok izlenme kazanmanın ücretsiz yolları",
                "ul": [
                    "Başlığa ve küçük resme kurguya harcadığınız kadar zaman ayırın; tıklamaya onlar karar verir.",
                    "Bir videonun ya da Shorts'un ilk saniyelerinde sadede gelin.",
                    "Bir izlenmenin bir sonrakine götürmesi için bitiş ekranları ve oynatma listeleri ekleyin.",
                    "Yorumlara cevap verin; insanlar sohbetlere geri döner.",
                ],
            },
        ],
        "faqs": [
            ("1.000 YouTube izlenmesini ücretsiz alabilir miyim?", "Gerçek insanlardan hayır, bizden de hayır. Bedava bin izlenme takaslardan ya da yazılımlardan gelir. Bu sayfada gerçekten ücretsiz olan kısım hesaplayıcı."),
            ("Ücretsiz Shorts izlenmeleri farklı mı?", "Hayır. Aynı hilelerden gelirler. Bir Shorts videosu ancak gerçek insanlar onu sonuna kadar izlediğinde yol alır; yazılım oynatmaları ona yardım etmez."),
            ("Ücretsiz izlenmeler kanalımın yaptırım almasına yol açabilir mi?", "Gerçek bir risk. Otomatik sistemlerden ya da takaslardan gelen izlenmeler YouTube'un sahte etkileşim politikasına girer; YouTube onları silebilir ya da kanala karşı önlem alabilir."),
            ("Ücretsiz bir izlenme paketiniz var mı?", "Hayır. En küçük paket ayda {starter_price} olan {starter_name}; izlenmeler de içinde, abone olan gerçek insanlardan gelir."),
            ("Etkileşim oranı bana ne söyler?", "Kitlenizin ne kadarının gerçekten orada olduğunu. Büyük bir abone sayısıyla düşük bir oran, genellikle birçok abonenin izlemeyi bıraktığını ya da hiç izlemediğini gösterir."),
        ],
    },
    {
        "service": "views",
        "modifier": "free-trial",
        "slug": "youtube/izlenme/ucretsiz-deneme",
        "label": "YouTube izlenme ücretsiz deneme?",
        "plan": "starter",
        "title": "Ücretsiz YouTube İzlenme Denemesi mi? Doğru Test | Growsterr",
        "description": "Ücretsiz YouTube izlenme denemesi yok ve izlenmeyi tek başına satmıyoruz. Bizi bir aylık gerçek izleyicilerle ve YouTube'un kendi analizleriyle test edin.",
        "h1": ("Bir YouTube izlenme denemesi ", "yalnızca bir sayacın oynayabildiğini kanıtlar."),
        "intro": "Hiçbir şey ödemeden önce ücretsiz denemeyle YouTube izlenme mi satın almak istiyorsunuz? Burada deneme yok ve izlenme de asla tek başına satılmaz. Bir saatte birkaç bin izlenmelik bir deneme, yalnızca birinin yazılımı olduğunu gösterirdi. Sunduğumuz, kanalınıza gerçek insanlar getiren aylık bir paket; izlenmeler de aynı insanlardan gelir ve istediğiniz zaman iptal edebilirsiniz.",
        "hero": {"image": "youtube-hub", "alt": "YouTube analizlerini bir büyüme paneliyle karşılaştıran bir içerik üreticisi"},
        "sections": [
            {
                "h2": "Bir izlenme denemesi neyi ölçer?",
                "p": [
                    "Tek bir şeyi: sayının oynayıp oynamadığını. Kimin izlediği, ne kadar izlediği ya da birinin geri gelip gelmediği hakkında hiçbir şey söylemez. Önemli olan sorular bunlardır ve onları yalnızca gerçek izleyiciler cevaplayabilir.",
                ],
            },
            {
                "h2": "Bizi YouTube'un kendi rakamlarıyla test edin",
                "p": [
                    "İlk ayınızda YouTube Studio'yu panelimizin yanında açın. Geri gelen izleyicilere, ortalama izlenme süresine ve yeni abonelere bakın. Gerçek insanlar bu rakamlarda, satın alınan oynatmaların asla bırakmadığı bir iz bırakır.",
                ],
            },
        ],
        "faqs": [
            ("YouTube izlenmesi için deneme var mı?", "Ne izlenme ne de başka bir şey için deneme yok. En kısa taahhüt bir aylık pakettir ve yenilenmeden önce iptal edebilirsiniz."),
            ("Test etmek için küçük bir izlenme paketi alabilir miyim?", "İzlenmeyi küçük ya da büyük ayrı bir paket olarak satmıyoruz. Ayda {starter_price} olan {starter_name}, başlamanın en küçük yolu."),
            ("Gerçek izlenmeleri satın alınanlardan nasıl ayırt ederim?", "Sayının ötesine bakın: izlenme süresi, geri gelen izleyiciler ve insanların yazdığı yorumlar size orada gerçekten kimin olduğunu söyler."),
            ("İlk aydan sonra iptal edersem ne olur?", "Paketiniz ödenen ay bittiğinde durur. Abone olan izleyiciler, ayrılmayı kendileri seçmedikçe abone kalır."),
            ("İzlenmeler aboneyle birlikte mi gelir?", "Evet. Her paket yeni abone, beğeni ve yorum getirir; aynı insanlar videolarınızı da izler."),
        ],
    },
]
