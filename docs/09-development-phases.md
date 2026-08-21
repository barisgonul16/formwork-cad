# 9. V1 GELİŞTİRME AŞAMALARI (Geliştirme Planı)

## 9.1 Geliştirme Metodolojisi

**Agile Sprint Modeli:**
- Her sprint: 2 hafta
- Daily standup: 15 dakika
- Sprint review: Cuma
- Sprint retrospective: Cuma

**Test Stratejisi:**
- Unit tests yazılır (70% coverage hedefi)
- İnsan testi (manual testing)
- Regression testing her sprint sonunda

---

## 9.2 V1 Aşamaları (Toplam ~20 hafta = 10 sprint)

### PHASE 1: Temel Altyapı (Sprint 1-2)

#### Sprint 1: Proje Kurulumu

**Hedefler:**
- ✅ Git repo hazır
- ✅ Proje yapısı oluşturulmuş
- ✅ Development environment kurulmuş
- ✅ SQLite + SQLAlchemy entegrasyonu
- ✅ Temel logger systemi

**Görevler:**
```
1. app/ klasör yapısı oluştur
2. requirements.txt yazılsın
3. database/ modülü ve SQLite bağlantısı
4. models/ (BaseModel, Project)
5. Logger konfigürasyonu
6. İlk testleri yaz
7. GitHub Actions CI setup (ileride)
```

**Teslim Edilecek:**
- Çalışan kod yapısı
- Database bağlantısı test edilmiş
- Docs güncellenmesi

**Kabul Kriterleri:**
```
✓ Program başlatılabilir
✓ Database oluşturulabilir
✓ İlk proje kaydedilir
✓ Tests %80 pass
```

---

#### Sprint 2: UI Framework + Main Window

**Hedefler:**
- ✅ PySide6 kurulu ve çalışıyor
- ✅ Main window tasarımı
- ✅ Sol panel (ağaç yapısı)
- ✅ Sağ panel (özellikler)
- ✅ Toolbar (temel butonlar)
- ✅ Menü yapısı

**Görevler:**
```
1. MainWindow sınıfı yazılsın
2. LeftPanel (QTreeWidget)
3. RightPanel (QScrollArea)
4. Toolbar tasarımı
5. Menu yapısı
6. Signal/Slot temel işlevler
7. İkonlar ekle
```

**Teslim Edilecek:**
- Çalışan UI iskeletonu
- Tüm paneller görünür
- Menu ve toolbar functional

**Kabul Kriterleri:**
```
✓ Application başlatılabilir
✓ Windows minimize/maximize/close çalışır
✓ Paneller resize edilebilir
✓ Menüler açılabilir
```

---

### PHASE 2: Veri Modelleri ve Malzeme Kütüphanesi (Sprint 3-4)

#### Sprint 3: Veri Modelleri (ORM)

**Hedefler:**
- ✅ Tüm SQLAlchemy modellemeleri
- ✅ Database şeması migration
- ✅ Repository pattern (CRUD işlemleri)
- ✅ Model testleri

**Görevler:**
```
1. Material, MaterialCategory, Column, Wall modellemeleri
2. FormworkElement, Layer, Drawing modellemeleri
3. SQLAlchemy ilişkiler
4. Migration sistemi
5. Repository sınıfları (CRUD)
6. Comprehensive tests
```

**Teslim Edilecek:**
- Tüm modeller DB'de
- CRUD işlevleri test edilmiş
- Migration scripti

**Kabul Kriterleri:**
```
✓ Proje DB'ye kaydedilir
✓ Material CRUD çalışır
✓ İlişkiler doğru kurulmuş
✓ Test coverage ≥80%
```

---

#### Sprint 4: Malzeme Kütüphanesi UI

**Hedefler:**
- ✅ Material Library diyalogu
- ✅ Yeni malzeme ekleme
- ✅ Malzeme düzenleme/silme
- ✅ Kategori yönetimi
- ✅ Malzeme listesi (tablo görünüş)

**Görevler:**
```
1. MaterialDialog yazılsın
2. Material CRUD diyalogları
3. Category yönetimi
4. Malzeme tablosu (QTableWidget)
5. Filtreleme ve arama
6. Renk seçici entegrasyonu
7. Icon/Symbol görünüş
```

**Teslim Edilecek:**
- Çalışan malzeme kütüphanesi
- Kullanıcı malzeme ekleyebilir
- Kategorilenmiş malzemeler

**Kabul Kriterleri:**
```
✓ Yeni material oluşturulabilir
✓ Material silinebilir
✓ Kategori oluşturulabilir
✓ Malzeme listesi gösterilir
✓ Renk değiştirebilir
```

---

### PHASE 3: 2D Çizim Sistemi (Sprint 5-6)

#### Sprint 5: Drawing Canvas

**Hedefler:**
- ✅ QGraphicsView/Scene kurulumu
- ✅ Grid sistemi
- ✅ Zoom (in/out/fit)
- ✅ Pan (orta fare)
- ✅ Layer yönetimi

**Görevler:**
```
1. DrawingCanvas sınıfı (QGraphicsView)
2. QGraphicsScene setup
3. Grid çizim ve kontrol
4. Zoom işlevleri
5. Pan işlevleri
6. LayerManager
7. Coordinate converter
```

**Teslim Edilecek:**
- Çalışan 2D canvas
- Grid ve Snap sistemi
- Zoom/Pan işlevleri

**Kabul Kriterleri:**
```
✓ Canvas başlar
✓ Grid görülür
✓ Zoom/Pan çalışır
✓ Layer sistemi çalışır
```

---

#### Sprint 6: Temel Şekiller ve Seçim

**Hedefler:**
- ✅ Rectangle ve Polygon şekilleri
- ✅ Shape seçimi
- ✅ Shape taşıma
- ✅ Shape silme
- ✅ Ölçü araçları

**Görevler:**
```
1. FormworkRectangle sınıfı
2. GraphicsItem custom rendering
3. Selection logic
4. Move/Drag işlevleri
5. Delete işlevi
6. Measurement line
7. Keyboard shortcuts
```

**Teslim Edilecek:**
- Canvas'ta şekiller çizilebilir
- Şekiller seçilebilir/taşınabilir
- Ölçüleri alınabilir

**Kabul Kriterleri:**
```
✓ Rectangle eklenebilir
✓ Shape seçilir (highlight)
✓ Drag & drop çalışır
✓ Delete çalışır
✓ Measurement çalışır
```

---

### PHASE 4: Kolon ve Perde Tasarımı (Sprint 7-8)

#### Sprint 7: Kolon Modülü

**Hedefler:**
- ✅ Kolon oluşturma diyalogu
- ✅ Kolon özellikleri düzenleme
- ✅ Kolon görünüşleri (ön, yan, üst)
- ✅ Kolon geometrisi rendering

**Görevler:**
```
1. ColumnDialog (yeni, düzenle)
2. ColumnGeometry sınıfı
3. ColumnService (CRUD + business logic)
4. Kolon çizimi (canvas'ta)
5. 3 görünüş (ön, yan, üst) JSON storage
6. Left panel'e kolon ağacı
7. Tests
```

**Teslim Edilecek:**
- Kolon oluşturulabilir
- Kolonlar DB'de saklanır
- Canvas'ta görünür

**Kabul Kriterleri:**
```
✓ Kolon dialogi açılır
✓ Kolon oluşturulur
✓ Kolon canvas'ta görünür
✓ Kolon özellikleri düzenlenebilir
✓ 3 görünüş oluşturulur
```

---

#### Sprint 8: Perde Modülü

**Hedefler:**
- ✅ Perde oluşturma diyalogu
- ✅ Perde geometrisi
- ✅ Perde görünüşleri (ön, arka, üst)
- ✅ Kolon ve Perde birlikte çalışması

**Görevler:**
```
1. WallDialog (yeni, düzenle)
2. WallGeometry sınıfı
3. WallService (CRUD)
4. Perde çizimi (canvas'ta)
5. 3 görünüş JSON storage
6. Left panel'e perde ağacı
7. Tests
```

**Teslim Edilecek:**
- Perde oluşturulabilir
- Perdeler DB'de saklanır
- Canvas'ta görünür

**Kabul Kriterleri:**
```
✓ Perde dialogi açılır
✓ Perde oluşturulur
✓ Perde canvas'ta görünür
✓ Kolon ve perde birlikte gösterilir
```

---

### PHASE 5: Manuel ve Otomatik Yerleştirme (Sprint 9-10)

#### Sprint 9: Manuel Yerleştirme

**Hedefler:**
- ✅ Malzeme → Canvas drag & drop
- ✅ Grid snap sistemi
- ✅ Döndürme (Rotation)
- ✅ FormworkElement oluşturma
- ✅ Manuel taşıma/silme

**Görevler:**
```
1. ManualPlacement sınıfı
2. Drag & drop logic
3. Ghost item preview
4. Rotation mechanism
5. Snap to grid algoritması
6. FormworkElement DB kayıt
7. Canvas rendering
8. Tests
```

**Teslim Edilecek:**
- Malzeme manuel yerleştirilebilir
- Grid snap çalışır
- Döndürme çalışır

**Kabul Kriterleri:**
```
✓ Malzeme sürüklenebilir
✓ Ghost preview gösterilir
✓ Snap grid'e yakalanır
✓ Rotasyon çalışır
✓ Element DB'ye kaydedilir
```

---

#### Sprint 10: Otomatik Yerleştirme (Layout Engine)

**Hedefler:**
- ✅ Layout Engine kurulumu
- ✅ Panel kombinator algoritması
- ✅ Otomatik panel yerleşimi
- ✅ Kısıtlama kontrolü (overlap)
- ✅ Kullanıcı UI entegrasyonu

**Görevler:**
```
1. LayoutEngine sınıfı
2. PanelCombinator sınıfı
3. Kombinasyon bulma algoritması
4. ConstraintChecker
5. PlacementOptimizer
6. AutoLayoutDialog UI
7. Kolon ve Perde otomatik yerleştir
8. Comprehensive tests
```

**Teslim Edilecek:**
- Otomatik yerleştirme çalışır
- Panel kombinasyonları bulunur
- Kolon ve perde otomatik yerleştirilebilir

**Kabul Kriterleri:**
```
✓ Otomatik yerleştir butonu çalışır
✓ Kombinasyonlar bulunur
✓ Paneller yerleştirilir
✓ Çakışma kontrolü çalışır
✓ Manuel düzeltme yapılabilir
```

---

### PHASE 6: Dosya İşlemleri ve DXF Export (Sprint 11)

#### Sprint 11: Proje Kaydet/Yükle ve DXF Export

**Hedefler:**
- ✅ Proje kaydetme (.kalp dosyası)
- ✅ Proje yükleme
- ✅ DXF export işlevselliği
- ✅ Dosya diyalogları

**Görevler:**
```
1. ProjectFileHandler sınıfı
2. .kalp dosya formatı (JSON)
3. Proje serialization
4. DXF Exporter (ezdxf)
5. Layer dönüşümü (app → DXF)
6. Entity dönüşümü
7. File dialogs (Save, Open, Export)
8. Tests
```

**Teslim Edilecek:**
- Proje kaydedilebilir
- Proje yüklenebilir
- DXF export çalışır

**Kabul Kriterleri:**
```
✓ Proje kaydet çalışır
✓ Proje aç çalışır
✓ .kalp dosyası oluşturulur
✓ DXF export çalışır
✓ AutoCAD'de açılabilir
```

---

### PHASE 7: Test, Optimizasyon, Dokümantasyon (Sprint 12)

#### Sprint 12: Finalleştirme

**Hedefler:**
- ✅ Comprehensive testing
- ✅ Performance optimization
- ✅ User documentation
- ✅ Release preparation

**Görevler:**
```
1. End-to-end testing
2. Regression testing
3. Performance profiling
4. Memory leak testi
5. User guide yazılması
6. Tutorial oluşturulması
7. Known issues dokümantasyonu
8. Release notes
9. README update
10. PyInstaller ile .exe yapma
```

**Teslim Edilecek:**
- Çalışan V1 release
- Dokümantasyon
- Executable (.exe)

**Kabul Kriterleri:**
```
✓ Tüm features çalışır
✓ Kritik hata yoktur
✓ Test coverage ≥80%
✓ Dokümantasyon tamamlandı
✓ .exe çalışır
```

---

## 9.3 Sprint Şablonu

### Sprint Planlaması
```
Sprint Başlığı: Sprint 5 - Drawing Canvas
Süre: 2 hafta (Pazartesi - Cuma)
Hedef: Canvas zoom/pan/grid sistemi

User Stories:
1. Grid gösterilir ve açılıp kapatılabilir
2. Zoom in/out çalışır
3. Pan (orta fare) çalışır
4. Fit to view çalışır
5. Layer sistemi çalışır

Tasks:
- DrawingCanvas sınıfını yaz
- Grid algoritması
- Zoom işlevleri
- Pan işlevleri
- LayerManager sınıfı
- Unit tests
- Integration tests
- Documentation

Kabul Kriterleri:
✓ Canvas başlatılır
✓ Grid görülür
✓ Zoom 5x kadar
✓ Pan etkili
✓ Smooth rendering
✓ Tests ≥80%
```

---

## 9.4 Risk Yönetimi

| Risk | Olasılık | Etki | Önlem |
|------|----------|------|-------|
| PySide6 performance issues | Düşük | Yüksek | Early prototype |
| Panel kombinator algoritması çok yavaş | Orta | Orta | NumPy optimizasyonu |
| DXF format karmaşıklığı | Orta | Düşük | ezdxf library |
| Requirements değişmesi | Düşük | Yüksek | Erken feedback |
| Takım üye kaybı | Çok Düşük | Yüksek | Dokümantasyon |

---

## 9.5 Prioritization Matrix

### Must Have (V1 içinde zorunlu)
- 2D Canvas + Zoom/Pan
- Kolon ve Perde tasarımı
- Manuel yerleştirme
- Otomatik yerleştirme
- DXF export
- Proje kaydet/yükle

### Should Have (V1 sonunda hedef)
- Ölçü araçları
- Layer sistemi
- Undo/Redo
- Material kategorisi

### Nice to Have (V2+)
- Grid ayarlanabilirlik
- Custom themes
- Import DXF
- Raporlar

### Won't Have (V1 kapsamı dışı)
- 3D modelleme
- Engineering calculations
- BIM entegrasyonu
- Bulut sistemi

---

## 9.6 Performans Hedefleri

| Metrik | Hedef |
|--------|-------|
| Uygulama başlama süresi | < 2 saniye |
| 100 panel yükleme | < 1 saniye |
| Zoom çıkmazlık (jank) | 0 frame drops |
| Memory usage | < 300 MB |
| Panel kombinasyon bulma (6000mm) | < 500ms |
| DXF export (100 eleman) | < 2 saniye |

---

## 9.7 Gıydirim Metrikler

| Metrik | Hedef |
|--------|-------|
| Code coverage | ≥ 80% |
| Documentation | 100% public API |
| Commit message quality | Conventional commits |
| Code review | 2 reviewer minimum |
| Release notes | Detaylı changelog |

---

## 9.8 V1 Sürüm Kriterleri

V1 release için tüm aşağıdakiler tamamlanmalıdır:

- ✅ Tüm sprint hedefleri tamamlandı
- ✅ Critical bugs sıfır
- ✅ Test coverage ≥80%
- ✅ User documentation yazıldı
- ✅ Known issues belgelendi
- ✅ Performans hedefleri met edildi
- ✅ Security audit geçildi
- ✅ Executable oluşturuldu
- ✅ Changelog yazıldı
- ✅ Release notes hazırlandı

---

## 9.9 Post-V1 Feedback Loop

- ✅ Kullanıcı feedback topla
- ✅ Bug raporları anal
- ✅ Feature request önceliklendir
- ✅ V2 planlamasını başlat

---

## Sonuç

✅ Geliştirme Planı:
- 12 sprint = 24 hafta = ~6 ay
- Evreli ve manageable görevler
- Clear acceptance criteria
- Risk mitigation strategies
- Performans hedefleri
- Kalite kontrol mekanizmaları
