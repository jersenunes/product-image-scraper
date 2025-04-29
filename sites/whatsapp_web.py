# type: ignore
import os
import time
from config.settings import *
from utils.utils_helpers import *
from utils.utils_browser import *

def send_images_to_whatsapp():
    main()

def main():
    #Making browser with webdriver and does login to site
    browser = browser_make_chrome_browser(OPTIONS_BROWSER)
    
    #Get site
    browser_get_site(browser=browser, url=SITE_WHATSAPP)
    time.sleep(TIME_TO_WAIT*2)

    #Get group
    browser_get_group_name(browser=browser, group_name=GROUP_WHATSAPP)
    
    #Import the lists
    url_list = read_file(PRODUCTS_SELECTED)
    sended_whatsapp = read_file(SENDED_WHATSAPP)

    for url in url_list:
        if url in sended_whatsapp:
            continue

        send_status = False
        #Make path for image
        IMAGE = make_variables(url=url, path=PROMO_IMAGES, site=SITE_SHOPEE, image_type="final")

        #Get attachment
        browser_get_attachment(browser=browser, path=IMAGE)

        #Send message
        send_status = browser_set_message(browser=browser, message=url)

        if send_status:
            print(f"Success in uploading the image: {url}")
            write_a_file(path=SENDED_WHATSAPP, url=url)
        else:
            print(f"Failed in uploading the image: {url}")
            write_a_file(path=FAIL_TO_SEND, url=url)
        time.sleep(5)

    browser_quit(browser)

if __name__ == "__main__":
    main()