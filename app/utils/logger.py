"""Logging configuration for Formwork-CAD"""

import logging
import logging.handlers
import os
from pathlib import Path

# Create logs directory if it doesn't exist
LOGS_DIR = Path(__file__).parent.parent.parent / 'logs'
LOGS_DIR.mkdir(exist_ok=True)


def setup_logger(name: str, log_level=logging.INFO) -> logging.Logger:
    """
    Setup logger with both file and console handlers
    
    Args:
        name: Logger name (usually __name__)
        log_level: Logging level
    
    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_format = logging.Formatter(
        '[%(levelname)s] %(name)s: %(message)s'
    )
    console_handler.setFormatter(console_format)
    
    # File handler (rotating)
    log_file = LOGS_DIR / 'formwork-cad.log'
    file_handler = logging.handlers.RotatingFileHandler(
        log_file,
        maxBytes=5*1024*1024,  # 5MB
        backupCount=5
    )
    file_handler.setLevel(logging.DEBUG)
    file_format = logging.Formatter(
        '[%(asctime)s] [%(levelname)s] %(name)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(file_format)
    
    # Add handlers to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger


# Application logger
logger = setup_logger('formwork-cad')
