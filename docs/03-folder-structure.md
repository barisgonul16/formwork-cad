# 3. KLASÖR YAPISI

## 3.1 Proje Dizin Ağacı

```
formwork-cad/
│
├── app/                                    # Ana uygulama kodu
│   ├── __init__.py
│   ├── main.py                             # Uygulamanın giriş noktası
│   │
│   ├── ui/                                 # Kullanıcı arayüzü
│   │   ├── __init__.py
│   │   ├── main_window.py                  # Ana pencere
│   │   ├── widgets/                        # Özel Qt widgetleri
│   │   │   ├── __init__.py
│   │   │   ├── drawing_canvas.py           # 2D çizim alanı
│   │   │   ├── left_panel.py               # Sol panel (proje ağacı)
│   │   │   ├── right_panel.py              # Sağ panel (özellikler)
│   │   │   └── toolbar.py                  # Araç çubuğu
│   │   │
��   │   └── dialogs/                        # Diyaloglar
│   │       ├── __init__.py
│   │       ├── new_project_dialog.py       # Yeni proje
│   │       ├── column_dialog.py            # Kolon özellikleri
│   │       ├── wall_dialog.py              # Perde özellikleri
│   │       ├── material_dialog.py          # Malzeme ekleme
│   │       ├── settings_dialog.py          # Ayarlar
│   │       └── export_dialog.py            # DXF export seçenekleri
│   │
│   ├── database/                           # Veritabanı işlemleri
│   │   ├── __init__.py
│   │   ├── db_manager.py                   # Veritabanı yöneticisi
│   │   ├── connection.py                   # Bağlantı yönetimi
│   │   ├── migration.py                    # Database şema oluşturma
│   │   └── repositories/                   # Data access layer
│   │       ├── __init__.py
│   │       ├── base_repository.py          # Base class
│   │       ├── project_repository.py
│   │       ├── material_repository.py
│   │       ├── column_repository.py
│   │       ├── wall_repository.py
│   │       └── element_repository.py
│   │
│   ├── models/                             # Veri modelleri (SQLAlchemy ORM)
│   │   ├── __init__.py
│   │   ├── base_model.py                   # Base model class
│   │   ├── project.py                      # Project modeli
│   │   ├── material.py                     # Material modeli
│   │   ├── column.py                       # Column modeli
│   │   ├── wall.py                         # Wall modeli
│   │   ├── element.py                      # FormworkElement modeli
│   │   ├── layer.py                        # Layer modeli
│   │   └── category.py                     # MaterialCategory modeli
│   │
│   ├── geometry/                           # Geometri hesaplamaları
│   │   ├── __init__.py
│   │   ├── shapes.py                       # Temel şekiller (Rectangle, Polygon)
│   │   ├── transformations.py              # Koordinat transformasyonları
│   │   ├── intersections.py                # Kesişim tespiti
│   │   ├── measurements.py                 # Ölçü işlemleri
│   │   └── utilities.py                    # Yardımcı geometri fonksiyonları
│   │
│   ├── materials/                          # Malzeme yönetimi
│   │   ├── __init__.py
│   │   ├── material_service.py             # Malzeme servisi
│   │   ├── material_library.py             # Malzeme kütüphanesi
│   │   ├── category_manager.py             # Kategori yönetimi
│   │   └── symbol_manager.py               # 2D sembol yönetimi
│   │
│   ├── formwork/                           # Kalıp tasarım sistemleri
│   │   ├── __init__.py
│   │   │
│   │   ├── column/                         # Kolon kalıbı
│   │   │   ├── __init__.py
│   │   │   ├── column_model.py             # Kolon data modeli
│   │   │   ├── column_geometry.py          # Kolon geometrisi oluşturma
│   │   │   ├── column_views.py             # Kolon görünüşleri (ön, yan, üst)
│   │   │   └── column_service.py           # Kolon servisi
│   │   │
│   │   ├── wall/                           # Perde kalıbı
│   │   │   ├── __init__.py
│   │   │   ├── wall_model.py               # Perde data modeli
│   │   │   ├── wall_geometry.py            # Perde geometrisi oluşturma
│   │   │   ├── wall_views.py               # Perde görünüşleri (ön, arka, üst)
│   │   │   └── wall_service.py             # Perde servisi
│   │   │
│   │   └── layout/                         # Otomatik yerleştirme
│   │       ├── __init__.py
│   │       ├── layout_engine.py            # Ana layout algoritması
│   │       ├── panel_combinator.py         # Panel kombinasyon hesaplama
│   │       ├── placement_optimizer.py      # Yerleşim optimizasyonu
│   │       └── constraints.py              # Tasarım kısıtlamaları
│   │
│   ├── drawing/                            # 2D çizim sistemi
│   │   ├── __init__.py
│   │   ├── canvas.py                       # QGraphicsView + QGraphicsScene
│   │   ├── tools.py                        # Çizim araçları (Select, Move, vb.)
│   │   ├── layer_manager.py                # Layer yönetimi
│   │   ├── graphics_items.py               # Qt grafik objeleri
│   │   ├── pen_and_brush.py                # Çizim stili (renk, çizgi kalınlığı)
│   │   └── viewport.py                     # View transformasyonları
│   │
│   ├── dxf/                                # DXF export/import
│   │   ├── __init__.py
│   │   ├── exporter.py                     # DXF export
│   │   ├── importer.py                     # DXF import (ileride)
│   │   ├── layer_converter.py              # Layer dönüşümü
│   │   └── entity_converter.py             # Entity dönüşümü
│   │
│   ├── project/                            # Proje yönetimi
│   │   ├── __init__.py
│   │   ├── project_manager.py              # Proje yöneticisi
│   │   ├── project_service.py              # Proje servisi
│   │   ├── file_handler.py                 # .kalp dosya işlemleri
│   │   └── backup.py                       # Yedekleme sistemi (ileride)
│   │
│   ├── services/                           # İşletme mantığı servisleri
│   │   ├── __init__.py
│   │   └── (Services buraya taşınabilir yapısı)
│   │
│   └── utils/                              # Yardımcı fonksiyonlar
│       ├── __init__.py
│       ├── logger.py                       # Loglama
│       ├── config.py                       # Konfigürasyon yönetimi
│       ├── constants.py                    # Sabitler (layer adları vb.)
│       ├── validators.py                   # Validasyon fonksiyonları
│       ├── converters.py                   # Birim dönüşümleri (mm, cm, m)
│       └── exceptions.py                   # Özel exception sınıfları
│
├── tests/                                   # Testler
│   ├── __init__.py
│   ├── conftest.py                         # Pytest konfigürasyonu
│   │
│   ├── unit/                               # Unit testleri
│   │   ├── __init__.py
│   │   ├── test_geometry.py
│   │   ├── test_materials.py
│   │   ├── test_layout.py
│   │   ├── test_column.py
│   │   ├── test_wall.py
│   │   └── test_validators.py
│   │
│   ├── integration/                        # Entegrasyon testleri
│   │   ├── __init__.py
│   │   ├── test_column_workflow.py
│   │   ├── test_wall_workflow.py
│   │   ├── test_project_save_load.py
│   │   └── test_dxf_export.py
│   │
│   └── fixtures/                           # Test verileri
│       ├── __init__.py
│       ├── sample_data.py
│       └── test_materials.json
│
├── config/                                  # Konfigürasyon dosyaları
│   ├── defaults.json                       # Varsayılan ayarlar
│   ├── settings.json                       # Kullanıcı ayarları
│   ├── categories.json                     # Malzeme kategorileri
│   └── templates.json                      # Şablonlar (ileride)
│
├── data/                                    # Uygulama verileri
│   ├── formwork.db                         # SQLite veritabanı
│   ├── temp/                               # Geçici dosyalar
│   └── samples/                            # Örnek projeler
│
├── resources/                               # Kaynaklar
│   ├── icons/                              # Uygulama ikonları
│   │   ├── new.png
│   │   ├── open.png
│   │   ├── save.png
│   │   ├── column.png
│   │   ├── wall.png
│   │   └── ...
│   │
│   └── themes/                             # UI temalar (ileride)
│       └── dark.qss                        # Qt stylesheet
│
├── docs/                                    # Dokümantasyon
│   ├── 01-architecture.md
│   ├── 02-technology-selection.md
│   ├── 03-folder-structure.md
│   ├── 04-database-schema.md
│   ├── 05-data-models.md
│   ├── 06-drawing-system.md
│   ├── 07-placement-system.md
│   ├── 08-ui-design.md
│   ├── 09-development-phases.md
│   ├── API.md                              # API dokümantasyonu
│   ├── CONTRIBUTING.md                     # Geliştirme kılavuzu
│   └── CHANGELOG.md                        # Sürüm notları
│
├── scripts/                                 # Yardımcı scriptler
│   ├── setup.py                            # Kurulum scripti
│   ├── build.py                            # Build scripti (PyInstaller)
│   ├── run_tests.sh                        # Test çalıştırıcı
│   └── db_init.py                          # Veritabanı başlatıcı
│
├── requirements.txt                         # Python bağımlılıkları
├── .gitignore                               # Git ignore kuralları
├── .github/                                 # GitHub konfigürasyonları
│   └── workflows/                          # CI/CD (ileride)
│       └── tests.yml
│
├── README.md                                # Proje özeti
├── LICENSE                                  # Lisans (MIT)
├── CHANGELOG.md                             # Değişiklik günlüğü
└── setup.cfg                                # Setuptools konfigürasyonu
```

---

## 3.2 Modül Açıklamaları

### 3.2.1 app/ (Ana Uygulama)
Tüm uygulama mantığı burada bulunur. Alt modüller belirli görevleri yerine getirir.

### 3.2.2 app/ui/
- **main_window.py:** Uygulamanın ana penceresi, menüler, durum çubuğu
- **widgets/:** Özel Qt widgetleri (2D canvas, paneller)
- **dialogs/:** Kullanıcı diyalogları (yeni proje, özellik girişi, vb.)

### 3.2.3 app/database/
- **db_manager.py:** Singleton pattern, veritabanı bağlantısı ve işlemleri
- **repositories/:** Veri erişim layer'ı (repository pattern)

### 3.2.4 app/models/
SQLAlchemy ORM modellemeleri. Her tablo için bir sınıf.

### 3.2.5 app/geometry/
Shapely, NumPy ile geometri hesaplamaları.

### 3.2.6 app/formwork/
Kalıp tasarımı için modüller:
- **column/:** Kolon kalıbı
- **wall/:** Perde kalıbı
- **layout/:** Otomatik yerleştirme algoritması

### 3.2.7 app/drawing/
Qt QGraphicsView/QGraphicsScene tabanlı 2D çizim sistemi.

### 3.2.8 app/utils/
Yardımcı fonksiyonlar:
- **logger.py:** Loglama sistemi
- **config.py:** Konfigürasyon yönetimi
- **constants.py:** Sabitler (layer adları, kategori adları, vb.)
- **exceptions.py:** Özel exception sınıfları

---

## 3.3 Önemli Dosyalar

| Dosya | Amaç |
|-------|------|
| `app/main.py` | Uygulamanın giriş noktası |
| `app/ui/main_window.py` | Ana pencere yapısı |
| `app/database/db_manager.py` | Veritabanı yöneticisi |
| `app/models/__init__.py` | Tüm modellemeleri import eder |
| `app/formwork/layout/layout_engine.py` | Otomatik yerleştirme algoritması |
| `app/drawing/canvas.py` | 2D çizim alanı |
| `app/dxf/exporter.py` | DXF export |
| `requirements.txt` | Python bağımlılıkları |
| `docs/` | Tüm dokümantasyon |

---

## 3.4 Dosya İsimlendirme Kuralları

### Python Dosyaları
- **snake_case** kullanılır: `project_manager.py`, `material_service.py`
- Modül adı sınıf adıyla ilgili: `column.py` → `Column` sınıfı

### Python Sınıfları
- **PascalCase** kullanılır: `ProjectManager`, `MaterialService`, `ColumnGeometry`

### Python Fonksiyonları ve Değişkenler
- **snake_case** kullanılır: `get_column_area()`, `total_width`

### Sabitleri
- **UPPER_CASE** kullanılır: `DEFAULT_LAYER_COLOR`, `GRID_SPACING`

### Veritabanı Tabloları
- **Tekil, snake_case:** `project`, `material`, `column`, `wall`

---

## 3.5 İçeri Aktarma (Import) Kuralları

### Doğru:
```python
# Mutlak import
from app.models import Project, Column
from app.geometry import shapes
from app.utils import logger

# Relatif import (aynı paket içinde)
from .column_geometry import ColumnGeometry
from ..utils import validators
```

### Yanlış:
```python
# Dairesel import (circular import)
from app.ui import main_window  # main_window zaten ui modülünü import ediyor

# Karmaşık relatif import
from ...app.models import Project  # Çok derin
```

---

## 3.6 .gitignore Şablonu

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
ENV/
env/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# Veritabanı
*.db
*.sqlite

# Temp files
*.tmp
temp/
.DS_Store

# Test coverage
.coverage
htmlcov/
.pytest_cache/

# Proje dosyaları (geçici)
data/temp/

# Config (kullanıcı özel)
config/settings.json
```

---

## 3.7 Klasör Oluşturma Adımları

```bash
# Temel yapı
mkdir -p app/{ui/{widgets,dialogs},database/repositories,models,geometry,materials}
mkdir -p app/{formwork/{column,wall,layout},drawing,dxf,project,services,utils}
mkdir -p tests/{unit,integration,fixtures}
mkdir -p config resources/{icons,themes} docs scripts

# Test dosyaları
touch tests/__init__.py tests/conftest.py
touch tests/unit/__init__.py tests/integration/__init__.py
touch tests/fixtures/__init__.py

# Konfigürasyon
touch config/defaults.json config/settings.json config/categories.json
touch .gitignore requirements.txt README.md
```

---

## 3.8 Modül İnit Dosyaları

Tüm Python paketlerinde `__init__.py` bulunmalıdır (boş olabilir).

**Örnek: app/models/__init__.py**
```python
"""Models package."""
from .project import Project
from .material import Material
from .column import Column
from .wall import Wall
from .element import FormworkElement

__all__ = [
    'Project',
    'Material',
    'Column',
    'Wall',
    'FormworkElement',
]
```

---

## 3.9 Dosya Organizasyonu İlkeleri

✅ **Yapılması Gerekenler:**
- Her modül bir görev yapar
- İlgili sınıflar/fonksiyonlar birlikte
- Dosya boyutu makul (500-1000 satır)
- Açık ve tutarlı isimlendirme

❌ **Yapılmaması Gerekenler:**
- Çok büyük dosyalar (2000+ satır)
- Birbiriyle ilgisiz kodlar aynı dosyada
- İç içe geçmiş 4+ seviye klasör
- Tekrar edilen kod

---

## Sonuç

Yapı:
✅ Modüler ve ölçeklenebilir
✅ Bakım kolay
✅ Yeni geliştirme kolay
✅ Test yazılması basit
✅ Gelecekte genişletilebilir
