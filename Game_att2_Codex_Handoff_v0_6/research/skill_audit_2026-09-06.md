# Skill ve D0 plan denetimi — 2026-09-06

**PAPER ONLY.** İncelenen başlangıç: `2e82194c02b616965accc1197742b411f8604917`.
Çalışma dalı: `codex/skill-audit-d0-plan-20260906`. Yeni Underground City runtime
dosyası veya engine projesi saptanmadı; Python/H1/lab ayrı legacy/research yüzeyidir.
Bu sonuç gameplay doğrulaması veya projenin tamamlanma yüzdesi değildir.

## Kapsam ve yöntem

Kök/paket AGENTS, AI çalışma sözleşmesi, README haritaları, beş yaşayan belge,
proje skill'i ve plugin-routing, yerel frontend/debug/Playwright skill'leri,
Claude grill-me/grilling/to-spec/to-tickets/setup dosyaları incelendi.
DWF araştırmasının kaynak tablosu ve model giriş/çıkışı; kart guardrail haritası ve
Brain yöntem notu değerlendirildi. Tüm legacy kod için güvenlik veya regresyon taraması
yapılmadı; tüm tarihsel kaynakların doğruluğu yeniden belgelendi iddiası yoktur.

Tasarım rolü deneyim bağlantısını, sistem rolü state/ekonomi karşı örneklerini, UX rolü
okunurluk ve input sınırını, araştırma rolü iddia-kaynak bağını, üretim rolü karar/görev
bağımlılığını inceledi. Ayrıca ayrı bir ajan yaşayan belgeleri salt okunur olarak
inceledi ve revize skill'i üç senaryoda davranış açısından yürüttü. Bu LLM
incelemesi insan playtest'i veya kapsamlı bağımsız kalite sertifikası değildir.

## Kritik skill bulguları ve uygulanan düzeltmeler

Öncelik burada görev üzerindeki etkiyi belirtir; güvenlik açığı sınıflandırması değildir.

| Bulgu | Somut önceki kanıt | Nedensel risk | Değişiklik / kalan sınır |
|---|---|---|---|
| P1 — yanlış kaynak önceliği | Production skill Establish authority önce Development Master/Combat Rules zincirini herkese uyguluyordu | Yeni kart/dövüş tasarımı legacy YAML'la geriye çevrilebilir | Aktif demo ile simulator bakımını ayrı otorite tablosuna ayırdım |
| P1 — eski ürün hedefi | Skill gate listesi Guard spike ardından Merchant/Exit Keeper kapsamına odaklıydı; güncel ledger A/B/graft/boss/reset ister | Tek oda sonucu bütün demo diye kabul edilebilir veya gerekli boss downstream sanılabilir | Gate durumunu living ledger'dan okutan yönlendirme; D1 ile tüm sample ayrımı |
| P1 — gereksiz koruma kapatma | Playwright preconditions/troubleshooting danger-full-access öneriyordu | Eksik araç, yetkisiz global değişim ve yeni web scaffold'a dönüşebilir | Bu talimat kaldırıldı; gerçek araçları kullanma ve unavailable check'i raporlama |
| P1 — erken ready/publish | Claude to-spec/to-tickets ready-for-agent ve tracker kurulum varsayıyordu | OPEN ürün kararı implementation izni gibi işlenebilir | Yerel uyarlamalar: blocked-owner/dependency, explicit gate ve local-first çıktı |
| P2 — bağımlı interview yükü | Claude wrapper Skill tool ister; grilling tüm frontier'ı tek tur ister | Çalışmayan tool veya aşırı soru yükü; bağımlı kararlar erken sorulabilir | Self-contained grill-me, küçük bağımsız tur, tool yoksa düz soru, yanıtsız OPEN |
| P2 — bilimsel görünümlü fakat işlemsiz yöntem | Eski skill'de genel evidence card vardı; karar→test→ticket kapanışı yoktu | Kaynak göstermek, ölçülebilir yanlışlanabilirlik yerine geçer | Kaynak kapsamı, sensitivity, counterexample, test sınıfı ve reopen trigger referansları |
| P2 — liveness boşluğu | “State changes” tek başına sonsuzluğu dışlamıyor | Evade/pass veya refill döngüsü aynı duruma dönebilir | Safety/reachability/liveness ayrımı, finite irreversible fact ve döngü örnekleri |
| P2 — frontend genellemesi | Kırık accessibility-checklist yolu; kaynaklandırılmamış “3x”; prototype→production varsayımı | Web best practice native demo kapsamını ve doğruluk iddiasını şişirir | Kırık link düzeltildi; desteklenmeyen oran/genel hukuk iddiası kaldırıldı; platform sınırı eklendi |
| P2 — skill keşfinde popülerlik | Vercel finder popularity/star eşikleri öneriyor | İndirme sayısı görev uyumu veya izin güvenilirliği sayılabilir | Bağımsız proje uyarlaması: içerik/prerequisite/side effect/license denetimi; toplu global kurulum yok |

Debug-interactive-demo'nun gerçek start/input/retry/no-input doğrulaması yararlı;
aktif web artifact yokken çağrılması gerekmiyor. Web için mobile viewport, DOM ve
React örnekleri native Unity gereksinimi haline getirilmedi. Harici upstream dosyalar
değiştirilmedi; proje içinde mevcut kopyalara kapsam düzeltmesi yapıldı.

Production skill artık tarihli gate sonuçlarını yeniden otorite olarak depolamıyor.
İki koşullu referans ayrıntıyı ihtiyaç anında yüklüyor. Bu “maksimizasyon” sözcük sayısını
artırmak değil, karar hatasını azaltacak özgül talimatlar üretmek olarak uygulandı.

## Projede kalan en önemli tasarım boşlukları

1. **G1 yalnız release anını sınar.** Mevcut model, önceden verilen attack/defense
   sayılarıyla released state predicate'ini hesaplar; wound tick sonrası Fight A'ya
   geçiş veya gerçek deck erişimi türetmez. Q03-Q07/Q17 bunun için ayrı yol defteri ister.
2. **Anti-stall henüz exact mechanic değil.** Başarılı Evade, free pass, Spent/refill,
   heal ve geçersiz claim aynı tam state'i döndürebilir. Q14 owner fixture'ı seçilmeden
   tur limiti icat edilemez. Will'in azalmış olması sözleşmedeki finite fact listesini
   otomatik değiştirmez.
3. **Brain ödülü terminal endpoint'e çarpabilir.** Boss/progression kaynağı onaylı;
   son boss sonrası equip/replay/death kanıt yolu açık. Q19-Q20 çözülmeden kalıcılık
   sadece state injection ile gösterilemez.
4. **Graft ile boss iki rotası beraber seçilmeli.** Uzuv, drawback, Blood yield/cap,
   treatment ve downstream maliyet ayrı seçilirse surrendered limb domine eder veya
   graft zorunlu anahtar olur. Q15-Q17 aynı paketle bağlanır.
5. **Geçersiz surrender ve terminal sıra tanımsız kalabilir.** Dead donor, unavailable
   limb, lost credible threat, player Broken, paid action Blood-0 ve Ruined Torso
   farklı sonuçlar doğurabilir. Q07-Q08/Q12-Q13 exact event/fallback ister.
6. **Tek/iki fight kanıt tercihidir.** İki fight öğrenmeyi boss değerlendirmesinden
   ayırabilir; süre/maliyet yükü vardır. Tek fight seçilirse öğretim karışması dürüstçe
   raporlanır. Bu bir bilimsel zorunluluk değil, owner'ın tradeoff kararıdır.

Bu açıklar skill düzeltmesiyle “çözülmüş” sayılmadı.
[24 karar, 13 kabul satırı ve 21 görev](../docs/planning/D0_EXECUTION_PLAN_2026-09-06.md)
bunları sahiplerine ve kapılarına bağlar.

## Harici skill / eklenti kararı ve köken

Dört yeni proje skill'i: grill-me, to-spec, to-tickets, find-skills.
İlk üçü makinedeki Claude örneklerinden iş akışı esinlenerek Codex/proje için yeniden
yazıldı; Claude Skill tool, wizard, otomatik yayın ve hazır iş etiketi taşınmadı.
Finder'ın önceki Claude kopyası taranan yerel skill dizinlerinde bulunamadı; bunun aynı
dosya olduğu iddia edilmedi. Vercel upstream finder incelenip bağımsız uyarlama yazıldı.

Kaynaklar: [Matt Pocock skills](https://github.com/mattpocock/skills),
[MIT lisansı](https://github.com/mattpocock/skills/blob/main/LICENSE),
[Vercel find-skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills),
[Vercel MIT lisansı](https://github.com/vercel-labs/skills/blob/main/LICENSE).
Erişim 2026-09-06; upstream commit kimliği sabitlenmedi. Yeni dosyalar upstream snapshot
veya otomatik güncellenen kopya değildir. Kaynak/esinlenme bağlantıları skill'lerde var;
uzun upstream metin veya executable installer kopyalanmadı.

İncelenen yerel orijinallerin SHA256 kimlikleri:

| Claude dosyası | SHA256 |
|---|---|
| grilling/SKILL.md | C00A8CC786D3349D45F5D986F563383F874658E218BACE610E32EDC417F735F5 |
| to-spec/SKILL.md | 3868F99EB2ACC817DA8917B66B624844868D69D952201CEA9836A1BBAF46B9B7 |
| to-tickets/SKILL.md | E2BF71F57A55F3214C4B46DEE0728A8760E809DCC044F56CC7FB5186EC01768B |

Yeni skill dosyaları oluşturuldu, okundu ve bu görevde doğrudan kullanıldı. Sonraki tur
otomatik katalog keşfi ayrıca sınanmadı; yeni skill'ler sonraki turda kullanılabilir.
Bu ifade çalışan bir Claude/Codex cross-tool entegrasyonu iddiası değildir.

Ayrı hesap eklentisi kurulmadı: bu istekte eksik harici veri/iş takip kapasitesi yok.
Linear/Asana/Drive/Figma vb. hesap eklemek karar boşluklarını kapatmaz. Public web ile
birincil metodoloji ve skill kaynakları okundu; repository, katılımcı kaydı veya owner
tasarım metni dış servise yüklenmedi. Remote issue/PR/mesaj/yayın yapılmadı.

## Referans temeli ve sınırı

- [MDA](https://www.cs.northwestern.edu/~hunicke/MDA.pdf): mekanik, davranış ve deneyim
  ilişkisinin çift yönden incelenmesi. Buradaki limb→plan→yeniden kurma zinciri bizim
  projeye uygulamamızdır; MDA doğru Blood maliyetini veya eğlenceyi kanıtlamaz.
- [NIST combinatorial testing](https://csrc.nist.gov/pubs/book/2013/06/introduction-to-combinatorial-testing/final):
  faktör etkileşimlerini görünür coverage ile sınama. Exact source/exchange kritik
  örnekleri + sıradan pairwise + riskli triples önerisi proje stratejisidir.
- [XAG 107](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/107):
  remapping yanında input hızı/karmaşıklığı ve alternatifler. Projenin erişilebilir
  olduğuna veya ±90 ms'nin doğru olduğuna kanıt değildir.
- [XAG 116](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/116):
  çekirdek gameplay dışı UI zaman sınırları. Eski DWF kaynak tablosundaki genel
  “timing guidance” aktarımı geniş yorumlanmamalı; bu kaynak Parry penceresi türetmez.
  Araştırma yöntemi referansında bu sınır açıklaştırıldı; DWF sayıları değiştirilmedi.
- [Unity zaman yönetimi](https://docs.unity3d.com/6000.0/Documentation/Manual/time-handling-variations.html):
  frame ve fixed simulation zamanının farklılığı. Önerimiz replayable rule event'lerini
  sunum/input zamanından ayırmaktır; FixedUpdate determinism garantisi değildir.
- [Unity Personal](https://unity.com/products/unity-personal): mevcut ürün/lisans
  bilgisi resmi kaynakta bulunur. Bu denetim owner eligibility veya kurulum onayı
  vermez; sürüm/koşul T09'da yeniden doğrulanır.

Creative constraint matrix (source × consequence × lost alternative × later pressure)
ve risk/bağımlılık frontier'ı bu çalışmanın tasarım heuristiğidir. Bilimsel olarak
optimal veya bağımsız deneyle doğrulanmış yöntem diye sunulmaz.

## Taze doğrulama kaydı

Kullanılan yorumlayıcı:
`C:/Users/xxx/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe`
(Python 3.12.14). Aşağıdaki python komutları bu tam yol ile çalıştırıldı.

| Kontrol | Exit | Sonuç / sınır |
|---|---:|---|
| Başlangıç dosya/env okumaları | 0 veya belirtilen keşif hatası | Claude'da istenen üç workflow bulundu; .agents/yerel finder bazı arama köklerinde yok. Birleşik keşif komutlarının son exit'i her alt komutun sonucu sayılmadı |
| Yerel feature branch oluşturma | ilk deneme izin hatası, yükseltilmiş tekrar 0 | Kullanıcının istediği değişiklikler için branch oluşturuldu; push/commit yok |
| DWF paper model | 0 | Block matrix ve Will dağılım assert'leri geçti; iki G1 release predicate PASS |
| Bundled quick_validate.py | 1 | PyYAML bulunamadı; bu doğrulayıcı geçti iddiası yok, runtime/global bağımlılık eklenmedi |
| Bundled Node yaml keşfi | 1 | yaml modülü bulunamadı; başarısız fallback keşfi |
| `validate_planning.py --root <workspace>` | 0 | 8 skill metadata, 21 ticket, 24 Q, 13 RQ, 188 yerel link/36 Markdown; eksik ID/döngü yok; runtime işleri blocked |
| git diff --check | 0 | Whitespace kontrolü; CRLF bilgilendirmesi hata değildir |

DWF taze sonucu: varsayılan Parry başarı olasılığı %35/%55/%70/%85 olduğunda model
median round 13/8/7/5, p95 26/16/12/9 verir. Bunlar insan başarı oranı değil modele
verilmiş olasılıklardır. “5–7 tur” hedefini tüm oyunculara genellemek bu veriden çıkmaz.
G1 predicate PASS, sonraki wound/deck/route yolunun doğrulandığı anlamına gelmez.

Bağımsız skill senaryoları: “G1 makul, paper only, D1 hazırla” durumunda G1 provisional,
T11 blocked kalır; living card vs legacy YAML durumunda aktif spec living kaynağı
kullanır; zaten yetkili bounded runtime işinde yeni genel onay istenmez. Üçü beklenen
otorite davranışını üretti. Async tool bulunmazsa fallback belirsizliği saptandı ve
grill-me'ye açık düz-soru yolu eklendi. Bu statik walkthrough, geniş skill eval'i değildir.

## Değişen dosyalar ve kapsam denetimi

- Production SKILL.md, plugin-routing ve iki yeni referans: doğru authority/gate,
  araştırma, karar/ticket ve araç rotası.
- Üçüncü taraf kökenli yerel frontend ve Playwright kopyaları: somut kapsam/link/
  izin sorunları. Debug skill incelendi, değiştirilmedi.
- Dört yeni yerel skill: mevcut talebe yönelik, sıfır harici hesap bağımlılığı.
- Production skill altında küçük stdlib validator: bu paket için metadata/link/
  blocker/coverage denetimi; genel skill doğrulayıcının yerine geçtiği iddia edilmez.
- docs/planning: plan, ticket indeksi ve T01-T21. docs/README yalnız navigasyon.
- Bu research raporu: gerçek audit, köken, kaynak, bulgu ve doğrulama kaydı.

Legacy src/config/tests/examples ve research modelleri değiştirilmedi.
Engine/runtime/asset kurulumu, owner kural terfisi, global Codex/Claude ayarı, commit,
push veya remote publication yapılmadı.

Öneri: skill ve plan değişiklikleri belge/araç düzeyinde gözden geçirilebilir.
Bu öneri D0, runtime veya tasarım tercihlerine merge/onay değildir.
Kalan en zayıf bağlantı: OPEN seçimler gerçek owner yanıtı ve exact fixture'a dönüşmedi.
Bu ilk denetim anının sonraki sorusu Q01 idi. Aynı gün sonraki owner yanıtları Q01'i
iki dövüş, Q02'yi yeni boss mekaniğine izin olarak kapattı; aşağıdaki revizyon geçerlidir.

## Son owner yönüyle demo uzlaştırması — 2026-09-06

**PAPER ONLY.** Owner'ın cehennemde ruh başlangıcı, insan/asimetrik yakın tehditten
oluşan iki normal NPC, ana oyunda da amaçlanan güçlü boss'un yeni mekaniği ve kısa
savaş sonrası oyuncu yenilgisi/demo sonu yönü beş living belgeye, çalışma sözleşmesine,
plan ve bağlı ticket'lara işlendi. Önceki boss zaferi/kaçış kabulü açıkça değiştirildi.
Önceki dated ledger girişleri tarihsel köken olarak tutuldu; güncel kapsam değildir.

### Kaynak ve çıkarım sınırı

- [İlk vizyon arşivi](../docs/archive/design_history_2026-08-21/01_PROJECT_STATE_HISTORY_VISION.md)
  hell-loop ve broken-body/yeniden kurma kökenini taşır. Bu, literal ruh başlangıcı,
  seçilmiş boss kimliği veya zorunlu final ölümü kanıtı değildir.
- [Beden bütünlüğü owner incelemesi](../docs/archive/design_history_2026-08-21/33_SOURCE_FIRST_MODULAR_INTEGRITY_OWNER_REVIEW_v0_1.md)
  eksik uzvun kayıp yerel işlevle ele alınmasını destekler. “Üstün kol + eksik bacak”
  kendi başına eşit zorluk ispatı değildir; hedeflenebilir kaynak, legal eylem ve
  savunma açıkları seçili fixture'da karşılaştırılmalıdır.
- MDA yukarıdaki yöntem kaynağıdır. Graft'ın normal kullanımını boss yeniliğinden
  önce gözlemek karışan etkileri azaltmaya yönelik tasarım önerisidir; bu demo için
  deneysel olarak doğrulanmış ideal sıra iddiası değildir.
- [Steam demo rehberi](https://partner.steamgames.com/doc/store/application/demos)
  gelecekte ana oyun mağaza/istek listesine yönlendirme seçeneğini destekler. Harici
  uygulama kurulmadı/yayın yapılmadı; yönlendirme ya da arkadaş ilgisi talep kanıtı değildir.

### Kritik nedensel düzeltmeler

1. Final yenilgi onaylı; kesinlik, kayıp/ölüm ayrımı ve tetikleyici Q25 açık. Yüksek
   hasar, kusursuz Evade/Parry ve survival karşısında kaçınılmazlığı kanıtlamaz.
2. İkinci rakip donor olursa sıradan graft testi için savaş kalmaz. Q26 üç sıra
   adayını taşır; insan donoruyla eksik normal işlevi geri kazanma da mümkündür.
   İlk iletilen iki seçenek bu üçüncü ihtimali dışlamaz. Yeni prova onaysız eklenmez.
3. Final boss yenilmiyorsa eski zafer Brain ödülü korunamaz. Q19/Q20 kapsamı açık;
   erken ödül, ölüm ödülü veya otomatik playable reset sessizce eklenmedi.
4. Guard/şehir açılışı Q27'de uzlaştırılacak; ruh/beden, aktör nedenleri ve final
   merakı Q28'de seçilecek. Öneri hikâye/mekanik tabloları yeni kanon değildir.
5. Normal dövüş ilgisi, boss yeniliğinin anlaşılması/adaleti ve devam beklentisi
   ayrı gözlem sınıfları oldu. Sabit kayıp finalin görülmesi eğlence kanıtı sayılmaz.

Güncel koordinasyon: [plan ve kabul matrisi](../docs/planning/D0_EXECUTION_PLAN_2026-09-06.md).
Bu tur engine, legacy kaynak/config/test veya harici hesap ayarı değiştirmez.

### Revizyon kontrolü

Bağımsız salt-okunur inceleme, güncel Combat/Director/ledger özetlerindeki koşulsuz
reset ifadelerini ve graft tablosunda kalan gate-boss sınamasını işaretledi. Bu
ifadeler Q19/Q20/Q25/Q26 koşullarına bağlandı; tarihsel girişler silinmedi.
Standart kütüphaneli plan doğrulayıcısı exit 0: 8 skill, 21 ticket, 28 karar, 14
gereksinim; eksik ID veya ticket bağımlılık döngüsü yok; 192 yerel bağlantı/36 Markdown.
Bu kontrol semantik doğruluk, oyun dengesi veya insan deneyimi kanıtı değildir.
