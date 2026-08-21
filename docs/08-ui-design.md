# 8. KULLANICI ARAYÜZÜ TASLAĞI

## 8.1 Ana Pencere Düzeni

```
┌─────────────────────────────────────────────────────────────────────┐
│  Formwork-CAD v1.0                                        [_][□][×]  │
├─────────────────────────────────────────────────────────────────────┤
│ File  Edit  View  Project  Design  Tools  Help                      │
├─────────┬───────────────────────────────────────┬────────────────┤
│         │                                       │                 │
│  [+] Pro│                                       │  Özellikler     │
│  ├─ K101│  ┌─────────────���───────────────────┐ │ ┌─────────────┐ │
│  ├─ K102│  │                                 │ │ │ Seçili Eleman
│  └─ P01 │  │  Drawing Canvas (2D)            │ │ │ ─────────────│ │
│         │  │                                 │ │ │ ID: 45      │ │
│  [+] Mat│  │  Grid: On    Snap: On           │ │ │ Tür: Panel  │ │
│  ├─ PANEL│ │                                 │ │ │ Layer: PANEL│ │
│  ├─ H20 │  │  (M) Pan + Çiz                  │ │ │ Konum:      │ │
│  └─ Payanda  │                                 │ │ │   X: 500   │ │
│         │  │                                 │ │ │   Y: 200   │ │
│  [+] Kls│  │                                 │ │ │   Z: 0     │ │
│         │  │                                 │ │ │ Dön: 0°    │ │
│         │  │                                 │ │ │            │ │
│         │  └─────────────────────────────────┘ │ └─────────────┘ │
│         │                                       │                 │
│         │  [Grid] [Zoom] [Pan] [Ölçü] [Yaz]  │ [Sil] [Düzenle] │
│         │                                       │                 │
└─────────┴───────────────────────────────────────┴────────────────┘
```

---

## 8.2 Menü Yapısı

### File Menüsü
```
┌─ File
│  ├─ Yeni Proje           (Ctrl+N)
│  ├─ Aç...                (Ctrl+O)
│  ├─ Son Projeler
│  │  ├─ Proje A
│  │  └─ Proje B
│  ├─ Kaydet               (Ctrl+S)
│  ├─ Farklı Kaydet...     (Ctrl+Shift+S)
│  ├─ ─────────────────────
│  ├─ DXF Olarak Dışa Aktar
│  ├─ DXF'den İçe Aktar    (ileride)
│  ├─ ─────────────────────
│  ├─ Proje Özelikleri
│  ├─ ─────────────────────
│  └─ Çık                  (Alt+F4)
```

### Edit Menüsü
```
┌─ Edit
│  ├─ Geri Al              (Ctrl+Z)
│  ├─ İleri Al             (Ctrl+Y)
│  ├─ ─────────────────────
│  ├─ Kes                  (Ctrl+X)
│  ├─ Kopyala              (Ctrl+C)
│  ├─ Yapıştır             (Ctrl+V)
│  ├─ ─────────────────────
│  ├─ Tümünü Seç           (Ctrl+A)
│  └─ Seçimi Kaldır        (Escape)
```

### View Menüsü
```
┌─ View
│  ├─ Yakınlaş             (Ctrl++)
│  ├─ Uzaklaş              (Ctrl+-)
│  ├─ Tümünü Göster        (Home)
│  ├─ ─────────────────────
│  ├─ Grid Göster/Gizle    (G)
│  ├─ Snap Etkin/Pasif     (S)
│  ├─ ─────────────────────
│  ├─ Katmanları Göster    (Ctrl+L)
│  ├─ Ölçüleri Göster      (D)
│  └─ Eksenleri Göster     (A)
```

### Project Menüsü
```
┌─ Project
│  ├─ Kolon Ekle           (Ctrl+Shift+C)
│  ├─ Perde Ekle           (Ctrl+Shift+W)
│  ├─ ─────────────────────
│  ├─ Kolon Özelikleri
│  ├─ Perde Özelikleri
│  └─ Tüm Elemanları Sil
```

### Design Menüsü
```
┌─ Design
│  ├─ Malzeme Kütüphanesi  (Ctrl+M)
│  ├─ ─────────────────────
│  ├─ Kolon Kalibini Otomatik Yerleştir
│  ├─ Perde Kalibini Otomatik Yerleştir
│  ├─ ─────────────────────
│  ├─ Seçili Elemanları Döndür
│  ├─ Seçili Elemanları Aynala
│  └─ Seçili Elemanları Düzenle Aralık
```

### Tools Menüsü
```
┌─ Tools
│  ├─ Seçim Aracı          (S)
│  ├─ Taşıma Aracı         (M)
│  ├─ ─────────────────────
│  ├─ Ölçü Aracı           (D)
│  ├─ Yazı Aracı           (T)
│  ├─ Çizgi Çizme Aracı    (L)
│  ├─ ─────────────────────
│  ├─ Silme Aracı          (Del)
│  └─ Ayarlar              (F12)
```

---

## 8.3 Sol Panel (Proje Ağacı)

```
┌─────────────────────────────┐
│  Proje Ağacı                │
├─────────────────────────────┤
│  📁 Proje A                 │
│    📑 Kolonlar              │
│      ├─ K101 (400×800×3200) │
│      ├─ K102 (400×800×3200) │
│      └─ [+] Yeni Kolon      │
│    📑 Perdeler              │
│      ├─ P01 (6000×300×3200) │
│      └─ [+] Yeni Perde      │
│    📑 Malzemeler            │
│      ├─ PANEL               │
│      │  ├─ Panel 500        │
│      │  ├─ Panel 1000       │
│      │  └─ [+] Yeni         │
│      ├─ H20 KİRİŞ           │
│      │  └─ H20 Std          │
│      ├─ PAYANDA             │
│      └─ [+] Yeni Kategori   │
│    📑 Çizimler              │
│      ├─ K101 - Ön Görünüş   │
│      ├─ K101 - Yan Görünüş  │
│      ├─ K101 - Üst Görünüş  │
│      └─ [+] Yeni Çizim      │
│                              │
└─────────────────────────────┘
```

**Sağ Tıkla Menüsü:**
```
K101 seçili iken:
├─ Düzenle
├─ Sil
├─ Kopyala
├─ ─────────
├─ Otomatik Yerleştir
├─ Tüm Kalıp Elemanlarını Sil
└─ Özellikleri Göster
```

---

## 8.4 Sağ Panel (Özellikler)

### Boş Seçim
```
┌──────────────────────────┐
│  Seçili Eleman Yok       │
│                          │
│  Bir eleman seçin veya   │
│  canvas'ı tıklayın.      │
│                          │
└──────────────────────────┘
```

### Kolon Seçili
```
┌──────────────────────────┐
│  Kolon: K101             │
├──────────────────────────┤
│  Özellikler              │
│  ──────────────────────  │
│  Ad:          [K101    ] │
│  Genişlik:    [400     ] │
│  Uzunluk:     [800     ] │
│  Yükseklik:   [3200    ] │
│  X Konum:     [0       ] │
│  Y Konum:     [0       ] │
│  Kod:         [0       ] │
│  ──────────────────────  │
│  [Görünüşleri Oluştur]   │
│  [Otomatik Yerleştir]    │
│  [Kalıp Elemanları Sil]  │
│                          │
└──────────────────────────┘
```

### Panel Seçili
```
┌──────────────────────────┐
│  Panel: Element #45      │
├──────────────────────────┤
│  Malzeme: PERI Panel 500 │
│  ──────────────────────  │
��  Konum                   │
│    X:         [500    ]  │
│    Y:         [200    ]  │
│    Z:         [0      ]  │
│  ──────────────────────  │
│  Dönüş:       [0°     ]  │
│  Ölçek X:     [1.0    ]  │
│  Ölçek Y:     [1.0    ]  │
│  ──────────────────────  │
│  Layer:       [PANEL  ]  │
│  Miktar:      [1      ]  │
│  Yerleştirme: [Manual ]  │
│  ──────────────────────  │
│  [Taşı] [Döndür] [Sil]   │
│                          │
└──────────────────────────┘
```

---

## 8.5 Toolbar Butonları

```
┌────────────────────────────────────────────┐
│ [Yeni]  [Aç]  [Kaydet]  │  [Geri] [İleri] │
├────────────────────────────────────────────┤
│ [✕ Seç] [→ Taşı] [↻ Döndür] [◇ Ölçü] [A Yazı]
├────────────────────────────────────────────┤
│ [Grid] [Snap] [İleri] [0°] [90°] [180°] [270°]
├────────────────────────────────────────────┤
│ Zoom: [◯-] [▦] [◯+]  │  Katmanlar [▼]
└────────────────────────────────────────────┘
```

---

## 8.6 Diyaloglar

### Yeni Proje Diyaloğu
```
┌─────────────────────────────┐
│ Yeni Proje Oluştur          │
├─────────────────────────────┤
│                             │
│ Proje Adı:                  │
│ [______________________]    │
│                             │
│ Açıklama:                   │
│ [__________              ]  │
│ [__________              ]  │
│                             │
│         [Oluştur] [İptal]   │
└─────────────────────────────┘
```

### Kolon Diyaloğu
```
┌─────────────────────────────┐
│ Kolon Ekle/Düzenle          │
├─────────────────────��───────┤
│ Kolon Adı: [K101         ]  │
│                             │
│ Boyutlar (mm)               │
│ Genişlik:   [400  ] mm      │
│ Uzunluk:    [800  ] mm      │
│ Yükseklik:  [3200 ] mm      │
│                             │
│ Konum                       │
│ X:   [0    ]  Y:  [0    ]   │
│ Kod: [0    ]                │
│                             │
│   [Tamam] [İptal] [Sil]     │
└─────────────────────────────┘
```

### Malzeme Ekle Diyaloğu
```
┌──────────────────────────────┐
│ Yeni Malzeme                 │
├──────────────────────────────┤
│ Malzeme Kodu: [PERI-P500   ] │
│ Malzeme Adı:  [Panel 500mm ] │
│ Üretici:      [PERI        ] │
│ Kategori:     [PANEL      ▼] │
│ Açıklama:                    │
│ [________________________]    │
│                              │
│ Boyutlar (mm)                │
│ Genişlik:  [500  ]  mm       │
│ Uzunluk:   [     ]  mm       │
│ Yükseklik: [3200 ]  mm       │
│ Kalınlık:  [     ]  mm       │
│                              │
│ Birim: [adet▼]               │
│                              │
│ Sembol Tipi: [rectangle▼]    │
│ Renk: [■ Yeşil] [Renk Seç]   │
│                              │
│  [Oluştur] [İptal]           │
└──────────────────────────────┘
```

### Otomatik Yerleştirme Diyaloğu
```
┌──────────────────────────────┐
│ Otomatik Yerleştirme         │
├──────────────────────────────┤
│                              │
│ Kolon: K101 (400×800×3200)   │
│                              │
│ Uygun panel kombinasyonları: │
│                              │
│ ◉ [500+500+400]  (3 panel)   │
│   Verimlilik: 99.8%          │
│   Adaptörleri: 2             │
│                              │
│ ○ [1000+1000+800]            │
│   Verimlilik: 97.5%          │
│   Adaptörleri: 1             │
│                              │
│ ○ [2000+800]                 │
│   Verimlilik: 95%            │
│   Adaptörleri: 0             │
│                              │
│   [Yerleştir] [İptal]        │
└──────────────────────────────┘
```

### DXF Export Diyaloğu
```
┌──────────────────────────────┐
│ DXF Olarak Dışa Aktar        │
├──────────────────────────────┤
│                              │
│ Dosya Adı: [kolon_k101     ] │
│ Konum:     [C:\Projeler...] │
│            [  Gözat...  ]    │
│                              │
│ Export Seçenekleri:          │
│ ☑ Beton hattını dahil et     │
│ ☑ Kalıp panellerini dahil et │
│ ☑ Kalıp desteğini dahil et   │
│ ☑ Dikme ve payandaları dahil │
│ ☑ Ölçüleri dahil et          │
│ ☑ Kat bilgilerini dahil et   │
│                              │
│ Ölçek: [1:50              ▼] │
│                              │
│   [Export] [İptal]           │
└──────────────────────────────┘
```

---

## 8.7 Durum Çubuğu (Status Bar)

```
┌────────────────────────────────────────────────────────────┐
│ Ready | Seçili: 3 eleman | Zoom: 100% | Grid: 50mm | Snap: On
└────────────────────────────────────────────────────────────┘
```

---

## 8.8 Renk Şeması

### Varsayılan Renkler
```
- BETON:        Siyah (#000000)
- KALIP:        Mavi (#0000FF)
- PANEL:        Yeşil (#00C800)
- H20:          Kırmızı (#FF0000)
- KUŞAK:        Sarı (#FFFF00)
- PAYANDA:      Turuncu (#FFA500)
- DİKME:        Mor (#A020F0)
- ÖLÇÜ:         Siyah (#000000), kesikli
- YAZI:         Siyah (#000000)
- AKS:          Mavi (#0000FF), kesikli
- Arka Plan:    Açık Gri (#E0E0E0)
- Grid:         Açık Gri (#C8C8C8)
```

---

## 8.9 Kısayol Tuşları

| Tuş | İşlem |
|-----|-------|
| Ctrl+N | Yeni Proje |
| Ctrl+O | Aç |
| Ctrl+S | Kaydet |
| Ctrl+Z | Geri Al |
| Ctrl+Y | İleri Al |
| Ctrl+A | Tümünü Seç |
| Ctrl+M | Malzeme Kütüphanesi |
| Ctrl++ | Yakınlaş |
| Ctrl+- | Uzaklaş |
| Home | Tümünü Göster |
| G | Grid Göster/Gizle |
| S | Snap Etkin/Pasif |
| D | Ölçüleri Göster |
| A | Eksenleri Göster |
| Delete | Seçiyi Sil |
| Escape | Seçimi Kaldır |
| R | Seçiliyi Döndür |
| M | Taşı Aracı |
| Orta MB | Pan |

---

## 8.10 Responsif Tasarım

- **Minimum Pencere:** 1024×768
- **Önerilen:** 1600×900
- **Sol Panel:** Genişlik ≥ 200px
- **Sağ Panel:** Genişlik 300-400px (ayarlanabilir)
- **Canvas:** Kalan alan

---

## 8.11 Tema Desteği (İleride)

```python
# app/ui/themes/dark.qss

QMainWindow {
    background-color: #2b2b2b;
    color: #ffffff;
}

QPushButton {
    background-color: #0d47a1;
    color: #ffffff;
    border-radius: 4px;
    padding: 6px 12px;
}

QPushButton:hover {
    background-color: #1565c0;
}
```

---

## Sonuç

✅ UI Tasarımı:
- Profesyonel ve mühendislik yazılımı tarzı
- Intuitive kullanıcı deneyimi
- Tüm temel işlevlere kolay erişim
- Keyboard shortcuts desteği
- Responsive layout
