function figure36
clc
close all;
f = imread('Fig0306(a)(bone-scan-GE).tif');
subplot(1,2,1); imshow(f);% axes image off;
g = intrans(f, 'stretch', mean2(im2double(f)),0.9);
subplot(1,2,2); imshow(g);% axes image off;
colormap(gray);