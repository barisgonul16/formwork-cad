"""Pytest configuration and fixtures"""

import pytest
from pathlib import Path
from app.database import DatabaseManager
from app.utils.logger import logger


@pytest.fixture(scope='session')
def db_manager():
    """Database manager fixture for tests"""
    logger.info("Setting up test database")
    manager = DatabaseManager()
    manager.db_path = Path('data/test_formwork.db')
    manager.create_all_tables()
    
    yield manager
    
    logger.info("Tearing down test database")
    manager.drop_all_tables()
    manager.close()
    
    # Clean up test database file
    if manager.db_path.exists():
        manager.db_path.unlink()


@pytest.fixture
def db_session(db_manager):
    """Database session fixture for tests"""
    session = db_manager.get_session()
    yield session
    session.close()
