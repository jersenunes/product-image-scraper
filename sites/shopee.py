# type: ignore
import os
import time
from config.settings import *
from utils.utils_helpers import *
from utils.utils_browser import *
from utils.utils_image import *

'''
Get product images from Shopee website
Crop and resize products images
Overlay products images in background image
'''

def get_images_promo_shopee():
    main()

def main():
    browser = browser_make_chrome_browser(OPTIONS_BROWSER)

    cookies_status = browser_load_cookies(browser=browser, cookies_path=COOKIES_SHOPEE, url=SITE_SHOPEE_PRODUCT)

    if cookies_status == False:
        browser = browser_login_to_site(browser=browser, username=SHOPEE_USERNAME,
                                        password=SHOPEE_PASSWORD, login_url=LOGIN_SHOPEE)

        browser_get_site(browser=browser, url=SITE_SHOPEE_PRODUCT)

        browser_save_cookies(browser=browser, cookies_path=COOKIES_SHOPEE)

    time.sleep(TIME_TO_WAIT_10)


    if os.path.exists(SHOPEE_URLS):
        review_list(path_list=SHOPEE_URLS)
        url_list = read_file(SHOPEE_URLS)

        round_value = 0

        for url in url_list:
            round_value += 1
            if round_value > PRODUCT_LIMIT:
                break
            else:
                if os.path.exists(PRODUCTS_URLS):
                    
                    products_url = read_file(PRODUCTS_URLS)
                    if url in products_url:
                        continue
        
                FULL_IMAGE = make_path(url=url, option="image_full")
                IMAGE_FINAL = make_path(url=url, option="image_final")
                FIRST_CUT = make_path(url=url, option="image_first")
                SECOND_CUT = make_path(url=url, option="image_second")

                browser_get_site(browser=browser, url=url)
                
                browser_wait_for_site_to_load(browser=browser)

                PRODUCT_NAME = browser_get_title(browser=browser)

                if check_for_product_registered(path=PRODUCTS_URLS_JSON, product_name=PRODUCT_NAME):
                    continue
                
                if browser_detect_and_skip(browser=browser):
                    continue

                browser_enable_full_screen(browser=browser)                

                move_mouse()
                    
                browser_save_screenshot(browser=browser, path=FULL_IMAGE)

                image_crop_and_resize(path_full=FULL_IMAGE,
                                        path_1=FIRST_CUT, path_2=SECOND_CUT,
                                        crop_1=SHOPEE_CROP_1, crop_2=SHOPEE_CROP_2,
                                        resize_1=SHOPEE_RESIZE_1, resize_2=SHOPEE_RESIZE_2)

                image_overlay_background(path_background=BACKGROUND, path_final=IMAGE_FINAL,
                                            path_1=FIRST_CUT, path_2=SECOND_CUT,
                                            position_1=SHOPEE_POSITION_1, position_2=SHOPEE_POSITION_2)
                
                PRODUCT_VIDEO = browser_get_video(browser=browser)
                PRODUCT_PRICE = browser_get_price(browser=browser)
                PRODUCT_HREF = browser_get_href_product(browser=browser)

                save_a_json(path=PRODUCTS_URLS_JSON, args=[SHOPEE_NAME, PRODUCT_NAME, PRODUCT_PRICE, PRODUCT_HREF, url, PRODUCT_VIDEO])
                write_a_file(path=PRODUCTS_URLS, text=url, type="a")

                delete_file(path_file = FULL_IMAGE)
                delete_file(path_file = FIRST_CUT)
                delete_file(path_file = SECOND_CUT)                

    browser_quit(browser=browser)

    review_products_names(products_path=PRODUCTS_URLS, images_path=PROMO_IMAGES, site=SITE_SHOPEE)

    clean_products_selected(initial_path=SHOPEE_URLS, selected_path=PRODUCTS_URLS)

if __name__ == "__main__":
    main()