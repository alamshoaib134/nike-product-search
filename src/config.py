"""
Configuration settings for the Nike Product Search Application.
Create a config_local.py file with your actual credentials and settings.
"""

# Google Images Search API Configuration
GOOGLE_API_KEY = "your_api_key_here"
GOOGLE_CX = "your_custom_search_engine_id_here"

# Application Settings
DEBUG = False
MAX_SEARCH_RESULTS = 5
SUPPORTED_IMAGE_FORMATS = ['.jpg', '.jpeg', '.png']
DEFAULT_TIMEOUT = 10

# Directory Settings
PRODUCT_IMAGES_DIR = "product_images"
TEST_IMAGES_DIR = "test_images"

try:
    from config_local import *
except ImportError:
    pass