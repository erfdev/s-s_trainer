'''
    split_image.py
    --------------
    Use this to split an image into multiple smaller images of equal size.
    Used for creating multiple negative/background samples for training. 

    Usage:
    python split_image.py <image> <dir_to_save_img>
                
'''

import sys
import cv2 as cv
import argparse

img = cv.imread(sys.argv[1])

height, width, channels = img.shape

print sys.argv[1], ' image is resolution:', height, 'x', width

# Crop image into 150x150 sized images, tweak this if needed.
w = 150
h = 150


y = 0
x = 0

img_num = 0
for j in range (height//h) :
    x = 0
    for i in range(width//w) :
        img_num = img_num + 1
        crop_img = img[y:y+h, x:x+w]
        cv.imshow("crop", crop_img) 
        cv.waitKey(0)
        img_name = sys.argv[2]+'bg_'+str(img_num)+'.png'
        cv.imwrite(img_name, crop_img)
        x = x + w
        if x > width:
            break
    y = y + h
    if y > height:
        break
        


cv.imwrite('crop.png', crop_img)

