"""Database manager and connection handling"""

from pathlib import Path
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session
from app.utils.logger import logger
from app.utils.exceptions import DatabaseError
from app.utils.constants import DB_DEFAULT_PATH, DB_ECHO


class DatabaseManager:
    """Singleton database manager"""
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
        
        self.db_path = Path(DB_DEFAULT_PATH)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        
        self.engine: Engine = None
        self.SessionLocal = None
        
        self._connect()
        self._initialized = True
    
    def _connect(self) -> None:
        """Create database connection"""
        try:
            db_url = f'sqlite:///{self.db_path}'
            self.engine = create_engine(
                db_url,
                echo=DB_ECHO,
                connect_args={'check_same_thread': False}
            )
            self.SessionLocal = sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self.engine
            )
            logger.info(f"Database connected: {self.db_path}")
        except Exception as e:
            logger.error(f"Database connection failed: {e}")
            raise DatabaseError(f"Cannot connect to database: {e}")
    
    def get_session(self) -> Session:
        """Get database session"""
        if self.SessionLocal is None:
            raise DatabaseError("Database not initialized")
        return self.SessionLocal()
    
    def create_all_tables(self) -> None:
        """Create all database tables"""
        try:
            from app.models import Base
            Base.metadata.create_all(bind=self.engine)
            logger.info("Database tables created")
        except Exception as e:
            logger.error(f"Failed to create tables: {e}")
            raise DatabaseError(f"Cannot create tables: {e}")
    
    def drop_all_tables(self) -> None:
        """Drop all database tables (WARNING: destructive)"""
        try:
            from app.models import Base
            Base.metadata.drop_all(bind=self.engine)
            logger.warning("All database tables dropped")
        except Exception as e:
            logger.error(f"Failed to drop tables: {e}")
            raise DatabaseError(f"Cannot drop tables: {e}")
    
    def close(self) -> None:
        """Close database connection"""
        if self.engine:
            self.engine.dispose()
            logger.info("Database connection closed")
