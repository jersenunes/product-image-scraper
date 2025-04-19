# type: ignore
from config.settings import *
from utils.utils_helpers import *
from PIL import Image

def image_crop_and_resize(path_full:str, path_1:str, path_2:str, crop_1:tuple, crop_2:tuple, resize_1:tuple, resize_2:tuple) -> None:
    """
    Crops two regions from a source image, resizes them, and saves them as separate image files.

    Args:
        path_full (str): Path to the source image.
        path_1 (str): Output path for the first cropped and resized image.
        path_2 (str): Output path for the second cropped and resized image.
        crop_1 (tuple): Crop box for the first image (left, upper, right, lower).
        crop_2 (tuple): Crop box for the second image (left, upper, right, lower).
        resize_1 (tuple): Target size for the first image (width, height).
        resize_2 (tuple): Target size for the second image (width, height).

    Returns:
        None
    """
    try:
        try:        
            full_image = Image.open(path_full)
            log_message(path=FILE_LOG, message=f"Full image loaded from: {path_full}")
        except (FileNotFoundError, UnidentifiedImageError) as e:
            log_message(path=FILE_LOG, message=f"Error: {e}.")
            return

        #Crop and resize the first image
        title_image = full_image.crop(crop_1)
        log_message(path=FILE_LOG, message="Full image cropped to form title image.")
        try:
            title_image = title_image.resize(resize_1, Image.Resampling.LANCZOS)
        except AttributeError:
            title_image = title_image.resize(resize_1, Image.LANCZOS)
        log_message(path=FILE_LOG, message="Title image resized.")

        #Crop and resize the second image
        product_image = full_image.crop(crop_2)
        log_message(path=FILE_LOG, message="Full image cropped to form product image.")
        try:
            product_image = product_image.resize(resize_2, Image.Resampling.LANCZOS)
        except AttributeError:
            product_image = product_image.resize(resize_2, Image.LANCZOS)
        log_message(path=FILE_LOG, message="Product image resized.")
        
        #Save the resulting images
        title_image.save(path_1)
        log_message(path=FILE_LOG, message=f"Title image saved in: {path_1}")
        product_image.save(path_2)
        log_message(path=FILE_LOG, message=f"Product image saved in: {path_2}")

    except Exception as e:
        log_message(path=FILE_LOG, message=f"Error: {e}.")

def image_overlay_background(path_background:str, path_1:str, path_2:str, path_final:str, position_1:tuple, position_2:tuple) -> None:
    """
    Overlays two images (title and product) onto a background image and saves the final result.

    Args:
        path_background (str): Path to the background image.
        path_1 (str): Path to the first overlay image.
        path_2 (str): Path to the second overlay image.
        path_final (str): Path where the final composed image will be saved.
        position_1 (tuple): (x, y) position for the first image overlay on the background.
        position_2 (tuple): (x, y) position for the second image overlay on the background.

    Returns:
        None
    """
    try:
        background = Image.open(path_background).convert("RGBA")
        log_message(path=FILE_LOG, message=f"Background image loaded from: {path_background}")
    except (FileNotFoundError, UnidentifiedImageError) as e:
        log_message(path=FILE_LOG, message=f"Error: {e}.")
        return

    try:
        title_image = Image.open(path_1).convert("RGBA")
        log_message(path=FILE_LOG, message=f"Title image loaded from: {path_1}")
    except (FileNotFoundError, UnidentifiedImageError) as e:
        log_message(path=FILE_LOG, message=f"Error: {e}.")
        return

    try:
        product_image = Image.open(path_2).convert("RGBA")
        log_message(path=FILE_LOG, message=f"Product image loaded from: {path_2}")
    except (FileNotFoundError, UnidentifiedImageError) as e:
        log_message(path=FILE_LOG, message=f"Error: {e}.")
        return

    try:
        background.paste(product_image, position_2, product_image)
        background.paste(title_image, position_1, title_image)
        log_message(path=FILE_LOG, message="Product and Title Images overlaid on the background image.")
        background.save(path_final)
        log_message(path=FILE_LOG, message=f"Promo image saved with success in: {path_final}")
    except Exception as e:
        log_message(path=FILE_LOG, message=f"Error: {e}.")