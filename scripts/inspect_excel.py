"""
Utility script to inspect and analyze ATP Excel file structure.
"""
import pandas as pd
import sys
from pathlib import Path

# Add parent directory to Python path for imports
sys.path.append(str(Path(__file__).parent.parent))
from src import config

def inspect_excel_file(file_path):
    """
    Analyze Excel file structure and content.
    
    Args:
        file_path (str): Path to Excel file
    """
    try:
        print(f"\nInspecting Excel file: {file_path}")
        
        # Read Excel file
        df = pd.read_excel(file_path)
        
        # Get column names from first row
        first_row = df.iloc[0]
        
        # Print column information
        print("\nColumn names in the Excel file:")
        for i, col in enumerate(df.columns):
            print(f"- Original: {col}")
            print(f"  Header Value: {first_row[i]}")
        
        # Create DataFrame with proper headers
        df.columns = df.iloc[0]
        df = df.iloc[1:].reset_index(drop=True)
        
        # Print sample data
        print("\nFirst few rows of formatted data:")
        print(df.head())
        
        # Print unique values in key columns
        key_columns = [
            'Matl Nbr',
            'Matl Long Nm',
            'Sz Desc',
            'Gndr Age Desc',
            'Sport Acty Desc',
            'Colr Comb Desc'
        ]
        
        print("\nSample values from key columns:")
        for col in key_columns:
            if col in df.columns:
                print(f"\n{col}:")
                unique_values = df[col].unique()
                print(f"- Total unique values: {len(unique_values)}")
                print("- Sample values:")
                for val in unique_values[:5]:
                    print(f"  * {val}")
        
        # Print data statistics
        print("\nDataset Statistics:")
        print(f"- Total rows: {len(df)}")
        print(f"- Total columns: {len(df.columns)}")
        
        return True
        
    except Exception as e:
        print(f"\nError analyzing Excel file: {str(e)}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python inspect_excel.py <excel_file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    if not Path(file_path).exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    
    success = inspect_excel_file(file_path)
    sys.exit(0 if success else 1)