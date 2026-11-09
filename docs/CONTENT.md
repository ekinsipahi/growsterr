# Para sayfaları: içerik rehberi

Instagram, TikTok ve YouTube satış sayfaları (`/instagram/followers/1000/` gibi) koddan değil,
içerik dosyalarından üretilir. Bu rehber yeni sayfa, yeni dil ve görsel eklemeyi anlatır.

## Kısaca sistem

- **Her sayfa bir varyanttır:** platform × hizmet × (adet) × (niteleyici) × dil.
  - Hizmetler: Instagram ve TikTok'ta `followers`, YouTube'da `subscribers`; ayrıca `likes`, `views`, `comments`.
  - Hizmeti olmayan sayfa, o platformun hub'ıdır (`/instagram/`).
- **İçerik yoksa sayfa da yoktur.** Route açılmaz, sitemap'e girmez, adres 404 verir. Böylece ince sayfa oluşmaz.
- **Dosyalar:**

| Dosya | İçinde ne var |
|---|---|
| `apps/pages/content/<dil>/<platform>.py` | `PAGES`: o dilde o platformun sayfaları, hub dahil |
| `apps/pages/content/<dil>/<platform>_<parça>.py` | Aynı platformun diğer sayfaları, parçalara bölünmüş (`instagram_countries.py`, `tiktok_quantities.py`…). Motor hepsini okur; bölmek, birden fazla kişinin aynı anda yazabilmesi içindir |
| `apps/pages/content/<dil>/articles*.py` | `ARTICLES`: platform × hizmet ızgarasının dışındaki sayfalar (rehber, rakip alternatifi, ödeme, agency, araç, niyet). Aşağıya bkz. |
| `apps/pages/content/<dil>/ui.py` | Her sayfada ortak olan metinler: bölüm başlıkları, "Nasıl çalışır", "Gerçek insan, bot değil" |
| `apps/pages/dimensions.py` | Boyutlar: platformlar, hizmetler, niteleyiciler (`MODIFIERS`), ülkeler |
| `apps/pages/images.py` | Görseller: dosya yolu, boyut, placeholder çizimi |
| `apps/pages/checks.py` | `check_pages` kuralları, yasak kelime listeleri dahil |

- **Kontrol:** `python manage.py check_pages`. Hata varsa komut 1 koduyla çıkar. Testler de bu kontrolü çalıştırır.
- **İçerik değişince sunucuyu yeniden başlat.** Route'lar açılışta kurulur; canlıda bunu deploy yapar.

## Anahtar kelime araştırmasından sayfaya

1. **Her niyet kümesine bir varyant açılır.**
   - "buy instagram followers" → `instagram` + `followers`
   - "buy 1000 instagram followers" → aynısına `quantity: 1000`
   - "real instagram followers" → aynısına `modifier: "real"`
2. **Aynı niyete iki sayfa açılmaz.** Benzer kelimeler aynı sayfanın başlığına, H1'ine, metnine ve SSS'ine dağıtılır.
3. **Yeni niteleyici önce sözlüğe girer.** `dimensions.MODIFIERS`'a eklenir, sonra sayfada kullanılır.
   - Bir platforma özelse sınırlanır: `"reels": ("instagram",)`.
   - `instant`, `free`, `cheap`, `bot` gibi kurallara aykırı niteleyiciler eklenmez.
4. **Adet sayfası bir hedeftir, paket değildir.** "1000 takipçi" sayfası, aylık paketin oraya nasıl götürdüğünü anlatır. Sayfadaki "nasıl ulaşırsınız" grafiği ve süreler kendiliğinden hesaplanır.

## Yeni sayfa (varyant) eklemek

`apps/pages/content/en/instagram.py` içindeki `PAGES` listesine bir sözlük eklenir:

```python
{
    # Kimlik: hangi varyant (dil dosyadan, platform dosya adından gelir)
    "service": "followers",            # hub için yazılmaz
    "quantity": 5000,                  # isteğe bağlı
    "modifier": "real",                # isteğe bağlı, dimensions.MODIFIERS'ta olmalı
    # Adres ve link metni
    "slug": "instagram/followers/5000",       # /<dil>/ önekinden sonraki yol
    "label": "{quantity} Instagram followers",  # diğer sayfaların link metni, en fazla 60 karakter
    # Meta
    "title": "...",                    # 20–65 karakter (yer tutucular doldurulduktan sonra)
    "description": "...",              # 70–160 karakter
    "updated": "2026-11-20",           # isteğe bağlı: gerçek içerik değişikliğinin tarihi (sitemap lastmod)
    # Sayfa
    "h1": ("Düz kısım ", "renkli vurgulu kısım."),   # ya da tek bir metin
    "intro": "...",                    # 1–3 cümle
    "hero": {"image": "instagram-followers-5000", "alt": "..."},
    "sections": [                      # sayfaya özel bölümler (isteğe bağlı)
        {"h2": "...", "p": ["paragraf", "paragraf"], "ul": ["madde", "madde"],
         "image": {"image": "...", "alt": "..."}},          # görsel isteğe bağlı
    ],
    "faqs": [("Soru?", "Cevap."), ...],  # en az 3 tane; FAQPage JSON-LD buradan üretilir
    # İsteğe bağlı
    "plan": "pro",                     # önceden seçili paket (yazılmazsa otomatik seçilir)
    "quantity_text": "...",            # adet bölümüne ek bir paragraf
    "included": [(başlık, metin), ...], "steps": [...], "compare": [...],  # ortak blokların yerine
}
```

Bunları yazmaya gerek yok, motor kendisi üretir:

- breadcrumb ve BreadcrumbList JSON-LD
- fiyatlı Product/Offer JSON-LD (puan ve yorum eklenmez)
- canonical ve hreflang
- dil menüsü
- ilgili sayfa linkleri (aynı platformun diğer hizmetleri, diğer platformlarda aynı hizmet, diğer adetler, diğer niteleyiciler)
- "Nasıl çalışır", "Neler dahil", "Gerçek insan, bot değil" blokları

### Yer tutucular

Fiyatı ve aralıkları elle yazma (`$79.99`, `1,000–4,000` gibi). Bunlar `apps/growth/plan.py`'den
otomatik doldurulur; fiyat ya da aralık değişince bütün sayfalar kendiliğinden güncellenir.

| Yer tutucu | Örnek |
|---|---|
| `{platform}` `{audience}` `{follow}` `{profile}` `{handle}` `{content}` | Instagram · followers · follow · profile · username · posts |
| `{service}` `{service_name}` | followers · Followers |
| `{quantity}` | 1,000 (yalnızca adet sayfalarında; dilin sayı biçimiyle) |
| `{from_price}` | en ucuz paketin fiyatı |
| `{starter_name}` `{starter_price}` `{starter_audience}` `{starter_likes}` `{starter_comments}` | paket adı, fiyatı, tipik aylık aralıkları |
| `{rising_…}` `{pro_…}` | diğer paketler için aynısı |
| `{pick_…}` | bu sayfanın önceden seçtiği paket |

Link metni (`label`) yalnızca ilk iki satırdaki kelime yer tutucularını kullanabilir.

### Önceden seçili paket

- **Adet sayfası:** tipik aylık aralığının ortası hedefe ulaşan en küçük paket seçilir. 1.000 → Starter, 5.000 → Rising, 10.000 → Pro.
- **Diğer sayfalar:** en popüler paket (Rising) seçilir.
- **Değiştirmek için:** `"plan"` yazılır.
- **Görüntülenme (views) adetleri:** tipik oran yok, bu sayfalarda `"plan"` yazılmalı. Yazılmazsa `check_pages` uyarır.

### Slug kuralları

- Küçük harf kullanılır. Kelimeler `-`, yol parçaları `/` ile ayrılır, başta ve sonda `/` olmaz.
- İngilizce slug bir dil koduyla başlayamaz (`de/...` olmaz).
- İngilizce hub slug'ları sabittir: `instagram`, `tiktok`, `youtube`. Menü ve footer bu adreslere link verir.
- Slug başka bir uygulamanın adresiyle çakışırsa (`pricing`, `account`, `order`...) `check_pages` hata verir.

## Niyet sayfaları (cheap, free, instant…)

İnsanlar satmadığımız şeyleri de arar. Her aramaya, o soruyu dürüstçe cevaplayan ve pakete
bağlayan bir sayfa açılır. Ayrıntılı açılar: `docs/keywords/WRITING.md`.

- Niteleyiciler `dimensions.MODIFIERS`'ta: `cheap`, `fast`, `free`, `free-trial`, `smm-panel`, `verified`, `female`, `ai`, `custom`.
- Normalde yasak olan kelime yalnızca kendi sayfasında serbesttir (`dimensions.INTENT_ALLOWS`):
  - `free` ve `free-trial` sayfası "free" diyebilir;
  - `verified` sayfası "verified/celebrity" diyebilir;
  - `female` sayfası cinsiyet kelimesini kullanabilir.

  Garanti, SEO ve sahte puan gibi diğer bütün kurallar orada da geçerlidir.
- Metin her zaman "bunu satmıyoruz, işe yarayan şu" der.
- `"tool": "engagement-calculator"` ya da `"growth-calculator"` sayfaya tarayıcıda çalışan bir hesaplayıcı ekler. Hiçbir veri gönderilmez.

## Makaleler (ızgaranın dışındaki sayfalar)

`articles*.py` içinde `ARTICLES = [...]`. Bir makale:

```python
{
    "article": "can-you-buy-instagram-followers",   # her dilde aynı anahtar (hreflang bununla eşleşir)
    "kind": "guide",        # guide | alternative | payment | agency | tool | intent
    "platform": "instagram",  # metindeki {platform} kelimeleri ve sipariş butonu bu platformla
    "slug": "guides/can-you-buy-instagram-followers",
    # geri kalanı para sayfasıyla aynı: label, title, description, h1, intro, hero, sections, faqs...
}
```

- Hizmet, adet, niteleyici ve ülke alanı yoktur.
- `guide` önce okuma düzeninde gösterilir (bölümler, SSS, sonra paketler) ve Article JSON-LD alır. Diğer türler para sayfası düzeninde ve Product JSON-LD ile gösterilir.
- Sitemap, hreflang ve dil menüsü kendiliğinden çalışır.
- Tür başına serbest kelimeler (`dimensions.ARTICLE_ALLOWS`):
  - `guide`: "free" ve "celebrity";
  - `payment`: "crypto";
  - `tool` ve `intent`: "free".
- Rakip adı yalnızca `alternative` sayfasında geçer. Orada da rakip hakkında hiçbir iddiada bulunulmaz.

## Yeni dil eklemek

1. `apps/pages/content/<kod>/` klasörünü ve içine boş bir `__init__.py` aç. Kodlar: `de nl fr it es pl ru uk ar sv da no ro az tr`.
2. `en/ui.py`'yi `ui.py` olarak kopyala ve değerleri çevir. Anahtarlar aynı kalır; eksik anahtarları `check_pages` listeler.
3. `<platform>.py` dosyalarına çevrilen sayfaları yaz.
   - Varyant alanları (`service`, `quantity`, `modifier`) İngilizcedekiyle aynı olur, hreflang sayfaları buna göre eşleştirir.
   - Slug, metinler ve alt metinleri o dilde yaz.
   - Bir dilde olmayan sayfa o dilde açılmaz. Tek tek çevirerek yayına alabilirsin.
4. `python manage.py check_pages --lang <kod>` çalıştır.

Sonuç:

- **Adres:** `/<kod>/<slug>/`. İngilizce sayfalar kökte durur.
- **hreflang:** sayfanın bulunduğu her dil, artı `x-default`, yani İngilizce sürüm.
- **Dil menüsü:** o dilde aynı sayfa yoksa en yakın üst sayfaya gider (hizmet sayfası, yoksa hub).
- **Arapça:** sağdan sola görüntülenir, ayrı bir iş gerekmez.

## Görseller

1. **`apps/pages/images.py`'ye bir kez tanımla.** Tanım bütün dillerde ortaktır.
   ```python
   "instagram-followers-5000": {"src": "img/pages/instagram/followers-5000.webp",
                                "width": 1600, "height": 1200, "art": "growth", "pending": True},
   ```
   - `width` ve `height`: dosyanın gerçek boyutu. Yer tutucu da bu oranda çizilir, görsel gelince sayfa kaymaz.
   - `art`: dosya gelene kadar gösterilecek marka çizimi. Seçenekler: `hub followers subscribers likes views comments growth`.
2. **İçerikte id ile kullan.** Alt metni her dil kendi yazar: `"hero": {"image": "instagram-followers-5000", "alt": "..."}`.
3. **Dosya gelince** `static/img/pages/...` altına koy, `"pending"` satırını sil ve `check_pages` çalıştır.
   - Dosya varken `pending` duruyorsa uyarı verir.
   - Dosya yokken `pending` yoksa hata verir.

Öneriler:

- **Biçim:** WebP. Hero 1600×1200 (4:3), bölüm görseli 1200×900.
- **İçerik:** stok fotoğraf, uydurma rakamlı ekran görüntüsü, rakip ya da ünlü görseli kullanılmaz.
- **Yükleme:** hero hemen yüklenir (sayfanın ilk görüntüsü). Bölüm görselleri lazy yüklenir.
- **Paylaşım:** görsel dosyası gelince Product JSON-LD'ye ve `og:image`'a kendiliğinden eklenir.

## Sayfa sitemap'e nasıl girer

İçerik dosyasında olan her sayfa sitemap'e kendiliğinden girer, elle bir şey yapılmaz.

| Adres | İçinde ne var |
|---|---|
| `/sitemap.xml` | index |
| `/sitemaps/pages-<dil>.xml` | o dildeki bütün sayfalar, hreflang alternatifleriyle |
| `/sitemaps/core.xml`, `/sitemaps/legal.xml`... | diğer uygulamaların sayfaları (her uygulamanın `sitemap.py` `entries()` fonksiyonundan) |

- **lastmod:** sayfanın `updated` alanı; yoksa dosyanın başındaki `UPDATED` değeri. Gerçek bir içerik değişikliğinde güncellenir.
- **Hesap, sipariş ve admin adresleri** sitemap'e asla girmez. Bir uygulama yanlışlıkla verirse ayıklanır.
- **Önbellek:** sitemap 1 saat önbellekte tutulur.

## Metin kuralları

Her dilde ve her metinde, alt metinler dahil, geçerlidir.

- **Arama motoru konusu yok:** "SEO", arama motoru, anahtar kelime ve sıralama geçmez.
- **Yasak sözler:** garanti, ücretsiz/bedava, kripto, ünlü ya da onaylı yorum, cinsiyet hedefleme, sahte yorum ve puan.
- **Instant / anında:** yalnızca "biz yapmıyoruz, anında = bot" anlamında geçer.
- **Tek başına satış yok:** beğeni, izlenme ve yorum hep paketin içinde anlatılır.
- **Rakamlar söz değildir:** "tipik aylık aralık", "genellikle" gibi ifadeler kullanılır.
- **Şifre istenmez.** Rakip adı da geçmez.

`check_pages` yasak kelimelerin çoğunu 16 dilde yakalar (`apps/pages/checks.py`, `FORBIDDEN_LANG`). "Instant" ve "tek başına satış" gibi anlam kurallarını ise ancak okuyarak kontrol edebilirsin.

## Komutlar

```bash
python manage.py check_pages               # bütün içerik
python manage.py check_pages --lang de     # tek dil
python manage.py check_pages --strict      # uyarılar da hata sayılır
DEBUG=True python manage.py test apps.pages
```
