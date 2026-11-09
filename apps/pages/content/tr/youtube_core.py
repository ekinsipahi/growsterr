"""Turkish YouTube pages beyond the hub and subscribers: likes, views and the ways people ask for
subscribers (real, safe, monthly...). Mirrors en/youtube_core.py; keys and placeholders:
docs/CONTENT.md. Views are never counted in advance; we never promise monetization, watch hours
or retention."""

UPDATED = "2026-11-09"

PAGES = [
    # --- Likes ---------------------------------------------------------------------------
    {
        "service": "likes",
        "slug": "youtube/begeni",
        "label": "YouTube beğeni",
        "title": "YouTube Beğeni Satın Al, İzleyenlerden | Growsterr",
        "description": "YouTube beğeni mi satın almak istiyorsunuz? Paketlerimizdeki her beğeni izlemiş bir izleyiciden, yeni abone ve yorumlarla gelir. Başlangıç: ayda {from_price}.",
        "h1": ("YouTube beğeni satın almak mı istiyorsunuz? ", "İzlemiş insanlardan alın."),
        "intro": "YouTube beğeni satın almak için geldiyseniz önce net bir cevap: beğeniyi paket paket satmıyoruz. Her paket kanalınıza, videolarınızı izleyip keyif aldıklarını beğenen gerçek insanlar getirir; {starter_name} ile genellikle ayda {starter_likes} beğeni, büyük paketlerle daha fazlası.",
        "hero": {"image": "youtube-viewers", "alt": "Az önce izledikleri bir YouTube videosunu telefonlarından beğenen izleyiciler"},
        "sections": [
            {
                "h2": "Bir beğeni YouTube'a ne anlatır?",
                "p": [
                    "Beğeni, oynat tuşuna basmış birinin verdiği küçük, herkese açık bir oydur. YouTube onu o izleyicinin yaptığı her şeyle birlikte okur: ne kadar izledi, abone oldu mu, bir sonraki video için geri geldi mi?",
                    "Hiç izlemeyen bir hesaptan gelen beğeni bu deseni bozar. Videonuzun altındaki sayaç yükselirken çevresindeki her şey yerinde sayar; YouTube da yapay saydığı etkileşimi spam olarak değerlendirir.",
                ],
            },
            {
                "h2": "Beğeniler nereye düşer: videolar, müzik ve gönderiler",
                "p": [
                    "Yeni izleyiciler keyif aldıklarını beğenir; genellikle en yeni videolarınızı ve onları kanalınıza getiren videoyu. Müzisyenler aynısını müzik ve sözlü videolarda görür: parçayı dinleyip daha fazlasını isteyen dinleyicilerden beğeniler.",
                    "Topluluk gönderileri farklı işler. Aboneleriniz onları akışlarında görür ve kendi istekleriyle beğenebilir, ama verdiğimiz aralıklar videolarınıza gelen beğenilerdir.",
                ],
                "image": {"image": "youtube-channel", "alt": "YouTube müzik videosu için ev stüdyosunda şarkı kaydeden bir müzisyen"},
            },
            {
                "h2": "Beğeniler neden abonelerle gelir?",
                "p": [
                    "Beğeni, bir izleyicinin yapabileceği en hafif şeydir. Pakette aynı insanlardan gelen daha ağır sinyallerle birlikte gelir: bir abonelik, bir yorum, bir sonraki video için geri dönüş. Bu rakamlar birlikte yükseldiğinde, insanların keyif aldığı bir kanalı anlatırlar; çünkü öyledir.",
                ],
            },
        ],
        "faqs": [
            ("Abone olmadan YouTube beğeni satın alabilir miyim?", "Hayır. Beğeniler her paketin içinde, aynı gerçek insanlardan gelen yeni abone ve yorumlarla birlikte gelir. Arkasında izleyen kimse olmayan bir beğeni, YouTube'un spam saydığı türden etkileşimdir."),
            ("Tipik bir ayda kaç beğeni gelir?", "{pick_name} ile genellikle {pick_likes}; bu da her yeni abone için kabaca iki üç beğeni demektir. Neyi beğeneceklerine gerçek insanlar karar verir, bu yüzden hiçbir ay diğerine benzemez."),
            ("YouTube topluluk gönderisine beğeni alabilir miyim?", "Ayrı bir sipariş olarak hayır. Yeni aboneleriniz topluluk gönderilerinizi akışlarında görebilir ve bazıları isteyerek beğenir. Her paketteki tipik aralıklar videolara gelen beğenileri sayar."),
            ("Müzik videoları da beğeni alır mı?", "Evet. Kanalınız müzikse, getirdiğimiz insanlar parçalarınızı dinleyip keyif aldıklarını beğenen dinleyicilerdir. Kampanyayı dinleyicilerinizin olduğu şehre, bölgeye ya da ülkeye yöneltebilirsiniz."),
            ("Hangi videolarım beğeni alır?", "Seçimi gerçek izleyiciler yapar; genellikle en yeni videolarınız ve onları kanalınıza ilk getiren video."),
            ("İlk beğeniler ne zaman görünür?", "Kampanyanızın ilk günlerinde, ilk izleyiciler geldikçe; sonra ayın geri kalanında her gün birkaç tane."),
        ],
    },
    {
        "service": "likes",
        "modifier": "comment-likes",
        "slug": "youtube/begeni/yorum-begenisi",
        "label": "YouTube yorum beğenisi",
        "title": "YouTube Yorum Beğenisi: Gerçek Olanı Nasıl Gelir? | Growsterr",
        "description": "YouTube yorum beğenisi almayı mı düşünüyorsunuz? Tek bir yorumu yukarı itmiyoruz. Gerçek izleyiciler videolarınızdaki sohbeti okur, katıldıklarını beğenir.",
        "h1": ("YouTube yorum beğenisi satın almak mı? ", "Beğenilmeye değer bir yorum bölümü kurun."),
        "intro": "YouTube yorum beğenisi satın alanlar genellikle tek bir yorumun en üste çıkmasını ister. Bunu satmıyoruz. Kanalınıza gerçek izleyiciler getiriyoruz; videolarınızın altındaki yorumları okuyanlar da onlara hitap eden yanıtları, soruları ve esprileri beğeniyor, sabitlenmiş yorumunuz da dahil.",
        "hero": {"image": "youtube-viewers", "alt": "Bir YouTube videosunun altındaki yorumlarda gezinip bir yanıtı beğenen izleyici"},
        "sections": [
            {
                "h2": "Amaç en üstteki tek bir yorum değil",
                "p": [
                    "Neredeyse hiç kıpırdamamış bir videonun altında yüzlerce beğenisi olan bir yorum, sohbeti okuyan herkesin gözüne batar. Yorum beğenileri de diğerleri gibi etkileşimdir; yani yazılımlardan gelen beğeniler de YouTube'un spam kurallarına girer.",
                    "Yorum başka bir içerik üreticisinin videosunun altındaysa, onu yukarı taşımak zaten yaptığımız bir şey değil. Biz kendi kanalınızı, onu seçen insanlarla büyütürüz.",
                ],
            },
            {
                "h2": "Bir yorum bölümü nasıl canlanır?",
                "p": [
                    "Gerçek izleyiciler izledikten sonra yorumları okur. Cevap verir, katıldıkları yorumları beğenir ve kendi yorumlarını bırakırlar: {pick_name} ile genellikle ayda {pick_comments} yeni yorum, yazılımların değil insanların yazdığı.",
                ],
                "ul": [
                    "İzleyicilere gerçek bir soru soran bir yorumu sabitleyin. Cevaplar kendi sohbetlerini başlatır.",
                    "Yeni bir videodaki ilk yorumlara cevap verin. Sohbette görünen bir içerik üreticisi oraya daha çok insan çeker.",
                    "Sevdiğiniz yorumlara kalp bırakın. İzleyiciler fark eder ve konuşmak için geri gelir.",
                ],
                "image": {"image": "youtube-channel", "alt": "Yeni bir YouTube videosunun altında yorumlara bir soru sabitleyen içerik üreticisi"},
            },
            {
                "h2": "Paket neyi sayar, neyi saymaz?",
                "p": [
                    "Abonelerin, video beğenilerinin ve yorumların tipik aylık aralıkları var. Yorum beğenilerinin yok: bir izleyici diğerine katıldığında olur ve bunu kimse planlayamaz.",
                ],
            },
        ],
        "faqs": [
            ("Başka bir kanalın videosundaki yorumuma beğeni ekleyebilir misiniz?", "Hayır. Kendi kanalınızı, onu seçen gerçek insanlarla büyütürüz. Başkasının videosunun altındaki bir yorumu yukarı taşımak yaptığımız işin parçası değil."),
            ("Yorum beğenileri pakete dahil mi?", "Hareketli her kanalda nasıl geliyorsa öyle gelirler: videolarınızın altındaki sohbetleri okuyan gerçek izleyicilerden. Onları önceden saymıyoruz, çünkü her biri birine katılan bir insandır."),
            ("Yorum bölümlerim gerçekten hareketlenir mi?", "İnsanlar geldikçe evet: {starter_name} ile genellikle ayda {starter_comments}, {rising_name} ile {rising_comments}, {pro_name} ile {pro_comments} yeni yorum; abone olan aynı insanlardan."),
            ("Yorumları botlar ya da yapay zekâ mı yazıyor?", "Hayır. Her yorum, videonuzu izleyip söyleyecek bir şeyi olan bir insandan gelir. Yorumları asla önceden hazırlamaz, kimse için yazmayız."),
            ("Kendi videomdaki tek bir yoruma beğeni gönderebilir misiniz?", "Hayır. Kanalınızı tanıtırız; hangi yorumların beğeniyi hak ettiğine izleyiciler karar verir, sizinkiler de dahil. Gerçek bir şey soran sabitlenmiş bir yorum, beğeni toplama ihtimali en yüksek olandır."),
            ("YouTube yorumları için beğeni satın almak riskli mi?", "Bir bot hizmetinden, evet: yorum beğenileri etkileşimdir ve YouTube yapay etkileşimi spam sayar. Sohbeti gerçekten okuyan insanlardan gelen beğeniler ise kanalın olağan hayatıdır."),
        ],
    },
    {
        "service": "likes",
        "modifier": "live",
        "slug": "youtube/begeni/canli-yayin",
        "label": "YouTube canlı yayın beğenisi",
        "title": "YouTube Canlı Yayın Beğenisi, Sohbetten Gelir | Growsterr",
        "description": "YouTube canlı yayın beğenisi almadan önce: yayında beğeniler sohbetteki insanlardan gelir. Katılabilecek gerçek aboneleri büyütürüz. Başlangıç: ayda {from_price}.",
        "h1": ("YouTube canlı yayın beğenisi mi? ", "Sohbetinizdeki insanlardan gelir."),
        "intro": "YouTube canlı yayın beğenisi satın almadan önce düğmeye kimin bastığını düşünün: yayınınızı gerçekten izleyen insanlar. Bir yayına belirli bir dakikada beğeni bırakamayız ve bırakabiliyormuş gibi de yapmayız. Canlı olduğunuzu görüp katılmayı seçebilecek gerçek aboneleri büyütürüz.",
        "hero": {"image": "youtube-channel", "alt": "Kamerası ve mikrofonu olan bir masadan YouTube'da canlı yayın yapan bir içerik üreticisi"},
        "sections": [
            {
                "h2": "Canlı yayın beğenisi bir sayı değil, bir tepkidir",
                "p": [
                    "Yayın sırasında beğeniler ekranda bir şey olduğunda gelir: kritik bir hamle, iyi bir cevap, sohbetin istediği şarkı. Bunlar kitlenin o anki tepkisidir.",
                    "İzlemeyen hesaplardan gelen beğeniler hiçbir şeye tepki vermez. Sessiz bir sohbetin yanına blok halinde düşerler ve katılan her gerçek insan ikisinin uyuşmadığını görür.",
                ],
            },
            {
                "h2": "Yayının en iyi anlarını beğeniye dönüştürmek",
                "ul": [
                    "Beğeniyi ilk dakikada değil, yayının en heyecanlı yerinde ve bir kez isteyin.",
                    "Sohbetteki isimleri sesli söyleyin: insanlar parçası olduklarını hissettikleri yayınları beğenir.",
                    "Sonradan gelenlere neler olduğunu anlatan bir yorum sabitleyin ki tepki verecek kadar kalsınlar.",
                    "Tekrarı yayında tutun ki yayını kaçıranlar yine izleyip beğenebilsin.",
                ],
                "image": {"image": "youtube-viewers", "alt": "İçerik üreticisi konuşurken YouTube canlı sohbetinde yazışıp tepki veren insanlar"},
            },
            {
                "h2": "Bir sonraki yayından önce kitleyi büyütün",
                "p": [
                    "Getirdiğimiz aboneler kanalınızı bulup kalmaya karar veren gerçek insanlardır. Bazıları kendi programlarına göre bir sonraki sohbetinizde olacak. Bu grup büyüdükçe, yayında iyi bir şey olduğunda tepki verecek insan sayısı da artar.",
                ],
            },
        ],
        "faqs": [
            ("Canlı yayınım sırasında beğeni gönderebilir misiniz?", "Hayır. Gerçek insanların kendi programları var, bu yüzden dürüst olan kimse belirli bir saatte tepki sözü veremez. Bizim büyüttüğümüz, canlı yayına geçtiğinizde izliyor olabilecek kitledir."),
            ("Yeni abonelerim yayınlarımı izler mi?", "Bazıları, kendilerine uyan günlerde. Kanalınızı gördükten sonra seçtiler, yani yayınlarınız onlara ulaşabilir; katılıp katılmamak onların kararı."),
            ("İnsanlar bir yayını bittikten sonra beğenebilir mi?", "Evet. Tekrar, kanalınızda bir video olarak kalır ve onu sonradan izleyen herkes beğenebilir."),
            ("Neden bir bot hizmetinden canlı yayın beğenisi almayayım?", "Çünkü sahte etkileşim en kolay yayında fark edilir. Sessiz bir sohbetin yanındaki yüzlerce beğeni, katılan herkese odanın göründüğü gibi olmadığını söyler."),
            ("Yayın kitlem ne kadar büyüyebilir?", "Bu yayınlarınıza bağlı, ama havuz her gün büyür: {pick_name} bir ayda genellikle {pick_audience} abone ekler ve her biri bir dahaki sefere sohbette olabilecek biridir."),
        ],
    },
    {
        "service": "likes",
        "modifier": "shorts",
        "slug": "youtube/begeni/shorts",
        "label": "YouTube Shorts beğeni",
        "title": "YouTube Shorts Beğeni Satın Al: Gerçek Olanı | Growsterr",
        "description": "Kaydırmayı bırakan gerçek insanlardan YouTube Shorts beğenisi, asla bot değil. Abone ve yorumla birlikte aylık bir pakette gelir. Başlangıç: ayda {from_price}.",
        "h1": ("YouTube Shorts beğeni satın almak mı? ", "Kaydırmayı bırakan insanlardan kazanın."),
        "intro": "Shorts akışında bir beğeni, birinin önemsemeye yetecek kadar kaydırmayı bıraktığı anlamına gelir. YouTube Shorts beğeni satın almak istiyorsanız sahip olmaya değer tek tür de bu: her gün kanalınıza getirdiğimiz, izleyen, beğenen ve bazen abone olan gerçek insanlardan gelen beğeniler.",
        "hero": {"image": "youtube-viewers", "alt": "Telefonlarında YouTube Shorts izleyip beğeniye dokunan insanlar"},
        "sections": [
            {
                "h2": "Bir Shorts beğenisinin değeri",
                "p": [
                    "Shorts, insanların hızla geçtiği bir akışta oynar. Oradaki bir beğeni, Shorts videonuzun oynamasına izin veren, çoğu zaman birden fazla kez izleyen ve onun bir dokunuşu hak ettiğine karar veren bir izleyiciden gelir.",
                    "Üretilmiş beğeniler bunların hepsini atlar. Kimsenin izlemeye devam etmediği bir Shorts videosuna yığılırlar; bu da bir beğeninin söylemesi gerekenin tam tersidir.",
                ],
            },
            {
                "h2": "Bir Shorts videosunu beğenilmeye değer kılan nedir?",
                "ul": [
                    "Sonuçla başlayın. İlk saniye insanların kalıp kalmayacağına karar verir.",
                    "Sonu başa bağlayın ki tekrar izlemek doğal gelsin.",
                    "Shorts videolarınıza altyazı ekleyin: birçok insan sesi kapalı kaydırır.",
                    "Kanalınızı ziyaret etmek için net bir nedenle bitirin.",
                ],
                "image": {"image": "youtube-channel", "alt": "Telefonu kol mesafesinde tutarak dikey bir YouTube Shorts videosu çeken içerik üreticisi"},
            },
            {
                "h2": "Paket Shorts videolarınız için ne yapar?",
                "ul": [
                    "Kanalınızı tanıtırız; onu keşfeden izleyiciler izlemek istedikleri Shorts ve videoları seçer.",
                    "{pick_name} bir ayda genellikle {pick_likes} beğeni ekler; insanların keyif aldığı neyse ona yayılır.",
                    "Şehri, bölgeyi ya da ülkeyi bize söyleyin ki Shorts videolarınız, onları kimin için yaptıysanız o yerdeki insanlara ulaşsın.",
                ],
            },
        ],
        "faqs": [
            ("Yalnızca tek bir Shorts videosuna beğeni alabilir miyim?", "Tek seferlik olarak hayır. Beğeniler aylık bir paketin içinde, insanların keyif aldığı Shorts ve videolara yayılarak, abone ve yorumlarla birlikte gelir."),
            ("Shorts beğenileri uzun videolarıma yardım eder mi?", "Dolaylı olarak. Bir Shorts videosundan keyif alan bazı insanlar arkasındaki kanalı açar; birkaçı da uzun videolarınızı izleyip abone olur."),
            ("Shorts videolarıma beğeniler ne kadar hızlı gelir?", "Kampanyanızın ilk günlerinden itibaren, sonra ay boyunca her gün birkaç tane. Bir saat içinde gelen binlerce Shorts beğenisi izleyicilerden değil botlardan gelir."),
            ("Shorts videolarımı kimler beğeniyor?", "Seçtiğiniz konumda, kampanyamız aracılığıyla kanalınıza denk gelen insanlar. İzlemeye de beğenmeye de kendileri karar verdi; kimse onlardan istemedi."),
            ("İnsanlar Shorts videolarıma yorum da yapar mı?", "Bazıları yapar. Kanalınızın genelinde {pick_name} genellikle ayda {pick_comments} yorum getirir; her birini bırakan kişi kendisi yazar."),
        ],
    },
    # --- Subscribers ---------------------------------------------------------------------
    {
        "service": "subscribers",
        "modifier": "gradual",
        "slug": "youtube/abone/kademeli",
        "label": "Kademeli YouTube abone",
        "title": "YouTube Abone Satın Al: Yavaş ve İstikrarlı | Growsterr",
        "description": "Yavaş ve istikrarlı YouTube abonesi: ayın her günü, kendi hızlarında birkaç birkaç abone olan gerçek insanlar. Başlangıç: ayda {from_price}.",
        "h1": ("Yavaş ve istikrarlı YouTube abone satın almak mı? ", "Gerçek insanların tek hızı bu."),
        "intro": "YouTube aboneyi yavaş ve istikrarlı satın almak istiyorsanız doğru şeyi istiyorsunuz. Burada yavaşlık, insanların yaptığı şeyin ta kendisi: kanalınızı kendi günlerinde keşfeder, bir iki video izler ve karar verirler. {pick_name} ile bu, ay boyunca genellikle {pick_audience} abone eder.",
        "hero": {"image": "youtube-subscribers", "alt": "Bir ay boyunca her gün biraz yükselen bir YouTube kanalının abone sayısı"},
        "sections": [
            {
                "h2": "Yavaş botlar da yine bottur",
                "p": [
                    "Bazı hizmetler damla damla gönderim seçeneği satar: aynı bot aboneler, eğri yumuşak görünsün diye birkaç birkaç salınır. Hız değişir, arkasındaki değişmez. Hiç izlemeyen hesaplar, abonelerinizin etkileşime giren kısmını yine küçültür.",
                    "Kademeli büyüme, insanların tek tek karar vermesinden geldiğinde bir anlam taşır. Hiçbir ayar bunu taklit edemez, buna gerek de yoktur.",
                ],
            },
            {
                "h2": "İstikrar panelinizde nasıl görünür?",
                "p": [
                    "Panelinizi herhangi bir gün açın, iki çizgi görürsünüz: kampanya aracılığıyla kanalınızı ziyaret eden insanlar ve bunlardan kaçının abone olduğu. Bazı günler diğerlerinden yoğundur; insanların keşfettiği her kanalda olduğu gibi. Görmeyeceğiniz şey, bir gecede binlerce aboneyle gelen bir sıçramadır.",
                ],
            },
            {
                "h2": "YouTube'da istikrar neden ani sıçramayı yener?",
                "p": [
                    "Her hafta izlenme ve yorumlarla birlikte abone kazanan bir kanal, insanların bulduğu bir kanaldır. Her yeni video biraz daha büyük bir gerçek insan grubuna ulaşır ve bu aylar içinde birikir.",
                ],
                "image": {"image": "youtube-channel", "alt": "Dizüstü bilgisayarda bir aylık istikrarlı kanal büyümesini inceleyen bir YouTube içerik üreticisi"},
            },
        ],
        "faqs": [
            ("Yavaş ne kadar yavaş?", "İnce ince yayılmış: çoğu gün birkaç yeni abone, asla bir yığın değil. 30 gün boyunca bu, paketin tipik aralığına ulaşır ve her gün biraz farklıdır."),
            ("Abonelerin ne kadar hızlı geleceğini seçebilir miyim?", "Saat saat değil, çünkü bunu gerçek insanlar belirler. Siz paketi seçersiniz: büyük bir paket kanalınızı her gün daha çok insana gösterir."),
            ("Yavaş bir damlatma kanalım için daha mı güvenli?", "Yalnızca aboneler gerçekse. Botların yavaş damlatılması yine sahte etkileşimdir; gerçek insanların kendi hızlarında abone olması ise olağan büyümedir."),
            ("Her gün gelen aboneler şüpheli görünür mü?", "Hayır. İnsanların bulduğu kanallar her gün abone kazanır; büyümenin normal şekli budur. Göze batan, bir saatte binlercesinin gelmesidir."),
            ("Ay bitince ne olur?", "Siz iptal etmedikçe paket yenilenir ve kampanya aynı istikrarlı hızla devam eder. İptal bir sonraki ödemeyi durdurur; içinde bulunduğunuz ay sonuna kadar sürer."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "monthly",
        "slug": "youtube/abone/aylik",
        "label": "Aylık YouTube abone",
        "title": "Aylık YouTube Abone Satın Al, Dilediğinizde İptal | Growsterr",
        "description": "YouTube aboneyi aylık satın alın: ay boyunca kanalınıza gerçek insanlar getiren, kartla ödenen ve dilediğiniz an iptal edilen bir paket. Başlangıç: {from_price}.",
        "h1": ("Aylık YouTube abone satın alın, ", "kanallar gerçekte böyle büyür."),
        "intro": "Aylık paket tam olarak bizim çalışma şeklimiz. Bizden aylık YouTube abone satın aldığınızda kanalınız her gün gerçek insanlara gösterilir, beğenenler abone olur ve paket siz durdurmaya karar verene kadar her ay yenilenir.",
        "hero": {"image": "youtube-subscribers", "alt": "Aydan aya yeni aboneler kazanan bir YouTube kanalı"},
        "sections": [
            {
                "h2": "Neden tek seferlik paket değil de abonelik?",
                "p": [
                    "Bir kanal tek bir patlamayla bitmez. Video yüklemeye devam edersiniz, yani sizi bulacak yeni insanlara da ihtiyacınız devam eder. Aylık paket bu ritme uyar: her yeni video hâlâ büyüyen bir kitleye ulaşır.",
                    "Tek seferlik paketler tersini yapar. İlk gün bir sayı teslim eder, sonra hiçbir şey; hiçbir gerçek kitle komutla ortaya çıkmadığından da o sayı neredeyse her zaman bottur.",
                ],
            },
            {
                "h2": "Ay ay ödemek",
                "ul": [
                    "Ödeme Stripe'ın güvenli ödeme sayfasında kartla ya da destekleyen cihazlarda Apple Pay ve Google Pay ile yapılır.",
                    "Paket başladığınız günden itibaren her ay yenilenir.",
                    "Durdurmak hesabınızda tek bir tıklamadır ve sonrasında ödeme alınmaz.",
                    "Videolarınız daha çok insana hazır olduğunda bir üst pakete geçebilirsiniz.",
                ],
            },
            {
                "h2": "Aydan aya biriken şey",
                "p": [
                    "Her ay, kanalınızdan keyif aldıkları sürece kalan gerçek aboneler ekler. Birkaç ay içinde bu, videolarınızı gören bir insan tabanına dönüşür; böylece her yeni video daha fazlasıyla başlar.",
                ],
                "image": {"image": "youtube-channel", "alt": "Duvar takviminde gelecek ayın YouTube videolarını planlayan bir içerik üreticisi"},
            },
        ],
        "faqs": [
            ("Bu bir abonelik mi?", "Evet. Her paket aylık bir aboneliktir; Stripe üzerinden kart, Apple Pay ya da Google Pay ile ödenir. Tek seferlik paket yoktur."),
            ("Her ay genellikle ne kadar ekler?", "{starter_name} genellikle {starter_audience}, {rising_name} {rising_audience}, {pro_name} {pro_audience} abone getirir. Her ay biraz farklıdır, çünkü her abone seçim yapan bir insandır."),
            ("İlk aydan sonra iptal edebilir miyim?", "Evet. İstediğiniz an hesabınızdan iptal edin; ödediğiniz ay son gününe kadar sürer ve sonrasında hiçbir şey yenilenmez."),
            ("İptal edersem abonelerim bende kalır mı?", "Siz ödemeyi bıraktınız diye kimse ayrılmaz: onlar insan ve kanalınız ilgilerini çektiği sürece abone kalırlar. İptal yeni kampanyaları sonlandırır, kimseyi silmez."),
            ("Neyle ödeyebilirim?", "Kartla ya da telefonunuz sunuyorsa Apple Pay veya Google Pay ile. Hangisini seçerseniz, iptal edene kadar her ay ondan tahsil edilir."),
            ("Küçük başlayıp daha büyük bir pakete geçebilir miyim?", "Evet. Kanalınızın bugün olduğu yerden başlayın, çoğu zaman {starter_name} ile; daha çok insanı karşılayacak kadar video yüklediğinizde bir üst pakete geçin."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "no-drop",
        "slug": "youtube/abone/dusmeyen",
        "label": "Düşmeyen YouTube abone",
        "title": "Düşmeyen YouTube Abone: Düşüş Yok, Bot Yok | Growsterr",
        "description": "Abone sayıları, aboneler hiç gerçek olmadığında düşer. Bizimkiler kanalınızı seçen insanlar, temizlenmeyi bekleyen hesaplar değil. Başlangıç: ayda {from_price}.",
        "h1": ("Düşmeyen YouTube abone satın almak mı? ", "Kanalınızı seçen insanlarla başlayın."),
        "intro": "Düşmeyen YouTube abone satın almak istemek, genellikle daha önce bir sayının düştüğünü görmüş olmak demektir. Aboneler hiç insan olmadıklarında düşer: YouTube spam ve kapatılmış hesapları temizler, bot aboneler de onlarla gider. Bizimkiler abone olmayı seçen gerçek izleyicilerdir; bir temizliğin dokunmamak üzere tasarlandığı türden hesaplar.",
        "hero": {"image": "youtube-subscribers", "alt": "Gerçek yeni aboneler gelirken sabit kalan bir YouTube abone sayısı"},
        "sections": [
            {
                "h2": "Abone sayıları neden düşer?",
                "p": [
                    "YouTube spam saydığı aboneleri, kapatılmış hesaplarla birlikte siler. Bot abone satın almış kanallar bu sayıların basamak basamak düştüğünü görür; bazen satın almadan aylar sonra.",
                    "Düşüş görünen kısımdır. Görünmeyen kısım, o hesapların kanalınızda hiç izlemeden geçirdiği zaman ve abonelerinizin etkileşime giren kısmını düşürmeleridir.",
                ],
            },
            {
                "h2": "Telafi neden çözüm değil?",
                "p": [
                    "Bazı satıcılar düşeni telafi etmeyi vaat eder. Bu, silinen botların yerine yeni botlar koymak demektir; sayıyı yukarıda, sorunu da sürdürür. Gerçek bir abonenin yerine yenisini koymaya gerek yoktur.",
                ],
            },
            {
                "h2": "Düşmemenin dürüst hali",
                "p": [
                    "Gerçek insanlar, her kanalda olduğu gibi abonelikten çıkabilir ve zamanla birkaçı çıkar. Bu olağan bir değişimdir ve botların ardında bıraktığı dalgaların yanında küçüktür. Kalan şey, siz video yüklediğinizde hâlâ orada olan bir kitledir.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Bir içerik üreticisinin en yeni YouTube videosunu kanepede izleyen eski aboneler"},
            },
        ],
        "faqs": [
            ("Yeni abonelerimden hiç ayrılan olur mu?", "Bazıları ayrılabilir; zevkleri değiştiğinde insanlar her kanalda bunu yapar. Olmayacak olan, birlikte silinmeyi bekleyen bir sahte hesap yığınıdır."),
            ("Aboneler düşerse telafi var mı?", "Hayır, çünkü doldurulacak sahte bir sayı yok. Aylık bir gerçek insan paketi alırsınız; sonrasında ne yapacakları, her kitlede olduğu gibi onların seçimidir."),
            ("Başka bir hizmetten sonra sayım neden düştü?", "Büyük ihtimalle YouTube spam saydığı ya da kapatılmış hesapları sildi. Bot aboneler bu temizliklerde genellikle büyük yığınlar halinde gider."),
            ("Bot aboneler gittikten sonra bile kanalıma zarar verebilir mi?", "Silinmeleri küçük olan sorundur. Oradayken tek bir videoyu bile izlemediler; bu da kitlenizi gerçekte olduğundan daha az ilgili gösterdi."),
            ("Panelim YouTube'daki sayımla eşleşir mi?", "Tam olarak değil. Paneliniz kampanyamızın getirdiği yeni aboneleri sayar; YouTube'un gösterdiği toplam, başka yerlerden gelen büyümeyi ve abonelikten çıkanları da içerir."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "organic",
        "slug": "youtube/abone/organik",
        "label": "Organik YouTube abone",
        "title": "Organik YouTube Abone Satın Al: Nasıl İşler? | Growsterr",
        "description": "Organik YouTube abone satın alınır mı? Tanıtım kampanyalarıyla tanıştırmanın bedelini biz öderiz; abone olma kararı izleyicinindir. Başlangıç: ayda {from_price}.",
        "h1": ("Organik YouTube abone satın almak mı? ", "Tanıştırmayı biz öderiz, seçimi onlar yapar."),
        "intro": "Organik YouTube abone satın almak isteyen herkese dürüst cevap şu: kimse size bir karar satamaz. Bizim ödediğimiz şey tanıştırmadır. Kanalınız iş ortağı ağımızdaki tanıtım kampanyalarıyla gerçek insanlara gösterilir; abone olan da bunu istediği için yapar.",
        "hero": {"image": "youtube-subscribers", "alt": "Videolarını keşfettikten sonra bir YouTube kanalına katılan yeni aboneler"},
        "sections": [
            {
                "h2": "Ücretli ile organik arasındaki çizgi",
                "p": [
                    "Reklam veren her kanal dikkat için ödeme yapar. Sonrasında olan ya organiktir ya değildir: bir insan izler, videoyu beğenir ya da beğenmez, abone olur ya da geçer.",
                    "Biz o çizgiyi temiz tutarız. Kanalınızı her gün insanların önüne çıkarmak için ödeme yaparız; kimseye abone olması için asla ödeme yapmaz, abonelik takası yapmaz ve komutla hareket eden hesaplar kullanmayız.",
                ],
            },
            {
                "h2": "Organik aboneler diğerlerinden nasıl ayırt edilir?",
                "ul": [
                    "İsimleri bir sonraki videonuzun altındaki yorumlarda belirir.",
                    "Yorumları insan gibi okunur: sorular, espriler, arada bir itiraz.",
                    "Yeni aboneler kanal ziyaretleriyle birlikte gelir, asla onlarsız değil.",
                    "Kampanya bittikten sonra da kalırlar, çünkü onları orada tutan bir şey yoktu.",
                ],
            },
            {
                "h2": "Organik, beklemek demek zorunda değil",
                "p": [
                    "Organik büyüme genellikle şanslı tek bir video için yıllarca beklemek olarak düşünülür. Tanıtım kampanyası beklemeyi kısaltır: gerçek insanlar kanalınızı ilk günlerden görür. Kısaltamadığı tek şey onların kararıdır; korunmaya değer kısım da odur.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Elinde kahvesiyle o sabah bulduğu bir kanala abone olan biri"},
            },
        ],
        "faqs": [
            ("Kanalımı tanıtıyorsanız büyüme yine organik mi?", "Abonelikler organik. Kanalınızın gösterilmesi için biz öderiz; kimseye abone olduğu için ödeme yapılmaz ya da ödül verilmez. Her abone videolarınızı gördükten sonra kendi başına karar verdi."),
            ("Abone takası ya da değiş tokuş ağları kullanıyor musunuz?", "Asla. Karşılığında abonelik almak için abone olan insanlar videolarınızla ilgilenmez ve onları nadiren izler; YouTube da bu takasları sahte etkileşim sayar."),
            ("Organik büyüme bir ayda neye ulaşır?", "{pick_name} ile genellikle ayda {pick_audience} arasında bir yere varır. Her biri seçim yapan bir insan olduğu için bu bir sayı değil, bir aralıktır."),
            ("Organik aboneler videolarımı izler mi?", "Kanalınızı gördükten sonra seçtiler; bu, herhangi bir abonenin sahip olabileceği en iyi başlangıç. Her videoyu izleyip izlemeyecekleri, herkeste olduğu gibi videoya bağlı."),
            ("Kampanya sırasında bir şey yapmam gerekiyor mu?", "Kanalınızı herkese açık tutun ve video yüklemeye devam edin. Videolarınız kanal sayfanızın vaat ettiğine ne kadar uyarsa, ziyaret edenlerin o kadar fazlası abone olmaya karar verir."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "real",
        "slug": "youtube/abone/gercek",
        "label": "Gerçek YouTube abone",
        "title": "Gerçek YouTube Abone Satın Al, Kontrol Edin | Growsterr",
        "description": "Her YouTube abonesinde kontrol edebileceğiniz dört gerçeklik işareti ve aylık paketlerimizin bu testi geçen insanları nasıl getirdiği. Başlangıç: ayda {from_price}.",
        "h1": ("Gerçek YouTube abone satın alın. ", "Nasıl anlaşılır, anlatalım."),
        "intro": "İnsanlar YouTube abone satın alırken, bir kez yandıktan sonra araya “gerçek” kelimesini ekler. Bize göre bu, kontrol edebileceğiniz bir şey anlamına gelmeli: kanalınıza denk gelen, abone olmaya değer bulduğuna karar veren ve sonra izlenme, beğeni ve yorumlarınızda görünen bir insan.",
        "hero": {"image": "youtube-subscribers", "alt": "Bir ay boyunca gerçek abonelerin geldiği bir YouTube kanal sayfası"},
        "sections": [
            {
                "h2": "Bir abonenin gerçek olduğunu gösteren dört işaret",
                "p": [
                    "Yüksek kalite, içten, gerçek: her satıcı bu kelimeleri kullanır. Onları birbirinden ayıran kontroller şunlar.",
                ],
                "ul": [
                    "Önce bir ziyaret oldu: biri abone olmadan önce kanalınızı açtı.",
                    "İzliyorlar: bir sonraki videonuzdaki izlenmeler abone sayısıyla birlikte artar.",
                    "Konuşuyorlar; hiçbir yazılımın yazmayacağı yorumlarla.",
                    "Kampanyayı yönelttiğiniz yerde, sipariş verirken belirttiğiniz konumda yaşıyorlar.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Bir YouTube videosunun altına kendi cümleleriyle yorum yazan yeni bir abone"},
            },
            {
                "h2": "Bizi YouTube Studio ile karşılaştırın",
                "p": [
                    "Hikâyenin bizim tarafı Growsterr panelinizdir: kampanyadan kanalınıza gelen ziyaretler ve aralarından abone olanlar. YouTube Studio aynı ayı YouTube'un tarafından anlatır. Bir ay boyunca ikisini birlikte okuyun: aboneler geldikçe videolarınız da yeni insanlardan izlenme ve yorum kazanmalıdır.",
                ],
            },
            {
                "h2": "Gerçek abonelerin yapamadıkları",
                "p": [
                    "Gerçek insanlar saat saat sipariş edilemez, onlara ne yorum yapacakları söylenemez ve her videoyu izleyeceklerine söz veremezler. Bunları sunan herkes, insan olmayan bir şeyi anlatıyordur. Size bir sayı satmaktansa sınırları söylemeyi tercih ederiz.",
                ],
            },
        ],
        "faqs": [
            ("YouTube aboneleri için yüksek kalite ne demek?", "Bize göre kendi hesabı olan, kanalınızı seçmiş ve izleyebilen, beğenebilen, yorum yapabilen bir insan. Profil fotoğrafı ve hesap yaşı kolayca taklit edilir; gerçek bir abone olma kararı edilemez."),
            ("Aboneleriniz gerçek insanlar mı, yoksa sizin kontrol ettiğiniz hesaplar mı?", "Gerçek insanlar. Hiçbir hesaba sahip değiliz, hesap yönetmiyor ya da kiralamıyoruz. Kanalınızı tanıtım kampanyalarıyla gösteririz, görenler de karar verir."),
            ("Giriş bilgilerimi paylaşmadan gerçek YouTube abone satın alabilir miyim?", "Evet; zaten kimseyle paylaşmamalısınız. Kanal kullanıcı adınıza ve herkese açık bir kanala ihtiyacımız var, başka bir şeye değil."),
            ("Gerçek aboneler kanalımın para kazanmasını sağlar mı?", "Bu YouTube'un kararı; bu yüzden asla para kazanma ya da izlenme saati sözü vermeyiz. Gerçek aboneler videolarınızı izleyebilir, botlar asla izlemez; ama kimin para kazanacağına YouTube'un kendi şartları ve incelemesi karar verir."),
            ("Bir aylık gerçek büyüme neye benzer?", "{pick_name} ile her gün az sayıda gelen, tipik olarak {pick_audience} yeni abone. Daha küçük bir kanal ayda {starter_price} olan {starter_name} ile başlayabilir."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "safe",
        "slug": "youtube/abone/guvenilir",
        "label": "Güvenilir YouTube abone",
        "title": "Güvenilir YouTube Abone Satın Al, Meşru ve Güvenli | Growsterr",
        "description": "YouTube abone satın almak meşru ve güvenli mi? Hizmeti kimin yürüttüğüne, ne istediğine ve abonelerin nasıl geldiğine bakın. Her birine cevabımız burada.",
        "h1": ("Güvenilir YouTube abone mi arıyorsunuz? ", "Önce arkasında kim olduğuna bakın."),
        "intro": "YouTube aboneyi meşru ve güvenli bir şekilde satın alıp alamayacağınızı mı merak ediyorsunuz? Meşru sayılmak için bir hizmetin üç kontrolden geçmesi gerekir: adını söyleyebileceğiniz bir şirket, giriş bilgilerinize dokunmayan bir süreç ve gerçek insan olan aboneler. Growsterr bir Sterr Agency ürünü; her birine cevabımız şöyle.",
        "hero": {"image": "youtube-subscribers", "alt": "Gerçek insanlardan gelen abonelerle güvenle büyüyen bir içerik üreticisinin YouTube kanalı"},
        "sections": [
            {
                "h2": "Kime ödeme yapıyorsunuz?",
                "p": [
                    "Growsterr'ın arkasında Sterr Agency var: Tallinn, Estonya'da Sterr Technologies OÜ olarak kayıtlı, merkezi Türkiye'de. Stripe'ın güvenli ödeme sayfası üzerinden ödersiniz ve abonelik, iptal edebileceğiniz kendi hesabınızda durur.",
                ],
            },
            {
                "h2": "Kanalınız nasıl korunur?",
                "ul": [
                    "Google şifreniz sizde kalır: onu asla istemeyiz ve ekibimizden kimse kanalınıza giriş yapmaz.",
                    "Kimseye abone olması için ödeme yapılmaz, abonelik takası da yoktur.",
                    "Aboneler ay boyunca gelir, asla bir yığın halinde değil.",
                    "Beğeni ve yorumlar abonelerin kendisinden gelir, böylece her rakam birlikte hareket eder.",
                ],
                "image": {"image": "youtube-channel", "alt": "Yalnızca kendi cihazında oturum açmış, masasında YouTube kanal ayarlarına bakan bir içerik üreticisi"},
            },
            {
                "h2": "Her büyüme hizmetindeki tehlike işaretleri",
                "ul": [
                    "Giriş bilgilerinizi ya da Google hesabınıza erişim ister.",
                    "Belirli bir tarihe kadar kesin sayıda abone vaat eder.",
                    "Abone, izlenme ve beğeniyi biner biner ayrı paketler halinde satar.",
                    "Abonelerin nereden geldiğini söyleyemez ya da ölçtüğünü gösteremez.",
                ],
            },
        ],
        "faqs": [
            ("YouTube abone satın almak meşru mu?", "Tanıtım için ödeme yapmak olağandır; reklam veren her kanal bunu yapar. Sahte etkileşime ödeme yapmak ise değildir: botlar, yazılımlar ve abonelik takasları YouTube'un spam saydığı şeylerdir. Biz kanalınızı yalnızca kendi kararını veren gerçek insanlara tanıtırız."),
            ("YouTube bu yüzden kanalımı kapatabilir mi?", "YouTube sahte etkileşime karşı önlem alır; biz de bu yüzden onu asla kullanmayız. YouTube'un kararları adına konuşamayız, ama insanların kanalınızı gördükten sonra seçmesi, tanıtımın her yerde işleyiş biçimidir."),
            ("Başlamak için ne vermem gerekiyor?", "Kanal kullanıcı adınız, kitlenizin nereden gelmesi gerektiği ve aylık paket için bir ödeme kartı. İnsanların abone olabilmesi için kanalınızın herkese açık olması gerekir."),
            ("Ödemem güvende mi?", "Kart, Apple Pay ya da Google Pay; her ödemeyi Stripe işler. Kart bilgileriniz bizde değil, Stripe'ta kalır."),
            ("Bana göre değilse ne olur?", "İstediğiniz zaman hesabınızdan iptal edin. Sonrasında yeni ödeme alınmaz ve içinde bulunduğunuz ay bitene kadar sürer."),
        ],
    },
    # --- Views ---------------------------------------------------------------------------
    {
        "service": "views",
        "slug": "youtube/izlenme",
        "label": "YouTube izlenme",
        "title": "YouTube İzlenme Satın Al: Her Gün Gerçek İnsanlar | Growsterr",
        "description": "YouTube izlenme mi arıyorsunuz? Bizimkiler izlemeyi seçen gerçek insanlardan; abone, beğeni ve yorumla birlikte aylık bir pakette gelir. Başlangıç: {from_price}.",
        "h1": ("YouTube izlenme satın almak mı? ", "Her biri bir insandan gelir."),
        "intro": "YouTube izlenme satın almak için buradaysanız, bizimkilerin nasıl işlediği şöyle. Burada bir izlenme sayısı menüsü yok. Her paket kanalınızı her gün gerçek insanlarla tanıştırır; ilgilerini çekeni oynatırlar ve birçoğu ardından beğenir, yorum yapar ve abone olur. İzlenmeler paketle birlikte gelir ve her biri bir insandır.",
        "hero": {"image": "youtube-viewers", "alt": "Bir içerik üreticisinin YouTube videosunda oynat tuşuna basan gerçek insanlar"},
        "sections": [
            {
                "h2": "Paketlerimizde neden bir izlenme sayısı yok?",
                "p": [
                    "Bir izlenme, izlemeye karar veren bir insandır ve kaç kişinin buna karar vereceğine kimse söz veremez. Belirli bir saate kadar kesin sayıda izlenme satan herkes, yazılımların ya da botların ürettiği oynatmaları satıyordur.",
                    "YouTube yapay olarak şişirilmiş izlenmeleri spam sayar: onları silebilir ve para kazanmaya asla sayılmazlar. Bu yüzden arkasında durabileceğimiz şeyi satıyoruz: gerçek insanlar getiren aylık bir kampanya ve bıraktıkları abone, beğeni ve yorumlar için tipik aralıklar.",
                ],
            },
            {
                "h2": "Müzik videoları, oynatma listeleri ve uzun videolar",
                "p": [
                    "Tek bir parçayı değil, kanalınızı tanıtırız. Onu keşfeden dinleyiciler dikkatlerini çeken şarkıları seçer; bir parçadan keyif alanlar oynatma listelerinizde devam edebilir. Oradaki her oynatma onlarındır.",
                ],
                "image": {"image": "youtube-channel", "alt": "YouTube kanalına yeni bir müzik videosu yükleyen bir müzisyen"},
            },
            {
                "h2": "YouTube izlenme satın alacağınız siteyi seçmeden önce",
                "ul": [
                    "Onlar için izlenmenin ne demek olduğunu sorun: izlemeyi seçen bir insan mı, ürettikleri bir oynatma mı?",
                    "İzlenmelerin tek başına mı, yoksa aynı insanlardan gelen abone, beğeni ve yorumlarla mı geldiğine bakın.",
                    "Bir şirket adı, gerçek bir ödeme sayfası ve bir iptal yolu arayın.",
                    "Google şifrenizi isteyen herkesten uzaklaşın.",
                ],
            },
        ],
        "faqs": [
            ("Paket olmadan izlenme sipariş edebilir miyim?", "Hayır. Getirdiğimiz her izlenme abone de olabilecek, beğenebilecek ya da yorum yapabilecek birine aittir; bu yüzden yalnızca bir paketin parçası olarak gelirler. Başka hiçbir şey kıpırdamazken tırmanan bir izlenme sayısı, yapay trafiğin desenidir."),
            ("Kaç izlenme bekleyeceğimi söyler misiniz?", "İzlenmelere bir sayı koymuyoruz, çünkü her biri bir insanın seçimidir. Verdiğimiz şey tipik aylık aralıklardır: {pick_name} ile {pick_audience} yeni abone ve {pick_likes} beğeni; bu insanlar ikisinden önce de izler."),
            ("YouTube izlenme satın almak için bir uygulama var mı?", "Uygulama kullanmıyoruz. Sitemizde bir paket seçer, Stripe üzerinden öder ve kampanyanızı herhangi bir tarayıcıdan hesap panelinizde takip edersiniz."),
            ("Premium YouTube izlenmesi nedir?", "YouTube'un tanıdığı bir şey değil. YouTube Premium izleyiciler için bir aboneliktir, kimsenin size satabileceği bir izlenme türü değil. Sahip olmaya değer tek izlenme, oynat tuşuna kendisi basan insanlarınkidir."),
            ("Satın alınan izlenmeler bir videoyu viral yapabilir mi?", "Buna kimse söz veremez. Gerçek izleyiciler bir videoya, onu paylaşabilecek daha çok insan kazandırır; viral olma şansının dürüst hali de budur."),
            ("İzlenmeler kanalımın para kazanmasına yardım eder mi?", "Ne para kazanma ne de izlenme saati sözü veririz. Yapay izlenmeler buna hiç sayılmaz; gerçek izleyiciler videolarınızı izleyebilir, ama kimin para kazanacağına YouTube karar verir."),
        ],
    },
    {
        "service": "views",
        "modifier": "gradual",
        "slug": "youtube/izlenme/kademeli",
        "label": "Kademeli YouTube izlenme",
        "title": "Yavaş YouTube İzlenme: Hızı İnsanlar Belirler | Growsterr",
        "description": "Ay boyunca birikerek gelen yavaş YouTube izlenmesi: gerçek izleyiciler kanalınızı azar azar bulur, abone ve beğeniler de aynı insanlardan. Başlangıç: {from_price}.",
        "h1": ("Yavaş YouTube izlenme satın almak mı? ", "Gerçek izleyiciler zaten başka türlü gelmez."),
        "intro": "YouTube izlenmeyi yavaş satın almak istemek iyi bir içgüdü: günler içinde izlenme kazanan bir video, insanların bulduğu bir videodur. Burada kimsenin o hızı açması gerekmez. Gerçek insanlar ayın her günü kanalınızı keşfeder ve ilgilerini çekeni izler; böylece izlenmeleriniz büyüyen her kanalda olduğu gibi birikir.",
        "hero": {"image": "youtube-viewers", "alt": "Birkaç hafta boyunca bir YouTube kanalını tek tek keşfeden izleyiciler"},
        "sections": [
            {
                "h2": "Planlanmış bir damlatma aynı şey değildir",
                "p": [
                    "Damla damla bir plan, üretilmiş oynatmaları bir saat yerine bir haftaya yayar. Sayaç daha sakin yükselir, ama oynatmalar yine gerçek izleme, beğeni ve abone olmadan gelir. YouTube yalnızca izleyicilerin ne kadar hızlı geldiğine değil, ne yaptıklarına da bakar.",
                ],
            },
            {
                "h2": "Eski videolarınız da izlenir",
                "p": [
                    "Haftalar içinde gelen izleyiciler yalnızca en yeni videonuzu izlemez. Bir videodan keyif alan biri kanal sayfanızdan bir başkasını açabilir; böylece eski videolar da aynı acelesiz hızla izlenme toplar. Tek bir bağlantıya yöneltilmiş bir damlatma bunu yapamaz.",
                ],
                "image": {"image": "youtube-channel", "alt": "Eski videolarından oluşan ızgarası yeni izlenmeler toplayan bir YouTube kanal sayfası"},
            },
            {
                "h2": "Takip edebileceğiniz bir hız",
                "p": [
                    "Panel oynatmaları değil insanları izler: kampanyadan kanalınıza gelen günlük ziyaretler ve aralarındaki aboneler. İzlenmeler orada yok, çünkü onları önceden saymıyoruz; onları YouTube Studio'da, insanların seçtiği videolarda bulursunuz.",
                ],
            },
        ],
        "faqs": [
            ("Güvenebileceğim günlük bir izlenme rakamı var mı?", "Verilecek günlük bir rakam yok: her izlenme birinin izlemeye karar vermesine bağlıdır. Bekleyebileceğiniz şey, ilk gün bir sıçrama değil, ayın her günü yeni izleyicilerdir."),
            ("İzlenmeleri belirli sayıda güne yayabilir miyim?", "Her kampanya 30 güne yayılır ve her ay yenilenir. O süre içinde hızı gerçek insanlar belirler, bu yüzden izlenmeleri günlere göre planlamayız."),
            ("Yavaş izlenmeler YouTube'a daha mı doğal görünür?", "Hız işin yalnızca bir parçası. YouTube izleyicilerin izlemeye devam edip etmediğini, videoyu beğenip beğenmediğini ve geri gelip gelmediğini de görür. Gerçek insanlar bunları her hızda yapar; planlanmış oynatmalar asla yapmaz."),
            ("Geçen yıl yüklediğim videolar ne olacak?", "Onlar da işin içinde. Bir videodan keyif alan insanlar kanalınızda başka ne olduğuna bakma eğilimindedir; eski videolar da çoğu zaman bir sonraki durakları olur."),
            ("İzlenmeleri daha hızlı istersem?", "Daha büyük bir paket seçin; böylece kanalınızı her gün daha çok insan görür. Bir saat içinde binlerce izlenme vaat eden her şey izleyici bulmuyor, oynatma üretiyordur."),
        ],
    },
    {
        "service": "views",
        "modifier": "high-retention",
        "slug": "youtube/izlenme/izlenme-suresi",
        "label": "Yüksek izlenme süreli YouTube izlenme",
        "title": "YouTube İzlenme Süresi Satın Al? Dürüst Bir Cevap | Growsterr",
        "description": "YouTube izlenme süresi satın alınamaz: izleyiciyi tutan şey videonun kendisidir. İzlemeye isteyerek başlayan gerçek izleyiciler getiririz. Başlangıç: {from_price}.",
        "h1": ("YouTube izlenme süresi satın almak mı? ", "İzlemek isteyen insanları getirin."),
        "intro": "YouTube izlenme süresi ya da yüksek tutma oranlı izlenme satın almak istiyorsanız, bir oynatma sayısının asıl mesele olmadığını zaten biliyorsunuz: kalan izleyiciler istiyorsunuz. Ama izlenme süresi kimsenin satabileceği bir şey değil; gerçek insanların izlemeye ne kadar devam etmeyi seçtiğidir. Bizim payımız oynat tuşuna isteyerek basan izleyiciler getirmek; ne kadar kalacakları videonuza bağlı.",
        "hero": {"image": "youtube-channel", "alt": "İzleyicileri izlemeye devam ettirmek için uzun bir YouTube videosunu düzenleyen içerik üreticisi"},
        "sections": [
            {
                "h2": "Satın alınabilen izlenme süresi bir zamanlayıcıdır",
                "p": [
                    "Bir satıcı belirli bir izlenme süresine sahip izlenmeler sunduğunda, arkasında belirli bir saniye boyunca oynayacak şekilde ayarlanmış bir oynatıcı vardır. Ekranda ne olursa olsun aynı şekilde izler; asla beğenmez, yorum yapmaz ya da abone olmaz. Ne kadar uzun oynarsa oynasın yapay etkileşimdir ve YouTube onu spam sayar.",
                ],
            },
            {
                "h2": "Gerçek izleyiciler izlenme süresine neden anlam katar?",
                "p": [
                    "İzlenme süresi önemlidir, çünkü bir videoya başlayanların izlemeye devam etmek istediğini gösterir. Bu ancak videoyu en başta kendileri seçtiklerinde geçerlidir. Gerçek izleyiciler size dürüst veri verir: nerede kaldıklarını, nerede çıktıklarını ve onları neyin geri getirdiğini.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Uzun bir YouTube videosunu sonuna kadar izlemek için öne eğilen bir izleyici"},
            },
            {
                "h2": "Sizin tarafınızda izlenme süresini ne artırır?",
                "ul": [
                    "Başlığın ve küçük resmin vaat ettiğini ilk saniyelerde verin.",
                    "Yavaş girişi kesin: önce asıl şeyi gösterin, sonra açıklayın.",
                    "Uzun videolara bölümler ekleyin ki izleyiciler çıkıp gitmek yerine aradıkları yere atlasın.",
                    "İzleyicilerin nerede düştüğünü YouTube Studio'da bulun ve bir sonraki videonuzda o anı düzeltin.",
                ],
            },
        ],
        "faqs": [
            ("İzlenme süresi yüzdesi ya da izlenme saati sözü veriyor musunuz?", "Hayır. İzlenme süresi videoya ve her izleyiciye bağlıdır. İzlemeyi seçen gerçek insanlar getiririz ve ne kadar kalacaklarına asla bir sayı koymayız."),
            ("İnsanlar videomun tamamını izler mi?", "Bazıları izler, bazıları izlemez; verilerini işe yarar kılan da tam olarak bu. YouTube Studio insanların nerede kaldığını ve nerede çıktığını gösterir."),
            ("Yüksek izlenme süreli izlenmeler para kazanmaya sayılır mı?", "Yapay izlenmeler, izlenme süreleri ne olursa olsun para kazanmaya hiç sayılmaz. Gerçek izleyicilerin izlenme süresi gerçektir, ama asla para kazanma sözü vermeyiz; bu YouTube'un kararıdır."),
            ("Kampanya izleyicileri tek bir videoya yönlendirebilir mi?", "Evet: sipariş verirken ya da sonra hesabınızdan, yeni izleyicilerin varacağı bir videoyu belirtebilirsiniz. Ne kadar izleyecekleri ise yine onlara ve videoya kalmıştır; bunun için bir süre vaat etmeyiz."),
            ("En çok hangi videolar fayda görür?", "Vaadini tutan videolar. Net bir açılış, dürüst bir küçük resim ve istikrarlı bir tempo yeni izleyicileri uzun izlemelere dönüştürür; kampanya kanalınıza ne kadar çok insan getirirse, bu videolar o kadar fazlasını tutabilir."),
        ],
    },
    {
        "service": "views",
        "modifier": "live",
        "slug": "youtube/izlenme/canli-yayin",
        "label": "YouTube canlı yayın izlenmesi",
        "title": "YouTube Canlı Yayın İzleyicisi: Gerçek Kitle Kurun | Growsterr",
        "description": "Kimse bir YouTube canlı yayınını belirli bir saatte gerçek insanlarla dolduramaz. Bir sonrakine katılabilecek aboneleri büyütürüz. Başlangıç: ayda {from_price}.",
        "h1": ("YouTube canlı yayın izleyicisi satın almak mı? ", "Gelecek kitleyi kurun."),
        "intro": "YouTube canlı yayın için izlenme satın almak istiyorsanız, başlat tuşuna bastığınızda boş hissettirmeyen bir yayın istiyorsunuz. Kimse belirli bir dakikada bir yayına gerçek insan teslim edemez, biz de bunu iddia etmiyoruz. Yaptığımız şey kanalınızı her gün gerçek abonelerle büyütmek; böylece her canlı yayında katılabilecek daha çok insan olur.",
        "hero": {"image": "youtube-channel", "alt": "Ekranda planlanmış bir yayınla YouTube'da canlıya geçmek üzere olan bir içerik üreticisi"},
        "sections": [
            {
                "h2": "Satın alınan canlı yayın sayısı neden geri teper?",
                "p": [
                    "İzleyici sayısı, bir canlı yayında herkesin ilk gördüğü şeydir. Yüzlerce der de sohbet sessizse, her gerçek ziyaretçi fark eder. Satın alınan canlı yayın izleyicileri yazmaz, tepki vermez ve tekrar için geri gelmez.",
                    "YouTube'un sahte izlenme kuralları siz canlıya geçince durmaz. Canlı yayın sayısı, taklit için daha güvenli bir yer değildir.",
                ],
            },
            {
                "h2": "Bir yayına kim, ne zaman katılır?",
                "p": [
                    "Katılma ihtimali en yüksek olanlar kanalınızı zaten tanıyan abonelerdir. Ayarlarına bağlı olarak YouTube onlara yayınınızı akışlarında gösterebilir ya da bildirim gönderebilir.",
                ],
                "ul": [
                    "Yayını önceden planlayın ki aboneler hatırlatıcı kurabilsin.",
                    "Yayın saatinizin akşama denk geldiği bir kitle konumu seçin.",
                    "Düzenli bir günde canlıya geçin ki izleyiciler ne zaman geri geleceklerini öğrensin.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Akşam saatlerinde telefonlarından planlanmış bir YouTube canlı yayınına katılan izleyiciler"},
            },
            {
                "h2": "Tekrar, izlenme kazanmaya devam eder",
                "p": [
                    "Yayın bittiğinde kanalınızda bir video olarak kalır. Canlı kaçıran yeni aboneler tekrarı orada bulup istedikleri zaman izleyebilir.",
                ],
            },
        ],
        "faqs": [
            ("Ben yayındayken yayınımı doldurabilir misiniz?", "Hayır. Gerçek insanlar seçtikleri zaman izler, bu yüzden belirli bir saatte kimseyi vaat edemeyiz. Yayınlarınızın beslendiği abone tabanını büyütürüz."),
            ("Seçtiğim konum yayınlar için önemli mi?", "Normal videolardan daha da önemli. Kitlenizin yaşadığı yeri seçin; yayın saatiniz onların gece yarısına değil, gününe denk gelsin."),
            ("Tekrar kampanyadan izlenme alır mı?", "Alabilir. Tekrar kanalınızda bir videodur; yayından sonra sizi bulan izleyiciler onu diğer videolar gibi izleyebilir."),
            ("Sayaç için canlı yayın izleyicisi satın alamaz mıyım?", "Alabilirsiniz, ama geri teper. Bir yayındaki yapay izleyiciler diğerleri gibi sahte etkileşimdir; boş bir sohbetin üstündeki dolu bir sayaç da gerçek izleyicilerin kolayca fark ettiği bir şeydir."),
            ("Yayın yapan bir kanala hangi paket uygun?", "{pick_name} en popüler paketimiz, genellikle ayda {pick_audience} yeni abone; yeni bir kanal {starter_name} ile başlayabilir. Sonrasındaki her yayında katılabilecek daha çok insan olur."),
        ],
    },
    {
        "service": "views",
        "modifier": "monthly",
        "slug": "youtube/izlenme/aylik",
        "label": "Aylık YouTube izlenme",
        "title": "Birden Çok Videoya YouTube İzlenme, Aylık | Growsterr",
        "description": "Zamanla birden çok videoya YouTube izlenme: aylık bir paket bütün kanalınıza gerçek izleyiciler getirir, ne izleyeceklerini onlar seçer. Başlangıç: {from_price}.",
        "h1": ("Birden çok videoya YouTube izlenme satın alın, ", "aydan aya."),
        "intro": "Birden çok videoya YouTube izlenme satın aldığınızda asıl istediğiniz, insanların geri gelmeye devam ettiği bir kanaldır. Aylık paket tam da bunun için kuruldu: gerçek insanlar kanalınızı her gün keşfeder ve ilgilerini çeken videoları izler; kampanya her ay yenilenir, böylece yeni videolar yeni izleyicilerle buluşmaya devam eder.",
        "hero": {"image": "youtube-viewers", "alt": "Aynı kanalda bir YouTube videosundan diğerine geçen bir izleyici"},
        "sections": [
            {
                "h2": "Tek kanal, birçok video",
                "p": [
                    "İlgilenen izleyiciler tek bir videoda durmaz. Sizi bir eğitim videosuyla bulan biri bir sonrakini, sonra kanal sayfanızın önerdiğini açar. Tek bir bağlantı yerine kanalınızın etrafında kurulan bir kampanya, insanların gerçekte nasıl izlediğini izler.",
                ],
            },
            {
                "h2": "Yeni izleyicilerin sonra nereye gideceğini şekillendirmek",
                "p": [
                    "Kanalınızı bir bütün olarak tanıtırız; hangi videoları açacaklarına izleyiciler karar verir. Sizin kontrolünüzde olan, geldiklerinde önlerine çıkan yoldur.",
                ],
                "ul": [
                    "Henüz abone olmamış ziyaretçiler için bir kanal fragmanı ayarlayın.",
                    "En güçlü videonuzu kanal sayfanızın en üstünde öne çıkarın.",
                    "İlgili videoları oynatma listelerinde toplayın ki biri diğerine götürsün.",
                    "İzleyicinin bundan sonra izlemesi gereken videoyu gösteren bitiş ekranları ekleyin.",
                ],
            },
            {
                "h2": "Zamana yaymak neden hepsi birden olmaktan iyidir?",
                "p": [
                    "Bir aya yayılan izlenmeler her videoya yeniyken ulaşır ve eskilerini canlı tutar. Birkaç videoya tek seferlik bir patlama ise tersini yapar: her birinde bir sıçrama, sonra sessizlik.",
                ],
                "image": {"image": "youtube-channel", "alt": "Ay boyunca yayımlamak üzere bir dizi YouTube videosunu sıraya koyan bir içerik üreticisi"},
            },
        ],
        "faqs": [
            ("İzlenmeler kaç videoya gidebilir?", "Ne bir liste ne de bir sınır var. Kanalınızı tanıtırız, izleyiciler de kanalınızın herhangi bir yerinde ilgilerini çekeni izler."),
            ("Ay içinde yüklediğim yeni videolar izlenme alır mı?", "Evet. Kampanya her gün çalışır; ayın ortasında yayımladığınız bir video da yeni insanlarla buluşur ve yeni aboneleriniz onu her abone gibi görebilir."),
            ("Fiyat video başına mı?", "Hayır, bütün kanalınız için aylıktır: kaç videonuz olursa olsun {starter_name} ayda {starter_price}, {rising_name} {rising_price}, {pro_name} {pro_price}. İzlenmeler abone, beğeni ve yorumlarla birlikte içinde gelir."),
            ("Bir aydan sonra durdurabilir miyim?", "Evet. Hesabınızdan iptal edin; ödenen ay normal şekilde biter ve bir sonraki ay için ödeme alınmaz."),
            ("İzlenmeler tek bir şehirden gelebilir mi?", "Evet. Tek bir şehir de olur, bir bölge ya da bütün bir ülke de. Bu, bir şehir yemek rehberi ya da yerel bir haber kanalı gibi yerel kitlesi olan kanallara uyar."),
        ],
    },
    {
        "service": "views",
        "modifier": "no-drop",
        "slug": "youtube/izlenme/dusmeyen",
        "label": "Düşmeyen YouTube izlenme",
        "title": "Düşmeyen YouTube İzlenme: Sayılar Neden Düşer? | Growsterr",
        "description": "Satın almadan sonra YouTube izlenme sayıları neden düşer ve oynat tuşuna kendisi basan insanların izlenmeleri neden farklıdır. Başlangıç: ayda {from_price}.",
        "h1": ("Düşmeyen gerçek YouTube izlenme mi? ", "Hiç sahte olmamış izlenmelerle başlayın."),
        "intro": "Düşmeyen gerçek YouTube izlenme satın almak isteyen herkes genellikle bir sayının düştüğünü görmüştür. İzlenmeler, YouTube yapay saydığı oynatmaları sildiğinde düşer. Bizimkiler aylık bir paketin içinde, oynat tuşuna basmayı seçen gerçek insanlardan gelir; yani geri alınmayı bekleyen sahte bir oynatma yığını yoktur.",
        "hero": {"image": "youtube-channel", "alt": "Stüdyosunda bir YouTube videosunun sabit kalan izlenme sayısına bakan bir içerik üreticisi"},
        "sections": [
            {
                "h2": "İzlenme sayıları neden düşer?",
                "p": [
                    "YouTube izlenmeleri inceler ve gerçek saymadıklarını siler: botlardan, yazılımlardan ve diğer yapay trafikten gelen oynatmaları. Bu bir satın almadan sonra olduğunda sayı düşer, bazen teslimattan çok sonra; videonun geçmişi de bir sıçramanın ardından bir düşüş gösterir.",
                ],
            },
            {
                "h2": "Neye söz verebiliriz, neye veremeyiz?",
                "p": [
                    "YouTube'un bir sayıyı asla düzeltmeyeceğine söz veremeyiz; bizimkiler dahil bütün trafiği kontrol eder. Size söyleyebileceğimiz, izlenmelerimizin nasıl oluştuğudur: gerçek bir insan kanalınızı bir tanıtım kampanyasıyla görür ve izlemeyi seçer. YouTube'un kontrollerinin korumak için var olduğu izlenme türü budur.",
                ],
            },
            {
                "h2": "İzlenme, beğeni ve aboneler birlikte yükseldiğinde",
                "p": [
                    "Gerçek izlenmeler nadiren tek başına gelir. Pakette aynı insanlardan gelen yeni abone, beğeni ve yorumlarla birlikte gelirler; rakamlarınız birlikte yükselir ve içlerinde ne YouTube'a ne de bir izleyiciye yersiz görünen bir şey olur.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Bir YouTube videosunu birlikte izleyip bittiğinde beğeni bırakan arkadaşlar"},
            },
        ],
        "faqs": [
            ("İzlenmelerim hiç düşer mi?", "YouTube trafiği incelerken herhangi bir videonun sayısını düzeltebilir; bu yüzden dürüst olan kimse hiç oynamayan bir sayı vaat edemez. İzlemeyi seçen insanların izlenmeleri, incelemenin korumak üzere tasarlandığı türdendir."),
            ("Sayı düşerse izlenmeleri tamamlar mısınız?", "Hayır. Telafi, silinen sahte oynatmaları yenileriyle değiştirir. Biz bunun yerine aylık bir gerçek insan paketi satıyoruz; yerine konacak yapay bir şey yok."),
            ("Önceki bir satın almadan sonra izlenmelerim neden düştü?", "Çoğu zaman YouTube yapay saydığı oynatmaları sildiği için. Bu teslimattan haftalar sonra olabilir; düşüşün sürpriz gibi gelmesinin nedeni de bu."),
            ("Tek bir video için düşmeyen izlenme satın alabilir miyim?", "Tek bir sipariş olarak hayır. İzlenmeler bütün kanalınızı büyüten aylık bir paketin içinde gelir; böylece her video fayda görebilir."),
            ("İzlenmelerle birlikte başka ne gelir?", "Gerisini izleyiciler kendileri getirir. {pick_name} ile genellikle ayda {pick_audience} abone, {pick_likes} beğeni ve {pick_comments} yorum."),
        ],
    },
    {
        "service": "views",
        "modifier": "organic",
        "slug": "youtube/izlenme/organik",
        "label": "Organik, hedefli YouTube izlenme",
        "title": "Hedefli YouTube İzlenme: Şehir ya da Ülke Seçin | Growsterr",
        "description": "Kitlenizin yaşadığı şehir, bölge ya da ülkeden hedefli YouTube izlenme: izlemeyi seçen organik izleyiciler, aylık bir pakette. Başlangıç: ayda {from_price}.",
        "h1": ("Hedefli YouTube izlenme satın alın, ", "kitlenizin yaşadığı yerden."),
        "intro": "Hedefli YouTube izlenme satın almak için izleyicilerinizin nerede olması gerektiğini söyleyin: bir şehir, daha geniş bir bölge ya da bütün bir ülke. Kanalınızı oradaki gerçek insanlara tanıtım kampanyalarıyla gösteririz; izlenmeler de önemli olan anlamda organiktir: her biri izlemeyi seçmiş biridir.",
        "hero": {"image": "youtube-channel", "alt": "Yerel bir kitle için şehir sokağında YouTube videosu çeken bir içerik üreticisi"},
        "sections": [
            {
                "h2": "Neden önemli olan hedefleme konumdur?",
                "p": [
                    "İzmir'de bir yemek kanalı, Dubai'de bir emlak kanalı, Türkçe yayın yapan bir oyun kanalı: her birinin bir yerde yaşayan ve bir dil konuşan bir kitlesi var. O yerden gelen izleyiciler videolarınızı anlar, bir sonraki için geri gelir ve bir şey satıyorsanız müşteri olabilir.",
                    "Kampanyanızı önce seçtiğiniz yere yöneltiriz. Kanalınız için en yakın eşleşme hemen sınırın ötesindeki daha büyük bir kitleyse, izleyicilerinizin bir kısmı oradan gelebilir.",
                ],
            },
            {
                "h2": "Hedefli, zorla demek değil",
                "p": [
                    "İnsanların bulunduğu yeri hedefleriz, sonra karar vermelerine izin veririz. Kimse videonuzu izlemeye zorlanmaz ve seçilmemiş hiçbir şey oynamaz. Hedefli bir izlenme yine bir seçimdir; onu organik yapan da budur.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Bir kafede kendi şehirlerinde çekilmiş bir YouTube videosunu izleyen yerel izleyiciler"},
            },
            {
                "h2": "Konumunuzu nasıl seçmelisiniz?",
                "ul": [
                    "Sayabileceğiniz en büyük yeri değil, videolarınızın yapıldığı yeri seçin.",
                    "Yerel bir işletme ya da şehir kanalı için şehrin kendisini seçin.",
                    "Bir yer yerine bir dil hedefliyorsanız, o dili konuşanların çoğunun yaşadığı ülkeyi seçin.",
                    "Uluslararası bir niş için en çok ulaşmak istediğiniz izleyicilerin ülkesiyle başlayın.",
                ],
            },
        ],
        "faqs": [
            ("Hedefleme ne kadar hassas?", "Bir şehir kadar hassas. Yer ne kadar küçükse kitlesi de o kadar küçüktür; bu yüzden küçük bir kasabada izleyicilerin bir kısmı çevre bölgeden gelebilir."),
            ("Hedefleme izlenmeleri daha az organik yapar mı?", "Hayır: izleme kararı onlarda kalır. Kanalınızı seçtiğiniz yerde göstermek için ödeme yaparız; sonra her izleyici kendisi karar verir ve kimse izlediği için ödüllendirilmez."),
            ("Şehrimden gelen izleyiciler abone olur mu?", "Kanalınız onlara hitap ediyorsa bazıları olur. {pick_name} ile genellikle ayda {pick_audience} yeni abone; seçtiğiniz yerden ve çevresinden."),
            ("Neden mümkün olan en geniş alanı seçmeyelim?", "Daha büyük bir alan daha büyük bir havuz demektir, ama dilinizi ya da bağlamınızı paylaşmayan izleyiciler nadiren kalır. Doğru yer, en büyük yeri yener."),
            ("İzleyicileri hedeflemek için kanalıma erişiminiz gerekir mi?", "Hayır. Hedefleme kanal ayarlarınızda değil, kampanyalarımızda olur. Kullanıcı adınıza ve bir konuma ihtiyacımız var, şifrenize asla."),
        ],
    },
    {
        "service": "views",
        "modifier": "promote",
        "slug": "youtube/izlenme/tanitim",
        "label": "YouTube videolarınızı tanıtın",
        "title": "Reklamla YouTube İzlenme mi, Bizim Tanıtım mı? | Growsterr",
        "description": "Google Ads ile YouTube izlenmesi mi düşünüyorsunuz? Kanalınızı sizin için her ay gerçek insanlara tanıtırız; abone, beğeni ve yorumla. Başlangıç: {from_price}.",
        "h1": ("Reklamla YouTube izlenme mi? ", "Ya da tanıtımı biz yürütelim."),
        "intro": "Google Ads (eski adıyla AdWords) üzerinden YouTube izlenme satın almak isteyenler, bir videoyu ücretli erişimle tanıtmak ister. Google'ın kendi reklamları bir yoldur: Google'ın reklam araçlarında kurduğunuz, yönettiğiniz ve ödediğiniz bir kampanya. Biz başka bir yoluz. Kanalınızı her gün iş ortağı ağımızdaki kampanyalarla gerçek insanlara tanıtırız; sonuçları da panelinizden takip edersiniz.",
        "hero": {"image": "youtube-viewers", "alt": "Telefon ve tabletlerinde tanıtılan bir YouTube videosunu keşfeden insanlar"},
        "sections": [
            {
                "h2": "Reklamları kendiniz yürütmek ya da yönetilen bir kampanya",
                "p": [
                    "AdWords'ün yerini alan Google Ads ile kampanyayı kendiniz kurarsınız: kitle, teklifler, bütçe ve reklamın kendisi. Sistem gösterim yaptıkça ödersiniz; göz kulak olmak da sizin işinizdir.",
                    "Bir Growsterr paketi işin sizin yerinize yapılan tarafıdır. Bize kanal kullanıcı adınızı ve bir hedef konum verirsiniz; ekibimiz tanıtımı her gün yürütür, paneliniz de kanal ziyaretlerini ve yeni aboneleri gösterir. Tek bir aylık fiyat, yönetilecek teklif yok.",
                ],
            },
            {
                "h2": "Tanıtılan bir izlenme neye götürmeli?",
                "p": [
                    "Ücretli bir izlenme ancak izleyici sonra bir şey yaparsa karşılığını verir: başka bir video izler, beğenir, abone olur. Paketlerimizin bir oynatma sayısı yerine abonelerin etrafında, aynı insanlardan gelen beğeni, yorum ve izlenmelerle kurulmasının nedeni bu.",
                ],
                "image": {"image": "youtube-channel", "alt": "Bir tanıtım başladıktan sonra YouTube videosunun yeni abonelerine bakan bir içerik üreticisi"},
            },
            {
                "h2": "Yapmadıklarımız",
                "ul": [
                    "Google Ads kurmuyor ya da yönetmiyoruz ve Google hesabınıza asla erişim istemiyoruz.",
                    "İzlenmeyi biner biner ya da izlenme başına fiyatla satmıyoruz.",
                    "Yeni izleyicilerin varacağı bir videoyu belirtebilirsiniz, ama tanıtımı bir lansman saatine göre zamanlamıyoruz.",
                    "Para kazanma, izlenme saati ya da önerilerde bir yer sözü vermiyoruz.",
                ],
            },
        ],
        "faqs": [
            ("Bu, YouTube reklamı yürütmekle aynı şey mi?", "Hayır. YouTube reklamları kendi Google Ads hesabınızda, kendi bütçeniz ve ayarlarınızla yürür. Biz kanalınızı iş ortağı ağımız üzerinden tanıtır ve kampanyayı sizin için yürütürüz; hesabınızda hiçbir şey çalışmaz."),
            ("Google Ads kampanyalarımı yönetebilir misiniz?", "Bu sunduğumuz bir şey değil. İşimiz aylık büyüme paketleri; daha büyük bir şey için bize WhatsApp'tan ya da e-postayla yazın."),
            ("Maliyet reklamlardan nasıl farklı?", "Reklamlar gösterim yaptıkça ücretlendirir; harcamanız tekliflerinize ve bütçenize göre değişir. Paketlerimizin sabit bir aylık fiyatı var: {starter_price}, {rising_price} ya da {pro_price}; abone, beğeni ve yorum için tipik aralıklarla."),
            ("Aynı anda kendi reklamlarımı yürütebilir miyim?", "Evet. Reklamlarınız sizin hesabınızda, kampanyamız bizim ağımızda yürür; biri diğerinin önüne geçmez."),
            ("Hangi videoları tanıtıyorsunuz?", "Tek bir videoyu değil, kanalınızı bir bütün olarak; ne izleyeceklerini izleyiciler seçer. Bir lansmanı ya da yeni bir seriyi kanalınızın öne çıkan alanına koymak, yeni ziyaretçilerin onu bulmasına yardım eder."),
        ],
    },
    {
        "service": "views",
        "modifier": "real",
        "slug": "youtube/izlenme/gercek",
        "label": "Gerçek YouTube izlenme",
        "title": "Kaliteli YouTube İzlenme: Her Biri Bir İnsan | Growsterr",
        "description": "İzlemeyi seçen gerçek insanlardan kaliteli YouTube izlenmesi; aynı izleyicilerden abone, beğeni ve yorumla aylık bir pakette. Başlangıç: ayda {from_price}.",
        "h1": ("Kaliteli YouTube izlenme satın almak mı? ", "Her oynatmanın arkasında bir insan olsun."),
        "intro": "Kaliteli YouTube izlenme satın almadan önce kaliteyi tanımlamak işe yarar. Bize göre kaliteli bir izlenmenin arkasında bir insan vardır: kanalınızı gören, bir video seçen ve ilgisini çektiği için izleyen biri. Paketlerimizin getirdiği tek tür bu; aynı insanlar abone de olur, beğenir ve yorum yapar.",
        "hero": {"image": "youtube-viewers", "alt": "Bir içerik üreticisinin kanalından izleyeceği YouTube videosunu seçen gerçek bir izleyici"},
        "sections": [
            {
                "h2": "Gerçek bir izlenmeyi oynatmadan ayıran nedir?",
                "ul": [
                    "Onu bir insan seçti: kimseye oynat tuşuna basması için ödeme yapılmadı, hiçbir yazılım bastırmadı.",
                    "Bir yere varır: bazı izleyiciler beğenir, yorum yapar ya da abone olur.",
                    "Bir yeri vardır: izleyici, kampanyayı yönelttiğiniz yerde yaşar.",
                    "Sağlamdır: içinde YouTube'un sileceği yapay hiçbir şey yoktur.",
                ],
            },
            {
                "h2": "Sınıflandırılmış bot izlenmeleri neden yine kaliteli değil?",
                "p": [
                    "Bazı satıcılar izlenmelerini standart, yüksek kalite ya da premium diye sınıflar. Etiket ne olursa olsun önemli olan soru aynı kalır: bir insan izlemeyi seçti mi? Seçmediyse, daha yüksek bir sınıf yalnızca aynı boş oynatma için daha yüksek bir fiyat demektir.",
                ],
            },
            {
                "h2": "YouTube Studio'da okuyabileceğiniz kalite",
                "p": [
                    "Gerçek izlenmeler iz bırakır: izleyiciden izleyiciye değişen izlenme süresi, videonuza cevap veren yorumlar ve insanların izlediği videolarda kazanılan aboneler. Bir izlenmeyi sahip olmaya değer kılan bu izlerdir; üretilmiş oynatmalar ise asla iz bırakmaz.",
                ],
                "image": {"image": "youtube-channel", "alt": "Analizlerinde bir YouTube videosunun izlenme süresini ve yorumlarını okuyan bir içerik üreticisi"},
            },
        ],
        "faqs": [
            ("Kaliteli bir izlenme ucuz olandan nasıl farklıdır?", "Ucuz bir izlenme genellikle ardından hiçbir şey gelmeyen bir oynatmadır. Kaliteli bir izlenme beğenebilecek, yorum yapabilecek, abone olabilecek ya da geri gelebilecek bir insandır; kanalınıza yalnızca bu tür yardım eder."),
            ("İzleyicilerin kim olduğunu görebilir miyim?", "Paneliniz kampanyanızın kanal ziyaretlerini ve yeni aboneleri gösterir; YouTube Studio da izleyicilerin nerede olduğunu ve ne kadar izlediğini. Tek tek izleyiciler, her kanalda olduğu gibi gizli kalır."),
            ("İzlenmeler abone ya da beğeni olmadan gelir mi?", "Hayır. Aynı insanlardan tek bir pakette gelirler; onları bir sayı değil büyüme yapan da budur."),
            ("Neden bin izlenmelik paketler yok?", "Çünkü sipariş üzerine bin izlenme, birinin ürettiği bin oynatma demektir. İnsan getirmeyi ve ne izleyeceklerini onlara bırakmayı tercih ederiz."),
            ("İzleyicilerin nerede yaşadığını seçebilir miyim?", "Evet: sipariş verirken yeri söyleyin, tek bir şehirden bütün bir ülkeye kadar. Yerel izleyiciler videolarınızı anlar; izlenmelerini bir sayıdan daha değerli kılan da budur."),
        ],
    },
    {
        "service": "views",
        "modifier": "safe",
        "slug": "youtube/izlenme/guvenilir",
        "label": "Güvenilir YouTube izlenme",
        "title": "Güvenilir YouTube İzlenme: Kanalı Ne Korur? | Growsterr",
        "description": "YouTube izlenmeyi meşru ve güvenli mi almak istiyorsunuz? YouTube neyi sahte sayar, kanalınız için riski ne ve gerçek izleyiciler size bizimle nasıl ulaşır.",
        "h1": ("Güvenilir YouTube izlenme mi? ", "Bir kanalı neyin riske attığını bilin."),
        "intro": "YouTube izlenmeyi meşru ve güvenli bir şekilde satın almak istiyorsanız, YouTube'un neye karşı önlem aldığıyla başlayın: botlardan, yazılımlardan ve izlemeyi seçen bir insan olmayan her türlü trafikten gelen izlenmeler. Kanalınızı yalnızca isterlerse izleyen gerçek insanlara tanıtarak bu çizginin doğru tarafında kalırız.",
        "hero": {"image": "youtube-channel", "alt": "Sessiz bir ev ofisinde YouTube kanalının durumunu inceleyen bir içerik üreticisi"},
        "sections": [
            {
                "h2": "YouTube neyi sahte izlenme sayar?",
                "p": [
                    "YouTube'un sahte etkileşim kuralları aşağıdakilerin hepsini kapsar. İzlenmeleri silebilir; bunlarla şişirilmiş içerikler de kaldırılabilir.",
                ],
                "ul": [
                    "Botlardan ya da otomatik yazılımlardan gelen oynatmalar.",
                    "İzlemeleri için ödeme yapılan ya da ödüllendirilen insanlardan gelen izlenmeler.",
                    "İzleyicilerin hiç seçmediği yerlerde kendiliğinden oynatılan videolar.",
                    "Kanallar arasında takas edilen izlenmeler.",
                ],
            },
            {
                "h2": "İzlenmelerimiz nasıl gelir?",
                "p": [
                    "İş ortağı ağımız, kanalınızı gerçek insanların önüne çıkaran tanıtım kampanyaları yürütür. Kimseye izlemesi için ödeme yapılmaz, seçilmeden hiçbir şey oynamaz ve YouTube hesabınıza hiçbir şey dokunmaz. Gördüğünü beğenenler daha fazla izler, beğenir, yorum yapar ve abone olur.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Telefonunda tanıtılan bir YouTube videosunu izlemeyi seçen bir izleyici"},
            },
            {
                "h2": "Hesabınız için de güvenli",
                "ul": [
                    "Herkese açık kanal kullanıcı adınızla çalışırız: giriş yok, erişim talebi yok.",
                    "Faturalandırma, hesabınızdan yönettiğiniz aylık bir Stripe aboneliğidir.",
                    "Bitirmek size kalmış; istediğiniz an, kimseye açıklama yapmadan.",
                ],
            },
        ],
        "faqs": [
            ("İzlenme satın almak videomun kaldırılmasına yol açabilir mi?", "Sahte izlenmeler açabilir: YouTube onları sayıdan çıkarabilir, sahte etkileşim kurallarını çiğneyen içerikleri de kaldırabilir. İzlemeyi seçen insanlardan gelen izlenmeler sahte etkileşim değildir."),
            ("Growsterr'ı kim yürütüyor?", "Kayıtlı şirketi Tallinn, Estonya'daki Sterr Technologies OÜ olan Sterr Agency. Ekibin merkezi Türkiye'de."),
            ("YouTube ya da Google giriş bilgilerime ihtiyacınız var mı?", "Hayır; bunu isteyen bir hizmet zaten başlı başına bir risktir. Yalnızca herkese açık kanal kullanıcı adınıza ihtiyacımız var."),
            ("YouTube'da bir videoyu tanıtmaya izin var mı?", "İnsanların keşfedebilmesi için bir videoyu tanıtmak olağandır; kanallar bunu her gün reklamlarla yapar. YouTube'un çizgiyi çektiği yer yapay ya da teşvikli izlenmelerdir ve biz o çizginin doğru tarafında kalırız."),
            ("Memnun kalmazsam ne olur?", "Aboneliği hesabınızdan durdurun, bir sonraki ay için ödeme alınmaz. Paneliniz ölçtüklerimizi gösterir; kampanyayı gerçeklere bakarak değerlendirebilirsiniz."),
        ],
    },
    {
        "service": "views",
        "modifier": "shorts",
        "slug": "youtube/izlenme/shorts",
        "label": "YouTube Shorts izlenme",
        "title": "YouTube Reels İzlenme mi? YouTube'da Adı Shorts | Growsterr",
        "description": "YouTube'da reels videolarının adı Shorts. Shorts videolarınızı izlemeye devam eden gerçek izleyiciler getiririz, abonelerle birlikte. Başlangıç: ayda {from_price}.",
        "h1": ("YouTube reels izlenme satın almak mı? ", "İzlemeye devam eden Shorts izleyicileri edinin."),
        "intro": "YouTube reels izlenme satın almak istiyorsanız Shorts'u kastediyorsunuz: YouTube'un kısa, dikey videoları. Shorts izlenmesini toptan satmıyoruz. Kanalınıza her gün gerçek insanlar getiririz; Shorts videolarınızdan keyif alanlar izler, tekrar izler, beğenir ve bazen abone olur.",
        "hero": {"image": "youtube-viewers", "alt": "Telefonda bir YouTube Shorts videosu izleyip döngüde oynamasına izin veren biri"},
        "sections": [
            {
                "h2": "Ucuz Shorts izlenmesi kolay taklit edilir, kolay anlaşılır",
                "p": [
                    "Ucuz Shorts izlenmesi her yerde, çünkü bir oynatma üretmek saniyeler sürer. Zor olan oynatmadan sonra olanlardır: izleyici izlemeye devam etti mi, tekrar izledi mi, beğendi mi, kanalınızı açtı mı? Üretilmiş oynatmalar hepsine hayır der ve YouTube onları spam sayar.",
                ],
            },
            {
                "h2": "Bir Shorts izleyicisi nasıl abone olur?",
                "p": [
                    "Shorts bir ön kapıdır. Birinden keyif alan gerçek bir izleyici adınıza dokunabilir, kanalınıza göz atabilir ve abone olabilir; o andan itibaren uzun videolarınız da ona ulaşabilir. Bir insandan gelen Shorts izlenmesinin bir oynatmadan çok daha değerli olmasının nedeni bu yoldur.",
                ],
                "image": {"image": "youtube-channel", "alt": "Yayımlamadan önce telefonda dikey bir YouTube Shorts videosunu inceleyen bir içerik üreticisi"},
            },
            {
                "h2": "Paylaştığınız Shorts videolarından daha fazlasını almak",
                "ul": [
                    "En iyi Shorts videolarınızı, meraklı izleyicilerin geldiği kanal sayfanızda kolay bulunur tutun.",
                    "Shorts videonuzdan ilgili uzun bir videoya bağlantı verin ki ilgilenen izleyicilerin gidecek bir yeri olsun.",
                    "Düzenli bir ritimle paylaşın ki yeni aboneler her ziyarette taze bir şey bulsun.",
                ],
            },
        ],
        "faqs": [
            ("YouTube reels ile Shorts aynı şey mi?", "Evet. Reels, Instagram'ın verdiği isim; YouTube'da aynı kısa dikey formata Shorts denir. Bu sayfadaki her şey Shorts için geçerlidir."),
            ("Tek bir Shorts videosu için ucuz izlenme alabilir miyim?", "Shorts başına bir fiyat yok. Paket kanalınızı tanıtır, izleyiciler de istedikleri Shorts videolarını seçer."),
            ("Shorts videolarımı Shorts akışına sokabilir misiniz?", "Bu, kimsenin dürüstçe veremeyeceği bir söz; biz de vermiyoruz. Gerçek izleyiciler getiririz; YouTube'un bir Shorts videosunu sonra nasıl yayacağı kendi kararıdır."),
            ("Neden bir Shorts izlenme sayısı vermiyorsunuz?", "Bir Shorts videosu tekrar oynatılabilir, geçilebilir ya da döngüye alınabilir; önceden vaat edilen bir izlenme sayısı ancak oynatma üreterek tutturulabilir. Biz insanların izledikten sonra yaptıkları için tipik aylık aralıklar veririz: abone olmak, beğenmek ve yorum yapmak."),
            ("YouTube Shorts izlenmesi satın almak güvenli mi?", "Bir bot hizmetinden, hayır: video otuz saniye de sürse bir saat de sürse sahte oynatma sahtedir. Shorts videolarınızı seçen gerçek izleyiciler, hangi formatta paylaşırsanız paylaşın olağan bir kitledir."),
        ],
    },
]
