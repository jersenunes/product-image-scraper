# type: ignore
import os
import time
from datetime import datetime
from config.settings import *
from utils.utils_helpers import *
from utils.utils_browser import *
from utils.utils_image import *


def get_images_promo_shopee():
    main()

def main():
    log_message(path=FILE_LOG, message="Started the script.")

    #Making browser with webdriver and does login to site
    browser = browser_make_chrome_browser(OPTIONS_BROWSER)

    #Load cookies to use
    cookies_status = browser_load_cookies(browser=browser, cookies_path=COOKIES_SHOPEE, url=SITE_SHOPEE_PRODUCT)

    print(f"Cookies status is: {cookies_status}")
    #Check for cookies
    if cookies_status == False:
        browser = browser_login_to_site(browser=browser, username=SHOPEE_USERNAME,
                                        password=SHOPEE_PASSWORD, login_url=LOGIN_SHOPEE,
                                        time_wait=TIME_TO_WAIT)
        
        #Time sleep for user solve the captcha
        time.sleep(TIME_TO_WAIT*6)

        #Get product url to next step of save cookies
        browser_get_site(browser=browser, url=SITE_SHOPEE_PRODUCT)

        #Save cookies to reuse again
        browser_save_cookies(browser=browser, cookies_path=COOKIES_SHOPEE)

    #Time sleep
    time.sleep(TIME_TO_WAIT)

    #Import the products url list
    url_list = read_file(PRODUCTS_URL)

    #Perform FOR in products url list for get products
    for url in url_list:
        
        #Get paths for images that will be edited
        FULL_IMAGE = make_variables(url=url, path=PROMO_IMAGES, site=SITE_SHOPEE, image_type="full")
        IMAGE_FINAL = make_variables(url=url, path=PROMO_IMAGES, site=SITE_SHOPEE, image_type="final")
        FIRST_CUT = make_variables(url=url, path=PROMO_IMAGES, site=SITE_SHOPEE, image_type="first")
        SECOND_CUT = make_variables(url=url, path=PROMO_IMAGES, site=SITE_SHOPEE, image_type="second")

        #Open product url in browser
        browser.get(url)
        
        #Time sleep for site load totally
        browser_wait_for_site_to_load(browser=browser, time_wait=TIME_TO_WAIT)
        
        #Verify for offers and take a decision
        if browser_detect_and_skip_offer(browser):
            continue

        #Enable full screen in browser
        browser_enable_full_screen(browser=browser)
        
        #Detect video url and save it in the file
        browser_detect_video(browser=browser, move_mouse=MOVE_MOUSE, url=url)
            
        
        #Save screenshot
        browser_save_screenshot(browser=browser, path=FULL_IMAGE)

        #Crop and resize products images
        image_crop_and_resize(path_full=FULL_IMAGE,
                                 path_1=FIRST_CUT, path_2=SECOND_CUT,
                                 crop_1=SHOPEE_CROP_1, crop_2=SHOPEE_CROP_2,
                                 resize_1=SHOPEE_RESIZE_1, resize_2=SHOPEE_RESIZE_2
                                 )

        #Overlay products images in background image
        image_overlay_background(path_background=BACKGROUND, path_final=IMAGE_FINAL,
                                    path_1=FIRST_CUT, path_2=SECOND_CUT,
                                    position_1=SHOPEE_POSITION_1, position_2=SHOPEE_POSITION_2)
        
        #Save the current url in file
        write_a_file(path=PRODUCTS_SELECTED, url=url)

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
    review_products_names(products_path=PRODUCTS_SELECTED, images_path=PROMO_IMAGES, site=SITE_SHOPEE)

    #Clean the "Products Urls.txt" file, removing the URLs used to generate the images
    clean_products_selected(initial_path=PRODUCTS_URL, selected_path=PRODUCTS_SELECTED)

    #Review the "Videos_urls.txt" file, removing the duplicates
    review_video_urls(path_videos=VIDEOS_URL)

if __name__ == "__main__":
    main()