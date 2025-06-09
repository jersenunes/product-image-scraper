# type: ignore
import os
import time
from config.settings import *
from utils.utils_helpers import *
from utils.utils_browser import *
from utils.utils_image import *

def get_images_promo_magalu():
    main()

def main():
    #Making browser with webdriver
    browser = browser_make_chrome_browser(OPTIONS_BROWSER)

    #Import the products url list
    if os.path.exists(MAGALU_URLS):
        url_list = read_file(MAGALU_URLS)

        #Perform FOR in url_list for get each url product
        for url in url_list:
            if os.path.exists(PRODUCTS_URLS):
                #Import the products_url PRODUCTS_URLS
                products_url = read_file(PRODUCTS_URLS)

                #Checking if the url has already been selected
                if url in products_url:
                    continue

            #Open product url in browser
            browser_get_site(browser=browser, url=url)

            #Time sleep for site load totally
            time.sleep(TIME_TO_WAIT_5)

            #Checking classes for url skip
            if browser_detect_and_skip(browser=browser, option="magalu"):
                continue

            #Make paths for images that will be edited
            FULL_IMAGE = make_path(url=url, option="image_full")
            IMAGE_FINAL = make_path(url=url, option="image_final")
            FIRST_CUT = make_path(url=url, option="image_first")
            SECOND_CUT = make_path(url=url, option="image_second")

            #Trying remove the section header
            browser_hidden_class(browser=browser)

            #Trying to modify the width of the product title
            browser_modify_width_title(browser=browser)

            #Save screenshot
            browser_save_screenshot(browser=browser, path=FULL_IMAGE)

            #Checking the size of the product title in characters
            MAGALU_CROP_3 = browser_checking_characters_number(browser)

            #Crop and resize products images
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
            
            #Overlay products images in background image
            image_overlay_background(path_background=BACKGROUND, path_final=IMAGE_FINAL,
                                        path_1=FIRST_CUT, path_2=SECOND_CUT,
                                        position_1=MAGALU_POSITION_1, position_2=MAGALU_POSITION_2)

            #Save the current url in file
            write_a_file(path=PRODUCTS_URLS, text=url, type="a")

            #Remove images that are not needed
            if os.path.exists(FULL_IMAGE):
                os.remove(FULL_IMAGE)
            if os.path.exists(FIRST_CUT):
                os.remove(FIRST_CUT)
            if os.path.exists(SECOND_CUT):
                os.remove(SECOND_CUT)

    #Close the browser driver
    browser_quit(browser=browser)

    #Review the products names and fix it
    review_products_names(products_path=PRODUCTS_URLS, images_path=PROMO_IMAGES, site=SITE_MAGALU)

    #Clean the "Products Urls.txt" file, removing the URLs used to generate the images
    clean_products_selected(initial_path=MAGALU_URLS, selected_path=PRODUCTS_URLS)

if __name__ == "__main__":
    main()