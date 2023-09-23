function figure38
clc;
close all;
f = imread('Fig0308(a)(pollen).tif');
subplot(2,2,1); imshow(f);
subplot(2,2,2); imhist(f);
ylim('auto');
g = histeq(f, 256);
subplot(2,2,3); imshow(g);
subplot(2,2,4); imhist(g);
ylim('auto');
