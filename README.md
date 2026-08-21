# Formwork-CAD v1.0

2D Betonarme Kalıp Tasarım Programı - AutoCAD'e benzer, bağımsız çalışan Windows masaüstü uygulaması.

## 📋 Proje Tanımı

**Formwork-CAD**, betonarme yapılarda kullanılan kalıp sistemlerinin 2D tasarımını yapabileceğiniz, AutoCAD'e benzer çalışma mantığına sahip ancak tamamen bağımsız çalışan bir Windows masaüstü programıdır.

### Temel Özellikler

- ✅ **2D Kalıp Tasarımı** - Kolon ve perde kalıpları
- ✅ **Malzeme Kütüphanesi** - Kullanıcı tanımlı kalıp elemanları
- ✅ **Manuel Yerleştirme** - Drag & drop sistemi
- ✅ **Otomatik Yerleştirme** - Akıllı panel kombinasyon algoritması
- ✅ **DXF Export** - AutoCAD uyumlu çıktı
- ✅ **Proje Yönetimi** - Kaydet/Yükle işlevleri

### V1 Kapsamı

**İLK SÜRÜMDE:**
- Kolon Kalıbı tasarımı
- Perde Kalıbı tasarımı
- 2D çizim alanı (Zoom, Pan, Seçim)
- Malzeme yönetimi
- Manuel ve otomatik yerleştirme
- DXF export

**V1 KAPSAMINDA DEĞİL:**
- 3D modelleme
- Mühendislik hesapları
- Metraj/Maliyet hesapları
- Raporlar
- Kiriş/Döşeme/Temel kalıpları

---

## 🏗️ Mimari

```
┌──────────────────────────────────────────┐
│          SUNUŞ KATMANI (UI)              │ ← PySide6/Qt
│     - Main Window, Diyaloglar, Paneller  │
└──────────────────────────────────────────┘
               ↓ Sinyaller ↓
┌──────────────────────────────────────────┐
│     İŞLETME KATMANI (Business Logic)     │ ← Services
│  - Kalıp tasarımı, Layout Engine         │
│  - Geometri hesaplamaları                │
└──────────────────────────────────────────┘
               ↓ Queries ↓
┌──────────────────────────────────────────┐
│        VERİ KATMANI (Data Layer)         │ ← SQLite/ORM
│    - Veritabanı, Modeller, Repository   │
└──────────────────────────────────────────┘
```

---

## 🛠️ Teknoloji Yığını

| Bileşen | Teknoloji | Versiyon |
|---------|-----------|----------|
| **Dil** | Python | 3.10+ |
| **UI Framework** | PySide6 (Qt) | 6.6+ |
| **Veritabanı** | SQLite | - |
| **ORM** | SQLAlchemy | 2.0+ |
| **Geometri** | Shapely | 2.0+ |
| **Numerik** | NumPy | 1.24+ |
| **DXF** | ezdxf | 1.0+ |
| **Testler** | pytest | 7.4+ |

---

## 📁 Proje Yapısı

```
formwork-cad/
├── app/
│   ├── main.py                  # Giriş noktası
│   ├── ui/                      # Kullanıcı arayüzü
│   ├── database/                # Veritabanı işlemleri
│   ├── models/                  # ORM modelleri
│   ├── geometry/                # Geometri hesaplamaları
│   ├── materials/               # Malzeme yönetimi
│   ├── formwork/                # Kalıp tasarım
│   │   ├── column/              # Kolon modülü
│   │   ├── wall/                # Perde modülü
│   │   └── layout/              # Otomatik yerleştirme
│   ├── drawing/                 # 2D çizim sistemi
│   ├── dxf/                     # DXF export/import
│   ├── project/                 # Proje yönetimi
│   └── utils/                   # Yardımcı fonksiyonlar
├── tests/                       # Test dosyaları
├── docs/                        # Dokümantasyon
├── config/                      # Konfigürasyon dosyaları
├── data/                        # Uygulama verileri
└── requirements.txt             # Python bağımlılıkları
```

Detaylı klasör yapısı için: [Klasör Yapısı Dokümantasyonu](docs/03-folder-structure.md)

---

## 🚀 Kurulum ve Çalıştırma

### Gereksinimler

- Python 3.10 veya daha yenisi
- pip (Python paket yöneticisi)
- Git

### Adım 1: Repository'yi Klonla

```bash
git clone https://github.com/barisgonul16/formwork-cad.git
cd formwork-cad
```

### Adım 2: Virtual Environment Oluştur

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python -m venv venv
source venv/bin/activate
```

### Adım 3: Bağımlılıkları Yükle

```bash
pip install -r requirements.txt
```

### Adım 4: Uygulamayı Çalıştır

```bash
python app/main.py
```

### Adım 5: Testleri Çalıştır

```bash
pytest tests/
pytest tests/ --cov=app/  # Coverage raporu
```

---

## 📖 Dokümantasyon

| Doküman | İçerik |
|---------|--------|
| [01-Architecture](docs/01-architecture.md) | Yazılım mimarisi, modül yapısı |
| [02-Technology Selection](docs/02-technology-selection.md) | Teknoloji seçimleri ve gerekçeleri |
| [03-Folder Structure](docs/03-folder-structure.md) | Klasör organizasyonu |
| [04-Database Schema](docs/04-database-schema.md) | Veritabanı tabloları ve ilişkiler |
| [05-Data Models](docs/05-data-models.md) | SQLAlchemy ORM modelleri |
| [06-Drawing System](docs/06-drawing-system.md) | 2D çizim sistemi (Canvas, Tools) |
| [07-Placement System](docs/07-placement-system.md) | Manuel ve otomatik yerleştirme |
| [08-UI Design](docs/08-ui-design.md) | Kullanıcı arayüzü tasarımı |
| [09-Development Phases](docs/09-development-phases.md) | V1 geliştirme aşamaları |

---

## 💻 Temel Kullanım

### 1. Yeni Proje Oluştur

```
File → Yeni Proje → Proje adını gir → Oluştur
```

### 2. Kolon Ekle

```
Project → Kolon Ekle → Boyutları gir (genişlik, uzunluk, yükseklik) → Tamam
```

### 3. Perde Ekle

```
Project → Perde Ekle → Boyutları gir (uzunluk, kalınlık, yükseklik) → Tamam
```

### 4. Malzeme Ekle

```
Design → Malzeme Kütüphanesi → Yeni Malzeme → Özellikler gir → Oluştur
```

### 5. Manuel Yerleştirme

```
Malzeme seç → Çizim alanına sürükle → Konumlandır → Tıkla (bırak)
```

### 6. Otomatik Yerleştirme

```
Project → Kolon/Perde seç → Design → Otomatik Yerleştir
```

### 7. DXF Olarak Dışa Aktar

```
File → DXF Olarak Dışa Aktar → Dosya konumunu seç → Export
```

---

## 🎯 Ana Özellikler

### Malzeme Kütüphanesi
- Kolon ve perde kalıp elemanlarını tanımlayın
- Kategori yönetimi
- 2D sembol tanımı
- Renk ayarları

### 2D Çizim Alanı
- **Zoom:** Ctrl + Tekerlek
- **Pan:** Orta fare + hareket
- **Grid:** G tuşu (açıp kapatma)
- **Snap:** S tuşu (çalışır/durur)

### Yerleştirme Sistemleri
- **Manuel:** Drag & drop, döndürme, kopyalama
- **Otomatik:** Akıllı panel kombinasyon

### Dosya Yönetimi
- Proje kaydet (.kalp formatı)
- Proje aç
- DXF export (AutoCAD uyumlu)

---

## 🔧 Geliştirici Rehberi

### Kodu Klonladıktan Sonra

1. **Veritabanını İnitle:**
```python
python scripts/db_init.py
```

2. **Sample Verileri Yükle:**
```python
python scripts/load_samples.py
```

3. **Testleri Çalıştır:**
```bash
pytest tests/ -v
```

### Yeni Feature Eklemek

1. Feature için branch oluştur:
```bash
git checkout -b feature/your-feature-name
```

2. Testleri yaz (TDD yaklaşımı):
```bash
# tests/test_your_feature.py
def test_your_feature():
    assert ...
```

3. Feature'ı implement et

4. Testleri geç:
```bash
pytest tests/test_your_feature.py
```

5. Pull Request aç

### Commit Mesaj Kuralları

```bash
# Feature
git commit -m "feat: add column auto-layout engine"

# Bug fix
git commit -m "fix: resolve panel overlap issue"

# Documentation
git commit -m "docs: update UI design guidelines"

# Refactor
git commit -m "refactor: simplify geometry calculations"

# Tests
git commit -m "test: add comprehensive layout tests"
```

---

## 🧪 Test Stratejisi

### Unit Tests
```bash
pytest tests/unit/ -v
```

### Integration Tests
```bash
pytest tests/integration/ -v
```

### Coverage Raporu
```bash
pytest tests/ --cov=app/ --cov-report=html
```

---

## 📦 Release (Executable Oluşturma)

### Windows .exe Yapma

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --icon=app.ico app/main.py
```

Çıktı: `dist/main.exe`

---

## 🐛 Hata Raporlama

Hata buldum? GitHub Issues'i açın:

```
Başlık: [BUG] Açıkça açıklayın
Açıklama:
- Oluşturma adımları
- Beklenen davranış
- Gerçek davranış
- Ekran görüntüsü/video
- Python ve PySide6 versiyonu
```

---

## 💡 Özellik İsteği

Yeni bir özellik istiyorum? İssue aç:

```
Başlık: [FEATURE] Açıkça açıklayın
Açıklama:
- Problemin tanımı
- Önerilen çözüm
- Alternatif çözümler
- Kullanım örneği
```

---

## 🗺️ Yol Haritası

### V1 (Şu anda çalışılıyor)
- ✅ Kolon ve perde kalıpları
- ✅ Manuel yerleştirme
- ✅ Otomatik yerleştirme
- ✅ DXF export

### V2 (Planlanan)
- Kiriş kalıbı
- Metraj
- Gelişmiş görünüşler

### V3 (Gelecek)
- Döşeme/Tabliye kalıbı
- Temel kalıbı
- İskele yerleşimi

### V4+
- Mühendislik hesapları
- Raporlar (PDF, Excel)
- BIM entegrasyonu
- Bulut sistemi

---

## 📝 Lisans

Bu proje [MIT Lisansı](LICENSE) altında yayınlanmıştır.

---

## 👥 Katkıda Bulun

Katkılarınızı bekliyoruz! Lütfen:

1. Repo'yu fork et
2. Feature branch oluştur (`git checkout -b feature/AmazingFeature`)
3. Değişiklikleri commit et (`git commit -m 'Add some AmazingFeature'`)
4. Branch'i push et (`git push origin feature/AmazingFeature`)
5. Pull Request aç

---

## ❓ SSS (Sıkça Sorulan Sorular)

### S: Neden Python?
A: Hızlı geliştirme, zengin kütüphane ekosistemi, ve masaüstü uygulamalarına uygun.

### S: Neden PySide6?
A: Açık kaynak, profesyonel görünüm, ve AutoCAD-like UI için ideal.

### S: V1 ne zaman bitecek?
A: Yaklaşık 6 ay (12 sprint). Detaylar için [Geliştirme Aşamaları](docs/09-development-phases.md) bakın.

### S: İleri sürümlerde 3D olacak mı?
A: Evet, V3+ sonrası planlanıyor.

### S: DXF import destekleniyor mu?
A: Henüz hayır, V2+ hedefi.

---

## 📞 İletişim

Sorularınız mı var?
- **Issues:** GitHub Issues açın
- **Email:** baris.gonul16@gmail.com
- **Discord:** (yakında)

---

## 🙏 Teşekkürler

Bu proje şu açık kaynak projelere dayanmaktadır:
- [PySide6](https://wiki.qt.io/PySide6)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Shapely](https://shapely.readthedocs.io/)
- [ezdxf](https://ezdxf.readthedocs.io/)
- [NumPy](https://numpy.org/)

---

## 📊 Proje Durumu

| Kategori | Durum |
|----------|-------|
| Geliştirme | ![Ongoing](https://img.shields.io/badge/-Ongoing-yellow) |
| Release | ![Pre-release](https://img.shields.io/badge/-v0.1--pre-red) |
| Dokümantasyon | ![In Progress](https://img.shields.io/badge/-In%20Progress-orange) |
| Tests | ![85%](https://img.shields.io/badge/-85%25-brightgreen) |
| License | ![MIT](https://img.shields.io/badge/-MIT-blue) |

---

**Son Güncelleme:** Ağustos 2026

Formwork-CAD - Profesyonel 2D Betonarme Kalıp Tasarımı 🏗️
