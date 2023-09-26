import numpy as np
import cv2 as cv #Version 4.8.0Users

source_file = 'C:/Users/oniel/iCloudDrive/Coding/Personal/Rust TC Sorter/Test images/fso2.png'
image_2find = 'C:/Users/oniel/iCloudDrive/Coding/Personal/Rust TC Sorter/hqm.png'

original_img = cv.imread(source_file,cv.IMREAD_COLOR)
stone_img = cv.imread(image_2find,cv.IMREAD_COLOR)

result = cv.matchTemplate(original_img,stone_img,cv.TM_CCOEFF_NORMED)

threashold = 0.6 # above 60% confidence
locations = np.where(result >= threashold) # Finds all the locations(in the array) where the confidence is above the threashold
locations = list(zip(*locations[::-1]))

if locations:
    print('Found')
    template_width = stone_img.shape[1]
    template_height = stone_img.shape[0]
    line_color = (0,255,0)
    line_type = cv.LINE_4
    for loc in locations:
        top_left = loc
        bottom_right = (top_left[0] + template_width, top_left[1] + template_height)
        cv.rectangle(original_img,top_left,bottom_right,line_color,line_type)
    cv.imshow('Original',original_img) # Shows the image with the rectangle
    cv.waitKey() # Waits for a key press to close the image
else:
    print('Not Found')