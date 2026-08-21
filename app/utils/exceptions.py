"""Custom exception classes for Formwork-CAD"""


class ApplicationError(Exception):
    """Base exception for the application"""
    pass


class DatabaseError(ApplicationError):
    """Database operation error"""
    pass


class GeometryError(ApplicationError):
    """Geometry calculation error"""
    pass


class ValidationError(ApplicationError):
    """Data validation error"""
    pass


class FileError(ApplicationError):
    """File operation error"""
    pass


class ExportError(ApplicationError):
    """Export operation error"""
    pass
