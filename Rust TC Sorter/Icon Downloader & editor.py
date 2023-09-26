#This file will download every rust item icon from the rustlabs website and edit them to be the correct size 
#and have the correct background for the inventory slot.
#Please only do this once as it will take a while to download all the images

import requests # Imports the requests module to get the image from the url
import json # Imports the json module to read the json file
import os # Imports the os module for getting the directory of the script
from PIL import Image # Imports the Image module from the Pillow library for editing the image
import shutil # Imports the shutil module for deleting and moving the images after they have been edited

# Get the directory where the script is located
dir_path = os.path.dirname(os.path.realpath(__file__))+'/'
output_path = dir_path+'Rust Items Icons/'

with open (dir_path + 'RustItems.json', 'r') as f:
    data = json.load(f)

for i in range(len(data)):
# downloading the image
     url = data[i]['image'] # Url of the image to download
     name = dir_path+url.split('/')[-1] # Gets the name of the image from the url
     if os.path.isfile(output_path+name.split('/')[-1]): # Checks if the image already exists
          print(i+1,'completed out of',len(data),name.split('/')[-1],'already exists')
          continue # Skips the image if it already exists to save time and bandwidth for both the user and the website
     headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
     response = requests.get(url, headers=headers)
     if response.status_code == 200 and response.content:
          with open(name, "wb") as f: 
               f.write(response.content) # Writes the image to the file
          #print(name,'saved')
     else:
          print('Error downloading image:', url, 'with error code:', response.content, i+1,'completed out of',len(data))
# cropping the image
     img = Image.open(name) # Opens the image
     img = img.resize((87,87)) # Resizes the image to 87x87
     img.save(name) # Saves the image
     #print(name,'Cropped down')
# adding the rust inventory slot background to the image
     from PIL import Image
     img = Image.open(name) # Opens the image
     img = img.convert('RGBA') # Converts the image to RGBA to ensure compatibility with the background image
     bg = Image.open(dir_path+'empty background.png') # Opens the background image
     bg = bg.convert('RGBA')
     result = Image.alpha_composite(bg, img) # Combines the PNG image and the background image
     result.save(name) # Saves the combined image
     shutil.copy2(name, output_path) # Moves the image to the output folder and overwrites any existing images with the same name
     os.remove(name) # Deletes the image from the main directory because it is no longer needed
     print(i+1,'completed out of',len(data), 'dowloaded and edited image:', name.split('/')[-1])
print('All items downloaded and edited')