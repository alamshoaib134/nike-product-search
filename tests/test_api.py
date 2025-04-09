"""
Tests for Google Images Search API connectivity and configuration.
"""
import sys
from pathlib import Path
import unittest

# Add parent directory to Python path for imports
sys.path.append(str(Path(__file__).parent.parent))
from src import config
from google_images_search import GoogleImagesSearch

class TestGoogleImagesAPI(unittest.TestCase):
    """Test cases for Google Images Search API"""
    
    def setUp(self):
        """Initialize test environment"""
        self.api_key = config.GOOGLE_API_KEY
        self.cx = config.GOOGLE_CX
        self.gis = GoogleImagesSearch(self.api_key, self.cx)
    
    def test_api_credentials(self):
        """Test if API credentials are properly configured"""
        self.assertNotEqual(self.api_key, "your_api_key_here", 
                          "API key not configured")
        self.assertNotEqual(self.cx, "your_custom_search_engine_id_here", 
                          "Custom Search Engine ID not configured")
    
    def test_basic_search(self):
        """Test basic image search functionality"""
        search_params = {
            'q': 'test',
            'num': 1,
            'safe': 'off',
        }
        
        try:
            self.gis.search(search_params=search_params)
            results = list(self.gis.results())
            self.assertTrue(len(results) > 0, "No search results returned")
            
            # Verify result has required attributes
            result = results[0]
            self.assertIsNotNone(result.url, "Result URL is None")
            
        except Exception as e:
            self.fail(f"Search failed with error: {str(e)}")
    
    def test_product_search(self):
        """Test product-specific image search"""
        test_material = "CW0373-010"
        search_params = {
            'q': f"{test_material} nike product",
            'num': 1,
            'fileType': 'jpg|png',
            'safe': 'off',
            'imgSize': 'large',
            'imgType': 'photo'
        }
        
        try:
            self.gis.search(search_params=search_params)
            results = list(self.gis.results())
            self.assertTrue(len(results) > 0, 
                          f"No search results for material: {test_material}")
            
        except Exception as e:
            self.fail(f"Product search failed with error: {str(e)}")

if __name__ == '__main__':
    unittest.main(verbosity=2)