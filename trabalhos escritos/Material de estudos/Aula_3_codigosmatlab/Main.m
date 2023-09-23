img = imread('cameraman.tif');

Img_Media = Filtro_Media(img,3);

Img_Mediana = Filtro_Mediana(img,3);

figure, imshow(uint8(Img_Media)), figure, imshow(uint8(Img_Mediana));