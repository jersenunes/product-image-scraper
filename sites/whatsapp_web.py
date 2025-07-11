# type: ignore
import os
import time
from config.settings import *
from utils.utils_helpers import *
from utils.utils_browser import *

'''
Check for generated product images
Open Whatsapp Web in the browser
Send product images to the Whatsapp group
'''

def send_images_to_whatsapp():
    browser = browser_make_chrome_browser(OPTIONS_BROWSER)

    browser_get_site(browser=browser, url=SITE_WHATSAPP)
    time.sleep(TIME_TO_WAIT_10*3)

    browser_get_group_name(browser=browser)

    if os.path.exists(PRODUCTS_URLS_JSON):
        json_list = read_a_json(path=PRODUCTS_URLS_JSON)

        for item in json_list.values():
            if os.path.exists(WHATSAPP_URLS):
                whatsapp_urls = read_file(WHATSAPP_URLS)
                if item.get("ShortLink") in whatsapp_urls:
                    continue

                send_status = False

                IMAGE = make_path(url=item.get("ShortLink"), option="image_final")

                browser_get_attachment(browser=browser, path=IMAGE)

                send_status = browser_send_message(browser=browser, message=item)
                
                if send_status:
                    print(f"Success in uploading the image: {item.get("ShortLink")}")
                    write_a_file(path=WHATSAPP_URLS, text=item.get("ShortLink"), type="a")
                else:
                    print(f"Failed in uploading the image: {item.get("ShortLink")}")
                    write_a_file(path=FAIL_TO_SEND, text=item.get("ShortLink"), type="a")

                time.sleep(TIME_TO_WAIT_5)

    browser_quit(browser)

    clean_products_selected(initial_path=PRODUCTS_URLS, selected_path=WHATSAPP_URLS)

if __name__ == "__main__":
    send_images_to_whatsapp()