function figure310
f = imread('Fig0310(a)(Moon Phobos).tif');
subplot(2,2,1); imshow(f);
subplot(2,2,2); imhist(f);
g = histeq(f,256);
subplot(2,2,3); imshow(g);
subplot(2,2,4); imhist(g);