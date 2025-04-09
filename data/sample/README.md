# Sample Data Directory

This directory contains sample data files for testing and demonstration purposes.

## Files

### ATP Excel 010524.xlsx
- Sample ATP (Available to Promise) Excel file
- Contains product information including:
  * Material numbers
  * Product descriptions
  * Sizes
  * Pricing
  * Inventory levels

### FQ7860-001-1-Photoroom.png
- Sample product image
- Used for testing image handling functionality
- Demonstrates expected image format and quality

## Using Sample Data

1. For testing:
   ```bash
   python scripts/inspect_excel.py data/sample/ATP\ Excel\ 010524.xlsx
   ```

2. For development:
   - Copy sample files to a development directory
   - Use them for testing new features
   - Verify data processing functionality

## Data Structure

### Excel File Columns
- Matl Nbr (Material Number)
- Matl Long Nm (Material Long Name)
- Sz Desc (Size Description)
- Gndr Age Desc (Gender/Age Description)
- Sport Acty Desc (Sport Activity Description)
- Colr Comb Desc (Color Description)
- INDI MSRP (Price)
- INDI Whlsl Prc (Wholesale Price)
- ATP Qty (Available Quantity)

### Image Naming Convention
- Format: {material_number}_{sequence}.{extension}
- Example: FQ7860-001-1.png

## Notes
- Sample data is for demonstration only
- Do not use in production
- Keep this directory clean and minimal
- Update samples as data structure changes