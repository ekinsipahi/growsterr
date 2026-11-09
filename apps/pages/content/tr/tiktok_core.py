"""Turkish TikTok pages: followers, views and comments, and the ways people ask for them (real,
organic, gradual, monthly, no-drop, safe, private accounts, LIVE, the For You page...). Mirrors
en/tiktok_core.py; the hub and likes live in tiktok.py. Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-09"

PAGES = [
    # --- Followers ------------------------------------------------------------------------
    {
        "service": "followers",
        "slug": "tiktok/takipci",
        "label": "TikTok takipçi",
        "title": "TikTok Takipçi Satın Al: Gerçek İnsanlar, Aylık | Growsterr",
        "description": "TikTok takipçiyi dürüst yoldan satın alın: gerçek insanlar videolarınızı keşfeder ve takip etmeyi seçer, her gün birkaç tane. Başlangıç: ayda {from_price}.",
        "h1": ("TikTok takipçi satın alın, ", "her birinin arkasında gerçek bir insan olsun."),
        "intro": "Hesabınızı botlarla doldurmadan TikTok takipçi satın almak mı istiyorsunuz? Aylık paketlerimiz profilinizi her gün yeni insanlara ulaştırır; tarzınızı beğenen izleyiciler de takip eder. {starter_name} ile bu genellikle ayda {starter_audience} yeni takipçi demek; büyük paketler daha fazlasını getirir.",
        "hero": {"image": "tiktok-creator", "alt": "Gerçek insanlardan takipler gelirken yeni bir video çeken bir TikTok içerik üreticisi"},
        "sections": [
            {
                "h2": "Gerçekte neye ödeme yapıyorsunuz?",
                "p": [
                    "Bizden TikTok takipçi satın aldığınızda bir sayıya değil, bir kampanyaya ödeme yaparsınız. İş ortağı ağımızdaki tanıtım kampanyalarıyla profiliniz ayın her günü gerçek insanlara ulaşır. Birinin takip edip etmeyeceği ona kalmıştır; takibi değerli kılan da bu seçimdir.",
                    "TikTok'ta bir takipçinin değeri, sonra ne yaptığındadır: yeni videonuzu izler, sonuna kadar kalır, beğenir, bir arkadaşına gönderir. İnsanlar bunların hepsini yapar. Bir sayıyı şişirmek için açılmış bir hesap hiçbirini yapmaz.",
                ],
            },
            {
                "h2": "TikTok takipçi satın alacağınız siteyi nasıl seçersiniz?",
                "p": ["Hangi siteye ya da uygulamaya bakıyor olursanız olun, birkaç soru gerçek hizmetleri bot dükkânlarından hızla ayırır."],
                "ul": [
                    "Şifrenizi ya da TikTok ile giriş yapmanızı istiyor mu? Bir takipçi hizmetinin ikisine de asla ihtiyacı olmaz.",
                    "Dakikalar içinde binlerce takipçiden söz ediyor mu? O kadar hızlı yalnızca botlar gelir.",
                    "Ölçtüklerini gün gün mü gösteriyor, yoksa sonda yalnızca bir sayı mı?",
                    "Aboneliği kendiniz durdurabiliyor musunuz, yoksa e-posta atıp beklemeniz mi gerekiyor?",
                    "Beğeni ve yorumlar ek olarak mı satılıyor, yoksa takipçilerin kendisinden mi geliyor?",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Bir içerik üreticisinin son videolarını telefonlarından izleyen yeni TikTok takipçileri"},
            },
            {
                "h2": "Önce takipçiler, sonra getirdikleri her şey",
                "p": [
                    "Yeni takipçiler paylaştıklarınızı Takip Edilenler akışında görür; izlemeleri, beğenmeleri ve paylaşmaları, TikTok'un bir videodan başka kimlerin keyif alabileceğini anlamasına yardım eder. Bot takipçiler o ilk kitleyi sessiz bırakır, bu yüzden her yeni video daha zayıf bir konumdan başlar.",
                ],
            },
        ],
        "faqs": [
            ("Growsterr ile nasıl TikTok takipçi alırım?", "Bir paket seçin, TikTok kullanıcı adınızı verin, yeni kitlenizin nerede yaşaması gerektiğini söyleyin ve Stripe üzerinden kartla ödeyin. Kampanyanız başlar ve yeni takipçiler gelmeye başlar, her gün birkaç tane."),
            ("Abonelik olmadan tek seferlik TikTok takipçi satın alabilir miyim?", "Hayır. Tek seferlik paket satmıyoruz. Gerçek insanlar tek bir teslimatta değil haftalar içinde gelir, bu yüzden büyüme aylık bir paket olarak yürür. İstediğiniz zaman iptal edebilir, ödediğiniz ayı sonuna kadar kullanabilirsiniz."),
            ("Bir uygulama yüklemem gerekiyor mu?", "Hayır. Siparişi bu sitede verir, kampanyanızı herhangi bir tarayıcıda Growsterr hesabınızdan takip edersiniz. Yabancıları takip etmeniz karşılığında takipçi dağıtan uygulamalara karşı dikkatli olun: o takipler, takas biter bitmez kaybolma eğilimindedir."),
            ("TikTok takipçi satın almak beni viral yapar mı?", "Buna kimse söz veremez. Gerçek takipçiler her yeni videoya, onu sonuna kadar izleyip başkasına iletebilecek daha çok insan kazandırır; bu da şansını artırır. Videonun yayılıp yayılmayacağı yine videoya bağlıdır."),
            ("Takipçiler takip ettikten sonra ne yapar?", "Gerçek insanların hep yaptığını: bazıları her videoyu izler, bazıları beğenir ve yorum yapar, birkaçı da zamanla uzaklaşır. {pick_name} bir ay boyunca aynı insanlardan genellikle {pick_likes} beğeni ve {pick_comments} yorum getirir."),
            ("2026'da TikTok takipçi satın almak hâlâ mantıklı mı?", "Bot satın almak mantıklı değil: TikTok sahte hesapları silmeye devam ediyor, sayı küçülürken erişiminize verilen zarar kalıyor. Gerçek insanların profilinizi keşfetmesi için ödeme yapmak ise farklı bir şey; çünkü onlar kendi emeğinizle kazanacağınız kitle gibi davranır."),
        ],
    },
    {
        "service": "followers",
        "modifier": "real",
        "slug": "tiktok/takipci/gercek",
        "label": "Gerçek TikTok takipçi",
        "title": "Gerçek TikTok Takipçi Satın Al, Etkileşimli | Growsterr",
        "description": "Gerçek TikTok takipçi satın alın: videolarınızı bulup takip etmeyi seçen, beğenen ve yorum yapan aktif insanlar. Aylık paketler, başlangıç: ayda {from_price}.",
        "h1": ("Gerçek TikTok takipçi satın alın: ", "aktif, gerçek ve kendi isteğiyle."),
        "intro": "Bizden gerçek TikTok takipçi satın aldığınızda her biri bir insandır: kampanyamız sayesinde profilinizi gören, birkaç video izleyen ve takip etmeye karar veren biri. Gerçek insanlar nasıl aktifse öyle aktiftirler: bir şey hoşlarına gittiğinde beğenir ve yorum yaparlar, bir video onlara göre değilse sessiz kalırlar.",
        "hero": {"image": "tiktok-likes", "alt": "Bir TikTok profilinde gerçek insanlardan biriken kalpler ve yeni takipler"},
        "sections": [
            {
                "h2": "Bir TikTok takipçisini gerçek yapan nedir?",
                "ul": [
                    "Hesabın arkasında kendi videoları, beğenileri ve geçmişi olan bir insan.",
                    "Takip etmek için bir neden: önce videolarınızı izlediler.",
                    "Kendi seçimleri: kimse onlara ödeme yapmadı, kimse karşılığında takip beklemiyor.",
                    "İnsan hızı: takip etmeye değer bir şeyi keşfeden herkes gibi birkaç birkaç gelirler.",
                ],
            },
            {
                "h2": "Aktif takipçinin dürüst tanımı",
                "p": [
                    "Kimse bir insanı aktif yapamaz. Bir hizmet binlerce aktif takipçi satıyorsa, bir programa göre beğenen hesapları anlatıyordur. Gerçek insanlar bir şey dikkatlerini çektiğinde etkileşime girer; bu daha az öngörülebilir ve çok daha değerlidir.",
                    "{pick_name} ile gelen insanlar bir ay boyunca genellikle {pick_likes} beğeni ve {pick_comments} yorum bırakır. {pick_audience} yeni takipçiden gelen gerçek etkileşim çoğunlukla böyle görünür.",
                ],
            },
            {
                "h2": "Yüksek kalite, iyi bir uyum demektir",
                "p": [
                    "Yüksek kaliteli takipçi, bir sonraki videonuzu izleyebilecek takipçidir. Bu da uyuma bağlıdır: nerede yaşadıkları, hangi dili konuştukları, neyi izlemeyi sevdikleri. Yeri siz seçersiniz, gerisini videolarınız ayıklar; çünkü insanlar yalnızca kendilerine hitap edeni takip eder.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Çekimler arasında yeni TikTok takipçilerinin yorumlarını okuyan bir içerik üreticisi"},
            },
        ],
        "faqs": [
            ("Takipçilerin gerçek olduğunu nasıl anlarım?", "Onlara bakın. Yeni takipçilerden birkaçına dokunun; kendi videoları ve beğenileri olan profiller göreceksiniz. İzlenme ve beğenilerinizi de izleyin, çünkü gerçek takipçiler onları hareket ettirir. Paneliniz kampanyamızın her gün getirdiği ziyaretleri ve takipleri gösterir."),
            ("Her takipçi beğenip yorum yapacak mı?", "Hayır, bu normal. Bazı insanlar neredeyse her şeye tepki verir, bazıları çoğunlukla izler. Beğeni ve yorum için verdiğimiz tipik aylık aralıklar, bir senaryodan değil gerçek kitlelerin yaptıklarından gelir."),
            ("Gerçek takipçiler bottan daha mı pahalı?", "Evet, çünkü gerçek bir insana ulaşmanın bir maliyeti var. {starter_name} ayda {starter_price} ve genellikle {starter_audience} yeni takipçi getirir. Botlar en basit nedenle daha ucuzdur: orada kimse yoktur."),
            ("Gerçek takipçiler nereden gelir?", "Kampanyayı nereye yöneltirseniz oradan: tek bir şehir, daha geniş bir bölge ya da bütün bir ülke. Profilinizi tanıtım kampanyalarımız aracılığıyla keşfederler, sonra herkes gibi TikTok'ta takip ederler."),
            ("Yepyeni bir hesap için gerçek takipçi satın alabilir miyim?", "Evet, ama önce birkaç video paylaşın. İnsanlar profilinizde bulduklarına göre karar verir; boş bir profil onlara takip edecek hiçbir şey sunmaz."),
        ],
    },
    {
        "service": "followers",
        "modifier": "organic",
        "slug": "tiktok/takipci/organik",
        "label": "Organik TikTok takipçi",
        "title": "Organik TikTok Takipçi Satın Al, Konum Hedefli | Growsterr",
        "description": "Organik TikTok takipçiyi şeffaf yoldan alın: profilinizi seçtiğiniz yerde gerçek insanlara göstermek için ödeme yaparız, takip etmek tamamen onların kararıdır.",
        "h1": ("Organik TikTok takipçi satın alın: ", "erişim ücretli, karar onların."),
        "intro": "Organik TikTok takipçi satın alınabilir mi? Tam olarak ne yaptığımızı anlatalım. İş ortağı ağımız üzerinden, profilinizi seçtiğiniz bir yerdeki gerçek insanlara ulaştıran tanıtım kampanyalarına ödeme yaparız. Sonrasındaki her şey organiktir: insanlar izler, kararını verir ve daha fazlasını isterse takip eder.",
        "hero": {"image": "tiktok-creator", "alt": "Kendi şehrindeki izleyiciler için TikTok videosu çeken yerel bir içerik üreticisi"},
        "sections": [
            {
                "h2": "Neyin bedeli ödenir, neyin ödenmez?",
                "p": [
                    "Görünürlüğün bedeli ödenir. Kararın ödenmez. Kimse sizi takip ettiği için ödüllendirilmez, kimse bir takasın parçası olarak takip etmez ve hiçbir hesap bir yazılımla takip etmez. Organik takipçiyle satın alınmış takipçi arasındaki çizgi budur.",
                    "Pratikte, bir içerik üreticisinin kendi profilini tanıtmasına çok benzer; farkı, kampanyayı bir ekibin yürütmesi ve ölçülenleri bir panelin göstermesidir.",
                ],
            },
            {
                "h2": "Konuma göre hedefli TikTok takipçi",
                "p": [
                    "Hedefleme konuma göredir. Tek bir şehir, bir bölge ya da bütün bir ülke belirtin; profiliniz önce orada gösterilir. Bursa'daki bir fırın Bursa'daki insanları ister; bir dil öğretmeni ise öğrencilerin yaşadığı ülkeleri. En iyi eşleşen insanlar daha geniş bir alana yayılmışsa, takipçilerin bir kısmı çevre bölgeden gelebilir.",
                ],
            },
            {
                "h2": "Her gün gerçek TikTok takipçileri",
                "ul": [
                    "Ayın her günü birkaç yeni insan profilinizi bulur.",
                    "Her biri videolarınız aracılığıyla gelir, yani neyi takip ettiğini bilir.",
                    "Paneliniz her günün ziyaretlerini ve takiplerini listeler; olanları kendiniz izleyebilirsiniz.",
                ],
            },
        ],
        "faqs": [
            ("Kampanyaya ödeme yapıyorsanız bu organik mi?", "Siz erişimin bedelini ödersiniz. Takibin kendisi organiktir: insanlar profilinizi görür, ilgilerini çekeni izler ve kendi başlarına karar verir; kimse takip ettiği için bir şey almaz. Bir takibi organik yapan budur."),
            ("Bunun takibe takipten farkı ne?", "Takibe takip bir takastır: insanlar karşılığında bir şey almak için sizi takip eder ve birçoğu onu aldıktan sonra takibi bırakır. Kampanyamız kimseden bir şey istemez. İnsanlar daha fazlasını görmek istedikleri için takip eder."),
            ("Konum dışında neyi hedefleyebilirim?", "Bir konum seçersiniz; tek bir şehirden bütün bir ülkeye kadar. Onun içinde ayıklamayı videolarınız yapar. Durup takip edenler, içeriğinizin hitap ettiği insanlardır; hiçbir ayar onları bu kadar iyi seçemez."),
            ("Organik takipçiler videolarımla etkileşime girer mi?", "Birçoğu, kendi bildiği gibi girer: {pick_name} ile bir ay boyunca takip eden insanlar genellikle toplamda {pick_likes} beğeni ve {pick_comments} yorum bırakır."),
            ("Organik takipçiler ne kadar hızlı gelir?", "Kampanyanızın ilk günlerinden ayın sonuna kadar her gün biraz. Organik hiçbir zaman hepsi birden demek değildir."),
        ],
    },
    {
        "service": "followers",
        "modifier": "monthly",
        "slug": "tiktok/takipci/aylik",
        "label": "Aylık TikTok takipçi",
        "title": "Aylık TikTok Takipçi Satın Al: Büyüme Aboneliği | Growsterr",
        "description": "TikTok takipçiyi aylık satın alın: her gün gerçek insanlar getiren bir abonelik. Stripe üzerinden kartla ödenir, her ay yenilenir, dilediğinizde iptal edilir.",
        "h1": ("Aylık TikTok takipçi satın alın. ", "Kendiliğinden yenilenen büyüme."),
        "intro": "TikTok takipçiyi aylık satın almak, tam olarak bizim çalışma şeklimiz. Bir paket seçersiniz, 30 gün sürer ve siz durdurana kadar yenilenir. Her ayın her günü yeni insanlar profilinize denk gelir; videolarınızdan daha fazlasını isteyenler de takip eder.",
        "hero": {"image": "tiktok-likes", "alt": "Gerçek insanlarla aydan aya yükselen bir TikTok takipçi sayısı"},
        "sections": [
            {
                "h2": "Büyüme neden aylık satılır?",
                "p": [
                    "Gerçek insanlar sipariş üzerine gelmez. Bir profile denk gelir, birkaç video izler ve karar verirler; bu da günler sürer. Bu yüzden tek seferlik bir takipçi paketi ancak bot olabilir. Gerçek büyüme için doğal birim aydır: insanların sizi bulmasına yetecek kadar uzun, yön değiştirmeye yetecek kadar kısa.",
                    "Her ay bir öncekinin üzerine de kurulur. İlk ayınızın takipçileri yeni videolarınızı görür; onları paylaşanlar da profilinizi hiç göstermediğimiz insanları getirebilir.",
                ],
            },
            {
                "h2": "Aylık ödeme nasıl işler?",
                "ul": [
                    "Stripe üzerinden kartla ödersiniz; destekleyen cihazlarda Apple Pay ve Google Pay de olur.",
                    "Hesabınız bir sonraki yenileme tarihini gösterir.",
                    "Hesabınızdan iptal etmek bir sonraki ödemeyi durdurur; ödenen ay sonuna kadar sürer.",
                    "Yalnızca seçtiğiniz paket için ödeme alınır, üstüne hiçbir şey eklenmez.",
                ],
            },
            {
                "h2": "İkinci ay ve sonrası",
                "p": [
                    "İlk ay kampanyayı yola koyar. İkinci ve üçüncü aya geldiğinizde panelinizde okuyabileceğiniz bir desen oluşur: hangi haftalar daha çok ziyaret getirdi, hangi videolar ziyaretçileri takipçiye dönüştürdü. Devam etmeye, bir üst pakete geçmeye ya da durmaya karar vermek en kolay o zaman olur.",
                ],
            },
        ],
        "faqs": [
            ("Her ay yeniden sipariş vermem gerekiyor mu?", "Hayır. Paketiniz tarihinde yenilenir ve kampanya ara vermeden sürer. Yalnızca değiştirmek ya da iptal etmek isterseniz bir şey yapmanız gerekir."),
            ("En az kaç ay kalmam gerekir?", "Alt sınır yok. İlk aydan sonra iptal edebilir ya da işinize yaradığı sürece devam edebilirsiniz. İptal bir sonraki ödemeyi durdurur, ödediğiniz ay da son gününe kadar sürer."),
            ("Her ay aynı sayıda takipçi mi gelir?", "Tam olarak değil. Her paketin tipik bir aralığı var, örneğin {pick_name} ile ayda {pick_audience}; gerçek insanlar da her ayı biraz farklı kılar."),
            ("Panelim her ay neyi gösterir?", "Kampanyanızdan gelen günlük profil ziyaretlerini, bunların getirdiği yeni takipçileri ve takipçi sayınızın şu an nerede olduğunu. Aydan aya, paketin ne yaptığının kaydıdır."),
            ("Aylık plan için hangi ödeme yöntemleri geçerli?", "Stripe üzerinden kart; destekleyen telefon ve tarayıcılarda Apple Pay ya da Google Pay. Bir abonelik her ay yenilenebilen bir yöntem ister; havale gibi tek seferlik seçenekleri bu yüzden almıyoruz."),
        ],
    },
    {
        "service": "followers",
        "modifier": "gradual",
        "slug": "tiktok/takipci/kademeli",
        "label": "Kademeli TikTok takipçi",
        "title": "TikTok Takipçi Satın Al, Her Gün Kademeli | Growsterr",
        "description": "TikTok takipçiyi kademeli satın alın: gerçek insanlar profilinizi keşfeder, 30 gün boyunca her gün birkaç kişi takip eder. Zamanlayıcı yok, yalnızca insan hızı.",
        "h1": ("Kademeli TikTok takipçi satın alın, ", "insanların gerçekten takip ettiği hızda."),
        "intro": "TikTok takipçiyi tek bir şüpheli sıçramayla değil de kademeli satın almak istiyorsanız, aylık paket doğası gereği böyle işler. Her gün gerçek insanlar profilinize denk gelir ve beğenenler takip eder. Hiçbir şey bekletilmez ya da bir zamanlayıcıyla salınmaz: yavaş, günlük bir hız, insanların davranış biçimidir.",
        "hero": {"image": "tiktok-likes", "alt": "Her gün birkaç gerçek insanla hafifçe yükselen bir TikTok takipçi çizgisi"},
        "sections": [
            {
                "h2": "Damla damla gönderim ile gerçek günlük hız",
                "p": [
                    "Birçok hizmet damla damla gönderim sunar: aynı botlar, sıçrama daha küçük görünsün diye küçük partiler halinde salınır. Takipçiler yine hiç izlemeyen hesaplardır. Onları zamana yaymak yalnızca teslimatı bir süreliğine gizler.",
                    "Bizim günlük hızımız bir ayar değil. O gün profilinizi gören ve tek tek karar veren insanlardan gelir.",
                ],
            },
            {
                "h2": "Kademeli büyüme profilinizde nasıl görünür?",
                "ul": [
                    "Takipçi sayınız çoğu gün biraz artar; sakin günler de olur, yoğun günler de.",
                    "İzlenme ve beğeniler de onunla birlikte yükselir, çünkü izleyen aynı insanlardır.",
                    "Paneliniz her günün profil ziyaretlerini ve yeni takipçilerini gösterir; eğimi kendiniz görürsünüz.",
                ],
            },
            {
                "h2": "Kalıcı büyüme neden yavaştır?",
                "p": [
                    "İstikrarlı büyüyen hesaplar kazandıkları kitleyi genellikle tutar. Her yeni takipçi beğendiği bir video yüzünden gelir; böylece bir sonraki videonuzu bekleyen biri zaten vardır.",
                ],
                "image": {"image": "tiktok-creator", "alt": "İstikrarlı bir kitle oluşurken günlük TikTok videosunu paylaşan bir içerik üreticisi"},
            },
        ],
        "faqs": [
            ("Tek bir gün kaç yeni takipçi getirir?", "Değişir. Bütün bir ay boyunca {pick_name} genellikle {pick_audience} yeni takipçi ekler; profilinizi kimin gördüğüne ve son zamanlarda ne paylaştığınıza göre bazı günler daha fazla, bazıları daha az getirir."),
            ("Teslimat hızını ayarlayabilir miyim?", "Hayır, çünkü yavaşlatılacak bir teslimat yok. İnsanlar istediklerinde takip eder. Sizin seçtiğiniz şey pakettir; onunla birlikte de profilinizi her ay kaç kişinin göreceği."),
            ("Yavaş teslimat hesabım için daha mı güvenli?", "Hız işin yalnızca bir parçası. Yavaş yavaş gelen botlar da yine bottur. Bir hesabı sağlıklı tutan, her takipçinin takip etmeyi seçmiş bir insan olmasıdır; biz yalnızca böylelerini getiririz."),
            ("İlk takipçiler ne zaman gelir?", "Sipariş verdikten sonra kampanyanız başlar ve ilk profil ziyaretleri genellikle ilk günlerde görünür. Takipçiler bu ziyaretlerden, birbiri ardına gelir."),
            ("Kademeli büyüme 30 gün sonra durur mu?", "Her paket 30 gün sürer ve her ay yenilenir; yani günlük hız, siz iptal edene kadar bir sonraki aya devam eder."),
        ],
    },
    {
        "service": "followers",
        "modifier": "no-drop",
        "slug": "tiktok/takipci/dusmeyen",
        "label": "Düşmeyen TikTok takipçi",
        "title": "Düşmeyen TikTok Takipçi: Gerçekler Neden Kalır? | Growsterr",
        "description": "Bot temizliklerinde düşmeyen TikTok takipçi satın alın: sizi takip etmeyi seçen gerçek insanlar temizliklerde kaybolmaz. Ne kalır, ne kalmaz ve neden.",
        "h1": ("Düşmeyen TikTok takipçi satın alın. ", "Gerçekten isteyen insanlarla başlayın."),
        "intro": "Düşmeyen TikTok takipçi satın almak isteyenler genellikle bir sayının küçülmesini izlemekten bıkmıştır. Bu, takipçiler bot olduğunda ve TikTok onları temizlediğinde olur. Bizim takipçilerimiz takip etmeyi seçen gerçek insanlardır, yani bir temizliğin silebileceği bir şey yoktur. Her gerçek kitlenin değiştiği gibi, birkaçı ileride takibi bırakabilir.",
        "hero": {"image": "tiktok-likes", "alt": "Bir aylık gerçek büyümenin ardından sabit kalan bir TikTok takipçi sayısı"},
        "sections": [
            {
                "h2": "Düşüşler nereden gelir?",
                "p": [
                    "Ani düşüşlerin genellikle tek bir nedeni vardır: sahte hesapların silinmesi. TikTok onları düzenli olarak siler ve tuttukları her takip de onlarla birlikte kaybolur. Sonra hizmetler telafi sunar; bu da bir sonraki temizliği bekleyen daha fazla bot demektir.",
                    "Gerçek takipçiler dalgalar halinde gitmez. Bazıları zamanla, tek tek uzaklaşır; herkesin takibi bıraktığı nedenlerle: ilgisini kaybetmiştir ya da takip ettiklerini toparlamıştır.",
                ],
            },
            {
                "h2": "Kimse size kalıcı takipçi satamaz",
                "p": [
                    "Kalıcı TikTok takipçi satan herkese karşı dikkatli olun. Gerçek bir insan her zaman fikrini değiştirebilir; sıfır takipten çıkma vaadi ancak hiç düşünmeyen hesaplar için anlamlıdır. Söyleyebileceğimiz şu: takip etmeyi seçen insanlar genellikle kalır, çünkü videolarınız için takip ettiler.",
                ],
            },
            {
                "h2": "Kalan takipçileri nasıl tutarsınız?",
                "ul": [
                    "Onları takip etmeye iten türde videolar paylaşmaya devam edin.",
                    "Yorumlara cevap verin: insanlar dinlendiklerini hissettikleri yerde kalır.",
                    "Nişinizi değiştirecekseniz bir gecede değil, yavaş yavaş değiştirin.",
                    "Orada olduğunuzu unutmayacakları sıklıkta paylaşım yapın.",
                ],
            },
        ],
        "faqs": [
            ("Getirdiğiniz takipçilerden hiç kaybeder miyim?", "Her gerçek kitlenin değiştiği gibi, belki birkaçını. Görmeyeceğiniz şey ani bir kayıp dalgasıdır; çünkü TikTok'un temizleyeceği sahte hesap yoktur."),
            ("Telafi sunuyor musunuz?", "Hayır. Telafi, silinen botların yerine yenisini koymak için vardır; burada yerine konacak bot yok. Takipçilerimiz insan ve paketiniz çalıştığı her gün yenilerini getirmeye devam eder."),
            ("İptal ettikten sonra takipçiler bende kalır mı?", "Sizin olarak kalırlar. İptal, ödediğiniz ay bittiğinde kampanyayı sonlandırır; sizi takip eden insanlar videolarınızı sevdikleri sürece takip etmeye devam eder."),
            ("TikTok takipçileriniz kalıcı mı?", "Hiçbir gerçek takipçi sözleşmeyle kalıcı değildir, bizimkiler de. Onlar insan ve insanlar takibi bırakabilir. Aynı zamanda temizlikte kaybolmayan tek takipçi türü de onlardır."),
            ("Mevcut takipçilerim arasındaki botları nasıl fark ederim?", "Birkaç profili açın. Gerçek takipçilerin kendi videoları, beğenileri ve bir geçmişi vardır. Botların genellikle hiç videosu yoktur, rastgele bir adı ve takip ettiği binlerce hesap vardır. İzlenmeleriniz de söyler: gerçek takipçiler onları hareket ettirir, botlar ettirmez."),
        ],
    },
    {
        "service": "followers",
        "modifier": "safe",
        "slug": "tiktok/takipci/guvenilir",
        "label": "Güvenilir TikTok takipçi",
        "title": "Güvenle TikTok Takipçi Satın Al: Şifre Gerekmez | Growsterr",
        "description": "TikTok takipçi satın almanın güvenli yolu: şifre yok, giriş yok, yalnızca gerçek insanlar; Stripe ile kart ödemesi ve dilediğiniz an iptal edilen aylık plan.",
        "h1": ("TikTok takipçiyi güvenle satın alın, ", "hesabınızı kimseye teslim etmeden."),
        "intro": "TikTok takipçiyi güvenle satın almanın ilk kuralı basit: hesabınız sizin elinizde kalır. İhtiyacımız olan tek şey kullanıcı adınız. Asla şifre istemeyiz, asla giriş yapmayız ve hesabınızda asla hiçbir şey çalıştırmayız. Gerçek insanlar profilinizi keşfeder ve kendi kararını verir.",
        "hero": {"image": "tiktok-creator", "alt": "Gerçek takipçilerle büyürken kendi TikTok hesabının kontrolü elinde olan bir içerik üreticisi"},
        "sections": [
            {
                "h2": "Hesabınız için güvenli",
                "p": [
                    "Çoğu takipçi hizmetindeki risk takip butonu değildir. Asıl risk onunla birlikte gelenlerdir: yabancılara verilen şifreler, sizin adınıza giriş yapan uygulamalar, kaybolup etkileşiminizi bomboş gösteren botlar. Bunların hiçbiri burada olmaz.",
                    "TikTok tarafında her yeni takipçi, profilinizi ziyaret edip takip butonuna dokunan bir insandır. Hesabınızın içinde hiçbir şey yapılmaz, bu yüzden sonradan temizlenecek bir şey de olmaz.",
                ],
            },
            {
                "h2": "TikTok takipçi için güvenilir bir site nasıl anlaşılır?",
                "ul": [
                    "Şifrenizi ya da TikTok ile giriş yapmanızı asla istemez.",
                    "Dakikalar içinde binlerce takipçi vaat etmez.",
                    "Arkasındaki şirketin adını verir.",
                    "Ödemeyi bilinen bir ödeme altyapısıyla alır ve kendi başınıza iptal etmenize izin verir.",
                    "Kesin sayılarla değil, tipik aralıklarla konuşur; çünkü gerçek insanlar önceden sayılamaz.",
                ],
            },
            {
                "h2": "Growsterr'ın arkasında kim var?",
                "p": [
                    "Growsterr'ın arkasında Sterr Agency var: şirket, Estonya'nın Tallinn kentinde kayıtlı Sterr Technologies OÜ'dür ve merkezimiz Türkiye'dedir. Ödemeler Stripe'ın güvenli ödeme sayfasından geçer: kart, Apple Pay ya da Google Pay. Bir sorunuz olduğunda WhatsApp'ta ya da e-postada bir insan cevap verir.",
                ],
            },
        ],
        "faqs": [
            ("Bu, TikTok hesabımı sıkıntıya sokabilir mi?", "Hesabınıza asla dokunmayız: şifre yok, giriş yok, otomasyon yok. Profilinize ulaşan şey, ziyaret edip takip eden insanlardır; tıpkı videolarınızdan biri paylaşıldığında olduğu gibi. TikTok adına konuşamayız, ama sizin tarafınızda daha fazla gerçek ziyaretçiden başka bir şey yoktur."),
            ("Growsterr meşru bir şirket mi?", "Evet. Sterr Agency markasının arkasında, Estonya'nın Tallinn kentinde kayıtlı Sterr Technologies OÜ var. Stripe üzerinden ödersiniz, kampanyanızı ölçülmüş rakamlardan oluşan bir panelde takip edersiniz ve dilediğiniz zaman hesabınızdan iptal edersiniz."),
            ("Ödemem güvende mi?", "Ödeme Stripe'ın güvenli ödeme sayfasından geçer, yani kart numaranızın tamamı bize hiç ulaşmaz. Kart, Apple Pay ya da Google Pay ile ödeyebilirsiniz."),
            ("Hangi bilgileri istiyorsunuz?", "TikTok kullanıcı adınızı, kitlenizin nereden gelmesi gerektiğini, bir de Growsterr hesabınız için e-posta, telefon numarası ve şifre. TikTok şifrenizi asla."),
            ("Memnun kalmazsam ne olur?", "Hesabınızdan iptal edin, paket yenilenmez. Ödediğiniz ay son gününe kadar sürer ve iade edilmez; yani getirdiği her şey sizde kalır."),
        ],
    },
    {
        "service": "followers",
        "modifier": "private-account",
        "slug": "tiktok/takipci/gizli-hesap",
        "label": "Gizli hesaba TikTok takipçi",
        "title": "Gizli Hesaba TikTok Takipçi Satın Alınır mı? | Growsterr",
        "description": "Gizli hesaba TikTok takipçi mi almak istiyorsunuz? Gerçek insanlar gizli profillere yalnızca istek gönderebilir; bu yüzden paket sürerken açık hesap istiyoruz.",
        "h1": ("Gizli hesaba TikTok takipçi satın almak mı? ", "Nasıl işlediğini anlatalım."),
        "intro": "Gizli bir hesap için TikTok takipçi satın almayı mı düşünüyorsunuz? Gerçek insanlar gizli bir profili doğrudan takip edemez: yalnızca istek gönderebilir ve siz onaylayana kadar videolarınızı göremez. Kampanyalarımızın herkese açık hesaplarda çalışmasının ve paketiniz sürerken hesabınızı açık tutmanızı istememizin nedeni bu.",
        "hero": {"image": "tiktok-creator", "alt": "Bir kampanya öncesinde TikTok hesabını gizliden herkese açığa çeviren bir içerik üreticisi"},
        "sections": [
            {
                "h2": "Gizli hesap ile gerçek büyüme neden bağdaşmaz?",
                "p": [
                    "Biri gizli bir TikTok hesabına geldiğinde bir isim, bir fotoğraf ve bir kilit görür. Video yok, karar verecek bir şey yok; bu yüzden ziyaretçilerin çoğu çıkıp gider. İstek gönderen birkaç kişi kabul etmenizi bekler ve büyüyen bir istek yığını kolayca gözden kaçar.",
                    "Siz her isteği onaylamadan gizli bir hesabı büyütebileceğini söyleyen bir hizmet, ya onları kabul etmek için sizin adınıza giriş yapıyordur ya da hiçbir şey eklemiyordur.",
                ],
            },
            {
                "h2": "Gizlilik sizin için önemliyse seçenekleriniz",
                "ul": [
                    "Paketinizin sürdüğü aylarda herkese açık moda geçin, sonra karar verin.",
                    "Arkadaşlarınız ve aileniz için ayrı, gizli bir hesap tutun; herkese açık olanı büyütün.",
                    "Kişisel videolarınızı Arkadaşlar ya da Yalnızca ben olarak ayarlayın, gerisini yeni insanlara açık bırakın.",
                ],
            },
        ],
        "faqs": [
            ("Gizli bir TikTok hesabını büyütebilir misiniz?", "İyi değil ve aksini iddia etmeyeceğiz. Gerçek insanların karar vermeden önce videolarınızı görmesi gerekir, gizli profil ise onları saklar. Paket sürerken hesabınızı herkese açık tutun."),
            ("Takip isteklerini onaylamam gerekir mi?", "Yalnızca gizli hesapta; bu yüzden herkese açığa geçmenizi istiyoruz. Herkese açık bir hesapta insanlar hemen takip eder ve sizin yapmanız gereken bir şey kalmaz."),
            ("Ay bitince tekrar gizliye geçebilir miyim?", "Geçebilirsiniz. Mevcut takipçileriniz kalır. Yeni insanlar yeniden yalnızca istek gönderebilir, bu yüzden büyüme onayladığınız kadarına iner."),
            ("İstekleri benim yerime kabul etmek için giriş bilgilerime ihtiyacınız var mı?", "Hayır, kimsenin de olmamalı. Asla şifrenizi istemez ya da hesabınıza giriş yapmayız. İstekleri hesabınızın içinden yönetmeyi teklif eden herkes, bir büyüme hizmetinin ihtiyaç duyduğundan fazla erişim istiyordur."),
            ("Bazı videolarım gizli kalabilir mi?", "Evet. TikTok her videoyu kimin izleyebileceğini ayarlamanıza izin verir. Keşfedilebilmek için profilinizi açık tutun, birkaç kişisel videoyu sınırlayın."),
        ],
    },
    {
        "service": "followers",
        "modifier": "live",
        "plan": "starter",
        "slug": "tiktok/takipci/canli-yayin",
        "label": "Canlı yayın için TikTok takipçi",
        "title": "Canlı Yayın İçin TikTok Takipçi Satın Al | Growsterr",
        "description": "TikTok'ta canlı yayın için 1.000 takipçi gerekir. Oraya yayına katılabilecek gerçek insanlarla ulaşın: {starter_name} genellikle ayda {starter_audience} getirir.",
        "h1": ("Canlı yayın için TikTok takipçi satın alın, ", "yayını izleyecek biri de olsun."),
        "intro": "Canlı yayın açmak için TikTok takipçi satın almak, ancak o takipçiler yayına gelebiliyorsa anlamlıdır. TikTok canlı yayını açmadan önce 1.000 takipçi ister; paketlerimiz sizi oraya, videolarınızı bulup takip etmeye karar veren gerçek insanlarla götürür. Bir aylık {starter_name} genellikle bunlardan {starter_audience} ekler.",
        "hero": {"image": "tiktok-creator", "alt": "İlk TikTok canlı yayını için telefonunu ve halka ışığını kuran bir içerik üreticisi"},
        "sections": [
            {
                "h2": "1.000 takipçi eşiği ve botların onu neden gerçekten açmadığı",
                "p": [
                    "Bot takipçiler sayıyı 1.000'in üstüne itebilir, ama canlı yayın bir odadır ve botlar içeri girmez. Kimsenin izlemediğini gösteren bir sayaca yayın yaparsınız. TikTok sahte hesapları dalgalar halinde de siler, yani sayı yeniden eşiğin altına inebilir.",
                    "Gerçek takipçiler farklıdır. Videolarınızı beğendikleri için takip ettiler; canlı yayına geçtiğinizde fark edip uğrama ihtimali en yüksek olanlar onlardır.",
                ],
            },
            {
                "h2": "Büyürken canlı yayına hazırlanmak",
                "ul": [
                    "Uygulamanızdaki canlı yayın seçeneğine bakın: TikTok'un ayrıca yaş şartı ve yayınlar için kendi kuralları var.",
                    "Paket sürerken paylaşım yapmaya devam edin ki yeni takipçilerin kalmak için bir nedeni olsun.",
                    "Videolarınızda ilk canlı yayının yaklaştığını söyleyin.",
                    "İlk yayını somut bir şeyin etrafında planlayın: soru-cevap, bir eğitim, kamera arkası.",
                ],
            },
            {
                "h2": "1.000'i geçtikten sonra",
                "p": [
                    "Paketiniz siz iptal edene kadar aydan aya devam eder, yani canlı yayın açıldıktan sonra da kitle büyümeye devam eder. Belirli bir saatte yayına izleyici göndermeyiz; kimin katılacağı onlara kalmıştır. Büyüyen şey, katılabilecek insanların sayısıdır.",
                ],
            },
        ],
        "faqs": [
            ("Canlı yayın açabilmem ne kadar sürer?", "Nereden başladığınıza bağlı. {starter_name} genellikle ayda {starter_audience} yeni takipçi getirir; küçük bir hesap için eşik genellikle birkaç haftalık iştir. Ne zaman takip edeceklerine insanlar karar verir, bu yüzden tarih veremeyiz."),
            ("Canlı yayın şartı hâlâ 1.000 takipçi mi?", "Bu, TikTok'un uzun süredir uyguladığı eşik; ama kuralları TikTok belirler ve değiştirebilir ya da deneyebilir. Uygulamanızdaki canlı yayın seçeneği hesabınız için neyin geçerli olduğunu gösterir."),
            ("Yeni takipçilerim canlı yayınımı izler mi?", "Bazıları izleyebilir. Videolarınız için takip eden gerçek insanlar onlar; katılıp katılmayacakları da her kitlede olduğu gibi o günkü hallerine bağlı. Botlar asla izlemez."),
            ("İlk canlı yayınıma izleyici gönderebilir misiniz?", "Hayır. Kimse seçtiğiniz bir saatte bir yayına gerçek insan koyamaz; komutla katılan hesaplar da orada sessizce oturur. Bizim yapabileceğimiz, gelebilecek kitleyi büyütmek."),
            ("Canlı yayına geçmek için hangi paket uygun?", "{starter_name} eşiğe ulaşmak için genellikle yeterlidir. Düzenli yayın yapmayı planlıyorsanız {rising_name} kitleyi daha hızlı büyütür ve ilginin hangi videolara gideceğini seçmenizi sağlar."),
        ],
    },
    # --- Comments -------------------------------------------------------------------------
    {
        "service": "comments",
        "slug": "tiktok/yorum",
        "label": "TikTok yorum",
        "title": "TikTok Yorum Satın Al: Gerçek Yorumlar Pakette | Growsterr",
        "description": "TikTok yorum satın almanın dürüst yolu: gerçek insanlar videolarınız hakkında ne düşündüğünü yazar; {starter_name} ile genellikle ayda {starter_comments} yorum.",
        "h1": ("TikTok yorum satın almak mı? ", "Söyleyecek sözü olan insanlar gelsin."),
        "intro": "TikTok yorum satın almaya geldiyseniz, dürüst hali şu: yorumu tek başına satmıyoruz. Her paket size gerçek insanlar gönderir; bazıları keyif aldığı videolara kendi cümleleriyle yorum yapar. {starter_name} genellikle ayda {starter_comments} yorum getirir, büyük paketler daha fazlasını.",
        "hero": {"image": "tiktok-watch-time", "alt": "Az önce izledikleri bir TikTok videosunun altına yorum yazan izleyiciler"},
        "sections": [
            {
                "h2": "Yorumlar neden stok gibi sipariş edilemez?",
                "p": [
                    "Bir yorum, birinin size ne düşündüğünü anlatmasıdır. Sipariş üzerine yazıldığı an bu olmaktan çıkar: aynı birkaç kalıp, aynı emojiler, kendi videosu olmayan hesaplardan. İzleyiciler bunları fark eder ve kaydırıp geçer.",
                    "Gerçek yorumlar daha dağınık ve çok daha işe yarar. Soru sorarlar, itiraz ederler, espri cümlenizi size geri yazarlar ve bunu görmesi gereken bir arkadaşı etiketlerler.",
                ],
            },
            {
                "h2": "Her paket kaç yorum getirir?",
                "ul": [
                    "{starter_name}: {starter_audience} yeni takipçiyle birlikte genellikle ayda {starter_comments} yorum.",
                    "{rising_name}: genellikle {rising_comments}; ilginin hangi videolara gideceğine siz karar verirsiniz.",
                    "{pro_name}: genellikle {pro_comments}; üstüne öncelikli yerleşim ve doğrudan bize ulaşan bir WhatsApp hattı.",
                ],
            },
            {
                "h2": "Gerçek yorumları bir sonraki videonuza dönüştürün",
                "p": [
                    "TikTok bir yoruma videoyla cevap vermenizi sağlar; bir izleyicinin içten sorusu, bulabileceğiniz en kolay fikirlerden biridir. Önceden yazılmış yorumlar cevaplamaya değer hiçbir şey sormaz.",
                ],
                "image": {"image": "tiktok-creator", "alt": "TikTok'ta bir izleyicinin sorusuna video cevap çeken bir içerik üreticisi"},
            },
        ],
        "faqs": [
            ("Takipçi olmadan TikTok yorumu alabilir miyim?", "Hayır. Yorumlar her aylık paketin parçasıdır ve sizi takip edip beğenen aynı insanlardan gelir. Ayrıca satılmazlar."),
            ("İnsanların ne yazacağına karar verebilir miyim?", "Hayır; işin özü de bu: insanlar gerçekten ne düşünüyorsa onu yazar. Bir sohbet başlatmak için açıklamanızda ya da videonun sonunda bir soru sorun. Gerçek izleyiciler sorulara cevap verir."),
            ("Hangi videolar yorum alır?", "Çoğunlukla en yenileri, çünkü insanlar profilinizde önce onları görür. Sohbetin tek bir videoda toplanmasını istiyorsanız {rising_name} ve {pro_name} kampanyayı ona yöneltmenizi sağlar."),
            ("Yorumlar benim dilimde mi olur?", "İnsanlar konuştukları dilde yorum yapar. Kampanyanızı dilinizin konuşulduğu bir yere yöneltin; okuyacağınız da genellikle o dil olur."),
            ("Yorumlar hepsi birden mi gelir?", "Hayır. İnsanlar videolarınızı keşfettikçe ay boyunca gelirler. Neredeyse kimsenin izlemediği bir videoya ilk dakikada gelen bir yorum yağmuru, onu gören herkese yanlış görünür."),
        ],
    },
    # --- Views ----------------------------------------------------------------------------
    {
        "service": "views",
        "slug": "tiktok/izlenme",
        "label": "TikTok izlenme",
        "title": "TikTok İzlenme Satın Al: Gerçekten İzleyenlerden | Growsterr",
        "description": "Gerçek izlemeyle gelen TikTok izlenmesi: insanlar profilinizi keşfeder ve videolarınızı izler; takipçi ve beğeni de getiren aylık bir paketin içinde.",
        "h1": ("TikTok izlenme satın alın: ", "gerçekten izleyen insanlardan."),
        "intro": "TikTok izlenme satın almak mı istiyorsunuz? Biner biner oynatma satmıyoruz. Her paket profilinize yeni izleyiciler gönderir; onlar da dikkatlerini çeken videoları izler, keyif aldıklarını beğenir ve daha fazlasını istediklerinde takip eder. İzlenmeleri paketin bir parçasıdır, asla ayrı bir sayı değil.",
        "hero": {"image": "tiktok-watch-time", "alt": "Telefonlarında TikTok videolarını tek tek izleyen gerçek insanlar"},
        "sections": [
            {
                "h2": "Bir izlenme, izlemenin kendisi kadar değerlidir",
                "p": [
                    "TikTok bir videonun oynatılmaya başladığı an bir izlenme sayar. Önemli olan sonra ne olduğudur: izleyici kaldı mı, tekrar izledi mi, paylaştı mı, profilinizi açtı mı? Bir saniye sonra duran binlerce oynatma, TikTok'a umduğunuzun tam tersini söyler.",
                    "Gerçek insanlardan gelen izlenmeler hikâyenin geri kalanını da taşır; çünkü izleyen kişi aynı zamanda beğenebilecek, takip edebilecek ya da videoyu başkasına iletebilecek kişidir.",
                ],
            },
            {
                "h2": "İzlenmelere neden bir sayı koymuyoruz?",
                "p": [
                    "Takipçi, beğeni ve yorumların tipik aylık aralıkları var. İzlenmelerin yok, çünkü izleyici kadar videoya da bağlıdırlar: biri bir videoyu bir kez izleyip geçer, bir başkası onu döngüye alıp üç video daha açar. Bu yüzden izlenme sayısı satmıyoruz. İnsanları biz getiririz, gerisini videolarınız yapar.",
                ],
            },
            {
                "h2": "TikTok izlenme satın alacağınız yeri seçmek",
                "ul": [
                    "Gerçek bir izlenme bir izleyiciyle gelir: yanında hareket eden beğeni, takip ve yorumlara bakın.",
                    "Biner biner satılan ucuz izlenmeler insan değil, oynatmadır.",
                    "İzlenme teslim etmek için TikTok giriş bilgilerinizi isteyen bir site, terk edilecek bir sitedir.",
                    "Bir hizmet size panel gösteriyorsa, gerçekte neyi ölçtüğüne bakın.",
                ],
            },
        ],
        "faqs": [
            ("Videolarım kaç izlenme alır?", "İzlenmeleri önceden saymıyoruz. Her gün profilinizi keşfeden gerçek insanlardan gelirler; ne kadar izleyecekleri de videolarınıza bağlıdır. Ölçüp size gösterdiğimiz şey, kampanyanızdan gelen profil ziyaretleri ve bunların getirdiği yeni takipçilerdir."),
            ("Belirli bir TikTok videosu için izlenme satın alabilir miyim?", "Tek başına hayır. {rising_name} ve {pro_name} ile ilginin hangi videolara gideceğini siz seçersiniz; böylece önemsediğiniz bir videoyu getirdiğimiz insanların daha fazlası görür."),
            ("Ucuz TikTok izlenmeleri zarar verir mi?", "Verebilir. Bot izlenmeleri kimsenin izlemediği oynatmalardır; insanların videonuzda ortalama ne kadar kaldığını düşürürler. İnsanların ne kadar kaldığı da TikTok'un bir videoyu sonra kime göstereceğine karar verirken tarttığı şeylerden biridir."),
            ("TikTok izlenme satın almak için uygulama gerekir mi?", "Hayır. Her şey tarayıcıdaki Growsterr hesabınızdan yürür: sipariş verirsiniz, kartla ya da Apple Pay gibi bir telefon cüzdanıyla ödersiniz ve panelinize bakarsınız. İzlenme açmak için TikTok ile giriş yapmanızı isteyen uygulamalardan uzak durun."),
            ("İzlenmeler takipçi ve beğeniyle birlikte mi gelir?", "Evet. Videolarınızı izleyen insanlar, takip eden ve beğenen insanlarla aynıdır: {pick_name} ile genellikle ayda {pick_audience} yeni takipçi ve {pick_likes} beğeni."),
        ],
    },
    # --- Likes (the likes page itself is in tiktok.py) ----------------------------------------
    {
        "service": "likes",
        "modifier": "real",
        "slug": "tiktok/begeni/gercek",
        "label": "Gerçek TikTok beğeni",
        "title": "Gerçek TikTok Beğeni Satın Al, Bot Değil İnsan | Growsterr",
        "description": "Gerçek insanlardan TikTok beğenisi, bot yok: videonuzu izleyip beğenen izleyiciler; takipçi ve yorumla birlikte aylık bir paketin içinde.",
        "h1": ("Gerçek TikTok beğeni satın alın. ", "Her biri izlemiş bir insandan."),
        "intro": "Growsterr üzerinden gerçek TikTok beğeni satın aldığınızda her beğeni bir insandan gelir, asla bir bottan değil: kampanyamız sayesinde profilinizi bulan, bir video oynatan ve onu beğenen biri. Beğeniler her pakette takipçi ve yorumla birlikte gelir; {starter_name} ile genellikle ayda {starter_likes}.",
        "hero": {"image": "tiktok-likes", "alt": "Bir TikTok videosunun sonunda gerçek bir izleyicinin dokunduğu kalp"},
        "sections": [
            {
                "h2": "Gerçek beğeni ile bot beğenisi nasıl ayırt edilir?",
                "ul": [
                    "Kimin beğendiğine bakın: etkinlikleriniz hesapları gösterir; gerçek olanların kendi fotoğrafları, videoları ve takipçileri vardır.",
                    "Beğenileri izlenmelerle karşılaştırın: gerçek beğeniler izleyenlerin bir dilimidir, asla hepsinden fazla değil.",
                    "Zamanlamaya bakın: gerçek beğeniler günler içinde damla damla gelir, bot beğenileri bir blok halinde düşer.",
                    "Yanlarında ne geldiğine bakın: gerçek beğenenler bazen yorum yapar, takip eder ya da paylaşır.",
                ],
            },
            {
                "h2": "Yüksek kaliteli beğeninin tanımı",
                "p": [
                    "Yüksek kaliteli beğeni, arkasında gerçek bir izlenme olan, tekrar izleyebilecek birinden gelen beğenidir. Hesabın ne kadar parlak göründüğü önemli değil. Önemli olan, bir insanın videonuzu seçmesi ve kalbe dokunacak kadar onunla kalmasıdır.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Keyif aldığı bir TikTok videosunda duran, başparmağı kalbin üzerinde bir izleyici"},
            },
            {
                "h2": "Gerçek beğeniler paketin geri kalanıyla gelir",
                "p": [
                    "Beğeniler, aynı insanların yaptıklarının bir parçasıdır: takip de ederler, yorum da yaparlar. {pick_name} ile bir ay genellikle {pick_likes} beğeni, {pick_audience} yeni takipçi ve {pick_comments} yorum eder; hepsi gerçek insanlardan.",
                ],
            },
        ],
        "faqs": [
            ("Beğeniler hiç bot olmadan, gerçek insanlardan mı?", "Evet. Hiçbir yerde bot, sahte hesap ya da otomasyon kullanmıyoruz. Her beğeniyi, kampanyamız aracılığıyla videonuza ulaşıp kalbe dokunmaya karar veren biri bırakır."),
            ("Takipçi olmadan gerçek beğeni satın alabilir miyim?", "Hayır. Gerçek beğeniler yalnızca gerçek izleyicilerden gelir, gerçek izleyiciler de canları istediğinde takip eder, yorum yapar ve paylaşır. Her şeyin tek pakette gelmesinin nedeni bu."),
            ("Kaç beğeni alacağımı neden tam söyleyemiyorsunuz?", "Çünkü kararı insanlar verir. Gerçek kitlelerin genellikle ne yaptığını biliyoruz, bu yüzden aralık veriyoruz; örneğin {pick_name} ile ayda {pick_likes}. Sabit bir sayı, birine beğenmesinin söylendiği anlamına gelirdi."),
            ("Gerçek beğeniler videolarımın daha çok kişiye ulaşmasına yardım eder mi?", "Bot beğenilerinde hiç olmayan şeyle gelirler: gerçek izlenme süresi ve bazen bir paylaşım ya da takip. Bir videonun yol almasına yardım eden bu daha dolu tablodur, çıplak bir sayı değil."),
            ("Videolarımı beğenen insanlar nereli?", "Sipariş verirken verdiğiniz konumdan: tek bir şehir, daha geniş bir bölge ya da bütün bir ülke. Kitlenize en yakın eşleşme bundan biraz daha genişse, beğenilerin bir kısmı çevre bölgeden gelir."),
        ],
    },
    {
        "service": "likes",
        "modifier": "organic",
        "slug": "tiktok/begeni/organik",
        "label": "Organik TikTok beğeni",
        "title": "Organik TikTok Beğeni: Videolarınızın Hak Ettiği | Growsterr",
        "description": "Organik TikTok beğeni satın alın: gerçek insanlar kampanyamızla profilinize ulaşır ve hak eden videoları beğenir; beğeniler en iyi işlerinizde toplanır.",
        "h1": ("Organik TikTok beğeni satın alın, ", "her video kendi beğenisini kazansın."),
        "intro": "Organik TikTok beğeni satın alınabilir mi? İnsanların videolarınızı görmesi için ödeme yapabilirsiniz; paketlerimizin yaptığı da bu. Beğeniler organik kalır, çünkü her biri gerçek bir insanın izlediği bir videoya verdiği tepkidir. Kimseye neyi beğeneceği söylenmez ve doğal görünsün diye hiçbir şey eşit dağıtılmaz.",
        "hero": {"image": "tiktok-likes", "alt": "Bir içerik üreticisinin TikTok videolarında dengesiz biriken, en çok en iyisinde toplanan beğeniler"},
        "sections": [
            {
                "h2": "Organik beğeniler neye benzer?",
                "p": [
                    "Organik beğeniler dengesizdir. En iyi videonuz en zayıfından çok daha fazlasını alır, eski videolara beğeni gelmeye devam eder ve tek bir hit profilinizdeki her şeye beğeni çekebilir. Satın alınan beğeniler düz görünür: her gönderide aynı sayı, hepsi aynı anda.",
                ],
            },
            {
                "h2": "Beğenilerin nereye gideceğine videolarınız karar verir",
                "ul": [
                    "İlk saniyeler, birinin beğenecek kadar kalıp kalmayacağına karar verir.",
                    "İnsanların tanıdığı bir ses, kaydırmayı bırakmalarını sağlayan şey olabilir.",
                    "Altyazı ve ekran yazıları, sesi kapalı izleyenlere yardım eder.",
                    "Net bir kapanış ya da kusursuz bir döngü, insanların tekrar izlemesini sağlar.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Paylaşmadan önce bir TikTok videosu için ses seçen bir içerik üreticisi"},
            },
            {
                "h2": "Paket neyi ekler?",
                "p": [
                    "Bizim eklediğimiz şey insandır: ayın her günü, seçtiğiniz yerden düzenli bir gerçek izleyici akışı. {pick_name} ile onlardan genellikle {pick_likes} beğeni gelir; yeni takipçiler ve yorumlarla birlikte.",
                ],
            },
        ],
        "faqs": [
            ("Ödeme yapıyorsam beğeniler gerçekten organik mi?", "Paranız görünme şansını satın alır. Her beğeni yine videonuzu izleyen birinin verdiği bir karardır; organik de bu demektir. Bir video tutmazsa daha az alır, bu da bilmeye değer bir şeydir."),
            ("Tüm videolarım aynı sayıda beğeni mi alır?", "Hayır. Organik beğeniler kaliteyi, zamanlamayı ve biraz da şansı izler. Bu dengesizlik, onları inandırıcı kılan şeyin bir parçasıdır."),
            ("Organik beğeniler belirli bir ülkeden gelebilir mi?", "Evet. Bir şehir, bölge ya da ülke seçin; profilinizi gören insanlar önce oradan gelir. Beğenileri de aynı yerden gelir."),
            ("Organik beğeniler bir videonun daha çok gösterilmesine yardım eder mi?", "TikTok beğenilere izlenme süresi, paylaşımlar ve takiplerle birlikte bakar. İzlemiş insanlardan gelen beğeniler bu diğer sinyalleri de yanında taşır; bot beğenileri hiçbirini taşımaz."),
            ("Bunun etkileşim gruplarından farkı ne?", "Etkileşim grupları beğeni takas eder: siz onlarınkini beğenirsiniz, onlar sizinkini. Hesaplar gerçektir ama ilgi gerçek değildir. Bizim izleyicilerimizin size bir borcu yok; bir videoyu beğendiklerinde bunu içten yaparlar."),
        ],
    },
    {
        "service": "likes",
        "modifier": "monthly",
        "slug": "tiktok/begeni/aylik",
        "label": "Aylık TikTok beğeni",
        "title": "Aylık TikTok Beğeni, Otomatik Beğeni Değil | Growsterr",
        "description": "TikTok beğeniyi gerçek insanlardan aylık alın: her ay yenilenen, her yeni videonuza izleyici getiren bir paket. Otomatik beğeninin aksine ortada yazılım yok.",
        "h1": ("Aylık TikTok beğeni satın alın. ", "Bir bot değil, gerçek insanlar."),
        "intro": "Her yeni videonuz iyi bir başlangıç yapsın diye TikTok beğeniyi aylık satın almak mı istiyorsunuz? Paketlerimiz bunu yapar; otomatik beğeniden tek bir farkla: ortada yazılım yoktur. Paket her ay kendiliğinden yenilenir ve her gün gerçek insanlar profilinizi keşfeder, izler ve keyif aldıkları videoları beğenir.",
        "hero": {"image": "tiktok-likes", "alt": "Bir içerik üreticisinin en yeni TikTok videolarına gerçek izleyicilerden gelen beğeniler"},
        "sections": [
            {
                "h2": "Otomatik beğeni ile aylık paket",
                "p": [
                    "TikTok otomatik beğeni hizmetleri hesabınızı izler ve her yeni videoya dakikalar içinde belirli sayıda beğeni gönderir. Her video aynı sayıyı, onu hiç izlemeyen hesaplardan alır. Otomatik görünür, çünkü öyledir.",
                    "Aylık paket yalnızca olması gereken tek yerde otomatiktir: ödemede. Yeniden sipariş vermezsiniz ve kampanyanız aylar arasında durmaz. Beğenilerin kendisi insan işi kalır; harika bir video daha çok, sakin bir video daha az alır.",
                ],
            },
            {
                "h2": "Bir aylık beğeni neye benzer?",
                "ul": [
                    "Beğeniler 30 güne ve insanların izlemeyi seçtiği videolara yayılır.",
                    "En güçlü videolarınız en çok beğeniyi toplar, olması gerektiği gibi.",
                    "Yeni videolar taze bir kitleyle buluşur, çünkü her gün yeni insanlar profilinizi bulur.",
                    "{rising_name} ve {pro_name}, bu ay en önemli videoları seçmenizi sağlar.",
                ],
            },
            {
                "h2": "Aylık ritim TikTok'a neden uyar?",
                "p": [
                    "TikTok'ta içerik üreticileri ritimlerle çalışır: bir seri, haftalık bir format, bir lansman. Aylık paket buna uyar. Her ay panelinizin neyi ölçtüğünü görür, insanların hangi videoları beğendiğine bakar ve gelecek ayın neye odaklanacağına karar verirsiniz.",
                ],
            },
        ],
        "faqs": [
            ("Her yeni video otomatik olarak beğeni alır mı?", "Bir takvime göre değil. Yeni videoları o gün profilinizi keşfeden insanlar görür ve keyif aldıklarını beğenirler. Bazı videolar çok, bazıları daha az toplar; gerçek bir kitle böyle davranır."),
            ("Her ay kaç beğeni alırım?", "{starter_name} genellikle ayda {starter_likes}, {rising_name} {rising_likes}, {pro_name} {pro_likes} getirir; hepsi sizi takip eden insanlardan."),
            ("Paylaşım yaptığımda size haber vermem gerekir mi?", "Hayır. Kampanya profilinizi gösterir, insanlar da en yeni ne varsa onu görür. Bir video diğerlerinden önemliyse {rising_name} ve {pro_name} ilgiyi oraya yöneltmenizi sağlar."),
            ("Otomatik beğeninin nesi yanlış?", "Paylaştıktan dakikalar sonra, her seferinde aynı sayıda, hiç izlemeyen hesaplardan gelir. Arkasında izlenme süresi olmayan beğeniler ve her videoda aynı sayı, herkesin okuyabileceği bir desen oluşturur."),
            ("Aylık beğenileri durdurabilir miyim?", "Evet. Hesabınızdan iptal etmek yenilemeleri sonlandırır; içinde bulunduğunuz ay yine son gününe kadar sürer."),
        ],
    },
    {
        "service": "likes",
        "modifier": "gradual",
        "slug": "tiktok/begeni/kademeli",
        "label": "Kademeli TikTok beğeni",
        "title": "Yavaş TikTok Beğeni, Gerçek İzleyicilerden | Growsterr",
        "description": "TikTok beğeniyi yavaş ve doğal alın: gerçek insanlar videolarınızı gün gün, azar azar beğenir; takipçi ve yorum da getiren bir paketin içinde.",
        "h1": ("Yavaş TikTok beğeni satın alın, ", "gerçek izleyicilerin verdiği gibi."),
        "intro": "TikTok beğeniyi yavaş yavaş satın alanlar, doğal görünmesini ister. Bunun en basit yolu doğal olmasıdır. Ayın her günü kampanyamız profilinize yeni izleyiciler getirir; izlerler ve keyif aldıklarını birkaç birkaç beğenirler. {pick_name} ay boyunca genellikle {pick_likes} beğeniye ulaşır.",
        "hero": {"image": "tiktok-likes", "alt": "Birkaç gün boyunca birer ikişer beliren TikTok video beğenileri"},
        "sections": [
            {
                "h2": "Gerçek beğeniler bir videonun ömrüne nasıl yayılır?",
                "p": [
                    "Gerçek bir video tüm beğenilerini ilk saatte almaz. İnsanlar onu günler sonra profilinizden bulur, eski videolara geri kaydırır ve kaçırdıklarını beğenir. O uzun kuyruk, gerçek ilginin görünüşüdür ve ani bir beğeni yığınında tam olarak eksik olan şeydir.",
                ],
            },
            {
                "h2": "Kademeli teslimat neden asıl mesele değil?",
                "p": [
                    "Bazı hizmetler kademeli teslimat satar: aynı bot beğenileri, birkaç saate yayılarak salınır. Hız değişir, beğeniler değişmez. Arkasında izlenme olmayan bir beğeni, ne kadar yavaş gelirse gelsin boştur.",
                    "Bizde salınacak bir şey yok. Beğeniler izleyen insanlardan, izledikleri gün gelir.",
                ],
            },
            {
                "h2": "Hafta hafta ne beklemeli?",
                "ul": [
                    "Birinci hafta: ilk ziyaretçiler ve ilk beğenileri, genellikle en yeni videolarınızda.",
                    "İkinci ve üçüncü hafta: profilinizi daha çok insan bulup geriye kaydırdıkça düzenli bir akış.",
                    "Dördüncü hafta: tek bir videoya yığılmak yerine birçok videoya yayılmış bir aylık beğeni.",
                ],
            },
        ],
        "faqs": [
            ("Günde kaç beğeni alırım?", "Günden güne değişir. Ay boyunca {starter_name} genellikle {starter_likes}, {rising_name} {rising_likes} beğeni getirir; 30 güne ve insanların izlemeyi seçtiği videolara yayılır."),
            ("Beğenilerin ne kadar yavaş geleceğini seçebilir miyim?", "Bir hız ayarı yok, çünkü kimse beğenileri bir zamanlayıcıyla salmıyor. İnsanlar izlediğinde gelirler. Belirli videolara daha çok ilgi istiyorsanız {rising_name} ve {pro_name} onları seçmenizi sağlar."),
            ("Eski videolarım neden beğeni alıyor?", "Çünkü gerçek insanlar göz atar. Bir videodan keyif alan biri çoğu zaman profilinizi açıp birkaç tane daha izler. Bu beğeniler iyiye işarettir: insanların sizden daha fazlasını istediğini gösterir."),
            ("Beğeniler izlenmeyle birlikte mi gelir?", "Her zaman. Burada bir beğeni, bir insanın önce videoyu izlediği anlamına gelir; yani izlenmeleriniz de onunla birlikte artar. Bir videonun aldığı izlenmeden fazla beğeni, işin içinde botların olduğunu ele verir."),
            ("Beğeniler ilk aydan sonra da devam eder mi?", "Evet, paketiniz yenilendiği sürece. Her ay taze bir izleyici akışı getirir; önceki aylarda takip edenler de genellikle yeni videolarınızı beğenmeye devam eder."),
        ],
    },
    {
        "service": "likes",
        "modifier": "no-drop",
        "slug": "tiktok/begeni/dusmeyen",
        "label": "Düşmeyen TikTok beğeni",
        "title": "Düşmeyen TikTok Beğeni: Yalnızca Gerçek İnsanlar | Growsterr",
        "description": "Videolarınızda kalan TikTok beğenisi: gerçek insanlardan gelen beğeniler, TikTok sahte hesapları temizlediğinde kaybolmaz. Her pakette, asla tek başına değil.",
        "h1": ("Düşmeyen TikTok beğeni satın alın, ", "çünkü onu bir insan içten verdi."),
        "intro": "Düşmeyen TikTok beğeni satın almak için hiçbir temizliğin dokunamayacağı beğenilere ihtiyacınız var. Sahte bir hesap silindiğinde bıraktığı her beğeni de onunla kaybolur. Bizim beğenilerimiz aylık bir paketin içinde, videolarınızı izleyen gerçek insanlardan gelir; insanlar da bir kez verdikleri beğeniyi nadiren geri alır.",
        "hero": {"image": "tiktok-likes", "alt": "Haftalar boyunca sabit kalan bir TikTok beğeni sayısı"},
        "sections": [
            {
                "h2": "Satın alınan beğeniler neden kaybolur?",
                "p": [
                    "Beğeni sayıları esas olarak tek bir nedenle düşer: arkalarındaki hesaplar artık yoktur. TikTok sahte hesapları ve sahte etkileşimi siler; sildiğinde beğeniler de gider. Bir video bir hafta büyük bir sayı, ertesi hafta çok daha küçüğünü gösterebilir; arada sizin hiçbir şey yapmamanıza rağmen.",
                ],
            },
            {
                "h2": "Kalan beğeniler ve nedenleri",
                "ul": [
                    "Kendi geçmişi olan gerçek hesaplardan gelirler; bir temizliğin onları silmesi için bir neden yoktur.",
                    "İzleyen insanlardan gelirler, yani arkalarındaki izlenmeler de gerçektir.",
                    "Günlere ve videolara yayılırlar, asla tek bir gönderiye yığılmazlar.",
                    "Çoğu zaman takip de eden insanlara aittirler; yani gerçek bir kitleye bağlıdırlar.",
                ],
            },
            {
                "h2": "Daha önce beğeni satın aldıysanız",
                "p": [
                    "Beğenileri kendiniz kaldıramazsınız, buna gerek de yok. Bot beğenileri, TikTok arkalarındaki hesapları temizledikçe silinir. Yapabileceğiniz en iyi şey, sonraki videolarınıza gerçek izleyiciler getirmektir; böylece hesabınız adına konuşan, yeni rakamlar olur.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Gerçek izleyiciler için yeni bir TikTok videosuyla sıfırdan başlayan bir içerik üreticisi"},
            },
        ],
        "faqs": [
            ("Beğeniler hiç kaybolur mu?", "Yalnızca arkasındaki kişi beğeniyi kaldırırsa ya da hesabını silerse; bu da nadirdir. Bekleyen bir silinme dalgası yok, çünkü arkalarında sahte hesap yok."),
            ("Takipçi olmadan kalıcı beğeni alabilir miyim?", "Hayır. Beğeniler her paketin parçasıdır; aynı izleyicilerin bıraktığı takip ve yorumlarla birlikte gelir. Ayrıca satmıyoruz ve kalıcı olmalarının bir nedeni de bu: takip etmeyi seçmiş insanlara bağlıdırlar."),
            ("Başka yerden aldığım beğeniler neden düştü?", "Büyük ihtimalle arkalarındaki hesaplar silindi. Satıcı ne vaat etmiş olursa olsun, TikTok'ta sahte etkileşimin er ya da geç başına gelen budur."),
            ("Her ay kaç beğeni kalır?", "Bütün beğenilerimizi gerçek insanlar bırakır; yani asıl soru videolarınızı kaç kişinin beğendiğidir: {pick_name} ile genellikle ayda {pick_likes}."),
            ("Az sayıda gerçek beğeni, büyük bir satın alınmış sayıdan iyi mi?", "Evet. Tam bir izlenme, bir takip ya da bir yorumla gelen beğeni, gerçek ilgi gibi okunan bir desenin parçasıdır. Çevresinde hiçbir şey olmayan büyük bir sayı ise tam olarak neyse öyle okunur."),
        ],
    },
    {
        "service": "likes",
        "modifier": "safe",
        "slug": "tiktok/begeni/guvenilir",
        "label": "Güvenilir TikTok beğeni",
        "title": "TikTok Beğeni Satın Almak Güvenli mi? Bizim Yolumuz | Growsterr",
        "description": "TikTok beğeni almanın güvenilir yolu: gerçek izleyiciler, giriş yok, Stripe ile kart ödemesi, ölçüm paneli ve kendiniz iptal edebileceğiniz bir plan.",
        "h1": ("TikTok beğeni satın almanın güvenilir yolu: ", "gerçek insanlar, kestirme yok."),
        "intro": "TikTok beğeni satın almanın güvenilir olup olmadığını sormak doğru bir içgüdü. Beğeni satıcılarının çoğu bot teslim eder, bazıları giriş bilgilerinizi de ister. Bizim yaptığımız şu: gerçek insanlar profilinizi keşfeder ve keyif aldıkları videoları beğenir; Stripe üzerinden ödediğiniz ve hesabınızdan iptal edebileceğiniz aylık bir paketin içinde.",
        "hero": {"image": "tiktok-likes", "alt": "Hiçbir kestirme yol olmadan gerçek izleyicilerden beğeni alan bir TikTok videosu"},
        "sections": [
            {
                "h2": "Bir TikTok beğeni satıcısındaki tehlike işaretleri",
                "ul": [
                    "Bir saat içinde binlerce beğeni vaadi.",
                    "Bin beğeni için bir kahveden ucuz fiyat.",
                    "TikTok şifrenizin ya da TikTok ile giriş yapmanızın istenmesi.",
                    "Şirket adı yok, adres yok, koşullar yok.",
                    "Kimin izleyeceğinden hiç söz etmeden her bağlantıya satılan beğeniler.",
                ],
            },
            {
                "h2": "Bizi güvenilir kılan nedir?",
                "p": [
                    "Biz Growsterr'ız; Sterr Agency ekibi (Sterr Technologies OÜ, Tallinn, Estonya) tarafından kurulduk. Hesapları, onları gerçek insanlara gösteren, iş ortağı ağımızdaki tanıtım kampanyalarıyla büyütürüz ve yapamadıklarımız konusunda açığız: rakam sözü veremeyiz ve beğeniler asla tek başına satılmaz.",
                    "Paneliniz ölçtüklerimizi gösterir: her günün profil ziyaretleri ve bunların kaçının takibe dönüştüğü.",
                ],
            },
            {
                "h2": "Videolarınız için de güvenli",
                "p": [
                    "Bot beğenileri yalnızca sonradan kaybolmaz. Oradayken de tabloyu çarpıtırlar: bol kalp, az izlenme süresi, hiç yorum. Gerçek beğenileri izleyen insanlar bırakır; böylece videonuzun altındaki rakamlar birbiriyle uyuşur.",
                ],
            },
        ],
        "faqs": [
            ("Growsterr'ın dolandırıcılık olmadığını nasıl anlarım?", "Ne istediğimize ve neye söz verdiğimize bakın. Kullanıcı adınızı isteriz, şifrenizi asla. Tipik aralıklar veririz, kesin sayılar asla. Ödeme Stripe üzerinden geçer ve iptal, kimseye sormadan hesabınızda yapılır."),
            ("Beğeniler için iade alabilir miyim?", "Paketler aylık aboneliktir. İptal ederseniz ödediğiniz ay sürmeye devam eder ve iade edilmez; sonrasında da hiçbir ödeme alınmaz."),
            ("Güvenilir beğeniler daha önce aldıklarımdan farklı mı görünür?", "Genellikle evet. Günler içinde, videolarınıza yayılarak gelirler ve aynı insanlardan gelen izlenme, takip ve yorumlarla birliktedirler. Bot beğenileri ise genellikle tek bir videoya tek blok halinde düşer."),
            ("Bir şey yanlış görünürse kiminle konuşabilirim?", "Ekibimizden biriyle, e-postayla ya da WhatsApp'tan. {pro_name} ayrıca doğrudan bir WhatsApp hattıyla gelir."),
            ("TikTok beğenisine para ödemek hiç meşru mu?", "Bota para ödemek meşru değil: arkasında kimse olmayan bir sayı alırsınız. Gerçek insanların videolarınızı görmesi için ödeme yapmak ise farklıdır; bir işletmenin görünmek için ödeme yapması gibi. Bizim sattığımız büyüme bu türden."),
        ],
    },
    {
        "service": "likes",
        "modifier": "comment-likes",
        "slug": "tiktok/begeni/yorum-begenisi",
        "label": "TikTok yorum beğenisi",
        "title": "TikTok Yorum Beğenisi: Gerçek İzleyiciler Ne Yapar? | Growsterr",
        "description": "TikTok yorum beğenisi mi arıyorsunuz? Tek tek yorumlara beğeni satmıyoruz. Yorum bölümünüzü okuyan gerçek izleyiciler, içlerine sinen yanıtları beğenir.",
        "h1": ("TikTok yorum beğenisi satın almak mı? ", "Neyin değerli olduğuna izleyiciler karar versin."),
        "intro": "Sabitlenmiş bir yorumu ya da bir yanıtı en üste taşımak için TikTok yorum beğenisi satın almak istiyorsanız, net cevap şu: tek tek yorumlara beğeni satmıyoruz. Kampanyalarımız gerçek insanları profilinize getirir; yorum bölümünüzü okuyanlar da katıldıkları yorumları beğenir, sizinkiler de dahil.",
        "hero": {"image": "tiktok-watch-time", "alt": "Bir TikTok yorum bölümünü okuyup bir yanıtı beğenen izleyici"},
        "sections": [
            {
                "h2": "Yorumlara neden beğeni satmıyoruz?",
                "p": [
                    "Yüzlerce beğenisi olup hiç yanıtı olmayan bir yorum, kaydırıp geçen herkese tuhaf görünür. Botlardan gelen yorum beğenileri de işe yarar bir şeye işaret etmez: gelir, orada durur ve yorumun iyi olup olmadığı hakkında hiçbir şey söylemez.",
                    "Başkasının videosundaki bir yorumu da yukarı taşıyamayız. Kampanyalarımız profilinizi insanlara gösterir; diğer içerik üreticilerinin yorum bölümlerinde ne olacağı onların izleyicilerine kalmıştır.",
                ],
            },
            {
                "h2": "İnsanların gerçekten beğendiği yorumlar",
                "ul": [
                    "Bir şey katan bir yorumu sabitleyin: ikinci bölümün bağlantısı, herkesin sorduğu sorunun cevabı.",
                    "Video tazeyken, yorum bölümü en hareketli olduğunda cevap verin.",
                    "İzleyicilerin konuşacak bir şeyi olsun diye açıklamada bir soru sorun.",
                    "Cevaplarınızı kısa ve kendi sesinizle tutun; insanlar size benzeyen yorumları beğenir.",
                ],
            },
            {
                "h2": "Bir pakette yorum beğenileri nereden gelir?",
                "p": [
                    "Her paket videolarınıza aynı insanlardan beğeni ve yorum getirir; bir ayda {pick_name} genellikle {pick_likes} beğeni ve {pick_comments} yorum demektir. Bu insanlar okurken çoğu zaman başka yorumları da beğenir, ama bunu ne sayarız ne de yönlendiririz.",
                ],
            },
        ],
        "faqs": [
            ("Büyük bir içerik üreticisinin videosundaki yorumuma beğeni getirebilir misiniz?", "Hayır. Kampanyalarımız yalnızca kendi profilinizi büyütür. Başkasının yorum bölümünde bir yorumu yukarı taşımak, onu beğenmeleri için oraya hesap göndermek demektir; botlar tam da bu iş için yapılır."),
            ("Paketleriniz yorum beğenisi içeriyor mu?", "Bir sayı olarak hayır. Paketler videolarınıza beğeni ve gerçek insanların yazdığı yorumları içerir. Aynı insanlar bazen okudukları yorumları da beğenir; bu onların kendi seçimidir ve ölçtüğümüz bir şey değildir."),
            ("Sabitlenmiş yorumum nasıl beğeni alır?", "Sabitlenmiş yorum zaten en üsttedir. Ona beğeni kazandıran şey okumaya değer olmasıdır: bir devam, bir cevap, bir espri. Gerçek izleyiciler videoya bir şey kattığında onu beğenir."),
            ("Satın alınmış yorum beğenileri videoma yardım eder mi?", "Önemli olan hiçbir şekilde etmez. Videoyu hiç izlemeyen bir hesabın bir yoruma bıraktığı beğeni, videonun performansında hiçbir şeyi değiştirmez; tek bir yoruma gelen ani bir yığın da kolayca fark edilir."),
            ("Yorumlarıma en çok hareketi hangi paket getirir?", "Genellikle ayda {pro_comments} yorumla {pro_name}, ardından {rising_comments} yorumla {rising_name}. Daha çok yorum daha hareketli bir yorum bölümü demektir; hareketli yorum bölümleri de okunur."),
        ],
    },
    {
        "service": "likes",
        "modifier": "private-account",
        "slug": "tiktok/begeni/gizli-hesap",
        "label": "Gizli TikTok hesabına beğeni",
        "title": "Gizli TikTok Hesabına Beğeni Satın Alınır mı? | Growsterr",
        "description": "Gizli hesaba TikTok beğeni satın alınır mı? Gizli videoları yalnızca onayladığınız takipçiler görür, yeni insanlar beğenemez. İşe yarayan yol ise şu.",
        "h1": ("Gizli hesaba TikTok beğeni mi? ", "Önce insanların videoları görmesi gerekir."),
        "intro": "Gizli bir hesaba TikTok beğeni satın almak istiyorsanız, önce bilmeye değer bir engel var: gizli hesapta videolarınızı yalnızca onayladığınız takipçiler izleyebilir. Yeni insanlar onları göremez, dolayısıyla beğenemez. Paketlerimiz gerçek izleyiciler getirir; bu yüzden çalışırken herkese açık bir profile ihtiyaç duyar.",
        "hero": {"image": "tiktok-watch-time", "alt": "Yeni izleyicilerin izleyip beğenebilmesi için herkese açık yapılmış bir TikTok videosu"},
        "sections": [
            {
                "h2": "Gizli bir videoyu kim beğenebilir?",
                "p": [
                    "Gizli bir TikTok hesabında videolarınız yalnızca kabul ettiğiniz takipçilere ulaşır. Diğer herkes kilitli bir profil görür. Bir beğeni bir izlenme ister, bir izlenme de erişim ister; yani beğeniler yalnızca içeri aldığınız insanlardan gelebilir.",
                    "Bu, bir büyüme paketinin amacının tam tersidir. Kampanyalarımız sizi henüz tanımayan insanlara ulaşmak için vardır ve onlar yalnızca izlemelerine izin verilen şeyi beğenebilir.",
                ],
            },
            {
                "h2": "Özel anları olan herkese açık bir hesap",
                "ul": [
                    "Yeni insanlar sizi bulup gördüklerini beğenebilsin diye hesabı herkese açık yapın.",
                    "Kişisel videoları Arkadaşlar ya da Yalnızca ben ile sınırlayın; kampanyadan gelen ziyaretçiler onları görmez.",
                    "Daha fazla kontrol istiyorsanız tek tek videolarda düet, birleştirme ya da indirmeyi kapatın.",
                    "Sohbeti istediğiniz gibi tutmak için TikTok'un yorum filtrelerini kullanın.",
                ],
            },
            {
                "h2": "Herkese açık bir ay neler getirir?",
                "p": [
                    "Hesap herkese açıkken kampanyamızın getirdiği insanlar herkesle paylaştığınız her şeyi izleyebilir. {pick_name} ile bu genellikle ayda {pick_likes} beğeni eder; {pick_audience} yeni takipçiyle birlikte.",
                ],
            },
        ],
        "faqs": [
            ("Gizli yaptığım videolara beğeni gelir mi?", "Hayır. Arkadaşlar ya da Yalnızca ben olarak ayarlanan videoları yalnızca o kişiler görür; kampanyadan gelen ziyaretçiler onları izleyemez ve beğenemez. Yeni izleyicilerden yalnızca herkesin görebildiği videolar beğeni alır."),
            ("Ay bitince yeniden gizliye geçebilir miyim?", "Evet. Paketiniz bittiğinde yeniden gizliye geçebilirsiniz. Videolarınızdaki mevcut beğeniler kalır, ama yeni insanlar onları izleyemez."),
            ("Gizli kalıp yalnızca takipçilerimden beğeni alabilir miyim?", "Mevcut takipçileriniz istediklerini beğenebilir; onları buna zorlayamayız. Kampanyalarımız profilinizi yeni insanlara göstererek çalışır ve bu ancak onlar videolarınızı görebiliyorsa işe yarar."),
            ("Gizliden herkese açığa geçmek riskli mi?", "Bu sizin kontrol ettiğiniz ve geri alabileceğiniz bir ayar. Geçmeden önce hangi videoların herkese açık olduğuna bakın ve kişisel olan her şeyi Arkadaşlar ya da Yalnızca ben ayarına taşıyın."),
            ("Beğeni göndermek için birinin hesabıma erişmesi gerekir mi?", "Kimsenin gerekmemeli. Yalnızca kullanıcı adınızla çalışırız ve hesabınıza asla giriş yapmayız. Bir hizmet gizli bir hesaba beğeni getirmek için giriş bilgilerinizi istiyorsa, onları kendinize saklayın."),
        ],
    },
    {
        "service": "likes",
        "modifier": "live",
        "slug": "tiktok/begeni/canli-yayin",
        "label": "TikTok canlı yayın beğenisi",
        "title": "TikTok Canlı Yayın Beğenisi Satın Alınır mı? | Growsterr",
        "description": "TikTok canlı yayın beğenisi mi istiyorsunuz? Yayındaki dokunuşlar odadaki insanlardan gelir. Katılabilecek takipçileri büyütürüz, yayına beğeni göndermeyiz.",
        "h1": ("TikTok canlı yayın beğenisi mi? ", "Odayı doldurun, dokunuşlar gelir."),
        "intro": "TikTok canlı yayın beğenisi satın almak istiyorsanız, ne olduklarını bilmek işe yarar: şu an yayınınızı izleyen insanların ekrana dokunuşları. Canlı yayına dokunuş göndermiyoruz; gerçek olanını kimse gönderemez. Büyüttüğümüz şey katılabilecek kitledir: videolarınıza denk gelip onları kalacak kadar beğenen gerçek takipçiler.",
        "hero": {"image": "tiktok-likes", "alt": "Gerçek izleyicilerle bir TikTok canlı yayınında ekranda yükselen kalpler"},
        "sections": [
            {
                "h2": "TikTok canlı yayın beğenileri gerçekte neyi ölçer?",
                "p": [
                    "Canlı yayın beğenileri odanın nabzıdır. Bir izleyici istediği kadar dokunabilir; yani birkaç ilgili insanın olduğu bir yayın bol beğeni toplayabilir. Dokunuşların size ve uğrayan herkese gösterdiği şey, izleyenlerin keyif aldığıdır.",
                    "İzlemeyen hesaplardan gönderilen dokunuşlar böyle hiçbir şey göstermez. Sohbet sessiz kalır, kalpler ekranda olanla uyuşmaz ve katılan herkes bunu hisseder.",
                ],
            },
            {
                "h2": "Bir paket canlı yayınlarınıza nasıl yardım eder?",
                "p": [
                    "Odayı satın alamazsınız, ama içeri girebilecek insanların listesini büyütebilirsiniz. Kampanyalarımızın getirdiği her takipçi videolarınızı seçmiş biridir; takipçileriniz de her canlı yayının başladığı kitledir.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Ev stüdyosundan TikTok canlı yayınında izleyicilerle konuşan bir içerik üreticisi"},
            },
            {
                "h2": "Katılanlardan daha çok dokunuş almak",
                "ul": [
                    "Ekranda bir hedef koyun ya da dokunuşla oylama yapın ki izleyicilerin dokunmak için bir nedeni olsun.",
                    "Kalpler yükseldiğinde sesli tepki verin; insanlar karşılık bulduğunu gördüğünde daha çok dokunur.",
                    "İlk dakikaları canlı tutun; yeni gelenler kalıp kalmayacaklarına o zaman karar verir.",
                    "Müdavimlere adlarıyla teşekkür edin: topluluk gibi hissettiren bir oda, topluluk gibi dokunur.",
                ],
            },
        ],
        "faqs": [
            ("Şu an süren bir TikTok canlı yayını için beğeni satın alabilir miyim?", "Hayır. Bir yayına beğeni, izleyici ya da yorum göndermiyoruz. Gerçek insanlar bir canlı yayını gördüklerinde ve istediklerinde katılır; bunu kimse planlayamaz."),
            ("Paketleriniz canlı yayınlara beğeni getirir mi?", "Doğrudan değil. Paketler takipçi getirir, bir de videolarınıza beğeni ve yorum. O takipçilerin bazıları canlı yayınlarınıza katılıp dokunabilir; bu onlara kalmıştır ve biz bunu saymayız."),
            ("Canlı yayın beğenilerinin önemli olması için 1.000 takipçi gerekir mi?", "Canlı yayının kendisi, hesap 1.000 takipçiye ulaşana kadar kilitli kalır. Henüz orada değilseniz önce takipçilerinizi büyütün; canlı yayın beğenileri daha sonra, kalan insanlardan gelir."),
            ("Çok takipçim olmasına rağmen canlı yayın beğenilerim neden düşük?", "Hiç izlemeyen takipçiler yayınlara katılmaz. Sayı botlarla kurulduysa canlı yayın boş hissettirir. Dokunuşları getiren şey gerçek takipçiler, düzenli yayınlar ve canlı bir açılıştır."),
            ("Canlı yayın beğenileri yayınımı kimin göreceğini etkiler mi?", "TikTok hangi canlı yayınları göstereceğini tam olarak nasıl seçtiğini açıklamıyor; ama insanların kaldığı, sohbet ettiği ve dokunduğu bir oda ona üzerinde çalışabileceği bir şey verir. Sessiz hesaplarla dolu bir oda vermez."),
        ],
    },
    # --- Views: the ways people ask for them --------------------------------------------------
    {
        "service": "views",
        "modifier": "real",
        "slug": "tiktok/izlenme/gercek",
        "label": "Gerçek TikTok izlenme",
        "title": "Gerçek TikTok İzlenme Satın Al: Ölçülebilir Kalite | Growsterr",
        "description": "Yazılımdan değil insanlardan gerçek TikTok izlenmesi: izleyen, profilinizi açan, isterse takip eden izleyiciler. Kalite, her izlenmede bir insan.",
        "h1": ("Gerçek TikTok izlenme satın alın, ", "oynat tuşuna kendisi basan insanlardan."),
        "intro": "Bir Growsterr paketiyle gerçek TikTok izlenme satın aldığınızda insanlara ödeme yaparsınız: profilinizi keşfeden, oynat tuşuna kendisi basan ve videonuz onları tuttuğu sürece izleyen gerçek izleyicilere. Kalite, seçtiğiniz bir kademe değildir. Her izlenmenin arkasında bir insan olduğunda elde ettiğiniz şeydir.",
        "hero": {"image": "tiktok-watch-time", "alt": "Bir içerik üreticisinin TikTok videosunda oynat tuşuna basan gerçek bir izleyici"},
        "sections": [
            {
                "h2": "TikTok izlenmelerinin kalitesi nasıl ölçülür?",
                "ul": [
                    "İzlenme süresi: gerçek izleyiciler video iyiyse kalır, değilse çıkar.",
                    "Profil ziyaretleri: bir videodan keyif alanlar daha fazlasını görmek için profilinizi açar.",
                    "Takip ve beğeniler: bazı izleyiciler daha fazlasını ister ve bunu gösterir.",
                    "Yorumlar: gerçek bir kitle kendi cümleleriyle karşılık verir.",
                    "Paylaşımlar: hepsinin en net işareti; bunu yalnızca insanlar yapar.",
                ],
            },
            {
                "h2": "Gerçek izlenmeler profilinizde başlar",
                "p": [
                    "Kampanyalarımız profilinizi iş ortağı ağımızdaki gerçek izleyicilerle tanıştırır. Merak edenler onu TikTok'ta açıp izlemeye başlar; izlenmeleriniz de oradan gelir. Profil ziyaretlerini ölçmemizin nedeni de bu: bir ziyaret, gelen bir insandır ve izlenmeler onu izler.",
                    "Yüksek hacimli izlenmeler bu adımı atlar. Tek bir video bağlantısına yönlendirilir, bir yazılım tarafından oynatılır ve bir saniye içinde biter.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Yeni izleyicilerin açıp videolarına göz attığı bir içerik üreticisinin TikTok profili"},
            },
        ],
        "faqs": [
            ("Gerçek izlenme ile yüksek kaliteli izlenme arasındaki fark ne?", "Bizim için yok. Gerçek bir izlenme izlemeyi seçen bir insandan gelir; önemli olan tek kalite budur. İzlenme paketlerindeki kalite etiketleri genellikle yalnızca hesapların profil fotoğrafı olduğu anlamına gelir."),
            ("Getirdiğiniz izlenmeleri bana gösterebilir misiniz?", "Ölçtüğümüzü gösteririz: kampanyadan profilinize gelen günlük ziyaretler ve bunların takibe dönüşen kısmı. İzlenmeleriniz, izlenme süresiyle birlikte TikTok'un kendi analizlerinde görünür."),
            ("Gerçek izlenmeler diğer izlenmelerle aynı mı sayılır?", "İzlenme sayısında izlenme izlenmedir. Fark, çevresindeki her şeydedir: gerçek izleyiciler izler, tepki verir ve bazen takip eder; bir videonun daha çok kişiye ulaşmasına yardım eden de budur."),
            ("Neden takipçisiz izlenme satmıyorsunuz?", "Çünkü gerçek izleyiciler parça parça gelmez. İzleyen aynı kişi beğenebilir, yorum yapabilir ya da takip edebilir; bu yüzden bir oynatma sayısı değil insan getiririz ve hepsi tek bir paketin içinde gelir."),
            ("Gerçek izlenmeler satın alınanlardan daha mı yavaş?", "Evet. İnsanlar ayın her günü, gün boyunca gelir. İnsanların bir videoyu bulabileceğinden hızlı gelen hiçbir şey insan değildir."),
        ],
    },
    {
        "service": "views",
        "modifier": "organic",
        "slug": "tiktok/izlenme/organik",
        "label": "Organik TikTok izlenme",
        "title": "Organik TikTok İzlenme, Seçtiğiniz Yerden | Growsterr",
        "description": "Organik TikTok izlenme satın alın: kitlenizin yaşadığı şehir, bölge ya da ülkeden gerçek izleyiciler profilinizi bulur ve istedikleri için izler.",
        "h1": ("Organik TikTok izlenme satın alın, ", "kitlenizin yaşadığı yerdeki insanlardan."),
        "intro": "Bir anlam taşıyan organik TikTok izlenmesi için iki şey önemlidir: gerçek bir insan izlemeyi seçmiştir ve doğru insandır. Paketlerimiz ikisini de halleder. Profilinizi seçtiğiniz yerdeki gerçek insanlara yöneltiriz; izlenmeler de durup izleyenlerden gelir.",
        "hero": {"image": "tiktok-watch-time", "alt": "Tek bir şehirdeki insanların yerel bir içerik üreticisinin TikTok videolarını izlemesi"},
        "sections": [
            {
                "h2": "Konuma göre hedefli TikTok izlenmesi",
                "p": [
                    "Antalya'daki bir restoranın Antalya'dan izlenmeye ihtiyacı vardır. Almanca içerik üreten biri Almanca anlayan izleyiciler ister. Yalnızca Türkiye içine kargo gönderen bir dükkân, başka bir kıtadan gelen izlenmeden pek bir şey kazanmaz. Yeri seçmek, izlenmeleri değerli kılmanın en basit yoludur.",
                    "Siparişinizde bir şehir, bölge ya da ülke belirtin; kampanya oradan başlar.",
                ],
            },
            {
                "h2": "Bir izlenmeyi organik yapan nedir?",
                "ul": [
                    "İzleyiciye izlemesi için ödeme yapılmadı, rica edilmedi, yazılımla izletilmedi.",
                    "Videonuza profilinizden ulaştı ve oynat tuşuna kendisi bastı.",
                    "Kaydırıp geçebilirdi, ama geçmedi.",
                    "Sonra ne yapacağı, beğeni, takip, paylaşım ya da hiçbir şey, ona kalmıştır.",
                ],
            },
            {
                "h2": "Doğru yerden gelen izlenmeler neden daha ileri gider?",
                "p": [
                    "Doğru yerden gelen izlenmeler gerisini de getirir: cevap verebileceğiniz bir dilde yorumlar, kapınızdan gerçekten girebilecek insanlardan takipler, yakında yaşayan arkadaşlara paylaşımlar. Dünyanın öbür ucundan, önemsemek için hiçbir nedeni olmayan bir izlenme bunların hiçbirini getirmez.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Şehrindeki müşteriler için TikTok videosu çeken küçük bir işletme sahibi"},
            },
        ],
        "faqs": [
            ("TikTok izlenmelerini ülkeye göre hedefleyebilir miyim?", "Evet, şehir ya da bölgeye göre de. Sipariş verirken yeri belirtin; oradaki insanlar profilinizi önce görür. En iyi eşleşme biraz daha genişse, izleyicilerin bir kısmı çevresinden gelebilir."),
            ("Hedefli izlenmeler yine organik mi?", "Evet. Profilinizi kimin göreceğini seçmek, kimin izleyeceğini seçmek değildir. O yerdeki her insan, videonuzun zamanına değip değmeyeceğine kendisi karar verir."),
            ("Kitlem birkaç ülkedeyse ne olur?", "Onları kapsayan bölgeyi ya da en önemli ülkeyi belirtin. Daha özel bir şeye ihtiyacınız varsa sipariş vermeden önce bize yazın."),
            ("İzlenmeler kitlemin saat dilimini izler mi?", "Gerçek insanlar uyanıkken gezinir; bu yüzden seçtiğiniz yerden gelen izlenmeler oranın gündüzünü izleme eğilimindedir. Bot izlenmeleri sizin orada saatin kaç olduğunu umursamaz."),
            ("Organik izlenmeler takipçiyle birlikte mi gelir?", "Evet. İzleyenler, takip edenlerle aynı insanlardır: {pick_name} ile genellikle ayda {pick_audience} yeni takipçi, beğenileri ve yorumlarıyla birlikte."),
        ],
    },
    {
        "service": "views",
        "modifier": "monthly",
        "slug": "tiktok/izlenme/aylik",
        "label": "Her videoya TikTok izlenme",
        "title": "Birden Çok Videoya Aylık TikTok İzlenme | Growsterr",
        "description": "Tek bir aylık paketle birden çok videoya TikTok izlenme: gerçek insanlar profilinize göz atar ve ay boyunca dikkatlerini çeken her videoyu izler.",
        "h1": ("Birden çok videoya TikTok izlenme satın alın, ", "ay boyunca, gerçek insanlardan."),
        "intro": "Her video için ayrı sipariş vermeden birden çok videoya TikTok izlenme mi almak istiyorsunuz? Aylık bir paket bütün profilinizi kapsar. Gerçek insanlar sizi her gün keşfeder ve profilinize geldiklerinde birden fazla video izler: en yenisini, sabitlenmiş olanları, dikkatlerini çeken neyse onu. İzlenmeler zamanla, paylaştığınız her şeyde birikir.",
        "hero": {"image": "tiktok-watch-time", "alt": "Bir içerik üreticisinin TikTok profilinde birkaç video arasında gezinen bir izleyici"},
        "sections": [
            {
                "h2": "Tek paket, her video",
                "p": [
                    "Video başına izlenme paketleri sizi seçim yapmaya zorlar: bu yardım alır, şu almaz, gelecek hafta yine sipariş verirsiniz. Aylık paket profiliniz düzeyinde çalışır. Ay içinde paylaştığınız her video, daha önce paylaştıklarınızla birlikte, getirdiğimiz insanlar için oradadır.",
                    "{rising_name} ve {pro_name} ayrıca en çok ilgiyi hangi videoların göreceğini belirlemenizi sağlar.",
                ],
            },
            {
                "h2": "TikTok otomatik izlenme ve neden yapmıyoruz",
                "p": [
                    "Otomatik izlenme, her yeni videoya yüklendiği an sabit sayıda oynatma gönderir. En iyisi de olsa en zayıfı da olsa her video aynı artışı alır ve bu oynatmaların hiçbiri bir izleyiciyle gelmez. Fark edilmesi kolay bir desendir.",
                ],
            },
            {
                "h2": "Zamanla daha çok izlenme almak",
                "ul": [
                    "En güçlü üç videonuzu sabitleyin; sabitlenmiş videolar profilinizde ilk sırada durur.",
                    "Bir seri yapın ki insanların bir sonraki ve bir önceki bölümü izlemek için nedeni olsun.",
                    "Profilinizi derli toplu, biyografinizi net tutun; ziyaretçiler ne bulacaklarını bilsin.",
                    "Yeni insanlar gelmeye devam ettikçe eski videolar da izlenme kazanmaya devam eder.",
                ],
            },
        ],
        "faqs": [
            ("Paket paylaştığım her videoyu kapsar mı?", "Evet. Kampanya insanları tek bir bağlantıya değil, profilinize getirir; yani oradaki herkese açık her şey izlenebilir. Yeni videolar genellikle en çoğunu alır, çünkü ziyaretçilerin gördüklerinin en üstündedirler."),
            ("İzlenmeler videolarım arasında nasıl dağılır?", "İzleyicilere göre. İlgilerini çekeni izlerler, bu yüzden en güçlü videolarınız daha fazlasını toplar. Aralarında bir sayıyı bölüştürmüyoruz, çünkü ortada bir sayı yok."),
            ("Eski videolar izlenme almaya devam eder mi?", "Yeni insanlar profilinizi keşfettiği sürece evet. Her ay, daha önce paylaştıklarınıza geri kaydırabilecek taze bir kitle getirir."),
            ("Bu, TikTok otomatik izlenmeyle aynı şey mi?", "Hayır. Otomatik izlenme her yeni gönderiye kendiliğinden oynatma yollar. Bizim paketimiz kendiliğinden yenilenir, ama izlenmeler izlemeyi seçen insanlardan gelir."),
            ("Birden fazla TikTok hesabı için izlenme alabilir miyim?", "Her paket bir hesabı büyütür. Birden fazla hesabınız varsa her biri için bir paket başlatın; hepsi aynı Growsterr hesabında durur."),
        ],
    },
    {
        "service": "views",
        "modifier": "gradual",
        "slug": "tiktok/izlenme/kademeli",
        "label": "Kademeli TikTok izlenme",
        "title": "Yavaş TikTok İzlenme: Doğal Bir Günlük Akış | Growsterr",
        "description": "TikTok izlenmeyi zamanlayıcı olmadan, yavaşça alın: gerçek insanlar her gün profilinize denk gelir ve aylık bir paketin içinde kendi hızında izler.",
        "h1": ("Yavaş TikTok izlenme satın alın, ", "her seferinde bir gerçek izleyici."),
        "intro": "TikTok izlenmeyi doğal görünsün diye yavaş yavaş mı satın almak istiyorsunuz? Damla damla gönderimi unutun. Doğal görünen izlenmeler insanlardan gelen izlenmelerdir. Paketlerimiz ayın her günü profilinize gerçek izleyiciler getirir; onlar da videolarınızı bulduklarında, insanların gerçekten gezindiği hızda izler.",
        "hero": {"image": "tiktok-watch-time", "alt": "Gerçek insanlar bir içerik üreticisinin videolarını buldukça gün gün biriken TikTok izlenmeleri"},
        "sections": [
            {
                "h2": "Gerçek izlenmelerin şekli",
                "p": [
                    "Gerçek izlenmeler düz bir çizgide gelmez. Bir video önce onu erken görenlerden bir ilk dalga alır, sonra günler ya da haftalar sonra profilinizde bulan izleyicilerden uzun bir kuyruk. Her yeni takipçi, bütün eski videolarınız için yeni bir izleyicidir.",
                    "Damla damla gönderilen izlenmeler bu şekli düzgün bir rampaya çevirir: saatte belirli sayıda, bir saniye sonra çıkan hesaplardan. Yavaş görünür ama gerçek görünmez.",
                ],
            },
            {
                "h2": "Her şeyle birlikte hareket eden izlenmeler",
                "ul": [
                    "İzlenmeler arttığında beğeni ve takipler de onunla artar, çünkü üçünü de aynı insanlar yapar.",
                    "Yeni insanlar profilinizi keşfettikçe eski videolarınız izlenmeye devam eder.",
                    "Her içerik üreticisinde olduğu gibi yoğun günlerle sakin günler birbirini izler.",
                ],
            },
            {
                "h2": "Bizim ölçtüğümüz ve TikTok'un ölçtüğü",
                "p": [
                    "İzlenmeleri önceden saymıyoruz, sayıyormuş gibi de yapmıyoruz. Paneliniz sistemimizin ölçtüklerini gösterir: kampanyadan gelen profil ziyaretleri ve bunların dönüştüğü takipçiler, gün gün. TikTok'un kendi analizleri izlenmelerinizi gösterir; arkalarında gerçek insanlar olduğunda ikisi aynı hikâyeyi anlatır.",
                ],
            },
        ],
        "faqs": [
            ("Videolarım günde kaç izlenme alır?", "Bu, bizden çok videolarınıza bağlı. Profilinize düzenli bir gerçek insan akışı getiririz; kaç video izleyecekleri ve ne sıklıkla, onların seçimidir."),
            ("İzlenmelerim neden eşit değil de dalga dalga geliyor?", "Çünkü insanlar eşit gezinmez. Akşamlar, hafta sonları ve yeni bir video daha yoğun günler yaratır. Her saat eşit bir izlenme akışı, bir makinenin ürettiği şeydir."),
            ("Eski videolar da izlenme alır mı?", "Çoğu zaman. Bir videoyu beğenen insanlar genellikle profilinizi açıp daha fazlasını izler. Gerçek bir kitlenin bıraktığı en iyi işaretlerden biri budur."),
            ("İzlenmeleri belirli videolara yayabilir miyim?", "{rising_name} ya da {pro_name} ile kampanyanın hangi videolara öncelik vereceğine siz karar verirsiniz; getirdiğimiz insanlar yine kendi hızında izler."),
            ("Hız aydan aya değişir mi?", "Biraz. Her ay yeni insanlar getirir; paylaştıklarınız da ne kadar izleyeceklerini belirler. Güçlü videolarla geçen bir ay genellikle daha yoğun hissettirir."),
        ],
    },
    {
        "service": "views",
        "modifier": "no-drop",
        "slug": "tiktok/izlenme/dusmeyen",
        "label": "Düşmeyen TikTok izlenme",
        "title": "Düşmeyen TikTok İzlenme: Gerçek Oynatmalar Kalır | Growsterr",
        "description": "Düşmeyen TikTok izlenme: gerçek insanların izlenmeleri sıradan oynatmalardır ve sayılmaya devam eder. Düşmemek telafiyle değil, gerçek izleyiciyle başlar.",
        "h1": ("Düşmeyen TikTok izlenme satın alın: ", "izlemiş insanlarla başlayın."),
        "intro": "Düşmeyen TikTok izlenme satın almak istiyorsanız, izlenmelerin neden düştüğüne bakın: hiçbir zaman gerçek oynatma değillerdi ve TikTok onları geri aldı. Paketlerimiz videolarınızı izleyen gerçek insanlar getirir; onların izlenmeleri sıradan izleyicilerden gelen sıradan izlenmelerdir. Geri alınacak bir şey yoktur.",
        "hero": {"image": "tiktok-watch-time", "alt": "Gerçek insanlar izlediği için rakamlarını koruyan bir TikTok izlenme sayısı"},
        "sections": [
            {
                "h2": "Bazı izlenme sayıları neden düşer?",
                "p": [
                    "TikTok sahte etkileşimi platformundan uzak tutmaya çalışır; gerçek olmayan oynatmaları ya da arkalarındaki hesapları sildiğinde sayı düzeltilir. Bir videonun bir gün ertesi günden daha fazla izlenme göstermesinin nedeni budur. Bir oynatma paketine yapıştırılan düşmez etiketi, oynatmaların ne olduğunu değiştirmez.",
                ],
            },
            {
                "h2": "Bir izlenmeyi kalıcı yapan nedir?",
                "ul": [
                    "Gerçek bir insan, kendi telefonunda, kendi seçimiyle oynat tuşuna bastı.",
                    "Videonuzu bir yazılıma verilen bir bağlantıdan değil, profilinizden buldu.",
                    "İzlenmesi, birbiriyle anlamlı duran beğeni, takip ve yorumlarla birlikte gelir.",
                ],
            },
            {
                "h2": "Gerçekten düşmeyen izlenmelerin dürüst hali",
                "p": [
                    "Bir sayının asla oynamayacağına söz vermeyiz, çünkü TikTok kendi sayımını yapar. Söyleyebileceğimiz şu: getirdiğimiz her izlenme, bir insanın izlemeye kendi verdiği karardır; bir temizliğin dokunması için hiçbir nedeni olmayan tek izlenme türü.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Bir ay boyunca gerçek insanlardan izlenme aldıktan sonra TikTok analizlerine bakan bir içerik üreticisi"},
            },
        ],
        "faqs": [
            ("Kampanyadan sonra izlenmelerim düşer mi?", "Gerçek insanlardan gelen izlenmeler diğer her izlenme gibi sayılır; paketiniz bittiğinde kaybolmaları için bir neden yok. Yeni insanlar gelmeyi bırakınca izlenmeleriniz yalnızca daha yavaş artar."),
            ("Diğer sitelerdeki düşmeyen izlenmeler neden yine düşüyor?", "Çünkü düşmez etiketi izlenmeleri değil, bir umudu anlatır. Oynatmalar bottan ya da yazılımdan geldiyse, etiket ne derse desin silinebilir."),
            ("İzlenmelerimin ne kadarı kalır?", "Gerçek insanların size verdiği her biri. İzlenmeleri önceden saymıyoruz, çünkü her insanın kaç video izleyeceğine bağlıdır; ama her biri gerçek bir insandan gelir."),
            ("Bir videoyu silip yeniden paylaşırsam izlenmeler kalır mı?", "Hayır. Silinen bir video, kim vermiş olursa olsun izlenmelerini de götürür. Yeniden paylaşım sıfırdan başlar; bu yüzden bir videoyu yayında tutup insanların onu bulmaya devam etmesine izin vermek genellikle daha iyidir."),
            ("Gerçek izlenmeler beğeniyle de gelir mi?", "Evet. Aynı izleyiciler istediklerinde beğenir, yorum yapar ve takip eder; {pick_name} ile bu genellikle ayda {pick_likes} beğeni ve {pick_comments} yorum eder."),
        ],
    },
    {
        "service": "views",
        "modifier": "safe",
        "slug": "tiktok/izlenme/guvenilir",
        "label": "Güvenilir TikTok izlenme",
        "title": "Güvenli TikTok İzlenme: Bot ve Giriş Olmadan | Growsterr",
        "description": "TikTok izlenme almak güvenli mi? Bot izlenmeleri analizlerinizi bulandırır ve silinebilir. Gerçek izleyici, giriş yok, Stripe ile ödeme: güvenli ve meşru.",
        "h1": ("TikTok izlenmeyi güvenle satın alın: ", "hesabınızı da analizlerinizi de temiz tutun."),
        "intro": "TikTok izlenmeyi güvenle satın almak için şifrenizden fazlasını düşünün. Bot izlenmeleri analizlerinizi de çarpıtır; artık hangi videoların işe yaradığını anlayamazsınız. Paketlerimiz profilinizi keşfedip kendi istekleriyle izleyen gerçek insanlar getirir. Giriş yok, yazılım yok, hesabınıza dokunan hiçbir şey yok; analizlerinizdeki rakamlar dürüst kalır.",
        "hero": {"image": "tiktok-watch-time", "alt": "Gerçek insanlardan gelen izlenme ve izlenme süresini gösteren temiz TikTok analizleri"},
        "sections": [
            {
                "h2": "Güvensiz izlenmelerin gizli bedeli",
                "p": [
                    "TikTok analizleriniz öğrenme aracınızdır: hangi açılışlar insanları tutuyor, hangi sesler işe yarıyor, hangi konular takipçi getiriyor. Bot izlenmeleri hepsine gürültü doldurur. Ortalama izlenme süresi çöker, trafik kaynakları anlamsızlaşır ve sonunda yalnızca işe yaramış gibi görünen videoyu taklit edersiniz.",
                ],
            },
            {
                "h2": "Bu, TikTok izlenme almanın meşru bir yolu mu?",
                "p": [
                    "İzlenmeyi bir ürün olarak satmıyoruz. Gerçek insanların profilinize denk geldiği tanıtım kampanyaları olarak yürütülen aylık bir büyüme paketi satıyoruz. İzlenmeler, o insanların videolarınızı beğendiklerinde yaptıkları şeydir. Meşru olan budur: görünmek için ödersiniz, gerisine insanlar karar verir.",
                ],
            },
            {
                "h2": "Neler güvende kalır?",
                "ul": [
                    "Giriş bilgileriniz: asla elinizden çıkmaz, çünkü bir kullanıcı adı yeterlidir.",
                    "Ödemeniz: kart, Apple Pay ya da Google Pay ile Stripe'ın güvenli ödeme sayfası.",
                    "Çıkışınız: istediğiniz zaman hesabınızdan iptal edin, ödediğiniz ayın kalanını kullanın.",
                    "Verileriniz: insanlardan gelen izlenme ve izlenme süresi; onlardan öğrendikleriniz doğru olur.",
                ],
            },
        ],
        "faqs": [
            ("İzlenme satın almak videolarımı riske atar mı?", "Kendi istekleriyle izleyen insanlar getiririz; hesabınızın içinde asla bir şey yapmaz, yazılımla oynatma göndermeyiz. TikTok kendi kararlarını verir, ama herkese açık videoları izleyen gerçek izleyiciler, uygulamanın tam olarak var olma nedenidir."),
            ("İzlenme göndermek için TikTok hesabıma erişiminiz gerekir mi?", "Hayır. İzlenmeler profilinizi açıp oynat tuşuna basan insanlardan gelir; bunun için sizden herkese açık bir hesap ve kullanıcı adınız dışında hiçbir şey gerekmez."),
            ("Ucuz izlenme paketleri neden riskli?", "Ucuzdurlar, çünkü kimse izlemiyordur. Bu oynatmalar silinebilir, ortalama izlenme sürenizi aşağı çeker ve analizlerinizi bir sonraki paylaşıma karar vermek için işe yaramaz hale getirir."),
            ("İzlenmelerin gerçek olduğunu nasıl anlarım?", "Yanlarında ne geldiğine bakın. Gerçek izlenmeler profil ziyaretleri, beğeniler, takipler ve arada bir yorum getirir; analizleriniz de izleyicilerin hepsinin aynı saniyede çıkması yerine farklı sürelerde kaldığını gösterir."),
            ("İçim rahat etmezse durdurabilir miyim?", "Evet, istediğiniz zaman hesabınızdan. Başka ödeme alınmaz ve içinde bulunduğunuz ay son gününe kadar sürer."),
        ],
    },
    {
        "service": "views",
        "modifier": "fyp",
        "slug": "tiktok/izlenme/kesfet",
        "label": "TikTok izlenme ve keşfet sayfası",
        "title": "TikTok Keşfet İçin İzlenme: Ne İşe Yarar? | Growsterr",
        "description": "TikTok izlenmesi sizi keşfete çıkarır mı? Sana Özel sayfasında yer satın alınamaz, vaat edilemez. Videoyu taşıyan, gerçek izleyicilerin onunla yaptıklarıdır.",
        "h1": ("Keşfet için TikTok izlenme: ", "bir videoyu gerçekte ne taşır?"),
        "intro": "Keşfet için TikTok izlenme satın almak genellikle tek bir şey demektir: bir videonuzun Sana Özel sayfasına, yani keşfete düşmesini istiyorsunuz. O yeri size kimse satamaz, biz de dahil. Bizim yapabileceğimiz, gün be gün profilinize gerçek insanlar göndermek; onların videolarınızla yaptıkları, yani izlemek, paylaşmak ve takip etmek, TikTok'un kullandığını söylediği türden sinyallerdir.",
        "hero": {"image": "tiktok-watch-time", "alt": "Bir TikTok videosunu sonuna kadar izleyip paylaşan izleyiciler"},
        "sections": [
            {
                "h2": "Sana Özel sayfasını neden kimse satamaz?",
                "p": [
                    "Sana Özel sayfası bir videonun konulduğu bir yer değildir. Herkes için farklıdır; her izleyicinin izlediği, beğendiği, paylaştığı ve atladığı şeylerden oluşur. TikTok onlar için video video seçer ve satın alınacak bir koltuk yoktur.",
                    "Yani bir hizmet keşfet izlenmesi sattığında oynatma satıyordur, genellikle botlardan. Kimsenin izlemediği oynatmalar TikTok'u kimsenin daha fazlasını görmek istediğine ikna edemez.",
                ],
            },
            {
                "h2": "TikTok neye baktığını söylüyor?",
                "p": [
                    "TikTok önerilerini neyin beslediğini anlattı ve bunların hiçbiri satın alınabilecek bir sayı değil:",
                ],
                "ul": [
                    "İnsanların nasıl etkileşime girdiği: neyi izledikleri, beğendikleri, paylaştıkları, yorumladıkları ve takip ettikleri.",
                    "Videonun kendi ayrıntıları: açıklamalar, sesler ve hashtag'ler.",
                    "Dil ve konum gibi ayarlar.",
                ],
            },
            {
                "h2": "TikTok'ta viral olmak, dürüstçe",
                "p": [
                    "Kimse viral bir video vaat edemez. Paylaşım ve kaydetmeler, bir izleyici bir arkadaşının bir şeyi görmesini ya da onu yeniden görmeyi istediğinde olur; bunları gerçek insanlardan kimse sipariş edemez. İstikrarlı büyümenin size verdiği şey daha çok şanstır: her videoyu gören daha çok gerçek insan, onu doğru anda paylaşabilecek daha çok kişi. Video yine de bunu hak etmelidir. Güçlü bir açılış, uyan bir ses ve tekrar izlemeye değer bir kapanış, satın alabileceğiniz her sayıdan fazlasını yapar.",
                ],
                "image": {"image": "tiktok-creator", "alt": "Paylaşmadan önce bir TikTok videosu için farklı sesleri deneyen bir içerik üreticisi"},
            },
        ],
        "faqs": [
            ("Paketiniz videomu keşfete çıkarır mı?", "Buna söz veremeyiz, dürüst olan kimse de veremez. Profilinize gerçek izleyiciler getiririz; izler, paylaşır ve takip ederlerse TikTok'un videonuzu onlara benzeyen daha çok insana göstermesi için nedenleri olur."),
            ("İzlenmeler bir videonun keşfete düşmesine yardım eder mi?", "Tek başına etmez. Bir saniye sonra duran bir oynatma, TikTok'a videonun dikkati tutmadığını söyler. Sonuna kadar izlemek, tekrar izlemek, paylaşmak ve kaydetmek çok daha önemlidir ve bunları yalnızca insanlar yapar."),
            ("Paylaşım ya da kaydetme satın alabilir miyim?", "Hayır. Paylaşım ve kaydetmeler, bir videoyu birine gönderecek ya da saklayacak kadar beğenen gerçek izleyicilerden gelir. Videolarınız hak ettiğinde paketle birlikte gelirler; onları asla ayrıca saymaz ya da satmayız."),
            ("TikTok'ta nasıl viral olurum?", "Bir düğmesi yok. Sık paylaşım yapın, izleyicileri ilk saniyelerde yakalayın, videoya uyan sesler kullanın ve insanların bir arkadaşına göndermek isteyeceği şeyler üretin. Gerçek izleyiciler her videoya daha çok şans verir; gerisi video ve biraz da şanstır."),
            ("#keşfet ya da #fyp etiketi işe yarar mı?", "TikTok hashtag'leri okur, ama #fyp ya da #keşfet videonuzun ne hakkında olduğunu söylemez. Konunuzu anlatan bir hashtag, doğru insanların onu bulmasına yardım eder."),
            ("Tek bir video için en çok hangi paket işe yarar?", "{rising_name} ya da {pro_name} ile önemli videoları seçebilirsiniz; böylece inandığınız video ziyaretçilerimizin daha fazlasının önüne çıkar. Sonrasında ne kadar yol alacağı izleyenlere kalmıştır."),
        ],
    },
    {
        "service": "views",
        "modifier": "high-retention",
        "slug": "tiktok/izlenme/izlenme-suresi",
        "label": "Yüksek izlenme süreli TikTok izlenme",
        "title": "Yüksek İzlenme Süreli TikTok İzlenme, Dürüstçe | Growsterr",
        "description": "Yüksek izlenme süreli TikTok izlenmesi mi? Süre, izlemeye devam eden insanlardan gelir. İzleyiciyi biz getiririz; açılışınız ve temponuz onu tutar.",
        "h1": ("Yüksek izlenme süreli TikTok izlenme mi? ", "Önce izleyici, sonra bitirmeye değer bir video."),
        "intro": "Yüksek izlenme süreli TikTok izlenme satın almak istiyorsanız sırrı zaten biliyorsunuz: TikTok'ta kaç kişinin başladığı değil, insanların ne kadar izlediği önemlidir. Ancak izlenme süresi satılamaz; izlemeye devam etmeye karar veren bir insandır. Bizim işimiz gerçek insanları profilinize getirmek; onları sonuna kadar tutmak videonuzun işi.",
        "hero": {"image": "tiktok-watch-time", "alt": "Bir TikTok videosunun son saniyelerinde hâlâ izlemeye devam eden bir izleyici"},
        "sections": [
            {
                "h2": "Yüksek izlenme süreli izlenmeler genellikle nedir?",
                "p": [
                    "Biri yüksek izlenme süreli izlenme sattığında, geçip gitmeden önce belirli bir saniye boyunca oynayacak şekilde programlanmış oynatmaları kasteder. İzlenme süresi yalnızca bir ekranın onu oynatması anlamında gerçektir. Kimse görmedi, kimse gülmedi, kimse paylaşmadı; diğer rakamlarınız da bunu gösterir.",
                ],
            },
            {
                "h2": "Gerçekten artırabileceğiniz izlenme süresi",
                "ul": [
                    "Çoğu izleyicinin karar verdiği ilk bir iki saniyede sadede gelin.",
                    "Süreyi fikre göre ayarlayın: hızlı bir espri bir dakika sürmemeli.",
                    "Havaya uyan bir ses seçin ve sesinizi bastırmasına izin vermeyin.",
                    "Sesi kapalı izleyenler için altyazı ekleyin.",
                    "Tekrar izlemeyi doğal hissettiren bir kapanış yapın.",
                ],
                "image": {"image": "tiktok-creator", "alt": "İzleyicileri tutmak için bir TikTok videosunun ilk saniyelerini kırpan bir içerik üreticisi"},
            },
            {
                "h2": "Kendi izlenme sürenizi okuyun",
                "p": [
                    "TikTok analizleri ortalama izlenme sürenizi ve videoyu kaç izleyicinin tamamen izlediğini gösterir. Her paylaşımdan sonra bakın. Kampanyamız aracılığıyla videolarınızı gerçek insanlar bulduğunda bu rakamlar dürüst olur ve hangi videoların yabancıları tuttuğunu, hangilerinin tutmadığını görürsünüz.",
                ],
            },
        ],
        "faqs": [
            ("Belirli bir izlenme süresiyle izlenme teslim edebilir misiniz?", "Hayır. Her izlenme gerçek bir insandan gelir ve video onu tuttuğu sürece izler. Belirli bir izlenme süresi, kimsenin gerçekten izlemediği anlamına gelirdi."),
            ("Gerçek izleyiciler videomun tamamını izler mi?", "Videoya göre bazıları izler, bazıları izlemez. Onların izlenme süresinin değerli olmasının nedeni tam da bu: size ve TikTok'a neyin işe yaradığını söyler."),
            ("Uzun videoların izlenme süresi daha mı kötü olur?", "Her zaman değil. Uzunluğunu hak eden uzun bir video insanları iyi tutabilir. Zarar veren, fikrin taşıyamadığı uzunluktur."),
            ("İzlenme süresi beğeniden daha mı önemli?", "Birbirine bağlılar. Sonuna kadar izleyenler beğenme, yorum yapma ve paylaşma ihtimali en yüksek olanlardır; gerçek izleyiciler hepsini birden verir."),
            ("Videolarıma en çok izleyiciyi hangi paket getirir?", "{pro_name} profilinize en çok insanı getirir, genellikle ayda {pro_audience} yeni takipçi; üstüne öncelikli yerleşim ve ilginin hangi videolara gideceğini seçme imkânı ekler."),
        ],
    },
    {
        "service": "views",
        "modifier": "live",
        "slug": "tiktok/izlenme/canli-yayin",
        "label": "TikTok canlı yayın izleyicisi",
        "title": "TikTok Canlı Yayın İzleyicisi Satın Alınır mı? | Growsterr",
        "description": "TikTok canlı yayın izleyicisi mi arıyorsunuz? Gerçek insanlar bir yayına rezerve edilemez. Yayınlarınızın dayandığı takipçileri büyütürüz, bot getirmeyiz.",
        "h1": ("TikTok canlı yayın izleyicileri ", "önemseyen takipçilerden gelir."),
        "intro": "TikTok canlı yayın izleyicileri şu an odada olan insanlardır ve gerçek olanlarını kimse bir takvime göre teslim edemez. Bu yüzden canlı yayın izlenmesi ya da izleyicisi satmıyoruz. Katılabilecek kitleyi büyütürüz: ayın her günü videolarınızı keşfedip takip eden gerçek insanlar. Canlı yayına geçtiğinizde gelebilecek olanlar onlardır.",
        "hero": {"image": "tiktok-creator", "alt": "Gerçek izleyiciler katılıp sohbet ederken TikTok canlı yayını yapan bir içerik üreticisi"},
        "sections": [
            {
                "h2": "Satın alınan canlı yayın izleyicileri bir yayını neden kötüleştirir?",
                "p": [
                    "Sohbeti boş, izleyici sayısı yüksek bir yayın, uğrayan herkese bir şeylerin yolunda olmadığını söyler. Satın alınan izleyiciler odada konuşmadan, hediye göndermeden ya da yayını paylaşmadan oturur. Herkesin gördüğü tek sayıyı şişirir, bir canlı yayını ayakta tutan sayıları ise aç bırakırlar.",
                ],
            },
            {
                "h2": "Takipçileri canlı yayın izleyicisine dönüştürmek",
                "ul": [
                    "Yayını önceden bir canlı yayın etkinliği olarak planlayın ki takipçiler hatırlatıcı kurabilsin.",
                    "Bir gün önceki videolarınızda saati söyleyin.",
                    "Her hafta aynı saatte yayına geçin ki takipçileriniz için bir alışkanlık olsun.",
                    "Bir video iyi gittikten hemen sonra, izleyicileri sizi hâlâ merak ederken yayına geçin.",
                ],
            },
            {
                "h2": "Bir canlı yayın için neyi yapabiliriz, neyi yapamayız?",
                "p": [
                    "Cuma akşamı saat sekizde yayınınızı dolduramayız ve bir izleyici sayısı vaat edemeyiz. Yapabileceğimiz şey, her ay daha çok gerçek insanın videolarınızı tanımasını ve sizi takip etmesini sağlamaktır; böylece her canlı yayın, gelebilecek daha büyük bir grupla başlar.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Bir içerik üreticisinin TikTok canlı yayınını telefonlarından açan takipçiler"},
            },
        ],
        "faqs": [
            ("TikTok canlı yayınım için gerçek izleyici satın alabilir miyim?", "Kimse alamaz. Gerçek insanlar bir yayına, onu gördükleri ve o anda istedikleri için katılır. Talep üzerine teslim edilen izleyiciler izlemeyen hesaplardır ve bir canlı yayını doldurmaz, daha boş hissettirir."),
            ("Paketleriniz canlı yayın izlenmelerime nasıl yardım eder?", "Takipçilerinizi gerçek insanlarla büyütür. Takipçiler, bekleyen canlı yayın kitlenizdir: her kitlede olduğu gibi bazıları siz yayındayken katılır, bazıları katılmaz."),
            ("Panelde canlı yayın izlenmelerini sayıyor musunuz?", "Hayır. Panel kampanyamızın ölçtüklerini gösterir: günlük profil ziyaretleri ve bunların getirdiği takipler. Yayınlarınıza kimin katıldığını TikTok'un kendi canlı yayın analizleri gösterir."),
            ("1.000 takipçim olmadan canlı yayın açabilir miyim?", "Genellikle hayır: TikTok önce 1.000 takipçi ister ve uygulamanız canlı yayının size açık olup olmadığını söyler. Eşiğe gerçek takipçilerle ulaşmak, ilk yayınınızda gelebilecek insanlar olması demektir."),
            ("Satın alınan canlı yayın izleyicileri yayınımın önerilmesini sağlar mı?", "Bunu beklemek için bir neden yok. Hiç sohbet etmeyen, hediye göndermeyen ya da kalmayan hesaplarla dolu bir oda, TikTok'a önermeye değer hiçbir şey vermez."),
        ],
    },
    {
        "service": "views",
        "modifier": "promote",
        "slug": "tiktok/izlenme/tanitim",
        "label": "TikTok videosu tanıtma",
        "title": "TikTok Promote mu, Sizin İçin Kampanya mı? | Growsterr",
        "description": "TikTok Promote ile izlenme ya da takipçi mi? Profiliniz için ay boyunca, seçtiğiniz yere yönelik, arkasında bir ekip olan tanıtım kampanyaları yürütürüz.",
        "h1": ("TikTok Promote ile izlenme mi, ", "sizin için yürütülen bir büyüme kampanyası mı?"),
        "intro": "TikTok Promote ile izlenme satın almayı mı yoksa başka bir şey denemeyi mi tartıyorsanız, bizim nerede durduğumuzu anlatalım. Sizin için TikTok reklamı yürütmüyoruz. İş ortağı ağımız üzerinden kendi tanıtım kampanyalarımızı yürütür, profilinizi bütün ay boyunca her gün, seçtiğiniz yerdeki gerçek insanlara gösteririz. Gördüğünü beğenenler izler, takip eder ve geri gelir.",
        "hero": {"image": "tiktok-creator", "alt": "Bir TikTok videosunu daha çok gerçek insana nasıl tanıtacağını planlayan bir içerik üreticisi"},
        "sections": [
            {
                "h2": "Bir TikTok videosunu tanıtmanın iki yolu",
                "p": [
                    "TikTok'un kendi Promote aracı, bütçeniz yettiği sürece bir videoyu daha çok insana göstermesi için TikTok'a ödeme yapmanızı sağlar: videoyu, hedefi ve harcamayı siz seçer, kendiniz yönetirsiniz.",
                    "Bir Growsterr paketi tek bir gönderiyi değil profilinizi tanıtır; bütün bir ay boyunca ve kampanyayı bir ekip yürütür. İnsanlar profilinize gelir, gözlerine çarpanı izler ve takip edip etmeyeceklerine karar verir.",
                ],
            },
            {
                "h2": "Bir aylık tanıtım neler getirir?",
                "ul": [
                    "Yeni takipçiler: {pick_name} ile genellikle {pick_audience}.",
                    "Aynı takipçilerden beğeni ve yorumlar: genellikle {pick_likes} beğeni ve {pick_comments} yorum.",
                    "Profiliniz genelinde izlenmeler; bunları önceden saymayız.",
                    "Profil ziyaretlerini ve yeni takipçileri gün gün gösteren bir panel.",
                ],
            },
            {
                "h2": "İkisini birlikte kullanabilir misiniz?",
                "p": [
                    "Kullanabilirsiniz. TikTok'un araçları tek bir videonun arkasında tek seferlik bir itiş için uygundur; aylık bir paket ise itişlerin arasında insanların profilinize gelmeye devam etmesini sağlar. Birindeki hiçbir şey diğerinin önüne geçmez.",
                ],
            },
        ],
        "faqs": [
            ("TikTok Promote ya da TikTok reklamları kullanıyor musunuz?", "Hayır. Kampanyalarımız TikTok'un reklam araçlarının dışında, iş ortağı ağımızda yürür. Hesabınıza ya da reklam bütçenize asla ihtiyacımız olmaz, yalnızca kullanıcı adınıza."),
            ("Fiyat, reklamları kendim yürütmekten nasıl farklı?", "Paket sabit bir aylık fiyattır: {starter_name} için {starter_price}, {rising_name} için {rising_price}, {pro_name} için {pro_price}. Reklamlarda kendi bütçenizi belirler ve yönetirsiniz. Hesabınız için hangisinin daha az tuttuğunu söyleyemeyiz, ama her paketin tam olarak ne kadar tuttuğunu söyleyebiliriz."),
            ("Belirli bir TikTok videosunu tanıtabilir miyim?", "{rising_name} ve {pro_name} ile evet: ilgi görecek videoları siz seçersiniz. {starter_name} profilinizi bir bütün olarak tanıtır."),
            ("Tanıtım bana TikTok takipçisi de getirir mi?", "Evet, işin büyük kısmı da bu. İzlediğinden keyif alan insanlar takip eder, {pick_name} ile genellikle ayda {pick_audience}; beğenileri ve yorumları da onlarla gelir."),
            ("İşletme hesabına ihtiyacım var mı?", "Hayır. Hesap herkese açık olduğu sürece kişisel hesaplar da işletme hesapları da olur; istediğimiz tek şey kullanıcı adınız."),
        ],
    },
]
