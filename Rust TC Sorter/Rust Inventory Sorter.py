#TODO add variablility for different screen resolutions other then 1080p
import subprocess
import os
from PIL import ImageGrab
import cv2 as cv
import time

dir_path = os.path.dirname(os.path.realpath(__file__))+'/' # Gets the path of the script. This is used to ensure compatibility with all operating systems and directorys

# Works, just needs to enebled again
# if input('Do you want to download the icons? (y/n) ') == 'y':
#     subprocess.run(['python3', dir_path+'Icon Downloader & editor.py'])
#     print('Icons downloaded')
# else:
#     print('Skipping icon download')

if input('do you have a Large Box or a tool cubord? (l/t) ') == 'l':
    print('Large box selected')
    largeBoxScreenShot = ImageGrab.grab(bbox=(0, 0, 1920, 1080)) # X1,Y1,X2,Y2
    largeBoxScreenShot.save(dir_path+'largeBox.png')
    tcMode = False
else:
    print('Tool Cubord selected')
    toolCubordScreenShot = ImageGrab.grab(bbox=(0, 0, 1920, 1080)) # X1,Y1,X2,Y2
    toolCubordScreenShot.save(dir_path+'toolCubord.png')
    tcMode = True

toolCubord = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]] #Row 1[slot 1-6], Row 2, Row 3, Row 4
largeBox = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]] #Row 1[slot 1-6], Row 2, Row 3, Row 4, Row 5, Row 6, Row 7, Row 8

#TODO divide each cell of the inventory into individual images, then compare them to the icons to find out what is in each slot

#TODO find the quantity of each item in the inventory

#TODO sort the items in the inventory with the most important items first