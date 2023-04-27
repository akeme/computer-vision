import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('opencv-files/haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier('opencv-files/haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('opencv-files/haarcascade_smile.xml')


cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    # para aplicar os classificadores => cinza

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,scaleFactor = 1.5, minNeighbors = 5)
    for (x,y,w,h) in faces:
    	print (x,y,w,h) #localização do rosto no frame
    	#região de interese - haar cascade identifica que existe um rosto
    	roi_gray = gray [y:y+h,x:x+w] #(ycord_start, ycord_end)
    	
        #aqui q salva a imagem
        img_item = "my-image.png"
    	cv2.imwrite(img_item,roi_gray)



    	color = (255,0,0) #BGR 0 - 255 (para desenhar)
    	stroke = 2 #valor da linha
    	end_cordX = x + w
    	end_cordY = y + h

    	#marcar o rosto na imagem 
    	#cv2.rectangle(imagen, (start point),(end point),color BRG, line)
    	cv2.rectangle(frame, (x,y) , (end_cordX, end_cordY),color, stroke)

    
    	#recognize? AI moldes, deep learn models predict - keras, tensorflow, pytorch, scikit
        #subitems = smile_cascade.detectMultiScale(roi_gray)
        #for (ex,ey,ew,eh) in subitems:
        #   cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)


    
    # display the result frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()