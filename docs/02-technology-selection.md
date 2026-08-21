# 2. TEKNOLOJİ SEÇİMİ VE GEREKÇESİ

## 2.1 Neden Python?

### Avantajlar:
- ✅ Hızlı geliştirme (prototyping)
- ✅ Kolay öğrenme ve okunabilirlik
- ✅ Zengin kütüphane ekosistemi
- ✅ Açık kaynak ve ücretsiz
- ✅ Windows masaüstü uygulamalarında kullanılabilir
- ✅ Bilimsel hesaplamalar için ideal (NumPy, Shapely)

### Dezavantajları:
- ⚠️ C/C++'ya göre daha yavaş
- ⚠️ Dağıtım biraz daha karmaşık (.exe yapma)

### Nihai Karar:
**Python 3.10+** kullanılacaktır. Hız problemi V1'de kritik değildir, V2+ sonra C extension gerekirse optimize edilir.

---

## 2.2 UI Framework: PySide6 (Qt for Python)

### Neden PySide6?

| Kriter | PySide6 | PyQt6 | Tkinter | PySimpleGUI |
|--------|---------|-------|---------|-------------|
| Profesyonel Görünüm | ✅ Mükemmel | ✅ Mükemmel | ⚠️ Temel | ⚠️ Temel |
| CAD-like UI | ✅ Evet | ✅ Evet | ❌ Hayır | ❌ Hayır |
| Özelleştirme | ✅ Geniş | ✅ Geniş | ⚠️ Sınırlı | ❌ Çok sınırlı |
| Performans | ✅ İyi | ✅ İyi | ✅ İyi | ⚠️ Yavaş |
| Lisans | ✅ Açık Kaynak | ⚠️ GPL/Ticari | ✅ BSD | ✅ Açık Kaynak |
| Topluluk | ✅ Büyük | ✅ Çok Büyük | ✅ Çok Büyük | ⚠️ Küçük |

### PySide6 Avantajları:
- Tamamen açık kaynak ve ücretsiz
- AutoCAD-like dockable panels
- Profesyonel görünüm (Windows native)
- 2D grafik rendering için `QGraphicsView` + `QGraphicsScene` ideal
- Signals/Slots sistemi (reactive programming)
- Cross-platform (Windows, Mac, Linux)

### Kurulum:
```bash
pip install PySide6
```

---

## 2.3 Geometri Kütüphanesi: Shapely

### Neden Shapely?

| İşlem | Shapely | NumPy Only | Pandas |
|-------|---------|-----------|--------|
| 2D Geometri | ✅ Özel | ⚠️ Manuel | ❌ Hayır |
| Kesişim Tespiti | ✅ Hazır | ❌ Yazmalı | ❌ Hayır |
| Transformasyon | ✅ Kolay | ⚠️ Manuel | ⚠️ Sınırlı |
| Buffer/Offset | ✅ Hazır | ❌ Yazmalı | ❌ Hayır |
| Union/Intersection | ✅ Hazır | ❌ Yazmalı | ❌ Hayır |

### Shapely ile Yapılacak İşlemler:
```python
from shapely.geometry import Rectangle, Polygon, Point

# Kolon geometrisi
column_rect = Rectangle(0, 0, 400, 800)

# Panel yerleşimi kontrolü
panel = Rectangle(0, 0, 1000, 3200)
if column_rect.intersects(panel):
    print("Panel kolon ile çakışıyor")

# Alan hesaplama
area = panel.area

# Koordinat transformasyonu
transformed = panel.buffer(10)  # 10mm offset
```

### Kurulum:
```bash
pip install shapely
```

---

## 2.4 Sayısal Hesaplamalar: NumPy

### Kullanım Alanları:
- Panel boyut kombinasyonlarının hesaplanması
- Koordinat transformasyonları (rotation, scaling)
- Matris işlemleri
- Performans gerektiren işlemler

### Örnek:
```python
import numpy as np

# Panel kombinasyonları
panels = np.array([1000, 1500, 2000])  # mm
target = 6000  # mm

# Uygun kombinasyonu bul
combinations = ...  # NumPy ile hesapla
```

### Kurulum:
```bash
pip install numpy
```

---

## 2.5 Veritabanı: SQLite + SQLAlchemy ORM

### Neden SQLite?

| Kriter | SQLite | PostgreSQL | MySQL |
|--------|--------|-----------|-------|
| Kurulum | ✅ Sıfır | ❌ Karmaşık | ❌ Karmaşık |
| Masaüstü App | ✅ Ideal | ⚠️ Server gerekli | ⚠️ Server gerekli |
| Performans | ✅ Yeterli | ✅ Yüksek | ✅ Yüksek |
| Dosya Tabanlı | ✅ Evet (.db) | ❌ Server | ❌ Server |
| Ölçeklenebilirlik | ⚠️ Sınırlı | ✅ Sınırsız | ✅ Sınırsız |
| Proje Taşınabilirliği | ✅ Kolay | ❌ Zor | ❌ Zor |

### SQLite Avantajları:
- Tek `.db` dosyası = taşınabilir proje
- Kurulum yoktur
- Sürüm kontrolüne kolay girer
- V1-V3 için yeterli
- Sonra PostgreSQL'e migre edilebilir

### Kurulum:
```bash
pip install sqlalchemy
# SQLite SQLAlchemy tarafından built-in desteklenir
```

---

## 2.6 DXF Kütüphanesi: ezdxf

### Neden ezdxf?

| Kriter | ezdxf | dxfgrabber | pydxf |
|--------|-------|-----------|-------|
| DXF Yazma | ✅ Mükemmel | ❌ Hayır | ⚠️ Temel |
| DXF Okuma | ✅ Mükemmel | ✅ İyi | ⚠️ Temel |
| Layer Yönetimi | ✅ Tam | ⚠️ Sınırlı | ⚠️ Sınırlı |
| Bloklar | ✅ Tam | ⚠️ Sınırlı | ❌ Hayır |
| Bakım | ✅ Aktif | ⚠️ Pasif | ⚠️ Pasif |

### ezdxf ile Yapılacak İşlemler:
```python
import ezdxf

# Yeni DXF dosyası
doc = ezdxf.new('R2000')

# Layers
msp = doc.modelspace()
msp.add_lwpolyline([(0, 0), (100, 0), (100, 100), (0, 100)], dxfattribs={'layer': 'PANEL'})

# Dosya kaydetme
doc.saveas('column.dxf')
```

### Kurulum:
```bash
pip install ezdxf
```

---

## 2.7 Loglama: Python logging

### Built-in logging modülü kullanılacaktır
```python
import logging

logger = logging.getLogger(__name__)
logger.info("Proje açıldı")
logger.error("Hata oluştu")
```

**Neden:** Yerleşik, hafif, projelerde standart.

---

## 2.8 Testler: pytest

### Kurulum:
```bash
pip install pytest pytest-cov
```

### Kullanım:
```bash
pytest tests/
pytest tests/ --cov=app/  # Coverage raporu
```

---

## 2.9 Konfigürasyon: JSON + Python Dictionaries

### Format:
```json
{
  "app_name": "Formwork-CAD",
  "version": "1.0.0",
  "database": {
    "path": "data/formwork.db"
  },
  "ui": {
    "window_width": 1200,
    "window_height": 800
  }
}
```

**Neden JSON:**
- İnsan tarafından okunabilir
- Python'da built-in `json` modülü
- Uzantı kolayı

---

## 2.10 Versionlama: Semantic Versioning

```
V1.0.0
 │ │ │
 │ │ └─ Patch (bug fixes)     → 1.0.1
 │ └─── Minor (new features)  → 1.1.0
 └───── Major (breaking changes) → 2.0.0
```

### Tagging:
```bash
git tag -a v1.0.0 -m "First release"
git push origin v1.0.0
```

---

## 2.11 Paket Yönetim: pip + requirements.txt

### requirements.txt:
```
PySide6==6.6.1
SQLAlchemy==2.0.23
shapely==2.0.2
numpy==1.24.3
ezdxf==1.0.2
pytest==7.4.3
pytest-cov==4.1.0
```

### Kurulum:
```bash
pip install -r requirements.txt
```

---

## 2.12 Dağıtım: PyInstaller

### Windows .exe Oluşturma:
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --icon=app.ico app/main.py
```

**Çıktı:** `dist/main.exe` (tek dosya)

---

## 2.13 Sürüm Kontrol: Git + GitHub

- Tüm kod GitHub'da
- Branch strategy: `main` (stable), `develop` (geliştirme)
- Commit mesajları: conventional commits
  - `feat: ...` (yeni özellik)
  - `fix: ...` (hata düzeltmesi)
  - `docs: ...` (dokümantasyon)
  - `refactor: ...` (kod iyileştirmesi)

---

## 2.14 Python Sürümü

**Python 3.10+** tercih edilir

Neden:
- Union types syntax: `int | str` (3.10+)
- Match statements: (3.10+)
- Yeni f-string features: (3.12)
- Geniş kütüphane desteği

---

## 2.15 IDE Önerisi

**VS Code** veya **PyCharm Community**

### VS Code Extensions:
- Python
- Pylance
- Qt for Python
- SQLAlchemy

---

## 2.16 Teknoloji Stack Özeti

```
┌─────────────────────────────────────────┐
│         Formwork-CAD Tech Stack         │
├─────────────────────────────────────────┤
│ Dil:          Python 3.10+              │
│ UI:           PySide6 (Qt)              │
│ Geometri:     Shapely                   │
│ Sayısal:      NumPy                     │
│ Veritabanı:   SQLite + SQLAlchemy ORM   │
│ DXF:          ezdxf                     │
│ Testler:      pytest                    │
│ Dağıtım:      PyInstaller               │
│ Versionlama:  Git + GitHub              │
│ IDE:          VS Code / PyCharm         │
└─────────────────────────────────────────┘
```

---

## 2.17 Kurulum Komutu (Geliştirme Ortamı)

```bash
# Repository klonla
git clone https://github.com/barisgonul16/formwork-cad.git
cd formwork-cad

# Virtual environment oluştur
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Bağımlılıkları yükle
pip install -r requirements.txt

# Uygulamayı çalıştır
python app/main.py

# Testleri çalıştır
pytest tests/
```

---

## Sonuç

✅ Seçilen teknolojiler:
- **Açık kaynak ve ücretsiz**
- **Masaüstü uygulamalarına uygun**
- **İlk sürüm için yeterli performans**
- **Gelecekte genişletilebilir**
- **Büyük topluluk ve dokümantasyon desteği**
