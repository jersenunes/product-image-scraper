import os
from pathlib import Path
from dotenv import load_dotenv

#Set .env variables
load_dotenv()
SHOPEE_USERNAME = os.getenv('SHOPEE_USERNAME')
SHOPEE_PASSWORD = os.getenv('SHOPEE_PASSWORD')

#Set urls settings
SITE_URL = "https://s.shopee.com.br/\n"
SITE_URL_PRODUCT = "https://s.shopee.com.br/9KUhKhkX8n"
LOGIN_URL = "https://shopee.com.br/buyer/login"

#Set browser settings
TIME_TO_WAIT = 10
OPTIONS_BROWSER = ('--start-maximized','--disable-blink-features=AutomationControlled','user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36')
MOVE_MOUSE = (375, 850)

#Set paths
ROOT_FOLDER = Path(__file__).parent.parent
COOKIES = ROOT_FOLDER / 'data' / 'Cookies' / 'cookies.pkl'
PRODUCTS_URL = ROOT_FOLDER / 'data' / 'Texts' / 'Products_urls.txt'
PRODUCTS_SELECTED = ROOT_FOLDER / 'data' / 'Texts' / 'Products_selected_urls.txt'
VIDEOS_URL = ROOT_FOLDER / 'data' / 'Texts' / 'Videos_urls.txt'
BACKGROUND = ROOT_FOLDER / 'data' / 'Images' / 'Background.jpeg'
PROMO_IMAGES = ROOT_FOLDER / 'data' / 'Images' / 'Promos_Images'
FILE_LOG = ROOT_FOLDER / 'logs' / 'logfile.log'

#Set images settings
FIRST_RESIZE = (560, 130)
SECOND_RESIZE = (560,675)
FIRST_POSITION = (77, 815)
SECOND_POSITION = (77, 140)
FIRST_CROP = (810, 220, 1677, 435)
SECOND_CROP = (217, 238, 784, 920)