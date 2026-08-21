"""Main database models for Formwork-CAD"""

from typing import Optional, List
from sqlalchemy import Column, String, Text, Float, Integer, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime

from .base_model import BaseModel


class Project(BaseModel):
    """Project model"""
    
    __tablename__ = 'projects'
    
    name = Column(String(255), nullable=False, unique=True)
    description = Column(Text)
    
    # Relationships
    columns = relationship("Column", back_populates="project", cascade="all, delete-orphan")
    walls = relationship("Wall", back_populates="project", cascade="all, delete-orphan")
    formwork_elements = relationship("FormworkElement", back_populates="project", cascade="all, delete-orphan")
    layers = relationship("Layer", back_populates="project", cascade="all, delete-orphan")
    drawings = relationship("Drawing", back_populates="project", cascade="all, delete-orphan")
    
    def __repr__(self) -> str:
        return f"<Project(name='{self.name}')>"
    
    def to_dict(self) -> dict:
        """Convert to dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }


class MaterialCategory(BaseModel):
    """Material category model"""
    
    __tablename__ = 'material_categories'
    
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)
    icon = Column(String(255))
    order_index = Column(Integer)
    
    # Relationships
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


class Material(BaseModel):
    """Material model"""
    
    __tablename__ = 'materials'
    
    code = Column(String(100), nullable=False, unique=True)
    name = Column(String(255), nullable=False)
    manufacturer = Column(String(255))
    category_id = Column(Integer, ForeignKey('material_categories.id'), nullable=False)
    description = Column(Text)
    
    # Geometric properties (mm)
    length = Column(Float)
    width = Column(Float)
    height = Column(Float)
    thickness = Column(Float)
    
    # Unit
    unit = Column(String(50), default='adet')  # 'adet', 'metre', 'm2'
    
    # 2D Symbol
    symbol_type = Column(String(50))  # 'rectangle', 'polygon', 'custom'
    symbol_data = Column(Text)  # JSON
    
    # Color (HSV)
    color_h = Column(Integer, default=0)     # 0-360
    color_s = Column(Integer, default=100)   # 0-100
    color_v = Column(Integer, default=100)   # 0-100
    
    # Relationships
    category = relationship("MaterialCategory", back_populates="materials")
    formwork_elements = relationship("FormworkElement", back_populates="material")
    
    def __repr__(self) -> str:
        return f"<Material(code='{self.code}', name='{self.name}')>"
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'code': self.code,
            'name': self.name,
            'manufacturer': self.manufacturer,
            'category_id': self.category_id,
            'unit': self.unit,
        }


class Column(BaseModel):
    """Column model"""
    
    __tablename__ = 'columns'
    
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    name = Column(String(100), nullable=False)
    
    # Geometric properties (mm)
    width = Column(Float, nullable=False)      # Column width
    length = Column(Float, nullable=False)     # Column length
    height = Column(Float, nullable=False)     # Column height
    
    # Position
    x = Column(Float, default=0)       # X coordinate
    y = Column(Float, default=0)       # Y coordinate
    z = Column(Float, default=0)       # Level/Elevation
    
    rotation = Column(Float, default=0)  # Rotation (degrees)
    
    # Views (JSON)
    front_view = Column(Text)   # JSON
    side_view = Column(Text)    # JSON
    top_view = Column(Text)     # JSON
    
    # Relationships
    project = relationship("Project", back_populates="columns")
    formwork_elements = relationship(
        "FormworkElement",
        primaryjoin="and_(Column.id==foreign(FormworkElement.parent_id), FormworkElement.parent_type=='column')",
        foreign_keys="FormworkElement.parent_id",
        back_populates="parent_column",
        cascade="all, delete-orphan"
    )
    
    def get_dimensions(self) -> dict:
        """Get column dimensions"""
        return {
            'width': self.width,
            'length': self.length,
            'height': self.height,
        }
    
    def get_position(self) -> dict:
        """Get column position"""
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


class Wall(BaseModel):
    """Wall model"""
    
    __tablename__ = 'walls'
    
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    name = Column(String(100), nullable=False)
    
    # Geometric properties (mm)
    length = Column(Float, nullable=False)      # Wall length
    thickness = Column(Float, nullable=False)   # Wall thickness
    height = Column(Float, nullable=False)      # Wall height
    
    # Start and end points
    start_x = Column(Float, default=0)
    start_y = Column(Float, default=0)
    start_z = Column(Float, default=0)
    
    end_x = Column(Float, default=0)
    end_y = Column(Float, default=0)
    
    rotation = Column(Float, default=0)  # Rotation (degrees)
    
    # Views (JSON)
    front_view = Column(Text)    # JSON
    back_view = Column(Text)     # JSON
    top_view = Column(Text)      # JSON
    
    # Relationships
    project = relationship("Project", back_populates="walls")
    formwork_elements = relationship(
        "FormworkElement",
        primaryjoin="and_(Wall.id==foreign(FormworkElement.parent_id), FormworkElement.parent_type=='wall')",
        foreign_keys="FormworkElement.parent_id",
        back_populates="parent_wall",
        cascade="all, delete-orphan"
    )
    
    def get_dimensions(self) -> dict:
        """Get wall dimensions"""
        return {
            'length': self.length,
            'thickness': self.thickness,
            'height': self.height,
        }
    
    def get_start_position(self) -> dict:
        """Get start position"""
        return {
            'x': self.start_x,
            'y': self.start_y,
            'z': self.start_z,
        }
    
    def get_end_position(self) -> dict:
        """Get end position"""
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


class FormworkElement(BaseModel):
    """Formwork element model (panel, beam, post, etc.)"""
    
    __tablename__ = 'formwork_elements'
    
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    material_id = Column(Integer, ForeignKey('materials.id'), nullable=False)
    
    # Relationship
    parent_type = Column(String(50))   # 'column', 'wall', 'drawing'
    parent_id = Column(Integer)    # Related element ID
    
    # Position and transformation
    x = Column(Float, nullable=False)
    y = Column(Float, nullable=False)
    z = Column(Float, default=0)
    
    rotation = Column(Float, default=0)        # Degrees
    scale_x = Column(Float, default=1.0)
    scale_y = Column(Float, default=1.0)
    
    # Properties
    layer = Column(String(50))         # Layer name
    quantity = Column(Integer, default=1)
    notes = Column(Text)
    
    placement_method = Column(String(50))  # 'manual', 'auto'
    
    # Relationships
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
    
    def get_position(self) -> dict:
        """Get element position"""
        return {
            'x': self.x,
            'y': self.y,
            'z': self.z,
        }
    
    def get_transformation(self) -> dict:
        """Get element transformation"""
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


class Layer(BaseModel):
    """Drawing layer model"""
    
    __tablename__ = 'layers'
    
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    name = Column(String(100), nullable=False)
    
    # Appearance
    color_h = Column(Integer, default=0)      # Hue (0-360)
    color_s = Column(Integer, default=0)      # Saturation (0-100)
    color_v = Column(Integer, default=50)     # Value (0-100)
    
    line_width = Column(Integer, default=1)   # Pixels
    line_style = Column(String(50), default='solid')  # 'solid', 'dashed', 'dotted'
    
    # Status
    is_visible = Column(Boolean, default=True)
    is_locked = Column(Boolean, default=False)
    
    order_index = Column(Integer)
    
    # Relationships
    project = relationship("Project", back_populates="layers")
    
    def get_color_rgb(self) -> tuple:
        """Convert HSV to RGB"""
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


class Drawing(BaseModel):
    """Drawing model"""
    
    __tablename__ = 'drawings'
    
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    name = Column(String(255), nullable=False)
    drawing_type = Column(String(100))  # 'column_front', 'wall_front', etc.
    
    element_id = Column(Integer)  # Related column/wall ID
    
    # Drawing data
    graphics_data = Column(Text)  # JSON
    
    # View settings
    scale = Column(Float, default=1.0)
    pan_x = Column(Float, default=0)
    pan_y = Column(Float, default=0)
    
    notes = Column(Text)
    
    # Relationships
    project = relationship("Project", back_populates="drawings")
    
    def get_view_settings(self) -> dict:
        """Get view settings"""
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
