import numpy as np
import cv2 as cv #Version 4.8.0Users

original_img = cv.imread('C:/Users/oniel/iCloudDrive/Coding/Personal/Rust TC Sorter/original.png',cv.IMREAD_COLOR)
stone_img = cv.imread('C:/Users/oniel/iCloudDrive/Coding/Personal/Rust TC Sorter/stone.png',cv.IMREAD_COLOR)

result = cv.matchTemplate(original_img,stone_img,cv.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result) # Finds the highest confidence value in the image

threashold = 0.6 # above 60% confidence
if max_val >= threashold:
    print('Found')
    cv.rectangle(original_img,max_loc,(max_loc[0]+87,max_loc[1]+87),(0,255,0),2) # Drwas a rectangle around the found image (87x87 is the size of the box on a standard 1920x1080 screen)
    cv.imshow('Original',original_img) # Shows the image with the rectangle
    cv.waitKey() # Waits for a key press to close the image
else:
    print('Not Found')