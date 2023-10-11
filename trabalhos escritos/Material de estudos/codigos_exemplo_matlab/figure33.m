function figure33
clc;
close all;
sprintf('This is a test of Imadjust in DIP Using Matlab (Gonzalez, 2002) \n');
[f,map]  = imread('Fig0303(a)(breast).tif');
g1 = imadjust(f,[0 1], [1 0]); % this is equal to g1 = imcomplement(f)
g2 = imadjust(f, [0.5 0.75],[0 1]);
g3 = imadjust(f,[] , [] , 2);

subplot(2,2,1); image(f); axis image off; 
subplot(2,2,2); image(g1); axis image off;
subplot(2,2,3); image(g2); axis image off;
subplot(2,2,4); image(g3); axis image off;
colormap(gray(256));
