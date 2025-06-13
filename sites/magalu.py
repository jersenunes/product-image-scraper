# type: ignore
import os
import time
from config.settings import *
from utils.utils_helpers import *
from utils.utils_browser import *
from utils.utils_image import *

'''
Get product images from Magalu website
Crop and resize products images
Overlay products images in background image
'''

def get_images_promo_magalu():
    main()

def main():
    browser = browser_make_chrome_browser(OPTIONS_BROWSER)

    if os.path.exists(MAGALU_URLS):
        url_list = read_file(MAGALU_URLS)

        for url in url_list:
            if os.path.exists(PRODUCTS_URLS):
                products_url = read_file(PRODUCTS_URLS)
                if url in products_url:
                    continue

            browser_get_site(browser=browser, url=url)

            time.sleep(TIME_TO_WAIT_5)

            if browser_detect_and_skip(browser=browser, option="magalu"):
                continue

            FULL_IMAGE = make_path(url=url, option="image_full")
            IMAGE_FINAL = make_path(url=url, option="image_final")
            FIRST_CUT = make_path(url=url, option="image_first")
            SECOND_CUT = make_path(url=url, option="image_second")

            browser_hidden_class(browser=browser)

            browser_modify_width_title(browser=browser)

            browser_save_screenshot(browser=browser, path=FULL_IMAGE)

            MAGALU_CROP_3 = browser_checking_characters_number(browser)

            if MAGALU_CROP_3:
                image_crop_and_resize(path_full=FULL_IMAGE,
                                        path_1=FIRST_CUT, path_2=SECOND_CUT,
                                        crop_1=MAGALU_CROP_1, crop_2=MAGALU_CROP_3,
                                        resize_1=MAGALU_RESIZE_1, resize_2=MAGALU_RESIZE_2)
            else:
                image_crop_and_resize(path_full=FULL_IMAGE,
                                        path_1=FIRST_CUT, path_2=SECOND_CUT,
                                        crop_1=MAGALU_CROP_1, crop_2=MAGALU_CROP_2,
                                        resize_1=MAGALU_RESIZE_1, resize_2=MAGALU_RESIZE_2)

            image_overlay_background(path_background=BACKGROUND, path_final=IMAGE_FINAL,
                                        path_1=FIRST_CUT, path_2=SECOND_CUT,
                                        position_1=MAGALU_POSITION_1, position_2=MAGALU_POSITION_2)

            write_a_file(path=PRODUCTS_URLS, text=url, type="a")

            delete_file(path_file = FULL_IMAGE)
            delete_file(path_file = FIRST_CUT)
            delete_file(path_file = SECOND_CUT)

    browser_quit(browser=browser)

    review_products_names(products_path=PRODUCTS_URLS, images_path=PROMO_IMAGES, site=SITE_MAGALU)

    clean_products_selected(initial_path=MAGALU_URLS, selected_path=PRODUCTS_URLS)

if __name__ == "__main__":
    main()