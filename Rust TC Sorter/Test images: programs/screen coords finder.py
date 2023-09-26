import cv2 as cv
import numpy as np
import os

# Load the image to be searched
img = cv.imread('image_to_search.png', cv.IMREAD_GRAYSCALE)

# Loop through each template image in the item folder
for filename in os.listdir('item_folder'):
    if filename.endswith('.png'):
        # Load the template image
        template = cv.imread(os.path.join('item_folder', filename), cv.IMREAD_GRAYSCALE)

        # Perform template matching
        res = cv.matchTemplate(img, template, cv.TM_CCOEFF_NORMED)

        # Threshold the match matrix to find the locations of the template in the image to be searched
        threshold = 0.8
        loc = np.where(res >= threshold)

        # Draw rectangles around the template(s) in the image to be searched
        w, h = template.shape[::-1]
        for pt in zip(*loc[::-1]):
            cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

# Display the resulting image with rectangles around the template(s)
cv.imshow('Result', img)
cv.waitKey(0)
cv.destroyAllWindows()