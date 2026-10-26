# İlk demo ve gerekli genel oyun tasarımı — karar ve cevap belgesi

Sürüm: 1.0 · Tarih: 2026-09-07 · Durum: **PAPER ONLY — müşteri karar paketi**.
Oynanabilir demo veya seçilmiş bütün tasarım kararları henüz yok. Bu dosya yanıt toplar
ve teknik çalışma sözleşmesini kaydeder; beş yaşayan tasarım belgesinin yerine geçmez.

**2026-09-08: bu form yanıtlandı.** Aşağıdaki soru kartları soru sürümünü korur;
boş örnek form güncel karar durumu değildir. [Yanıt kaydı ve sonraki karşılaştırmalar](DEMO_ANSWER_REVIEW_2026-09-08.md)
seçilmiş, kısmi ve açık cevapları ayrı tutar. Yeni kişi/F33 kapsam dışlama/pixel art/
kesin ölüm/ayar kaydı yönleri tarihsel 'bilinenler' listesini gerektiği yerde günceller.

## Amaç ve kullanım

Bu paket, ilk demoyu üretmek için gereken genel oyun temellerini ve demo kararlarını
aynı yerde ele alır. Tam ana oyun kampanyasını, bütün düşman/kart kataloğunu veya
nihai ekonomik dengeyi bitirmeye çalışmaz. Kamera, dünya bağlantısı, beden görünürlüğü
ve oyuncu vaadi gibi demo maliyetini belirleyen genel tercihler şimdi seçilir;
ilerideki bütün odalar/uzuvlar/sonlar kapsam dışında tutulur.

60 karar başlığı vardır; 60 uzun cevap gerekmez. Seçenek harfi, bir cümle veya aşağıdaki
yöntemlerden biri yeterlidir. Bir başlığın altında istenen bağlı ayrıntıları bilmiyorsan
yetki/sınır belirterek bana bırakabilirsin. **Öneriler önceden seçilmiş cevap değildir.**

| Cevap biçimi | Nasıl işlenir? |
|---|---|
| A / B / C veya kendi cevabım | O soru kapsamındaki tercihin kaydedilir; açıkça çelişiyorsa çelişki çözülmeden uygulanmaz |
| ÖNER | Tercih seçilmez; gerekçeli bir aday ve maliyeti hazırlanır |
| KARŞILAŞTIR: benim için önemli ölçüt | İki/üç aday o ölçütte karşılaştırılır; gerekiyorsa paper örneği veya sonradan izinli test tanımlanır |
| SEN SEÇ: sınırlarım | O sorunun kapsamındaki kararı sınırların içinde benim vermeme yetki verir; karar/gerekçe/geri dönüş koşuluyla dosyalanır |
| ÖNERİYİ KABUL EDİYORUM | Yalnız açıkça belirttiğin F kimliklerindeki görünür öneriyi seçer; belgenin bütününü otomatik onaylamaz |
| KOŞULLU: F06=B ise ..., değilse ... | Önkoşulun cevabı geldikten sonra uygun dal çözülür |
| DEMODA OLMASIN | Gerekli kabulü kırıp kırmadığı denetlenir; ana oyundan silme değildir |
| BİLMİYORUM / boş | OPEN kalır; onay sayılmaz. İstersen bunun yerine ÖNER veya SEN SEÇ kullan |

SEN SEÇ, önceden seçilmiş iki normal savaşı, asimetrik donor yönünü, temel kaynak
kurallarını veya runtime kapısını örtük değiştirmez. Değiştirmek istiyorsan açık yaz.
Gerçek yeni çelişki varsa ilgili seçenek geri getirilir; aynı verilmiş yetki tekrar sorulmaz.

## Şimdiden bilinenler — tekrar cevaplama

- Tek oyunculu PC örneği, cehennemde bir ruh karakteri.
- İki normal NPC: biri insan, biri yakın toplam tehditte asimetrik beden.
- **2026-09-07 owner tercihi: yeni uzvu asimetrik NPC'den almak.** Bunu mevcut yön
  olarak kullanıyoruz. Bu cevap rakibin ilk mi ikinci mi olduğunu belirlemiyor.
- Boss, ana oyunda da amaçlanan görece güçlü bir aktör; yeni mekanik kullanabilir.
- Kısa boss karşılaşması sonrası amaçlanan final oyuncunun yenilgisi ve demo sonu.
- Beden kaynaklı eylemler; en fazla bir Preparation + bir Main; saldırı QTE'si yok.
- Yellow → Block/Parry, Red → Evade; aynı görünür dünyada etkileşim; dövüş menzili yok.
- Kill → Blood ve o donorun uzvuna erişim kaybı; yaşayan teslimiyet → uzuv, kill-Blood yok.
- Graft somut oynanış farkı ve görünür bedel taşımalı; no-graft rota geçerli kalmalı.
- Concept/Brain temel ayrımı korunur; demodaki kazanım/kullanım kapsamı yeniden seçilecek.
- Unity ve sabit açılı stilize 3B önceki **hipotezlerdir**; seçilmiş nihai motor/kamera değildir.
- Şimdiki iş yalnız dosyalama. Engine projesi, asset kurulumu veya demo runtime'ı başlatılmaz.

## Soruların işlenme algoritması

1. Yanıtları F kimliklerine bağla; mevcut kararları tekrar oylama.
2. Önce hedef/öncelik ve kamera/dünya yönü; ardından açılış/aktör/graft; sonra combat/boss;
   en son sunum, kayıt ve teslim bütçesi etkilerini çöz. Bölümler okuma düzenidir;
   kartlarda ileri bir F'ye bağımlılık varsa cevabı koşullu tut.
3. Seçim, yetki devri, aday öneri ve teknik olguyu ayrı sınıflandır.
4. Bağımlılıkları sırala. Önkoşulu OPEN olan cevabı **koşullu** sakla; varsayımla kapatma.
5. Çakışma kontrolü: örneğin insan önce + donor asimetrik + yalnız iki savaş + normal
   savaşta graft testi birlikte seçilirse üçüncü savaş icat etme. Sıra veya kanıt
   beklentisinden hangisinin değişeceğini görünür yap.
6. SEN SEÇ verilen sınırlar içinde exact içerik/test setini üret; temel tercih verilmemişse
   “en popüler” seçeneği gerçek owner kararı gibi yazma.
7. Her seçimi kaynak cevap/tarih, gerekçe, maliyet, bağlı Q/R/T ve yeniden açma koşuluyla
   yaşayan belgeye işle. Teknik kararlar aşağıdaki kayıtta tutulur.
8. Sayısal ve içerik tablolarını doldur; iki kaynak rotası ve boss sonunu normal/olumsuz
   örneklerle kontrol et. Test edilmemiş eğlence veya erişilebilirlik kanıtı üretme.
9. Kapanışı üç ayrı sütunda raporla: **kağıt kararı seçildi / uygulama işi tanımlı /
   gerçek oynanışta sınanacak**. Soru sayısının bitmesi D0 kapanışı değildir.
10. Tek cevap mesajından sonra mümkün olan tüm kararları işlerim. ÖNER, KARŞILAŞTIR veya
    gerekli alanlarda boş cevap bırakırsan, ikinci karar turu gerekebilir; bunun nedenini
    yalnız kalan çelişki ve eksiklere indirgerim. Bir mesajda bütün tercihlerin kesin
    kapanacağını önceden garanti edemeyiz.

## Soru kartları

Her karttaki Q numaraları mevcut planla izlenebilirlik içindir; cevapta yalnız F numarası yeterli.
Seçenekler gerçek alternatiflerdir; serbest cevap bütün kartlarda geçerlidir.

| Cevap grubu | Başlıklar | Neyi belirler? |
|---|---|---|
| F01-F05 | Genel oyun temeli | Hedef oyuncu, his, oturum/dünya ve geleceğe verilen söz |
| F06-F11 | Kamera ve hareket | Bakış açısı, 2B/3B, beden, ton, traversal ve dövüş kadrajı |
| F12-F17 | Demo açılışı | Asimetrik donorun sırası, Guard, hedef, ruh/beden ve ilk bilgi |
| F18-F21 | NPC içeriği | Amaç, anatomi, konuşma ve davranış farkı |
| F22-F26 | Graft | Yeni işlev, bedel, işlem, no-graft yolu ve sonraki deneme |
| F27-F38 | Savaş/ilerleme | Zorluk, savunma, Will, yaralar, kartlar, bakım, Concept/Brain |
| F39-F44 | Boss/final | Rol, imza kuralı, kayıp, yerel etki, kapanış ve süre |
| F45-F49 | Sunum | Öğretim, dil, UI, erişim ve ses |
| F50-F53 | Tekrar/kayıt | Erken ölüm, kalıcılık, son ekran ve iki rota gözlemi |
| F54-F58 | Üretim | Dağıtım, cihaz, asset/kalite, zaman ve test |
| F59-F60 | Karar yetkisi | Bilinmeyen sayılar ve tasarım tercihlerinin nasıl kapanacağı |

### Dallanma kuralları — gereksiz ayrıntıyı atla

| Cevap | Sonraki işlem |
|---|---|
| F06 birinci şahıs | F08'de uzuv/beden görünürlüğünü bu görüşe göre çöz; üçüncü şahıs takip-kamera ayrıntısı isteme |
| F07 2B/2.5B | 3B rig/model üretimini zorunlu tutma; seçili açıda uzuv değişimi/okunurluk için karşılık yaz |
| F12 asimetrik önce | F26'nın normal ikinci savaş kanıtını uygula; yeni prova veya boss öğretim evresi ekleme |
| F12 asimetrik ikinci | F26'da seçilmiş prova/evreyi tanımla; normal savaşta graft testi yokluğunu kaydet |
| F13 Guard çıkarılsın | Q03/G1 dallarını demo için gerekçeli N/A yap; başlangıç bedeni ve ekonomi yine doldurulur |
| F33 bir koruma ertelensin | O korumanın demo tetik/charge tablosu N/A; kalan ölüm ve boss kuralı yeniden kontrol edilir |
| F37 Brain kazanımı ertelensin | Brain ödül/equip/use kanıtı N/A; korunmuş temel mimari ve seçili Concept kapsamı ayrıca değerlendirilir |
| F51 yalnız ayarlar | Oyun kaydını sürdürme/ödül-disk testleri N/A; ayar kaydı ve erken retry davranışı devam eder |
| F54 özel yerel test | Mağaza/hesap/yayın işi ekleme; F52 harici bağlantı ancak açık hedef seçilmişse hazırlanır |
| F59 SEN SEÇ | P01-P12'nin uygulanabilir gameplay ayrıntılarını verilen sınırlarla ajan doldurur; ÖNER seçilirse aday olarak bırakır |

N/A yalnız bağlı kapsam gerçekten dışlandığında kullanılır; gerekli bir kararı saklamak
için kullanılamaz. Çocuk sorulara verilmiş cevaplar dal değişirse silinmez, koşullu saklanır.

## A — Genel oyundan demoya taşınacak temel

### F01 — Kimin için tasarlıyoruz?

İlk demonun hedef oyuncusunu ve oyun deneyimini tarif et.

A) Strateji/kart oyuncusu (başlangıç önerisi). B) Aksiyon ağırlıklı oyuncu. C) İkisine de yeni oyuncu.

**Neden / sınır:** A, mevcut düşünme ağırlığıyla uyumlu; refleks beklentisinin ayrıca yönetilmesi gerekir.

Bağ: Q29,Q23. Önkoşul: Yok.

### F02 — Öncelik ve vazgeçilmeyecek his

Beden değiştirme, taktik ustalık ve cehennem hikâyesini önem sırasına koy; bir vazgeçilmez ve bir istemediğin his yaz.

Öneri: bedenle değişen taktik > ustalık > hikâye merakı. Kendi sıralamanı verebilirsin.

**Neden / sınır:** Aynı sahnede her hedefi eşit büyütmek kapsam ve okunurluk çatışması yaratabilir.

Bağ: Q29. Önkoşul: F01.

### F03 — Genel oyunun oturum omurgası

Genel oyunda bir denemenin neyi başlatıp neyle bittiğini hangi yönde düşünüyoruz? İlk demo bunun neresinden kesit?

A) Aynı günü öğrenerek farklı beden/rota denemek (mevcut modelden öneri). B) Bölgeler boyunca devam eden kampanya. C) Sefer/hub ve geri dönüş.

**Neden / sınır:** Bu genel yön seçilir; tüm kampanya süresi ve haritası şimdi tasarlanmaz. Ölüm/progression etkisi F37/F50'ye taşınır.

Bağ: Q29,Q20. Önkoşul: F02.

### F04 — Genel dünya bağlantısı

Dünyada ilerlemek daha çok nasıl hissettirsin?

A) Birbirine bağlanan, seçilmiş yolları olan küçük bölgeler (öneri). B) Hub'dan seçilen seferler. C) Geniş serbest dolaşım.

**Neden / sınır:** A, küçük demoyla temsil edilebilir; C seçilirse ilk örneğin serbest dünya derinliğini kanıtlamadığı açık yazılır.

Bağ: Q29,Q31. Önkoşul: F03.

### F05 — Ana oyuna verilen sözün sınırı

Demo sonunda geleceğe dair hangi tek şeyi vaat edebiliriz; hangi sırları saklamalıyız?

A) Farklı bedenlerin yeni çözüm yolları (öneri). B) Cehennem/ruh döngüsünün gizemi. C) Boss ve dünya hiyerarşisini aşmak.

**Neden / sınır:** Gösterilmeyen bir sistemi çalışıyormuş gibi pazarlamayız. İlerideki kesin boss karşı hamlesi tasarlanmadan vaat edilmez.

Bağ: Q29,Q28. Önkoşul: F02,F03,F04.

## B — Kamera, beden görünürlüğü ve hareket

### F06 — Bakış açısı

Genel oyunun ve ilk demonun bakış açısını seç. İkisinin farklı olmasını istiyorsan ayrı belirt.

A) Birinci şahıs: karakterin gözünden. B) Üçüncü şahıs, sabit/yüksek açı (önceki hipotez; öneri). C) Üçüncü şahıs, serbest takip kamerası.

**Neden / sınır:** B'de iki beden ve hedef bölgeleri aynı anda göstermek kolaylaşabilir; A beden hissini, C kamera özgürlüğünü öne çıkarır. Bunlar sınanacak tasarım öngörüleridir.

Bağ: Q30,Q21. Önkoşul: F02.

### F07 — Görsel üretim biçimi

Mekân ve bedenler nasıl üretilecek? F06 ile tutarlı bir biçim seç.

A) Stilize, sade 3B (öneri). B) 2B/2.5B çizim veya piksel. C) Gerçekçi 3B.

**Neden / sınır:** A önceki adayla uyumlu; B'de açı/uzuv varyantları, C'de model/animasyon üretim yükü ayrıca karşılaştırılmalı. Eski dışlama ifadeleri kesin karar değildir.

Bağ: Q30,Q22. Önkoşul: F06.

### F08 — Kendi bedenini ve uzuv değişimini görme

Kazanılan ve kaybedilen uzuvları hangi yüzeylerde görmek istiyorsun?

A) Dünyadaki karakter + açılabilir beden incelemesi (öneri). B) Birinci şahısta uzuvlar + beden paneli. C) Ayrıntılı beden modeli yalnız incelemede.

**Neden / sınır:** A/C, F06'nın birinci şahıs seçimiyle gerekirse uyarlanır; sadece ikon değiştirmek fiziksel graft gösterimi yerine geçmez.

Bağ: Q30,Q21. Önkoşul: F06,F07.

### F09 — Görsel ton ve rahatsızlık sınırı

Ton, şiddet/beden korkusu ve istemediğin görüntüleri belirt; varsa iki referans ve her birinden alınacak özelliği yaz.

A) Stilize karanlık beden korkusu (öneri). B) Daha soyut, düşük grafik şiddet. C) Yoğun anatomik/grafik şiddet.

**Neden / sınır:** Şiddet seviyesi durum okunurluğunu ve içerik üretimini etkiler. Bu seçim yaş sınıflandırması yapıldığı anlamına gelmez.

Bağ: Q30,Q22. Önkoşul: F02,F07.

### F10 — Dünya içindeki hareket

Dövüş dışında oyuncu karakteri nasıl yönlendirsin?

A) Yön tuşlarıyla serbest yürüme (öneri). B) Tıklanan yere yürüme. C) Sınırlı noktalar arasında geçiş.

**Neden / sınır:** Zıplama, tırmanma, sprint, fizik bulmacası istiyorsan tek tek ekle; yoksa bu eylemler onaylı sayılmaz. Dövüşe menzil/konum sistemi eklenmez.

Bağ: Q31,Q21. Önkoşul: F04,F06.

### F11 — Dövüşte kamera ve geçiş

Dünya üzerinde açılan dövüş arayüzünde kamera nasıl davransın?

A) Aynı sahnede sabit okunur kadraj (öneri). B) Aynı sahnede kısa yaklaşma/açı geçişi. C) Oyuncu aynı sahnede kamerayı çevirebilsin.

**Neden / sınır:** A en az kamera yönetimini ister; diğerlerinde hedef seçimi, örtülme ve savunma işaretleri ayrıca sınanır. Ayrı savaş ekranı mevcut karar değildir.

Bağ: Q30,Q21. Önkoşul: F06,F10.

## C — Demo sırası ve açılış

### F12 — Asimetrik donorun sırası

Yeni uzvun kaynağı asimetrik rakip olacak yönünde ilerliyoruz. Bu rakip hangi sırada olsun?

A) Asimetrik → graft → insan → boss (öneri). B) İnsan → asimetrik → graft → savaş dışı kısa prova → boss. C) İnsan → asimetrik → graft → boss'ta önce bilinen kurallı evre.

**Neden / sınır:** A graft'ı normal savaşta denetir ama ilk öğretimi zorlaştırabilir. B prova ekler; C boss zorluğu ile graft etkisini karıştırır. İkisinde eksik normal-savaş kanıtı açık kalır; üçüncü normal savaş yok.

Bağ: Q26. Önkoşul: F02.

### F13 — Guard ve eski şehir açılışı

Önceki esaret/Guard tavizi açılışını ne yapalım?

A) Kısa, dövüşsüz taviz olarak koru. B) Cehenneme doğrudan başlangıç; Guard'ı bu demodan çıkar (sadelik önerisi). C) Aynı bedensel bedeli başka bir açılışa uyarla.

**Neden / sınır:** A için reddetme/bağlı saldırı/ödeme sonuçları tanımlanır; B/C mevcut başlangıç bedeni ve ekonomi hesaplarını değiştirir. Çıkarma ancak yanıtla seçilir.

Bağ: Q27,Q03. Önkoşul: F12.

### F14 — Oyuncunun hemen şimdi amacı

Karakter ilk birkaç dakikada ne elde etmeye çalışıyor; bu neden iki NPC'ye ve boss'a götürüyor?

A) Bir geçide ulaşmak (işlevsel öneri). B) Yaşamak için bedensel bir ihtiyacı gidermek. C) Bir kişi/iz/cevabı bulmak.

**Neden / sınır:** Bir cümle hedef + engel yeterli; kozmoloji anlatımı ilk eylemin yerini almamalı.

Bağ: Q28. Önkoşul: F03,F13.

### F15 — Ruh ve beden ilişkisi

Cehennemdeki ruhun oynadığımız bedenle ilişkisi ne?

A) Ruh maddi bir bedende eyleyebilir; beden değişebilir (öneri). B) Beden ruhun fiziksel yansımasıdır. C) Ruh kendisine verilmiş/ödünç bir bedende başlar.

**Neden / sınır:** Ölümün anlamını F43/F50 ile bağla. Yeni soul barı, bedensiz dolaşım veya yeni kaynak bu seçeneklerden otomatik çıkmaz.

Bağ: Q28. Önkoşul: F03,F14.

### F16 — Başlangıç karakteri ve bedeni

Sabit karakterin başlangıç durumunu, kişiliğini ve özelleştirme ihtiyacını belirt.

A) Sabit sıradan insan bedeni ve sınırlı kişilik (öneri). B) Sabit eksik/yaralı beden; eksik işlevi tarif et. C) Küçük bir başlangıç bedeni seçimi.

**Neden / sınır:** Demo karakteri tek bir ruh olarak kalır; görünüş/isim seçimi isteniyorsa kapsamı yaz. Graft yeni işlev getirebilir; başlangıçta eksik uzuv zorunlu değildir.

Bağ: Q04,Q28. Önkoşul: F13,F15.

### F17 — İlk sahnede bilgi miktarı

Oyuncu ve karakter başlangıçta hangi gerçekleri biliyor?

A) Cehennem, mevcut beden ve yakın amaç açık; köken gizemli (öneri). B) Karakter bilir, oyuncu aşamalı öğrenir. C) İkisi de büyük ölçüde bilgisiz.

**Neden / sınır:** B/C'de belirsizlik eylem kurallarını saklamamalı; bilinmeyen hikâye ile bilinmeyen maliyet ayrı tutulur.

Bağ: Q28,Q22. Önkoşul: F14,F15,F16.

## D — İki normal NPC'nin içeriği

### F18 — İnsan NPC'nin nedeni

İnsan NPC ne istiyor, neden dövüşüyor ve neden durabilir?

A) Hayatta kalmak için Blood/tedavi ihtiyacı (öneri). B) Görev/bağlılık yüzünden yolu tutmak. C) Kendi hedefi için oyuncuyu kullanmak.

**Neden / sınır:** İstersen tek cümle motif ver; ayrıntılı Goal/Need/RedLine/Claim tablosunu bu sınırda ben yazarım. Nihai isim şart değildir.

Bağ: Q15,Q28. Önkoşul: F12,F14.

### F19 — Asimetrik NPC'nin bedeni ve nedeni

Güçlü uzvu dışında hangi işlevi eksik; kendisi ne istiyor?

A) Güçlü kol, sınırlı bacak işlevi. B) Güçlü bir kol, diğer kol eksik. C) Kendi bileşimin; üstün ve eksik işlevi birlikte yaz.

**Neden / sınır:** Öneri B: kaynak kaybı doğrudan savunma/saldırı seçeneklerinde görülebilir. A seçilirse Red savunması gibi yollar otomatik kapatılmaz; gerçek denge karşılaştırması gerekir. Motif F18'den farklılaşmalı.

Bağ: Q15,Q16,Q28. Önkoşul: F12,F14.

### F20 — NPC iradesi ve konuşma yoğunluğu

İki NPC'nin hedef ve pazarlıkları ne kadar konuşmayla anlatılsın?

A) Kısa niyet + sınırlı anlaşma/reddetme replikleri (öneri). B) Birkaç dallanan konuşma. C) Ağırlıkla davranış ve çevresel anlatım.

**Neden / sınır:** Her seçenekte teslimiyet ve iddia anlaşılır kalır; ek konuşma dalları yeni ödül veya üçüncü çatışma yaratmaz.

Bağ: Q12,Q13,Q15,Q22. Önkoşul: F18,F19.

### F21 — Normal düşmanların farkı

İki normal düşmanın temel dövüş davranışı hangi farkı taşısın?

A) İnsan temel saldırı/savunma, asimetrik tek güçlü uzvuna dayalı riskli oyun (öneri). B) İnsan daha temkinli, asimetrik agresif. C) Kendi karşıtlığın.

**Neden / sınır:** Kart ve saldırı sayısını F59 kapsamında ben çıkarabilirim; her biri oyuncuya yeni bir karar göstermeli. Tam düşman kataloğu gerekmiyor.

Bağ: Q15,Q22. Önkoşul: F18,F19,F27.

## E — Yeni uzvun oynanış farkı

### F22 — Uzuvla hangi davranış değişsin?

Asimetrik rakipten alınan uzuv neyi yapabilmeyi değiştirsin?

A) Kıskaç benzeri kol: tutma/baskı rolü. B) Zırhlı kol: farklı korunma/karşılama rolü. C) Uzanan/esnek kol: yeni kaynak/çoklu kaynak etkileşimi.

**Neden / sınır:** Öneri A, net bir farklı eylem adayıdır; otomatik stun kilidi değildir. C dövüş menzili eklemez. Tür/şekil ve özel hareketi başka türlü de tarif edebilirsin.

Bağ: Q16. Önkoşul: F19.

### F23 — Yeni uzvun bedeli

Yeni yeteneği kazanırken hangi tür bedel daha ilginç?

A) Önceki bir hareket/savunma seçeneğinin kaybı (öneri). B) Belirli kullanımda Blood veya bakım baskısı. C) Güçlü eylem sonrası açık/sonraki seçenek kısıtı.

**Neden / sınır:** Bedel önceden görünür ve gerçek olmalı; global rastgele ceza veya bütün zaman pencerelerini gizlice küçültme yok. Tam miktar F59 ile hazırlanabilir.

Bağ: Q16,Q17. Önkoşul: F22.
ü
### F24 — Transferin sunumu ve konumu

Yaşayan teslimiyetten sonra Grafting Table geçişi nasıl sunulsun?

A) Aynı mekânda kısa masa işlemi (öneri). B) Bağlı güvenli küçük odada masa. C) Kısa anlatı/animasyon geçişiyle işlem.

**Neden / sınır:** Sökme, takma, tedavi, onarım ve Blood maliyeti ayrı sonuçlardır; bu sunum seçimi bedelsiz işlem veya otomatik tam iyileşme onayı değildir.

Bağ: Q16,Q17,Q22. Önkoşul: F12,F22.

### F25 — Graft almayan oyuncu

Oyuncu asimetrik NPC'yi öldürüp Blood alırsa öğretim nasıl devam etsin?

A) Sonucu açık göster, no-graft rotası sürsün; başka denemede graft'ı keşfetsin (öneri). B) Önceden güçlü öğretim uyarısı ver, seçim yine serbest kalsın.

**Neden / sınır:** Graft her tek oturumda garanti değil. Zorunlu graft istiyorsan bunu mevcut kill/limb serbestliğiyle açık bir tasarım revizyonu olarak belirt; gizli yeniden doğan donor eklenmez.

Bağ: Q17,Q23. Önkoşul: F12,F22.

### F26 — Graft'ı fiilen deneme anı

Seçtiğin sırada oyuncu hangi somut eylemle yeni kazancı ve bedeli görecek?

A) Sonraki normal rakipte bir yeni eylem + kaybolan seçenek (F12=A için öneri). B) Kısa güvenli prova (F12=B). C) Boss'un yeni kuralından önce sınırlı eylem fırsatı (F12=C).

**Neden / sınır:** Karakter gücüyle birlikte düşman/sahne de değiştiğinden bunu kontrollü deney diye adlandırmayız. Somut hareketi bilmiyorsan seçtiğin uzuv sınırında SEN SEÇ yaz.

Bağ: Q16,Q26,Q23. Önkoşul: F12,F22,F23.

## F — Savaşın his ve kural tercihleri

### F27 — Zorluk ve öğrenme temposu

İlk normal dövüş ve ikinci dövüşün baskısı nasıl artsın?

A) İlk anlaşılır ve hatayı tolere eden, ikinci kombinasyon isteyen (öneri). B) Baştan yüksek baskı. C) İkisinde düşük baskı, asıl zorluk boss'ta.

**Neden / sınır:** Blood/hasar/tur sayısı henüz seçilmez; amaç ve hata toleransını buradan türeteceğim. Kısa boss yüksek hasar demek değildir.

Bağ: Q11,Q12,Q23. Önkoşul: F01,F02.

### F28 — Savunma girişi ve yardım

Block/Parry/Evade için tercih ettiğin girdi ve yardım davranışı nedir?

A) Ayrı okunur savunma girdileri; ayarlanabilir hız/pencere ve isteğe bağlı otomasyon (mevcut aday öneri). B) Ortak zaman girdisi + önceden seçilen savunma. C) Kendi düzenin.

**Neden / sınır:** Yellow/Red eşlemesi korunur. Tuşlar F55'te seçilen cihazla belirlenir; sürüklemenin klavye alternatifi bulunur. Yardımın erişim yeri ve ilk açılış varsayılanını da belirt veya SEN SEÇ.

Bağ: Q11,Q21. Önkoşul: F06,F27.

### F29 — Oyuncuya gösterilen kesinlik

Saldırı niyeti ve maliyetlerde ne kadar sayısal bilgi gösterelim?

A) Kaynak/target ve kesin maliyet; sonuçlar okunur sayıyla (öneri). B) Kesin maliyet, sonuçta açık aralık/şiddet sınıfı. C) Sayılar ayrıntı panelinde.

**Neden / sınır:** Kaynak ve önemli risk her seçenekte açıklanır. B rastgele hasara izin değildir; belirsizlik varsa kaynağı ayrıca tanımlanır.

Bağ: Q21,Q11,Q15. Önkoşul: F27.

### F30 — Oyuncunun Will'i kırılınca

Oyuncunun iradesi kırıldığında rakibin önceden açıklanmış talebine nasıl yanıt verebilsin?

A) Yasal talep uygulanır. B) Talebi kabul veya bir son ölümcül direnme seçimi (öneri).

**Neden / sınır:** Geri çekilme/gönüllü teslimiyet isteniyorsa hangi karşılaşmada mümkün olduğunu ekle. Talep ölümden ayrı sonuçtur; rakip sonradan en değerli eşyayı uyduramaz.

Bağ: Q13. Önkoşul: F20,F27.

### F31 — Sonsuz savunmayı bitiren baskı

Oyuncu sürekli savunarak veya pas geçerek neyi riske atsın?

A) Açık sınırlı kaynak/eylem baskısı (öneri). B) Baştan görünür karşılaşma hedefi/deadline. C) Görünür sonlu düşman hazırlığının sonuçlanması.

**Neden / sınır:** A için exact azalan olguyu F59'da hesaplarım; geçici statünün değişmesi tek başına sonlanma kanıtı değildir. B/C yeni davranış olarak açık seçilir.

Bağ: Q14. Önkoşul: F27,F28.

### F32 — Yara ve zaman deneyimi

Kanama ve bakımın baskısı hangi anlarda ilerlesin?

A) Açık tur/olay sınırlarında; okurken durur (öneri). B) Yalnız savaşta belirli sınırda. C) Keşifte de gerçek zaman baskısı.

**Neden / sınır:** A/B için oda geçişi ve savaş başı/sonu tick tablosu gerekir; C okuma ve erişilebilirlik yükünü büyütür. Wounds veya Integrity Echo'yu demodan çıkarmak istersen açıkça belirt.

Bağ: Q05,Q06,Q22. Önkoşul: F10,F27.

### F33 — Ölümden korunma mekaniklerinin demo kapsamı

Panic Pulse ve uzuv feda ederek hayatta kalma bu demoda ne kadar gösterilsin?

A) İkisi de seçilmiş birer dar durumla (önceki yönü koruyan öneri). B) Birini koru; hangisi? C) Demo için açıkça ikisini ertele.

**Neden / sınır:** Dahil edilen mekanikte trigger, kullanım limiti, Torso istisnası ve reset kesinleşir. Kapsam düşürme ana oyundan silme değildir; boss bitişi bu korumaları hesaba katar.

Bağ: Q07,Q22. Önkoşul: F27,F32.

### F34 — Elde görünen kartların temposu

Kart erişimi ne hissettirsin; değiştirme ne zaman mümkün olsun?

A) Elde kalan kartlar + kullanılan/geçersiz yerlerin yenilenmesi (mevcut öneri). B) Bu çerçevede daha küçük ve kolay okunan başlangıç seti. C) Farklı akış önerin.

**Neden / sınır:** Kartlar hâlâ beden ve Concept Deck'e bağlı; Brain fiziksel kaynak yaratmaz. Ücretli redraw istiyor musun belirt. Kesin el/deste/etiket sayıları F59'a devredilebilir.

Bağ: Q09,Q18. Önkoşul: F27.

### F35 — Eşya ve envanter kapsamı

İlk demoda oyuncu kaç tür bakım/eşya kararıyla uğraşsın?

A) Tek anlamlı readied item ve küçük sabit envanter (öneri). B) Birkaç bakım aracı arasında hazırlık seçimi. C) Daha geniş envanter; gereken somut kararları yaz.

**Neden / sınır:** Karşılaşma içinde yeniden hazırlama istiyorsan ayrıca belirt. Otomatik item replacement veya sınırsız envanter erişimi yok; kapasite/stack/discard davranışı içerik tablosunda kapanır.

Bağ: Q10,Q22. Önkoşul: F27,F32.

### F36 — Bakım ve Blood ekonomisi

İki dövüş arasında bakım kararının ağırlığı ne olsun?

A) Sınırlı mevcut imkânlarla Blood'u harcama/koruma tercihi (öneri). B) Güvenli durakta birkaç ayrı tedavi/onarım seçeneği. C) Minimum bakım ve daha çok dövüş.

**Neden / sınır:** Sıradan Blood kazanımı kill yoludur; bedava refill varsayılmaz. Yeni tüccar/oda/ödül kaynağı istiyorsan açık yaz. Her rota masraf/kalabilir seçenek defteriyle kontrol edilir.

Bağ: Q17,Q10,Q22. Önkoşul: F23,F32,F35.

### F37 — Concept ve Brain'i demoda gösterme

Graft'ın yanında kalıcı ilerlemenin hangi kısmını ilk demoda gerçekten kazandırıp kullandıralım?

A) Concept kazanım/kullanımı; Brain'i açık demo kapsamı dışına al (sadelik önerisi). B) İkisini de ayrı, boss zaferine bağlı olmayan onaylı progression fırsatlarıyla. C) İlk demoda ikisinin kazanımını ertele; mevcut beden/kart ilişkisini göster.

**Neden / sınır:** A/C önceki minimum kabulü daraltır, yanıt olmadan uygulanmaz. B yeni sahne veya ödül gerekçesi ister. Ölmek/yeni boss'a kaybetmek otomatik Brain ödülü vermez.

Bağ: Q18,Q19,Q20. Önkoşul: F03,F22.

### F38 — Kart ve tekniklerin içerik yetkisi

Başlangıç Punch/Kick/Headbutt dışındaki somut teknikleri nasıl tamamlayalım?

A) Seçtiğim rollerle sınırlı minimum kart listesini sen yaz (öneri). B) Kart adlarını/etkilerini ben vereceğim. C) Önce kısa alternatif setler sun.

**Neden / sınır:** Her kart için kaynak, target, maliyet, Preparation/Main, interruption, kötü durum ve görünür fark gerekir. A seçimi sayısal dengeyi F59'dan bağımsız otomatik kapatmaz.

Bağ: Q08,Q09,Q10,Q18,Q19,Q22. Önkoşul: F21,F22,F34,F35,F37.

## G — Boss, yenilgi ve hikâye beklentisi

### F39 — Boss'un dünyadaki görevi

Görece güçlü ana-oyun boss'u kimdir ve neden bu zayıf ruhla çatışır?

A) Bir geçişi/kurumu koruyan görevli. B) Bedenleri kendi amacı için toplayan/dönüştüren aktör. C) Mevcut karakterin veya kendi fikrin.

**Neden / sınır:** Öneri: önce rol/motif seç, isim sonra. B beden mekaniğine bağlanabilir; sadece demoyu bitirmek amacı yeterli değildir. Önceki Warden/Jeff otomatik bu boss değildir.

Bağ: Q15,Q28. Önkoşul: F05,F14,F15.

### F40 — Boss'un imza mekaniği

Boss'ta hangi yeni ilişkiyi görmek istiyoruz?

A) Görünür, sonlu rezervlerden kendi bedenini yeniden kurma (başlangıç adayı). B) Önceden işaretlediği bir kaynağı sınırlı süre bastırma. C) Belirli beden eylemini başka görünür sonuca bağlama.

**Neden / sınır:** Üçü de yalnız öneri. Maliyet, karşı hamle, source loss ve istisna tanımlanır; A sonsuz iyileşme, B bütün inputu sebepsiz kapatma, C gizli ceza değildir.

Bağ: Q15,Q25. Önkoşul: F22,F28,F39.

### F41 — Final kaybının kesinliği

Onaylı yenilgi sonunu tüm legal oyunlarda kesin mi yapalım; yoksa nadir bir alternatif sonuç kabul ediyor musun?

A) Görünür nedensel kural ile kesin yenilgi (önceki yönle uyumlu öneri). B) Olağanüstü başarı için sınırlı alternatif final; asıl yön yenilgi.

**Neden / sınır:** A seçilirse kusursuz savunma/assist/survival/source loss sonlanma kanıtına dahil edilir. Boss'un çok güçlü olması kanıt değildir. B ayrıca anlatı/kabul kapsamı ister.

Bağ: Q25. Önkoşul: F30,F33,F40.

### F42 — Kaybederken iyi oyunun karşılığı

Oyuncunun iyi oynaması finalde hangi yerel farkı yaratsın?

A) Boss'un bir işlevini geçici bozabilmek (öneri). B) Bir bilgi/zaafı açığa çıkarmak. C) Kayıp sırasında belli bedensel sonucu korumak/değiştirmek.

**Neden / sınır:** Seçilen fark ana oyuna otomatik save transferi değildir. Hiç fark istemiyorsan bunu belirt; adalet/etki hissi için risk olarak sınanır.

Bağ: Q25,Q28. Önkoşul: F40,F41.

### F43 — Yenilginin somut anlamı ve kapanış

Boss sonunda oyuncuya ne yapıyor; son görüntü/cümle hangi merakı bırakıyor?

A) Bedeni öldürür; ruhun geleceğiyle ilgili seçili ipucu. B) Esir alır veya kullanılamaz hale getirir. C) Kovulma/amaç kaybı gibi farklı yenilgi.

**Neden / sınır:** Ölüm ile esaret aynı kural değildir. İstersen sadece duyguyu ve saklanacak bilgiyi yaz, metni o sınırda ben tasarlarım; yeni kozmolojik gerçek eklemem.

Bağ: Q25,Q28. Önkoşul: F15,F39,F41,F42.

### F44 — Kısa boss ve toplam oturum

Yaklaşık 30 dakika referansını koruyor musun; 'kısa boss' için hangi deneyim yeterli?

A) Birkaç anlamlı yanıt ve yeni kuralın görülmesi; süre gözlemle belirlensin (öneri). B) Tercih ettiğin dakika aralığını yaz. C) Toplam kısa ilk oturum hedefini ayrıca yaz.

**Neden / sınır:** Süre tercihi gizli ölüm sayacı değildir. Okuma/yeni oyuncu süresi ile tekrar denemesi ayrı ölçülür.

Bağ: Q23,Q25,Q22. Önkoşul: F12,F27,F40.

## H — Arayüz, öğretim, ses ve erişim

### F45 — Öğretim biçimi

İlk kararları nasıl öğretelim?

A) İhtiyaç anında kısa ipucu + tekrar açılabilir açıklama (öneri). B) Daha yönlendirilmiş ilk tur. C) Az metin, çevre ve davranış ağırlığı.

**Neden / sınır:** İpucu eylem ödülünü zorla seçmez. Atlamaya/tekrar görmeye izin ve yanlış anlamada verilecek yardım protokolü yazılır.

Bağ: Q21,Q22,Q23. Önkoşul: F12,F17,F27.

### F46 — Dil ve metin sesi

İlk demonun metin dili, terim dili ve anlatım üslubu ne olsun?

A) Türkçe, teknik terimler tutarlı sözlükle (owner testi için öneri). B) İngilizce. C) İki dil.

**Neden / sınır:** Karakterlerin konuşma tonu ve altyazı ihtiyacını belirt. İki dil seçilirse çeviri/QA kapsamı artar; altyapı metinleri yine kimlikle ayırır.

Bağ: Q21,Q22. Önkoşul: F17,F20.

### F47 — Arayüzün his ve yoğunluğu

El/kart, beden, niyet ve kaynak bilgisi nasıl dağılsın?

A) Alt bölüm kartlar, sahnede niyet, açılabilir beden/ayrıntı (öneri). B) Daha sürekli görünür beden paneli. C) Seçtiğin başka düzen veya referans.

**Neden / sınır:** Ekran yerleşimi camera ve hedef cihazla uyarlanır. Ana menü/ayar/pause/yeni deneme/son ekranın içerik taslağı F52 ve teknik ekte eşlenir.

Bağ: Q21,Q22. Önkoşul: F06,F08,F29,F34.

### F48 — Erişim ve rahatsızlık seçenekleri

Metin boyutu, renk dışı işaret, yeniden tuş atama, hareket/sarsıntı, yanıp sönme ve şiddet görünümü için ihtiyaç/sınır var mı?

A) Okunur ölçek, renk dışı işaret, alternatif input, ayarlanabilir ses/hareket; azaltılmış gore gerekirse seçilebilir (öneri). B) Ek kişisel gereksinimleri yaz.

**Neden / sınır:** Redundant cue zaten korunur. Controller, ekran okuyucu veya belirli motor erişilebilirlik özelliği destekleniyor diye varsayılmaz; kapsam/test cihazı gerekir.

Bağ: Q11,Q21,Q22. Önkoşul: F09,F28,F47.

### F49 — Ses, müzik ve seslendirme

İlk demoda hangi ses katmanları gerekli?

A) Ayırt edilebilir eylem/tehdit/sonuç sesleri + sınırlı ambiyans; konuşma metin (öneri). B) Buna müzik. C) Seslendirme de dahil.

**Neden / sınır:** Sesler tek bilgi kanalı olmaz. Satın alma/üretim bütçesi F56'ya bağlıdır; yapay ses veya müzik kullanımı otomatik seçilmez.

Bağ: Q22,Q32. Önkoşul: F09,F20,F46.

## I — Ölüm, kayıt ve son ekran

### F50 — Erken ölüm ve yeniden deneme

İki normal savaşta erken yenilgi/ölüm olursa oyuncu nereye dönsün?

A) Seçilen aynı gün başlangıcına, korunması seçilmiş abstract kazanımlarla (önceki model önerisi). B) Karşılaşma öncesi checkpoint. C) Menüden temiz demo denemesi.

**Neden / sınır:** B/C önceki persistence yönünü demo için değiştirir. Ölüm olmayan claim sonucu farklı olabilir; hangi sonuç tekrar başlatır yazılmalı. Final boss sonu ayrı.

Bağ: Q20,Q04,Q07. Önkoşul: F03,F30,F33,F37.

### F51 — Uygulamayı kapatınca ne kalsın?

Oturum kapanması/kesintisinde neyi saklayalım?

A) Ayarlar; oynanış yeni deneme (küçük özel test için öneri). B) Ayarlar + kazanılmış kalıcı katmanlar. C) Seçilen checkpoint'ten sürdürme de dahil.

**Neden / sınır:** A, oturum içi korunumu yasaklamaz; ürün vaadi açık yazılır. B/C kayıt sınırı, çökme, bozuk kayıt ve eski sürüm davranışı ister; bulut kayıt varsayılmaz.

Bağ: Q20,Q24. Önkoşul: F37,F50.

### F52 — Final ekranından sonraki eylem

Boss yenilgisi ve kapanış sonrası oyuncu ne yapabilsin?

A) Yeniden dene / menü / çıkış (öneri). B) Bunlara gönüllü geri bildirim bağlantısı. C) Kamuya açıksa ana oyun sayfası yönlendirmesi.

**Neden / sınır:** Link/hedef yoksa uydurulmaz; otomatik mesaj/telemetri gönderilmez. Replay final sonunu kaldırmaz veya postgame eklemez.

Bağ: Q20,Q25,Q32. Önkoşul: F43,F50,F51,F54.

### F53 — İki rotanın değerlendirilmesi

Tek oyuncu oturumunda graft alınmadıysa demo testini nasıl yorumlayalım?

A) İlk doğal tercihi kaydet; ayrı denemede diğer rotayı değerlendir (öneri). B) Graft rotasına isteğe bağlı ikinci deneme öner.

**Neden / sınır:** No-graft teknik olarak geçerli, fakat graft deneyimi o oturumda gözlenmemiş sayılır. Aynı kişinin ikinci denemesi yeni oyuncu ilk izlenimi değildir.

Bağ: Q17,Q23. Önkoşul: F25,F26,F50.

## J — İlk sürümün kapsamı ve üretim koşulları

### F54 — İlk teslim ve çevrimiçi kapsam

İlk demo kime, nereden ve hangi cihaz ailesinde ulaşacak?

A) Windows PC'de sahibi/arkadaşları için özel, yerel örnek (mevcut kapsam önerisi). B) Herkese açık indirilebilir PC demosu. C) Başka hedefi yaz.

**Neden / sınır:** Tek oyunculu oyun yönü yeniden sorulmuyor; çok oyunculu/hesap/servis isteği varsa açık kapsam değişikliğidir. B yayın, mağaza ve lisans kontrolleri ekler.

Bağ: Q24,Q32. Önkoşul: F01.

### F55 — Gerçek cihaz ve girdi sınırı

Test bilgisayarı GPU/CPU/RAM/işletim sistemi, ekran çözünürlüğü ve gerekli mouse/klavye/controller desteğini biliyorsan yaz.

Bilmiyorsan DONANIMI İNCELE yaz; salt okunur yerel inceleme yaparım. Öneri: ilk ölçüm mevcut Windows PC ve mouse/klavye; controller ayrı açık seçim.

**Neden / sınır:** Hedef performans/ekran oranı F59 teknik ölçüm tablosuna konur; başka oyuncuların cihazları senin cihazından çıkarılmaz.

Bağ: Q24,Q21,Q32. Önkoşul: F06,F10,F54.

### F56 — Görsel kalite ve asset kaynağı

İlk test için kabul edeceğin görsel kalite, sahip olunan assetler ve harcama tavanı nedir?

A) Tutarlı sade geçici modeller/UI; okunurluk öncelikli (öneri). B) Hazır lisanslı assetler ve seçili özgün parçalar. C) Büyük ölçüde özgün içerik.

**Neden / sınır:** Bütçeyi miktar/para birimiyle veya 'ücretli asset yok' diye yaz. Üretken görsel/ses, dış sanatçı ve satın alma ayrı tercihtir; A final kalite vaadi değildir.

Bağ: Q22,Q24,Q32. Önkoşul: F07,F09,F49,F54.

### F57 — Zaman, iş gücü ve araç kısıtları

Haftalık ayırabileceğin süre, hedef tarih, bütçe ve bildiğin/istemediğin araçlar nedir?

Unity önceki tercih hipotezi olarak duruyor. Motor teknik karşılaştırmasını kamera/asset/build kapsamına göre benim yapmamı veya zorunlu aracını belirt.

**Neden / sınır:** Lisans/sürüm/kurulum doğrulanmadan kesin maliyet sözü verilmez. Tarih yoksa 'hedef tarih yok' geçerli yanıttır; iş süresi uydurulmaz.

Bağ: Q24,Q32. Önkoşul: F54,F56.

### F58 — İnsan testi ve revizyon kararı

Kimlerle test edebiliriz, kaç kişi erişilebilir, hangi sonuçta revize ederiz?

A) Önce owner, ardından az sayıda hedef profile yakın gönüllü arkadaş; nitel gözlem (öneri). B) Belirttiğin daha sistemli grup.

**Neden / sınır:** Katılımcı sayısı/ilişki/ön bilgi/yardım sınırı ve kayıt izni belirtilir. Anlama, normal savaş ilgisi, boss adaleti ve merak ayrı incelenir; küçük örnek pazar kanıtı değildir.

Bağ: Q23,Q32. Önkoşul: F01,F27,F44,F53,F54.

## K — Bilmediğin detayları nasıl kapatacağız?

### F59 — Sayısal kurallar ve içerik ayrıntıları

Seçtiğin deneyime uyan exact ilk-test değerlerini ve içerik tablolarını benim tamamlamamı ister misin?

A) SEN SEÇ: seçilmiş sınırlar içinde geçici test setini hesapla, dosyala ve karşı örnekleri denetle (öneri). B) ÖNER: değer/alternatif paketini getir, ben seçeceğim. C) Kendi değerlerimi vereceğim.

**Neden / sınır:** A final balance iddiası değildir; gameplay değerlerinin seçimi için açık yetki olur. Yeni kaynak/kural/kimlik ekleme yetkisi değildir. Eksik tercih için sessiz varsayım yapılmaz.

Bağ: Q04,Q05,Q06,Q07,Q08,Q09,Q10,Q11,Q12,Q14,Q15,Q16,Q17,Q18,Q19,Q24. Önkoşul: Yok; değerlerin üretimi ilgili deneyim cevaplarına bağlı.

### F60 — Cevabı olmayan tasarım tercihleri ve kırmızı çizgiler

Bilmediğin soruları nasıl ele alalım; önerilerimin asla değiştirmemesi gereken sınırların neler?

Soru bazında ÖNER, KARŞILAŞTIR veya SEN SEÇ kullan. İstersen belirli F aralıklarına ortak yöntem ver; istisnaları yaz.

**Neden / sınır:** SEN SEÇ gerçekten kapsamlı karar yetkisidir; aynı kararı tekrar onaylatmam. ÖNER/KARŞILAŞTIR ise karar değildir. Boş bırakılan cevap OPEN kalır.

Bağ: Q29,Q30,Q31,Q32. Önkoşul: Yok.

## Teknik ek — müşteri tasarım tercihi olmayan kararlar

Aşağıdakiler bu talepteki “şimdilik dosyala” yetkisiyle **TEKNİK KARAR — DOSYALANDI**.
Henüz kod, asset, engine veya kurulum değildir. Motor bağımsız, geri alınabilir uygulama
sözleşmeleridir. Hasar, can, süre, kamera, kayıt kapsamı ve içerik sayısı bu kategoriye
sokulmadı; bunlar deneyimi değiştirir.

| ID | Dosyalanan karar | Neden / uygulama ve kontrol sınırı | İlgili işler |
|---|---|---|---|
| TD01 | Yeni demo legacy simülatörden ayrı ürün dizininde kurulacak; planlanan kök `demo/` | Şimdilik dizin oluşturulmaz. Legacy src/config/tests içerikleri taşınmaz veya oyuna kopyalanmaz | T09,T10 |
| TD02 | Kurallar/durum, içerik tanımları, giriş/sunum ve kayıt adaptörleri ayrı sorumluluklar | Motor UI'si hasar/ödül hesaplamaz; framework büyütmeden tek dilimde gereken dosyalar açılır | T10-T20 |
| TD03 | İçerik kaynak biçimi sürümlü UTF-8 JSON; değişmez ASCII kimlikler | İsim/çeviri kimliği değiştirmez. Motor farklı yükleme biçimi isterse dönüştürücü teknik revizyonla eklenir; gameplay değişmez | T13,T15-T19 |
| TD04 | Tek combat komut işleme noktası; source/target/cost ön kontrolü ve atomik commit | Çift tıklama aynı eylemi iki kez ödemez. Başlamış eylem tamamlanır; sonraki illegal eylem reddedilir. İade/turn kuralı Q08'den gelir | T12-T16 |
| TD05 | Rastlantı varsa tek enjekte edilen seed/kayıtlı RNG akışı | Hangi olgunun rastgele olacağı Q09/ilgili içerikten gelir; teknik RNG eklenmesi yeni ihtimal yaratmaz | T13,T15,T19 |
| TD06 | Oyun mantığı olay/tur saati ile sunum/input saati ayrı | Pause, wound ve savunma saatinin player-facing davranışı F28/F32 ile seçilir; render frame sayısı kural saati değildir | T10,T12,T14 |
| TD07 | Durum geçişi tek isimli olay ve önce/sonra özeti üretir | Fixture/build/seed/input ile yeniden üretilebilir hata kaydı; gizli analitik servisi veya otomatik gönderim yok | T10-T21 |
| TD08 | Geçersiz içerik yüklemede kimlik/alan hatası; geçersiz oyuncu eyleminde mutation yok ve açıklama var | Eksik donor/source yerine otomatik başka nesne konmaz; geliştirici assert'i kullanıcıya çökme yolu yapılmaz | T12-T19 |
| TD09 | Graft ve reward için tek sonuç/işlem kimliği | Bir NPC aynı denemede hem kill-Blood hem living-limb vermez; table yarım aktarım bırakmaz | T15,T16 |
| TD10 | Gösterim metni kimlikli sözlükte; input eylem adından bağlanır | Dil ve tuş seçimi değişebilir; yeniden tuş atama/alternatif input seçilen kapsamda test edilir | T11-T21 |
| TD11 | Ayar/oyun kayıtları kapsamına göre sürümlü, atomik dosya değiştirme ve eski-kayıt denetimi | Yalnız F51'de saklanması seçilen alanlar tutulur; bozuk dosyada korunmuş yedek/okunur uyarı, sessiz veri silme yok | T20 |
| TD12 | Asset kayıt defteri: kaynak, lisans/izin, sürüm, kullanım, üretim yöntemi | Satın alma, dış üretim veya generated asset seçimi F56'dan gelir; placeholder final içerik sayılmaz | T08,T10,T21 |
| TD13 | Doğrulama katmanları: saf kural → geçiş entegrasyonu → gerçek input/build → insan gözlemi | Sadece ilgili katman kanıtlanır; legacy test geçişi demo kabulü sayılmaz | T10-T21 |
| TD14 | İçerik değiştirme sınırı: önce küçük veri değişikliği, sonra gerekirse primitive incelemesi | Var olmayan genel crafting/dialogue/economy framework'ü kurulmaz; boss'un yeni davranışı seçili kaynak sözleşmesiyle sınırlı | T15-T19 |
| TD15 | Teknik araç seçimi sırası: cihaz/ekip kısıtı → kamera/asset ihtiyaçları → sürüm/lisans kontrolü → küçük build/input denemesi | Unity önceki aday olarak değerlendirilir; motor, plugin, LFS veya ücretli araç kurulmadı. Deneme için ayrıca mevcut runtime gate gerekir | T09,T10 |

### Doldurulacak kesin içerik ve sayı tabloları

Bu alanlar boş tasarım bırakmak için değil, kullanıcıyı teknik formül yazmaya zorlamadan
uygulamaya girecek sözleşmeyi tanımlamak içindir. Sahibi **ajan**, deneyim sınırı **ilgili
F yanıtı**; gameplay değeri seçme yetkisi **F59=A veya açık soru-bazlı yetki**.
Yetki yoksa tablo aday olarak sunulur; onaylı sayılmaz. Mevcut DWF/WNR sayıları yalnız
aday başlangıçtır, otomatik üretim ayarı değildir.

| Tablo | Üretilecek tam alanlar | Kaynak karar | Olumlu / olumsuz kontrol |
|---|---|---|---|
| P01 Başlangıç ve beden | Altı slot, source profili, bütünlük max/eşik, Blood başlangıç/cap, wound, inventory, ilk legal eylem | Q04,Q06; F13,F16 | İlk savaşa legal devam; missing source'tan action yok |
| P02 Wound/tedavi/ölüm | Etki, tick saati ve sırası, pause/traversal/encounter sınırları, tekrar/üstünlük, tedavi/onarım ayrımı | Q05-Q07; F32,F33 | Tick iki kez çalışmaz; treatment Blood/Integrity doldurmaz |
| P03 Tur ve savunma | Lead/sıra, Preparation/Main, interception, rezervasyon/iade, source loss, defense cue/lock/window/assist, focus loss | Q08,Q11; F27-F29 | Atomik eylem, erken/geç/yanlış/no-input; frame/pause farkı |
| P04 Will ve NPC sonucu | Değer/recovery, goal/claim/leverage, surrender/Defy/fallback, escape sınırı | Q12,Q13,Q15; F18-F21,F30 | Broken tek başına donor transferi yaratmaz; ölü donor yok |
| P05 Sonlanma | Geri kazanılamayan sonlu olgu, kaynak alt sınırı, cycle/recovery koşulları | Q14,Q25; F31,F41 | Perfect defense/pass/redraw/heal ve no-input sonsuz çevrimleri |
| P06 Kart/Attention/Item | Exact source/condition/target/labels, cost/timing/intercept/effect; deck/hand/weights/redraw; refill/Spent/Invalid/Dormant; item capacity/stack/uses/readiness/drop | Q08-Q10; F21,F34,F35,F38 | Boş/uyumsuz el, duplicate, inventory bypass ve hayali source yok |
| P07 Aktör ve içerik | Oyuncu/iki NPC/boss anatomy; aktör Goal/Need/Want/RedLine/Claim/Fallback; action listesi ve kısa metinler | Q15,Q28; F16,F18-F22,F39 | Asimetrik üstünlük gerçek kayıp işlevle sınırlı; irade ve fizik ayrı |
| P08 Graft ve rota ekonomisi | Donor asimetrik; slot/eski/yeni işlev, non-card fark, drawback, Table cost/işlem/recipient/donor wound, kill yield/collection/cap; route ledger | Q16,Q17,Q26; F12,F22-F26,F36 | Graft/no-graft doğal prefix; yetersiz Blood/ruined source/tekrar transfer |
| P09 Kalıcı katman | Dahilse achievement, Concept remove/add/equip ve Brain effect/nerf, award/duplicate/edit/save boundary | Q18-Q20; F37,F50,F51 | Doğal award/use; uyumsuz beden Dormant; death reward yok |
| P10 Boss ve final | Yeni kural source/tell/cost/yanıt/exception, evre, local success, exact defeat ve survival önceliği, kapanış/replay geçişi | Q15,Q25,Q28; F39-F44,F52 | Assist, source ruin, claim, çift terminal, beklenmeyen kazanma durumu |
| P11 Sahne/UI/ses | Scene akışı, traversal giriş/çıkış, beden/intent/hand/info yüzeyleri, menü/ayar/pause/kayıt/son ekran, cues/metin/animation/SFX listesi | Q21,Q22,Q30-Q32; F06-F11,F45-F49 | Hedef örtülmesi, kamera çarpışması, softlock, okunmayan maliyet, yalnız renk/ses bilgisi |
| P12 Build/test | Cihaz/OS/input/window, hedef performans ve yükleme sınırı, sürüm/hash, test fixture/seed, katılımcı/protokol/yardım/kriter, asset izinleri | Q23,Q24,Q32; F54-F58 | Temiz açılış, resize/focus loss, restart/corrupt save, düşük performansta defense davranışı |

### İçerik envanteri nasıl kapanacak?

Her sahne/varlık için şu alanlar doldurulur:
`kimlik / oyuncuya işlev / gerekli F-Q-R / giriş-çıkış / gereken görsel-ses-metin /
veri kuralı / dahil-hariç / placeholder-final sınırı / doğrulama / sorumlu`.

Sahne rolleri: seçili açılış, iki normal NPC, seçili graft masası/deneme fırsatı,
boss ve kapanış; ayrıca oyuncuya gereken menü/ayar/pause/yeniden deneme yüzeyleri.
Bunlar ayrı oda sayısı değildir. Aynı sahne birden fazla rol taşıyabilir.
Ek keşif, ödül, anlatı, hazard veya puzzle istenirse F04/F10/F14 altında adı ve kanıtı
seçilir; varsayılan tüccar, servis, envanter ekranı veya save sistemi eklenmez.

## Kapsama matrisi ve görev sırası

Yeni ön görev [T00](tickets/T00.md), genel tasarımın demo için bağlayıcı asgari kısmını
çözer. Sonra mevcut T01-T09 karar/fixture işleri ve yalnız izinli durumda T10-T21
uygulama dilimleri gelir. Paper taslaklar paralel olgunlaşabilir; kapanış bağımlılıkları
atlamaz. Tek dosya cevapları, aşağıdaki sorumlu belgelere dağıtılır.

| Q grubu | F kapsamı | Yaşayan kaynak / iş |
|---|---|---|
| Q01-Q02 | Bilinen iki NPC ve boss yeniliği; tekrar soru yok | Director, World / T01 |
| Q03-Q04 | F13,F16,F50,F59 | Core, Combat / T02,T03 |
| Q05-Q07 | F32,F33,F50,F59 | Combat / T03 |
| Q08-Q10 | F28,F34,F35,F38,F59 | Deck, Core / T04 |
| Q11-Q14 | F27-F32,F59 | Combat, Core / T05 |
| Q15-Q17 | F18-F26,F36,F39-F43,F59 | Core, Combat, World / T06 |
| Q18-Q20 | F03,F34,F37,F38,F50-F52,F59 | Deck, Core / T07 |
| Q21-Q22 | F06-F11,F28-F29,F32-F38,F44-F49,F56 | Director, Core, World / T08 |
| Q23-Q24 | F01,F25-F27,F44,F53-F59 | Director, World / T08,T09 |
| Q25-Q28 | F12-F20,F22-F26,F39-F44,F50-F52 | Core, World / T01,T02,T06 |
| Q29 Genel oyun asgari taahhüdü | F01-F05,F60 | Director, Core, World / T00 |
| Q30 Kamera ve görsel üretim | F06-F09,F11,F60 | Director, World / T00,T08 |
| Q31 Dünya bağlantısı ve traversal | F04,F10,F60 | Core, World / T00,T02 |
| Q32 İlk teslim/sunum/üretim sınırı | F49,F52,F54-F58,F60 | Director, World / T00,T08,T09 |

Öncelik değişikliği: önce kamera/dünya/ürün sınırı, sonra exact savaş içeriği. Genel
oyunun tüm run/harita tasarımını bitirmek ilk demo önkoşulu değildir; demodaki ölüm,
ilerleme ve vaatle çelişmeyen asgari çerçeve yeterlidir.

## D0 kapanış ve sonraki işlem

- Gerekli her F için seçilmiş/bağlı yetkiyle kararlaştırılmış/owner tarafından kapsam dışı
  durum vardır. ÖNER ve cevapsız zorunlu soru kapanış değildir.
- P01-P12'nin seçilen kapsamına uygulanabilir exact tabloları, iki doğal rota ve final
  negatif örnekleri vardır. Sadece tablo başlıkları uygulama girdisi sayılmaz.
- R01-R16 kabulü ve T00-T21 bağımlılıkları yeni kararlara uyarlanmıştır.
- Gerekli cihaz/araç araştırması ayrıca doğrulanır. İş gücü/bütçe belli değilse kesin
  teslim tarihi çıkarılmaz.
- Demo uygulama kapısı ancak açık kullanıcı talebiyle açılır. Bu belgeyi cevaplamak
  veya teknik ekteki seçimler engine kurma izni değildir.
- Final eğlence, adalet, erişilebilirlik ve beklenti insan testinde sınanır. İlk cevap
  mesajından sonra kalan deneysel belirsizlikler kapatılmış gibi yazılmaz.

Kapsam dışı kalan genel oyun ayrıntıları: bütün kampanya haritası, tüm boss/uzuv/kart
kataloğu, final lore çözümü, uzun vadeli güç eğrisi, ticari fiyat, bütün platformlar.
Bunlardan biri demo kararıyla gerçekten çelişirse yalnız gerekli parçası yeniden açılır.

## Tek sonraki mesaj için cevap formu

Tüm belgeyi tekrar göndermen gerekmez. Aşağıdaki formu doldur veya yalnız F kimliklerini
yaz. Bölüm/soru aralığına ortak yöntem verebilirsin; bireysel cevap ortak yöntemi ezer.
Örnek: `F06=B; F12=A; F18-F21=SEN SEÇ, NPC'ler sırf kötü oldukları için savaşmasın;
F40=KARŞILAŞTIR, kaybetsem de etkimi görmek istiyorum; F59=A`.
Bu yalnız kullanım örneğidir; cevap olarak kaydedilmez.

```text
Ortak yöntem (boş bırakılanlar OPEN kalır):
Değişmez sınırlarım:
F01 — Kimin için tasarlıyoruz?:
F02 — Öncelik ve vazgeçilmeyecek his:
F03 — Genel oyunun oturum omurgası:
F04 — Genel dünya bağlantısı:
F05 — Ana oyuna verilen sözün sınırı:
F06 — Bakış açısı:
F07 — Görsel üretim biçimi:
F08 — Kendi bedenini ve uzuv değişimini görme:
F09 — Görsel ton ve rahatsızlık sınırı:
F10 — Dünya içindeki hareket:
F11 — Dövüşte kamera ve geçiş:
F12 — Asimetrik donorun sırası:
F13 — Guard ve eski şehir açılışı:
F14 — Oyuncunun hemen şimdi amacı:
F15 — Ruh ve beden ilişkisi:
F16 — Başlangıç karakteri ve bedeni:
F17 — İlk sahnede bilgi miktarı:
F18 — İnsan NPC'nin nedeni:
F19 — Asimetrik NPC'nin bedeni ve nedeni:
F20 — NPC iradesi ve konuşma yoğunluğu:
F21 — Normal düşmanların farkı:
F22 — Uzuvla hangi davranış değişsin?:
F23 — Yeni uzvun bedeli:
F24 — Transferin sunumu ve konumu:
F25 — Graft almayan oyuncu:
F26 — Graft'ı fiilen deneme anı:
F27 — Zorluk ve öğrenme temposu:
F28 — Savunma girişi ve yardım:
F29 — Oyuncuya gösterilen kesinlik:
F30 — Oyuncunun Will'i kırılınca:
F31 — Sonsuz savunmayı bitiren baskı:
F32 — Yara ve zaman deneyimi:
F33 — Ölümden korunma mekaniklerinin demo kapsamı:
F34 — Elde görünen kartların temposu:
F35 — Eşya ve envanter kapsamı:
F36 — Bakım ve Blood ekonomisi:
F37 — Concept ve Brain'i demoda gösterme:
F38 — Kart ve tekniklerin içerik yetkisi:
F39 — Boss'un dünyadaki görevi:
F40 — Boss'un imza mekaniği:
F41 — Final kaybının kesinliği:
F42 — Kaybederken iyi oyunun karşılığı:
F43 — Yenilginin somut anlamı ve kapanış:
F44 — Kısa boss ve toplam oturum:
F45 — Öğretim biçimi:
F46 — Dil ve metin sesi:
F47 — Arayüzün his ve yoğunluğu:
F48 — Erişim ve rahatsızlık seçenekleri:
F49 — Ses, müzik ve seslendirme:
F50 — Erken ölüm ve yeniden deneme:
F51 — Uygulamayı kapatınca ne kalsın?:
F52 — Final ekranından sonraki eylem:
F53 — İki rotanın değerlendirilmesi:
F54 — İlk teslim ve çevrimiçi kapsam:
F55 — Gerçek cihaz ve girdi sınırı:
F56 — Görsel kalite ve asset kaynağı:
F57 — Zaman, iş gücü ve araç kısıtları:
F58 — İnsan testi ve revizyon kararı:
F59 — Sayısal kurallar ve içerik ayrıntıları:
F60 — Cevabı olmayan tasarım tercihleri ve kırmızı çizgiler:
```

## Dayanak ve sınırlar

Yetki: son owner mesajları ve
[Director](../GAME_DIRECTOR_BRIEF.md),
[Core](../CORE_LOOP_ENCOUNTER_AND_RUN.md),
[Combat](../COMBAT_BODY_AND_BLOOD.md),
[Deck](../DECK_BRAIN_AND_ACTIONS.md),
[World](../WORLD_PROGRESSION_AND_DECISIONS.md).
Koordinasyon: [ana plan](D0_EXECUTION_PLAN_2026-09-06.md),
[çalışma sözleşmesi](../DEMO_MINIGAME_AI_WORKING_CONTRACT.md).

Üretim, grill-me, to-spec ve to-tickets rollerinin çıktıları bu dosyada soru/bağımlılık,
nedensel karşı örnek, kabul ve görev eşlemesi olarak kullanıldı. Kullanıcının açık toplu
soru-belgesi isteği nedeniyle küçük mülakat turları yerine tüm dallar birlikte verildi.
[MDA](https://www.cs.northwestern.edu/~hunicke/MDA.pdf) mekanik→davranış→deneyim
ayrımına yöntem dayanağıdır; önerilen kamera/sıra/boss'un üstünlüğünü kanıtlamaz.
[Tespit ve araştırma sınırları](../../research/skill_audit_2026-09-06.md) önceki kaynak
incelemesini içerir. Bu paket klinik/psikometrik olarak doğrulanmış bir müşteri anketi
veya bilimsel optimum tasarım algoritması değildir; izlenebilir üretim karar yöntemidir.

## Belge doğrulama kaydı — 2026-09-07

Plan doğrulayıcısı exit 0: 8 yerel skill metadata, 22 ticket, 32 Q, 16 R kapsamı;
ticket bağımlılık döngüsü/eksik kimlik yok; 210 yerel bağlantı/38 Markdown kontrolü.
60 soru kimliği benzersiz; belirtilmiş F önkoşullarında döngü veya eksik soru yok.
Q01/Q02 zaten kararlı; kalan Q03-Q32 soru kartlarıyla eşleniyor. Whitespace denetimi
exit 0. Bunlar belge yapısı kontrolleridir; gerçek oyun, denge veya müşteri deneyimi
doğrulaması değildir. TD kayıtları dosyalandı, P tablolarının gameplay değerleri henüz seçilmedi.
