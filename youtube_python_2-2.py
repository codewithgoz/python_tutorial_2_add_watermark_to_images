##############################################################
# CODE WITH GOZ Youtube Channel - Python Video No.2 - Script 2
##############################################################
# Description: Simple script to add centered watermark
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
logo_width = round(logo.size[0]/2)
logo_height = round(logo.size[1]/2)

path = "/home/goz/youtube/python/video_2/images"
os.chdir(path)
images = os.listdir()

for image in images:
    try:
        image1 = Image.open(image)
        x_coordinate = round(image1.size[0]/2) - logo_width
        y_coordinate = round(image1.size[1]/2) - logo_height
        image1.paste(logo, (x_coordinate, y_coordinate), logo)
        image1.save('new_' + image)
        image1.close()
        print(f"new_{image} ha sido creada!!!")
    except:
        print(f"{image} no se puede modificar")    





















