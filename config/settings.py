import os
from pathlib import Path
from dotenv import load_dotenv

#Set .env variables
load_dotenv()
SHOPEE_USERNAME = os.getenv('SHOPEE_USERNAME')
SHOPEE_PASSWORD = os.getenv('SHOPEE_PASSWORD')


#Set general settings
SHOPEE_NAME = "Shopee"
MAGALU_NAME = "Magalu"
PRODUCT_LIMIT = 50
TIME_TO_WAIT_10 = 10
TIME_TO_WAIT_5 = 5
MOVE_MOUSE = (375, 850)

#Set urls settings
SITE_WHATSAPP = "https://web.whatsapp.com"
GROUP_WHATSAPP = "Descubra Promoss"
SITE_MAGALU = "https://www.magazinevoce.com.br/magazinedescubrapromoss/"
SITE_SHOPEE = "https://s.shopee.com.br/\n"
SITE_SHOPEE_PRODUCT = "https://s.shopee.com.br/VtNOK1R0i"
LOGIN_SHOPEE = "https://shopee.com.br/buyer/login"


#Set browser settings
OPTIONS_BROWSER = ('--start-maximized','--disable-blink-features=AutomationControlled','user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36')
HIDDEN_XPATH = ["/html/body/div/div/main/section[1]","/html/body/div/div/main/section[2]/div[1]","/html/body/div[1]/div/main/section[2]/div[2]/span","/html/body/div/div/main/section[2]/div[1]","/html/body/div/div/main/section[4]/div[9]",'//*[contains(@class, "sc-fqkvVR") and contains(@class, "gbbVVp")]','//*[contains(@class, "sc-iGgWBj") and contains(@class, "fMMVmr")]','//*[contains(@class, "container-banner-cookie")]','//*[contains(@class, "sc-bwjutS") and contains(@class, "llnpdR")]']
HIDDEN_CSS = ["mod-attributelist","mod-sellerdetails","mod-deliveryguarantee","mod-bestinstallment","coupon-code-copy","buyButton","bagButton","shipping"]
CLASSES_TO_SKIP = ["csNtH", "dpKtiF", "wV4oFQ", "jw_y2_", "kkBEei"]
PRODUCTS_NAMES = ['div.WBVL_7 > h1.vR6K3w', 'div[data-testid="mod-headingproduct"]']
CANONICAL = '//link[@rel="canonical"]'
PRICE_CSS = ".IZPeQz.B67UQ0"
USERNAME_CLASS = "navbar__username"
WHATSAPP_XPATHS = ['(//span[@aria-label=" Entregue "])[last()]', '(//span[@aria-label=" Enviada "])[last()]']


#Set paths
ROOT_FOLDER = Path(__file__).parent.parent
#Path LogFile
FILE_LOG = ROOT_FOLDER / 'logs' / 'logfile.log'
#Path Folders
IMAGES_FOLDER = ROOT_FOLDER / 'data' / 'Images'
URLS_FOLDER = ROOT_FOLDER / 'data' / 'Urls'
COOKIES_FOLDER = ROOT_FOLDER / 'data' / 'Cookies'
#Path Cookies
COOKIES_WHATSAPP = COOKIES_FOLDER / 'cookies_whatsapp.pkl'
COOKIES_SHOPEE = COOKIES_FOLDER / 'cookies_shopee.pkl'
COOKIES_MAGALU = COOKIES_FOLDER / 'cookies_magalu.pkl'
#Path Urls
MAGALU_URLS = URLS_FOLDER / 'Magalu_urls.txt'
SHOPEE_URLS = URLS_FOLDER / 'Shopee_urls.txt'
PRODUCTS_URLS = URLS_FOLDER / 'Products_urls.txt'
PRODUCTS_URLS_JSON = URLS_FOLDER / 'Products_urls.json'
WHATSAPP_URLS = URLS_FOLDER / 'Whatsapp_urls.txt'
FAIL_TO_SEND = URLS_FOLDER / 'Fail_to_send_urls.txt'
VIDEOS_URL = URLS_FOLDER / 'Videos_urls.txt'
#Path Images
BACKGROUND = IMAGES_FOLDER / 'Background.jpeg'
PROMO_IMAGES = IMAGES_FOLDER / 'Promos_Images'


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