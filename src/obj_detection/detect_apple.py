import numpy as np
import cv2 as cv
apple_cascade = cv.CascadeClassifier('cascade.xml')
#img = cv.imread('ss3.png')

cap = cv.VideoCapture('g1.mp4')

while(cap.isOpened()):
    ret, img = cap.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    apples = apple_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in apples:
        if w > 90 : 
            continue
        if h > 90 : 
            continue
        cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
    cv.imshow('img',img)
    cv.waitKey(1) #FIXME 



while cv.waitKey() != 27 :
    i = 1	

cap.release()
cv.destroyAllWindows()


