# type: ignore
import time
import pyautogui
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
    log_message(path=FILE_LOG, message=f"Function {inspect.currentframe().f_code.co_name} called.")
    try:
        chrome_options = webdriver.ChromeOptions()
        if options is not None:
            for option in options:
                chrome_options.add_argument(option)
                log_message(path=FILE_LOG, message=f"{option} argument added to ChromeOptions.")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        log_message(path=FILE_LOG, message="Experimental options added to ChromeOptions.")
        browser = webdriver.Chrome(options=chrome_options)
        log_message(path=FILE_LOG, message="Chrome browser webdriver created with success.")
        browser.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument",
            {"source": """
                Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
                });
            """},)
        log_message(path=FILE_LOG, message="Executed JavaScript to remove the webdriver property.")
        return browser
    except Exception as e:
        log_message(path=FILE_LOG, message=f"Error: {e}.")

def browser_login_to_site(browser, username, password, login_url, time_wait) -> webdriver.Chrome:
    log_message(path=FILE_LOG, message=f"Function {inspect.currentframe().f_code.co_name} called.")
    login_success = False

    while login_success == False:
        try:
            browser.get(login_url)
            log_message(path=FILE_LOG, message=f"Browser get url {login_url}.")

            element_username = WebDriverWait(browser, time_wait).until(
                EC.presence_of_element_located((By.NAME, 'loginKey')))
            element_password = WebDriverWait(browser, time_wait).until(
                EC.presence_of_element_located((By.NAME, 'password')))
            
            element_username.send_keys(username)
            element_password.send_keys(password)
            time.sleep(1)
            element_password.send_keys(Keys.ENTER)
            log_message(path=FILE_LOG, message="Used credentials to login.")

            login_success = bool(WebDriverWait(browser, time_wait*3).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'Y6xFir'))))
            if login_success:
                log_message(path=FILE_LOG, message="Login with success.")
                break

        except Exception as e:            
            log_message(path=FILE_LOG, message=f"Error: {e}.")
            log_message(path=FILE_LOG, message="Failed to Login! Trying again...")
            
            browser.quit()
    return browser

def browser_save_cookies(browser, cookies_path) -> None:
    log_message(path=FILE_LOG, message=f"Function {inspect.currentframe().f_code.co_name} called.")
    try:
        make_folder(path_folder=cookies_path)
        with open(cookies_path, "wb") as file:
            pickle.dump(browser.get_cookies(), file)
            log_message(path=FILE_LOG, message="Browser cookies have been saved.")
        time.sleep(1)
    except Exception as e:
        log_message(path=FILE_LOG, message=f"Error: {e}.")

def browser_load_cookies(browser, cookies_path, url) -> bool:
    log_message(path=FILE_LOG, message=f"Function {inspect.currentframe().f_code.co_name} called.")
    try:
        make_folder(path_folder=cookies_path)
        browser.get(url)
        log_message(path=FILE_LOG, message=f"Browser get url {url}.")
        time.sleep(3)

        log_message(path=FILE_LOG, message="Checking for cookies.")
        if os.path.exists(cookies_path):
            with open(cookies_path, "rb") as file:
                cookies = pickle.load(file)
                
                for cookie in cookies:
                    cookie.pop('sameSite', None)
                    browser.add_cookie(cookie)
                log_message(path=FILE_LOG, message="Browser cookies have been loaded.")

            browser.get(url)
            log_message(path=FILE_LOG, message=f"Browser get url {url}.")
            time.sleep(3)
            return True
        
        log_message(path=FILE_LOG, message="There are no saved browser cookies.")
        return False
    except Exception as e:
        log_message(path=FILE_LOG, message=f"Error: {e}.")
        return False

def browser_get_site(browser, url) -> None:
    log_message(path=FILE_LOG, message=f"Function {inspect.currentframe().f_code.co_name} called.")
    try:
        browser.get(url)
        log_message(path=FILE_LOG, message=f"Browser get url {url.strip('\n')}")
        time.sleep(3)
    except Exception as e:
        log_message(path=FILE_LOG, message=f"Error: {e}.")

def browser_wait_for_site_to_load(browser, time_wait) -> None:
    log_message(path=FILE_LOG, message=f"Function {inspect.currentframe().f_code.co_name} called.")
    try:
        WebDriverWait(browser, time_wait).until(
            EC.presence_of_element_located((By.CLASS_NAME, '_OguPS')))
        log_message(path=FILE_LOG, message=f"Page url loaded.")
    except Exception as e:
        log_message(path=FILE_LOG, message=f"Error: {e}.")

def browser_enable_full_screen(browser) -> None:
    log_message(path=FILE_LOG, message=f"Function {inspect.currentframe().f_code.co_name} called.")
    try:
        title_name = browser.find_element(By.CLASS_NAME, "WBVL_7")
        ActionChains(browser).move_to_element_with_offset(title_name, 10, 10).click().perform()
        log_message(path=FILE_LOG, message="Initial click on title performed.")

        time.sleep(0.5)

        browser.execute_script("""
            if (document.fullscreenElement == null) {
                document.documentElement.requestFullscreen();
            }
        """)
        log_message(path=FILE_LOG, message="Enabled full screen on browser.")
        time.sleep(1)
    except Exception as e:
        log_message(path=FILE_LOG, message=f"Error: {e}.")

def browser_detect_video(browser, move_mouse, url) -> str:
    log_message(path=FILE_LOG, message=f"Function {inspect.currentframe().f_code.co_name} called.")
    try:

        log_message(path=FILE_LOG, message="Checking for video url.")

        if browser.find_elements(By.CLASS_NAME, "NYFAyb"):

            log_message(path=FILE_LOG, message="Detected a video url.")

            video_url = browser.execute_script("""
                const video = document.querySelector('video');
                return video ? video.src : null;
            """)
        
        pyautogui.moveTo(*move_mouse, duration=0.1)

        log_message(path=FILE_LOG, message="Mouse moved to second thumbnail.")

        time.sleep(0.5)

        if video_url in locals():
            if ".mp4" in video_url:
                log_message(path=FILE_LOG, message="Trying to save a video url.")
                write_a_file(path=VIDEOS_URL, url=url, video_url=video_url, type="a")
        else:
            log_message(path=FILE_LOG, message="No video URL detected.")

    
    except Exception as e:
        log_message(path=FILE_LOG, message=f"Error: {e}.")

def browser_detect_and_skip(browser, option) -> bool:
    log_message(path=FILE_LOG, message=f"Function {inspect.currentframe().f_code.co_name} called.")
    try:
        if option == "shopee":
            for element in SHOPEE_CLASSES:
                try:
                    log_message(path=FILE_LOG, message=f"Checking if must skip url, by class: {element}")
                    if browser.find_elements(By.CLASS_NAME, element):
                        log_message(path=FILE_LOG, message="Skipping the url.")
                        return True
                except:
                    if element == SHOPEE_CLASSES[-1]:
                        pass
                    continue
        elif option == "magalu":
            for element in MAGALU_CLASSES:
                try:
                    log_message(path=FILE_LOG, message=f"Checking if must skip url, by class: {element}")
                    if browser.find_elements(By.CLASS_NAME, element):
                        log_message(path=FILE_LOG, message="Skipping the url.")
                        return True
                except:
                    if element == MAGALU_CLASSES[-1]:
                        pass
                    continue
        return False
    
    except Exception as e:
        log_message(path=FILE_LOG, message=f"Error: {e}.")
        return False

def browser_hidden_class(browser) -> None:
    log_message(path=FILE_LOG, message=f"Function {inspect.currentframe().f_code.co_name} called.")
    try:   
        for element in MAGALU_CSS:
            try:
                log_message(path=FILE_LOG, message=f"Trying to hidden the element: {element}")
                element_item = browser.find_element(By.CSS_SELECTOR, f'div[data-testid="{element}"]')
                browser.execute_script("arguments[0].style.display = 'none';", element_item)
                log_message(path=FILE_LOG, message=f"Successfully hidden the element: {element}")
            except:
                if element == MAGALU_CSS[-1]:
                    break
                continue

        for element in MAGALU_XPATHS:
            try:
                if element == MAGALU_XPATHS[-1]:
                    time.sleep(1)
                log_message(path=FILE_LOG, message=f"Trying to hidden the element: {element}")
                element_item = browser.find_element(By.XPATH, element)
                browser.execute_script("arguments[0].style.display = 'none';", element_item)
                log_message(path=FILE_LOG, message=f"Successfully hidden the element: {element}")
            except:
                if element == MAGALU_XPATHS[-1]:
                    break
                continue

    except Exception as e:
        log_message(path=FILE_LOG, message=f"Error: {e}.")

def browser_modify_width_title(browser) -> None:
    log_message(path=FILE_LOG, message=f"Function {inspect.currentframe().f_code.co_name} called.")
    try:
        log_message(path=FILE_LOG, message=f"Trying to modify the width of the product title.")
        element_item = browser.find_element(By.CSS_SELECTOR, 'div[data-testid="mod-headingproduct"]')
        browser.execute_script("arguments[0].style.width = '850px';", element_item)
        log_message(path=FILE_LOG, message=f"Modified the width with success.")

        log_message(path=FILE_LOG, message=f"Trying to modify the fontSize of the product title.")
        element_item = browser.find_element(By.XPATH, "/html/body/div/div/main/section[2]/div[2]/h1")
        browser.execute_script("arguments[0].style.fontSize = '28px';", element_item)
        log_message(path=FILE_LOG, message=f"Modified the fontSize with success.")
        

    except Exception as e:
        log_message(path=FILE_LOG, message=f"Error: {e}.")

def browser_checking_characters_number(browser) -> tuple | bool:
    log_message(path=FILE_LOG, message=f"Function {inspect.currentframe().f_code.co_name} called.")
    try:
        log_message(path=FILE_LOG, message=f"Trying to get the product title.")
        element_item = browser.find_element(By.CSS_SELECTOR, 'div[data-testid="mod-headingproduct"]')
        
        log_message(path=FILE_LOG, message=f"Checking if the product title is less than 70 characters.")
        if len(element_item.text) < 70:
            log_message(path=FILE_LOG, message=f"Product title is less than 70 characters.")
            return (1250, 90, 1615, 275)
        return False

    except Exception as e:
        log_message(path=FILE_LOG, message=f"Error: {e}.")

def browser_get_group_name(browser, group_name) -> None:
    log_message(path=FILE_LOG, message=f"Function {inspect.currentframe().f_code.co_name} called.")
    try:
        log_message(path=FILE_LOG, message="Checking for search box.")
        search_box = browser.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        search_box.send_keys(group_name)

        time.sleep(2)

        log_message(path=FILE_LOG, message="Checking for group name.")
        group = browser.find_element(By.XPATH, f'//span[@title="{group_name}"]')
        group.click()
    except Exception as e:
        log_message(path=FILE_LOG, message=f"Error: {e}.")

def browser_get_attachment(browser, path) -> None:
    log_message(path=FILE_LOG, message=f"Function {inspect.currentframe().f_code.co_name} called.")
    try:
        time.sleep(TIME_TO_WAIT_5)
        try:
            log_message(path=FILE_LOG, message="Trying to click the attachment button.")
            attachment_box = WebDriverWait(browser, TIME_TO_WAIT_10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@title="Anexar"]'))
            )
            attachment_box.click()
            log_message(path=FILE_LOG, message="Clicked on the attachment button.")

        except:
            log_message(path=FILE_LOG, message="Trying to click the attachment button again.")
            attachment_box = WebDriverWait(browser, TIME_TO_WAIT_10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[title="Anexar"]'))
            )
            attachment_box.click()
            log_message(path=FILE_LOG, message="Clicked on the attachment button.")

        log_message(path=FILE_LOG, message="Trying to click the image/video option.")
        image_box = browser.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        log_message(path=FILE_LOG, message="Clicked on the image/video option.")

        log_message(path=FILE_LOG, message="Trying to get image for attachment.")
        image_box.send_keys(os.path.abspath(path))
        log_message(path=FILE_LOG, message="Image selected for attachment successfully.")
        
        time.sleep(2)

    except Exception as e:
        log_message(path=FILE_LOG, message=f"Error: {e}.")

def browser_send_message(browser, message) -> None:
    log_message(path=FILE_LOG, message=f"Function {inspect.currentframe().f_code.co_name} called.")
    try:
        log_message(path=FILE_LOG, message="Trying to find message box.")
        message_box = browser.find_element(By.XPATH, '//div[@aria-label="Adicione uma legenda"]')
        message_box.click()
        log_message(path=FILE_LOG, message="Message box found and clicked.")

        log_message(path=FILE_LOG, message=f"Trying to send message: {message.strip('\n')}")
        message_box.send_keys(message)               

        sended = browser_check_if_sent(browser)

        if sended:
            time.sleep(TIME_TO_WAIT_5) 
            url_video = check_video(url=message)
            if url_video:
                log_message(path=FILE_LOG, message="Trying to find message box.")
                message_box = browser.find_element(By.XPATH, '//div[@aria-label="Digite uma mensagem"]')
                message_box.click()   
                log_message(path=FILE_LOG, message="Message box found and clicked.") 

                log_message(path=FILE_LOG, message=f"Trying to send message.")
                message_box.send_keys(url_video)
                
            log_message(path=FILE_LOG, message=f"Message sent successfully.")
            return sended
        else:
            log_message(path=FILE_LOG, message="Message failed to be sent.")
            return sended

    except Exception as e:
        log_message(path=FILE_LOG, message=f"Error: {e}.")

def browser_check_if_sent(browser) -> bool:
    log_message(path=FILE_LOG, message=f"Function {inspect.currentframe().f_code.co_name} called.")
    try:
        count_try = 1
        while True:
            log_message(path=FILE_LOG, message=f"Attempt number {str(count_try)}.")
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
        log_message(path=FILE_LOG, message=f"Error: {e}.")    

def browser_save_screenshot(browser, path) -> None:
    log_message(path=FILE_LOG, message=f"Function {inspect.currentframe().f_code.co_name} called.")
    try:
        make_folder(path_folder=path)
        log_message(path=FILE_LOG, message="Trying to take a screenshot of the browser screen.")
        browser.save_screenshot(path)
        log_message(path=FILE_LOG, message=f"Screen shot saved in: {path}")
    except Exception as e:
        log_message(path=FILE_LOG, message=f"Error: {e}.")

def browser_quit(browser) -> None:
    log_message(path=FILE_LOG, message=f"Function {inspect.currentframe().f_code.co_name} called.")
    try:
        browser.quit()
        log_message(path=FILE_LOG, message="Blowser closed with success.")
    except Exception as e:
        log_message(path=FILE_LOG, message=f"Error: {e}.")