'''
Questão 37
Abrir uma imagem colorida, transformar para tom de cinza e 
aplique a limiarização de otsu. Apliquem o método cvDilate de forma 
iterativa, apresentando o resultado de cada iteração, verificando o 
que o método causa. 
Utilize um elemento estruturante com uma linha e três colunas,
com a referencia no centro, então o objeto deve crescer apenas na 
vertical, pois o elemento estruturante é vertical. O objeto deve 
ser branco e o fundo preto.

'''

import cv2

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
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 3))

# Apply the dilation
for i in range(9):
    dilation = cv2.dilate(threshold_image, kernel, iterations=i)

    # Show the result of the dilation
    cv2.imshow('Dilated image', dilation)
    cv2.waitKey(1000)