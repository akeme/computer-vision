'''
Daniel Anderson de Souza Leite
Engenharia de Telecomunicações-IFCE
Sistemas Multimídia
Prof. Dr. Pedro Pedrosa
'''
from sklearn.datasets import load_iris
from sklearn.linear_model import Perceptron
import matplotlib.pyplot as plt
import numpy as np
import cv2 #OpenCV
from sklearn.linear_model import Perceptron
import matplotlib.pyplot as plt
from featureExtraction import HU_FE

dataset=[]
rotulos=[]
imgList=[]

#Leitura banco de imagens arquivo.txt
inputData = open('ocr_car_numbers_rotulado.txt')
line = inputData.readline()
length = len(line) - 2

#Cria uma listas com strings equivalente a uma imagem que é um vetor-linha no banco. E cria os rótulos que são o último caracter no vetor-linha do banco.
while line:
    imgList.append(line[0:length:2])
    rotulos.append(int(line[length]))
    line = inputData.readline()

#Funções de Extração de caracteristicas
# Momentos de HU  = HU_FE(image)
# LBP =	 LBP_FE(image)
# GLCM 	= GLCM_FE(image)

#Cria o dataset com as caracteristicas das imagens
for num_img in range(len(imgList)):
    temp = imgList[num_img]
    # Transformando string em valores uint8
    imagem = np.zeros(1225, dtype=np.uint8)
    for x in range(1225):
        imagem[x] = int(temp[x])
    imagem = np.reshape(imagem, (35, 35))
    dataset.append(HU_FE(imagem))

if __name__ == '__main__':
    clf = Perceptron(tol=1e-5)
    clf.fit(dataset, rotulos)
    predicao=clf.predict(dataset)

    #print('Lista dos coeficientes:',clf.coef_) # the weights
    print('\nLista do Bias:',clf.intercept_) # the bias
    print('\nPredicão:',predicao)

    temp3 = np.zeros((len(dataset), 7), dtype=np.uint8)
    for i in range(len(dataset)):
        temp2 = dataset[i]
        for j in range(7):
            temp3[i][j] = temp2[j]
    #Taxa de Acerto
    hit = 0
    for m in range(len(rotulos)):
        if rotulos[m] == predicao[m]:
            hit += 1
    percet=(hit/len(rotulos))*100
    print("Hits: %.1f" % percet, '%')

    #Plot dos dados
    plt.figure(1, figsize=(5, 5))
    plt.clf()
    plt.scatter(temp3[:, 0], temp3[:, 4], c=rotulos, cmap=plt.cm.Set1, edgecolor='face')
    plt.show()

