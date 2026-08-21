"""Tests for base model"""

import pytest
from datetime import datetime
from app.models import BaseModel


def test_base_model_inheritance():
    """Test that BaseModel has required fields"""
    # BaseModel is abstract, so we can't instantiate it directly
    # But we can check its columns
    assert hasattr(BaseModel, 'id')
    assert hasattr(BaseModel, 'created_at')
    assert hasattr(BaseModel, 'updated_at')
    assert hasattr(BaseModel, 'is_active')
