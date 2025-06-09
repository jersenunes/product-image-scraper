# Product Image Scraper
This project is very useful for ecommerce affiliates, it automates the process of scraping product images from e-commerce sites (e.g. Shopee and Magazine Luiza), cropping, resizing, and overlaying them onto a background image.

## 🚀 Features
- Scrape product images from a list of product URLs
- Crop and resize according to predefined sizes and contitions
- Overlay images on a custom background
- Save results in a structured folder

## 🧰 Requirements
- Python 3.10+
- Selenium
- Pillow
- Pyautogui
- Other libraries listed in `requirements.txt`

## 📁 Folder Structure
- `sites/`: Modules to call functions to get product images (shopee and magalu) and send urls and products images for whatsapp group
- `utils/`: Modules to be used as functions to make and access a browser, get and resize images and others helpers functions
- `config/`: Configuration file and input data for control
- `logs/`: Execution and troubleshooting logs
- `data/`: Data used by script and for output images and texts

## 🔧 Setup
```bash
pip install -r requirements.txt
python main.py