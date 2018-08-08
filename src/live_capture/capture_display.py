##################################################
# Screen Capturing                               #
##################################################

# Library imports
from PIL import Image
import mss
import numpy as np
import cv2
import time

##################################################
# The following code is sourced from mss doc     #
##################################################

# Part of the screen to capture
monitor = {'top': 150, 'left': 330, 'width': 350, 'height': 300}

# Index of saving image
# imgIndex = 0

with mss.mss() as sct:

  while 'Screen capturing':
    
    # Capture the previous timestamp made
    last_time = time.time()
    
    # Once the elapsed time reaches our defined value aka. forced 1/(frame rate) seconds
    # we capture the gameplay image
    # elapsed_time = time.time() - last_time
    
    # Get raw pixels from the screen, save it to a Numpy array
    img = np.array(sct.grab(monitor))
    
    ##################################################
    # Image processing                               #
    ##################################################  
    
    # Preliminary method - Convert image into grayscale
    # img_gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    
    # (UNUSED) Method 1 - Compute Gradient
    
    # (ENABLED for OCR) Method 2 - Gaussian blur + Canny edge detection
    # Apply Gaussian blur on the image to remove high-frequency component
    # and to focus on structural component instead
    # img_gauss = cv2.GaussianBlur(img_gray, (3, 3), 0)
    # Apply Canny edge detection
    # img_canny = cv2.Canny(img_gauss, 30, 150)
    
    # (UNUSED) Display the original image
    # cv2.imshow('OpenCV/Numpy normal', img)
    
    # (UNUSED) Method 3 - Only apply histogram equilization on the grayscale image
    # img_eq = cv2.equalizeHist(img_gray)
    
    # Display the processed image
    # Crop image
    # img_crop = img_gray[0:150, 50:400]
    cv2.imshow('Post processed image', img)
    # Disable image write-out
    # cv2.imwrite('%d.png' % imgIndex, img_crop)
    # imgIndex = imgIndex + 1
    
    # Display current capturing FPS
    # current_time = time.time()
    print('fps: {0}'.format(1 / (time.time()-last_time)))
    # last_time = current_time
    
    # Press "q" to quit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
    
