UPDATED = "2026-11-09"

# Turkish Instagram intent pages: searches for things we don't sell (cheap, instant, free, free
# trial, panels, verified, female, AI or custom comments). Each answers honestly, then leads to
# the monthly package. Mirrors en/instagram_intents.py; keys and placeholders: docs/CONTENT.md.

PAGES = [
    # --- Comments -------------------------------------------------------------------------
    {
        "service": "comments",
        "modifier": "ai",
        "slug": "instagram/yorum/yapay-zeka",
        "label": "Yapay zekâ ile Instagram yorum?",
        "title": "Yapay Zekâ Instagram Yorumu mu? Biz İnsan Getiririz | Growsterr",
        "description": "Yapay zekâyla yazılmış Instagram yorumu satmıyoruz. Paketlerimizdeki her yorumu gönderinizi gören gerçek bir insan yazar; tipik bir ayda {starter_comments}.",
        "h1": ("Yapay zekâ ile Instagram yorumu mu? ", "Bizimkileri insanlar yazar."),
        "intro": "Yapay zekâ ile yazılmış Instagram yorum satın almak mı istiyorsunuz? Bunları satmıyoruz. Bir yazılımın ürettiği metin yine de bir hesaptan paylaşılmak zorundadır; kimsenin kullanmadığı bir hesap da cümleleri ne kadar zekice olursa olsun bir bottur. Paketlerimizde her yorumu, gönderinizi gören gerçek bir insan yazar: {starter_name} ile genellikle ayda {starter_comments}.",
        "hero": {"image": "instagram-real-people", "alt": "Bir içerik üreticisinin gönderisinin altına kendi yorumlarını yazan insanlar"},
        "sections": [
            {
                "h2": "Yapay zekâ yorumu gerçekte nedir?",
                "p": [
                    "Bir yazılım kıyafetiniz ya da tarifiniz hakkında bir saniyede bir cümle yazabilir. Yapamadığı şey biri olmaktır. O cümlenin gönderinizin altında görünmesi için bir hesaptan gelmesi gerekir; yalnızca üretilmiş metin paylaşmak için var olan bir hesap da daha iyi bir senaryoya sahip sahte bir profildir.",
                    "Yorumları kitleniz de okur. Bir arada gelen bir dizi cilalı, biraz genel cevap sahnelenmiş görünür ve gönderinizin altındaki gerçek sohbeti gömer.",
                ],
            },
            {
                "h2": "Bir insanın yorumu neden daha değerlidir?",
                "ul": [
                    "Bir sonraki gönderiniz için geri gelebilecek biri tarafından yazılır.",
                    "İnsanların gerçekte ne düşündüğünü söyler; neyi daha çok yapmanız gerektiğini anlarsınız.",
                    "Cevap verebileceğiniz bir sohbet açar; cevaplar da insanları geri getirir.",
                    "Paketin içinde aynı kişiden bir takip ve beğenilerle birlikte gelir.",
                ],
            },
            {
                "h2": "Yapay zekâyı kendi tarafınızda çalıştırın",
                "p": [
                    "Yapay zekâ araçlarını seviyorsanız onları işe yaradıkları yerde kullanın: açıklama fikirleri bulmak, bir carousel'i taslağa dökmek, bir aylık paylaşımı planlamak. Sonra yaptığınız şeye gerçek insanların tepki vermesine izin verin. Bu ayrım hesabınızı dürüst, yorum bölümünüzü canlı tutar.",
                ],
            },
        ],
        "faqs": [
            ("Gönderilerime yapay zekâyla üretilmiş yorum ekleyebilir misiniz?", "Hayır. Yorum üretmiyoruz ve kontrol ettiğimiz hesaplardan hiçbir şey paylaşmıyoruz. Bir paketteki her yorumu, bir şey söylemeyi seçen gerçek bir insan yazar."),
            ("O insanlara bir metin veriyor musunuz?", "Hayır. Gördükleri hakkında kendi cümleleriyle yazarlar. Bu yüzden bazı yorumlar tek bir emojidir, bazıları size soru sorar."),
            ("Her paketle kaç yorum gelir?", "{starter_name} ile genellikle ayda {starter_comments}, {rising_name} ile {rising_comments}, {pro_name} ile {pro_comments}. Sayı değil aralık, çünkü söyleyecek bir şeyleri olup olmadığına insanlar karar verir."),
            ("Yorumlar doğal görünür mü?", "Görünür, çünkü doğaldır. Gerçek insanlar farklı zamanlarda, farklı tarzlarda, gerçekten keyif aldıkları gönderilere yorum yapar."),
            ("Takipçi olmadan yorum alabilir miyim?", "Yorumlar ayrıca satılmaz. Bir gönderiden keyif alan kişi takip eden, beğenen ve yazan kişidir; bu yüzden üçü de her pakette birlikte gelir."),
        ],
    },
    {
        "service": "comments",
        "modifier": "custom",
        "slug": "instagram/yorum/ozel",
        "label": "Özel Instagram yorum?",
        "title": "Özel Instagram Yorum mu? Gerçek Yorum Daha Etkili | Growsterr",
        "description": "Kendi yazdığınız özel Instagram yorumları, kimsenin kullanmadığı hesaplardan paylaşılır. Biz insanların kendi cümleleriyle yazdığı yorumları getiririz.",
        "h1": ("Özel Instagram yorumu mu, ", "içten yazılmış yorum mu?"),
        "intro": "Metnini kendinizin belirlediği özel Instagram yorum satın almak isterseniz, kelimeler sizin olur ama onları paylaşan hesaplar gerçek olmaz. Bunu sunmuyoruz. Kampanyamız profilinizi gerçek insanlarla tanıştırır; söyleyecek bir şeyi olanlar da onu kendileri yazar: {pick_name} ile genellikle ayda {pick_comments} yorum.",
        "hero": {"image": "instagram-creator-studio", "alt": "Takipçilerine bir soruyla biten Instagram açıklaması yazan bir içerik üreticisi"},
        "sections": [
            {
                "h2": "Sizin cümlelerinizi neden paylaşmıyoruz?",
                "p": [
                    "Özel yorum hizmeti, cümle listenizi alır ve fotoğrafınızın altına bir hesap havuzundan paylaşır. Ne kadar iyi yazarsanız yazın, hesaplar işi ele verir: arkalarında kimse yoktur, asla geri gelmezler ve yorum bölümü bir gösteriye dönüşür.",
                    "Takipçiler, bir gönderinin altındaki yorumlar gönderiyi paylaşan kişi gibi konuştuğunda bunu fark eder.",
                ],
            },
            {
                "h2": "Neyi şekillendirebilirsiniz?",
                "p": [
                    "Gerçek insanların ne söyleyeceğini seçemezsiniz. Bir şey söylemelerini kolaylaştırabilirsiniz.",
                ],
                "ul": [
                    "Açıklamayı insanların birkaç kelimeyle cevaplayabileceği bir soruyla bitirin.",
                    "İlk yorumlara hızlı cevap verin; bir cevap çoğu zaman bir başkasını davet eder.",
                    "Yapmak istediğiniz sohbeti başlatan bir yorumu sabitleyin.",
                    "Yorum yapanların hangi şehir ya da ülkeden geleceğini seçin.",
                ],
            },
            {
                "h2": "Size bir şey anlatan yorumlar",
                "p": [
                    "Gerçek yorumlar geri bildirimdir. İnsanlar ceketinizi nereden aldığınızı ya da hangi tarifi deneyeceklerini sorduğunda, kitlenizin ne istediğini öğrenirsiniz. Önceden yazılmış yorumlar yalnızca zaten düşündüğünüzü tekrarlayabilir.",
                ],
            },
        ],
        "faqs": [
            ("Yorumları kendim yazabilir miyim?", "Hayır. Sizin yerinize asla yorum paylaşmayız; paylaşacak hesaplarımız da yok. Gerçek insanlar kendi yorumlarını yazar ve getirdiğimiz tek tür budur."),
            ("Yorumlar belirli bir dilde olabilir mi?", "Dolaylı olarak. Kitlenizin geleceği ülkeyi ya da şehri seçin; oradaki insanlar genellikle konuştukları dilde yorum yapar. Kelimeler her zaman onlarındır."),
            ("Hangi gönderilerin yorum alacağını seçebilir miyim?", "{rising_name} ve {pro_name} ile ilginin hangi gönderilere gideceğini seçebilirsiniz; ama yorumu insanlar, onlara dokunan gönderilere yazar. En güçlü gönderileriniz genellikle en çoğunu toplar."),
            ("Olumsuz yorum alır mıyım?", "Gerçek insanlar ne düşünüyorsa onu söyler. Çoğu gördüğünü beğendiği için yorum yapar, ama fikirleri filtrelemeyiz; Instagram'ın yorumları gizleme ya da silme araçları da sizin elinizde kalır."),
            ("Yorumlar gönderilerime yayılır mı?", "Ay boyunca, evet: {pick_name} genellikle {pick_comments} yorum getirir; tek seferde değil, 30 güne yayılarak. İnsanların hakkında daha çok söyleyecek şeyi olan gönderiler daha fazlasını toplar."),
        ],
    },
    {
        "service": "comments",
        "modifier": "fast",
        "slug": "instagram/yorum/hizli",
        "label": "Hızlı Instagram yorum?",
        "title": "Anında Instagram Yorum mu? Gerçek Yorum Zaman Alır | Growsterr",
        "description": "Anında gelen Instagram yorumları yazılımlardan gelir. Bizimkiler profilinizi bulan gerçek insanlardan, azar azar gelir: genellikle ayda {pick_comments}.",
        "h1": ("Anında Instagram yorumu yazılımdan gelir. ", "Bizimkiler insanlardan."),
        "intro": "Instagram yorumunu anında ancak yazılımlardan alabilirsiniz: hiçbir gerçek insan bir ödemeden saniyeler sonra bir gönderiyi okuyup cevap yazmaz. Anında teslim yapmıyoruz. Kampanyanız profilinizi her gün gerçek insanlara gösterir; yorumlar da onlar gönderilerinizi keşfettikçe gelir: {pick_name} ile genellikle ayda {pick_comments}.",
        "hero": {"image": "instagram-hub", "alt": "Bir ay boyunca Instagram gönderilerinin altında birkaç birkaç beliren yorumlar"},
        "sections": [
            {
                "h2": "Gerçek insanlarla hızlı ne demek?",
                "p": [
                    "Instagram'da hız, bir sayının ne kadar çabuk zıpladığı değildir. Gönderilerinizin ne kadar çabuk bir sohbet başlattığıdır. Gerçek yorumcular ay boyunca gelmeye devam eder; yani üçüncü haftada paylaştığınız bir gönderi de yeni insanlarla buluşur.",
                ],
            },
            {
                "h2": "Bir dakikada gelen yorum duvarı neden geri teper?",
                "p": [
                    "Birkaç beğenisi olan bir gönderiye aynı dakikada gelen otuz yorum popüler görünmez. Takipçilerinize ve sizinle çalışmayı düşünen her markaya satın alınmış görünür.",
                    "Sonra durur. Yazılım yorumları tek bir patlamayla gelir ve asla geri dönmez; bir sonraki gönderiniz karşılaştırınca sessiz görünür.",
                ],
            },
            {
                "h2": "Dürüst zaman çizelgesi",
                "ul": [
                    "Sipariş verdikten sonra: kampanyanız başlar ve ilk insanlar birkaç gün içinde profilinize ulaşır.",
                    "Ay boyunca: yorumlar, insanların en çok beğendiği gönderilere birkaç birkaç gelir.",
                    "Her yeni gönderide: o zamandan beri takip eden insanlar onu görmek ve cevap yazmak için oradadır.",
                ],
            },
        ],
        "faqs": [
            ("İlk yorumlar ne kadar sürede görünür?", "Genellikle kampanyanızın ilk günlerinde, gerçek insanlar gönderilerinizi bulmaya başladığında. Sonrasında bir patlama halinde değil, birkaç birkaç gelirler."),
            ("Bir gönderi paylaşıldığı an ona yorum gönderebilir misiniz?", "Hayır. Yorumları bir ana göre zamanlayamayız ve belirli bir gönderiye sayıyla yorum gönderemeyiz. Kampanya profilinizi tanıtır; insanlar da seçtikleri gönderilere, onları gördüklerinde yorum yapar."),
            ("Neden bütün yorumları ilk gün koymuyorsunuz?", "Çünkü o zaman insan olmayan hesaplardan gelmeleri gerekirdi. Gerçek yorumcuların kendi saatleri vardır; yorumlarının doğal görünmesinin nedeni de tam olarak budur."),
            ("Yorumlarla birlikte beğeni de gelir mi?", "Evet. Yorum yapan insanlar genellikle beğenir de: {pick_name} yeni takipçilerle birlikte genellikle ayda {pick_likes} beğeni getirir."),
            ("Bu hız bana göre değilse durdurabilir miyim?", "Evet. İstediğiniz zaman hesabınızdan iptal edin; bir daha ödeme alınmaz ve ödenen ay sonuna kadar sürer."),
        ],
    },
    {
        "service": "comments",
        "modifier": "female",
        "slug": "instagram/yorum/kadin",
        "label": "Kadınlardan Instagram yorum?",
        "title": "Kadınlardan Instagram Yorum mu? Bilmeniz Gerekenler | Growsterr",
        "description": "Cinsiyete göre hedefleme yapmıyoruz; gerçek insanlarla kimse yalnızca kadınlardan yorum vaat edemez. Nedeni ve gerçek yorumların size nasıl ulaştığı burada.",
        "h1": ("Yalnızca kadınlardan Instagram yorumu mu? ", "Bunu dürüstçe kimse vaat edemez."),
        "intro": "Kadınlardan Instagram yorum satın almayı mı umuyorsunuz? Net cevap şu: cinsiyete göre hedefleme yapmıyoruz ve yalnızca kadın hesaplardan yorum vaat eden bir hizmet bu sözü gerçek insanlarla tutamaz. Bu teklifler kadın gibi görünecek şekilde kurulmuş profillere dayanır. Biz profilinizin nerede gösterileceğini seçeriz; kimin yorum yapacağı onu görenlere kalmıştır.",
        "hero": {"image": "instagram-real-people", "alt": "Bir Instagram gönderisini okuyup yorum yapan çeşitli insanlardan oluşan bir grup"},
        "sections": [
            {
                "h2": "Kimin yorum yapacağına dair bir söz neden sahte hesap ister?",
                "p": [
                    "Gerçek bir insan yorum yapıp yapmayacağına kendisi karar verir. Bu yüzden dürüst hiçbir hizmet hem yorum sayısını hem de kimin yazacağını vaat edemez. Bir teklif ikisini birden yapıyorsa, hesapları satıcı ayarlıyordur ve üzerlerindeki fotoğraflar siparişe uysun diye seçilmiştir.",
                    "Cinsiyete göre hedefleme hiç sunmuyoruz. Profilinizin nerede gösterileceğine biz karar veririz; kimin karşılık vereceğini insanların kendisine bırakırız.",
                ],
            },
            {
                "h2": "Kimin katılacağına içeriğiniz karar verir",
                "p": [
                    "Bugün kitlenizin çoğu kadınsa, bunun nedeni paylaştıklarınız ve kime hitap ettikleridir. Bir kampanyanın getirdiği insanlar da aynı şekilde işler: bir gönderi onlara hitap ettiğinde yorum yaparlar.",
                ],
                "ul": [
                    "İdeal kitlenizin yaşadığı şehri ya da ülkeyi seçin.",
                    "O kitlenin önemsediği konularda düzenli paylaşım yapın.",
                    "Yorumlara cevap verin ki katılan insanlar dinlendiklerini hissetsin.",
                ],
            },
        ],
        "faqs": [
            ("Kadın ya da erkek yorumcu seçebilir miyim?", "Hayır. Cinsiyete göre hedefleme sunmuyoruz. Siz bir konum seçersiniz; yorum yapanlar gönderinizden keyif alan insanlardır."),
            ("Bazı teklifler neden kadınlardan yorum vaat ediyor?", "Çünkü yorumcuları kendi kontrol ettikleri hesaplardır. Bir isim ve profil fotoğrafı ayarlamak kolaydır; gerçek bir insanın yazmayı seçmesi değildir."),
            ("Gönderilerime hiç kadın yorum yapacak mı?", "Elbette, gönderileriniz onlara hitap ediyorsa. Gerçek kitleler karışıktır; sohbete kimin katılacağı ne paylaştığınıza ve nerede gösterildiğine bağlıdır."),
            ("O zaman kim yorum yapacak?", "Gönderilerinizden keyif alan herkes. {pick_name} yazmayı seçen her türden insandan genellikle ayda {pick_comments} yorum getirir; aynı insanlardan yeni takipçi ve beğenilerle birlikte."),
            ("Şifremi istiyor musunuz?", "Hayır. Instagram kullanıcı adınız yeterli; kampanya sürerken profilinizin herkese açık kalması gerekir."),
        ],
    },
    {
        "service": "comments",
        "modifier": "free",
        "slug": "instagram/yorum/ucretsiz",
        "label": "Ücretsiz Instagram yorum?",
        "plan": "starter",
        "tool": "engagement-calculator",
        "title": "Ücretsiz Instagram Yorum Olur mu? İşe Yarayan Bu | Growsterr",
        "description": "Instagram yorumunu ücretsiz dağıtmıyoruz. Bedava yorum uygulamalarının gerçek bedeli, ücretsiz etkileşim hesaplayıcı ve gerçek yorum kazandıran alışkanlıklar.",
        "h1": ("Ücretsiz Instagram yorumu mu? ", "Gerçekte neyin yorum kazandırdığını anlatalım."),
        "intro": "Instagram yorumunu ücretsiz mi almak istiyorsunuz? Biz dağıtmıyoruz; bedava dağıtan uygulamaların bedeli de şifreniz, yorum gruplarında geçen saatler ya da insan olmayan hesaplardır. Burada ücretsiz olanlar: kitlenizin ne kadarının tepki verdiğini gösteren etkileşim hesaplayıcı ve gerçek yorum kazandıran alışkanlıklar. Daha çok insana ulaşmak istediğinizde paketlerimiz gerçek insanlardan yorum getirir.",
        "hero": {"image": "instagram-creator-studio", "alt": "Telefonunda son gönderilerinin yorum sayılarına bakan bir içerik üreticisi"},
        "sections": [
            {
                "h2": "Ücretsiz yorumlar nereden gelir?",
                "ul": [
                    "Giriş bilgilerinizi isteyen, sonra karşılığında hesabınızı başkalarının gönderilerine yorum yapmak için kullanan yorum uygulamaları.",
                    "Birkaç tane geri almak için günde onlarca yorum sözü verdiğiniz etkileşim grupları.",
                    "Daha büyük bir paket için ödeme yapasınız diye bot ağlarından gönderilen bedava denemeler.",
                ],
                "p": [
                    "Bunların hiçbiri gönderilerinizi önemseyen birini getirmez; giriş bilgilerinizi vermek de büyütmeye çalıştığınız hesabı riske atar.",
                ],
            },
            {
                "h2": "Gerçekten ücretsiz olan: etkileşim oranınız",
                "p": [
                    "Bu sayfanın üstündeki hesaplayıcıyı kullanın: takipçi sayınızı ve son birkaç gönderinizdeki ortalama beğeni ve yorumu girin. Tarayıcınızda çalışır ve hiçbir yere bir şey göndermez.",
                    "Yorumlar genellikle tepkilerinizin küçük bir kısmı olur. Bu normal: bir yorum bir dokunuştan daha fazla emek ister; bu da onu bir gönderinin karşılık bulduğunun en net işareti yapar.",
                ],
            },
            {
                "h2": "Daha çok yorum kazandıran ücretsiz alışkanlıklar",
                "ul": [
                    "Açıklamada belirsiz bir soru yerine net bir soru sorun.",
                    "Paylaştıktan kısa süre sonra yorumlara cevap verin; cevaplar insanları geri getirir.",
                    "Takipçileriniz çevrimiçiyken paylaşın; hesap istatistikleriniz ne zaman olduğunu gösterir.",
                    "Gönderiyi Hikâyenizde paylaşın ve insanları sohbete yönlendirin.",
                ],
            },
        ],
        "faqs": [
            ("Ücretsiz Instagram yorumu veriyor musunuz?", "Hayır. Getirdiğimiz her yorum, kampanyamızın ulaştığı gerçek bir insandan gelir ve bu işin bir maliyeti var. Bu sayfada ücretsiz olan, hesaplayıcı ve tavsiyeler."),
            ("Bir uygulamadan bedava Instagram yorumu almak güvenli mi?", "Bu uygulamaların çoğu Instagram giriş bilgilerinizi ister; kaçınmanız gereken kısım da bu. Şifreniz kimdeyse sizin adınıza paylaşım yapabilir, takip edebilir, yorum yazabilir. Biz asla istemeyiz."),
            ("Yalnızca yorumu daha ucuza alabilir miyim?", "Yorumlar asla ayrıca satılmaz. Her paketin içinde aynı insanlardan gelen takipçi ve beğenilerle birlikte gelir: {starter_name} ile genellikle ayda {starter_comments} yorum."),
            ("İyi bir etkileşim oranı nedir?", "Nişinize ve büyüklüğünüze bağlı, bu yüzden kendinizle karşılaştırın. Oranınızı bugün, sonra bir ay sonra yeniden hesaplayın: yükselen bir oran, kitlenizin daha fazlasının önemsediği anlamına gelir."),
            ("Bana göre değilse iptal edebilir miyim?", "Evet, istediğiniz zaman hesabınızdan. Başka ödeme alınmaz ve ödediğiniz ay sizde kalır."),
        ],
    },
    {
        "service": "comments",
        "modifier": "verified",
        "slug": "instagram/yorum/onayli",
        "label": "Onaylı hesaplardan Instagram yorum?",
        "title": "Onaylı Hesaplardan Instagram Yorum mu? Dürüst Cevap | Growsterr",
        "description": "Kimse onaylı hesaplara ya da ünlülere sipariş üzerine yorum yaptıramaz. Biz bunun yerine gönderinizi gören gerçek insanlardan Instagram yorumu getiririz.",
        "h1": ("Onaylı hesaplardan ya da ünlülerden yorum mu? ", "Kimsenin satabileceği bir şey değil."),
        "intro": "Onaylı hesaplardan ya da ünlülerden Instagram yorum satın almak istemek anlaşılır bir şey: gönderinizin altındaki mavi tik bir onay gibi görünür. Bunları satmıyoruz; hiçbir büyüme hizmeti de onaylı bir hesaba ya da tanınmış birine sipariş üzerine yorum yaptıramaz. Bunu vaat eden teklifler benzer görünen profiller ya da yazılımlar kullanır. Bizim yorumlarımız gönderinizi gören gerçek insanlardan gelir.",
        "hero": {"image": "instagram-real-people", "alt": "Bir içerik üreticisinin fotoğrafına yorum bırakan sıradan Instagram kullanıcıları"},
        "sections": [
            {
                "h2": "Onaylı bir yorum nasıl işlemek zorunda olurdu?",
                "p": [
                    "Onaylı hesaplar, neye yorum yapacaklarına kendileri karar veren insanlara ve markalara aittir. Bir satıcı onlara sipariş veremez. Yani bir fiyat listesinde onaylı profillerden ya da ünlülerden yorum varsa, resmî görünsün diye kılık değiştirmiş hesaplar sunuluyordur.",
                    "Taklit profiller şikâyet edilir ve silinir; birinden gelen yorum gönderinizi daha güvenilir değil, daha az güvenilir gösterebilir.",
                ],
            },
            {
                "h2": "Bir gönderiye gerçekten yardım eden yorumlar",
                "p": [
                    "Bir yorum, geri gelebilecek birinden geldiğinde yardım eder: gönderiden keyif alan, bunu kendi cümleleriyle söyleyen ve müdavim olabilecek biri. Paketlerimizin getirdiği bu: {pick_name} ile tipik bir ayda {pick_comments} yorum, yeni takipçi ve beğenilerle birlikte.",
                ],
            },
            {
                "h2": "Daha büyük hesapların sizi fark etmesini istiyorsanız",
                "p": [
                    "Büyük hesapların ilgisi açıkta kazanılır. Gerçekten kullandığınız markaları etiketleyin, nişinizdeki içerik üreticilerini ortak gönderilere davet edin ve onların işlerine düşünülmüş yorumlar bırakın. Bir sipariş formundan yavaştır, ama gerçektir.",
                ],
            },
        ],
        "faqs": [
            ("Ünlülere gönderilerime yorum yaptırabilir misiniz?", "Hayır. Biz yaptıramayız; bunu paket olarak satan kimse de yaptıramaz. Tanınmış insanlar nereye yorum yapacaklarını kendileri seçer."),
            ("Yorumcularınız onaylı hesaplar mı?", "İnsanları rozete göre ayırmıyoruz. Yorumcularımız gönderinizi bulan gerçek Instagram kullanıcılarıdır; aralarında mavi tiki olan olup olmayacağını ne seçeriz ne de vaat ederiz."),
            ("Gerçek yorumlar onaylı hesap almama yardım eder mi?", "Doğrulama Instagram'ın kendi süreciyle yürür ve bizim bunda hiçbir payımız yok. Instagram ne karar verirse versin, gerçek etkileşim hesabınızı daha canlı ve daha güvenilir bir yer yapar."),
            ("Nasıl yorumlar alacağım?", "Sıradan Instagram kullanıcılarından, kendi cümleleriyle yorumlar. Tipik aylar: {starter_name} ile {starter_comments}, {pro_name} ile {pro_comments}, {rising_name} ikisinin arasında."),
            ("Hesabım sizinle güvende mi?", "Evet. Asla giriş yapmayız ve şifrenizi asla istemeyiz. Yalnızca kullanıcı adınıza ihtiyacımız var; yorumlar kendi başına hareket eden insanlardan gelir."),
        ],
    },
    # --- Followers ------------------------------------------------------------------------
    {
        "service": "followers",
        "modifier": "cheap",
        "slug": "instagram/takipci/ucuz",
        "label": "Ucuz Instagram takipçi?",
        "plan": "starter",
        "title": "Ucuz Instagram Takipçi Satın Al: Gerçek Maliyet | Growsterr",
        "description": "Bin tanesi birkaç liraya satılan ucuz Instagram takipçileri bottur. {starter_name} ayda {starter_price}; genellikle {starter_audience} gerçek takipçi getirir.",
        "h1": ("Ucuz Instagram takipçi mi? ", "Gerçek insan başına maliyeti hesaplayın."),
        "intro": "Ucuz Instagram takipçi satın almadan önce her takipçinin neye mal olduğunu ve ne yaptığını karşılaştırın. Bin tanesi birkaç lira olan takipçiler kaybolan ve erişiminizi aşağı çeken botlardır. {starter_name} ayda {starter_price}; genellikle {starter_audience} yeni takipçi getirir: takip etmeyi seçen gerçek insanlar, beğeni ve yorumlar dahil. Bu, gerçek insan başına birkaç sent demek.",
        "hero": {"image": "instagram-followers", "alt": "Tek bir aylık paketle gerçek insanlarla büyüyen bir Instagram takipçi sayısı"},
        "sections": [
            {
                "h2": "En ucuz fiyat gerçekte neyi satın alır?",
                "p": [
                    "En ucuz fiyatta bir takipçi, toplu olarak üretilmiş, gönderisi olmayan, varsa da ödünç bir fotoğrafı olan bir hesaptır. Neredeyse hiçbir şeye mal olmaz, çünkü arkasında kimse yoktur.",
                    "Bu hesaplar asla beğenmez ya da yorum yapmaz. Instagram sahte profilleri temizlediğinde giderler; kaldıkları sürece de her gönderiniz önemseyen insanların daha küçük bir kısmına ulaşır.",
                ],
            },
            {
                "h2": "Gerçek takipçilerin hesabı",
                "p": [
                    "{starter_price} tutarını, {starter_name} ile bir ayda genellikle gelen {starter_audience} takipçiye bölün; her gerçek insan birkaç sente gelir. Sonra onlarla birlikte geleni ekleyin: aynı insanlardan genellikle {starter_likes} beğeni ve {starter_comments} yorum, ek ücret olmadan.",
                ],
            },
            {
                "h2": "Düşük maliyet, gizli hiçbir şey yok",
                "ul": [
                    "Tek bir aylık fiyat takipçiyi, beğeniyi ve yorumu kapsar.",
                    "Stripe üzerinden kartla ödeme; cihazınız destekliyorsa Apple Pay ya da Google Pay ile.",
                    "İstediğiniz zaman iptal edin, ödediğiniz ayın kalanını kullanın.",
                    "En düşük fiyatımız olan {starter_name} ile başlayın, yalnızca daha fazlasını isterseniz yükseltin.",
                ],
            },
        ],
        "faqs": [
            ("Gerçek Instagram takipçilerinin fiyatı nedir?", "En düşük fiyatımız {starter_name} için ayda {starter_price}; genellikle {starter_audience} yeni takipçi getirir. {rising_name} {rising_price}, {pro_name} {pro_price}; daha büyük aralıklarla."),
            ("Neden birkaç liraya bin takipçi almayayım?", "Çünkü o fiyatta kimse gerçek değildir. Bin takipçi için birkaç lira, ancak yazılımla üretilmiş hesapları karşılar; bunlar da bir temizlikte ilk gidenlerdir."),
            ("Hem ucuz hem hızlı takipçi alabilir miyim?", "Ucuz ve anında bir arada her zaman bot demektir. Gerçek takipçiler, kampanyanız çalışmaya başladıktan sonra her gün birkaç tane gelir."),
            ("{starter_name} paketinden daha ucuz bir şey var mı?", "Hayır. Ayda {starter_price} olan {starter_name} en küçük paketimiz. Küçük tek seferlik paketler satmıyoruz: gerçek bir kampanyanın insanlara ulaşması için bir ay gerekir, aşırı ucuz paketler de botların yuvasıdır."),
            ("Beğeni ve yorum için ek ödeme yapar mıyım?", "Hayır. Sizi takip eden insanlardan, paketin içinde gelirler: {starter_name} ile genellikle ayda {starter_likes} beğeni ve {starter_comments} yorum."),
        ],
    },
    {
        "service": "followers",
        "modifier": "fast",
        "slug": "instagram/takipci/hizli",
        "label": "Hızlı Instagram takipçi?",
        "title": "Hızlı Instagram Takipçi Satın Al, Gerçek İnsan | Growsterr",
        "description": "Gerçek insanlardan hızlı Instagram takipçi: kampanyanız ilk günlerde başlar, yeni takipçiler her gün gelir. Asla anında değil, çünkü anında demek bot demek.",
        "h1": ("Hızlı Instagram takipçi, ", "gerçek insanların hızında."),
        "intro": "Instagram takipçiyi hızlı mı satın almak istiyorsunuz? Kampanya çabuk başlayabilir, ama gerçek takipçiler anında gelemez: kimse siz ödeme yaptıktan saniyeler sonra bir hesabı takip etmeye karar vermez. Bizde gerçek insanlar ilk günlerde gelmeye başlar ve her gün gelmeye devam eder: {pick_name} ile genellikle ayda {pick_audience}. Çoğu içerik üreticisinin asıl istediği hız, her hafta görebildiği büyümedir.",
        "hero": {"image": "instagram-followers-1000", "alt": "Instagram'da her gün biraz daha yükselen bir takipçi çizgisi"},
        "sections": [
            {
                "h2": "Çabuk başlangıç, istikrarlı tırmanış",
                "p": [
                    "Sipariş verdikten sonra kampanyanızı kurarız ve profiliniz gerçek insanlara gösterilmeye başlar. İlk ziyaretler ve takipler genellikle birkaç gün içinde panelinizde görünür; çizgi de oradan yükselmeye devam eder.",
                ],
            },
            {
                "h2": "En hızlı teklifler neden kaçınılması gerekenlerdir?",
                "p": [
                    "Bir saatte binlerce takipçi bir özellik değil, bir uyarı işaretidir. O kadar hızlı hareket etmek için satıcının söyleneni yapan hesaplara ihtiyacı vardır; Instagram da bunları dalgalar halinde siler.",
                    "Böyle bir sıçrama ziyaretçilere de tuhaf görünür: geçen haftanın birkaç beğenisini taşıyan gönderilerin üstünde bir gecede ikiye katlanmış bir takipçi sayısı.",
                ],
            },
            {
                "h2": "Gerçek büyümeyi hızlandırmanın yolları",
                "ul": [
                    "Daha büyük bir paket seçin: {pro_name} genellikle ayda {pro_audience} takipçi getirir.",
                    "Kampanya sürerken paylaşım yapmaya devam edin ki ziyaretçiler yeni bir şey bulsun.",
                    "Biyografinizi net, profilinizi herkese açık tutun; bir ziyaretçi saniyeler içinde karar verir.",
                    "İçeriğinizin uyduğu bir konum seçin ki daha çok ziyaretçi takipçiye dönüşsün.",
                ],
            },
        ],
        "faqs": [
            ("Yeni takipçileri ne kadar hızlı görürüm?", "Kampanyanızın ilk günlerinde, gerçek insanlar profilinizi ziyaret etmeye başladıkça. Paneliniz her günün ziyaretlerini ve takiplerini ölçtüğümüz gibi gösterir."),
            ("Bir saat içinde takipçi teslim edebilir misiniz?", "Hayır; gerçek insanlarla kimse edemez. O kadar hızlı gelen her şey insan olmayan hesaplardan gelir ve genellikle yeniden kaybolur."),
            ("Hangi paket en hızlı büyütür?", "{pro_name}: genellikle ayda {pro_audience} yeni takipçi; {rising_name} ile {rising_audience}, {starter_name} ile {starter_audience}."),
            ("Hızlı büyüme şüpheli görünür mü?", "Bizim hızımızda hayır. İnsanlar her gün birkaç birkaç takip eder; büyüyen her hesap takipçiyi böyle kazanır."),
            ("Daha hızlı büyümek için sonra yükseltebilir miyim?", "Evet. Profilinizi daha çok insanın görmesini istediğinizde daha büyük bir pakete geçebilirsiniz."),
        ],
    },
    {
        "service": "followers",
        "modifier": "free",
        "slug": "instagram/takipci/ucretsiz",
        "label": "Ücretsiz Instagram takipçi?",
        "plan": "starter",
        "tool": "growth-calculator",
        "title": "Ücretsiz Instagram Takipçi: Gerçekte Ne Alırsınız? | Growsterr",
        "description": "30 ya da 50'şer gelen, şifresiz verilen ücretsiz Instagram takipçileri bot ya da takas hesaplarıdır. Biz vermiyoruz; ücretsiz büyüme hesaplayıcımızı deneyin.",
        "h1": ("30 ya da 50 ücretsiz Instagram takipçi mi? ", "Gerçekte ne olduklarını anlatalım."),
        "intro": "30 ücretsiz Instagram takipçi ya da şifresiz 50 bedava takipçi dağıtan siteler, bot ağlarından numuneler ya da takibe takip takasları veriyor. Biz ücretsiz takipçi vermiyoruz. Bu sayfada ücretsiz olan büyüme hesaplayıcısı: bugünkü takipçi sayınızı ve hedefinizi girin, her paketle gerçek büyümenin genellikle ne kadar sürdüğünü görün.",
        "hero": {"image": "instagram-followers", "alt": "Kaç gerçek Instagram takipçisi hedefleyeceğini planlayan bir içerik üreticisi"},
        "sections": [
            {
                "h2": "Ücretsiz bir takipçi size neye mal olur?",
                "ul": [
                    "Daha fazlası için ödeme yapasınız diye bir bot ağından gönderilen 30 ya da 50 hesaplık bir numune.",
                    "Takibe takip uygulamaları: yabancıları takip edersiniz, onlar geri takip eder, siz bıraktığınızda onlar da gider.",
                    "Şifrenizi isteyen ve hesabınızı başkalarını takip etmek için kullanan uygulamalar.",
                ],
                "p": [
                    "100 bin bedava takipçiye gelince, böyle bir şey hiçbir yerde yok. O büyüklükte botların bile bir maliyeti var; yani sunulan ne olursa olsun takipçi değil.",
                ],
            },
            {
                "h2": "Şifresiz: doğru içgüdü",
                "p": [
                    "Şifresiz takipçi istemek, şifrenizi kimseye vermemeniz gerektiğini zaten bildiğiniz anlamına gelir. Böyle kalsın. Biz de asla istemeyiz: profilinizi gerçek insanlara göstermek için kullanıcı adınız yeterli.",
                ],
            },
            {
                "h2": "Gerçek büyümeyi hesaplayıcıyla planlayın",
                "p": [
                    "Yukarıdaki büyüme hesaplayıcısı ücretsizdir ve tarayıcınızda çalışır. Bugünkü takipçi sayınızı ve ulaşmak istediğiniz sayıyı girin; her paketin oraya genellikle kaç ayda vardığını gösterir. Sonra gerçek rakamlar önünüzdeyken karar verebilirsiniz.",
                ],
            },
        ],
        "faqs": [
            ("Ücretsiz Instagram takipçi veriyor musunuz?", "Hayır. Getirdiğimiz her takipçi, ücretli bir kampanyanın ulaştığı gerçek bir insandır; dağıtılacak bedava bir şey yok. Bu sayfadaki hesaplayıcı ise ne kadar kullanırsanız kullanın ücretsiz."),
            ("Şifresiz takipçi almak güvenli mi?", "Şifrenizi kendinize saklamak her zaman daha güvenlidir. Sunulan takipçiler ise ayrı bir konu: şifre istemeyen ücretsiz hizmetler genellikle bot hesap gönderir ya da sizden yabancıları takip etmenizi ister."),
            ("100 bin Instagram takipçisini bedavaya alabilir miyim?", "Kimse size bu kadar gerçek takipçiyi karşılıksız veremez. 100 bine gerçek büyüme aylar sürer; hesaplayıcı her paketle kabaca kaç ay sürdüğünü gösterir."),
            ("Başlamanın en düşük maliyetli yolu ne?", "Ayda {starter_price} olan {starter_name}; genellikle {starter_audience} gerçek takipçi getirir. İstediğiniz zaman iptal edin; ödediğiniz ay sonuna kadar sürer."),
            ("Ücretsiz takipçiler hesabıma zarar verebilir mi?", "Verebilir. Hiç etkileşime girmeyen hesaplar, gönderilerinize tepki veren takipçilerin oranını düşürür ve Instagram sahte profilleri sildiğinde genellikle kaybolur."),
        ],
    },
    {
        "service": "followers",
        "modifier": "free-trial",
        "slug": "instagram/takipci/ucretsiz-deneme",
        "label": "Instagram takipçi ücretsiz deneme?",
        "plan": "starter",
        "title": "Instagram Takipçi Ücretsiz Deneme mi? Sunduğumuz Bu | Growsterr",
        "description": "Instagram takipçide ücretsiz deneme sunmuyoruz. İlk ayınız asıl testtir: gerçek insanlar, ölçüm yapan bir panel ve istediğiniz zaman iptal.",
        "h1": ("Instagram takipçide ücretsiz deneme yok. ", "İlk ayınız asıl test."),
        "intro": "Instagram takipçiyi önce ücretsiz denemeyle mi satın almak istiyorsunuz? Deneme sunmuyoruz; bir saatte 50 takipçilik bir deneme de yalnızca satıcının botları olduğunu kanıtlar. Asıl test ilk ayınızdır: {starter_name} ayda {starter_price}, gerçek insanlar ilk günlerde gelmeye başlar, paneliniz ölçtüklerimizi gösterir ve istediğiniz zaman iptal edebilirsiniz.",
        "hero": {"image": "instagram-hub", "alt": "Gerçek takipçilerle büyümesinin ilk ayındaki bir Instagram profili"},
        "sections": [
            {
                "h2": "Neden deneme sunmuyoruz?",
                "p": [
                    "Bir kampanyanın her günü, profilinizi iş ortağı ağımızdaki tanıtım kampanyalarıyla gerçek insanlara göstermek demektir; bunun maliyeti birinci günde de otuzuncu günde de aynıdır. Gerçek insanlarla kısa bir versiyonu ucuza yürütmenin yolu yok.",
                    "Küçük bir deneme zaten size pek bir şey anlatmazdı. Gerçek büyüme, ilk öğleden sonraki bir sayı değil, bir ay boyunca süren bir hızdır.",
                ],
            },
            {
                "h2": "İlk ayınızda bizi nasıl değerlendirirsiniz?",
                "ul": [
                    "Panele bakın: gün gün profil ziyaretleri ve yeni takipçiler.",
                    "Kimin takip ettiğine bakın: kendi gönderileri ve hayatları olan gerçek profiller.",
                    "Aynı insanlardan gelen beğeni ve yorumlarınızı kontrol edin.",
                    "İkna olmadınız mı? Bir sonraki yenilemeden önce hesabınızdan iptal edin.",
                ],
            },
        ],
        "faqs": [
            ("Ücretsiz deneme var mı?", "Hayır. Deneme yapmıyor ya da takipçi dağıtmıyoruz. En yakın şey bir aylık {starter_name}: yenilenmeden önce iptal ederseniz bir daha ödeme yapmazsınız."),
            ("İlk aydan sonra memnun kalmazsam ne olur?", "Hesabınızdan iptal edin, yenileme olmaz. O ay sizi takip eden gerçek insanlar iptal ettiğinizde kaybolmaz."),
            ("En az ne kadar taahhüt gerekiyor?", "Bir ay. Bunun ötesinde sözleşme yok: her ay yalnızca paketi çalışır bıraktığınızda yenilenir."),
            ("Sonuçları ne kadar sürede değerlendirebilirim?", "İlk haftalar içinde. Panel her gün ziyaretleri ve yeni takipçileri gösterir; ay bitmeden çok önce hızın oluştuğunu görebilirsiniz."),
            ("Diğer siteler neden deneme sunuyor?", "Takipçiler bot olduğunda birkaç düzine takipçilik bir denemeyi dağıtmak ucuzdur. Gerçek insanlarla her takipçi ücretli bir kampanyadan gelir; bu yüzden ucuz değildir."),
        ],
    },
    {
        "service": "followers",
        "modifier": "smm-panel",
        "slug": "instagram/takipci/smm-panel",
        "label": "SMM panelinden Instagram takipçi?",
        "title": "SMM Panelden Instagram Takipçi mi? Farkımız Bu | Growsterr",
        "description": "SMM panelleri, Discord ve Telegram satıcıları bot takipçiyi toptan satar. Growsterr bir ajanstır: gerçek insanlar, bir ekip ve ölçüm gösteren bir hesap paneli.",
        "h1": ("SMM panelleri sayı satar. ", "Biz insan getiren bir ajansız."),
        "intro": "Ucuz bir SMM panelinden, bir Discord sunucusundan ya da bir Telegram kanalından Instagram takipçi almak üzereyseniz, satılan şeyi bilin: SMM panelleri bot trafiğini toptan, binlik fiyatla ve hesap verecek kimse olmadan yeniden satar. Growsterr bir büyüme ajansıdır. Kampanyanızı bir ekip yürütür, takip etmeye gerçek insanlar karar verir ve ölçülen sonuçları hesap panelinizde görürsünüz.",
        "hero": {"image": "instagram-creator-studio", "alt": "Gerçek bir ekibin yürüttüğü Instagram büyüme kampanyasını inceleyen bir içerik üreticisi"},
        "sections": [
            {
                "h2": "Bir SMM paneli nasıl çalışır?",
                "p": [
                    "Panel bir fiyat listesidir. Instagram takipçisi, beğenisi ve izlenmesi yan yana durur; biner biner satılır ve çoğu zaman bir panelden diğerine yeniden satılır. Bir bağlantı yapıştırır, bakiyeden ödersiniz ve bir sayacın oynamasını izlersiniz.",
                    "Bir panelde kimse profilinize ya da kitlenize bakmaz. Ucuz kalmasının yolu budur; gelen şeyin bot trafiği olmasının nedeni de budur.",
                ],
            },
            {
                "h2": "Discord, Telegram ve pazar yeri satıcıları",
                "p": [
                    "Discord sunucularında, Telegram kanallarında ya da pazar yeri ilanlarında satılan takipçi ve beğeniler genellikle aynı toptan panellerden gelir, ortada bir bayiyle. Peşin ödersiniz, çoğu zaman anonim bir kullanıcı adına; hesap yok, kayıt yok, sayılar düştüğünde soracak kimse yok.",
                ],
            },
            {
                "h2": "Bir ajans neyi farklı yapar?",
                "ul": [
                    "Kampanyanızı bir ekip kurar ve takip eder.",
                    "Gerçek insanlar profilinizi görür ve takip edip etmeyeceklerini seçer.",
                    "Beğeni ve yorumlar aynı insanlardan, paketin içinde gelir.",
                    "Hesap paneliniz ölçülen profil ziyaretlerini ve getirdikleri takipçileri raporlar.",
                    "Aylık aboneliğinizi kendi hesabınızdan yönetirsiniz.",
                ],
            },
        ],
        "faqs": [
            ("SMM paneli takipçileri gerçek mi?", "Panel takipçileri toptan satılan bot trafiğidir. Bazı hesapların fotoğrafı ve adı vardır, ama hiçbiri sizi takip etmeyi seçmemiştir ve etkileşime girmezler."),
            ("Bir panelde Instagram beğenisi satıyor musunuz?", "Hayır. Panel işletmiyoruz ve burada beğeni asla tek başına satılmaz. Beğeniler her paketin içinde, sizi takip eden gerçek insanlardan gelir: {pick_name} genellikle ayda {pick_likes} getirir."),
            ("Paketlerinizi kendi panelimde satabilir miyim?", "Panel ya da bayi erişimi sunmuyoruz. Her paket, tek bir hesap için tek bir kampanyadır. Müşterileriniz için birkaç hesap yönetiyorsanız bize yazın, konuşalım."),
            ("Discord ve Telegram satıcıları neden bu kadar ucuz?", "Toptan bot trafiğini üstüne bir kâr koyarak aktarırlar. Arkasında bir kampanya, gerçek insanlara ulaşan biri yoktur."),
            ("Bunun yerine sizden nasıl sipariş veririm?", "Bir paket seçin, Instagram kullanıcı adınızı ve kitlenizin nereden gelmesi gerektiğini verin, kartla ödeyin. Şifreniz hiçbir aşamada işin içine girmez."),
        ],
    },
    {
        "service": "followers",
        "modifier": "verified",
        "slug": "instagram/takipci/onayli",
        "label": "Onaylı Instagram takipçi?",
        "title": "Mavi Tikli Instagram Takipçi mi? Mümkün Olan Bu | Growsterr",
        "description": "Kimse mavi tikli Instagram takipçisi ya da onaylı hesabın kendisini satamaz. Biz sizi takip etmeyi seçen gerçek insanları, beğeni ve yorumlarıyla getiririz.",
        "h1": ("Onaylı Instagram takipçi mi? ", "Bunu dürüstçe kimse satamaz."),
        "intro": "Mavi tikli Instagram takipçi ya da sizi onaylı hesap yapacak takipçiler satın almayı umduysanız, iki sorunun cevabı da hayır. Onaylı hesaplar kimi isterlerse onu takip eder ve hiçbir hizmet onlara emir veremez. Doğrulamayı Instagram'ın kendisi yapar; hiçbir dış hizmet onu satamaz. Bizim getirdiğimiz, takip etmeyi seçen gerçek insanlar: {pick_name} ile genellikle ayda {pick_audience}.",
        "hero": {"image": "instagram-followers-1000", "alt": "Bir içerik üreticisinin profilini takip eden sıradan Instagram kullanıcıları"},
        "sections": [
            {
                "h2": "Mavi tikli takipçiler",
                "p": [
                    "Onaylı hesap, kimliğini Instagram'a doğrulatmış bir kamu figürüne, içerik üreticisine ya da markaya aittir. Bu insanlar da herkes gibi ilginç buldukları hesapları takip eder. Bir satıcı onlara sizi takip ettiremez; yani bir fiyat listesindeki “onaylı takipçiler”, önemli görünsün diye yapılmış profiller demektir.",
                ],
            },
            {
                "h2": "Onaylı hesap olmak için takipçi",
                "p": [
                    "Daha büyük bir sayı tek başına mavi tik kazandırmaz; sahte takipçilerle gelen ani bir sıçrama da yardım etmekten çok soru işareti doğurur. Doğrulama her zaman Instagram'ın kendi sürecinden geçer, asla bir büyüme hizmetinden değil.",
                    "Bir hesabı güvenilir gösteren şey bir sıçramanın tam tersidir: gerçek, istikrarlı büyüyen ve gönderilerinizin altında aktif olan bir kitle.",
                ],
            },
            {
                "h2": "Bizim yapabileceklerimiz",
                "ul": [
                    "Profilinizi her gün, seçtiğiniz yerde yeni insanlara göstermek.",
                    "Sizi seçmiş takipçileri, beğeni ve yorumlarıyla getirmek.",
                    "Panelinizde tam olarak neyi ölçtüğümüzü göstermek.",
                ],
            },
        ],
        "faqs": [
            ("Onaylı hesapların beni takip etmesini sağlayabilir misiniz?", "Hayır. Onaylı kullanıcılar kimi takip edeceklerine kendileri karar verir ve hiçbir paket bunu değiştirmez. Getirdiğimiz gerçek insanlar arasında mavi tik ne seçilir ne de vaat edilir."),
            ("Takipçi satın almak bana mavi tik getirir mi?", "Hayır. Takipçi sayısı tek başına doğrulama kazandırmaz ve biz doğrulamayı hiçbir biçimde sunmuyoruz."),
            ("Takipçileriniz gerçek hesaplar mı?", "Evet. Her biri kendi hesabı olan, profilinize denk gelip takip etmeye karar vermiş bir insandır."),
            ("Ünlüler paketleriniz aracılığıyla geri takip eder mi?", "Hayır. Kampanyalarımız sıradan Instagram kullanıcılarına ulaşır. Ünlülerden takip vaat eden herkes taklit hesaplar kullanıyordur."),
            ("Bir ay kaç takipçi getirir?", "Tipik aylık aralıklarla {starter_name} ile {starter_audience}, {pro_name} ile {pro_audience}. Her biri takip etmeyi seçmiş bir insandır."),
        ],
    },
    # --- Likes ----------------------------------------------------------------------------
    {
        "service": "likes",
        "modifier": "cheap",
        "slug": "instagram/begeni/ucuz",
        "label": "Ucuz Instagram beğeni?",
        "plan": "starter",
        "title": "Ucuz Instagram Beğeni mi? Neyi Aldığınıza Bakın | Growsterr",
        "description": "Ucuz Instagram beğenileri tek bir gönderiye düşer ve biter. Bizimkiler aylık paketin içinde gerçek takipçilerden gelir: genellikle ayda {starter_likes} beğeni.",
        "h1": ("Ucuz Instagram beğenisi ", "göründüğünden pahalıya gelir."),
        "intro": "Ucuz Instagram beğeni satın almadan önce birkaç liralık bir paketin ne olduğuna bakın: bir sonraki gönderinizi asla görmeyecek hesaplardan gelen dokunuşlar. Beğeniyi tek başına satmıyoruz. Her paketin içinde, sizi takip eden gerçek insanlardan gelir: {starter_name} ile ayda {starter_price} karşılığında genellikle {starter_likes} beğeni; yeni takipçi ve yorumlarla birlikte.",
        "hero": {"image": "instagram-hub", "alt": "Bir içerik üreticisinin Instagram ızgarasına yayılmış, gerçek takipçilerden gelen beğeniler"},
        "sections": [
            {
                "h2": "Tek bir gönderi ile her gönderi",
                "p": [
                    "Ucuz bir beğeni paketi tek bir gönderiye düşer ve durur. Bir sonraki gönderiniz sıfırdan başlar; yani yalnızca görüntüyü korumak için satın almaya devam etmeniz gerekir.",
                    "Sizi takip eden insanlardan gelen beğeniler tersine işler. Yeni gönderilerinizi görür ve keyif aldıklarını beğenirler; böylece bu ay paylaştığınız her şey payını alır.",
                ],
            },
            {
                "h2": "Küçük bir bütçe en çok nerede işe yarar?",
                "p": [
                    "Fiyat sizin için en önemlisiyse, parayı çalışmaya devam ettiği yere koyun: beğenmeye devam eden gerçek takipçiler. {starter_name} en düşük fiyatımız ve tek bir aylık ödeme takipçiyi, beğeniyi ve yorumu kapsar.",
                ],
            },
            {
                "h2": "Satın alınmış gibi görünmeyen beğeniler",
                "p": [
                    "Üç yorumu olan ve yeni takipçi getirmemiş bir gönderideki yüzlerce beğeni, dikkat eden herkese satın alınmış görünür; markalar da dahil. Beğeni, takip ve yorum aynı insanlardan geldiğinde rakamlar birlikte anlam taşır.",
                ],
            },
        ],
        "faqs": [
            ("Sizde Instagram beğenisinin fiyatı ne?", "Beğenilerin ayrı bir fiyatı yok. {starter_name} ayda {starter_price} ve aynı insanlardan {starter_audience} yeni takipçi ve {starter_comments} yorumla birlikte genellikle {starter_likes} beğeni getirir."),
            ("Tek bir gönderi için az miktarda beğeni alabilir miyim?", "Hayır. Tek gönderiye beğeni satmıyoruz. Kampanya profilinizi tanıtır ve ulaştığı insanlar hangi gönderileri beğeneceklerini seçer; böylece paylaştığınız her şey şansını bulur."),
            ("Birkaç liralık beğeniler neden bu kadar ucuz?", "Çünkü arkalarında kimse yok. Yazılımla toplu üretilirler ve Instagram sahte etkinliği temizlediğinde kaybolabilirler."),
            ("En ucuz paket hangisi?", "Ayda {starter_price} ile {starter_name}. Sunduğumuz en düşük fiyat bu ve istediğiniz zaman iptal edebilirsiniz."),
            ("Gerçek beğeniler erişimime yardım eder mi?", "Gerçek beğeniler gönderilerinize gerçekten bakan insanlardan gelir; bu tür bir ilgi, satın alınmış bir sayacın asla yapamayacağı şekilde bir gönderinin yol almasına yardım eder."),
        ],
    },
    {
        "service": "likes",
        "modifier": "fast",
        "slug": "instagram/begeni/hizli",
        "label": "Hızlı Instagram beğeni?",
        "title": "Hızlı Instagram Beğeni: Önce Gerçek Takipçi | Growsterr",
        "description": "Anında Instagram beğenisi bot beğenisidir. Hızlı beğeni, gönderinizi paylaşır paylaşmaz gören gerçek takipçilerden gelir. Paketlerimiz o kitleyi kurar.",
        "h1": ("Hızlı Instagram beğenisi, ", "gönderiyi gerçekten görmüş insanlardan."),
        "intro": "Instagram beğeniyi hızlı, hatta anında mı satın almak istiyorsunuz? Anında beğeni bot beğenisidir: kimse görmediği bir gönderiye kalp bırakamaz. Beğenilerin çabuk gelmesini sağlayan şey, gönderilerinizi paylaştıktan kısa süre sonra gören gerçek insanlardan oluşan bir kitledir. Paketlerimiz o kitleyi beğenileriyle birlikte kurar: {pick_name} ile genellikle ayda {pick_likes}.",
        "hero": {"image": "instagram-real-people", "alt": "Yeni bir Instagram gönderisini paylaşıldıktan kısa süre sonra beğenen takipçiler"},
        "sections": [
            {
                "h2": "Çabuk beğeni almanın gerçek yolu",
                "p": [
                    "Paylaştıktan sonraki ilk saatler, takipçilerinizin gönderiyi gördüğü zamandır. Ne kadar çok gerçek takipçiniz varsa o kadar çok beğeni erken gelir; erken bir başlangıç da bir gönderinin daha uzağa gitmesine yardım eder.",
                    "Para ödemeye değer hız budur: bir kez desteklenen tek bir gönderi değil, bir öncekinden daha hızlı başlayan her yeni gönderi.",
                ],
            },
            {
                "h2": "Anında beğeniler neden gelip gider?",
                "p": [
                    "Bir ödemeden saniyeler sonra beliren beğeniler, meraka değil bir programa göre çalışan hesaplardan gelir. Tek bir blok halinde düşerler, yorum ya da takibe hiçbir şey katmazlar ve aynı hızla kaybolabilirler.",
                ],
            },
            {
                "h2": "Bizden ne beklemelisiniz?",
                "ul": [
                    "Kampanyanız sipariş verdikten sonraki ilk günlerde başlar.",
                    "Beğeniler ay boyunca, insanların en çok keyif aldığı gönderilere gelir.",
                    "Her yeni takipçi, sonraki gönderilerinizi de beğenebilecek biridir.",
                ],
            },
        ],
        "faqs": [
            ("Beğeniler ne kadar çabuk başlar?", "Kampanyanız başladıktan kısa süre sonra, ilk günlerde. Profilinizi daha çok insan buldukça ay boyunca gelmeye devam eder."),
            ("Paylaştığım an beğeni gönderebilir misiniz?", "İşaretle değil. Gerçek insanlar gönderileri gördüklerinde beğenir; kitleniz büyüdükçe her yeni gönderiyi paylaşıldıktan kısa süre sonra daha çoğu görür."),
            ("Anında beğeniler hesabıma zarar verir mi?", "Rakamlarınızı tuhaf gösterebilir: yorum ve yeni takipçi olmadan gelen bir beğeni patlaması. Sonraki gönderiler için de hiçbir şey yapmazlar."),
            ("Gerçek insanlardan çabuk beğeni mümkün mü?", "Evet, kendi takipçilerinizden. Önce kitlenizi büyütmemizin nedeni bu: beğenmek, gerçek takipçilerin yaptığı şeydir."),
            ("Bir paketle kaç beğeni gelir?", "{pick_name} genellikle ayda {pick_likes} beğeni getirir; sizi takip eden ve yorum yapan aynı insanlardan."),
        ],
    },
    {
        "service": "likes",
        "modifier": "female",
        "slug": "instagram/begeni/kadin",
        "label": "Kadınlardan Instagram beğeni?",
        "title": "Kadınlardan Instagram Beğeni mi? Neden Sunmuyoruz | Growsterr",
        "description": "Kadınlardan Instagram beğenisi satmıyor, cinsiyete göre hedefleme yapmıyoruz. Bu paketler sahte profillerle dolar; gerçek beğeni gerçek insandan gelir.",
        "h1": ("Kadınlardan Instagram beğenisi mi? ", "Gerçek beğeni cinsiyete göre ayrılmış gelmez."),
        "intro": "Kadın hesaplardan Instagram beğeni satın almak mı istiyorsunuz? Cinsiyete göre hedefleme yapmıyoruz ve kalbe kimin dokunacağına söz veremeyiz: o kararı her insan kendisi verir. Kadın beğeni paketleri, kadın gibi görünecek şekilde kurulmuş hesaplarla doldurulur. Bizim sunduğumuz, seçtiğiniz yerdeki gerçek insanlardan beğeniler; takipçi ve yorumla birlikte aylık bir paketin içinde.",
        "hero": {"image": "instagram-real-people", "alt": "Bir içerik üreticisinin Instagram fotoğrafını beğenen her türden insan"},
        "sections": [
            {
                "h2": "Kadın beğenileri neden bulunmaz da üretilir?",
                "p": [
                    "Gerçek bir insan, kim olursa olsun, keyif aldığını beğenir. Yalnızca kadınlardan beğeni siparişini doldurmak için bir satıcının komutla beğenen hesaplara ve siparişe uyan fotoğraflara ihtiyacı vardır. Neye benzerse benzesin, bu sahte bir profildir.",
                ],
            },
            {
                "h2": "Markalar gerçekte neye bakar?",
                "p": [
                    "Bir markaya kitlenizde çok sayıda kadın olduğunu göstermek istiyorsanız, tek bir gönderinin altındaki isimlere bakmaz, hesap istatistiklerinizi ister. Sahte profiller o tabloyu yalnızca bulandırır. Doğru yerde, onlara hitap eden içerikle ulaşılan gerçek insanlar tabloyu doğru kılar.",
                ],
            },
            {
                "h2": "Kitlenizi içerik ve konumla şekillendirin",
                "ul": [
                    "Ulaşmak istediğiniz insanların yaşadığı şehri ya da ülkeyi belirtin.",
                    "Önemsedikleri konularda düzenli paylaşım yapın.",
                    "Hangi gönderilerin en çok beğeni aldığına dikkat edin ve onlara benzer daha çok gönderi üretin.",
                ],
            },
        ],
        "faqs": [
            ("Yalnızca kadınlardan beğeni alabilir miyim?", "Hayır. Ne beğeni ne de başka bir şey için cinsiyete göre hedefleme sunuyoruz. Gönderilerinizi her türden insan görür; keyif alanlar da beğenir."),
            ("Bunun yerine erkeklerden beğeni seçebilir miyim?", "Hayır, aynısı geçerli. Sunduğumuz tek hedefleme konuma göredir: bir şehir, bir bölge ya da bir ülke."),
            ("Instagram'da daha çok kadına nasıl ulaşırım?", "Paylaştıklarınızla. Ulaşmak istediğiniz insanlara hitap eden içerik onları çekme eğilimindedir; doğru konum da kampanyanızın onlara ulaşmasına yardım eder."),
            ("Beğeniler her pakete dahil mi?", "Evet. Her pakette var: {pick_name} ile tipik bir ay, takip eden ve yorum yapan insanlardan {pick_likes} beğeni getirir."),
            ("Kadın beğenileri marka iş birliklerine yardım eder mi?", "Pek olası değil. Markalar sizi gerçekte kimin takip ettiğine ve kiminle etkileşime girdiğine bakar; uydurma profillerden gelen beğeniler buna dayanmaz."),
        ],
    },
    {
        "service": "likes",
        "modifier": "free",
        "slug": "instagram/begeni/ucretsiz",
        "label": "Ücretsiz Instagram beğeni?",
        "plan": "starter",
        "tool": "engagement-calculator",
        "title": "Ücretsiz Instagram Beğeni mi? Zamanınıza Değen Bu | Growsterr",
        "description": "24 saatte bir 10 ile 100 arası ücretsiz Instagram beğenisi botlardan ya da beğeniye beğeni uygulamalarından gelir. Ücretsiz hesaplayıcımızı deneyin.",
        "h1": ("Ücretsiz Instagram beğenisinin ", "her zaman bir bedeli var. Bedelsiz olanı anlatalım."),
        "intro": "Instagram beğeniyi ücretsiz, 24 saatte bir 10, 50 ya da 100 tane mi almak istiyorsunuz? Bu teklifler bot hesaplarla ya da giriş bilgilerinizi veya zamanınızı alan beğeniye beğeni uygulamalarıyla çalışır. Biz beğeni dağıtmıyoruz. Burada ücretsiz olan, aşağıdaki etkileşim hesaplayıcı ve daha çok beğeni kazanmanın dürüst yolları. Daha çok insana ulaşmak istediğinizde paketlerimiz gerçek insanlardan beğeni getirir.",
        "hero": {"image": "instagram-creator-studio", "alt": "Son Instagram gönderilerinin etkileşim oranını hesaplayan bir içerik üreticisi"},
        "sections": [
            {
                "h2": "Ücretsiz beğeni uygulamaları nasıl çalışır?",
                "ul": [
                    "Bot hesaplardan günlük 10 ile 100 arası beğeni; size daha büyük bir paket satmak için.",
                    "Kredi kazanmak için yabancıların gönderilerine dokunduğunuz beğeniye beğeni uygulamaları.",
                    "Instagram giriş bilgilerinizi isteyen ve hesabınızı başka gönderileri beğenmek için kullanan araçlar.",
                    "Aynı türden bot hesaplardan yorumlarınıza bedava beğeniler.",
                ],
                "p": [
                    "Hepsinin bir bedeli var: şifreniz, saatleriniz ya da asla geri gelmeyen hesaplarla şişirilmiş bir kitle.",
                ],
            },
            {
                "h2": "Önce etkileşim hesaplayıcıyla ölçün",
                "p": [
                    "Yukarıdaki hesaplayıcı ücretsizdir ve girdiğiniz hiçbir şey tarayıcınızdan çıkmaz. Takipçi sayınızı, sonra yakın tarihli tipik bir gönderinin aldığı beğeni ve yorumu girin; kitlenizin ne kadarının tepki verdiğini görün. Denediğiniz şeyin işe yarayıp yaramadığını görmek için birkaç hafta sonra yeniden bakın.",
                ],
            },
            {
                "h2": "Bir gönderiye daha çok beğeni kazanmanın ücretsiz yolları",
                "ul": [
                    "En güçlü görselinizle ya da videonuzun ilk saniyesiyle açın; insanlar hızlı karar verir.",
                    "Reels paylaşın: Instagram onları sizi henüz takip etmeyen insanlara gösterir.",
                    "Takipçileriniz gönderilerinizi beklesin diye istikrarlı bir ritim tutturun.",
                    "İnsanlara durmak, kaydetmek ya da paylaşmak için bir neden veren açıklamalar yazın.",
                ],
            },
        ],
        "faqs": [
            ("24 saatte bir ücretsiz beğeni alabilir miyim?", "Bizden hayır; gerçek insanlardan da hiçbir yerde. Günlük ücretsiz beğeniler, sizi ücretli bir pakete yönlendirmek için bot hesaplardan verilen bir numunedir."),
            ("Bir gönderiye ücretsiz nasıl beğeni alırım?", "Yavaş yol işe yarar: insanların görmek istediği bir şey paylaşın, takipçileriniz çevrimiçiyken paylaşın ve Hikâyenizde de paylaşın. Hiçbir maliyeti yok ve gerçek kitleniz büyüdükçe daha iyi işler."),
            ("Yorumlarıma ücretsiz beğeniye ne dersiniz?", "Ücretsiz uygulamalardan gelen yorum beğenileri aynı bot hesaplardan gelir. Gerçek olanlar, insanlar bir gönderinin altındaki sohbeti okuyup bir şeye katıldığında gelir."),
            ("Ücretsiz bir planınız var mı?", "Hayır. Ücretli paketlerin en küçüğü ayda {starter_price} olan {starter_name}; gerçek insanlardan genellikle {starter_likes} beğeni, ayrıca takipçi ve yorum getirir. İstediğiniz zaman iptal edin."),
            ("Hesaplayıcı gerçekten ücretsiz mi?", "Evet. İstediğiniz kadar kullanın. Hesabı tarayıcınızda yapar ve bize hiçbir şey göndermez."),
        ],
    },
    {
        "service": "likes",
        "modifier": "verified",
        "slug": "instagram/begeni/onayli",
        "label": "Onaylı hesaplardan Instagram beğeni?",
        "title": "Onaylı Hesaplardan Instagram Beğeni mi? Net Cevap | Growsterr",
        "description": "Kimse onaylı Instagram hesaplarından beğeni satamaz. Biz gönderinizi gören gerçek insanlardan beğeni getiririz, takipçiyle birlikte aylık bir pakette.",
        "h1": ("Onaylı hesaplardan Instagram beğenisi ", "kimsenin satabileceği bir şey değil."),
        "intro": "Onaylı Instagram beğeni, yani mavi tikli hesaplardan beğeni satın almak istiyorsanız dürüst cevap şu: biz satamayız, gerçek insanlarla çalışan kimse de satamaz. Onaylı kullanıcılar neyi seçerlerse onu beğenir. Paketlerimiz gönderinizi gören gerçek Instagram kullanıcılarından beğeni getirir; takipçi ve yorum da getiren bir paketin içinde.",
        "hero": {"image": "instagram-hub", "alt": "Bir içerik üreticisinin son gönderisine sıradan Instagram kullanıcılarından gelen beğeniler"},
        "sections": [
            {
                "h2": "Onaylı bir beğeni neyi eklerdi?",
                "p": [
                    "Kimsenin göreceği pek bir şey değil. Bir beğeni kim verirse versin aynı sayılır; mavi tik de ancak biri beğenenler listesini açarsa görünür. İnsanların hayal ettiği değer tanınmaktır; taklit bir hesaptan gelen tanınma da sahip olmaya değmez.",
                ],
            },
            {
                "h2": "Bu teklifler neden var?",
                "p": [
                    "Satıcılar mavi tikin ağırlığını bilir, bu yüzden hesapları resmî görünsün diye süslerler; bazen profil fotoğrafının içine bir rozet çizerek. Gerçek bir rozet bir hesaba dışarıdan eklenemez; bu da gerçekte neyin sunulduğunu anlatır.",
                ],
            },
            {
                "h2": "Gelmeye devam eden beğeniler",
                "p": [
                    "Gerçek beğeniler, sizi takip eden ve sonra ne paylaştığınızı gören insanlardan gelir. {pick_name} ile bu, takip eden ve yorum yapan aynı insanlardan, gönderilerinize yayılmış genellikle ayda {pick_likes} beğeni eder.",
                ],
            },
        ],
        "faqs": [
            ("Beğenilerinizden herhangi biri onaylı hesaplardan mı geliyor?", "İnsanları rozete göre seçmiyoruz ve asla onaylı beğeni vaat etmiyoruz. Ulaştığımız insanlar gönderinizi görüp beğenen sıradan Instagram kullanıcılarıdır."),
            ("Onaylı beğeniler mavi tik almama yardım eder mi?", "Hayır. Instagram doğrulamaya kendi süreciyle karar verir ve hiçbir beğeni satıcısı bunu etkileyemez."),
            ("Bir ünlüden gelen beğeni ödemeye değer mi?", "Yalnızca gerçeği bir anlam taşırdı, gerçek olanlar da satın alınamaz. Taklit bir hesaptan gelen beğeni, ödünç bir isim taşıyan bir bot beğenisinden ibarettir."),
            ("Instagram'da nasıl daha çok beğeni alırım?", "Gönderilerinizi gören ve daha fazlasını isteyen gerçek insanların sayısını büyütün. Paketlerimizin yaptığı bu; beğeni, takip ve yorum aynı insanlardan gelir."),
            ("Hesabıma erişiminiz gerekir mi?", "Hayır. Kullanıcı adınız yeterli; şifrenizi asla istemeyiz."),
        ],
    },
]
