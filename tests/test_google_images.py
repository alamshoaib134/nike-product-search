"""
Tests for image search functionality and image management.
"""
import sys
from pathlib import Path
import unittest
import shutil
import os

# Add parent directory to Python path for imports
sys.path.append(str(Path(__file__).parent.parent))
from src import config
from src import image_search

class TestImageManagement(unittest.TestCase):
    """Test cases for image search and management functionality"""
    
    def setUp(self):
        """Set up test environment"""
        self.test_dir = Path("test_images_temp")
        self.test_dir.mkdir(exist_ok=True)
        
        # Sample material numbers for testing
        self.test_materials = [
            "CW0373-010",  # Known Nike product
            "FB7448-412",  # Another known product
            "TEST-123"     # Non-existent product
        ]
    
    def tearDown(self):
        """Clean up test environment"""
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)
    
    def test_init_google_search(self):
        """Test Google Images Search initialization"""
        gis = image_search.init_google_search()
        self.assertIsNotNone(gis, "Failed to initialize Google Images Search")
    
    def test_image_fetching(self):
        """Test image fetching for known products"""
        for material in self.test_materials[:2]:  # Test only known products
            images = image_search.fetch_product_images(
                material, save_dir=self.test_dir
            )
            self.assertIsInstance(images, list, 
                                f"Expected list of images for {material}")
            
            if images:  # Some materials might not have images
                for img_path in images:
                    path = Path(img_path)
                    self.assertTrue(path.exists(), 
                                 f"Image file not found: {img_path}")
                    self.assertTrue(path.stat().st_size > 0, 
                                 f"Image file is empty: {img_path}")
    
    def test_invalid_material(self):
        """Test handling of invalid material numbers"""
        images = image_search.fetch_product_images(
            self.test_materials[2], save_dir=self.test_dir
        )
        self.assertEqual(len(images), 0, 
                        "Should return empty list for invalid material")
    
    def test_image_naming(self):
        """Test image file naming convention"""
        material = self.test_materials[0]
        images = image_search.fetch_product_images(
            material, save_dir=self.test_dir
        )
        
        if images:
            for img_path in images:
                path = Path(img_path)
                expected_prefix = f"{material}_"
                self.assertTrue(path.name.startswith(expected_prefix),
                              f"Invalid image name format: {path.name}")
    
    def test_duplicate_handling(self):
        """Test handling of duplicate image downloads"""
        material = self.test_materials[0]
        
        # First download
        images1 = image_search.fetch_product_images(
            material, save_dir=self.test_dir
        )
        
        # Second download
        images2 = image_search.fetch_product_images(
            material, save_dir=self.test_dir
        )
        
        if images1 and images2:
            self.assertEqual(
                sorted(images1), 
                sorted(images2),
                "Duplicate downloads should maintain consistency"
            )
    
    def test_directory_structure(self):
        """Test creation and management of image directories"""
        material = self.test_materials[0]
        images = image_search.fetch_product_images(
            material, save_dir=self.test_dir
        )
        
        if images:
            # All images should be in the specified directory
            for img_path in images:
                path = Path(img_path)
                self.assertEqual(
                    path.parent.absolute(),
                    self.test_dir.absolute(),
                    f"Image not in correct directory: {img_path}"
                )

if __name__ == '__main__':
    unittest.main(verbosity=2)