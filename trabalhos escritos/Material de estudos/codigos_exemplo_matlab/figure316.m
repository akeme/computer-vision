function figure316
clc
close all;
f = imread('Fig0316(a)(moon).tif');
w = fspecial('laplacian',0);
g1 = imfilter(f, w, 'replicate');
subplot(2,2,1); imshow(f);
subplot(2,2,2); imshow(g1,[]);
f2 = im2double(f);
g2 = imfilter(f2, w, 'replicate');
subplot(2,2,3);imshow(g2, []);
g = f2-g2;
subplot(2,2,4); imshow(g);
