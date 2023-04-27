#analise por cores
#apricar o blur
#transformações morfologica
#https://docs.opencv.org/master/d9/d61/tutorial_py_morphological_ops.html#gsc.tab=0

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()  # _ valor necessário na função, mas não utilizado
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 

    #hsv - hue saturation value

    lower_range = np.array([0,0,50])
    upper_range = np.array([255,255,180])
    
    mask = cv2.inRange(hsv, lower_range, upper_range)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

# o kernel faz a média dos pixels no caso pegamos uma janela 15x15 
# e dividimos pelo total 15*15 =225

    kernel = np.ones((15,15),np.float32)/225
    smoothed = cv2.filter2D(res,-1,kernel)
    
    cv2.imshow('Original',frame)
    cv2.imshow('Averaging',smoothed)

    blur = cv2.GaussianBlur(res,(15,15),0)
    cv2.imshow('Gaussian Blurring',blur)

    median = cv2.medianBlur(res,15)
    cv2.imshow('Median Blur',median)

    bilateral = cv2.bilateralFilter(res,15,75,75)
    cv2.imshow('bilateral Blur',bilateral)

# Erosion is where we will "erode" the edges, work with a slider (kernel). 
# and if all of the pixels are white, then we get white, otherwise black. help eliminate some white noise. 
# Dilation if the entire area isn't black, then it is converted to white


    kernel = np.ones((5,5),np.uint8)
    erosion = cv2.erode(mask,kernel,iterations = 1)
    dilation = cv2.dilate(mask,kernel,iterations = 1)

    cv2.imshow('Erosion',erosion)
    cv2.imshow('Dilation',dilation)

# opening = erosion followed by dilation. - remove "false positives". 
#i.e. in the background,  "noise." 
# closing = Dilation followed by Erosio - remove the false negative
# It is useful in closing small holes inside the foreground objects, or small black points on the object.

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)


    cv2.imshow('opening',opening)
    cv2.imshow('closing',closing)

# Morphological Gradient = difference between dilation and erosion of an image.
# The result will look like the outline of the object.
   
    gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)
    cv2.imshow('morph',gradient)


    # It is the difference between input image and Opening of the image
    tophat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)

    cv2.imshow('Tophat',tophat)

    # It is the difference between the closing of the input image and input image.
    blackhat = cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernel)

    cv2.imshow('Blackhat',blackhat)


    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()