# type: ignore
import os
from pathlib import Path
from config.settings import *
from utils.utils_helpers import *

'''
Enumerate the files in Promos_Images Folder
Delete all product images in Promos_Images Folder
'''


def delete_product_images():
    for index, filename in enumerate(os.listdir(PROMO_IMAGES), start=1):
        full_path = PROMO_IMAGES / filename
        delete_file(path_file = full_path)

if __name__ == "__main__":
    delete_product_images()