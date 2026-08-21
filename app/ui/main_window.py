"""Main application window"""

from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QSplitter, QStatusBar
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon, QAction
import logging

logger = logging.getLogger(__name__)


class MainWindow(QMainWindow):
    """Main application window"""
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Formwork-CAD v1.0 - 2D Betonarme Kalıp Tasarımı")
        self.setWindowIcon(QIcon())
        self.setMinimumSize(QSize(1024, 768))
        self.resize(1600, 900)
        
        # Initialize UI
        self._setup_ui()
        self._setup_menu()
        self._setup_toolbar()
        self._setup_statusbar()
        
        logger.info("Main window initialized")
    
    def _setup_ui(self) -> None:
        """Setup main UI layout"""
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Left panel placeholder
        left_panel = QWidget()
        left_panel.setMinimumWidth(200)
        left_layout = QVBoxLayout(left_panel)
        left_layout.addWidget(QWidget())
        
        # Center (drawing area)
        center_panel = QWidget()
        center_layout = QVBoxLayout(center_panel)
        center_layout.addWidget(QWidget())
        
        # Right panel placeholder
        right_panel = QWidget()
        right_panel.setMinimumWidth(300)
        right_panel.setMaximumWidth(400)
        right_layout = QVBoxLayout(right_panel)
        right_layout.addWidget(QWidget())
        
        # Splitter
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(left_panel)
        splitter.addWidget(center_panel)
        splitter.addWidget(right_panel)
        splitter.setStretchFactor(0, 0)
        splitter.setStretchFactor(1, 1)
        splitter.setStretchFactor(2, 0)
        
        main_layout.addWidget(splitter)
        
        # Store references
        self.left_panel = left_panel
        self.center_panel = center_panel
        self.right_panel = right_panel
        
        logger.debug("UI layout setup complete")
    
    def _setup_menu(self) -> None:
        """Setup menu bar"""
        
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu("File")
        file_menu.addAction("New Project").triggered.connect(self._on_new_project)
        file_menu.addAction("Open").triggered.connect(self._on_open_project)
        file_menu.addSeparator()
        file_menu.addAction("Save").triggered.connect(self._on_save_project)
        file_menu.addAction("Save As...").triggered.connect(self._on_save_as_project)
        file_menu.addSeparator()
        file_menu.addAction("Exit").triggered.connect(self.close)
        
        # Edit menu
        edit_menu = menubar.addMenu("Edit")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")
        edit_menu.addSeparator()
        edit_menu.addAction("Cut")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Paste")
        
        # View menu
        view_menu = menubar.addMenu("View")
        view_menu.addAction("Zoom In")
        view_menu.addAction("Zoom Out")
        view_menu.addAction("Fit All")
        view_menu.addSeparator()
        view_menu.addAction("Grid").triggered.connect(self._on_toggle_grid)
        view_menu.addAction("Snap").triggered.connect(self._on_toggle_snap)
        
        # Project menu
        project_menu = menubar.addMenu("Project")
        project_menu.addAction("Add Column").triggered.connect(self._on_add_column)
        project_menu.addAction("Add Wall").triggered.connect(self._on_add_wall)
        
        # Design menu
        design_menu = menubar.addMenu("Design")
        design_menu.addAction("Material Library").triggered.connect(self._on_material_library)
        design_menu.addSeparator()
        design_menu.addAction("Auto Layout Column")
        design_menu.addAction("Auto Layout Wall")
        
        # Help menu
        help_menu = menubar.addMenu("Help")
        help_menu.addAction("About").triggered.connect(self._on_about)
        
        logger.debug("Menu bar setup complete")
    
    def _setup_toolbar(self) -> None:
        """Setup toolbar"""
        
        toolbar = self.addToolBar("Main Toolbar")
        toolbar.setMovable(False)
        
        # File actions
        toolbar.addAction("New")
        toolbar.addAction("Open")
        toolbar.addAction("Save")
        toolbar.addSeparator()
        
        # Edit actions
        toolbar.addAction("Undo")
        toolbar.addAction("Redo")
        toolbar.addSeparator()
        
        # View actions
        toolbar.addAction("Zoom In")
        toolbar.addAction("Zoom Out")
        toolbar.addAction("Fit All")
        
        logger.debug("Toolbar setup complete")
    
    def _setup_statusbar(self) -> None:
        """Setup status bar"""
        
        statusbar = self.statusBar()
        statusbar.showMessage("Ready")
        
        logger.debug("Status bar setup complete")
    
    # Menu action handlers
    def _on_new_project(self) -> None:
        """Handle new project action"""
        logger.info("New project action triggered")
        self.statusBar().showMessage("Creating new project...")
    
    def _on_open_project(self) -> None:
        """Handle open project action"""
        logger.info("Open project action triggered")
        self.statusBar().showMessage("Opening project...")
    
    def _on_save_project(self) -> None:
        """Handle save project action"""
        logger.info("Save project action triggered")
        self.statusBar().showMessage("Saving project...")
    
    def _on_save_as_project(self) -> None:
        """Handle save as project action"""
        logger.info("Save as project action triggered")
        self.statusBar().showMessage("Saving project as...")
    
    def _on_add_column(self) -> None:
        """Handle add column action"""
        logger.info("Add column action triggered")
        self.statusBar().showMessage("Add column...")
    
    def _on_add_wall(self) -> None:
        """Handle add wall action"""
        logger.info("Add wall action triggered")
        self.statusBar().showMessage("Add wall...")
    
    def _on_material_library(self) -> None:
        """Handle material library action"""
        logger.info("Material library action triggered")
        self.statusBar().showMessage("Opening material library...")
    
    def _on_toggle_grid(self) -> None:
        """Handle toggle grid action"""
        logger.info("Toggle grid action triggered")
        self.statusBar().showMessage("Grid toggled")
    
    def _on_toggle_snap(self) -> None:
        """Handle toggle snap action"""
        logger.info("Toggle snap action triggered")
        self.statusBar().showMessage("Snap toggled")
    
    def _on_about(self) -> None:
        """Handle about action"""
        logger.info("About action triggered")
        self.statusBar().showMessage("About Formwork-CAD")
    
    def closeEvent(self, event) -> None:
        """Handle window close event"""
        logger.info("Application closing")
        event.accept()
