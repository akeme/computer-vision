#https://pythonprogramming.net/loading-video-python-opencv-tutorial/
#https://www.youtube.com/watch?v=PmZ29Vta7Vc

import numpy as np
import cv2

cap = cv2.VideoCapture(0) # 0 num webcam, se tiver mais de um 0,1,2...
						  # ou (endereço do video)
						   
##record the video - uncomment the lines bellow
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read() #ret - true/false

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame) #color
    cv2.imshow('gray',gray)	  #cinza 
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
# evita que dê problemas ao chamar a webcam de novo
cap.release()
#out.release() #uncomment if you are recording
cv2.destroyAllWindows()
