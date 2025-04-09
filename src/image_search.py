"""
Google Images Search functionality for the Nike Product Search Application.
"""
from google_images_search import GoogleImagesSearch
from pathlib import Path
import os
from . import config

def init_google_search():
    """Initialize GoogleImagesSearch with credentials from config"""
    try:
        return GoogleImagesSearch(config.GOOGLE_API_KEY, config.GOOGLE_CX)
    except Exception as e:
        print(f"Error initializing Google Images Search: {e}")
        return None

def fetch_product_images(material_number, save_dir=None):
    """
    Fetch product images from Google Images Search
    
    Args:
        material_number (str): Product material number
        save_dir (str, optional): Directory to save images. Defaults to config.PRODUCT_IMAGES_DIR
    
    Returns:
        list: List of paths to downloaded images
    """
    if save_dir is None:
        save_dir = config.PRODUCT_IMAGES_DIR
    
    save_dir = Path(save_dir)
    save_dir.mkdir(exist_ok=True)
    
    gis = init_google_search()
    if not gis:
        return []
    
    search_params = {
        'q': f"{material_number} nike product",
        'num': config.MAX_SEARCH_RESULTS,
        'fileType': 'jpg|png',
        'safe': 'off',
        'imgSize': 'large',
        'imgType': 'photo'
    }
    
    try:
        gis.search(search_params=search_params)
        images = []
        
        for idx, image in enumerate(gis.results(), 1):
            try:
                image_path = save_dir / f"{material_number}_{idx}.jpg"
                if not image_path.exists():
                    image.download(str(save_dir))
                images.append(str(image_path))
            except Exception as e:
                print(f"Error downloading image {idx}: {e}")
                continue
                
        return images
    except Exception as e:
        print(f"Error searching for images: {e}")
        return []

if __name__ == "__main__":
    # Example usage
    images = fetch_product_images("DZ2949-010")
    print(f"Downloaded {len(images)} images")
    for img in images:
        print(f"- {img}")