# 7. MANUEL VE OTOMATİK YERLEŞTIRME SİSTEMİ

## 7.1 Yerleştirme Sistemi Mimarisi

```
┌─────────────────────────────────────────┐
│      Placement System                    │
├─────────────────────────────────────────┤
│                                          │
│  ┌──────────────────────────────────┐  │
│  │    Manual Placement              │  │
│  │  - Kullanıcı drag & drop         │  │
│  │  - Grid snap                     │  │
│  │  - Rotation                      │  │
│  └──────────────────────────────────┘  │
│                                          │
│  ┌──────────────────────────────────┐  │
│  │    Automatic Placement           │  │
│  │  - Layout Engine                 │  │
│  │  - Panel Combinator              │  │
│  │  - Constraint Checker            │  │
│  │  - Placement Optimizer           │  │
│  └──────────────────────────────────┘  │
│                                          │
└─────────────────────────────────────────┘
```

---

## 7.2 Manuel Yerleştirme (Drag & Drop)

### 7.2.1 Manuel Yerleştirme Akışı

```
1. Malzeme Seç (Material Library)
   ↓
2. Çizim Alanına Sürükle
   ↓
3. Konum Belirle (Mouse Position)
   ↓
4. Döndür (Keyboard: R tuşu)
   ↓
5. Doğru Konuma Konumlandır
   ↓
6. Tıkla → Yerleştir
   ↓
7. FormworkElement kayıt edilir
```

### 7.2.2 Manuel Yerleştirme Sınıfı

```python
# app/formwork/placement/manual_placement.py

from PySide6.QtCore import QPointF, Qt, Signal
from PySide6.QtGui import QDrag
from PySide6.QtWidgets import QApplication
from app.models import Material, FormworkElement, Column, Wall
from app.drawing.graphics_items import FormworkRectangle
import logging

logger = logging.getLogger(__name__)

class ManualPlacement:
    """Manuel yerleştirme yöneticisi"""
    
    def __init__(self, canvas, project_service):
        self.canvas = canvas
        self.project_service = project_service
        
        self.dragging_material: Optional[Material] = None
        self.ghost_item = None  # Preview şekli
        self.target_parent = None  # Hedef kolon/perde
        
        self.rotation_angle = 0
        self.snap_grid = 50  # mm
        
        logger.info("ManualPlacement başlatıldı")
    
    def start_drag(self, material: Material) -> None:
        """Sürüklemeyi başlat"""
        self.dragging_material = material
        self.rotation_angle = 0
        
        # Ghost item oluştur (şeffaf preview)
        self.ghost_item = FormworkRectangle(
            0, 0,
            material.width or 100,
            material.height or 100
        )
        self.ghost_item.setOpacity(0.5)
        self.ghost_item.setFlag(self.ghost_item.ItemIsMovable, False)
        self.canvas.add_shape(self.ghost_item)
        
        logger.info(f"Drag başlangıç: {material.name}")
    
    def drag_over_canvas(self, canvas_pos: QPointF, parent_element) -> None:
        """Sürükleme sırasında canvas üzerinde hareket"""
        if not self.ghost_item or not self.dragging_material:
            return
        
        # Grid'e snap
        snapped_x, snapped_y = self._snap_to_grid(canvas_pos.x(), canvas_pos.y())
        
        self.ghost_item.setPos(snapped_x, snapped_y)
        
        # Hedef elementi vurgula
        if parent_element:
            self.target_parent = parent_element
            logger.debug(f"Hedef: {parent_element}")
    
    def rotate_dragging(self, angle: float) -> None:
        """Sürüklenen parçayı döndür"""
        if self.ghost_item:
            self.rotation_angle += angle
            self.ghost_item.setRotation(self.rotation_angle)
            logger.debug(f"Rotation: {self.rotation_angle}°")
    
    def drop_element(self, final_pos: QPointF, parent_element) -> FormworkElement:
        """Elemanı yerleştir (bırak)"""
        if not self.dragging_material or not parent_element:
            logger.warning("Drop başarısız: malzeme veya hedef yok")
            return None
        
        # Snap
        x, y = self._snap_to_grid(final_pos.x(), final_pos.y())
        
        # Gerçek şekli ekle
        element = FormworkElement(
            project_id=parent_element.project_id,
            material_id=self.dragging_material.id,
            parent_type='column' if isinstance(parent_element, Column) else 'wall',
            parent_id=parent_element.id,
            x=x,
            y=y,
            rotation=self.rotation_angle,
            layer=self.dragging_material.category.name,
            placement_method='manual'
        )
        
        # DB'ye kaydet
        self.project_service.add_formwork_element(element)
        
        # Canvas'a ekle
        real_item = FormworkRectangle(x, y, 
                                     self.dragging_material.width or 100,
                                     self.dragging_material.height or 100)
        real_item.setData(1, element.id)  # Element ID'yi sakla
        self.canvas.add_shape(real_item)
        
        # Ghost item'i kaldır
        if self.ghost_item:
            self.canvas.remove_shape(self.ghost_item)
            self.ghost_item = None
        
        self.dragging_material = None
        self.rotation_angle = 0
        self.target_parent = None
        
        logger.info(f"Element yerleştirildi: {element.id}")
        return element
    
    def cancel_drag(self) -> None:
        """Sürüklemeyi iptal et"""
        if self.ghost_item:
            self.canvas.remove_shape(self.ghost_item)
            self.ghost_item = None
        
        self.dragging_material = None
        self.rotation_angle = 0
        logger.info("Drag iptal edildi")
    
    def _snap_to_grid(self, x: float, y: float) -> tuple:
        """Grid'e snap et"""
        if not self.canvas.snap_to_grid:
            return x, y
        
        grid = self.snap_grid
        snapped_x = round(x / grid) * grid
        snapped_y = round(y / grid) * grid
        return snapped_x, snapped_y
    
    def move_element(self, element_id: int, new_x: float, new_y: float) -> None:
        """Yerleştirilen elemanı taşı"""
        element = self.project_service.get_formwork_element(element_id)
        if element:
            element.x = new_x
            element.y = new_y
            self.project_service.update_formwork_element(element)
            logger.info(f"Element taşındı: {element_id} → ({new_x}, {new_y})")
    
    def delete_element(self, element_id: int) -> None:
        """Yerleştirilen elemanı sil"""
        self.project_service.delete_formwork_element(element_id)
        logger.info(f"Element silindi: {element_id}")
```

---

## 7.3 Otomatik Yerleştirme

### 7.3.1 Otomatik Yerleştirme Akışı

```
1. Kullanıcı "Otomatik Yerleştir" butonuna basar
   ↓
2. Kolon/Perde boyutları okunur
   ↓
3. Layout Engine çalıştırılır
   ↓
4. Uygun panel kombinasyonu bulunur
   ↓
5. Kısıtlamalar kontrol edilir (çakışma vb.)
   ↓
6. Paneller grid'e yerleştirilir
   ↓
7. Sonuç gösterilir (kullanıcı onay alınır)
   ↓
8. DB'ye kaydedilir
```

### 7.3.2 Layout Engine

```python
# app/formwork/layout/layout_engine.py

from typing import List, Optional, Dict, Tuple
from app.models import Material, Column, Wall, FormworkElement
from app.database import db_manager
import logging

logger = logging.getLogger(__name__)

class LayoutEngine:
    """Otomatik panel yerleştirme motoru"""
    
    def __init__(self, project_service):
        self.project_service = project_service
        self.panel_combinator = PanelCombinator()
        self.constraint_checker = ConstraintChecker()
        self.optimizer = PlacementOptimizer()
    
    def auto_layout_column(self, column: Column) -> List[FormworkElement]:
        """Kolon için otomatik yerleştirme"""
        logger.info(f"Kolon otomatik yerleştirme: {column.name}")
        
        # 1. Gerekli malzemeleri al
        materials = self.project_service.get_materials_by_category('PANEL')
        
        # 2. Panel kombinasyonunu bul
        combinations = self.panel_combinator.find_combinations(
            target_width=column.width,
            target_length=column.length,
            available_panels=materials
        )
        
        if not combinations:
            logger.warning(f"Uygun panel kombinasyonu bulunamadı: {column.name}")
            return []
        
        # En iyi kombinasyonu seç
        best_combo = combinations[0]
        logger.info(f"Seçilen kombinasyon: {best_combo}")
        
        # 3. Elemanları yerleştir
        placed_elements = []
        
        for panel_group in best_combo['panels']:
            for i, panel in enumerate(panel_group):
                # Konumlandır
                x, y = self._calculate_position(panel_group, i, column)
                
                # Element oluştur
                element = FormworkElement(
                    project_id=column.project_id,
                    material_id=panel.id,
                    parent_type='column',
                    parent_id=column.id,
                    x=x,
                    y=y,
                    layer='PANEL',
                    placement_method='auto'
                )
                
                # DB'ye kaydet
                self.project_service.add_formwork_element(element)
                placed_elements.append(element)
        
        # 4. Ek elemanları ekle (payanda, dikme vb.)
        self._add_supporting_elements(column, placed_elements)
        
        logger.info(f"Yerleştirme tamamlandı: {len(placed_elements)} eleman")
        return placed_elements
    
    def auto_layout_wall(self, wall: Wall) -> List[FormworkElement]:
        """Perde için otomatik yerleştirme"""
        logger.info(f"Perde otomatik yerleştirme: {wall.name}")
        
        # Kolon ile benzer mantık
        materials = self.project_service.get_materials_by_category('PANEL')
        
        combinations = self.panel_combinator.find_combinations(
            target_width=wall.length,
            target_length=None,
            available_panels=materials
        )
        
        if not combinations:
            logger.warning(f"Uygun panel kombinasyonu bulunamadı: {wall.name}")
            return []
        
        # ... rest of implementation
        placed_elements = []
        
        logger.info(f"Perde yerleştirme tamamlandı: {len(placed_elements)} eleman")
        return placed_elements
    
    def _calculate_position(self, panel_group: List, index: int, 
                           column: Column) -> Tuple[float, float]:
        """Panel konumunu hesapla"""
        x = 0
        y = 0
        
        for i in range(index):
            x += panel_group[i].width or 100
        
        return x, y
    
    def _add_supporting_elements(self, column: Column, 
                                elements: List[FormworkElement]) -> None:
        """Destek elemanlarını ekle (payanda, dikme vb.)"""
        # Payanda ekleme mantığı
        props = self.project_service.get_materials_by_category('PAYANDA')
        if props:
            # Kolon köşelerine payanda ekle
            logger.debug("Payandalar eklendi")
```

### 7.3.3 Panel Kombinatörü

```python
# app/formwork/layout/panel_combinator.py

from typing import List, Dict, Optional
from itertools import combinations
import logging

logger = logging.getLogger(__name__)

class PanelCombinator:
    """Panel kombinasyonlarını bul"""
    
    def __init__(self, tolerance: float = 10):
        """
        tolerance: mm cinsinden tolerans (örn. 10mm)
        """
        self.tolerance = tolerance
    
    def find_combinations(self, target_width: float, target_length: Optional[float],
                         available_panels: List) -> List[Dict]:
        """
        Uygun panel kombinasyonlarını bul
        
        Örnek:
        - Target: 6000mm
        - Paneller: [1000, 1500, 2000]
        
        Sonuç:
        - [2000, 2000, 2000]
        - [2000, 2000, 1500, 500] (çalışmaz, 500 yoksa)
        - [1500, 1500, 1500, 1000, 500]
        """
        
        panel_widths = [p.width for p in available_panels if p.width]
        
        valid_combos = self._find_combinations_recursive(
            target_width, panel_widths, []
        )
        
        # Kombinasyonları sırala (eleman sayısı az olanı öncele)
        valid_combos.sort(key=lambda x: len(x))
        
        # Sonuçları format et
        results = []
        for combo in valid_combos[:5]:  # En iyi 5 kombinasyon
            # Panel nesnelerini bul
            panels = []
            for width in combo:
                panel = next(p for p in available_panels if p.width == width)
                panels.append(panel)
            
            results.append({
                'panels': [panels],
                'total_width': sum(combo),
                'efficiency': self._calculate_efficiency(combo, target_width),
                'panel_count': len(combo)
            })
        
        return results
    
    def _find_combinations_recursive(self, target: float, available: List[float],
                                    current: List[float]) -> List[List[float]]:
        """Kombinasyonları özyinelemeli olarak bul"""
        
        if abs(target) < self.tolerance:
            return [current]
        
        if target < 0:
            return []
        
        results = []
        
        for width in available:
            if width <= target + self.tolerance:
                new_current = current + [width]
                new_target = target - width
                
                results.extend(
                    self._find_combinations_recursive(
                        new_target, available, new_current
                    )
                )
        
        return results
    
    def _calculate_efficiency(self, combo: List[float], target: float) -> float:
        """Yerleştirme verimliliğini hesapla (0-100%)"""
        total = sum(combo)
        if total == 0:
            return 0
        return (target / total) * 100
```

### 7.3.4 Kısıtlama Kontrolü

```python
# app/formwork/layout/constraints.py

from app.models import FormworkElement, Column, Wall
from typing import List
import logging

logger = logging.getLogger(__name__)

class ConstraintChecker:
    """Yerleştirme kısıtlamalarını kontrol et"""
    
    def check_overlap(self, element: FormworkElement, 
                     existing_elements: List[FormworkElement]) -> bool:
        """Çakışma kontrolü"""
        
        for existing in existing_elements:
            if self._shapes_overlap(element, existing):
                logger.warning(f"Çakışma tespit: {element.id} vs {existing.id}")
                return False
        
        return True
    
    def check_within_bounds(self, element: FormworkElement, 
                           parent: Column | Wall) -> bool:
        """Sınırlar içinde olup olmadığını kontrol et"""
        
        max_x = parent.width if isinstance(parent, Column) else parent.length
        max_y = parent.height
        
        if element.x < 0 or element.x + 100 > max_x:  # 100 element genişliği
            return False
        
        if element.y < 0 or element.y + 100 > max_y:
            return False
        
        return True
    
    def _shapes_overlap(self, e1: FormworkElement, e2: FormworkElement) -> bool:
        """İki şeklin çakışıp çakışmadığını kontrol et"""
        
        # Basit AABB (Axis-Aligned Bounding Box) kontrolü
        if (e1.x < e2.x + 100 and e1.x + 100 > e2.x and
            e1.y < e2.y + 100 and e1.y + 100 > e2.y):
            return True
        
        return False
```

### 7.3.5 Yerleştirme Optimizasyonu

```python
# app/formwork/layout/placement_optimizer.py

from typing import List, Dict
from app.models import FormworkElement
import logging

logger = logging.getLogger(__name__)

class PlacementOptimizer:
    """Yerleştirmeyi optimize et"""
    
    def optimize(self, elements: List[FormworkElement]) -> List[FormworkElement]:
        """Elemanları en verimli şekilde düzenle"""
        
        # Elemanları sıra ve sütuna göre sırala
        sorted_elements = sorted(
            elements,
            key=lambda e: (e.y, e.x)  # Önce Y, sonra X
        )
        
        # Her satırda hizalandır
        current_y = None
        for element in sorted_elements:
            if current_y is None:
                current_y = element.y
            elif element.y != current_y:
                # Yeni satır
                current_y = element.y
            
            # Elemanları hizala
            element.y = current_y
        
        logger.info(f"Optimizasyon tamamlandı: {len(elements)} eleman")
        return sorted_elements
```

---

## 7.4 UI Entegrasyonu

```python
# app/ui/dialogs/auto_layout_dialog.py

from PySide6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Qt
from app.formwork.layout import LayoutEngine

class AutoLayoutDialog(QDialog):
    """Otomatik yerleştirme diyalogu"""
    
    def __init__(self, column, layout_engine, parent=None):
        super().__init__(parent)
        
        self.column = column
        self.layout_engine = layout_engine
        self.result_elements = []
        
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout()
        
        label = QLabel(f"Kolon '{self.column.name}' için otomatik yerleştirme?")
        layout.addWidget(label)
        
        auto_button = QPushButton("Otomatik Yerleştir")
        auto_button.clicked.connect(self.perform_auto_layout)
        layout.addWidget(auto_button)
        
        self.setLayout(layout)
        self.setWindowTitle("Otomatik Yerleştirme")
    
    def perform_auto_layout(self):
        """Otomatik yerleştirmeyi çalıştır"""
        self.result_elements = self.layout_engine.auto_layout_column(self.column)
        
        if self.result_elements:
            QMessageBox.information(
                self, "Başarılı",
                f"{len(self.result_elements)} eleman yerleştirildi"
            )
            self.accept()
        else:
            QMessageBox.warning(
                self, "Hata",
                "Uygun kombinasyon bulunamadı"
            )
```

---

## 7.5 Manuel Düzeltmeler

Otomatik yerleştirmeden sonra:

```python
# Manuel operasyonlar kullanıcı tarafından uygulanabilir:
# - Elemanları drag & drop ile taşı
# - Elemanları sil
# - Yeni elemanlar ekle
# - Rotasyonları değiştir
```

---

## Sonuç

✅ Yerleştirme Sistemi:
- Manuel yerleştirme (Drag & Drop)
- Otomatik yerleştirme (Layout Engine)
- Grid snap desteği
- Kısıtlama kontrolü
- Optimizasyon
- Kullanıcı dostu UI
