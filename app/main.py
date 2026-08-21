"""Formwork-CAD Application Entry Point"""

import sys
import logging
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from PySide6.QtWidgets import QApplication
from app.ui.main_window import MainWindow
from app.database import DatabaseManager
from app.utils.logger import logger as app_logger


def main():
    """Main application entry point"""
    
    # Setup logging
    app_logger.info("="*50)
    app_logger.info("Formwork-CAD v1.0 Starting")
    app_logger.info("="*50)
    
    # Initialize database
    try:
        db_manager = DatabaseManager()
        db_manager.create_all_tables()
        app_logger.info("Database initialized successfully")
    except Exception as e:
        app_logger.error(f"Failed to initialize database: {e}")
        sys.exit(1)
    
    # Create Qt application
    app = QApplication(sys.argv)
    
    # Create main window
    main_window = MainWindow()
    main_window.show()
    
    app_logger.info("Main window displayed")
    
    # Run application
    exit_code = app.exec()
    
    # Cleanup
    db_manager.close()
    app_logger.info("Formwork-CAD Closed")
    
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
