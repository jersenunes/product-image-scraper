# type: ignore
from config.settings import *
from utils.utils_helpers import *
from PIL import Image

def image_crop_and_resize(path_full:Path, path_1:Path, path_2:Path, crop_1:tuple, crop_2:tuple, resize_1:tuple, resize_2:tuple) -> None:
    """
    Crops two regions from a source image, resizes them, and saves them as separate image files.

    Args:
        path_full (Path): Path to the source image.
        path_1 (Path): Output path for the first cropped and resized image.
        path_2 (Path): Output path for the second cropped and resized image.
        crop_1 (tuple): Crop box for the first image (left, upper, right, lower).
        crop_2 (tuple): Crop box for the second image (left, upper, right, lower).
        resize_1 (tuple): Target size for the first image (width, height).
        resize_2 (tuple): Target size for the second image (width, height).

    Returns:
        None
    """
    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    try:
        make_folder(path_folder=path_full)
            
        full_image = Image.open(path_full)
        log_message(path=FILE_LOG, message=f"INFORMATIONAL: Full image loaded from: {path_full}")

        product_image = full_image.crop(crop_1)
        log_message(path=FILE_LOG, message="INFORMATIONAL: Full image cropped to form Product image.")

        product_image = product_image.resize(resize_1, Image.Resampling.LANCZOS)
        log_message(path=FILE_LOG, message="INFORMATIONAL: Product image resized.")

        price_image = full_image.crop(crop_2)
        log_message(path=FILE_LOG, message="INFORMATIONAL: Full image cropped to form product image.")
        
        price_image = price_image.resize(resize_2, Image.Resampling.LANCZOS)
        log_message(path=FILE_LOG, message="INFORMATIONAL: Price image resized.")
        
        product_image.save(path_1)
        log_message(path=FILE_LOG, message=f"INFORMATIONAL: Product image saved in: {path_1}")
        price_image.save(path_2)
        log_message(path=FILE_LOG, message=f"INFORMATIONAL: Price image saved in: {path_2}")

    except Exception as e:
        log_message(path=FILE_LOG, message=f"ERROR: {e}.")

def image_overlay_background(path_background:Path, path_1:Path, path_2:Path, path_final:Path, position_1:tuple, position_2:tuple) -> None:
    """
    Overlays two images (title and product) onto a background image and saves the final result.

    Args:
        path_background (Path): Path to the background image.
        path_1 (Path): Path to the first overlay image.
        path_2 (Path): Path to the second overlay image.
        path_final (Path): Path where the final composed image will be saved.
        position_1 (tuple): (x, y) position for the first image overlay on the background.
        position_2 (tuple): (x, y) position for the second image overlay on the background.

    Returns:
        None
    """
    log_message(path=FILE_LOG, message=f"INFORMATIONAL: Function {inspect.currentframe().f_code.co_name} called.")
    try:
        make_folder(path_folder=path_background)
        make_folder(path_folder=path_final)
        try:
            background = Image.open(path_background).convert("RGBA")
            log_message(path=FILE_LOG, message=f"INFORMATIONAL: Background image loaded from: {path_background}")
        except (FileNotFoundError, UnidentifiedImageError) as e:
            log_message(path=FILE_LOG, message=f"ERROR: {e}.")
            return

        try:
            title_image = Image.open(path_1).convert("RGBA")
            log_message(path=FILE_LOG, message=f"INFORMATIONAL: Title image loaded from: {path_1}")
        except (FileNotFoundError, UnidentifiedImageError) as e:
            log_message(path=FILE_LOG, message=f"ERROR: {e}.")
            return

        try:
            product_image = Image.open(path_2).convert("RGBA")
            log_message(path=FILE_LOG, message=f"INFORMATIONAL: Product image loaded from: {path_2}")
        except (FileNotFoundError, UnidentifiedImageError) as e:
            log_message(path=FILE_LOG, message=f"ERROR: {e}.")
            return

        background.paste(product_image, position_2, product_image)
        background.paste(title_image, position_1, title_image)
        log_message(path=FILE_LOG, message="INFORMATIONAL: Product and Title Images overlaid on the background image.")
        background.save(path_final)
        log_message(path=FILE_LOG, message=f"INFORMATIONAL: Promo image saved with success in: {path_final}")
    except Exception as e:
        log_message(path=FILE_LOG, message=f"ERROR: {e}.")