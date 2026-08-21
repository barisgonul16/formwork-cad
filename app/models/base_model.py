"""Base model for all database entities"""

from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class BaseModel(Base):
    """Base model class for all database models"""
    
    __abstract__ = True
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(id={self.id})>"
