function figure35
f = imread('Fig0305(a)(spectrum).tif ');
g = im2uint8(mat2gray(log(1+double(f))));
subplot(1,2,1); imshow(f);%axis image off;
subplot(1,2,2); imshow(g);%axis image off;
colormap(gray); 