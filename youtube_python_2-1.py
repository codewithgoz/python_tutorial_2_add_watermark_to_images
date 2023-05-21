##############################################################
# CODE WITH GOZ Youtube Channel - Python Video No.2 - Script 1
##############################################################
# Description: Simple script to add custom positioned watermark
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

logo_path = '/home/goz/youtube/python/video_2/assets/watermark1.png'
logo = Image.open(logo_path)
x_coordinate = 0
y_coordinate = 0

path = "/home/goz/youtube/python/video_2/images"
os.chdir(path)
images = os.listdir()

for image in images:
    try:
        image1 = Image.open(image)
        image1.paste(logo, (x_coordinate, y_coordinate), logo)
        image1.save('new_' + image)
        image1.close()
        print(f"new_{image} ha sido creada!!!")
    except:
        print(f"{image} no se puede modificar")    





















