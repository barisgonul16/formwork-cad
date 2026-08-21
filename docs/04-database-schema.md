# 4. VERİTABANI ŞEMASI

## 4.1 Veritabanı Diyagramı

```
┌──────────────┐
│   projects   │
└──────────────┘
       │
       ├──→ columns
       ├──→ walls
       └──→ drawings

┌──────────────────────┐
│ material_categories  │
└──────────────────────┘
       │
       └──→ materials

┌──────────────────────┐
│    materials         │
└──────────────────────┘
       │
       └──→ formwork_elements

┌──────────────────────┐
│    formwork_elements │
└──────────────────────┘
       │
       ├──→ columns
       ├──→ walls
       └──→ drawings

┌──────────────────────┐
│      layers          │
└──────────────────────┘
       │
       └──→ drawings
```

---

## 4.2 Tablo Tanımları

### 4.2.1 **projects** Tablosu

Proje bilgilerini saklar.

```sql
CREATE TABLE projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT 1
);
```

**Alanlar:**
- `id`: Benzersiz proje ID'si
- `name`: Proje adı (örn. "Proje 2024-01")
- `description`: Proje açıklaması
- `created_at`: Oluşturulma tarihi
- `updated_at`: Son güncelleme tarihi
- `is_active`: Aktif mi

**Örnek:**
```
1 | Proje A  | 6 katlı konut | 2026-01-15 | 2026-01-20 | 1
2 | Proje B  | Ticari bina  | 2026-02-01 | 2026-02-10 | 0
```

---

### 4.2.2 **material_categories** Tablosu

Malzeme kategorilerini saklar.

```sql
CREATE TABLE material_categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    icon TEXT,
    order_index INTEGER
);
```

**Alanlar:**
- `id`: Kategori ID'si
- `name`: Kategori adı (örn. "PANEL", "H20 KİRİŞ")
- `description`: Kategori açıklaması
- `icon`: İkon dosyası adı (ileride)
- `order_index`: Gösterim sırası

**Örnek:**
```
1  | PANEL             | Panel sistemi           | panel.png | 1
2  | H20 KİRİŞ         | H20 kiriş               | h20.png   | 2
3  | PLYWOOD           | Kontrplak               | plywood.png | 3
4  | KUŞAK             | Metal kuşak             | strap.png | 4
5  | PAYANDA           | Payanda/destek          | prop.png  | 5
6  | DİKME             | Teleskopik dikme        | post.png  | 6
7  | ANKRAJ            | Ankraj sistemleri       | anchor.png | 7
8  | BAĞLANTI ELEMANI  | Cıvata, kaynak, vb.     | conn.png  | 8
9  | DİĞER             | Diğer malzemeler        | other.png | 9
```

---

### 4.2.3 **materials** Tablosu

Malzeme kütüphanesini saklar.

```sql
CREATE TABLE materials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    manufacturer TEXT,
    category_id INTEGER NOT NULL,
    description TEXT,
    
    -- Geometrik bilgiler (mm cinsinden)
    length REAL,
    width REAL,
    height REAL,
    thickness REAL,
    
    -- Birim
    unit TEXT DEFAULT 'adet',  -- 'adet', 'metre', 'm2'
    
    -- 2D Sembol
    symbol_type TEXT,  -- 'rectangle', 'polygon', 'custom'
    symbol_data TEXT,  -- JSON formatında sembol tanımı
    
    -- Hue, Saturation, Value (HSV) renk sistemi
    color_h INTEGER DEFAULT 0,    -- 0-360
    color_s INTEGER DEFAULT 100,  -- 0-100
    color_v INTEGER DEFAULT 100,  -- 0-100
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT 1,
    
    FOREIGN KEY (category_id) REFERENCES material_categories(id)
);
```

**Alanlar:**
- `id`: Malzeme ID'si
- `code`: Malzeme kodu (örn. "PERI-PANEL-500")
- `name`: Malzeme adı
- `manufacturer`: Üretici adı (örn. "PERI", "Doka")
- `category_id`: Kategori (FK)
- `description`: Açıklama
- `length`, `width`, `height`, `thickness`: Boyutlar (mm)
- `unit`: Birim tipi
- `symbol_type`: Sembol türü
- `symbol_data`: Sembol tanımı (JSON)
- `color_h/s/v`: Çizim rengi
- `is_active`: Aktif mi

**Örnek:**
```
1 | PERI-PANEL-500 | PERI Panel 500x3200 | PERI | 1 | Panel sistemi | 500 | NULL | 3200 | NULL | m2 | rectangle | {...} | 20 | 80 | 100 | 2026-01-15 | 2026-01-15 | 1
2 | H20-STD-4000   | H20 Kiriş 4000mm    | PERI | 2 | H20 kiriş     | 4000 | 100 | 140 | 5    | metre | rectangle | {...} | 30 | 60 | 90  | 2026-01-15 | 2026-01-15 | 1
```

---

### 4.2.4 **columns** Tablosu

Projedeki kolonları saklar.

```sql
CREATE TABLE columns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    
    -- Geometrik bilgiler (mm cinsinden)
    width REAL NOT NULL,      -- Kolon genişliği
    length REAL NOT NULL,     -- Kolon uzunluğu
    height REAL NOT NULL,     -- Kolon yüksekliği
    
    -- Pozisyon
    x REAL DEFAULT 0,         -- X koordinatı
    y REAL DEFAULT 0,         -- Y koordinatı
    z REAL DEFAULT 0,         -- Kod/Seviye
    
    rotation REAL DEFAULT 0,  -- Rotasyon (derece)
    
    -- Görünüş
    front_view TEXT,          -- JSON formatında ön görünüş
    side_view TEXT,           -- JSON formatında yan görünüş
    top_view TEXT,            -- JSON formatında üst görünüş
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT 1,
    
    FOREIGN KEY (project_id) REFERENCES projects(id)
);
```

**Alanlar:**
- `project_id`: İlişkili proje
- `name`: Kolon adı (örn. "K101")
- `width`, `length`, `height`: Kolon boyutları
- `x`, `y`, `z`: Konumlandırma
- `rotation`: Dönüşüm açısı
- `*_view`: Görünüş verileri (JSON)

**Örnek:**
```
1 | 1 | K101 | 400 | 800 | 3200 | 0 | 0 | 0 | 0 | {...} | {...} | {...} | 2026-01-15 | 2026-01-15 | 1
2 | 1 | K102 | 400 | 800 | 3200 | 1200 | 0 | 0 | 0 | {...} | {...} | {...} | 2026-01-15 | 2026-01-15 | 1
```

---

### 4.2.5 **walls** Tablosu

Projedeki perdeleri saklar.

```sql
CREATE TABLE walls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    
    -- Geometrik bilgiler (mm cinsinden)
    length REAL NOT NULL,      -- Perde uzunluğu
    thickness REAL NOT NULL,   -- Perde kalınlığı (betonda)
    height REAL NOT NULL,      -- Perde yüksekliği
    
    -- Pozisyon
    start_x REAL DEFAULT 0,    -- Başlangıç X
    start_y REAL DEFAULT 0,    -- Başlangıç Y
    start_z REAL DEFAULT 0,    -- Başlangıç Kod
    
    end_x REAL DEFAULT 0,      -- Bitiş X
    end_y REAL DEFAULT 0,      -- Bitiş Y
    
    rotation REAL DEFAULT 0,   -- Rotasyon (derece)
    
    -- Görünüş
    front_view TEXT,           -- JSON formatında ön görünüş
    back_view TEXT,            -- JSON formatında arka görünüş
    top_view TEXT,             -- JSON formatında üst görünüş
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT 1,
    
    FOREIGN KEY (project_id) REFERENCES projects(id)
);
```

**Alanlar:**
- `project_id`: İlişkili proje
- `name`: Perde adı (örn. "P01")
- `length`, `thickness`, `height`: Perde boyutları
- `start_x/y/z`, `end_x/y`: Başlangıç ve bitiş koordinatları
- `*_view`: Görünüş verileri

**Örnek:**
```
1 | 1 | P01 | 6000 | 300 | 3200 | 0 | 0 | 0 | 6000 | 0 | 0 | {...} | {...} | {...} | 2026-01-15 | 2026-01-15 | 1
```

---

### 4.2.6 **formwork_elements** Tablosu

Kalıp elemanlarını (panel, kiriş, dikme vb.) saklar.

```sql
CREATE TABLE formwork_elements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    material_id INTEGER NOT NULL,
    
    -- İlişki
    parent_type TEXT,          -- 'column', 'wall', 'drawing'
    parent_id INTEGER,         -- İlişkili kolon/perde/çizim ID'si
    
    -- Pozisyon ve dönüşüm
    x REAL NOT NULL,           -- X koordinatı
    y REAL NOT NULL,           -- Y koordinatı
    z REAL DEFAULT 0,          -- Z koordinatı
    
    rotation REAL DEFAULT 0,   -- Rotasyon (derece)
    scale_x REAL DEFAULT 1.0,  -- X ölçeklendirmesi
    scale_y REAL DEFAULT 1.0,  -- Y ölçeklendirmesi
    
    -- Özellikler
    layer TEXT,                -- Layer adı (PANEL, H20, vb.)
    quantity INTEGER DEFAULT 1, -- Miktar
    notes TEXT,                -- Notlar
    
    -- Yerleştirme metodu
    placement_method TEXT,     -- 'manual', 'auto'
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT 1,
    
    FOREIGN KEY (project_id) REFERENCES projects(id),
    FOREIGN KEY (material_id) REFERENCES materials(id)
);
```

**Alanlar:**
- `material_id`: Malzeme (FK)
- `parent_type`: Ana eleman tipi (kolon, perde, vb.)
- `parent_id`: Ana eleman ID'si
- `x`, `y`, `z`: Konumlandırma
- `rotation`: Dönüşüm
- `scale_x/y`: Ölçeklendirme
- `layer`: Layer adı
- `quantity`: Adet
- `placement_method`: Manuel veya otomatik

**Örnek:**
```
1 | 1 | 1 | column | 1 | 50 | 100 | 0 | 0 | 1.0 | 1.0 | PANEL | 1 | Panel yerleştirildi | manual | 2026-01-15 | 2026-01-15 | 1
2 | 1 | 1 | column | 1 | 550 | 100 | 0 | 0 | 1.0 | 1.0 | PANEL | 1 | Panel yerleştirildi | manual | 2026-01-15 | 2026-01-15 | 1
```

---

### 4.2.7 **layers** Tablosu

Çizim katmanlarını saklar.

```sql
CREATE TABLE layers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    
    -- Görünüm
    color_h INTEGER DEFAULT 0,    -- Hue (0-360)
    color_s INTEGER DEFAULT 0,    -- Saturation (0-100)
    color_v INTEGER DEFAULT 50,   -- Value (0-100)
    
    line_width INTEGER DEFAULT 1, -- Çizgi kalınlığı (pixel)
    line_style TEXT DEFAULT 'solid', -- 'solid', 'dashed', 'dotted'
    
    -- Durumu
    is_visible BOOLEAN DEFAULT 1,  -- Görünür mü
    is_locked BOOLEAN DEFAULT 0,   -- Kilitli mi
    
    order_index INTEGER,           -- Sıra
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (project_id) REFERENCES projects(id),
    UNIQUE(project_id, name)
);
```

**Varsayılan Layers:**
- BETON (siyah)
- KALIP (mavi)
- PANEL (yeşil)
- H20 (kırmızı)
- KUŞAK (sarı)
- PAYANDA (turuncu)
- DİKME (mor)
- ÖLÇÜ (siyah, ince)
- YAZI (siyah)
- AKS (mavi, kesikli)

**Örnek:**
```
1 | 1 | PANEL   | 120 | 100 | 100 | 1 | solid | 1 | 0 | 1 | 2026-01-15 | 2026-01-15 | 1
2 | 1 | H20     | 0 | 100 | 80  | 1 | solid | 1 | 0 | 2 | 2026-01-15 | 2026-01-15 | 2
```

---

### 4.2.8 **drawings** Tablosu

Proje çizimlerini saklar.

```sql
CREATE TABLE drawings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    
    name TEXT NOT NULL,        -- Çizim adı (örn. "Kolon K101 - Ön Görünüş")
    drawing_type TEXT,         -- 'column_front', 'column_side', 'column_top', 'wall_front', vb.
    
    -- İlişki
    element_id INTEGER,        -- İlişkili kolon/perde ID'si
    
    -- Çizim verileri (JSON)
    graphics_data TEXT,        -- QGraphicsScene serialized data
    
    -- Görünüm ayarları
    scale REAL DEFAULT 1.0,    -- Zoom seviyesi
    pan_x REAL DEFAULT 0,      -- Pan X
    pan_y REAL DEFAULT 0,      -- Pan Y
    
    -- Metadata
    notes TEXT,
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT 1,
    
    FOREIGN KEY (project_id) REFERENCES projects(id)
);
```

**Örnek:**
```
1 | 1 | Kolon K101 - Ön  | column_front | 1 | {...} | 1.0 | 0 | 0 | Detaylı ön görünüş | 2026-01-15 | 2026-01-15 | 1
2 | 1 | Kolon K101 - Yan | column_side  | 1 | {...} | 1.0 | 0 | 0 | Detaylı yan görünüş | 2026-01-15 | 2026-01-15 | 1
```

---

## 4.3 SQL Sorguları

### Proje ve tüm elemanlarını getir:
```sql
SELECT p.*, 
       COUNT(DISTINCT c.id) as column_count,
       COUNT(DISTINCT w.id) as wall_count,
       COUNT(DISTINCT fe.id) as element_count
FROM projects p
LEFT JOIN columns c ON p.id = c.project_id
LEFT JOIN walls w ON p.id = w.project_id
LEFT JOIN formwork_elements fe ON p.id = fe.project_id
WHERE p.id = ?
GROUP BY p.id;
```

### Kolon için tüm kalıp elemanlarını getir:
```sql
SELECT fe.*, m.name as material_name
FROM formwork_elements fe
JOIN materials m ON fe.material_id = m.id
WHERE fe.parent_type = 'column' AND fe.parent_id = ?
ORDER BY fe.id;
```

### Kategori başına malzeme sayısı:
```sql
SELECT mc.name, COUNT(m.id) as material_count
FROM material_categories mc
LEFT JOIN materials m ON mc.id = m.category_id AND m.is_active = 1
GROUP BY mc.id
ORDER BY mc.order_index;
```

---

## 4.4 İndeksler (Performance)

```sql
-- Hızlı sorgulamalar için
CREATE INDEX idx_columns_project ON columns(project_id);
CREATE INDEX idx_walls_project ON walls(project_id);
CREATE INDEX idx_formwork_elements_project ON formwork_elements(project_id);
CREATE INDEX idx_formwork_elements_material ON formwork_elements(material_id);
CREATE INDEX idx_formwork_elements_parent ON formwork_elements(parent_type, parent_id);
CREATE INDEX idx_layers_project ON layers(project_id);
CREATE INDEX idx_drawings_project ON drawings(project_id);
CREATE INDEX idx_materials_category ON materials(category_id);
```

---

## 4.5 Veritabanı Migrasyonu

SQLAlchemy ile otomatik migration:

```python
# app/database/migration.py

from app.models import Base

def init_db(engine):
    """Create all tables"""
    Base.metadata.create_all(engine)

def drop_db(engine):
    """Drop all tables"""
    Base.metadata.drop_all(engine)
```

---

## 4.6 Veritabanı Veri Tanımı (DDL)

Tam SQL şeması: `docs/database-schema.sql` dosyasında bulunur.

---

## Sonuç

✅ Veritabanı:
- Modüler ve ölçeklenebilir
- İlişkiler doğru tanımlanmış
- İndeksler performans için ayarlanmış
- Gelecek özelliklere uygun yapı
