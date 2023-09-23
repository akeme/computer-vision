import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('Original',img)

    img_gaussian = cv2.GaussianBlur(img,(3,3),0)

    #canny
    img_canny = cv2.Canny(img,100,200)

    #sobel
    img_sobelx = cv2.Sobel(img_gaussian,cv2.CV_8U,1,0,ksize=5)
    img_sobely = cv2.Sobel(img_gaussian,cv2.CV_8U,0,1,ksize=5)
    img_sobel = img_sobelx + img_sobely


    #prewitt
    kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
    kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
    img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
    img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)

    cv2.imshow("Original Image", img)
    cv2.imshow("Canny", img_canny)
    cv2.imshow("Sobel X", img_sobelx)
    cv2.imshow("Sobel Y", img_sobely)
    cv2.imshow("Sobel", img_sobel)
    cv2.imshow("Prewitt X", img_prewittx)
    cv2.imshow("Prewitt Y", img_prewitty)
    cv2.imshow("Prewitt", img_prewittx + img_prewitty)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()