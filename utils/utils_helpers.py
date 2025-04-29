# type: ignore
import os
import inspect
from pathlib import Path
from datetime import datetime
from config.settings import *

def read_file(path:Path):
    log_message(path=FILE_LOG, message=f"Function {inspect.currentframe().f_code.co_name} called.")
    try:
        make_folder(path_folder=path)
        with open(path, 'r', encoding='UTF-8') as file:
            text_file = file.readlines()
            log_message(path=FILE_LOG, message=f"Text file loaded from: {path}")
            return text_file
    except Exception as e:
        log_message(path=FILE_LOG, message=f"Error: {e}.")

def write_a_file(path:Path=False, url:str=False, video_url:str=False, type:str=False):
    try:
        make_folder(path_folder=path)
        log_message(path=FILE_LOG, message=f"Function {inspect.currentframe().f_code.co_name} called.")
        if video_url:
            log_message(path=FILE_LOG, message='Argument "Video URL" received.')
            if type == "a":
                with open(path, "a", encoding='UTF-8') as file:
                    file.write(f'{url.strip('\n')},{video_url}\n')
                    log_message(path=FILE_LOG, message=f"Video URL saved in: {path}")
            elif type == "w":
                with open(path, "w", encoding='UTF-8') as file:
                    file.writelines(video_url)
                    log_message(path=FILE_LOG, message=f"Videos URL List saved in: {path}")
        else:
            with open(path, "a", encoding='UTF-8') as file:
                file.write(url)
                log_message(path=FILE_LOG, message=f"File text saved in: {path}")
    except Exception as e:
        log_message(path=FILE_LOG, message=f"Error: {e}.")

def log_message(path:Path, message:str):
    try:
        if not os.path.exists(path):
            make_folder(path_folder=path)
        log_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        with open(path, "a", encoding='UTF-8') as file:
            file.write(f"{log_time} - {message}\n")

    except Exception as e:
        log_message(path=FILE_LOG, message=f"Error: {e}.")

def make_folder(path_folder:Path):
    log_message(path=FILE_LOG, message=f"Function {inspect.currentframe().f_code.co_name} called.")
    try:
        log_message(path=FILE_LOG, message=f"Checking if the path exists: {path_folder}")
        os.makedirs(path_folder.parent, exist_ok=True)
    except Exception as e:
        log_message(path=FILE_LOG, message=f"Error: {e}.")

def make_variables(url:str, site:str, image_type:str, path:Path):
    log_message(path=FILE_LOG, message=f"Function {inspect.currentframe().f_code.co_name} called.")
    try:
        make_folder(path_folder=path)
        product_name = url.strip(site)
        product_names = [product_name + '.png', product_name + ' - 00.png', product_name + ' - 01.png', product_name + ' - 02.png']

        if image_type == "final":
            new_path = path / product_names[0]
            log_message(path=FILE_LOG, message=f"Was created the path: {new_path}")
            return new_path
        elif image_type == "full":  
            new_path =  path / product_names[1]
            log_message(path=FILE_LOG, message=f"Was created the path: {new_path}")
            return new_path
        elif image_type == "first":  
            new_path =  path / product_names[2]
            log_message(path=FILE_LOG, message=f"Was created the path: {new_path}")
            return new_path
        elif image_type == "second":  
            new_path =  path / product_names[3]
            log_message(path=FILE_LOG, message=f"Was created the path: {new_path}")
            return new_path
    except Exception as e:
        log_message(path=FILE_LOG, message=f"Error: {e}.")

def check_video(url) -> str:
    log_message(path=FILE_LOG, message=f"Function {inspect.currentframe().f_code.co_name} called.")
    try:
        video_list = read_file(VIDEOS_URL)
        log_message(path=FILE_LOG, message="Checking for match url and video.")
        url = url.strip("\n")
        for video in video_list:
            if url in video:
                video = video.split(',')[1]
                log_message(path=FILE_LOG, message="Url and video matched.")
                log_message(path=FILE_LOG, message=f"Returning the url video: {video}")
                return video
            
    except Exception as e:
        log_message(path=FILE_LOG, message=f"Error: {e}.")

def review_products_names(products_path:Path, images_path:Path, site:str):
    log_message(path=FILE_LOG, message=f"Function {inspect.currentframe().f_code.co_name} called.")
    try:
        new_products = []

        products = read_file(path=products_path)

        for product in products:
            
            log_message(path=FILE_LOG, message=f"Enumerating images from: {images_path}")
            for index, filename in enumerate(os.listdir(images_path), start=1):
                source_path = os.path.join(images_path, filename)
                new_filename = os.path.splitext(filename)[0]

                if new_filename in product:                    
                    new_products.append(product)
                    new_product = product.strip(site) + '.png'

                    if filename != new_product:
                        log_message(path=FILE_LOG, message=f"Divergent names detected: {filename} is different of {new_product}.")
                        destination_path = os.path.join(images_path, new_product)
                        os.rename(source_path, destination_path)
                        log_message(path=FILE_LOG, message=f"Divergent names fixed and saved.")
                    
        with open(products_path, "w", encoding='UTF-8') as file:
            file.writelines(new_products)

    except Exception as e:
        log_message(path=FILE_LOG, message=f"Error: {e}.")

def review_video_urls(path_videos:Path):
    log_message(path=FILE_LOG, message=f"Function {inspect.currentframe().f_code.co_name} called.")
    try:
        videos_url = read_file(path=path_videos)
        log_message(path=FILE_LOG, message=f"Trying to remove duplicates.")
        videos_url = set(videos_url)
        log_message(path=FILE_LOG, message=f"Removed duplicates with success.")

        write_a_file(path=VIDEOS_URL, video_url=videos_url, type="w")
            
    except Exception as e:
        log_message(path=FILE_LOG, message=f"Error: {e}.")

def clean_products_selected(initial_path:Path, selected_path:Path):
    log_message(path=FILE_LOG, message=f"Function {inspect.currentframe().f_code.co_name} called.")
    try:
        products_selected = read_file(path=selected_path)

        initial = read_file(path=initial_path)

        for product in products_selected:
            if product in initial:
                try:
                    log_message(path=FILE_LOG, message=f"Removing {product} from: {initial_path}")
                    initial.remove(product)
                except Exception as e:
                    log_message(path=FILE_LOG, message=f"Error: {e}.")
                    log_message(path=FILE_LOG, message=f"Failed to remove URL: {product}")
                    
        with open(initial_path, "w", encoding='UTF-8') as file:
            file.writelines(initial)
    except Exception as e:
        log_message(path=FILE_LOG, message=f"Error: {e}.")