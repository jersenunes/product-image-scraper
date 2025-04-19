# Product Image Scraper

This project automates the process of scraping product images from e-commerce sites (e.g. Shopee), cropping, resizing, and overlaying them onto a background image.

## 🚀 Features
- Scrape product images from a list of product URLs
- Crop and resize according to predefined regions
- Overlay images on a custom background
- Save results in a structured folder

## 🧰 Requirements
- Python 3.10+
- Selenium
- Pillow
- Other libraries listed in `requirements.txt`

## 📁 Folder Structure
- `utils/`: Browser, Image and Helper functions
- `config/`: Configuration files and input data
- `logs/`: Execution logs
- `data/`: Data used by script and for output images

## 🔧 Setup
```bash
pip install -r requirements.txt
python main.py
