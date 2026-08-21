"""Application constants and configuration"""

# Layer names
LAYER_BETON = 'BETON'
LAYER_KALIP = 'KALIP'
LAYER_PANEL = 'PANEL'
LAYER_H20 = 'H20'
LAYER_KUŞAK = 'KUŞAK'
LAYER_PAYANDA = 'PAYANDA'
LAYER_DIKME = 'DİKME'
LAYER_ÖLÇÜ = 'ÖLÇÜ'
LAYER_YAZI = 'YAZI'
LAYER_AKS = 'AKS'

DEFAULT_LAYERS = [
    LAYER_BETON,
    LAYER_KALIP,
    LAYER_PANEL,
    LAYER_H20,
    LAYER_KUŞAK,
    LAYER_PAYANDA,
    LAYER_DIKME,
    LAYER_ÖLÇÜ,
    LAYER_YAZI,
    LAYER_AKS,
]

# Material categories
CATEGORY_PANEL = 'PANEL'
CATEGORY_H20 = 'H20 KİRİŞ'
CATEGORY_PLYWOOD = 'PLYWOOD'
CATEGORY_STRAP = 'KUŞAK'
CATEGORY_PROP = 'PAYANDA'
CATEGORY_POST = 'DİKME'
CATEGORY_ANCHOR = 'ANKRAJ'
CATEGORY_CONNECTOR = 'BAĞLANTI ELEMANI'
CATEGORY_OTHER = 'DİĞER'

DEFAULT_CATEGORIES = [
    {'name': CATEGORY_PANEL, 'description': 'Panel sistemi', 'order': 1},
    {'name': CATEGORY_H20, 'description': 'H20 kiriş', 'order': 2},
    {'name': CATEGORY_PLYWOOD, 'description': 'Kontrplak', 'order': 3},
    {'name': CATEGORY_STRAP, 'description': 'Metal kuşak', 'order': 4},
    {'name': CATEGORY_PROP, 'description': 'Payanda/destek', 'order': 5},
    {'name': CATEGORY_POST, 'description': 'Teleskopik dikme', 'order': 6},
    {'name': CATEGORY_ANCHOR, 'description': 'Ankraj sistemleri', 'order': 7},
    {'name': CATEGORY_CONNECTOR, 'description': 'Cıvata, kaynak, vb.', 'order': 8},
    {'name': CATEGORY_OTHER, 'description': 'Diğer malzemeler', 'order': 9},
]

# Units
UNIT_PIECE = 'adet'
UNIT_METER = 'metre'
UNIT_SQUARE_METER = 'm2'

DEFAULT_UNITS = [UNIT_PIECE, UNIT_METER, UNIT_SQUARE_METER]

# Grid settings
DEFAULT_GRID_SPACING = 50  # mm
DEFAULT_SNAP_GRID = 50  # mm

# Drawing settings
DEFAULT_ZOOM_MIN = 0.1
DEFAULT_ZOOM_MAX = 5.0
DEFAULT_ZOOM_FACTOR = 1.2

# Database
DB_DEFAULT_PATH = 'data/formwork.db'
DB_ECHO = False  # SQL logging

# File extensions
PROJECT_FILE_EXT = '.kalp'
DXF_FILE_EXT = '.dxf'
