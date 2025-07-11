# type: ignore
import time
import pickle
import inspect
from config.settings import *
from utils.utils_helpers import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def browser_make_chrome_browser(options: str) -> webdriver.Chrome:
    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    try:
        chrome_options = webdriver.ChromeOptions()
        if options is not None:
            for option in options:
                chrome_options.add_argument(option)
                log_message(path=FILE_LOG, message=f"INFORMATIONAL: {option} argument added to ChromeOptions.")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        log_message(path=FILE_LOG, message="INFORMATIONAL: Experimental options added to ChromeOptions.")
        browser = webdriver.Chrome(options=chrome_options)
        log_message(path=FILE_LOG, message="INFORMATIONAL: Chrome browser webdriver created with success.")
        browser.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument",
            {"source": """
                Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
                });
            """},)
        log_message(path=FILE_LOG, message="INFORMATIONAL: Executed JavaScript to remove the webdriver property.")
        return browser
    except Exception as e:
        log_message(path=FILE_LOG, message=f"ERROR: {e}.")

def browser_login_to_site(browser, username, password, login_url) -> webdriver.Chrome:
    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    login_success = False

    while login_success == False:
        try:
            browser.get(login_url)
            log_message(path=FILE_LOG, message=f"INFORMATIONAL: Browser get url {login_url}.")

            element_username = WebDriverWait(browser, TIME_TO_WAIT_10).until(
                EC.presence_of_element_located((By.NAME, 'loginKey')))
            element_password = WebDriverWait(browser, TIME_TO_WAIT_10).until(
                EC.presence_of_element_located((By.NAME, 'password')))
            
            element_username.send_keys(username)
            element_password.send_keys(password)
            time.sleep(1)
            element_password.send_keys(Keys.ENTER)
            log_message(path=FILE_LOG, message="INFORMATIONAL: Used credentials to login.")

            # login_success = bool(WebDriverWait(browser, TIME_TO_WAIT_10*3).until(
            #     EC.presence_of_element_located((By.CLASS_NAME, 'Y6xFir'))))
            time.sleep(TIME_TO_WAIT_10*3)
            if browser_check_login(browser=browser):
                break

        except Exception as e:            
            log_message(path=FILE_LOG, message=f"ERROR: {e}.")
            log_message(path=FILE_LOG, message="INFORMATIONAL: Trying again...")
            
            browser.quit()
    return browser

def browser_check_login(browser) -> bool:
    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    try:
        log_message(path=FILE_LOG, message="INFORMATIONAL: Checking if login was successful.")
        login_success = WebDriverWait(browser, TIME_TO_WAIT_10*3).until(EC.presence_of_element_located((By.CLASS_NAME, USERNAME_CLASS)))
        if login_success.text == SHOPEE_USERNAME:
            log_message(path=FILE_LOG, message="INFORMATIONAL: Login with success.")
            return True
        log_message(path=FILE_LOG, message="INFORMATIONAL: Failed to login.")

    except Exception as e:
        log_message(path=FILE_LOG, message=f"ERROR: {e}.")

def browser_save_cookies(browser, cookies_path) -> None:
    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    try:
        make_folder(path_folder=cookies_path)
        with open(cookies_path, "wb") as file:
            pickle.dump(browser.get_cookies(), file)
            log_message(path=FILE_LOG, message="INFORMATIONAL: Browser cookies have been saved.")
        time.sleep(1)
    except Exception as e:
        log_message(path=FILE_LOG, message=f"ERROR: {e}.")

def browser_load_cookies(browser, cookies_path, url) -> bool:
    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    try:
        make_folder(path_folder=cookies_path)
        browser_get_site(browser=browser, url=url)
        log_message(path=FILE_LOG, message=f"INFORMATIONAL: Browser get url {url}.")
        time.sleep(3)

        log_message(path=FILE_LOG, message="INFORMATIONAL: Checking for cookies.")
        if os.path.exists(cookies_path):
            with open(cookies_path, "rb") as file:
                cookies = pickle.load(file)
                
                for cookie in cookies:
                    cookie.pop('sameSite', None)
                    browser.add_cookie(cookie)
                log_message(path=FILE_LOG, message="INFORMATIONAL: Browser cookies have been loaded.")

            browser_get_site(browser=browser, url=url)
  
            if browser_check_login(browser=browser):
                return True
        
        log_message(path=FILE_LOG, message="INFORMATIONAL: There are no saved browser cookies.")
        return False
    except Exception as e:
        log_message(path=FILE_LOG, message=f"ERROR: {e}.")
        return False

def browser_get_site(browser, url) -> None:
    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    try:
        browser.get(url)
        log_message(path=FILE_LOG, message=f"INFORMATIONAL: Browser get url {url.strip('\n')}")
        time.sleep(3)
    except Exception as e:
        log_message(path=FILE_LOG, message=f"ERROR: {e}.")

def browser_wait_for_site_to_load(browser) -> None:
    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    try:
        WebDriverWait(browser, TIME_TO_WAIT_10).until(
            EC.presence_of_element_located((By.CLASS_NAME, '_OguPS')))
        log_message(path=FILE_LOG, message=f"INFORMATIONAL: Page url loaded.")
    except Exception as e:
        log_message(path=FILE_LOG, message=f"ERROR: {e}.")

def browser_enable_full_screen(browser) -> None:
    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    try:
        title_name = browser.find_element(By.CLASS_NAME, "WBVL_7")
        ActionChains(browser).move_to_element_with_offset(title_name, 10, 10).click().perform()
        log_message(path=FILE_LOG, message="INFORMATIONAL: Initial click on title performed.")

        time.sleep(0.5)

        browser.execute_script("""
            if (document.fullscreenElement == null) {
                document.documentElement.requestFullscreen();
            }
        """)
        log_message(path=FILE_LOG, message="INFORMATIONAL: Enabled full screen on browser.")
        time.sleep(1)
    except Exception as e:
        log_message(path=FILE_LOG, message=f"ERROR: {e}.")

def browser_get_video(browser) -> str:
    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    try:
        log_message(path=FILE_LOG, message="INFORMATIONAL: Checking for video url.")
        if browser.find_elements(By.CLASS_NAME, "NYFAyb"):
            log_message(path=FILE_LOG, message="INFORMATIONAL: Video url founded with success.")
            video_url = browser.execute_script("""
                const video = document.querySelector('video');
                return video ? video.src : null;
            """)

            if ".mp4" in video_url:
                return video_url
        else:
            log_message(path=FILE_LOG, message="INFORMATIONAL: No video URL detected.")
            return "Null"

    except Exception as e:
        log_message(path=FILE_LOG, message=f"ERROR: {e}.")

def browser_get_title(browser) -> str:
    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    try:        
        for element in PRODUCTS_NAMES:
            try:
                log_message(path=FILE_LOG, message=f"INFORMATIONAL: Trying to get the product name with the class element: {element}")
                element_item = browser.find_element(By.CSS_SELECTOR, element)
                log_message(path=FILE_LOG, message=f"INFORMATIONAL: Getted with success the product name: {element_item.text}")
                return element_item.text
            except:
                if element == PRODUCTS_NAMES[-1]:
                        return "Null"
                continue

    except Exception as e:
        log_message(path=FILE_LOG, message=f"ERROR: {e}.")

def browser_get_price(browser) -> str:
    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    try:
        log_message(path=FILE_LOG, message=f"INFORMATIONAL: Trying to get the product price with the class element: {PRICE_CSS}")
        element_item = browser.find_element(By.CSS_SELECTOR, PRICE_CSS)
        log_message(path=FILE_LOG, message=f"INFORMATIONAL: Getted with success the product price: {element_item.text}")
        return element_item.text
    except Exception as e:
        log_message(path=FILE_LOG, message=f"ERROR: {e}.")

def browser_get_href_product(browser) -> str:
    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    try:
        log_message(path=FILE_LOG, message=f"INFORMATIONAL: Trying to get the href product with the class element: {CANONICAL}")
        canonical = browser.find_element(By.XPATH, CANONICAL)
        canonical_url = canonical.get_attribute("href")
        return canonical_url
    except Exception as e:
        log_message(path=FILE_LOG, message=f"ERROR: {e}.")

def browser_detect_and_skip(browser) -> bool:
    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    try:
        for element in CLASSES_TO_SKIP:
            try:
                log_message(path=FILE_LOG, message=f"INFORMATIONAL: Checking if must skip url, by class: {element}")
                if browser.find_elements(By.CLASS_NAME, element):
                    log_message(path=FILE_LOG, message="INFORMATIONAL: Skipping the url.")
                    return True
            except:
                if element == CLASSES_TO_SKIP[-1]:
                    return False
                continue
    
    except Exception as e:
        log_message(path=FILE_LOG, message=f"ERROR: {e}.")

def browser_hidden_class(browser) -> None:
    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    try:   
        for element in HIDDEN_CSS:
            try:
                log_message(path=FILE_LOG, message=f"INFORMATIONAL: Trying to hidden the element: {element}")
                element_item = browser.find_element(By.CSS_SELECTOR, f'div[data-testid="{element}"]')
                browser.execute_script("arguments[0].style.display = 'none';", element_item)
                log_message(path=FILE_LOG, message=f"INFORMATIONAL: Successfully hidden the element: {element}")
            except:
                if element == HIDDEN_CSS[-1]:
                    break
                continue

        for element in HIDDEN_XPATH:
            try:
                if element == HIDDEN_XPATH[-1]:
                    time.sleep(1)
                log_message(path=FILE_LOG, message=f"INFORMATIONAL: Trying to hidden the element: {element}")
                element_item = browser.find_element(By.XPATH, element)
                browser.execute_script("arguments[0].style.display = 'none';", element_item)
                log_message(path=FILE_LOG, message=f"INFORMATIONAL: Successfully hidden the element: {element}")
            except:
                if element == HIDDEN_XPATH[-1]:
                    break
                continue

    except Exception as e:
        log_message(path=FILE_LOG, message=f"ERROR: {e}.")

def browser_modify_width_title(browser) -> None:
    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    try:
        log_message(path=FILE_LOG, message=f"INFORMATIONAL: Trying to modify the width of the product title.")
        element_item = browser.find_element(By.CSS_SELECTOR, 'div[data-testid="mod-headingproduct"]')
        browser.execute_script("arguments[0].style.width = '850px';", element_item)
        log_message(path=FILE_LOG, message=f"INFORMATIONAL: Modified the width with success.")

        log_message(path=FILE_LOG, message=f"INFORMATIONAL: Trying to modify the fontSize of the product title.")
        element_item = browser.find_element(By.XPATH, "/html/body/div/div/main/section[2]/div[2]/h1")
        browser.execute_script("arguments[0].style.fontSize = '28px';", element_item)
        log_message(path=FILE_LOG, message=f"INFORMATIONAL: Modified the fontSize with success.")

    except Exception as e:
        log_message(path=FILE_LOG, message=f"ERROR: {e}.")

def browser_checking_characters_number(browser) -> tuple | bool:
    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    try:
        log_message(path=FILE_LOG, message=f"INFORMATIONAL: Trying to get the product title.")
        element_item = browser.find_element(By.CSS_SELECTOR, 'div[data-testid="mod-headingproduct"]')
        
        log_message(path=FILE_LOG, message=f"INFORMATIONAL: Checking if the product title is less than 70 characters.")
        if len(element_item.text) < 70:
            log_message(path=FILE_LOG, message=f"INFORMATIONAL: Product title is less than 70 characters.")
            return (1250, 90, 1615, 275)
        return False

    except Exception as e:
        log_message(path=FILE_LOG, message=f"ERROR: {e}.")

def browser_get_group_name(browser) -> None:
    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    try:
        log_message(path=FILE_LOG, message="INFORMATIONAL: Checking for search box.")
        search_box = browser.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        search_box.send_keys(GROUP_WHATSAPP)

        time.sleep(2)

        log_message(path=FILE_LOG, message="INFORMATIONAL: Checking for group name.")
        group = browser.find_element(By.XPATH, f'//span[@title="{GROUP_WHATSAPP}"]')
        group.click()
    except Exception as e:
        log_message(path=FILE_LOG, message=f"ERROR: {e}.")

def browser_get_attachment(browser, path) -> None:
    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    try:
        time.sleep(TIME_TO_WAIT_5)
        try:
            log_message(path=FILE_LOG, message="INFORMATIONAL: Trying to click the attachment button.")
            attachment_box = WebDriverWait(browser, TIME_TO_WAIT_10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@title="Anexar"]'))
            )
            attachment_box.click()
            log_message(path=FILE_LOG, message="INFORMATIONAL: Clicked on the attachment button.")

        except:
            log_message(path=FILE_LOG, message="INFORMATIONAL: Trying to click the attachment button again.")
            attachment_box = WebDriverWait(browser, TIME_TO_WAIT_10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[title="Anexar"]'))
            )
            attachment_box.click()
            log_message(path=FILE_LOG, message="INFORMATIONAL: Clicked on the attachment button.")

        log_message(path=FILE_LOG, message="INFORMATIONAL: Trying to click the image/video option.")
        image_box = browser.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        log_message(path=FILE_LOG, message="INFORMATIONAL: Clicked on the image/video option.")

        log_message(path=FILE_LOG, message="INFORMATIONAL: Trying to get image for attachment.")
        image_box.send_keys(os.path.abspath(path))
        log_message(path=FILE_LOG, message="INFORMATIONAL: Image selected for attachment successfully.")
        
        time.sleep(2)

    except Exception as e:
        log_message(path=FILE_LOG, message=f"ERROR: {e}.")

def browser_send_message(browser, message) -> None:
    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    try:
        while True:
            log_message(path=FILE_LOG, message="INFORMATIONAL: Trying to find message box.")
            message_box = browser.find_element(By.XPATH, '//div[@aria-label="Adicione uma legenda"]')
            message_box.click()
            log_message(path=FILE_LOG, message="INFORMATIONAL: Message box found and clicked.")

            log_message(path=FILE_LOG, message=f"INFORMATIONAL: Trying to send message: {message.get("ShortLink").strip('\n')}")
            if message.get("Video") != "Null":
                message = "*ShortLink:* _" + message.get("ShortLink").strip('\n') + "_     " + "*VideoLink:* _" + message.get("Video") + '_\n'
            else:
                message =  "*ShortLink:* _" + message.get("ShortLink") + "_"

            message_box.send_keys(message)

            sended = browser_check_if_sent(browser)

            if sended:
                return sended
            else:
                log_message(path=FILE_LOG, message="INFORMATIONAL: Message failed to be sent, trying again.")
                browser_reflesh_page(browser)
                continue

    except Exception as e:
        log_message(path=FILE_LOG, message=f"ERROR: {e}.")

def browser_check_if_sent(browser) -> bool:
    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    try:
        count_try = 1
        while True:
            log_message(path=FILE_LOG, message=f"INFORMATIONAL: Attempt number {str(count_try)}.")
            try:
                for element in WHATSAPP_XPATHS:
                    log_message(path=FILE_LOG, message=f'Checking for: {element}')
                    WebDriverWait(browser, TIME_TO_WAIT_10).until(EC.presence_of_element_located((By.XPATH, element)))
                    return True
            except:
                count_try += 1
                if count_try >= 11:
                    return False
                continue

    except Exception as e:
        log_message(path=FILE_LOG, message=f"ERROR: {e}.")    

def browser_reflesh_page(browser):
    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    try:
        log_message(path=FILE_LOG, message=f'Refreshing web page.')
        browser.refresh()

        time.sleep(TIME_TO_WAIT_5)

        log_message(path=FILE_LOG, message=f'Trying to get group name.')
        browser_get_group_name(browser=browser)

    except Exception as e:
        log_message(path=FILE_LOG, message=f"ERROR: {e}.")  

def browser_save_screenshot(browser, path) -> None:
    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    try:
        make_folder(path_folder=path)
        log_message(path=FILE_LOG, message="INFORMATIONAL: Trying to take a screenshot of the browser screen.")
        browser.save_screenshot(path)
        log_message(path=FILE_LOG, message=f"INFORMATIONAL: Screen shot saved in: {path}")
    except Exception as e:
        log_message(path=FILE_LOG, message=f"ERROR: {e}.")

def browser_quit(browser) -> None:
    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    try:
        browser.quit()
        log_message(path=FILE_LOG, message="INFORMATIONAL: Blowser closed with success.")
    except Exception as e:
        log_message(path=FILE_LOG, message=f"ERROR: {e}.")