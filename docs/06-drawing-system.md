# 6. 2D ÇİZİM SİSTEMİ

## 6.1 Mimari Bakış

2D çizim sistemi Qt's QGraphicsView + QGraphicsScene mimarisi üzerine kurulmuştur.

```
┌────────────────────────────────────────┐
│         MainWindow (UI)                 │
├────────────────────────────────────────┤
│  ToolBar | DrawingCanvas (QGraphicsView)│
│          │                              │
│  LeftPanel│  ┌──────────────────────┐  │
│          │  │  QGraphicsScene      │  │
│  RightPanel │  - Shapes (Rect, Poly) │  │
│          │  │  - Lines, Text        │  │
│          │  │  - Groups             │  │
│          │  └──────────────────────┘  │
│          │                              │
└────────────────────────────────────────┘
         ↓
  ViewPort Transformations
  (Zoom, Pan, Rotate)
```

---

## 6.2 Canvas Sınıfı

```python
# app/drawing/canvas.py

from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsItem
from PySide6.QtCore import Qt, Signal, QPointF, QRectF
from PySide6.QtGui import QPainter, QPen, QBrush, QColor
from typing import List, Optional
import logging

logger = logging.getLogger(__name__)

class DrawingCanvas(QGraphicsView):
    """2D çizim alanı"""
    
    # Sinyaller
    item_selected = Signal(QGraphicsItem)
    item_moved = Signal(QGraphicsItem, QPointF)
    scene_changed = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Scene oluştur
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        
        # Görünüm ayarları
        self.setRenderHint(QPainter.Antialiasing)
        self.setRenderHint(QPainter.SmoothPixmapTransform)
        
        # Grid ayarları
        self.grid_enabled = True
        self.grid_spacing = 50  # pixel
        self.snap_to_grid = True
        
        # Zoom ayarları
        self.zoom_factor = 1.0
        self.min_zoom = 0.1
        self.max_zoom = 5.0
        
        # Pan ayarları
        self.pan_mode = False
        self.last_pan_point = QPointF()
        
        # Seçim ayarları
        self.selected_items = []
        
        # Katman yönetimi
        self.layer_manager = None
        
        # Ölçü ayarları
        self.measure_mode = False
        self.measure_points = []
        
        logger.info("DrawingCanvas oluşturuldu")
    
    def drawBackground(self, painter: QPainter, rect: QRectF) -> None:
        """Arka plan çiz (grid)"""
        super().drawBackground(painter, rect)
        
        if not self.grid_enabled:
            return
        
        painter.setPen(QPen(QColor(200, 200, 200), 0))
        
        # Yatay çizgiler
        left = int(rect.left()) - (int(rect.left()) % self.grid_spacing)
        right = int(rect.right())
        
        y = int(rect.top()) - (int(rect.top()) % self.grid_spacing)
        while y <= right:
            painter.drawLine(left, y, right, y)
            y += self.grid_spacing
        
        # Dikey çizgiler
        top = int(rect.top()) - (int(rect.top()) % self.grid_spacing)
        bottom = int(rect.bottom())
        
        x = int(rect.left()) - (int(rect.left()) % self.grid_spacing)
        while x <= right:
            painter.drawLine(x, top, x, bottom)
            x += self.grid_spacing
    
    def zoom_in(self, factor: float = 1.2) -> None:
        """Yakınlaş"""
        if self.zoom_factor * factor <= self.max_zoom:
            self.scale(factor, factor)
            self.zoom_factor *= factor
            logger.debug(f"Zoom: {self.zoom_factor:.2f}")
    
    def zoom_out(self, factor: float = 1.2) -> None:
        """Uzaklaş"""
        if self.zoom_factor / factor >= self.min_zoom:
            self.scale(1/factor, 1/factor)
            self.zoom_factor /= factor
            logger.debug(f"Zoom: {self.zoom_factor:.2f}")
    
    def zoom_fit(self) -> None:
        """Tümünü göster"""
        self.fitInView(self.scene.itemsBoundingRect(), Qt.KeepAspectRatio)
        self.zoom_factor = 1.0
        logger.info("Zoom fit")
    
    def pan_start(self, point: QPointF) -> None:
        """Pan başlat"""
        self.pan_mode = True
        self.last_pan_point = point
    
    def pan_move(self, point: QPointF) -> None:
        """Pan taşı"""
        if not self.pan_mode:
            return
        
        delta = point - self.last_pan_point
        self.translate(delta.x(), delta.y())
        self.last_pan_point = point
    
    def pan_end(self) -> None:
        """Pan bitir"""
        self.pan_mode = False
    
    def add_shape(self, shape: QGraphicsItem) -> None:
        """Scene'e şekil ekle"""
        self.scene.addItem(shape)
        self.scene_changed.emit()
    
    def remove_shape(self, shape: QGraphicsItem) -> None:
        """Scene'den şekil sil"""
        self.scene.removeItem(shape)
        self.scene_changed.emit()
    
    def clear_scene(self) -> None:
        """Scene'i temizle"""
        self.scene.clear()
        self.selected_items = []
        self.scene_changed.emit()
    
    def select_item(self, item: QGraphicsItem, multiple: bool = False) -> None:
        """Şekil seç"""
        if not multiple:
            for item in self.selected_items:
                item.setSelected(False)
            self.selected_items = []
        
        item.setSelected(True)
        self.selected_items.append(item)
        self.item_selected.emit(item)
    
    def get_selected_items(self) -> List[QGraphicsItem]:
        """Seçili şekilleri getir"""
        return self.selected_items
    
    def toggle_grid(self) -> None:
        """Grid görünürlüğünü değiştir"""
        self.grid_enabled = not self.grid_enabled
        self.viewport().update()
    
    def mousePressEvent(self, event) -> None:
        """Mouse basılı tutma"""
        if event.button() == Qt.MiddleButton:
            self.pan_start(event.position())
        else:
            super().mousePressEvent(event)
    
    def mouseMoveEvent(self, event) -> None:
        """Mouse hareket"""
        if self.pan_mode:
            self.pan_move(event.position())
        else:
            super().mouseMoveEvent(event)
    
    def mouseReleaseEvent(self, event) -> None:
        """Mouse bırakılması"""
        if event.button() == Qt.MiddleButton:
            self.pan_end()
        else:
            super().mouseReleaseEvent(event)
    
    def wheelEvent(self, event) -> None:
        """Mouse tekerleği (zoom)"""
        if event.angleDelta().y() > 0:
            self.zoom_in(1.1)
        else:
            self.zoom_out(1.1)
```

---

## 6.3 Grafik Elemanları

```python
# app/drawing/graphics_items.py

from PySide6.QtWidgets import QGraphicsRectItem, QGraphicsPolygonItem, QGraphicsLineItem
from PySide6.QtGui import QPen, QBrush, QColor
from PySide6.QtCore import QRectF, QPointF, Qt
from typing import Optional

class FormworkRectangle(QGraphicsRectItem):
    """Kalıp paneli (dikdörtgen)"""
    
    def __init__(self, x: float, y: float, width: float, height: float, 
                 color: QColor = QColor(100, 150, 200)):
        super().__init__(x, y, width, height)
        
        self.setPen(QPen(QColor(0, 0, 0), 2))
        self.setBrush(QBrush(color))
        self.setAcceptHoverEvents(True)
        self.setFlag(self.ItemIsSelectable)
        self.setFlag(self.ItemIsMovable)
        self.setData(0, "FormworkRectangle")
    
    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.setZValue(self.zValue() + 1)
    
    def hoverEnterEvent(self, event):
        self.setPen(QPen(QColor(255, 0, 0), 3))
    
    def hoverLeaveEvent(self, event):
        self.setPen(QPen(QColor(0, 0, 0), 2))


class MeasurementLine(QGraphicsLineItem):
    """Ölçü çizgisi"""
    
    def __init__(self, x1: float, y1: float, x2: float, y2: float, 
                 label: str = ""):
        super().__init__(x1, y1, x2, y2)
        
        self.setPen(QPen(QColor(0, 0, 0), 1, Qt.DashLine))
        self.label = label
        self.setData(0, "MeasurementLine")
    
    def get_length(self) -> float:
        """Uzunluğu hesapla"""
        x1 = self.line().x1()
        y1 = self.line().y1()
        x2 = self.line().x2()
        y2 = self.line().y2()
        
        import math
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


class FormworkGroup(QGraphicsItem):
    """Kalıp elemanları grubu"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.children = []
        self.setAcceptHoverEvents(True)
        self.setFlag(self.ItemIsSelectable)
        self.setData(0, "FormworkGroup")
    
    def add_item(self, item):
        """Gruba öğe ekle"""
        self.children.append(item)
        item.setParentItem(self)
    
    def boundingRect(self):
        """Sınırlayıcı dikdörtgen"""
        if not self.children:
            return QRectF()
        
        rect = self.children[0].boundingRect()
        for child in self.children[1:]:
            rect = rect.united(child.boundingRect())
        return rect
    
    def paint(self, painter, option, widget=None):
        """Boşluk (children görünür)"""
        pass
```

---

## 6.4 Layer Yönetimi

```python
# app/drawing/layer_manager.py

from typing import Dict, List, Optional
from PySide6.QtGui import QColor
import logging

logger = logging.getLogger(__name__)

class LayerManager:
    """Çizim katmanlarını yönet"""
    
    def __init__(self):
        self.layers: Dict[str, Layer] = {}
        self._init_default_layers()
    
    def _init_default_layers(self) -> None:
        """Varsayılan katmanları oluştur"""
        layer_defs = {
            'BETON': {'color': QColor(0, 0, 0), 'visible': True},
            'KALIP': {'color': QColor(0, 0, 255), 'visible': True},
            'PANEL': {'color': QColor(0, 200, 0), 'visible': True},
            'H20': {'color': QColor(255, 0, 0), 'visible': True},
            'KUŞAK': {'color': QColor(255, 255, 0), 'visible': True},
            'PAYANDA': {'color': QColor(255, 165, 0), 'visible': True},
            'DİKME': {'color': QColor(160, 32, 240), 'visible': True},
            'ÖLÇÜ': {'color': QColor(0, 0, 0), 'visible': True},
            'YAZI': {'color': QColor(0, 0, 0), 'visible': True},
            'AKS': {'color': QColor(0, 0, 255), 'visible': True},
        }
        
        for name, props in layer_defs.items():
            self.add_layer(name, props['color'], props['visible'])
    
    def add_layer(self, name: str, color: QColor, visible: bool = True) -> None:
        """Yeni katman ekle"""
        self.layers[name] = {
            'color': color,
            'visible': visible,
            'locked': False,
        }
        logger.info(f"Katman eklendi: {name}")
    
    def remove_layer(self, name: str) -> None:
        """Katman sil"""
        if name in self.layers:
            del self.layers[name]
            logger.info(f"Katman silindi: {name}")
    
    def toggle_visibility(self, name: str) -> None:
        """Katman görünürlüğünü değiştir"""
        if name in self.layers:
            self.layers[name]['visible'] = not self.layers[name]['visible']
    
    def get_layer_color(self, name: str) -> Optional[QColor]:
        """Katman rengini getir"""
        if name in self.layers:
            return self.layers[name]['color']
        return None
    
    def get_all_layers(self) -> List[str]:
        """Tüm katmanları getir"""
        return list(self.layers.keys())
```

---

## 6.5 Araçlar (Tools)

```python
# app/drawing/tools.py

from enum import Enum
from PySide6.QtCore import QPointF, Qt

class DrawingTool(Enum):
    """Çizim araçları"""
    SELECT = 1
    MOVE = 2
    ROTATE = 3
    COPY = 4
    DELETE = 5
    ZOOM = 6
    PAN = 7
    MEASURE = 8
    DRAW_RECTANGLE = 9
    DRAW_LINE = 10
    DRAW_POLYGON = 11
    TEXT = 12
    MIRROR = 13


class Tool:
    """Temel tool sınıfı"""
    
    def __init__(self, canvas):
        self.canvas = canvas
        self.active = False
    
    def activate(self) -> None:
        """Tool aktivleş"""
        self.active = True
    
    def deactivate(self) -> None:
        """Tool pasifleş"""
        self.active = False
    
    def on_mouse_press(self, point: QPointF) -> None:
        """Mouse basılı"""
        pass
    
    def on_mouse_move(self, point: QPointF) -> None:
        """Mouse hareket"""
        pass
    
    def on_mouse_release(self, point: QPointF) -> None:
        """Mouse bırakılması"""
        pass


class SelectTool(Tool):
    """Seçim aracı"""
    
    def on_mouse_press(self, point: QPointF) -> None:
        item = self.canvas.itemAt(point)
        if item:
            self.canvas.select_item(item)


class MeasureTool(Tool):
    """Ölçü aracı"""
    
    def __init__(self, canvas):
        super().__init__(canvas)
        self.start_point = None
    
    def on_mouse_press(self, point: QPointF) -> None:
        self.start_point = point
    
    def on_mouse_release(self, point: QPointF) -> None:
        if self.start_point:
            # Ölçü çizgisi ekle
            from .graphics_items import MeasurementLine
            distance = ((point.x() - self.start_point.x())**2 + 
                       (point.y() - self.start_point.y())**2)**0.5
            
            line = MeasurementLine(
                self.start_point.x(), self.start_point.y(),
                point.x(), point.y(),
                label=f"{distance:.0f}mm"
            )
            self.canvas.add_shape(line)
            self.start_point = None


class DeleteTool(Tool):
    """Silme aracı"""
    
    def on_mouse_press(self, point: QPointF) -> None:
        item = self.canvas.itemAt(point)
        if item:
            self.canvas.remove_shape(item)
```

---

## 6.6 Çizim İşlem Seçenekleri

### Zoom İşlemleri:
- Fare tekerleği: Yakınlaş/Uzaklaş
- Ctrl + Fare: Daha hassas zoom
- "Tümünü Göster" butonunu: Fit to view

### Pan İşlemleri:
- Orta fare butonu + hareket: Pan
- Boşluk tuşu + hareket: Pan

### Seçim:
- Tek tıklama: Bir şekil seç
- Ctrl + Tıklama: Birden fazla seç
- Sürükleme: Kutu seçimi

### Transformasyon:
- Seçili + sürükleme: Taşı
- Seçili + Shift: Döndür
- Seçili + Ctrl: Kopyala
- Seçili + Delete: Sil

---

## 6.7 Koordinat Sistemi

```python
# app/drawing/coordinates.py

from typing import Tuple
from PySide6.QtCore import QPointF

class CoordinateConverter:
    """Gerçek dünya koordinatlarını canvas'a dönüştür"""
    
    def __init__(self, scale: float = 1.0):
        """
        scale: 1 mm = ? pixel
        """
        self.scale = scale  # mm -> pixel
        self.origin_x = 0
        self.origin_y = 0
    
    def to_canvas(self, x_mm: float, y_mm: float) -> Tuple[float, float]:
        """mm'den pixel'e dönüştür"""
        canvas_x = x_mm * self.scale + self.origin_x
        canvas_y = y_mm * self.scale + self.origin_y
        return canvas_x, canvas_y
    
    def from_canvas(self, canvas_x: float, canvas_y: float) -> Tuple[float, float]:
        """Pixel'den mm'ye dönüştür"""
        x_mm = (canvas_x - self.origin_x) / self.scale
        y_mm = (canvas_y - self.origin_y) / self.scale
        return x_mm, y_mm
```

---

## 6.8 Çizim Durumu

```python
# app/drawing/state.py

class DrawingState:
    """Çizim durumunu tut"""
    
    def __init__(self):
        self.is_modified = False
        self.current_layer = "PANEL"
        self.current_tool = None
        self.grid_enabled = True
        self.snap_to_grid = True
        self.show_axes = True
        self.show_dimensions = True
    
    def mark_modified(self) -> None:
        """Değiştirildi işareti"""
        self.is_modified = True
    
    def mark_saved(self) -> None:
        """Kaydedildi işareti"""
        self.is_modified = False
```

---

## Sonuç

✅ 2D Çizim Sistemi:
- Qt QGraphicsView/Scene tabanlı
- Zoom, Pan, Seçim, Taşıma işlevleri
- Layer yönetimi
- Araç sistemi (modüler tasarım)
- Koordinat dönüşümleri
