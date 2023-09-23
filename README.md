# Computer Vision

This  Repository contains my code while studing to Computer Vision Course / IFCE. 
And the codes that I use as a reference in group project. 


Trying to organize the files 

***Work in progress***

___

## Visão computacional
### OpenCV e Python 


vários materiais utilizando openCV e Python - 
* códigos básicos: filtros, tresholding
* reconhecimento e identificação de pessoas (a identificação não está muito boa)
* identificação de objetos
* Arquivos para trabalhar com videos
* materiais de estudos


***Importante*** 

<b>quando for trabalhar com ML ou DL</b>
```bash
#execute
python config.py

```
verifica se as bibliotecas estão instaladas e quais as versões. 


<p> arquivos .ipynb abrir com Jupyter Notebook </p>
<p>arquivos .py abrir com o python 3 #todos os códigos foram feitos com python3</p>

<p>arquivos .m abrir com o matlab  </p>



<b> observação </b>
utils.py classe criada para ajudar a configurar os videos, reaproveitar os códigos

olhar esse material 
https://www.cs.cmu.edu/~efros/courses/LBMV07/

objetivo primário: reconhecer e identificar pessoas na imagem / video 

<b>observação 2:</b> visual-logging biblioteca que facilita a apresentação dos resultados utilizando openCV, uma opção a ser utilizada



DICA: faça um ambiente virtual

olhar o trabalho de:
http://people.csail.mit.edu/tomasz/
http://cs.brown.edu/people/pfelzens/

<b>utilizando o jupyter notebook</b>>
```bash
#no windows, procurar Jupyter

#no linux - de preferência nas pastas dos arquivos

jupyter notebook 

#ou 

jupyter lab

```


<h2> um pouco de teoria </h2>

<b>reconhecimento ou detecção de rostos (ou de um objeto ): </b> dizer se na imagem existe ou não o objeto em questão
utiliza os haar cascades classifier, no caso do rosto indicado por  Paul Viola and Michael Jones

https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html

já existem classificadores prontos, porém dependendo do objeto que será identificado deverá ser construído

https://www.youtube.com/watch?v=jG3bu0tjFbk&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq&index=17

<b>identificação :</b>
dizer quem é na foto (ou o que é) precisa de treinamento - AI normalmente deep learning e uma biblioteca com diversas imagens para o treinamento
ferramentas para o python: keras, tensorflow, pytorch, sckit learn

<b> tracking: </b>
outro problema a ser abordado (depois) - detecção de movimento e "acompanhar"
um objeto de interesse


IMPORTANTE 
*verificar se ainda é valido*
<b> observação de instalação: </b>

ao instalar a openCV colocar opção dos arquivos de contrib
pois alguns módulos de reconhecimento não estão no módulo principal ainda.
exemplo createLBPHFaceRecognizer

```bash

pip install opencv-contrib-python

```

## alguns sites interessantes
https://www.pyimagesearch.com/2018/05/14/a-gentle-guide-to-deep-learning-object-detection/

https://medium.com/ensina-ai/detectando-objetos-com-m%C3%A9todos-cl%C3%A1ssicos-opencv-cascades-440e29913b1b

http://www.aishack.in/tutorials/image-moments/

