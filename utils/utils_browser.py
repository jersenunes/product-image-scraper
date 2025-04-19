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

def browser_login_to_site(browser, username, password, login_url, time_wait):
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

def browser_save_cookies(browser, cookies_path):
    log_message(path=FILE_LOG, message=f"Function {inspect.currentframe().f_code.co_name} called.")
    try:
        with open(cookies_path, "wb") as file:
            pickle.dump(browser.get_cookies(), file)
            log_message(path=FILE_LOG, message="Browser cookies have been saved.")
        time.sleep(1)
    except Exception as e:
        log_message(path=FILE_LOG, message=f"Error: {e}.")

def browser_load_cookies(browser, cookies_path, url):
    log_message(path=FILE_LOG, message=f"Function {inspect.currentframe().f_code.co_name} called.")
    try:
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

def browser_get_site(browser, url):
    log_message(path=FILE_LOG, message=f"Function {inspect.currentframe().f_code.co_name} called.")
    try:
        browser.get(url)
        log_message(path=FILE_LOG, message=f"Browser get url {url}.")
        time.sleep(3)
    except Exception as e:
        log_message(path=FILE_LOG, message=f"Error: {e}.")

def browser_wait_for_site_to_load(browser, time_wait):
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

def browser_detect_video(browser, move_mouse):
    log_message(path=FILE_LOG, message=f"Function {inspect.currentframe().f_code.co_name} called.")
    try:
        video_url = False

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

        if video_url:
            log_message(path=FILE_LOG, message="Saved a video url.")
            return video_url
        
        log_message(path=FILE_LOG, message="No video URL detected.")
        return video_url
    
    except Exception as e:
        log_message(path=FILE_LOG, message=f"Error: {e}.")

def browser_detect_and_skip_offer(browser) -> bool:
    log_message(path=FILE_LOG, message=f"Function {inspect.currentframe().f_code.co_name} called.")
    try:
        log_message(path=FILE_LOG, message="Checking for offer.")
        if browser.find_elements(By.CLASS_NAME, 'wV4oFQ'):
            log_message(path=FILE_LOG, message="Detected an offer.")
            return True
        elif browser.find_elements(By.CLASS_NAME, 'jw_y2_'):
            log_message(path=FILE_LOG, message="Detected an offer.")
            return True
        return False
    except Exception as e:
        log_message(path=FILE_LOG, message=f"Error: {e}.")

def browser_save_screenshot(browser, path):
    log_message(path=FILE_LOG, message=f"Function {inspect.currentframe().f_code.co_name} called.")
    try:        
        browser.save_screenshot(path)
        log_message(path=FILE_LOG, message=f"Screen shot saved in: {path}")
    except Exception as e:
        log_message(path=FILE_LOG, message=f"Error: {e}.")

def browser_quit(browser):
    log_message(path=FILE_LOG, message=f"Function {inspect.currentframe().f_code.co_name} called.")
    try:
        browser.quit()
        log_message(path=FILE_LOG, message="Blowser closed with success.")
    except Exception as e:
        log_message(path=FILE_LOG, message=f"Error: {e}.")