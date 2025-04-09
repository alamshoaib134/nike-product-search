"""
Nike Product Search Application package.
"""
from pathlib import Path

# Add base directory to Python path for proper imports
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import configuration
try:
    from .config_local import *
except ImportError:
    from .config_sample import *

# Create required directories
Path(PRODUCT_IMAGES_DIR).mkdir(exist_ok=True)
Path(TEST_IMAGES_DIR).mkdir(exist_ok=True)
