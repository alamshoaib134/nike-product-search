"""
Configuration settings for Nike Product Search Application.

This is a sample configuration file. To use the application:
1. Copy this file to config_local.py
2. Update the credentials and settings in config_local.py
3. Never commit config_local.py to version control

Required Credentials:
- Google Cloud Platform API Key
- Google Custom Search Engine ID (CX)

To obtain credentials:
1. Visit https://console.cloud.google.com
2. Create a new project or select existing one
3. Enable Custom Search API
4. Create API credentials
5. Visit https://programmablesearch.google.com/create/new
6. Create and configure a Custom Search Engine
7. Get the Search Engine ID (cx)
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

# Image Search Settings
IMAGE_SEARCH_PARAMS = {
    'fileType': 'jpg|png',
    'safe': 'off',
    'imgSize': 'large',
    'imgType': 'photo'
}

# Excel Processing Settings
REQUIRED_COLUMNS = [
    'Matl Nbr',           # Material Number
    'Matl Long Nm',       # Material Long Name
    'Sz Desc',           # Size Description
    'Gndr Age Desc',     # Gender/Age Description
    'Sport Acty Desc',   # Sport Activity Description
    'Colr Comb Desc',    # Color Combination Description
    'INDI MSRP',         # MSRP
    'INDI Whlsl Prc',    # Wholesale Price
    'ATP Qty'            # ATP Quantity
]