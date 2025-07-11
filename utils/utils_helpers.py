# type: ignore
import os
import json
import time
import inspect
import pyautogui
from pathlib import Path
from datetime import datetime
from config.settings import *

def read_file(path:Path) -> str:
    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    try:
        if not os.path.exists(path.parent):
            make_folder(path_folder=path)
        with open(path, 'r', encoding='UTF-8') as file:
            text_file = file.readlines()
            log_message(path=FILE_LOG, message=f"INFORMATIONAL: Text file loaded from: {path}")
            return text_file
    except Exception as e:
        log_message(path=FILE_LOG, message=f"ERROR: {e}.")

def write_a_file(path:Path=False, text:str=False, type:str=False) -> None:
    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    try:
        if not os.path.exists(path.parent):
            make_folder(path_folder=path)
        if type == "a":
            with open(path, "a", encoding='UTF-8') as file:
                file.write(text)
                log_message(path=FILE_LOG, message=f"INFORMATIONAL: File text saved in: {path}")
        elif type == "w":
            with open(path, "w", encoding='UTF-8') as file:
                file.writelines(text)
                log_message(path=FILE_LOG, message=f"INFORMATIONAL: File text saved in: {path}")

    except Exception as e:
        log_message(path=FILE_LOG, message=f"ERROR: {e}.")

def save_a_json(path:Path, args:list) -> None:
    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    try:
        products = {}

        if not os.path.exists(path.parent):
            make_folder(path_folder=path)

        if os.path.exists(path):
            with open(path, 'r') as file:
                try:
                    log_message(path=FILE_LOG, message="INFORMATIONAL: Loaded JSON file with Products.")
                    products = json.load(file)
                except:
                    pass
        
        log_message(path=FILE_LOG, message="INFORMATIONAL: Creation of JSON data with keys and values.")
        product_details = {
            "Site": args[0],
            "Name": args[1],
            "Price": args[2],
            "URL ": args[3],
            "ShortLink": args[4],
            "Video": args[5]
            }
        
        products.update({f"ID {len(products) + 1}": product_details})

        log_message(path=FILE_LOG, message="INFORMATIONAL: Trying save JSON file with Products.")
        with open(path, 'w') as file:            
            json.dump(products, file, ensure_ascii=True, indent=2)
            log_message(path=FILE_LOG, message="INFORMATIONAL: JSON file with Products saved with success.")

    except Exception as e:
        log_message(path=FILE_LOG, message=f"ERROR: {e}.")   

def read_a_json(path:Path) -> dict:
    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    try:
        if os.path.exists(path):
            with open(path, 'r') as file:
                log_message(path=FILE_LOG, message="INFORMATIONAL: Loaded JSON file with Products.")
                products = json.load(file)
                return products
             
    except Exception as e:
        log_message(path=FILE_LOG, message=f"ERROR: {e}.") 

def check_for_product_registered(path:Path, product_name:str) -> bool:
    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    try:
        if os.path.exists(path):
            with open(path, 'r') as file:
                try:
                    log_message(path=FILE_LOG, message="INFORMATIONAL: Loaded JSON file with Products.")
                    products = json.load(file)
                except:
                    return False

            log_message(path=FILE_LOG, message="INFORMATIONAL: Checking for product registered.")
            for product in products:
                if product.get("Name") == product_name:
                    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Already registered the product: {product_name}")
                    return True
                    
    except Exception as e:
        log_message(path=FILE_LOG, message=f"ERROR: {e}.")     

def log_message(path:Path, message:str) -> None:
    try:
        make_folder(path_folder=path)
        log_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        with open(path, "a", encoding='UTF-8') as file:
            file.write(f"{log_time} - ProductImageScrape - {message}\n")

    except Exception as e:
        log_message(path=FILE_LOG, message=f"ERROR: {e}.")

def delete_file(path_file:Path) -> None:
    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    try:
        log_message(path=FILE_LOG, message=f"INFORMATIONAL: Checking if the file exists: {path_file}")
        if os.path.exists(path_file):
            os.remove(path_file)
            log_message(path=FILE_LOG, message=f"INFORMATIONAL: File removed with success.")
        else:
            log_message(path=FILE_LOG, message=f"INFORMATIONAL: The file does not exist.")

    except Exception as e:
        log_message(path=FILE_LOG, message=f"ERROR: {e}.")

def make_folder(path_folder:Path) -> None:
    if path_folder != FILE_LOG:
        log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    try:
        if path_folder != FILE_LOG:
            log_message(path=FILE_LOG, message=f"INFORMATIONAL: Checking if the path exists: {path_folder}")
            if not os.path.exists(path_folder):
                os.makedirs(path_folder.parent, exist_ok=True)
            else:
                log_message(path=FILE_LOG, message=f"INFORMATIONAL: The path already exists: {path_folder}")
    except Exception as e:
        if path_folder != FILE_LOG:
            log_message(path=FILE_LOG, message=f"ERROR: {e}.")

def make_path(url:str, option:str) -> Path:
    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    try:
        make_folder(path_folder=PROMO_IMAGES)
        if "www.magazinevoce.com.br" in url:
            product_name = url.split("/")[4]
        elif "s.shopee.com.br" in url:
            url = url.strip('\n')
            product_name = url.split("/")[3]
        product_names = [product_name + '.png', product_name + ' - 00.png', product_name + ' - 01.png', product_name + ' - 02.png']

        if option == "image_final":
            new_path = PROMO_IMAGES / product_names[0]
            log_message(path=FILE_LOG, message=f"INFORMATIONAL: Was created the path: {new_path}")
            return new_path
        elif option == "image_full":  
            new_path =  PROMO_IMAGES / product_names[1]
            log_message(path=FILE_LOG, message=f"INFORMATIONAL: Was created the path: {new_path}")
            return new_path
        elif option == "image_first":  
            new_path =  PROMO_IMAGES / product_names[2]
            log_message(path=FILE_LOG, message=f"INFORMATIONAL: Was created the path: {new_path}")
            return new_path
        elif option == "image_second":  
            new_path =  PROMO_IMAGES / product_names[3]
            log_message(path=FILE_LOG, message=f"INFORMATIONAL: Was created the path: {new_path}")
            return new_path
    except Exception as e:
        log_message(path=FILE_LOG, message=f"ERROR: {e}.")

def move_mouse() -> None:
    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    try:
        log_message(path=FILE_LOG, message="INFORMATIONAL: Trying to move the mouse to second thumbnail.")
        pyautogui.moveTo(*MOVE_MOUSE, duration=0.1)
        log_message(path=FILE_LOG, message="INFORMATIONAL: Mouse moved with success to second thumbnail.")
        time.sleep(1.5)
    except Exception as e:
        log_message(path=FILE_LOG, message=f"ERROR: {e}.")

def review_products_names(products_path:Path, images_path:Path, site:str) -> None:
    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    try:
        new_products = []

        products = read_file(path=products_path)

        for product in products:
            
            log_message(path=FILE_LOG, message=f"INFORMATIONAL: Enumerating images from: {images_path}")
            for index, filename in enumerate(os.listdir(images_path), start=1):
                source_path = os.path.join(images_path, filename)
                new_filename = os.path.splitext(filename)[0]

                if new_filename in product:                    
                    new_products.append(product)
                    new_product = product.strip(site) + '.png'

                    if filename != new_product:
                        log_message(path=FILE_LOG, message=f"INFORMATIONAL: Divergent names detected: {filename} is different of {new_product}.")
                        destination_path = os.path.join(images_path, new_product)
                        os.rename(source_path, destination_path)
                        log_message(path=FILE_LOG, message=f"INFORMATIONAL: Divergent names fixed and saved.")
                    
        with open(products_path, "w", encoding='UTF-8') as file:
            file.writelines(new_products)

    except Exception as e:
        log_message(path=FILE_LOG, message=f"ERROR: {e}.")

def review_video_urls(path_videos:Path) -> None:
    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    try:
        videos_url = read_file(path=path_videos)
        log_message(path=FILE_LOG, message=f"INFORMATIONAL: Trying to remove duplicates.")
        videos_url = set(videos_url)
        log_message(path=FILE_LOG, message=f"INFORMATIONAL: Removed duplicates with success.")

        write_a_file(path=VIDEOS_URL, video_url=videos_url, type="w")
            
    except Exception as e:
        log_message(path=FILE_LOG, message=f"ERROR: {e}.")

def review_list(path_list:Path) -> None:
    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    try:
        file_list = read_file(path=path_list)

        log_message(path=FILE_LOG, message="INFORMATIONAL: Trying to remove duplicates.")
        file_list = set(file_list)
        log_message(path=FILE_LOG, message="INFORMATIONAL: Removed duplicates with success.")

        write_a_file(path=path_list, text=file_list, type="w")
        time.sleep(3)

    except Exception as e:
        log_message(path=FILE_LOG, message=f"ERROR: {e}.")

def clean_products_selected(initial_path:Path, selected_path:Path) -> None:
    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    try:
        products_selected = read_file(path=selected_path)

        initial = read_file(path=initial_path)

        for product in products_selected:
            if product in initial:
                try:
                    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Removing {product} from: {initial_path}")
                    initial.remove(product)
                except Exception as e:
                    log_message(path=FILE_LOG, message=f"ERROR: {e}.")
                    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Failed to remove URL: {product}")
                    
        with open(initial_path, "w", encoding='UTF-8') as file:
            file.writelines(initial)
    except Exception as e:
        log_message(path=FILE_LOG, message=f"ERROR: {e}.")