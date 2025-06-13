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
    main()

def main():
    browser = browser_make_chrome_browser(OPTIONS_BROWSER)

    browser_get_site(browser=browser, url=SITE_WHATSAPP)
    time.sleep(TIME_TO_WAIT_10*2)

    browser_get_group_name(browser=browser, group_name=GROUP_WHATSAPP)

    if os.path.exists(PRODUCTS_URLS):
        url_list = read_file(PRODUCTS_URLS)

        for url in url_list:
            if os.path.exists(WHATSAPP_URLS):
                whatsapp_urls = read_file(WHATSAPP_URLS)
                if url in whatsapp_urls:
                    continue

                send_status = False

                IMAGE = make_path(url=url, option="image_final")

                browser_get_attachment(browser=browser, path=IMAGE)

                send_status = browser_send_message(browser=browser, message=url)

                if send_status:
                    print(f"Success in uploading the image: {url}")
                    write_a_file(path=WHATSAPP_URLS, text=url, type="a")
                else:
                    print(f"Failed in uploading the image: {url}")
                    write_a_file(path=FAIL_TO_SEND, text=url, type="a")

                time.sleep(TIME_TO_WAIT_5)

    browser_quit(browser)

    clean_products_selected(initial_path=PRODUCTS_URLS, selected_path=WHATSAPP_URLS)

if __name__ == "__main__":
    main()