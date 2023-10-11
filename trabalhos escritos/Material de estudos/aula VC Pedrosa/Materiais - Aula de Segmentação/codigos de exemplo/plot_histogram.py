import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)
plt.ion()

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #img = cv2.cvtColor(frame, 0)

    # Display the resulting frame
    cv2.imshow('frame',img)

    # Display image histogram - 1    
    plt.clf()    
    plt.hist(img.ravel(), 256, [0,256], color=None, cumulative=False, stacked=False)                
    plt.draw()
    plt.pause(0.00001)
    
    # Display image histogram - GRB    
    '''
    plt.clf()        
    color = ('g','r','b')
    for i,col in enumerate(color):
        histr = cv2.calcHist([img],[i],None,[256],[0,256])
        plt.plot(histr, color = col)
        plt.xlim([0,256])    
    plt.draw()
    plt.pause(0.00001)
    '''    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()