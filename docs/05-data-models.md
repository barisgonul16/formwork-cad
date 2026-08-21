# 5. VERİ MODELLERİ

## 5.1 Veri Modeli Tasarım Prensipleri

1. **SQLAlchemy ORM kullanılacaktır** - SQL yazmaktan ziyade Python nesneleri
2. **BaseModel sınıfı** - Ortak alanlar (id, created_at, updated_at)
3. **Type hints** - Python 3.10+ ile tam tip belirtimi
4. **Validasyon** - Model seviyesinde validasyon

---

## 5.2 BaseModel (Tüm Modellerin Temel Sınıfı)

```python
# app/models/base_model.py

from datetime import datetime
from typing import Optional
from sqlalchemy import Column, Integer, DateTime, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class BaseModel(Base):
    """Tüm modeller için temel sınıf"""
    
    __abstract__ = True
    
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    created_at: datetime = Column(DateTime, default=datetime.utcnow)
    updated_at: datetime = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active: bool = Column(Boolean, default=True)
    
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(id={self.id})>"
```

---

## 5.3 Project Modeli

```python
# app/models/project.py

from typing import List, Optional
from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from .base_model import BaseModel

class Project(BaseModel):
    """Proje modeli"""
    
    __tablename__ = 'projects'
    
    name: str = Column(String(255), nullable=False, unique=True)
    description: Optional[str] = Column(Text)
    
    # İlişkiler
    columns = relationship("Column", back_populates="project", cascade="all, delete-orphan")
    walls = relationship("Wall", back_populates="project", cascade="all, delete-orphan")
    formwork_elements = relationship("FormworkElement", back_populates="project", cascade="all, delete-orphan")
    layers = relationship("Layer", back_populates="project", cascade="all, delete-orphan")
    drawings = relationship("Drawing", back_populates="project", cascade="all, delete-orphan")
    
    def __repr__(self) -> str:
        return f"<Project(name='{self.name}')>"
    
    def to_dict(self) -> dict:
        """Sözlüğe dönüştür"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }
```

---

## 5.4 MaterialCategory Modeli

```python
# app/models/category.py

from typing import List, Optional
from sqlalchemy import Column, String, Text, Integer
from sqlalchemy.orm import relationship

from .base_model import BaseModel

class MaterialCategory(BaseModel):
    """Malzeme kategorisi modeli"""
    
    __tablename__ = 'material_categories'
    
    name: str = Column(String(100), nullable=False, unique=True)
    description: Optional[str] = Column(Text)
    icon: Optional[str] = Column(String(255))
    order_index: int = Column(Integer)
    
    # İlişkiler
    materials = relationship("Material", back_populates="category")
    
    def __repr__(self) -> str:
        return f"<MaterialCategory(name='{self.name}')>"
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'order_index': self.order_index,
        }
```

---

## 5.5 Material Modeli

```python
# app/models/material.py

from typing import Optional, Dict, Any
from sqlalchemy import Column, String, Text, Float, Integer, ForeignKey, JSON
from sqlalchemy.orm import relationship
import json

from .base_model import BaseModel

class Material(BaseModel):
    """Malzeme modeli"""
    
    __tablename__ = 'materials'
    
    code: str = Column(String(100), nullable=False, unique=True)
    name: str = Column(String(255), nullable=False)
    manufacturer: Optional[str] = Column(String(255))
    category_id: int = Column(Integer, ForeignKey('material_categories.id'), nullable=False)
    description: Optional[str] = Column(Text)
    
    # Geometrik bilgiler (mm)
    length: Optional[float] = Column(Float)
    width: Optional[float] = Column(Float)
    height: Optional[float] = Column(Float)
    thickness: Optional[float] = Column(Float)
    
    # Birim
    unit: str = Column(String(50), default='adet')  # 'adet', 'metre', 'm2'
    
    # 2D Sembol
    symbol_type: Optional[str] = Column(String(50))  # 'rectangle', 'polygon', 'custom'
    symbol_data: Optional[str] = Column(Text)  # JSON
    
    # Renk (HSV)
    color_h: int = Column(Integer, default=0)     # 0-360
    color_s: int = Column(Integer, default=100)   # 0-100
    color_v: int = Column(Integer, default=100)   # 0-100
    
    # İlişkiler
    category = relationship("MaterialCategory", back_populates="materials")
    formwork_elements = relationship("FormworkElement", back_populates="material")
    
    def get_symbol_data(self) -> Dict[str, Any]:
        """Sembol verisini JSON'dan döndür"""
        if self.symbol_data:
            return json.loads(self.symbol_data)
        return {}
    
    def set_symbol_data(self, data: Dict[str, Any]) -> None:
        """Sembol verisini JSON'a çevir"""
        self.symbol_data = json.dumps(data)
    
    def get_dimensions(self) -> Dict[str, Optional[float]]:
        """Tüm boyutları döndür"""
        return {
            'length': self.length,
            'width': self.width,
            'height': self.height,
            'thickness': self.thickness,
        }
    
    def get_color_rgb(self) -> tuple:
        """HSV'den RGB'ye dönüştür"""
        import colorsys
        r, g, b = colorsys.hsv_to_rgb(
            self.color_h / 360,
            self.color_s / 100,
            self.color_v / 100
        )
        return (int(r * 255), int(g * 255), int(b * 255))
    
    def __repr__(self) -> str:
        return f"<Material(code='{self.code}', name='{self.name}')>"
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'code': self.code,
            'name': self.name,
            'manufacturer': self.manufacturer,
            'category_id': self.category_id,
            'dimensions': self.get_dimensions(),
            'unit': self.unit,
            'color_rgb': self.get_color_rgb(),
        }
```

---

## 5.6 Column Modeli

```python
# app/models/column.py

from typing import Optional
from sqlalchemy import Column, String, Float, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
import json

from .base_model import BaseModel

class Column(BaseModel):
    """Kolon modeli"""
    
    __tablename__ = 'columns'
    
    project_id: int = Column(Integer, ForeignKey('projects.id'), nullable=False)
    name: str = Column(String(100), nullable=False)
    
    # Geometrik bilgiler (mm)
    width: float = Column(Float, nullable=False)      # Kolon genişliği
    length: float = Column(Float, nullable=False)     # Kolon uzunluğu
    height: float = Column(Float, nullable=False)     # Kolon yüksekliği
    
    # Pozisyon
    x: float = Column(Float, default=0)       # X koordinatı
    y: float = Column(Float, default=0)       # Y koordinatı
    z: float = Column(Float, default=0)       # Kod/Seviye
    
    rotation: float = Column(Float, default=0)  # Rotasyon (derece)
    
    # Görünüşler (JSON)
    front_view: Optional[str] = Column(Text)   # JSON
    side_view: Optional[str] = Column(Text)    # JSON
    top_view: Optional[str] = Column(Text)     # JSON
    
    # İlişkiler
    project = relationship("Project", back_populates="columns")
    formwork_elements = relationship(
        "FormworkElement",
        foreign_keys="FormworkElement.parent_id",
        primaryjoin="and_(Column.id==foreign(FormworkElement.parent_id), FormworkElement.parent_type=='column')",
        back_populates="parent_column"
    )
    
    def get_dimensions(self) -> Dict[str, float]:
        """Kolon boyutlarını döndür"""
        return {
            'width': self.width,
            'length': self.length,
            'height': self.height,
        }
    
    def get_position(self) -> Dict[str, float]:
        """Kolon konumunu döndür"""
        return {
            'x': self.x,
            'y': self.y,
            'z': self.z,
        }
    
    def __repr__(self) -> str:
        return f"<Column(name='{self.name}', {self.width}x{self.length}x{self.height})>"
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'project_id': self.project_id,
            'dimensions': self.get_dimensions(),
            'position': self.get_position(),
            'rotation': self.rotation,
        }
```

---

## 5.7 Wall Modeli

```python
# app/models/wall.py

from typing import Optional, Dict
from sqlalchemy import Column, String, Float, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship

from .base_model import BaseModel

class Wall(BaseModel):
    """Perde modeli"""
    
    __tablename__ = 'walls'
    
    project_id: int = Column(Integer, ForeignKey('projects.id'), nullable=False)
    name: str = Column(String(100), nullable=False)
    
    # Geometrik bilgiler (mm)
    length: float = Column(Float, nullable=False)      # Perde uzunluğu
    thickness: float = Column(Float, nullable=False)   # Perde kalınlığı
    height: float = Column(Float, nullable=False)      # Perde yüksekliği
    
    # Başlangıç ve bitiş noktaları
    start_x: float = Column(Float, default=0)
    start_y: float = Column(Float, default=0)
    start_z: float = Column(Float, default=0)
    
    end_x: float = Column(Float, default=0)
    end_y: float = Column(Float, default=0)
    
    rotation: float = Column(Float, default=0)  # Rotasyon (derece)
    
    # Görünüşler (JSON)
    front_view: Optional[str] = Column(Text)    # JSON
    back_view: Optional[str] = Column(Text)     # JSON
    top_view: Optional[str] = Column(Text)      # JSON
    
    # İlişkiler
    project = relationship("Project", back_populates="walls")
    formwork_elements = relationship(
        "FormworkElement",
        foreign_keys="FormworkElement.parent_id",
        primaryjoin="and_(Wall.id==foreign(FormworkElement.parent_id), FormworkElement.parent_type=='wall')",
        back_populates="parent_wall"
    )
    
    def get_dimensions(self) -> Dict[str, float]:
        """Perde boyutlarını döndür"""
        return {
            'length': self.length,
            'thickness': self.thickness,
            'height': self.height,
        }
    
    def get_start_position(self) -> Dict[str, float]:
        """Başlangıç konumunu döndür"""
        return {
            'x': self.start_x,
            'y': self.start_y,
            'z': self.start_z,
        }
    
    def get_end_position(self) -> Dict[str, float]:
        """Bitiş konumunu döndür"""
        return {
            'x': self.end_x,
            'y': self.end_y,
        }
    
    def __repr__(self) -> str:
        return f"<Wall(name='{self.name}', length={self.length}mm)>"
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'project_id': self.project_id,
            'dimensions': self.get_dimensions(),
            'start_position': self.get_start_position(),
            'end_position': self.get_end_position(),
            'rotation': self.rotation,
        }
```

---

## 5.8 FormworkElement Modeli

```python
# app/models/element.py

from typing import Optional, Dict
from sqlalchemy import Column, String, Float, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship

from .base_model import BaseModel

class FormworkElement(BaseModel):
    """Kalıp elemanı modeli (panel, kiriş, dikme vb.)"""
    
    __tablename__ = 'formwork_elements'
    
    project_id: int = Column(Integer, ForeignKey('projects.id'), nullable=False)
    material_id: int = Column(Integer, ForeignKey('materials.id'), nullable=False)
    
    # İlişki
    parent_type: str = Column(String(50))   # 'column', 'wall', 'drawing'
    parent_id: Integer = Column(Integer)    # İlişkili eleman ID'si
    
    # Pozisyon ve transformasyon
    x: float = Column(Float, nullable=False)
    y: float = Column(Float, nullable=False)
    z: float = Column(Float, default=0)
    
    rotation: float = Column(Float, default=0)        # Derece
    scale_x: float = Column(Float, default=1.0)
    scale_y: float = Column(Float, default=1.0)
    
    # Özellikler
    layer: str = Column(String(50))         # Layer adı
    quantity: int = Column(Integer, default=1)
    notes: Optional[str] = Column(Text)
    
    placement_method: str = Column(String(50))  # 'manual', 'auto'
    
    # İlişkiler
    project = relationship("Project", back_populates="formwork_elements")
    material = relationship("Material", back_populates="formwork_elements")
    
    parent_column = relationship(
        "Column",
        foreign_keys=[parent_id],
        primaryjoin="and_(FormworkElement.parent_id==foreign(Column.id), FormworkElement.parent_type=='column')",
        back_populates="formwork_elements"
    )
    parent_wall = relationship(
        "Wall",
        foreign_keys=[parent_id],
        primaryjoin="and_(FormworkElement.parent_id==foreign(Wall.id), FormworkElement.parent_type=='wall')",
        back_populates="formwork_elements"
    )
    
    def get_position(self) -> Dict[str, float]:
        """Konumlandırmayı döndür"""
        return {
            'x': self.x,
            'y': self.y,
            'z': self.z,
        }
    
    def get_transformation(self) -> Dict[str, float]:
        """Transformasyonları döndür"""
        return {
            'rotation': self.rotation,
            'scale_x': self.scale_x,
            'scale_y': self.scale_y,
        }
    
    def __repr__(self) -> str:
        return f"<FormworkElement(material_id={self.material_id}, parent={self.parent_type})>"
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'material_id': self.material_id,
            'parent_type': self.parent_type,
            'parent_id': self.parent_id,
            'position': self.get_position(),
            'transformation': self.get_transformation(),
            'layer': self.layer,
            'quantity': self.quantity,
            'placement_method': self.placement_method,
        }
```

---

## 5.9 Layer Modeli

```python
# app/models/layer.py

from typing import Tuple
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from .base_model import BaseModel

class Layer(BaseModel):
    """Çizim katmanı modeli"""
    
    __tablename__ = 'layers'
    __table_args__ = (UniqueConstraint('project_id', 'name', name='_project_layer_uc'),)
    
    project_id: int = Column(Integer, ForeignKey('projects.id'), nullable=False)
    name: str = Column(String(100), nullable=False)
    
    # Görünüm
    color_h: int = Column(Integer, default=0)      # Hue (0-360)
    color_s: int = Column(Integer, default=0)      # Saturation (0-100)
    color_v: int = Column(Integer, default=50)     # Value (0-100)
    
    line_width: int = Column(Integer, default=1)   # Pixel
    line_style: str = Column(String(50), default='solid')  # 'solid', 'dashed', 'dotted'
    
    # Durumu
    is_visible: bool = Column(Boolean, default=True)
    is_locked: bool = Column(Boolean, default=False)
    
    order_index: int = Column(Integer)
    
    # İlişkiler
    project = relationship("Project", back_populates="layers")
    
    def get_color_rgb(self) -> Tuple[int, int, int]:
        """HSV'den RGB'ye dönüştür"""
        import colorsys
        r, g, b = colorsys.hsv_to_rgb(
            self.color_h / 360,
            self.color_s / 100,
            self.color_v / 100
        )
        return (int(r * 255), int(g * 255), int(b * 255))
    
    def __repr__(self) -> str:
        return f"<Layer(name='{self.name}', visible={self.is_visible})>"
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'color_rgb': self.get_color_rgb(),
            'line_width': self.line_width,
            'line_style': self.line_style,
            'is_visible': self.is_visible,
            'is_locked': self.is_locked,
        }
```

---

## 5.10 Drawing Modeli

```python
# app/models/drawing.py

from typing import Optional, Dict, Any
from sqlalchemy import Column, String, Float, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
import json

from .base_model import BaseModel

class Drawing(BaseModel):
    """Çizim modeli"""
    
    __tablename__ = 'drawings'
    
    project_id: int = Column(Integer, ForeignKey('projects.id'), nullable=False)
    name: str = Column(String(255), nullable=False)
    drawing_type: str = Column(String(100))  # 'column_front', 'wall_front', vb.
    
    element_id: Optional[int] = Column(Integer)  # İlişkili kolon/perde
    
    # Çizim verileri
    graphics_data: Optional[str] = Column(Text)  # JSON
    
    # Görünüm ayarları
    scale: float = Column(Float, default=1.0)
    pan_x: float = Column(Float, default=0)
    pan_y: float = Column(Float, default=0)
    
    notes: Optional[str] = Column(Text)
    
    # İlişkiler
    project = relationship("Project", back_populates="drawings")
    
    def get_graphics_data(self) -> Dict[str, Any]:
        """Grafik verisini döndür"""
        if self.graphics_data:
            return json.loads(self.graphics_data)
        return {}
    
    def set_graphics_data(self, data: Dict[str, Any]) -> None:
        """Grafik verisini ayarla"""
        self.graphics_data = json.dumps(data)
    
    def get_view_settings(self) -> Dict[str, float]:
        """Görünüm ayarlarını döndür"""
        return {
            'scale': self.scale,
            'pan_x': self.pan_x,
            'pan_y': self.pan_y,
        }
    
    def __repr__(self) -> str:
        return f"<Drawing(name='{self.name}', type='{self.drawing_type}')>"
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'drawing_type': self.drawing_type,
            'element_id': self.element_id,
            'view_settings': self.get_view_settings(),
        }
```

---

## 5.11 Model Özeti

| Model | Tablo | Amaç |
|-------|-------|------|
| Project | projects | Proje bilgileri |
| MaterialCategory | material_categories | Malzeme kategorileri |
| Material | materials | Malzeme kütüphanesi |
| Column | columns | Kolon tasarımı |
| Wall | walls | Perde tasarımı |
| FormworkElement | formwork_elements | Kalıp elemanları |
| Layer | layers | Çizim katmanları |
| Drawing | drawings | Proje çizimler |

---

## 5.12 Veri Validasyonu

Örnek validasyon:

```python
# app/utils/validators.py

def validate_column(column: Column) -> bool:
    """Kolon doğruluğu kontrol et"""
    if column.width <= 0 or column.length <= 0 or column.height <= 0:
        raise ValueError("Kolon boyutları sıfırdan büyük olmalıdır")
    if column.name is None or len(column.name.strip()) == 0:
        raise ValueError("Kolon adı boş olamaz")
    return True

def validate_material(material: Material) -> bool:
    """Malzeme doğruluğu kontrol et"""
    if material.code is None or len(material.code.strip()) == 0:
        raise ValueError("Malzeme kodu boş olamaz")
    if material.category_id is None:
        raise ValueError("Malzeme kategorisi seçilmeli")
    return True
```

---

## Sonuç

✅ Veri Modelleri:
- SQLAlchemy ORM ile tanımlanmış
- Type hints kullanılmış
- İlişkiler doğru kurulmuş
- Yardımcı metodlar sağlanmış
- Validasyon için hazırlı
