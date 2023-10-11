'''
Questão 35
Abrir uma imagem colorida, transformar para tom de cinza e 
aplique a limiarização de otsu. Apliquem o método cvDilate de 
forma iterativa, apresentando o resultado de cada iteração, 
verificando o que o método causa. O resultado deve ser aumentar
as regiões brancas, então se o objeto for branco este método 
aumentará o objeto.


'''

import cv2
import numpy as np

# Read a rgb image
image = cv2.imread('img/q35.jpg')

# Transform to grayscale
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Show the input image
cv2.imshow('Input grayscale image', grayscale_image)

# Apply the threshold
ret, threshold_image = cv2.threshold(grayscale_image, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# Show the result of the threshold
cv2.imshow('Threshold image', threshold_image)

# Create the structuring element
kernel = np.ones((5, 5), np.uint8)

# Apply the dilation
for i in range(7):
    dilation = cv2.dilate(threshold_image, kernel, iterations=i)

    # Show the result of the dilation
    cv2.imshow('Dilated image', dilation)
    cv2.waitKey(1000)