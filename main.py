from sites.shopee import *
from sites.whatsapp_web import *

def main():
    while True:
        try:
            option = int(input("Choose the option you want (Only Numbers):" \
            "\n1. Get product images from Shopee website." \
            "\n2. Send product images to Whatsapp Web."\
            "\nProvide only one number: "))
            
            if option == 1:
                print('Option "1. Get product images from Shopee website" selected.')
                get_images_promo_shopee()
                break
            elif option == 2:
                print('Option "2. Send product images to Whatsapp Web" selected.')
                send_images_to_whatsapp()
                break
            else:
                print(f'Option "{option}" provided does not exist.')
                continue

        except:
            print("Provided option is not allowed. Only Numbers!")

if __name__ == "__main__":
    main()