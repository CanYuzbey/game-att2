# Game att2 — Director Handoff ve Karar Metodolojisi

Son güncelleme: 2026-08-19
Belge türü: operasyonel yönlendirme ve bilgisayarlar arası devamlılık kaydı
Karar sahibi: Can Yüzbey

## 1. Bu belgenin amacı

Bu dosya, projeyi başka bir bilgisayarda veya yeni bir Codex oturumunda aynı karar
disipliniyle sürdürebilmek için hazırlanmıştır. Birincil tasarım otoritesinin yerine
geçmez; doğru kaynaklara, mevcut kapıya ve karar yöntemine açılan kısa yoldur.

Yeni ortamda ilk komut şu olmalıdır:

```powershell
git clone https://github.com/CanYuzbey/game-att2.git
cd game-att2
git status --short
git branch --show-current
```

Ardından bu dosya, kök `README.md`,
`Game_att2_Codex_Handoff_v0_6/AGENTS.md` ve aktif handoff README'si okunmalıdır.
İstenen çalışma kural, simülatör, test veya proje durumu değiştiriyorsa aşağıdaki tam
okuma sırası uygulanmadan değişiklik yapılmamalıdır.

## 2. Değişmez proje kimliği

Oyuncu silah toplamaz; Blood'u yaşam, para ve yakıt olarak harcarken bedenini yeniden
kurarak silahın kendisine dönüşür.

Kimlik sütunları:

- **Body as Build:** uzuvlar eylem, pasif, ödünleşim ve taktik kimlik üretir.
- **Blood as Volatile Bankroll:** Blood sağlık, para ve yetenek yakıtıdır.
- **Combat as Extraction:** başarı yalnızca öldürmek değil; neyin hasar göreceği,
  korunacağı, çıkarılacağı, graft edileceği veya satılacağı kararıdır.
- **Desperate Maintenance:** alınan her parça stabilizasyon, entegrasyon, koruma veya
  borç baskısı yaratır.
- **Ritualized Readability:** hedef, maliyet, sonuç, ödül ve yeni risk görünür olmalıdır.

Combat; tekrar tekrar saldırı seçip hasar izlenen gelişmiş bir stat menüsüne
dönüşmemelidir. Taktik kart fırsatları bedenden doğmalı, reflex uygulaması committed
eylemi değiştirmeli ve fiziksel sonuçlar sonraki kararları gerçekten daraltmalıdır.

## 3. Kaynak otoritesi ve zorunlu okuma sırası

Çelişki halinde öncelik sırası:

```text
AGENTS.md
-> Development Master v0.6 ve tarihli owner amendments
-> Combat Rules v0.5
-> Simulator Technical Spec v0.2
-> config/*.yaml (yalnızca ayarlanabilir değerler)
-> Test Plan / Acceptance
-> destekleyici kanıt ve tarihçe
```

`docs/archive/`, eski sonuç raporları ve Türkçe PDF tarihsel kanıttır; güncel otorite
değildir. Eski ama cilalı bir belgedeki kural, yeni otoritenin üstüne taşınamaz.

Kural, davranış, test veya proje durumu değişikliğinde şu sıra izlenir:

1. `Game_att2_Codex_Handoff_v0_6/AGENTS.md`
2. `Game_att2_Codex_Handoff_v0_6/docs/README.md`
3. `docs/01_PROJECT_STATE_HISTORY_VISION.md`
4. `docs/02_DEVELOPMENT_MASTER_v0_6.md`
5. `docs/03_COMBAT_RULES_v0_5.md`
6. `docs/04_SIMULATOR_TECHNICAL_SPEC_v0_2.md`
7. `docs/05_CONTENT_CATALOG_v0_1.md` ve `config/*.yaml`
8. `docs/06_TEST_PLAN_ACCEPTANCE_v0_2.md`
9. `docs/07_PAPER_TEST_EVIDENCE_v0_1.md`
10. `docs/08_DECISIONS_RISKS_OPEN_QUESTIONS.md`
11. `docs/09_PRODUCTION_OPERATING_SKILL_v4_1_CODEX.md` ve
    `.agents/skills/game-att2-production/SKILL.md`
12. `docs/10_CODEX_RETURN_CONTRACT.md`
13. `docs/11_SYSTEMIC_CAUSAL_DESIGN_SKILL_v0_1_CODEX.md`
14. `docs/19_CORE_GAMEPLAY_DIRECTION_AND_HANDOFF_2026-08-01.md`
15. `docs/20_H1_HYBRID_COMBAT_SPEC_v0_1.md`
16. `docs/17_COMBAT_MOTIVATION_AND_VICTORY_FRAMEWORK_v0_1.md`
17. `docs/18_OPEN_COMBAT_AND_MOBILITY_DECISIONS.md`
18. `docs/21_H1_IMPLEMENTATION_PLAN_v0_1.md`
19. `docs/22_H1_IMPLEMENTATION_RESULTS_v0_1.md`
20. `docs/23_REFLEX_INTERACTION_TAXONOMY_AND_DIAGNOSTIC_REVISION_v0_1.md`
21. `docs/24_CURRENT_DEVELOPMENT_LEAD_BRIEF_2026-08-12.md`
22. `docs/25_BOUNDED_VISUAL_INTERACTION_LAB_PLAN_v0_1.md`
23. `docs/26_VISUAL_INTERACTION_LAB_IMPLEMENTATION_RESULTS_v0_1.md`
24. `docs/27_AIMED_WOUND_SYSTEM_DIRECTION_AND_OWNER_REVIEW_v0_1.md`
25. `docs/28_SPACE_AND_REACH_DIRECTION_AND_OWNER_REVIEW_v0_1.md`
26. `docs/29_STRATEGIC_CARD_ACTION_ECONOMY_OWNER_INTERVIEW_v0_1.md`
27. `docs/30_WOUND_BLOOD_REPAIR_NUMERIC_OWNER_REVIEW_v0_1.md`
28. `docs/31_STRATEGIC_DEFENSE_CONTRACT_OWNER_REVIEW_v0_1.md`
29. `docs/32_INITIATIVE_AND_CONFLICT_RESOLUTION_OWNER_REVIEW_v0_1.md`
30. `docs/33_SOURCE_FIRST_MODULAR_INTEGRITY_OWNER_REVIEW_v0_1.md`
31. `docs/34_READIED_INVENTORY_CARD_ITEM_BOUNDARY_OWNER_REVIEW_v0_1.md`

Not: handoff README'sinin numaralı listesi şu anda belge 33'te biter; aktif
`docs/README.md`, karar defteri ve lead brief belge 34'ü de aktif otorite sayar. Bu
nedenle devam eden çalışma belge 34'ü de okumalıdır.

Encounter 3 üzerinde yalnızca kağıt araştırması yapılacaksa ayrıca
`docs/encounter_3/README.md` ve onun verdiği sıra izlenir. Bu, runtime izni değildir.

## 4. Güncel doğrulanmış konum

Proje, üretim oyunu değil; tasarım araştırması ve deterministik Python simülatörü
aşamasındadır. Onaylı dijital kapsam yalnızca şu zincirdir:

```text
S-001 -> Jeff -> emergency graft -> Anna -> Grafting Table
```

2026-08-12 kayıtlı teknik baseline:

- 261 test geçti;
- source-only line coverage yüzde 87;
- Ruff temiz;
- strict mypy, 32 kaynak dosyasında temiz;
- yedi senaryo seed 42 ile çalıştı, mini-campaign 25 Blood ile bitti;
- playable campaign replay 36 Blood ile tamamlandı;
- H1 karşılaştırmaları deterministik;
- visual lab 20 varyantta byte-identical replay verdi.

Bu sayılar yalnızca implementation fidelity ve yeniden üretilebilirlik kanıtıdır.
Eğlence, anlaşılabilirlik, erişilebilirlik, adalet, denge, pazar talebi veya production
readiness kanıtı değildir. Yeni bilgisayarda bu sayılar kopyalanıp güncelmiş gibi
sunulmamalı; testler yeniden çalıştırılarak tarihli sonuç verilmelidir.

## 5. Onaylanmış kararlar

### 5.1 Kimlik ve sunum

- Tek oyunculu PC hedefi, çoğunlukla sessiz self-insert, karanlık/rahatsız edici ton
  ve satirik rahatlama kilitlidir.
- Altı beden slotu ilk demo kapsamıdır; uzuvlar ana build motorudur.
- Side-view sunum grid, blok veya travel turn üretmez.
- Küçük demo önce gelir; final engine, art style ve production sunumu açık değildir.

### 5.2 Fiziksel sonuç ve yaralar

- Dört wound ailesi, dominant-wound occupancy, treatment/repair ayrımı, arms/Legs
  için repeat-Major Ruin, sever/harvest ayrımı ve oyuncu/rakip simetrisi kağıt
  yönelim olarak onaylıdır.
- Basic attack Major pressure yaratabilir ama tek başına Clean harvest üretemez.
- Ruined Torso conditional-fataldır ve bir rescue window gerektirir.
- WNR-0.1 Blood, treatment, repair, wounded-limb self-risk ve Torso rescue için
  geçici kağıt baseline'ıdır. Kesin değerler ve runtime uygulaması onaylı değildir.

### 5.3 Alan ve reach

- Clinch, Engaged ve Distant ortak durumdur; serbest movement seçeneği değildir.
- Range, action/defense/reflex veya açık başka bir etkinin sonucunda değişir.
- Korunmayan Clinch bir sonraki tam oynanabilir round boyunca, Distant iki round
  boyunca kalır; sonra Engaged'a yerleşir.
- Dedicated range build'leri authored tactical opportunity ile durumu koruyabilir
  veya yeniden yaratabilir.

### 5.4 Kart ve eylem ekonomisi

- Attention Slots üçten beşe gelişir; slot artışı play sayısını değil seçenekleri
  artırır.
- Kartlar persistent'tır; Decision Refresh ve round başına bir Reconsider vardır.
- Beden eligibility'yi, bilişsel katman seçimi sağlar; kaynak ve fiziksel uyumluluk
  hiçbir zaman atlanmaz.
- Tam kart seti, kesin ağırlıklar, final kapasite dengesi ve runtime henüz onaylı
  değildir.

### 5.5 Savunma, initiative ve çözümleme

- Reflex defense elle oynanan Response card değildir; incoming action ve mevcut build
  legal ise otomatik olarak bir reflex-defense event sunar.
- Zincir: chosen preparation -> bir otomatik reflex route -> uyumlu passive koruma
  -> final consequence resolution.
- Her round bir public Lead ve bir Reply kullanır. Lead önce lock eder, Reply izinli
  telegraph'ı görüp lock eder, Lead çözülür, state settle olur, Reply aynı commitment
  ile yeniden validate edilir.
- Cancellation sonrası replacement action yoktur; başlamış action atomiktir;
  gerçek same-timing etkiler batch olarak ele alınır.

### 5.6 Source-First Modular Integrity

- Capability kaynağa aittir ve Full/Strained/Desperate profilleriyle ifade edilir.
- Birden çok gerekli kaynakta weakest-required-source uygulanır.
- Effect package merkezi ve modülerdir; payload gerçek alıcıya teslim edilir.
- Integrity Echo Coherent/Shaken/Fractured olabilir ama yalnızca sınırlı bir
  micro-axis'i değiştirir; legality, slot, play, Lead, reflex-route varlığı,
  Blood/death veya sonucu değiştiremez.

### 5.7 Inventory sınırı

- Dört opportunity origin vardır: body, inventory, state-required ve automatic.
- Flexible Attention Slot içinde bilinçli seçilen tek Readied Inventory fırsatı vardır.
- Actor başına round'da en fazla bir voluntary inventory-origin action kullanılabilir.
- Item, Preparation/Main bütçesini kullanır; ücretsiz Fast-item rail yoktur.
- Reconsider kullanılmamış inventory opportunity'yi değiştirebilir; Spent slot'u
  yenileyip ikinci item action yaratamaz.
- Ownership, use, expiry, exact source ve weakest-source kuralı zorunludur; lock
  sonrasında tool/grip substitution yapılamaz.
- Passive equipment otomatik, activated tool ise readied olmalıdır.

### 5.8 Reflex araştırma sınırı

- Shared readiness/Stamina ve family-specific repetition pressure yalnızca araştırma
  hipotezidir.
- VL-WP1–VL-WP3 uygulanmış ve fidelity-verified'dır.
- VL-WP4 ve geniş reflex çalışması 2026-08-13'te owner tarafından ertelenmiştir.
- Runtime Stamina, final değerler, external pilot veya production integration onaylı
  değildir.

## 6. Şu an alınması gereken karar

Tek aktif ürün kapısı **range-maintenance action grammar**dır.

Karar sorusu:

> Hangi mevcut action profilleri, evrensel bir movement komutu, yeni content veya
> runtime implementation oluşturmadan Clinch/Engaged/Distant durumunu maintain,
> release veya exploit edebilir?

Bu çalışma kağıt tasarım paketi olarak yürütülmelidir. Her aday mevcut source,
Attention Slot, Lead/Reply, lock, telegraph, automatic defense, wound ve range-settling
kurallarıyla çelişki testinden geçirilmelidir. Bütün action/card profilleri aynı anda
tasarlanmamalı; mevcut içerikten minimum bounded fixture kullanılmalıdır.

Bu karar tamamlanmadan sıradaki kapıya geçilmez.

## 7. Sonraki kararların bağımlılık sırası

```text
range-maintenance action grammar (AKTİF)
-> treatment, repair, extraction ve graft commitment flow
-> Limb for Life ve catastrophic survival
-> mental defeat, surrender, negotiation ve encounter resolution
-> information ve interaction grammar
-> numeric reconciliation
-> daha sonraki reflex-mechanics gate
-> minimum complete game-design paper
-> az sayıda karakter/item/encounter için paper content set
-> engine ve production proposal
```

Bir sonraki adıma yalnızca aktif paketin kabul kriterleri sağlanıp owner kararı
kaydedildikten sonra geçilir.

## 8. Karar üretme metodolojisi

Her tasarım sorusu şu evidence card ile açılır:

```text
Question or hypothesis
Mechanic/config variant
Expected runtime dynamic
Desired player experience
Instrumentation
Continue / revise / kill criteria
Evidence class and contamination risks
Decision owner
```

Her meaningful action veya encounter transition şu nedensel zincire uymalıdır:

```text
prior state
-> legality ve source validation
-> approved rule + injected randomness
-> explicit mutation
-> capability ve legal affordance recomputation
-> forced consequences
-> remaining legal responses arasından motivation-supported choice
-> continuation veya state-derived resolution
-> structured evidence
```

Karar çalışma akışı:

1. İşi `audit`, `simulator maintenance`, `approved simulator change`, `design
   proposal`, `research` veya `out-of-scope` olarak sınıflandır.
2. Tek aktif gate'i ve karar sahibini yaz.
3. Otorite kaynaklarını ve çatışma ihtimalini listele.
4. Mevcut kurallarla çalışabilecek en küçük reversible fixture'ı kur.
5. Alternatifleri mechanic -> dynamic -> experience zincirinde karşılaştır.
6. Ölçülebilir continue/revise/kill kriterleri belirle.
7. İnsan kanıtı yoksa deneyim iddiası kurma.
8. Owner kararı gereken noktayı teknik tercih gibi gizleme.
9. Onay sonrası karar defteri, lead brief ve ilgili owner-review belgesini birlikte
   güncelle; runtime izni ayrıca verilmediyse kod/config değiştirme.
10. Hostile review yap; sonra yalnızca bir sonraki önerilen adımı belirt.

## 9. Kod değişikliği metodolojisi

Yalnızca açıkça onaylı bir implementation gate varsa:

- feature branch kullan; `main`e doğrudan push etme;
- requirement, authority, etkilenen modüller, risk ve acceptance test'i önce yaz;
- immutable definitions ile mutable runtime state'i ayır;
- tüm randomness'i injected `RNGService` üzerinden geçir ve seed/scripted roll kaydet;
- tunable değerleri validated config'te tut; config ile onaysız mechanic saklama;
- domain katmanında print yapma, structured event üret;
- Main action commit edilmeden prerequisites doğrula; rejected action atomik olmalı;
- source invalid olunca eylemi iptal et; planned scene'i korumak için kaynağı diriltme;
- her davranışla pozitif, negatif ve source-invalidation testi ekle;
- yeni runtime dependency ekleme;
- sonuç raporunda kanıt ile deneyim iddiasını kesin biçimde ayır.

Normal doğrulama:

```powershell
cd Game_att2_Codex_Handoff_v0_6
python -m pip install -e ".[dev]"
python -m pytest -q
python -m ruff check src tests
python -m mypy src
python -m game_att2_sim --all-scenarios --seed 42 --format markdown
python -m game_att2_sim.play_cli --seed 42 --script examples/play_cli_full_campaign_sequence.json
```

Determinism önemliyse aynı seeded komutu iki kez çalıştır ve çıktıları karşılaştır.
Dokümantasyon-only işte linkleri, authority label'larını, tarihleri ve version
referanslarını doğrula; eski test sayılarını yeni sonuç gibi kopyalama.

## 10. Kanıt sınıfları ve iddia sınırı

- Simulator/test kanıtı: rule fidelity, reproducibility, reachable state, exploit
  resistance ve numeric distribution gösterebilir.
- Owner diagnostic: yön ve instrument sorunu gösterebilir; external player evidence
  değildir.
- Designer self-play: dış insan kanıtı değildir.
- External pilot: consent, versioned fixture, raw observation, facilitator deviation
  ve contamination kaydı gerektirir.

Hiçbiri tek başına fun, accessibility, fairness, market demand veya replay desire
kanıtlamaz. Contaminated session geçerli pilot sayısına dahil edilmez.

## 11. Kesin kapsam kilitleri

Owner yeni bir gate açmadıkça:

- Warden veya Encounter 3 runtime'a eklenmez;
- Unity/engine seçimi, vertical slice, final UI, art/audio veya story production
  başlatılmaz;
- yeni enemy, limb, item, card, effect veya encounter production content'i eklenmez;
- Stamina, Block pressure veya geniş reflex ailesi campaign'e entegre edilmez;
- wound/card/defense/timing/integrity/inventory kağıt kararları runtime'a taşınmaz;
- movement command, full deck system, final wounds, full debt economy, generalized
  mental defeat veya multi-round negotiation icat edilmez;
- script immortality, resource theatre, decorative limb damage, outcome teleportation
  veya encounter-specific branch ile emergence taklit edilmez;
- tarihsel 37 Blood veya güncel 25/36 Blood bir balance target sayılmaz.

## 12. Owner'ın ayrıca karar vermesi gereken açık alanlar

- Final title, engine, art style, run/map, meta progression, roster, dialogue,
  store/release, save/load ve final debt economy.
- Exact range profiles ve hangi mevcut action/card'ın range'i maintain/release/exploit
  edeceği — aktif karar budur.
- Exact Attention Slot weights, repetition damping, final capacity, individual
  card/item içerikleri ve signature timing exceptions.
- Cognitive progression'ın anatomy/Head/table/shop/skill fiction'ı ve özel bias'ları.
- Automatic reflex success modeli, input family'leri, mitigation, exposure,
  readiness/repetition ve accessibility equivalence.
- Package D profil değerleri, Echo threshold/micro-values, coherence recalibration,
  signature overrides ve production effect catalogue.

Codex yalnızca class/module adı, test fixture düzeni, report formatting, tested integer
rounding ve benzeri geri alınabilir teknik ayrıntıları kendi başına belirleyebilir.

## 13. Hostile review kontrol listesi

Teslimden önce diff şu açılardan incelenir:

- rule/config drift veya stale authority;
- scope creep, yeni dependency veya secret;
- hidden randomness ya da non-atomic action;
- disabled source'un hâlâ eylem üretmesi;
- Blood/limb mutation'ın açıklanamaması;
- invented anatomy, psychology, reward veya balance claim;
- negative/source-invalidation test eksikliği;
- reflex skill'in stratejik hatayı silmesi veya assisted alternatifi dışlaması;
- historical evidence'ın güncel onay gibi sunulması;
- research fixture'ın production combat diye tanıtılması.

P0/P1 bulgusu varsa merge önerilmez.

## 14. Her oturumun teslim sözleşmesi

Her tamamlanan iş şunları raporlamalıdır:

- executive summary ve `merge / revise / do not merge` önerisi;
- değişen dosyalar ve amaçları;
- requirement/authority/test traceability;
- çalıştırılan komutlar ve exit status;
- test ve deterministic scenario sonuçları;
- assumptions, açık owner kararları ve reversibility;
- scope audit;
- severity içeren hostile-review bulguları;
- bilinen limitler;
- tam olarak bir recommended next step.

Bir sonraki product gate, yalnızca önerilmiş olması nedeniyle başlatılmaz.

## 15. Yeni bilgisayarda devam kontrolü

```powershell
git fetch origin
git switch main
git pull --ff-only
git status --short
git log -5 --oneline
```

Sonra:

1. Bu dosyanın `Son güncelleme` tarihini ve `docs/README.md` aktif listesini
   karşılaştır.
2. `docs/08_DECISIONS_RISKS_OPEN_QUESTIONS.md` ile
   `docs/24_CURRENT_DEVELOPMENT_LEAD_BRIEF_2026-08-12.md` içindeki en yeni tarihli
   owner kararını bul.
3. Bu dosyadaki aktif gate eskiyse önce `director.md`yi güncelle.
4. Çalışma ağacı kirliyse kullanıcı değişikliklerini koru; ilgisiz dosyaları commit'e
   alma.
5. Yeni iş için `codex/<kisa-konu>` dalı aç.
6. Task'i sınıflandır, doğru okuma sırasını tamamla ve tek gate üzerinde çalış.
7. Doğrulama, hostile review, commit ve push sonrası branch adını ve commit hash'ini
   teslim et.

Mevcut tek önerilen sonraki adım: mevcut action profilleri üzerinden bounded bir
**range-maintenance action grammar** owner-review paketi hazırlamak ve onaya sunmak.
