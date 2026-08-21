"""Tests for ORM models"""

import pytest
from app.models import (
    Project,
    Material,
    MaterialCategory,
    Column,
    Wall,
    FormworkElement,
    Layer,
    Drawing,
)


class TestProjectModel:
    """Test Project model"""
    
    def test_project_creation(self, db_session):
        """Test creating a project"""
        project = Project(name="Test Project", description="Test Description")
        db_session.add(project)
        db_session.commit()
        
        assert project.id is not None
        assert project.name == "Test Project"
        assert project.is_active == True
    
    def test_project_to_dict(self, db_session):
        """Test project to_dict conversion"""
        project = Project(name="Test Project")
        db_session.add(project)
        db_session.commit()
        
        project_dict = project.to_dict()
        assert project_dict['name'] == "Test Project"
        assert 'created_at' in project_dict


class TestMaterialCategoryModel:
    """Test MaterialCategory model"""
    
    def test_category_creation(self, db_session):
        """Test creating a material category"""
        category = MaterialCategory(name="PANEL", description="Panel System")
        db_session.add(category)
        db_session.commit()
        
        assert category.id is not None
        assert category.name == "PANEL"


class TestMaterialModel:
    """Test Material model"""
    
    def test_material_creation(self, db_session):
        """Test creating a material"""
        category = MaterialCategory(name="PANEL")
        db_session.add(category)
        db_session.commit()
        
        material = Material(
            code="PERI-P500",
            name="PERI Panel 500",
            category_id=category.id,
            width=500,
            height=3200
        )
        db_session.add(material)
        db_session.commit()
        
        assert material.id is not None
        assert material.code == "PERI-P500"
    
    def test_material_to_dict(self, db_session):
        """Test material to_dict conversion"""
        category = MaterialCategory(name="PANEL")
        db_session.add(category)
        db_session.commit()
        
        material = Material(
            code="PERI-P500",
            name="PERI Panel 500",
            category_id=category.id
        )
        db_session.add(material)
        db_session.commit()
        
        material_dict = material.to_dict()
        assert material_dict['code'] == "PERI-P500"


class TestColumnModel:
    """Test Column model"""
    
    def test_column_creation(self, db_session):
        """Test creating a column"""
        project = Project(name="Test Project")
        db_session.add(project)
        db_session.commit()
        
        column = Column(
            project_id=project.id,
            name="K101",
            width=400,
            length=800,
            height=3200
        )
        db_session.add(column)
        db_session.commit()
        
        assert column.id is not None
        assert column.name == "K101"
        assert column.width == 400
    
    def test_column_dimensions(self, db_session):
        """Test column dimensions getter"""
        project = Project(name="Test Project")
        db_session.add(project)
        db_session.commit()
        
        column = Column(
            project_id=project.id,
            name="K101",
            width=400,
            length=800,
            height=3200
        )
        db_session.add(column)
        db_session.commit()
        
        dims = column.get_dimensions()
        assert dims['width'] == 400
        assert dims['length'] == 800
        assert dims['height'] == 3200


class TestWallModel:
    """Test Wall model"""
    
    def test_wall_creation(self, db_session):
        """Test creating a wall"""
        project = Project(name="Test Project")
        db_session.add(project)
        db_session.commit()
        
        wall = Wall(
            project_id=project.id,
            name="P01",
            length=6000,
            thickness=300,
            height=3200
        )
        db_session.add(wall)
        db_session.commit()
        
        assert wall.id is not None
        assert wall.name == "P01"


class TestLayerModel:
    """Test Layer model"""
    
    def test_layer_creation(self, db_session):
        """Test creating a layer"""
        project = Project(name="Test Project")
        db_session.add(project)
        db_session.commit()
        
        layer = Layer(
            project_id=project.id,
            name="PANEL",
            color_h=120,
            color_s=100,
            color_v=100
        )
        db_session.add(layer)
        db_session.commit()
        
        assert layer.id is not None
        assert layer.name == "PANEL"
    
    def test_layer_color_rgb(self, db_session):
        """Test layer color HSV to RGB conversion"""
        project = Project(name="Test Project")
        db_session.add(project)
        db_session.commit()
        
        layer = Layer(
            project_id=project.id,
            name="PANEL",
            color_h=120,
            color_s=100,
            color_v=100
        )
        db_session.add(layer)
        db_session.commit()
        
        rgb = layer.get_color_rgb()
        assert isinstance(rgb, tuple)
        assert len(rgb) == 3
