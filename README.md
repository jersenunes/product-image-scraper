# 🖼️ Product Image Scraper

This project is designed for e-commerce affiliates and automates the process of scraping product images from online stores (currently supports Shopee and Magazine Luiza), cropping and resizing them, and placing them onto a custom background.

## 🚀 Features

- Scrape product images from a list of product URLs
- Automatically crop and resize images based on predefined rules
- Overlay images onto a custom background
- Save processed images in a structured folder system
- Send product images and links via WhatsApp (optional)

## 🧰 Requirements

- Python 3.10+
- Selenium
- Pillow
- PyAutoGUI
- Other dependencies listed in `requirements.txt`

## 📁 Project Structure

```
project/
│
├── sites/       # Modules for site-specific scraping (Shopee, Magalu) and WhatsApp integration
├── utils/       # Reusable helper functions for browser automation, image processing, etc.
├── config/      # Configuration files and input controls
├── logs/        # Execution and error logs
├── data/        # Input data, processed images, and output texts
└── main.py      # Entry point of the application
```

## 🔧 Setup & Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/product-image-scraper.git
   cd product-image-scraper
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## 📌 Notes

- Make sure Chrome and the appropriate ChromeDriver version are installed.
- Product URLs should be added to the appropriate config file before execution.
- WhatsApp functionality requires the desktop app to be open and logged in.

## 📄 License

This project is open-source and available under LICENSE.
