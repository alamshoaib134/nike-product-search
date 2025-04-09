"""
Main application file for Nike Product Search Application.
Handles Excel processing, search functionality, and image management.
"""
import gradio as gr
import pandas as pd
import numpy as np
from pathlib import Path
import os

from . import config
from . import image_search

class DataStore:
    """Stores application data and state"""
    def __init__(self):
        self.df = None

data_store = DataStore()

def process_excel_file(file):
    """Process the uploaded Excel file and return a message"""
    try:
        # Read Excel file with first row as header
        df = pd.read_excel(file.name)
        # Set proper column names from first row
        df.columns = df.iloc[0]
        # Remove the header row and reset index
        data_store.df = df.iloc[1:].reset_index(drop=True)
        return "Excel file successfully loaded!"
    except Exception as e:
        data_store.df = None
        return f"Error loading file: {str(e)}"

def search_products(search_term, search_type):
    """Search for products in the DataFrame"""
    if data_store.df is None:
        return "Please upload an Excel file first.", None, [], None
    
    if not search_term.strip():
        return "Please enter a search term.", None, [], None

    df = data_store.df
    
    if search_type == "Material Number":
        results = df[df["Matl Nbr"].astype(str).str.contains(search_term, case=False, na=False)]
    else:  # Material Long Name
        results = df[df["Matl Long Nm"].astype(str).str.contains(search_term, case=False, na=False)]
    
    if len(results) == 0:
        # Find similar products using fuzzy matching
        if search_type == "Material Long Name":
            def calculate_similarity(x):
                x_set = set(str(x).lower().split())
                search_set = set(search_term.lower().split())
                intersection = len(x_set & search_set)
                union = len(x_set | search_set)
                return intersection / union if union > 0 else 0
            
            similarities = df["Matl Long Nm"].apply(calculate_similarity)
            similar_products = df.iloc[np.argsort(similarities)[-5:][::-1]]
            
            # Format the similar products data
            similar_products_display = similar_products.apply(lambda row: {
                'Material Number': str(row['Matl Nbr']),
                'Material Name': str(row['Matl Long Nm']),
                'Size': str(row['Sz Desc']),
                'MSRP': str(row['INDI MSRP']),
                'Wholesale Price': str(row['INDI Whlsl Prc'])
            }, axis=1).to_list()
            
            return "No exact matches found. Here are similar products:", None, similar_products_display, None
        return "No matches found.", None, [], None
    
    exact_match = results.iloc[0]
    
    # Format the exact match data
    exact_match_display = {
        'Material Number': str(exact_match['Matl Nbr']),
        'Material Name': str(exact_match['Matl Long Nm']),
        'Size': str(exact_match['Sz Desc']),
        'Gender/Age': str(exact_match['Gndr Age Desc']),
        'Sport Activity': str(exact_match['Sport Acty Desc']),
        'Color': str(exact_match['Colr Comb Desc']),
        'MSRP': str(exact_match['INDI MSRP']),
        'Wholesale Price': str(exact_match['INDI Whlsl Prc']),
        'ATP Quantity': str(exact_match['ATP Qty'])
    }
    
    # Get product images
    material_number = str(exact_match["Matl Nbr"])
    images = image_search.fetch_product_images(material_number)
    
    # Format other matches
    other_matches = results.iloc[1:].apply(lambda row: {
        'Material Number': str(row['Matl Nbr']),
        'Material Name': str(row['Matl Long Nm']),
        'Size': str(row['Sz Desc']),
        'MSRP': str(row['INDI MSRP']),
        'Wholesale Price': str(row['INDI Whlsl Prc'])
    }, axis=1).to_list()
    
    return "Exact match found:", exact_match_display, other_matches, images

# Create the Gradio interface
def create_interface():
    """Create and configure the Gradio interface"""
    with gr.Blocks(title="Product Search Application") as interface:
        gr.Markdown("""
        # Product Search Application
        Search for products by Material Number or Material Long Name. 
        Upload an Excel file first, then use the search functionality.
        """)
        
        with gr.Row():
            file_input = gr.File(label="Upload Excel File")
        
        with gr.Row():
            file_status = gr.Textbox(label="File Status", interactive=False)
        
        with gr.Row():
            search_input = gr.Textbox(label="Search Term", placeholder="Enter material number or name...")
            search_type = gr.Radio(
                choices=["Material Number", "Material Long Name"],
                value="Material Number",
                label="Search Type"
            )
        
        search_button = gr.Button("Search", variant="primary")
        
        with gr.Row():
            message_output = gr.Textbox(label="Status", interactive=False)
            
        with gr.Row():
            product_info = gr.JSON(label="Product Details")
            
        with gr.Row():
            similar_products = gr.JSON(label="Other Matches / Similar Products")
            
        with gr.Row():
            gallery = gr.Gallery(label="Product Images")
        
        file_input.change(
            process_excel_file,
            inputs=[file_input],
            outputs=[file_status]
        )
        
        search_button.click(
            search_products,
            inputs=[search_input, search_type],
            outputs=[message_output, product_info, similar_products, gallery]
        )
    
    return interface

if __name__ == "__main__":
    # Create required directories
    Path(config.PRODUCT_IMAGES_DIR).mkdir(exist_ok=True)
    Path(config.TEST_IMAGES_DIR).mkdir(exist_ok=True)
    
    # Launch the application
    interface = create_interface()
    interface.launch(share=True, debug=config.DEBUG)
