from sites.shopee import *
from sites.magalu import *
from sites.whatsapp_web import *
from sites.delete_promo_images import *

'''
Main control script to select one of the options:
    - n1. Get product images from Shopee website;
    - n2. Get product images from Magalu website;
    - n3. Send product images to Whatsapp Web;
    - n4. Delete all product images.
'''

def main():
    try:
        option = int(input("Choose the option you want (Only Numbers):" \
        "\n1. Get product images from Shopee website." \
        "\n2. Get product images from Magalu website."\
        "\n3. Send product images to Whatsapp Web."\
        "\n4. Delete all product images."\
        "\nProvide only one number: "))
            
        if option == 1:
            print('Option "1. Get product images from Shopee website" selected.')
            get_images_promo_shopee()
        elif option == 2:
            print('Option "2. Get product images from Magalu website" selected.')
            get_images_promo_magalu()
        elif option == 3:
            print('Option "3. Send product images to Whatsapp Web" selected.')
            send_images_to_whatsapp()
        elif option == 4:
            print('Option "4. Delete all product images.')
            delete_product_images()
        else:
            print(f'Option "{option}" provided does not exist.')
    except:
        print("Provided option is not allowed. Only Numbers!")

if __name__ == "__main__":
    main()