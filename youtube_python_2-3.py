##############################################################
# CODE WITH GOZ Youtube Channel - Python Video No.2 - Script 3
##############################################################
# Description: Simple script to add custom text watermark
#              to multiple images
# Dependencies:
# ----------------------------------------
# pip install Pillow
# ----------------------------------------
# Author: Goz
# https://codewithgoz.com
##############################################################

import os
from PIL import Image, ImageDraw, ImageFont

text = "IMAGEN CON DERECHOS DE AUTOR"
font = ImageFont.truetype('/home/goz/youtube/python/video_2/assets/Pacifico-Regular.ttf', 56)

path = "/home/goz/youtube/python/video_2/images"
os.chdir(path)
images = os.listdir()

for image in images:
    try:
        image1 = Image.open(image)
        image2 = ImageDraw.Draw(image1)
        image2.text((90, 120), text, font=font)
        image1.save('new_' + image)
        image1.close()
        print(f"new_{image} ha sido creada!!!")
    except:
        print(f"{image} no se puede modificar")  