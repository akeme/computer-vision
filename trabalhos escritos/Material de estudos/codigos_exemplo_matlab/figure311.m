function figure311
close all;
f = imread('Fig0310(a)(Moon Phobos).tif ');
p = twomodegauss(0.15, 0.05, 0.75, 0.05,1,0.07,0.002);
subplot(2,2,1);  plot(p);
g = histeq(f, p);
subplot(1,2,2);
imshow(g);
subplot(2,2,3);
imhist(g);