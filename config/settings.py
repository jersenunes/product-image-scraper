import os
from pathlib import Path
from dotenv import load_dotenv

#Set .env variables
load_dotenv()
SHOPEE_USERNAME = os.getenv('SHOPEE_USERNAME')
SHOPEE_PASSWORD = os.getenv('SHOPEE_PASSWORD')

#Set urls settings
SITE_WHATSAPP = "https://web.whatsapp.com"
GROUP_WHATSAPP = "Descubra Promoss"
SITE_SHOPEE = "https://s.shopee.com.br/\n"
SITE_SHOPEE_PRODUCT = "https://s.shopee.com.br/9KUhKhkX8n"
LOGIN_SHOPEE = "https://shopee.com.br/buyer/login"

#Set browser settings
TIME_TO_WAIT = 10
OPTIONS_BROWSER = ('--start-maximized','--disable-blink-features=AutomationControlled','user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36')
MOVE_MOUSE = (375, 850)

#Set paths
ROOT_FOLDER = Path(__file__).parent.parent
COOKIES_WHATSAPP = ROOT_FOLDER / 'data' / 'Cookies' / 'cookies_whatsapp.pkl'
COOKIES_SHOPEE = ROOT_FOLDER / 'data' / 'Cookies' / 'cookies_shopee.pkl'
PRODUCTS_URL = ROOT_FOLDER / 'data' / 'Texts' / 'Products_urls.txt'
PRODUCTS_SELECTED = ROOT_FOLDER / 'data' / 'Texts' / 'Products_selected_urls.txt'
SENDED_WHATSAPP = ROOT_FOLDER / 'data' / 'Texts' / 'Sended_to_whatsapp_urls.txt'
FAIL_TO_SEND = ROOT_FOLDER / 'data' / 'Texts' / 'Fail_to_send_urls.txt'
VIDEOS_URL = ROOT_FOLDER / 'data' / 'Texts' / 'Videos_urls.txt'
BACKGROUND = ROOT_FOLDER / 'data' / 'Images' / 'Background.jpeg'
PROMO_IMAGES = ROOT_FOLDER / 'data' / 'Images' / 'Promos_Images'
FILE_LOG = ROOT_FOLDER / 'logs' / 'logfile.log'

#Set images settings
SHOPEE_RESIZE_1 = (560, 130)
SHOPEE_RESIZE_2 = (560,675)
SHOPEE_POSITION_1 = (77, 815)
SHOPEE_POSITION_2 = (77, 140)
SHOPEE_CROP_1 = (810, 220, 1677, 435)
SHOPEE_CROP_2 = (217, 238, 784, 920)