# Nike Product Search Application

A Python-based web application that provides seamless product search functionality for Nike products using Excel data and image management. Built with Gradio for the user interface and integrated with Google Images Search API for product visualization.

## Features

- **Excel File Processing**
  - Handles ATP Excel format with product details
  - Processes material numbers, descriptions, and pricing information
  - Supports real-time data updates via file upload
  

- **Advanced Search Capabilities**
  - Search by Material Number for exact matches
  - Search by Material Long Name with fuzzy matching
  - Display of similar products when exact matches aren't found
  - Comprehensive product details including size, color, and pricing

- **Image Management System**
  - Organized directory structure for product images
  - Automatic image fetching from Google Images
  - Local image caching for improved performance
  - Structured naming convention: `{material_number}_{sequence}.jpg`

- **User-Friendly Interface**
  - Clean and responsive Gradio web interface
  - Real-time search results
  - Image gallery for product visualization
  - Clear display of product details and pricing

## Setup

1. Install required packages:
```bash
pip install gradio pandas numpy google_images_search openpyxl requests
```

2. Configure Google Images Search API:
   - Go to [Google Cloud Console](https://console.cloud.google.com)
   - Create a new project or select existing one
   - Enable Custom Search API
   - Create credentials (API key)
   - Go to [Google Programmable Search Engine](https://programmablesearch.google.com/create/new)
   - Create a new search engine
   - Get your Search Engine ID (cx)
   - Update `API_KEY` and `CX` in `app.py`

3. Create required directories:
```bash
mkdir -p product_images test_images
```

4. Run the application:
```bash
python app.py
```

## Project Structure

```
.
├── app.py                 # Main application file
├── image_search.py        # Google Images Search implementation
├── test_api.py           # API credentials testing
├── test_google_images.py # Image search testing
├── product_images/       # Organized product images
│   └── {material_number}/  # Material-specific directories
└── README.md            # This file
```

## Usage

1. Launch the application
2. Upload ATP Excel file containing product data
3. Search using either:
   - Material Number (e.g., "CW0373-010")
   - Material Long Name (product description)
4. View results including:
   - Product details
   - Pricing information
   - Similar products
   - Product images

## Features in Detail

### Excel Processing
- First row header detection
- Proper column mapping
- Data validation and error handling

### Search Functionality
- Case-insensitive search
- Fuzzy matching for product names
- Similar product suggestions
- Comprehensive result formatting

### Image Management
- Structured directory organization
- Automatic image downloading
- Format standardization
- Caching mechanism

## Tech Stack

- **Backend**: Python
- **Frontend**: Gradio
- **Data Processing**: Pandas, NumPy
- **Image Search**: Google Images Search API
- **File Handling**: Pathlib, OS
- **HTTP Requests**: Requests

## Contributing

Feel free to contribute to this project by:
- Reporting issues
- Suggesting enhancements
- Submitting pull requests

## Example Usage

### Search by Material Number
```
Material Number: CW0373-010
Result: Nike Air Max 270
- Size: US 10
- Color: Black/White
- MSRP: $150
```

### Search by Product Name
```
Search Term: "Air Max"
Results:
1. CW0373-010 - Nike Air Max 270
2. FB7448-412 - Nike Air Max Plus
3. FN5856-457 - Nike Air Max 90
```

## API Setup Details

### Google Cloud Setup
1. Visit Google Cloud Console
2. Create/Select Project
3. Enable APIs & Services
4. Enable "Custom Search API"
5. Create Credentials
6. Copy API Key

### Custom Search Engine Setup
1. Visit Programmable Search Engine
2. Create New Search Engine
3. Configure for image search
4. Get Search Engine ID (cx)
5. Update application credentials

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Troubleshooting

### Common Issues and Solutions

1. **Excel File Loading Issues**
   - Ensure file is not open in another program
   - Check file format is .xlsx
   - Verify first row contains correct column headers
   - Make sure required columns exist:
     * Material Number (Matl Nbr)
     * Material Long Name (Matl Long Nm)
     * Size (Sz Desc)
     * Price fields (INDI MSRP, INDI Whlsl Prc)

2. **Image Search Problems**
   - Verify API credentials are correct
   - Run `test_api.py` to check API connectivity
   - Ensure internet connection is stable
   - Check if product_images directory exists and is writable
   - Look for specific error messages in terminal output

3. **Search Functionality Issues**
   - Material numbers should match exactly
   - Long name searches allow partial matches
   - Check for special characters in search terms
   - Verify Excel data is properly loaded (check file status)

### Debug Mode

To run the application in debug mode with detailed logging:
```bash
export DEBUG=1
python app.py
```

This will show:
- API requests and responses
- Image download progress
- Data processing steps
- Error details

## Support and Contributions

For issues and questions:
1. Check the troubleshooting section
2. Look through existing GitHub issues
3. Create a new issue with:
   - Detailed problem description
   - Steps to reproduce
   - Error messages
   - System information

Pull requests are welcome! Please:
- Follow existing code style
- Add tests for new features
- Update documentation
- Describe changes in PR