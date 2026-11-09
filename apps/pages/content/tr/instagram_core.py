"""Turkish Instagram pages: comments, likes, and the ways people ask for followers and likes
(gradual, organic, local, private accounts...). Mirrors en/instagram_core.py; keys and
placeholders: docs/CONTENT.md. Numbers come from the packages ({starter_likes}...)."""

UPDATED = "2026-11-09"

PAGES = [
    # --- Comments -----------------------------------------------------------------------
    {
        "service": "comments",
        "slug": "instagram/yorum",
        "label": "Instagram yorum",
        "title": "Instagram Yorum Satın Al: Gerçek İnsanlardan | Growsterr",
        "description": "Instagram yorum satın almak mı istiyorsunuz? Yorumlar her aylık paketin içinde, gerçek insanların kendi cümleleriyle gelir: genellikle ayda {starter_comments}.",
        "h1": ("Instagram yorum satın alın: ", "ne yazdığını bilen gerçek insanlardan."),
        "intro": "Instagram yorum satın almak için buradaysanız, bilmeniz gereken şu: yorumları tek bir yolla getiriyoruz. Aylık bir paketin içinde, gönderilerinizi keşfeden ve söyleyecek bir sözü olan gerçek insanlardan. {starter_name} ile genellikle ayda {starter_comments}, {pick_name} ile {pick_comments} yorum.",
        "hero": {"image": "instagram-real-people", "alt": "Bir Instagram gönderisinin altına kendi yorumlarını, sorularını ve emojilerini bırakan insanlar"},
        "sections": [
            {
                "h2": "Gerçek bir yorum bölümü neye benzer?",
                "p": [
                    "Gerçek yorumlar düzensizdir. Biri ceketin nereden alındığını sorar, bir başkası arkadaşını etiketler, bir diğeri iki kelime ve bir emoji yazar. Yorum bölümünü inandırıcı kılan tam da bu düzensizliktir; önceden yazılmış yorumların taklit edemediği şey de budur.",
                    "Toplu satın alınan yorumlar genellikle kendi gönderisi olmayan hesaplardan, birbirinin neredeyse aynısı satırlar halinde gelir. Akışta gezinen herkes bunları fark eder; etkilemek istediğiniz markalar ve iş birliği yapmak istediğiniz kişiler de.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "Masasında bir Instagram gönderisine gelen yorumları yanıtlayan bir içerik üreticisi"},
            },
            {
                "h2": "Her paket kaç yorum getirir?",
                "ul": [
                    "{starter_name}, ayda {starter_price} ile genellikle {starter_comments} yorum getirir; insanların en çok sevdiği gönderilere.",
                    "{rising_name}, {rising_price} ile genellikle {rising_comments} yorum getirir; ilginin hangi gönderilere gideceğini siz seçersiniz.",
                    "{pro_name}, {pro_price} ile genellikle {pro_comments} yorum getirir; üstüne öncelikli yerleşim ve doğrudan bir WhatsApp hattı.",
                ],
            },
            {
                "h2": "Yorumlar neden yalnızca paketle gelir?",
                "p": [
                    "Kırk yorumu ve bir düzine beğenisi olan bir gönderi, ne olduğunu herkese anlatır. Yorumlar ancak gerçek ilginin getirdiği takip, beğeni ve izlenmelerin yanında doğru görünür. Bu yüzden biz ilgiyi getiririz, yorumlar da o ilgiden doğar.",
                ],
            },
        ],
        "faqs": [
            ("Paket olmadan Instagram yorumu alabilir miyim?", "Hayır. Yorumlar yalnızca aylık paketlerimizin içinde, kampanyalarımız sayesinde profilinizi bulan insanlardan gelir. Kimse sipariş üzerine yorum yazmaz; bu yüzden yorumlar gerçek bir sohbet gibi okunur."),
            ("Yorumlarda ne yazılacağını seçebilir miyim?", "Hayır. İnsanlar kendi cümleleriyle yazar, yani bizim önceden hazırlayacağımız bir metin yoktur; bir talimata göre yazılan yorumlar da nadiren birinin gerçek tepkisi gibi okunur. Bunun yerine {rising_name} ya da {pro_name} ile ilginin nereye gideceğini seçebilirsiniz: sizin seçtiğiniz gönderilere."),
            ("Yorumlar ne zaman görünür?", "Ay boyunca azar azar, insanlar gönderilerinizi keşfettikçe. On dakikada gelen yüz yorum bir kitle değil, bir yazılımdır."),
            ("Yorumlar gönderilerimin daha çok kişiye ulaşmasına yardım eder mi?", "Yorumlar, insanların bir gönderiyi önemsediğini gösterir ve Instagram bunu fark eder. Gerçek yorumlar buna katkı sağlar. Erişim sözü veremeyiz, dürüst olan kimse veremez; ama önceden yazılmış yorumlar yalnızca gürültü ekler."),
            ("Şifremi istiyor musunuz?", "Hayır. Instagram kullanıcı adınız ve kitlenizin nereden gelmesi gerektiği yeterli. Hesabınızı herkese açık tutun ki insanlar gönderilerinizi okuyup sohbete katılabilsin."),
        ],
    },
    # --- Followers: the ways people ask for them ---------------------------------------
    {
        "service": "followers",
        "modifier": "gradual",
        "slug": "instagram/takipci/kademeli",
        "label": "Kademeli Instagram takipçi",
        "title": "Instagram Takipçi Satın Al: Her Gün, Toplu Değil | Growsterr",
        "description": "Instagram takipçiyi tek seferde değil, gün gün alın: gerçek insanlar 30 gün boyunca her gün profilinizi keşfeder, büyüme kendiliğinden kademeli olur.",
        "h1": ("Instagram takipçi satın alın, her gün biraz: ", "insanlar gerçekten böyle takip eder."),
        "intro": "Instagram takipçiyi bir seferde değil de her gün biraz almak istiyorsanız, zaten bir kitle gibi düşünüyorsunuz. Kampanyalarımız profilinizi 30 gün boyunca her gün gerçek insanlara gösterir; takipçiler de gün gün, kademeli olarak gelir: {pick_name} ile ay boyunca genellikle {pick_audience}.",
        "hero": {"image": "instagram-followers-1000", "alt": "Bir ay boyunca her gün biraz yükselen bir takipçi sayısı"},
        "sections": [
            {
                "h2": "Damla damla gönderim bir ayardır, günlük büyüme bir kampanya",
                "p": [
                    "Bazı hizmetler yavaş bir damlatma satar: eğri doğal görünsün diye birkaç birkaç salınan bir hesap yığını. Hesaplar yine bottur; gizlenen yalnızca zamanlamadır.",
                    "Bizim hızımız bir ayar değil. Profiliniz her gün insanlara gösterilir ve her takip, biri karar verdiğinde gerçekleşir. Kademeli eğri, insanların seçim yapmasının dışarıdan görünüşünden ibarettir.",
                ],
            },
            {
                "h2": "Yavaş yavaş, neden hepsi birden olmaktan iyidir?",
                "ul": [
                    "İstikrarlı bir yükseliş olduğu gibi görünür: insanların keşfetmeye devam ettiği bir hesap.",
                    "Her günün yeni takipçileri, ilgileri tazeyken bir sonraki gönderinizle karşılaşır.",
                    "Bir markanın ya da bir takipçinin sorgulayacağı ani bir sıçrama olmaz.",
                    "Neyin işe yaradığını görürsünüz, çünkü her gün kendi başına bir veri noktasıdır.",
                ],
            },
            {
                "h2": "Günlük rakamlarınızı okumak",
                "p": [
                    "Paneliniz her gün için, kampanya üzerinden profilinizi kaç kişinin ziyaret ettiğini ve bunlardan kaçının takip ettiğini listeler. Bazı günler daha yoğundur: güçlü bir gönderi, bir hafta sonu, bir bayram. Ay boyunca bu günler sabit bir günlük kotaya değil, tipik bir aralığa ulaşır.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "Profil ziyaretlerini ve yeni takipçileri gün gün gösteren grafiğe bakan bir içerik üreticisi"},
            },
        ],
        "faqs": [
            ("Her gün kaç takipçi gelir?", "Sabit bir günlük sayı yok, çünkü insanlar kendi kararını verir. {pick_name} ay boyunca genellikle {pick_audience} getirir; ortalama bir gün bunun bir dilimini getirir, bazı günler daha fazla, bazıları daha az."),
            ("Gönderim hızını kendim ayarlayabilir miyim?", "Hayır, buna gerek de yok. Hız bir düğmeden değil, insanlardan gelir: kampanya her gün çalışır ve takipçiler biri karar verdiğinde gelir."),
            ("Kademeli büyüme, büyük bir yığından daha mı az risklidir?", "Bir saatte yüzlerce takipçi, botların bıraktığı bir izdir. Gerçek insanlardan gelen kademeli büyüme bu izi bırakmaz, çünkü ortada bir kalıp yoktur. Instagram'ın bir hesaba nasıl davrandığı adına konuşamayız; yalnızca getirdiğimiz her takipçinin bir insan olmasını sağlayabiliriz."),
            ("Kademeli, daha az büyüme demek mi?", "Hayır. Kademeli, toplamı değil şekli anlatır. Biri ikinci gün de takip etse yirmi dokuzuncu gün de, ayın tipik aralığı aynıdır; yalnızca bir kitlenin oluştuğu şekilde gelir."),
            ("Beğeni ve yorumlar da kademeli mi gelir?", "Evet. Aynı insanlar gönderilerinizi buldukça beğenir ve yorum yapar; ikisi de takipçilerinizle birlikte birikir. {pick_name} ile bu, ay boyunca genellikle {pick_likes} beğeni ve {pick_comments} yorum eder."),
        ],
    },
    {
        "service": "followers",
        "modifier": "live",
        "slug": "instagram/takipci/canli-yayin",
        "label": "Instagram takipçi: teslimat ve canlı yayın",
        "title": "Instagram Takipçi Teslimatı Ne Kadar Hızlı? | Growsterr",
        "description": "Instagram takipçi satın alınca teslimat ne kadar hızlı? Kampanya kısa sürede başlar, her gün büyür ve canlı yayınlarınıza bir kitle kazandırır.",
        "h1": ("Hızlı teslimatlı Instagram takipçi mi arıyorsunuz? ", "Hızlı ne demek, anlatalım."),
        "intro": "Hızlı teslimatlı Instagram takipçi satın almak genelde iki şeyden birini ifade eder: dakikalar içinde fırlayan bir sayaç ya da hemen başlayıp devam eden bir kampanya. Biz yalnızca ikincisini yapıyoruz. Kampanyanız kısa sürede başlar, gerçek insanlar ilk günlerden gelir ve paneliniz her günün ne getirdiğini gösterir.",
        "hero": {"image": "instagram-creator-studio", "alt": "Masasındaki düzenekten Instagram'da canlı yayına hazırlanan bir içerik üreticisi"},
        "sections": [
            {
                "h2": "Gereken yerde hızlı, asla anında değil",
                "p": [
                    "Hızlı olan kısım başlangıçtır. Siparişinizden kısa süre sonra kampanyanızı kurarız ve insanlar ilk günlerden profilinizi görmeye başlar. Yapmayacağımız şey, bir aylık gerçek kararı bir saate sıkıştırmaktır; çünkü bunun tek yolu kimsenin kullanmadığı hesaplardır.",
                    "Bu yüzden teslimat sürelerini karşılaştırırken bir sayının ne kadar hızlı zıpladığına değil, gerçek büyümenin ne zaman başladığına ve sürüp sürmediğine bakın.",
                ],
            },
            {
                "h2": "Instagram canlı yayınlarınız için takipçiler",
                "p": [
                    "Canlı yayın takipçisi, siz yayına geçtiğinizde gelen takipçidir. Instagram bir yayın başladığında takipçilerinize haber verebilir; yani sizi takip etmeyi seçen insan sayısı arttıkça yayına katılabilecek insan sayısı da artar.",
                    "Canlı yayın izleyicisi satmıyoruz ve kimse belirli bir saatte bir kalabalık sözü veremez: insanlar ilgilendiklerinde ve müsait olduklarında katılır. Ay boyunca kazandığınız takipçiler, katılma ihtimali en yüksek olanlardır.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Bir içerik üreticisinin Instagram canlı yayınına katılıp yayın sürerken yorum yapan takipçiler"},
            },
            {
                "h2": "Beğenilerde de kademeli teslimat",
                "p": [
                    "Beğeniler de aynı ritmi izler. Profilinizi keşfeden insanlardan geldikleri için ay boyunca gönderilerinize yavaş yavaş düşerler; {pick_name} ile genellikle {pick_likes}. Planlanacak ayrı bir beğeni siparişi ve açıklanması gereken bir patlama yoktur.",
                ],
            },
        ],
        "faqs": [
            ("Teslimat ne kadar sürede başlar?", "Kısa sürede. Siparişiniz geldiğinde kampanyayı kurarız ve insanlar ilk günlerden profilinizi ziyaret etmeye başlar. Takipler bu ziyaretlerle başlar ve ay boyunca sürer."),
            ("Anında teslimat alabilir miyim?", "Hayır. Anında teslimat yalnızca botlarla olur, çünkü hiçbir insan bir ödemeden saniyeler sonra takip etmez. Biz bunun yerine hızlı başlar, her gün büyütürüz."),
            ("Bu akşamki canlı yayınımdan önce yeni takipçilerim olur mu?", "Kampanyanız zaten çalışıyorsa belki birkaç tane; ama insanları bir yayına göre zamanlayamayız. Bir canlı yayın sizin için önemliyse birkaç hafta önceden başlayın ki yeni takipçileriniz sizi tanımaya zaman bulsun."),
            ("Instagram canlı yayın için izleyici satıyor musunuz?", "Hayır. Canlı yayın izleyicisi, belirli bir dakikada izleyen insanlar demektir ve bunu dürüstçe kimse teslim edemez. Getirdiğimiz takipçiler canlı yayınlarınıza kendi istekleriyle katılabilir."),
            ("Teslimatımı nereden takip edebilirim?", "Panelinizden. Kampanyamızın getirdiği profil ziyaretlerini ve bunlardan gelen takipleri gün gün sayar. Hesabınızın kendi toplamı ise diğer büyümenizle ve takipten çıkanlarla birlikte değişir."),
        ],
    },
    {
        "service": "followers",
        "modifier": "no-drop",
        "slug": "instagram/takipci/dusmeyen",
        "label": "Düşmeyen Instagram takipçi",
        "title": "Düşmeyen Instagram Takipçi: Gerçek İnsanlar Kalır | Growsterr",
        "description": "Düşmeyen, kalıcı Instagram takipçi mi arıyorsunuz? Bot hesaplar temizliklerde silinir. Gerçek insanlar kalır, çünkü sizi takip etmek kendi fikirleriydi.",
        "h1": ("Düşmeyen Instagram takipçi ", "gerçek insanlarla başlar."),
        "intro": "Kalıcı Instagram takipçi satın almak için araştıran herkes öbür türünü görmüştür: bir sıçrama, ardından yavaş yavaş geri eriyen bir sayı. Takipçiler, en başından insan değillerse düşer. Bizimkiler sizi takip etmeyi seçen insanlardır; her gerçek kitle gibi kalırlar, biri ayrılırsa da herhangi bir takipçinin ayrıldığı nedenlerle ayrılır.",
        "hero": {"image": "instagram-followers", "alt": "Birkaç ay boyunca sabit kalıp yükselen bir Instagram takipçi sayısı"},
        "sections": [
            {
                "h2": "Satın alınan takipçiler neden düşer?",
                "p": [
                    "Instagram sahte ve spam hesapları düzenli olarak siler. Takipçileriniz bu hesaplarsa her temizlik sayınızdan bir parça koparır. Telafi gönderimleri sayıyı yine aynı türden hesaplarla doldurur ve döngü yeniden başlar.",
                    "Bir insan temizlikte silinmez. Yalnızca takibi bırakmaya karar verirse ayrılır; bu çok daha seyrek olur ve gönderilerinizin etkileyebileceği bir şeydir.",
                ],
            },
            {
                "h2": "Takipçileri ne tutar?",
                "ul": [
                    "Sizi onlar seçti; ilgiyle başlayan bir takip genellikle uzun sürer.",
                    "Kitlenizin yaşadığı yerden gelirler, bu yüzden gönderileriniz onlara anlamlı gelir.",
                    "Sonraki gönderilerinizi görürler ve her iyi gönderi kalmak için bir nedendir.",
                    "Paylaşım ritminiz bizim yaptığımız her şeyden önemlidir: insanlar merakla beklediği gönderiler için kalır.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Uzun süredir takip edenlerin bir içerik üreticisinin en yeni gönderisini hâlâ beğenip yorumlaması"},
            },
            {
                "h2": "Düşmemenin dürüst tanımı",
                "p": [
                    "Kimsenin asla takibi bırakmayacağını söylemeyeceğiz, çünkü insanlar öyle değildir. Söyleyebileceğimiz şu: sahte hesapların yol açtığı kayıp dalgalarını görmezsiniz. Paneliniz de kampanyamızın getirdiği yeni takipçileri gün gün gösterir; böylece neyin bizden geldiğini her zaman bilirsiniz.",
                ],
            },
        ],
        "faqs": [
            ("Takipçileriniz kalıcı mı?", "Onlar gerçek insanlar, bu yüzden istedikleri sürece kalırlar. Kimse bir insanın asla takibi bırakmayacağına söz veremez; söyleyebileceğimiz şey, hiçbirinin silinmeyi bekleyen sahte bir hesap olmadığıdır."),
            ("Takipçi düşerse telafi ediyor musunuz?", "Hayır, çünkü telafi edilecek bir şey yok. Telafi, temizliklerde kaybolan takipçiler için vardır. Bizimkiler insan; arada bir takibi bırakan olması her gerçek kitlenin parçasıdır."),
            ("Satın alınan takipçiler neden kaybolur?", "Çoğu zaman takibi bırakmazlar bile: hesaplar silinir. Instagram sahte ve spam profilleri dalgalar halinde siler, takipçi sayısı da onlarla birlikte düşer."),
            ("İptal edersem takipçilerime ne olur?", "Kalırlar. Bir abonelik söylediği için değil, istedikleri için takip ettiler. İptal etmek yalnızca ödenen ayınız bitince yeni insan getirmeyi bırakmamız demektir; kazandıklarınız takipçiniz olmaya devam eder."),
            ("Kazandığım takipçileri nasıl tutarım?", "Düzenli paylaşım yapın, yorumlara cevap verin ve yeni takipçilere ilk haftalarında geri gelmeleri için bir neden verin. İnsanlar, takip ettikleri nedenlerle kalır."),
        ],
    },
    {
        "service": "followers",
        "modifier": "organic",
        "slug": "instagram/takipci/organik",
        "label": "Organik Instagram takipçi",
        "title": "Organik Instagram Takipçi: Ödediğiniz Şey Erişim | Growsterr",
        "description": "Organik Instagram takipçi satın alınır mı? Seçtiğiniz yerde, her gün gerçek insanlara görünmek için ödeme yapabilirsiniz. Takip etmek yine onların kararıdır.",
        "h1": ("Organik Instagram takipçi satın almak mı? ", "Erişime ödeyin, seçimi insanlar yapsın."),
        "intro": "Aslında kimse organik Instagram takipçi satın alamaz: bir takip, onu bir insan seçtiği için organiktir. Satın alabileceğiniz şey erişimdir. Seçtiğiniz yerdeki gerçek insanlar her gün kampanyalarımız aracılığıyla profilinize denk gelir ve buradan doğan her takip, birinin kendi başına verdiği bir karardır.",
        "hero": {"image": "instagram-real-people", "alt": "Bir içerik üreticisinin Instagram profiline denk gelip takip etmeyi seçen insanlar"},
        "sections": [
            {
                "h2": "Ücretli kısım nerede biter, organik nerede başlar?",
                "p": [
                    "Kampanyalarımız tanıtımdır: profilinizi iş ortağı ağımızdaki insanların önüne çıkarmak için ödeme yaparız. Bu kısım ücretlidir ve bunu açıkça söylüyoruz. Sonrasındaki hiçbir şey ücretli değildir. Kimseden takip etmesi istenmez, kimse de bir takas karşılığında geri takip etmez.",
                    "Bir reklamla ya da başka birinin sayfasında öne çıkarılmakla aynı anlaşmadır: tanıştırılmanın bedelini ödersiniz, kararı kitle verir.",
                ],
            },
            {
                "h2": "Kitlenize göre hedeflenen organik takipçiler",
                "p": [
                    "Organik büyüme, sizi görenlerin ilgilenme ihtimali yüksek olduğunda en iyi sonucu verir. Kitlenizin yaşadığı şehri, bölgeyi ya da ülkeyi söyleyin; profilinizi önce orada gösteririz. İzmir'deki bir pastane ile Avrupa'nın dört bir yanında okuru olan bir gezi içerik üreticisi farklı insanlara ihtiyaç duyar, biz de hedefi buna göre belirleriz.",
                ],
            },
            {
                "h2": "Organik büyüme neleri dışarıda bırakır?",
                "ul": [
                    "Takibe takip takasları ve etkileşim grupları.",
                    "Ne kadar yavaş salınırsa salınsın, botlar ve sahte profiller.",
                    "Her türlü giriş bilgisi: şifreniz sizde kalır.",
                    "Hiçbir gerçek kitlenin yetişemeyeceği hızda takipçi patlamaları.",
                ],
            },
        ],
        "faqs": [
            ("Ücretli kampanyalar gerçekten organik mi?", "Erişim ücretli, takip değil. Her yeni takipçi profilinizi gördü ve kendi başına karar verdi; bir takipçiyi organik yapan da en başta budur."),
            ("Her gün gerçek Instagram takipçileri gelir mi?", "Evet. Kampanya ayın her günü çalışır ve insanlar sizi keşfettikçe takip eder. Bazı günler diğerlerinden fazlasını getirir; ay boyunca {pick_name} ile genellikle {pick_audience} eder."),
            ("Bu, Instagram reklamlarını kendim yürütmekle aynı şey mi?", "Ruhu benzer, pratiği farklı. Kampanyaları iş ortağı ağımızda biz yürütürüz, ekibimiz onlarla ilgilenir; siz de ölçülen ziyaretleri ve yeni takipçileri bir panelde görürsünüz. Bir reklam hesabına ya da yönetilecek bir bütçeye ihtiyacınız olmaz."),
            ("Organik büyüme gönderilerimin daha çok kişiye ulaşmasına yardım eder mi?", "Satın alınmış sayıların asla yapamayacağı kadar; çünkü organik takipçiler paylaştıklarınızı gerçekten görür ve tepki verir. Tek bir gönderinin ne kadar yol alacağı ise yine gönderiye bağlıdır."),
            ("Organik büyüme daha mı yavaş?", "Daha istikrarlı. Bir aylık organik büyüme bir saatte değil gün gün gelir ve bot patlamalarının ardından gelen düşüş onu izlemez."),
        ],
    },
    {
        "service": "followers",
        "modifier": "private-account",
        "slug": "instagram/takipci/gizli-hesap",
        "label": "Gizli hesaba Instagram takipçi",
        "title": "Gizli Instagram Hesabına Takipçi Almak | Growsterr",
        "description": "Gizli hesaba Instagram takipçi satın alınır mı? Gizli hesaba yalnızca takip isteği gönderilebilir; bu yüzden kampanya süresince herkese açık profil istiyoruz.",
        "h1": ("Gizli Instagram hesabına takipçi mi? ", "Büyürken hesabınızı herkese açın."),
        "intro": "Gizli hesabınıza Instagram takipçi satın almak ya da kazanmak istiyorsanız, dürüst cevap şu: insanlar gizli bir hesabı takip edemez, yalnızca takip isteği gönderebilir. Bu yüzden kampanyanız sürerken profilinizi herkese açık tutmanızı istiyoruz. Profilinizde ne olacağına yine siz karar verirsiniz ve şifrenize asla ihtiyacımız olmaz.",
        "hero": {"image": "instagram-followers", "alt": "Kilit simgeli gizli bir Instagram profili ve yanında aynı profilin herkese açık hali"},
        "sections": [
            {
                "h2": "Gizli hesap bir kampanyaya ne yapar?",
                "p": [
                    "Biri gizli bir profil bulduğunda bir isim, bir biyografi ve bir kilit görür. Takip isteği gönderebilir ama tek bir gönderi göremez; bu yüzden çoğu kişi geçip gider. İstek gönderen az sayıda kişi de onları tek tek onaylamanızı bekler.",
                    "İnsanları o kilitli kapıya gönderen bir kampanya, erişiminin çoğunu boşa harcar. Herkese açık bir profilde aynı insanlar gönderilerinize göz atabilir, kararını verebilir ve hemen takip edebilir.",
                ],
            },
            {
                "h2": "Bir hizmet gizli hesabın sorun olmadığını söylüyorsa",
                "p": [
                    "Gizli bir hesapta takipçi sayısı ancak istekler onaylanınca artar. Biri, siz kimseyi onaylamadan orada takipçi sözü veriyorsa, onaylamayı hesabınızın içinden kendisi yapmak zorundadır. Bunun için şifrenizi teslim etmek, asla yapmamanız gereken tek şeydir.",
                ],
            },
            {
                "h2": "Kontrolü bırakmadan herkese açılmak",
                "ul": [
                    "Kampanya için herkese açık moda geçin, dilediğiniz zaman tekrar gizliye alın.",
                    "Kendinize saklamak istediğiniz gönderileri arşivleyin; hiçbir şey silinmez.",
                    "Kişisel hikâyelerinizi herkesle değil, Yakın Arkadaşlar listenizle paylaşın.",
                    "Hesabınız açıkken takip eden herkes, tekrar gizliye geçseniz de takipçiniz olarak kalır.",
                ],
            },
        ],
        "faqs": [
            ("Gizli bir Instagram hesabını büyütebilir misiniz?", "Yalnızca çok az, bu yüzden denemiyoruz. İnsanlar takip isteği gönderebilir ama gönderilerinizi göremez, bu yüzden pek azı gönderir. Kampanya sürerken hesabı herkese açık tutun ki işini yapabilsin."),
            ("Tekrar gizliye geçersem takipçi kaybeder miyim?", "Hayır. Sizi zaten takip eden insanlar, gizliye geçtiğinizde de kalır. Yeni ziyaretçilerin istek göndermesi gerekir; bu yüzden hesap gizliyken büyüme yavaşlar."),
            ("Takip isteklerini onaylamam gerekir mi?", "Hesabınız herkese açıkken hayır: insanlar doğrudan takip eder. Ayın ortasında gizliye geçerseniz yeni istekler sizi bekler ve kampanya çok daha az takipçi getirir."),
            ("Hesabımı büyütmek için erişime ihtiyacınız var mı?", "Hayır. Giriş bilgileriniz sizde kalır; yalnızca kullanıcı adınıza ve gönderdiğimiz insanların bakabileceği herkese açık bir profile ihtiyacımız var."),
            ("Gizli hesapta beğeni gelir mi?", "Yalnızca sizi zaten takip edenlerden, çünkü başka kimse gönderileri göremez. Kampanyanın herkese açık bir profile ihtiyaç duymasının bir nedeni daha."),
        ],
    },
    {
        "service": "followers",
        "modifier": "real",
        "slug": "instagram/takipci/gercek",
        "label": "Aktif Instagram takipçi",
        "title": "Aktif Instagram Takipçi Satın Al, Gerçek Etkileşim | Growsterr",
        "description": "Aktif Instagram takipçi; beğenen, yorum yapan ve izleyen insanlardır. Bizimkiler beğeni ve yorumu aynı hesaplardan getirir: genellikle ayda {pick_likes} beğeni.",
        "h1": ("Aktif Instagram takipçi satın alın: ", "gerçekten etkileşime girenler."),
        "intro": "İnsanlar aktif Instagram takipçi satın almak istediğinde, yerinde sayan bir sayıyı değil; beğenen, yorum yapan ve izleyen takipçileri kasteder. Bu yalnızca gerçek insanlarla olur, biz de yalnızca onları getiririz: profilinizi keşfeden, takip etmeyi seçen ve keyif aldığı gönderilere tepki veren insanlar.",
        "hero": {"image": "instagram-real-people", "alt": "Yeni Instagram takipçilerinin bir gönderiyi beğenip yorumlarda sohbet başlatması"},
        "sections": [
            {
                "h2": "Gerçek görünmek ile gerçek olmak",
                "p": [
                    "Bazı takipçiler gerçek görünsün diye üretilir: ödünç alınmış bir fotoğraf, birkaç gönderi, akla yatkın bir isim. Hızlı bir bakışı geçerler, gerisinin hepsinde sınıfta kalırlar. Yeni gönderinizi asla beğenmezler, bir Reels videosunu asla sonuna kadar izlemezler, yorumlarda asla soru sormazlar.",
                    "Önemli olan tek anlamıyla yüksek kalite, bunları yapabilecek bir insan demektir. Profil fotoğrafı ve biyografi süstür; asıl sınav etkileşimdir.",
                ],
            },
            {
                "h2": "Etkileşim takipçilerle birlikte gelir",
                "p": [
                    "Takipçilerimiz insan olduğu için etkileşim de onlarla, aynı hesaplardan gelir. {pick_name} ile tipik bir ay {pick_audience} yeni takipçiyle birlikte {pick_likes} beğeni ve {pick_comments} yorum getirir.",
                ],
            },
            {
                "h2": "Takipçilerin aktif olup olmadığı nasıl anlaşılır?",
                "ul": [
                    "Son birkaç gönderinizde beğenileri takipçilerle karşılaştırın: gerçek büyüme ikisini birlikte hareket ettirir.",
                    "Yorumları okuyun: gerçek olanlar gönderiden bahseder, bot yorumları her gönderinin altına uyar.",
                    "Yeni takipçilerin birkaçının profilini açın: gerçek insanlarınki düzensiz ve kendine özgüdür.",
                    "Toplamı birkaç hafta izleyin: aktif takipçiler dalgalar halinde kaybolmaz.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "Son Instagram gönderilerindeki beğeni ve yorumları karşılaştıran bir içerik üreticisi"},
            },
        ],
        "faqs": [
            ("Bir takipçiyi aktif yapan nedir?", "Gönderilerinizi gören ve zaman zaman tepki veren bir insan olması: bir beğeni, bir yorum, izlenen bir Reels, bir paylaşım. Kimse her gönderiye tepki vermez ve bu normaldir."),
            ("Yeni takipçilerim gönderilerimi beğenecek mi?", "Birçoğu evet. Beğeniler takip eden aynı insanlardan gelir ve {pick_name} ile genellikle ayda {pick_likes} eder. İnsanlar keyif aldığını beğenir, bu yüzden en iyi gönderileriniz en çok beğeniyi toplar."),
            ("Bunlar kaliteli takipçiler mi?", "Onlar, adını verdiğiniz yerden sizi takip etmeye karar veren insanlar. Takipçileri profillerinin ne kadar parlak göründüğüne göre puanlamıyoruz; önemsediğimiz, her birinin arkasında birinin olması."),
            ("Takipçiler gerçek görünüyor mu?", "Gerçekler, bu yüzden sıradan Instagram kullanıcıları gibi görünürler: kendi fotoğrafları, arkadaşları ve alışkanlıklarıyla. Her kitlede olduğu gibi bazı profiller hareketli, bazıları sessizdir."),
            ("Growsterr gerçek bir site mi, yoksa bir bayi mi?", "Biz bir büyüme ajansıyız; Sterr Agency'nin (Sterr Technologies OÜ, Tallinn, Estonya) bir parçasıyız ve her kampanyayı bir ekip yürütür. Profilinize insan getiririz; takipçi stoku satmayız."),
        ],
    },
    {
        "service": "followers",
        "modifier": "safe",
        "slug": "instagram/takipci/guvenilir",
        "label": "Güvenilir Instagram takipçi",
        "title": "Güvenilir Siteden Instagram Takipçi Satın Al | Growsterr",
        "description": "Instagram takipçi için güvenilir bir site mi arıyorsunuz? Kim olduğumuz, ödemenin nasıl alındığı, asla istemediklerimiz ve her hizmette bakılacaklar.",
        "h1": ("Güvenilir bir siteden Instagram takipçi satın alın: ", "nasıl anlaşılır, anlatalım."),
        "intro": "Kendine güvenilir diyen bir siteden Instagram takipçi satın almadan önce, arkasında kimin olduğunu ve neyin ters gidebileceğini sormak hakkınız. İşte bizim tarafımız, açıkça: kim olduğumuz, ödemenin nasıl yapıldığı, hesabınızla ne yaptığımız (hiçbir şey) ve kendimiz dahil her büyüme hizmetinde yapacağımız kontroller.",
        "hero": {"image": "instagram-hub", "alt": "Kaydolmadan önce bir büyüme hizmetinin ayrıntılarını inceleyen bir Instagram içerik üreticisi"},
        "sections": [
            {
                "h2": "Kime ödeme yapıyorsunuz?",
                "p": [
                    "Growsterr, Sterr Agency'nin bir ürünüdür ve Estonya'nın Tallinn kentinde kayıtlı, merkezi Türkiye'de olan Sterr Technologies OÜ tarafından işletilir. Ödemeyi Stripe'ın ödeme sayfasından kartla ya da cihazınız destekliyorsa Apple Pay veya Google Pay ile yaparsınız; kart bilgileriniz bize değil, Stripe'a gider.",
                    "Bu aylık bir aboneliktir. Dilediğiniz zaman kendiniz iptal edebilirsiniz; kampanya, ödenen ay bitene kadar devam eder.",
                ],
            },
            {
                "h2": "Hesabınızla ne yapıyoruz: hiçbir şey",
                "p": [
                    "Asla giriş yapmayız, paylaşım yapmayız, sizin adınıza kimseyi takip etmeyiz ve hiçbir ayara dokunmayız. Kampanya hesabınızın dışında gerçekleşir: insanlar profilinizi iş ortağı ağımızda görür ve birinin önerdiği herhangi bir profili ziyaret eder gibi ziyaret eder.",
                ],
            },
            {
                "h2": "Her büyüme hizmetinde beş kontrol",
                "ul": [
                    "Şifrenizi istiyor mu? Meşru bir hizmetin buna asla ihtiyacı olmaz.",
                    "Dakikalar içinde binlerce takipçi vaat ediyor mu? O hız yalnızca botlardan gelir.",
                    "Rakamlar aralık mı, söz mü? İnsanlar önceden sayılamaz.",
                    "Kimseye yazmadan kendi başınıza iptal edebiliyor musunuz?",
                    "Sitenin arkasında bir şirket adı ve bir ülke var mı?",
                ],
            },
        ],
        "faqs": [
            ("Growsterr güvenilir mi?", "Evet. Kayıtlı bir şirketiz, ödeme yalnızca Stripe üzerinden alınır ve her kampanyayı bir ekip yürütür, panelinizde ölçülür. Hesabınızdan istediğiniz zaman durdurabilirsiniz."),
            ("Instagram hesabım için güvenli mi?", "Instagram adına konuşamayız; dürüst olan kimse bir hesaba nasıl davranılacağına söz veremez. Söyleyebileceğimiz şu: hesapları riske atan şeyleri yapmıyoruz. Giriş yok, bot yok, takipçi patlaması yok."),
            ("Benden ne gerekiyor?", "Instagram kullanıcı adınız, yeni takipçilerinizin nereden olması gerektiği ve herkese açık bir profil. Listenin tamamı bu."),
            ("Gösterdiğiniz rakamlara güvenebilir miyim?", "Tahmin değil, ölçülmüş rakamlar: paneliniz kampanyamızın getirdiği ziyaretleri ve aralarından gelen yeni takipçileri gün gün gösterir. Sipariş vermeden önce söz değil, tipik aralıklar veririz; çünkü insanlar kendi kararını verir."),
            ("İptal ettikten sonra ödeme alınır mı?", "Hayır. İptal, aboneliğin yenilenmesini durdurur. Ödediğiniz ay sizde kalır ve sonrasında hiçbir ödeme alınmaz."),
        ],
    },
    {
        "service": "followers",
        "modifier": "targeted",
        "slug": "instagram/takipci/hedefli",
        "label": "Yerel, hedefli Instagram takipçi",
        "title": "Yerel Instagram Takipçi Satın Al, Konuma Göre | Growsterr",
        "description": "Seçtiğiniz şehir, bölge ya da ülkeden yerel Instagram takipçi satın alın: müşterilerinizin yaşadığı yerde yaşayan gerçek insanlar, ayın her günü.",
        "h1": ("Yerel Instagram takipçi satın alın: ", "adını verdiğiniz yerden."),
        "intro": "Kadıköy'deki bir kafe, dünyanın öbür ucundaki takipçilerden pek bir şey kazanmaz. Yerel Instagram takipçi satın alırken asıl mesele yerdir; ilk sorduğumuz şey de bu: yeni takipçileriniz hangi şehir, bölge ya da ülkeden gelmeli? Türk takipçi istiyorsanız Türkiye, tek bir şehir istiyorsanız o şehir. Sonra kampanyanızı orada yaşayan insanlara yöneltiriz.",
        "hero": {"image": "instagram-followers", "alt": "Yerel bir işletmenin Instagram profiline aynı şehirden gelen yeni takipçiler"},
        "sections": [
            {
                "h2": "Yerel olmak neden toplamdan önemlidir?",
                "p": [
                    "Bir dükkân, stüdyo, restoran ya da insanlarla yüz yüze buluşan bir içerik üreticisi için sizi gerçekten ziyaret edebilecek bir takipçi, edemeyecek birkaç takipçiden değerlidir. Yerel takipçiler kapıdan girebilir, bir arkadaşına anlatabilir ve video çektiğiniz sokağı tanıyabilir.",
                    "Kitlenizi de tutarlı kılar. Takipçilerinizin çoğu aynı yeri ve aynı dili paylaştığında, her gönderiyi daha fazlası anlar.",
                ],
            },
            {
                "h2": "Konum hedefleme nasıl çalışır?",
                "ul": [
                    "Sipariş verirken bir şehir, bir bölge ya da bütün bir ülke belirtirsiniz.",
                    "Profilinizi ayın her günü önce oradaki insanlara gösteririz.",
                    "Oradaki uygun kitle küçükse, takipçilerin bir kısmı alakasız bir yerden değil, yakın çevreden gelebilir.",
                    "Gerisini içeriğiniz yapar: insanlar gönderileriniz onlara hitap ettiğinde takip eder.",
                ],
            },
            {
                "h2": "Hizmet verdiğiniz ülkeden takipçiler",
                "p": [
                    "Hiç paylaşım yapmadığınız bir ülkeden gelen takipçiler, o ülke neresi olursa olsun size yardım etmez. Müşterileriniz Almanya'daysa Almanya'daki insanları ararız; yalnızca İstanbul'daysa bunu söyleyin, oradan başlarız.",
                ],
            },
        ],
        "faqs": [
            ("Yalnızca ülke değil, şehir de seçebilir miyim?", "Evet. Şehir, bölge ya da bütün bir ülke; hepsi olur. Şehir en dar kitleyi verir, bölge ya da ülke ise kampanyaya ulaşabileceği daha çok insan sağlar."),
            ("Yabancı takipçi gelmesini önleyebilir miyim?", "Evet. Takipçilerinizin nereden geleceğini siz seçersiniz, biz de orayı hedefleriz. Hangi ülkeden olursa olsun takipçide bir sorun yok; asıl soru, onların sizin kitleniz olup olmadığı. Müşterileriniz Türkiye'deyse Türkiye'deki insanları ararız."),
            ("Her takipçi benim şehrimden mi olur?", "Profilinizi önce orada gösteririz. Çok benzer kitle çevre bölgede daha büyükse takipçilerin bir kısmı oradan gelebilir; yani bunu şehrinizle sınırlanmış değil, şehrinize yöneltilmiş bir kampanya olarak düşünün."),
            ("Yerel hedefleme için ek ödeme var mı?", "Hayır. Ayda {starter_price} olan {starter_name} dahil her pakette vardır."),
            ("Yaşa ya da ilgi alanına göre hedefleyebilir misiniz?", "Yalnızca konuma göre hedefliyoruz. O konum içinde kimin takip edeceğine içeriğiniz karar verir, çünkü insanlar ilgilerini çeken şeyi takip eder."),
            ("Yerel hedefleme online bir işletmeye uyar mı?", "Evet, kitleniz belirli bir yerde yaşıyorsa: bir dil bölgesi, bir ülke, girmeye hazırlandığınız bir pazar. Alıcılarınız bütün bir ülkeye yayılmışsa ülkeyi belirtin."),
        ],
    },
    {
        "service": "followers",
        "modifier": "viral",
        "slug": "instagram/takipci/viral",
        "label": "Viral olmak için Instagram takipçi",
        "title": "Viral Olmak İçin Instagram Takipçi: Ne İşe Yarar? | Growsterr",
        "description": "Viral olmak için Instagram takipçi satın alınır mı? Kimse viral olmayı vaat edemez. Gerçek takipçiler her gönderiye, onu paylaşacak daha çok insan kazandırır.",
        "h1": ("Viral olmak için Instagram takipçi satın almak mı? ", "Paylaşan insanları büyütün."),
        "intro": "Sayfasında ne yazarsa yazsın, kimse size viral bir gönderi satamaz. Bir gönderiyi yayan şey insanlardır: izlerler, bir arkadaşına gönderirler, kaydederler; Instagram da onu benzer insanlara gösterir. Instagram takipçi satın alma nedeniniz viral olmaksa, işe yarayabilecek kısmı satın alın: bir sonraki gönderinizi ilk görecek daha çok gerçek insan.",
        "hero": {"image": "instagram-followers-1000", "alt": "Popüler bir Reels sonrası sıçrayıp sonra sabit kalan bir içerik üreticisinin takipçi çizgisi"},
        "sections": [
            {
                "h2": "Büyük bir sayı bir gönderiyi neden yaymaz?",
                "p": [
                    "Bir gönderi, onu ilk görenler tepki verdiğinde yol alır. Hiç tepki vermeyen binlerce takipçi, tepki veren birkaç yüz kişiden daha kötü bir başlangıç verir; çünkü Instagram ilk kitlesinin görmezden geldiği bir gönderi görür.",
                ],
            },
            {
                "h2": "Gerçek takipçiler viral bir ana ne katar?",
                "ul": [
                    "Her gönderi için daha çok ilk izleyici: gönderinin yol alıp almayacağına karar veren insanlar.",
                    "Yalnızca insanların verebileceği paylaşımlar ve kaydetmeler.",
                    "Bir gönderi gerçekten yayıldığında takip etmeye değer bir profil; böylece o an geride bir şey bırakır.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Bir içerik üreticisinin Instagram gönderisini mesajlarda arkadaşlarıyla paylaşan insanlar"},
            },
            {
                "h2": "Dürüst ihtimaller",
                "p": [
                    "Gönderilerin çoğu viral olmaz; ne bizimkiler ne de başkasınınkiler. İstikrarlı büyüme, yayılabilecek gönderilerin yayılma ihtimalini artırır, yayılmayanları da paylaşmaya değer kılar. Sunduğumuz takas bu: bir an vaadi yok, her gönderi için daha iyi bir başlangıç noktası var.",
                ],
            },
        ],
        "faqs": [
            ("Gönderimi viral yapabilir misiniz?", "Hayır; bunu yapabileceğini söyleyen herkese karşı da dikkatli olun. Viral olmak gönderiye, zamanlamaya ve binlerce insanın seçimlerine bağlıdır. Bizim yapabileceğimiz, profilinize her gün taze ve gerçek izleyiciler getirmek; bu da her gönderiye daha iyi bir başlangıç verir."),
            ("Viral gönderiler takipçi getirir mi?", "Çoğu zaman, gönderinin arkasındaki profil insanlara kalmak için bir neden veriyorsa. Bu yüzden tek bir gönderiyi değil profili büyütüyoruz: bir şey yayıldığında yeni gelenler aktif bir kitle ve bir içerik birikimiyle karşılaşır."),
            ("Takipçi satın almak algoritmaya yardım eder mi?", "Satın alınan botlar orada aleyhinize çalışır, çünkü her gönderiyi görmezden gelinmiş gibi gösterirler. Tepki veren gerçek takipçiler her gönderinin daha iyi başlamasına yardım eder. İkisi de açıp kapatabileceğiniz bir düğme değildir."),
            ("Yayılabileceğini düşündüğüm bir gönderi için hangi paket uygun?", "{rising_name} ya da {pro_name}. İkisi de daha çok göz görmesi gereken gönderileri belirlemenizi sağlar; böylece inandığınız gönderiyi daha çok gerçek insan görür. {pro_name} buna öncelikli yerleşim ekler."),
            ("Farkı ne kadar sürede görürüm?", "Kampanyanız kısa sürede başlar ve yeni takipçiler ilk günlerden gelir. Bir gönderinin yayılması hiçbir zaman bir takvime bağlı değildir; büyümeniz ise öyledir."),
        ],
    },
    # --- Likes ----------------------------------------------------------------------------
    {
        "service": "likes",
        "slug": "instagram/begeni",
        "label": "Instagram beğeni",
        "title": "Instagram Beğeni Satın Al: Keyif Alan İnsanlardan | Growsterr",
        "description": "Gönderinizi görüp beğenen insanlardan Instagram beğenisi, her aylık paketin içinde: {starter_name} ile genellikle ayda {starter_likes} beğeni.",
        "h1": ("Instagram beğeni satın alın: ", "gönderiden keyif alan insanlardan."),
        "intro": "Gönderilerinize Instagram beğeni satın almak mı istiyorsunuz? Bizde beğeni asla tek başına satılmaz. Her paket profilinize gerçek insanlar gönderir, onlar da keyif aldıkları gönderileri beğenir: {starter_name} genellikle ayda {starter_likes}, {pick_name} {pick_likes} beğeni getirir; yeni takipçiler ve yorumlarla birlikte.",
        "hero": {"image": "instagram-hub", "alt": "Bir Instagram gönderi ızgarasında gerçek insanlardan toplanan beğeniler"},
        "sections": [
            {
                "h2": "Her şey bir beğeniyle başlar",
                "p": [
                    "Instagram'da bir beğeni, çoğu zaman birinin yaptığı birkaç şeyin ilkidir: profilinizi açar, birkaç gönderiye daha bakar, takip eder, ertesi hafta geri gelir. Tek başına satın alınan beğeniler birinci adımda durur; bol beğenili ama çevresinde başka hiçbir şey olmayan bir gönderi de tam olarak öyle okunur.",
                    "Bizimkiler o yolda ilerleyen insanlardan gelir. Bu yüzden tek başlarına değil, takip ve yorumlarla birlikte gelirler.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Bir Instagram gönderisini beğenip ardından içerik üreticisinin profilini açan biri"},
            },
            {
                "h2": "Seçtiğiniz gönderilere beğeni",
                "p": [
                    "{starter_name} ile beğeniler, insanların en çok keyif aldığı yerlere düşer; genellikle en yeni gönderilerinize. {rising_name} ve {pro_name} ise ilginin hangi gönderilere gideceğini seçmenizi sağlar; bir lansman, bir iş birliği ya da görülmesini istediğiniz bir gönderi için kullanışlıdır.",
                ],
            },
            {
                "h2": "2026'da Instagram beğeni nereden satın alınır?",
                "ul": [
                    "Kurulacak bir uygulama ve paylaşılacak bir giriş bilgisi yok: bunlardan birini isteyen site yanlış türde bir erişim istiyordur.",
                    "İzlenme ve takiplerden önce değil, onlarla birlikte gelen beğeniler.",
                    "Kesin sayılar yerine tipik aralıklar, çünkü kararı insanlar verir.",
                    "Adını söyleyebileceğiniz bir şirket ve tanıdığınız bir ödeme sayfası: bizimki Sterr Technologies OÜ, kart ödemelerini Stripe üzerinden alır.",
                ],
            },
        ],
        "faqs": [
            ("Tek bir gönderi için beğeni satın alabilir miyim?", "Tek seferlik bir sipariş olarak hayır. Beğeniler aylık bir paketin içinde, profilinizi keşfeden insanlardan gelir. {rising_name} ya da {pro_name} ile bu ilgiyi seçtiğiniz gönderilere yöneltebilirsiniz."),
            ("Instagram beğenisi için bir uygulama var mı?", "Bizim yok, size de gerekmez. Siparişi sitede verir, Stripe üzerinden ödersiniz ve kampanyanızı herhangi bir cihazdan hesabınızda takip edersiniz. Instagram giriş bilgilerinize asla ihtiyacımız olmaz."),
            ("Her paket kaç beğeni getirir?", "{starter_name} ile genellikle ayda {starter_likes}, {rising_name} ile {rising_likes}, {pro_name} ile {pro_likes}. Sayı değil aralık: her beğeni bir insanın tercihidir."),
            ("Beğeniler ne zaman başlar?", "Kampanyanız çalışmaya başlayıp ilk insanlar profilinize ulaşır ulaşmaz; genellikle ilk günler içinde. Ay boyunca gelmeye devam ederler, asla tek bir patlamayla değil."),
            ("Sayılar gizlenebildiğine göre beğeniler hâlâ önemli mi?", "Instagram beğeni sayılarının gizlenmesine izin veriyor, bu yüzden ekrandaki sayı eskisi kadar önemli değil. Hâlâ önemli olan, insanların gönderilerinizle etkileşime girmesi; gerçek beğenilerin yansıttığı da budur."),
        ],
    },
    {
        "service": "likes",
        "modifier": "comment-likes",
        "slug": "instagram/begeni/yorum-begenisi",
        "label": "Instagram yorum beğenisi",
        "title": "Instagram Yorum Beğenisi Satın Al? İşe Yarayan Bu | Growsterr",
        "description": "Instagram yorum beğenisi satın almak mı istiyorsunuz? Bunu satmıyoruz. Gönderilerinize gelen insanlar sohbeti okur, katıldıkları yanıtları beğenir.",
        "h1": ("Instagram yorum beğenileri ", "sohbeti okuyan insanlardan gelir."),
        "intro": "İnsanlar Instagram yorum beğenisi satın almayı iki nedenle ister: başkasının gönderisindeki bir yorumu yukarı taşımak ya da kendi yorum bölümünü daha hareketli göstermek. İkisini de satmıyoruz. Profilinize gerçek insanlar getiriyoruz; yorumlarınızı okuyanlar da katıldıkları yanıtları kendi istekleriyle beğenebilir.",
        "hero": {"image": "instagram-real-people", "alt": "Bir Instagram gönderisinin altında en iyi yanıtları beğeni alan hareketli bir yorum dizisi"},
        "sections": [
            {
                "h2": "Başkalarının gönderilerindeki yorumlar",
                "p": [
                    "Büyük bir hesabın gönderisinde en üstte duran, çok beğenilmiş bir yorum size ziyaretçi gönderebilir; insanların yorum beğenisi aramasının nedeni bu. Başkalarının gönderilerinde kampanya yürütmüyoruz. Bizim işimiz kendi profilinizde gerçekleşir: onu gerçek insanlara gösteririz, orada ne yapacaklarına onlar karar verir.",
                ],
            },
            {
                "h2": "Kendi gönderilerinizdeki yorum beğenileri",
                "p": [
                    "Kendi gönderilerinizde, bir sohbet başladığında yorum beğenileri kendiliğinden gelir. Kampanyanız aracılığıyla gelen insanlar yorumları okur, bazılarına cevap verir ve katıldıklarını beğenir; sizinkiler de dahil. Bu beğenileri saymıyor, tahmin de etmiyoruz; çünkü bir insanın hangi yanıtı beğeneceğini kimse öngöremez.",
                    "Saydığımız şey şu: {pick_name} ile bir ay genellikle gönderilerinize {pick_likes} beğeni ve {pick_comments} yorum getirir.",
                ],
            },
            {
                "h2": "Yanıtlarınıza daha çok beğeni almanın üç yolu",
                "ul": [
                    "İlk yorumlara hızlı cevap verin, insanlar hâlâ gönderideyken.",
                    "Okumaya değer bir cevap yazın: bir ipucu, bir ayrıntı, karşılık olarak bir soru.",
                    "İstediğiniz sohbeti başlatan bir yorumu sabitleyin.",
                ],
            },
        ],
        "faqs": [
            ("Instagram yorumlarına beğeni satıyor musunuz?", "Hayır. Yorum beğenileri de diğer tüm beğeniler gibi yalnızca onları vermeyi seçen insanlardan gelir. Paketlerimiz bu insanları gönderilerinize getirir; sohbette neyi beğenecekleri onlara kalmıştır."),
            ("Yorumumu başka bir hesabın gönderisinde en üste taşıyabilir misiniz?", "Hayır. Yalnızca kendi profilinizi büyütüyoruz ve başka hiçbir yerdeki yorumlara beğeni göndermiyoruz."),
            ("Yorum bölümüm hareketlenir mi?", "Genellikle evet, çünkü gönderilerinizi daha çok insan görür. {pick_name} ile ayda genellikle {pick_comments} yorum gelir ve yorumlar kendi yanıtlarını ve beğenilerini çekme eğilimindedir."),
            ("Yorum beğenileri paket rakamlarına dahil mi?", "Hayır. Tipik aralıklarımız gönderilerinize gelen beğenileri sayar. Tek tek yorumlara gelen beğeniler, insanlar verdikçe bunun üstüne eklenir."),
            ("Hesabıma giriş yapacak mısınız?", "Hayır. Bizim tarafımızda kimse hesabınıza dokunmaz ve şifreniz sizden hiç çıkmaz. Gönderilerinizde olan her şeyi insanlar kendi hesaplarından yapar."),
        ],
    },
    {
        "service": "likes",
        "modifier": "gradual",
        "slug": "instagram/begeni/kademeli",
        "label": "Yavaş, kademeli Instagram beğeni",
        "title": "Günlere Yayılan Yavaş Instagram Beğeni | Growsterr",
        "description": "Instagram beğeniyi tek bir sıçramayla değil, yavaş yavaş mı almak istiyorsunuz? Bizimkiler ay boyunca gönderilerinizi bulan gerçek insanlardan gelir.",
        "h1": ("Yavaş gelen Instagram beğenisi, ", "çünkü insanlar acele etmez."),
        "intro": "Instagram beğeniyi yavaş yavaş satın almak istiyorsanız, iki dakikada gelen yüzlerce beğeninin yanlış göründüğünü zaten biliyorsunuz. Yavaş doğrudur, ama hız işin yalnızca yarısıdır. Beğenilerimiz kademeli gelir, çünkü bir zamanlayıcıya bağlı bir kuyruktan değil, gönderilerinizi günler ve haftalar içinde bulan gerçek insanlardan gelirler.",
        "hero": {"image": "instagram-followers-1000", "alt": "Bir Instagram gönderisinde birkaç gün boyunca yavaşça biriken beğeniler"},
        "sections": [
            {
                "h2": "Gerçek bir gönderide beğeniler nasıl birikir?",
                "p": [
                    "Bir gönderi beğenileri bir eğri halinde toplar: önce paylaştıktan kısa süre sonra görenlerden bir ilk dalga, ardından profilinizde, bir hashtag'de ya da bir arkadaşın mesajlarında bulundukça uzun bir kuyruk. O kuyruk haftalarca sürebilir.",
                    "Kampanyalarımız o eğrinin her bölümüne insan ekler. Ay boyunca profilinizi ziyaret eder, gönderilerinize göz atar ve keyif aldıklarını beğenirler; yani yalnızca en yeni gönderi değil, eski gönderiler de beğeni kazanır.",
                ],
            },
            {
                "h2": "Zamanlayıcı neden zamanla aynı şey değildir?",
                "p": [
                    "Botlardan yavaş salınan beğeniler yanlış sorunu çözer. Sıçrama ortadan kalkar ama beğenilerin arkasındaki hesaplar yine hiç izlemez, takip etmez, yorum yapmaz; çevresinde izlenme, takip ya da yorum olmayan beğeniler yavaş bir hızda da aynı tuhaf görünür.",
                ],
            },
            {
                "h2": "Yavaş, istediğiniz şey değilse",
                "p": [
                    "Bir saat içinde bir gönderiye duvar dolusu beğeni gerekiyorsa yanlış yerdesiniz ve bunu şimdiden söylemeyi tercih ederiz. Her gönderinizin, önemseyen insanlardan beğeni toplamaya devam etmesini istiyorsanız, tam olarak bunun için varız.",
                ],
            },
        ],
        "faqs": [
            ("Beğeniler ne kadar yavaş gelir?", "İnsanların gönderilerinizi bulduğu hızda: bir kısmı kampanyanızın ilk günlerinde, daha fazlası sonraki haftalarda. Zamanlayıcı da yığın da yok, bu yüzden hiçbir gün birbirine benzemez."),
            ("Beğenilerin hızını seçebilir miyim?", "Hayır, bu bilinçli bir tercih. Hız, profilinizi ziyaret eden insanlardan gelir. {rising_name} ya da {pro_name} ile seçebileceğiniz şey, ilginin hangi gönderilere gideceğidir."),
            ("Eski gönderiler de beğeni alır mı?", "Çoğu zaman evet. Profilinizi keşfeden insanlar geriye doğru kaydırır ve keyif aldığını beğenir; beğeniler tek bir gönderiye yığılmak yerine akışınıza yayılır."),
            ("Yavaş beğeniler daha doğal mı görünür?", "Yavaşlık ancak arkasında insanlar varsa doğal görünür. Bizimkiler öyle görünür, çünkü öyledir: her beğeni, takip edebilecek ya da yorum yapabilecek bir insanla birlikte gelir."),
            ("Bir ayda kaç beğeni gelir?", "{pick_name} ile 30 gün boyunca genellikle {pick_likes}. Bu bir kota değil bir aralık, çünkü insanlar kendi hızında beğenir."),
        ],
    },
    {
        "service": "likes",
        "modifier": "monthly",
        "slug": "instagram/begeni/aylik",
        "label": "Aylık Instagram beğeni",
        "title": "Aylık Otomatik Instagram Beğeni, Tek Abonelik | Growsterr",
        "description": "Instagram beğeniyi gönderi gönderi değil, aylık alın: tek abonelik, gerçek insanlar, ay boyunca beğeni. Kendiliğinden yenilenir, dilediğinizde iptal.",
        "h1": ("Aylık otomatik Instagram beğeni, ", "bir yazılımdan değil, insanlardan."),
        "intro": "Aylık otomatik Instagram beğeni satın almak istiyorsanız, muhtemelen beğenileri her gönderi için ayrı ayrı düşünmekten yoruldunuz. Paket tam da bunu çözer. Bir kez abone olursunuz, kampanyanızı her gün biz yürütürüz ve gerçek insanlar ay boyunca keyif aldıkları gönderileri beğenir: {pick_name} ile genellikle {pick_likes} beğeni. Siz iptal edene kadar her ay yenilenir.",
        "hero": {"image": "instagram-creator-studio", "alt": "Duvar takviminde bir aylık Instagram paylaşımlarını planlayan bir içerik üreticisi"},
        "sections": [
            {
                "h2": "Otomatik, ama otomasyon değil",
                "p": [
                    "Otomatik beğeni genellikle her yeni gönderiyi yakalayıp dakikalar içinde ona belirli sayıda beğeni gönderen bir yazılım demektir. Otomatiktir ve o beğenilerin her biri kimsenin kullanmadığı bir hesaptan gelir.",
                    "Bizimkiler başka bir anlamda otomatiktir: her gönderi için bir şey yapmanız gerekmez. Kampanya çalışmaya devam eder, insanlar profilinizi keşfetmeye devam eder ve bıraktıkları beğeniler kendilerine aittir.",
                ],
            },
            {
                "h2": "Aylık bir paket neyi değiştirir?",
                "ul": [
                    "Her gönderi için bir sipariş yerine ayda tek fiyat: {pick_name} için {pick_price}.",
                    "Ayarlanacak sayı, planlanacak zamanlama yok.",
                    "İnsanlar buldukça hem yeni hem eski gönderilere beğeni.",
                    "Bir aylık beğeni, bir aylık geri bildirimdir: insanların gerçekten hangi gönderilerden keyif aldığını görürsünüz.",
                    "İhbar süresi olmadan, istediğiniz zaman durdurabilirsiniz.",
                ],
            },
        ],
        "faqs": [
            ("Yeni gönderiler otomatik olarak beğeni alır mı?", "Kararı insanlar verir, bu yüzden gönderi başına sabit bir sayı yok. İnsanlar genellikle yeni gönderilerden başlar; {rising_name} ya da {pro_name} ile hangi gönderilerin ilgi göreceğini bize söyleyebilirsiniz."),
            ("Abonelik otomatik olarak yenilenir mi?", "Evet. Stripe onu her ay seçtiğiniz ödeme yöntemiyle yeniler. İptal etmek hesabınızda bir dakikanızı alır ve ödediğiniz ay sonuna kadar devam eder."),
            ("Kaç gönderiye ihtiyacım var?", "Alt sınır yok; ama beğeniler profilinize göz atan insanlardan gelir, bu yüzden birkaç yeni gönderi onlara keyif alacak bir şey sunar. Ay boyunca paylaşım yapmak her yeni ziyaretçiye beğenecek daha çok şey verir."),
            ("Bir aydan diğerine paket değiştirebilir miyim?", "Evet. Bugün size uyan paketle başlayın, gönderileriniz daha çok insana hazır olduğunda bir üst pakete geçin."),
            ("Bu, otomatik beğeni yazılımıyla aynı şey mi?", "Hayır. Her gönderiyi bir zamanlayıcıyla beğenen yazılımlar, arkasında kimse olmayan hesaplar kullanır. Bizim beğenilerimiz profilinizi ziyaret edip bir gönderiden keyif alan insanlardan gelir."),
        ],
    },
    {
        "service": "likes",
        "modifier": "no-drop",
        "slug": "instagram/begeni/dusmeyen",
        "label": "Düşmeyen Instagram beğeni",
        "title": "Düşmeyen Instagram Beğeni: Gönderinizde Kalanlar | Growsterr",
        "description": "Düşmeyen Instagram beğeni mi arıyorsunuz? Beğeniler, arkasındaki hesaplar silinince kaybolur. Bizimkiler gerçek insanlardan gelir; biri geri almadıkça kalır.",
        "h1": ("Düşmeyen Instagram beğenisi: ", "çünkü onu bir insan verdi."),
        "intro": "Beğeniler esas olarak tek bir nedenle kaybolur: onları veren hesaplar silinir. Kalıcı Instagram beğeni satın almak istiyorsanız, kalıcı olanı insanlar verir. Bizimkiler öyledir; gönderinizdeki bir beğeni, onu veren kişi fikrini değiştirmedikçe orada kalır.",
        "hero": {"image": "instagram-hub", "alt": "Paylaşıldıktan haftalar sonra beğenileri sabit kalan bir Instagram gönderisi"},
        "sections": [
            {
                "h2": "Kaybolan beğeniler nereye gider?",
                "p": [
                    "Bir beğeni, onu veren hesaba aittir. Instagram sahte ya da spam hesapları sildiğinde, bıraktıkları her beğeni de onlarla gider; çoğu zaman siparişten haftalar sonra. Bir gönderi bir gecede beğenilerinin büyük bir kısmını kaybedebilir ve daha önce bakan herkes o boşluğu görebilir.",
                ],
            },
            {
                "h2": "İnsanlardan gelen beğeniler neden kalır?",
                "p": [
                    "Bir insanın hesabı bir temizlikte süpürülüp gitmez. Beğenisi, o bıraktığı sürece gönderinizde durur; insanlar keyif aldıkları bir şeyin beğenisini geri almaya nadiren döner.",
                    "Gerçek beğeniler gelmeye de devam eder. Profilinizi daha çok insan buldukça eski gönderiler yeni beğeniler toplar; bir gönderinin sayısı, paylaştıktan çok sonra bile artmaya devam edebilir.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Yeni ziyaretçilerin haftalar önce paylaşılmış bir Instagram gönderisini beğenmesi"},
            },
        ],
        "faqs": [
            ("Beğeniler hiç düşer mi?", "Satın alınan beğenilerin düştüğü gibi değil. Her beğeni bir insanın kendi hesabından gelir; yani biri ancak o kişi beğeniyi geri alırsa ya da hesabını kapatırsa gider. Bu nadirdir ve tek tek olur."),
            ("Telafi süresi var mı?", "Telafi süresi yok, çünkü beklenen bir düşüş yok. Telafi, bizim yaratmadığımız bir sorunu çözer."),
            ("Reels beğenileri de kalır mı?", "Evet. Beğeni, onu veren hesap durduğu sürece her gönderide kalır: fotoğraf, carousel ya da Reels."),
            ("Önceki beğenilerin bottan gelip gelmediğini nasıl anlarım?", "Bir temizlik sonrası ani düşüşlere, izlenmelerin çok üstünde beğenilere ve kendi gönderisi olmayan beğenen profillerine bakın. İnsanlardan gelen beğenilerde bunların hiçbiri pek görülmez."),
            ("Bir paket kaç beğeni getirir?", "{pick_name} genellikle ayda {pick_likes} getirir; insanların keyif aldığı gönderilere yayılır. Kalırlar ve sonraki ayın beğenileri onlara eklenir."),
        ],
    },
    {
        "service": "likes",
        "modifier": "organic",
        "slug": "instagram/begeni/organik",
        "label": "Organik Instagram beğeni",
        "title": "Sizi Bulan İnsanlardan Organik Instagram Beğeni | Growsterr",
        "description": "Organik Instagram beğeni satın alın, dürüst geri bildirim alın: gerçek insanlar gönderilerinizi kampanyalarımızla görür ve yalnızca keyif aldıklarını beğenir.",
        "h1": ("Organik Instagram beğenisi ", "ve size anlattıkları."),
        "intro": "Organik Instagram beğeni satın aldığınızda, satın alınan beğenilerin veremeyeceği bir şey elde edersiniz: dürüst geri bildirim. Kampanyalarımız gönderilerinizi gerçek insanların önüne çıkarır, onlar da yalnızca keyif aldıklarını beğenir. Bazı gönderiler diğerlerinden çok daha fazla toplar; bu fark da kitlenizin ne istediğini anlatır.",
        "hero": {"image": "instagram-real-people", "alt": "Bir dizi Instagram gönderisine farklı tepkiler veren, bazılarını daha çok beğenen insanlar"},
        "sections": [
            {
                "h2": "Dengesiz beğeniler iyiye işarettir",
                "p": [
                    "Satın alınan beğeniler şüphe uyandıracak kadar eşittir: her gönderi, ne olursa olsun, aşağı yukarı aynı sayıyı alır. Organik beğeniler değişir. Güçlü bir Reels öne geçer, sakin bir fotoğraf geride kalır ve ortaya çıkan desen fikirleri olan bir kitleye benzer; çünkü öyledir.",
                ],
            },
            {
                "h2": "Beğenilerinizi daha iyi paylaşım için kullanmak",
                "ul": [
                    "Ayın en iyi üç gönderinizi karşılaştırın: ortak noktaları ne?",
                    "İnsanların en çok hangi biçimi beğendiğine dikkat edin: Reels, carousel ya da fotoğraf.",
                    "İşe yarayandan daha fazla paylaşın, sonra beğenilerin gelip gelmediğine bakın.",
                    "{rising_name} ya da {pro_name} ile yeni bir fikri deneyen bir gönderiye ekstra ilgi yöneltin.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "Geçen ayın Instagram gönderilerini aldıkları beğenilere göre karşılaştıran bir içerik üreticisi"},
            },
            {
                "h2": "Organik beğeniler gönderilerinize nasıl ulaşır?",
                "p": [
                    "Profilinizi iş ortağı ağımızdaki insanlara, seçtiğiniz şehir, bölge ya da ülkede gösteririz. Göz atarlar, isterlerse takip ederler ve dikkatlerini çeken gönderileri beğenirler. Kimseden bir şeyi beğenmesi istenmez.",
                ],
            },
        ],
        "faqs": [
            ("Erişim için ödeme yapmak beğenileri organik olmaktan çıkarır mı?", "Hayır. Görünmek için ödeme yapmak, her reklamın ve öne çıkarılan her gönderinin çalışma şeklidir. Beğeninin kendisi yine birinin gönderinize verdiği kendi tepkisidir."),
            ("Her gönderi beğeni alır mı?", "İnsanların keyif aldığı gönderilerin çoğu alır, ama eşit değil; mesele de bu. En iyi gönderileriniz genellikle en çok beğeniyi toplar."),
            ("Ne kadar organik beğeni bekleyebilirim?", "{pick_name} ile tipik bir ay {pick_likes} getirir. Toplam bir aralıktır; gönderiler arasında nasıl dağılacağı, onları gören insanlara kalmıştır."),
            ("Organik beğeniler takipçiyle birlikte mi gelir?", "Evet. Gönderilerinizi beğenen insanlar çoğu zaman takip de eder: {pick_name} ile genellikle ayda {pick_audience} yeni takipçi; bazıları yorum da bırakır."),
            ("Bu, gönderi başına sabit bir sayıdan neden daha iyi?", "Çünkü sabit bir sayı size hiçbir şey söylemez. Organik beğeniler her gönderiyle inip çıkar; neyin tuttuğunu ve neyin tutmadığını gösterir."),
        ],
    },
    {
        "service": "likes",
        "modifier": "private-account",
        "slug": "instagram/begeni/gizli-hesap",
        "label": "Gizli Instagram hesabına beğeni",
        "title": "Gizli Hesaba Instagram Beğeni Satın Alınır mı? | Growsterr",
        "description": "Gizli hesaba Instagram beğeni satın alınır mı? Gönderileri yalnızca onayladığınız takipçiler görür, bu yüzden yeni kimse beğenemez. İşe yarayan yol ise şu.",
        "h1": ("Gizli Instagram hesabında beğeni ", "yalnızca takipçilerden gelebilir."),
        "intro": "Gizli bir hesap için Instagram beğeni satın almadan önce sınırı bilin: gizli bir profilde gönderilerinizi yalnızca onayladığınız takipçiler görebilir, bu yüzden yalnızca onlar beğenebilir. Bir kampanyanın profilinize getirdiği herkes bir kilitle karşılaşır. Bu yüzden kampanyanız sürerken profilin herkese açık olması gerekir; önemli olan yerlerde gizli kalmanın da iyi yolları var.",
        "hero": {"image": "instagram-hub", "alt": "Yalnızca kabul edilmiş takipçilerin görüp beğenebildiği bir Instagram gönderisi"},
        "sections": [
            {
                "h2": "Gizli bir hesapta bir gönderiyi kim beğenebilir?",
                "p": [
                    "Yalnızca onayladığınız insanlar. Diğer herkes adınızı, biyografinizi ve takipçi sayınızı görür ama tek bir gönderi görmez; yani beğenecek bir şey yoktur. Orada beğeni vaat eden bir hizmetin, hesaplarını önce takipçiniz olarak kabul ettirmesi gerekir: ya sizin tarafınızdan ya da sizin adınıza giriş yapmış biri tarafından.",
                ],
            },
            {
                "h2": "İşleri pratik yoldan gizli tutmak",
                "ul": [
                    "İşiniz için herkese açık ikinci bir hesap açın, kişisel hesabınızı gizli tutun.",
                    "Sayının görünmemesini tercih ediyorsanız herhangi bir gönderide beğeni sayısını gizleyin.",
                    "Sohbet olmadan paylaşmak istediğiniz gönderilerde yorumları kapatın.",
                ],
            },
            {
                "h2": "Profil herkese açılınca ne değişir?",
                "p": [
                    "İnsanlar gönderilerinizi görebilir ve keyif aldıklarını beğenebilir; {pick_name} ile bu, yeni takipçiler ve yorumlarla birlikte bir ayda genellikle {pick_likes} beğeni eder. Ne paylaşacağınıza ve kiminle konuşacağınıza yine siz karar verirsiniz.",
                ],
            },
        ],
        "faqs": [
            ("Beni takip etmeyenler gizli hesaptaki gönderileri beğenebilir mi?", "Hayır. Instagram gizli bir hesabın gönderilerini yalnızca kabul edilmiş takipçilere gösterir, bu yüzden başka kimse onları beğenemez."),
            ("Kampanyadan sonra herkese açık kalmak zorunda mıyım?", "Hayır, bu sizin seçiminiz; gönderilerinizdeki mevcut beğeniler de kalır. Ancak hesap gizliyken yeni insanlar gönderilerinizi göremez, bu yüzden çalışan bir kampanya size beğeni getiremez."),
            ("Bunun yerine ayrı, herkese açık bir hesap büyütebilir miyim?", "Evet. İşiniz için herkese açık bir hesap, arkadaşlarınız için gizli bir hesap iyi işler. Biz herkese açık olanı büyütürüz."),
            ("İstekleri onaylamak için erişime ihtiyacınız olacak mı?", "Hayır. Şifreniz sizde kalır ve hesabınıza asla giriş yapmayız. Herkese açık bir profilde onaylanacak bir şey yoktur: insanlar doğrudan takip eder ve beğenir."),
            ("Beğeni sayılarımı gizleyip yine de büyüyebilir miyim?", "Evet. Sayıyı gizlemek yalnızca ziyaretçilerin o gönderide ne gördüğünü değiştirir. İnsanlar yine beğenebilir, siz de sayıyı yine görürsünüz."),
        ],
    },
    {
        "service": "likes",
        "modifier": "real",
        "slug": "instagram/begeni/gercek",
        "label": "Gerçek Instagram beğeni",
        "title": "Gerçek Instagram Beğeni Satın Al, Bot Yok | Growsterr",
        "description": "Kendi hesabı olan gerçek insanlardan Instagram beğenisi, asla bot değil. Her pakette beğeniler, aynı insanlardan gelen takipçi ve yorumlarla birlikte gelir.",
        "h1": ("Gerçek Instagram beğenisi: ", "her biri içten beğenen bir insandan."),
        "intro": "Gerçek Instagram beğeni satın almak mı istiyorsunuz? Gerçek bir beğeni, gönderinize bakıp gördüğünü beğenen birinden gelir. Getirdiğimiz tek tür bu. Her paket profilinizi insanlara gösterir; bıraktıkları beğeniler aynı hesaplardan gelen takip, yorum ve izlenmelerin yanında durur. Etkileşiminiz gerçekçi görünür, çünkü gerçektir.",
        "hero": {"image": "instagram-real-people", "alt": "Her biri kendi profiline sahip farklı insanların aynı Instagram gönderisini beğenmesi"},
        "sections": [
            {
                "h2": "Premium beğeni, kaliteli beğeni ve gerçek beğeni",
                "p": [
                    "Birçok satıcı beğenileri kademelere ayırır: boş hesaplardan ucuz olanlar, fotoğrafı ve gönderisi olan hesaplardan premium ya da yüksek kaliteli olanlar. İki kademe de farklı kılığa girmiş aynı şeydir: komutla beğenen hesaplar. Daha iyi bir kılık, bir beğeniyi gerçek yapmaz.",
                    "Bir beğeni için kalite tek bir anlama gelir: onu bir insan vermeyi seçti. Gerisi ambalajdır.",
                ],
            },
            {
                "h2": "Beğeninin ötesine geçen gerçek beğeniler",
                "p": [
                    "Gerçek bir beğeni, takip edebilecek, yorum yapabilecek ya da bir sonraki Reels videonuzu izleyebilecek birinden gelir. Bu yüzden gerçek beğeniler diğer rakamlarınızın yanında öylece durmaz, onları da artırır: bir insanın yaptıklarının bir adımıdır, alışverişin tamamı değil.",
                ],
            },
            {
                "h2": "Yalnızca gerçek görünen beğeniler nasıl fark edilir?",
                "ul": [
                    "Beğeniler fırlarken izlenme, takip ve yorumlar yerinde sayar.",
                    "Beğenenlerin profillerinde hazır stok fotoğraflar, az gönderi ve takip edilen binlerce hesap vardır.",
                    "Paylaşımdan sonraki dakikalarda yüzlercesi gelir, sonra hiçbir şey.",
                    "Sayı birkaç hafta sonra düşer.",
                ],
            },
        ],
        "faqs": [
            ("Instagram beğenileriniz gerçek hesaplardan mı?", "Evet. Her beğeni bir insanın kendi hesabından gelir: kampanyamız aracılığıyla profilinizi keşfeden ve gönderiden keyif alan biri. Bot yok, hesap çiftliği yok."),
            ("Premium beğeni satıyor musunuz?", "Beğeniyi ne kademelere ayırarak ne de tek başına satıyoruz. Getirdiğimiz her beğeni, aylık bir paketin içinde bir insandan gelir; en küçük paket olan {starter_name} genellikle ayda {starter_likes} getirir."),
            ("Gerçek beğeniler erişimimi artırır mı?", "Yalnızca gerçek etkileşimin yapabildiği şekilde yardım ederler, çünkü arkalarındaki insanlar takip edebilir, yorum yapabilir ve paylaşabilir. Bir gönderinin nereye varacağı yine gönderinin kendisine bağlıdır; bu yüzden asla erişim sözü vermiyoruz."),
            ("Bazı satın alınmış beğeniler neden gerçek görünür?", "Çünkü öyle görünsün diye yapılırlar: profil fotoğrafları, birkaç gönderi, inandırıcı isimler. Çevrelerinde ne olduğuna bakın. İnsanlardan gelen beğeniler izlenme ve takiple gelir; kılık değiştirmiş olanlar tek başına gelir."),
            ("Yeni takipçi olmadan gerçek beğeni alabilir miyim?", "Hayır. Beğeniler paketin bir parçası olarak, profilinizi bulan insanlardan gelir ve bunların birçoğu takip de eder. Beğenileri gerçekçi tutan da budur."),
        ],
    },
    {
        "service": "likes",
        "modifier": "reels",
        "slug": "instagram/begeni/reels",
        "label": "Instagram Reels beğeni",
        "title": "Instagram Reels Beğeni Satın Al: İzleyenlerden | Growsterr",
        "description": "Instagram Reels beğenisini dürüst yoldan alın: insanlar videolarınızı izler ve keyif aldıklarını beğenir; böylece her beğeninin arkasında bir izlenme olur.",
        "h1": ("Reels videolarınıza beğeni, ", "gerçekten izleyen insanlardan."),
        "intro": "Reels için Instagram beğeni satın almadan önce, kimsenin izlemediği bir Reels'teki beğeninin değerini bilmek işe yarar: pek bir şey değil. Reels beğenilerimiz profilinizi keşfeden, videolarınızı izleyen ve onları tutan videoları beğenen gerçek insanlardan gelir; yeni takipçiler ve yorumlarla birlikte.",
        "hero": {"image": "instagram-creator-studio", "alt": "Masasında telefondan bir Instagram Reels videosu düzenleyen bir içerik üreticisi"},
        "sections": [
            {
                "h2": "Reels'te izlemek beğenmekten önce gelir",
                "p": [
                    "Reels videoları izleyicilerin yaptıklarıyla yaşar: sonuna kadar izliyorlar mı, tekrar izliyorlar mı, paylaşıyorlar mı, takip ediyorlar mı? Beğeni bu sinyallerden biridir ve gerçek bir izlemenin ardından geldiğinde en çok anlam taşır.",
                    "Tek başına satın alınan video beğenileri genellikle onlara denk izlenme olmadan gelir. Beğenisi izlenmesinden fazla olan bir Reels kolayca fark edilir ve o beğenileri nasıl aldığı hakkında iyi bir şey söylemez.",
                ],
            },
            {
                "h2": "Reels videolarınızın daha çok görülmesi",
                "ul": [
                    "İnsanlar profilinize göz atar ve yalnızca en yeniyi değil, dikkatlerini çeken Reels videolarını izler.",
                    "{rising_name} ve {pro_name}, belirli bir Reels'i daha çok insanın önüne çıkarmanızı sağlar.",
                    "İzleyiciler seçtiğiniz yerden gelir; diliniz ve göndermeleriniz yerini bulur.",
                ],
            },
            {
                "h2": "İlk saniyeleri değerlendirin",
                "p": [
                    "İnsanları Reels videolarınıza biz getirebiliriz; onları tutmak videonun işidir. İlk bir iki saniyede net bir kanca, sessiz izleyenler için altyazı ve tekrar izlemeyi cazip kılan bir kapanış; hepsi bir izlenmeyi beğeniye dönüştürmeye yardım eder.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Bir Instagram Reels videosunu sonuna kadar izleyip beğeniye dokunan izleyiciler"},
            },
        ],
        "faqs": [
            ("Beğenileri belirli bir Reels'e yönlendirebilir miyim?", "Evet, {rising_name} ya da {pro_name} ile: hangi gönderilerin ve Reels videolarının ilgi göreceğini siz seçersiniz, gerisini insanlar yapar. {starter_name} ile izleyiciler keyif aldıkları Reels videolarını kendileri bulur."),
            ("Reels beğenileri izlenmeyle birlikte mi gelir?", "Evet. İnsanlar beğenmeden önce izler, yani her beğeninin arkasında bir izlenme vardır. İzlenmeyi ayrıca satmıyor ya da saymıyoruz, çünkü her biri izlemeyi seçen bir insandır."),
            ("Bu, Reels'imi Keşfet'e çıkarır mı?", "Buna kimse söz veremez, biz de vermiyoruz. Keşfet'e ve Reels akışına neyin gireceğine Instagram karar verir. İzleyip tepki veren izleyiciler bir Reels'e adil bir başlangıç verir; izlenmesiz satın alınan beğeniler ise tuhaf bir başlangıç."),
            ("Hesabımın herkese açık olması gerekir mi?", "Evet, kampanyanız sürerken. Takipçileriniz dışındaki insanlar gizli bir hesapta Reels izleyemez, dolayısıyla beğenemez de."),
            ("Reels videolarım kaç beğeni alır?", "{pick_name} ile gönderileriniz ve Reels videolarınız genelinde genellikle ayda {pick_likes} beğeni. Nasıl dağılacağı, insanların en çok neden keyif aldığına bağlıdır."),
        ],
    },
    {
        "service": "likes",
        "modifier": "safe",
        "slug": "instagram/begeni/guvenilir",
        "label": "Güvenilir Instagram beğeni",
        "title": "Güvenilir Instagram Beğeni: Neye Bakmalı? | Growsterr",
        "description": "Güvenilir Instagram beğeni mi arıyorsunuz? Meşru bir beğeni, gönderinizi gören bir insandan gelir. Nasıl anlaşılır ve aylık paketlerimiz bunu nasıl getirir.",
        "h1": ("Güvenilir Instagram beğenisi ", "bir insanla ve bir gönderiyle başlar."),
        "intro": "Güvenilir bir yerden Instagram beğeni satın almak mı istiyorsunuz? Meşru bir beğeninin iki parçası vardır: gerçek bir insan ve onun gerçekten gördüğü bir gönderi. Yaptığımız her şey bu ikisi üzerine kurulu. Profilinizi insanlara gösteririz, gönderilerinizden keyif alanlar da beğenir; giriş bilgisi yok, bot yok, tek başına satılan beğeni yok.",
        "hero": {"image": "instagram-hub", "alt": "Instagram'da gezinirken keyif aldığı bir gönderiyi beğenmek için duran biri"},
        "sections": [
            {
                "h2": "Her beğeni teklifindeki tehlike işaretleri",
                "ul": [
                    "Bin beğeni başına fiyat: insanlar biner biner satın alınamaz.",
                    "Dakikalar içinde teslimat ya da kesin sayı vaadi.",
                    "Şifre talebi ya da bir uygulama üzerinden giriş.",
                    "Yanında izlenme, takip ya da yorum olmadan satılan beğeniler.",
                ],
            },
            {
                "h2": "Sahte beğeniler, kim satarsa satsın neden meşru değildir?",
                "p": [
                    "Instagram'ın kuralları insanlardan yapay yollarla beğeni toplamamalarını ister; komutla beğenen hesaplardan gelen beğeniler de tam olarak budur. Instagram'ın tek bir hesaba nasıl davrandığını söyleyemeyiz ve tahmin de yürütmeyeceğiz. Biz yalnızca hesabınıza yapay hiçbir şey getirmiyoruz.",
                ],
            },
            {
                "h2": "Beğenilerimiz nereden gelir?",
                "p": [
                    "Kampanyalarımızın profilinize getirdiği insanlardan: iş ortağı ağımızdaki kullanıcılar, seçtiğiniz yerde, ayın her günü. Keyif aldıklarını beğenirler; {pick_name} ile genellikle ayda {pick_likes} beğeni. Birçoğu takip eder ve yorum da yapar.",
                ],
            },
        ],
        "faqs": [
            ("Instagram beğeni satın almak meşru mu?", "Komutla beğenen hesaplardan beğeni satın almak, Instagram'ın yapay etkileşim kurallarına aykırıdır. Bizim sattığımız farklı: gerçek insanlara erişim; beğenip beğenmeyeceklerine onlar karar verir."),
            ("Satın alınan beğeniler yüzünden hesabımı kaybedebilir miyim?", "Instagram adına konuşamayız; bir sonuç vaat eden herkes tahmin yürütüyordur. Bizim kontrolümüzde olan şu: getirdiğimiz her beğeni bir insandan gelir ve giriş bilgilerinize asla dokunmayız."),
            ("Nasıl ödeme yaparım?", "Kart, Apple Pay ya da Google Pay ile, Stripe'ın güvenli ödeme sayfası üzerinden. Faturalandırma aylıktır ve iptal ettiğiniz an durur."),
            ("Instagram giriş bilgilerimi istiyor musunuz?", "Asla. Kampanyayı başlatmak için kullanıcı adınız yeterli. Bir beğeni hizmeti şifrenizi isterse oradan uzaklaşın."),
            ("Neden gönderi başına beğeni satmıyorsunuz?", "Çünkü belirli bir gönderiye belirli sayıda beğeni ancak komutla beğenen hesaplardan gelebilir. Biz bunun yerine insan getiririz; beğeni, bir gönderiden keyif aldıklarında yaptıkları şeydir."),
        ],
    },
    {
        "service": "likes",
        "modifier": "viral",
        "slug": "instagram/begeni/viral",
        "label": "Viral olmak için Instagram beğeni",
        "title": "Instagram Beğenisi Gönderiyi Viral Yapar mı? | Growsterr",
        "description": "Viral olmak için Instagram beğeni mi alacaksınız? Gönderiyi beğeniler değil; izleyen, paylaşan, kaydeden insanlar yayar. Gerçek beğeni neyi yapar, neyi yapamaz.",
        "h1": ("Viral Instagram beğenisi ", "bir sonuçtur, başlangıç düdüğü değil."),
        "intro": "İnsanlar bir gönderi viral olsun diye sık sık Instagram beğeni satın alır; büyük bir sayının Instagram'ı ve herkesi, gönderinin daha fazla ilgiyi hak ettiğine ikna edeceğini umarlar. Nadiren böyle işler. Gönderiyi izleyip keyif alan insanlardan gelen beğeniler bir ivmenin işaretidir; sessiz bir gönderiye yığılan beğeniler hiçbir şeyin. Biz birincisini getiririz ve viral kısmı için söz vermeyiz.",
        "hero": {"image": "instagram-followers-1000", "alt": "Yayılmaya başlayan bir Instagram gönderisinde birlikte yükselen beğeni, paylaşım ve kaydetmeler"},
        "sections": [
            {
                "h2": "Beğeniler yayılmadan sonra gelir, önce değil",
                "p": [
                    "Bir gönderi yayıldığında beğeniler, onu izleyen, arkadaşlarına gönderen ve sonra bakmak için kaydeden binlerce insanın görünür izidir. O izi insanlar olmadan kopyalarsanız, hareket olmadan bir sayı elde edersiniz.",
                ],
            },
            {
                "h2": "Bir gönderiye gerçekten şans veren nedir?",
                "ul": [
                    "Tepki veren bir ilk kitle: gönderiyi erken görüp beğenen, yorum yapan ya da paylaşan insanlar.",
                    "İnsanları durduran bir kanca ve gönderiyi birine göndermek için bir neden.",
                    "Kitlenizin olduğu yerde, onların dilinde, akışta gezindikleri saatte paylaşım yapmak.",
                    "Odak: {rising_name} ya da {pro_name} ile yol alabileceğini düşündüğünüz gönderiyi daha çok insan görür.",
                ],
            },
            {
                "h2": "Neye söz veriyoruz, neye vermiyoruz?",
                "p": [
                    "Her gün gerçek insanlar ve ölçtüklerimizi gösteren bir panel sözü veriyoruz. Milyonlarca izlenme, Keşfet'te bir yer ya da yayılan bir gönderi sözü vermiyoruz. Bunu vaat eden herkes, viral bir gönderinin görüntüsünü satıyordur.",
                ],
            },
        ],
        "faqs": [
            ("Beğeni satın almak gönderimi viral yapar mı?", "Tek başına hayır. Beğeni sayısı insanların ilgisinin sonucudur; satın alınan beğeniler ilgi olmadan sayıyı ekler. İzlemiş insanlardan gelen beğeniler bir gönderiye dürüst bir başlangıç verir; kimsenin sunabileceği en fazla şey de budur."),
            ("Viral bir gönderinin kaç beğeniye ihtiyacı vardır?", "Sihirli bir sayı yok. Mütevazı sayıdaki bir gönderi, görenler paylaşırsa yol alabilir; büyük sayıdaki bir gönderi de tıkanıp kalabilir."),
            ("Paylaştıktan sonraki ilk saatte beğeni gönderiyor musunuz?", "Beğenileri bir gönderiye göre zamanlamıyoruz. İnsanlar ay boyunca gelir ve keyif aldıklarını beğenir. Bir gönderi daha önemliyse {rising_name} ve {pro_name}, hangi gönderilerin ilgi göreceğini seçmenizi sağlar."),
            ("Paylaşım ve kaydetmeler dahil mi?", "Onları saymıyor ya da satmıyoruz ama olurlar: gönderilerinizi beğenen insanlar onları paylaşabilir ve kaydedebilir de; botların asla yapmadığı bir şey."),
            ("Yüksek bir beğeni sayısı başkalarının da beğenme ihtimalini artırır mı?", "İnsanlar hareketli bir gönderiyi fark eder. Ama yorumu ya da paylaşımı olmayan büyük bir sayı, etkilemek istediğiniz insanlara tam olarak sahnelenmiş görünür."),
        ],
    },
]
