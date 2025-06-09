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
SITE_MAGALU = "https://www.magazinevoce.com.br/magazinedescubrapromoss/"
SITE_SHOPEE = "https://s.shopee.com.br/\n"
SITE_SHOPEE_PRODUCT = "https://s.shopee.com.br/9KUhKhkX8n"
LOGIN_SHOPEE = "https://shopee.com.br/buyer/login"

#Set browser settings
TIME_TO_WAIT_10 = 10
TIME_TO_WAIT_5 = 5
OPTIONS_BROWSER = ('--start-maximized','--disable-blink-features=AutomationControlled','user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36')
MOVE_MOUSE = (375, 850)
MAGALU_XPATHS = ["/html/body/div/div/main/section[1]","/html/body/div/div/main/section[2]/div[1]","/html/body/div[1]/div/main/section[2]/div[2]/span","/html/body/div/div/main/section[2]/div[1]","/html/body/div/div/main/section[4]/div[9]",'//*[contains(@class, "sc-fqkvVR") and contains(@class, "gbbVVp")]','//*[contains(@class, "sc-iGgWBj") and contains(@class, "fMMVmr")]','//*[contains(@class, "container-banner-cookie")]','//*[contains(@class, "sc-bwjutS") and contains(@class, "llnpdR")]']
MAGALU_CSS = ["mod-attributelist","mod-sellerdetails","mod-deliveryguarantee","mod-bestinstallment","coupon-code-copy","buyButton","bagButton","shipping"]
MAGALU_CLASSES = ["csNtH", "dpKtiF"]
SHOPEE_CLASSES = ["wV4oFQ", "jw_y2_"]
WHATSAPP_XPATHS = ['(//span[@aria-label=" Entregue "])[last()]', '(//span[@aria-label=" Enviada "])[last()]']

#Set paths general
ROOT_FOLDER = Path(__file__).parent.parent
DATA_FOLDER = ROOT_FOLDER / 'data'
COOKIES_WHATSAPP = DATA_FOLDER / 'Cookies' / 'cookies_whatsapp.pkl'
COOKIES_SHOPEE = DATA_FOLDER / 'Cookies' / 'cookies_shopee.pkl'
COOKIES_MAGALU = DATA_FOLDER / 'Cookies' / 'cookies_magalu.pkl'
MAGALU_URLS = DATA_FOLDER / 'Texts' / 'Magalu_urls.txt'
SHOPEE_URLS = DATA_FOLDER / 'Texts' / 'Shopee_urls.txt'
PRODUCTS_URLS = DATA_FOLDER / 'Texts' / 'Products_urls.txt'
WHATSAPP_URLS = DATA_FOLDER / 'Texts' / 'Whatsapp_urls.txt'
FAIL_TO_SEND = DATA_FOLDER / 'Texts' / 'Fail_to_send_urls.txt'
VIDEOS_URL = DATA_FOLDER / 'Texts' / 'Videos_urls.txt'
BACKGROUND = DATA_FOLDER / 'Images' / 'Background.jpeg'
PROMO_IMAGES = DATA_FOLDER / 'Images' / 'Promos_Images'
FILE_LOG = ROOT_FOLDER / 'logs' / 'logfile.log'

#Set images settings for Shopee products
SHOPEE_RESIZE_1 = (560, 130)
SHOPEE_RESIZE_2 = (560, 675)
SHOPEE_POSITION_1 = (77, 815)
SHOPEE_POSITION_2 = (77, 140)
SHOPEE_CROP_1 = (810, 220, 1677, 435)
SHOPEE_CROP_2 = (217, 238, 784, 920)

#Set images settings for Magalu products
MAGALU_RESIZE_1 = (560, 675)
MAGALU_RESIZE_2 = (560, 130)
MAGALU_POSITION_1 = (77, 140)
MAGALU_POSITION_2 = (77, 815)
MAGALU_CROP_1 = (100, 15, 1230, 900)
MAGALU_CROP_2 = (1250, 120, 1615, 310)