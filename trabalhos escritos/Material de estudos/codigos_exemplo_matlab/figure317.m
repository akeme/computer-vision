function figure317
clc
close all;
f = imread('Fig0316(a)(moon).tif');
w4 = fspecial('laplacian',0);
g4 = f - imfilter(f, w4, 'replicate');
subplot(2,1,1); imshow(f);
subplot(2,2,3); imshow(g4,[]);
w8 = [1 1 1; 1 -8 1; 1 1 1];
g8 = f - imfilter(f, w8, 'replicate');
subplot(2,2,4); imshow(g8,[]);