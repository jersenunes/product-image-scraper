# type: ignore
import os
import time
from datetime import datetime
from config.settings import *
from utils.utils_helpers import *
from utils.utils_browser import *
from utils.utils_image import *

def main():
    log_message(path=FILE_LOG, message="Started the script.")

    #Making browser with webdriver and does login to site
    browser = browser_make_chrome_browser(OPTIONS_BROWSER)

    #Load cookies to use
    cookies_status = browser_load_cookies(browser=browser, cookies_path=COOKIES, url=SITE_URL_PRODUCT)

    print(f"Cookies status is: {cookies_status}")
    #Check for cookies
    if cookies_status == False:
        browser = browser_login_to_site(browser=browser, username=SHOPEE_USERNAME,
                                        password=SHOPEE_PASSWORD, login_url=LOGIN_URL,
                                        time_wait=TIME_TO_WAIT)
        
        #Time sleep for user solve the captcha
        time.sleep(TIME_TO_WAIT*6)

        #Get product url to next step of save cookies
        browser_get_site(browser=browser, url=SITE_URL_PRODUCT)

        #Save cookies to reuse again
        browser_save_cookies(browser=browser, cookies_path=COOKIES)

    #Time sleep
    time.sleep(TIME_TO_WAIT)

    #Import the products url list
    url_list = read_file(PRODUCTS_URL)

    #Perform FOR in products url list for get products
    for url in url_list:
        
        #Get paths for images that will be edited
        FULL_IMAGE = make_variables(url=url, path=PROMO_IMAGES, site=SITE_URL, image_type="full")
        IMAGE_FINAL = make_variables(url=url, path=PROMO_IMAGES, site=SITE_URL, image_type="final")
        FIRST_CUT = make_variables(url=url, path=PROMO_IMAGES, site=SITE_URL, image_type="first")
        SECOND_CUT = make_variables(url=url, path=PROMO_IMAGES, site=SITE_URL, image_type="second")

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
        video_url = browser_detect_video(browser=browser, move_mouse=MOVE_MOUSE)
        if video_url:
            write_a_file(path=VIDEOS_URL, url=url, video_url=video_url)
        
        #Save screenshot
        browser_save_screenshot(browser=browser, path=FULL_IMAGE)

        #Crop and resize products images
        image_crop_and_resize(path_full=FULL_IMAGE,
                                 path_1=FIRST_CUT, path_2=SECOND_CUT,
                                 crop_1=FIRST_CROP, crop_2=SECOND_CROP,
                                 resize_1=FIRST_RESIZE, resize_2=SECOND_RESIZE
                                 )

        #Overlay products images in background image
        image_overlay_background(path_background=BACKGROUND, path_final=IMAGE_FINAL,
                                    path_1=FIRST_CUT, path_2=SECOND_CUT,
                                    position_1=FIRST_POSITION, position_2=SECOND_POSITION)
        
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
    review_products_names(products_path=PRODUCTS_SELECTED, images_path=PROMO_IMAGES, site=SITE_URL)

    #Clean the "Products Urls.txt" file, removing the URLs used to generate the images
    clean_products_selected(initial_path=PRODUCTS_URL, selected_path=PRODUCTS_SELECTED)

if __name__ == "__main__":
    main()