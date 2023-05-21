##############################################################
# CODE WITH GOZ Youtube Channel - Python Video No.2 - Script 4
##############################################################
# Description: Simple script to add watermark as wallpaper
#              to multiple images
# Dependencies:
# ----------------------------------------
# pip install Pillow
# ----------------------------------------
# Author: Goz
# https://codewithgoz.com
##############################################################

import os
from PIL import Image

logo_path = '/home/goz/youtube/python/video_2/assets/watermark2.png'
logo = Image.open(logo_path)

path = "/home/goz/youtube/python/video_2/images"
os.chdir(path)
images = os.listdir()

for image in images:
    try:
        image1 = Image.open(image)
        image1.paste(logo, (0, 0), logo)
        image1.save('new_' + image)
        image1.close()
        print(f"new_{image} ha sido creada!!!")
    except:
        print(f"{image} no se puede modificar")    


