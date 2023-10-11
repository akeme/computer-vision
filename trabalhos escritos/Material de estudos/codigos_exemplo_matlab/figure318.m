function figure318
f = imread('Fig0318(a)(ckt-board-orig).tif');
subplot(2,2,1); imshow(f);
fn = imnoise(f, 'salt & pepper', 0.2);
subplot(2,2,2); imshow(fn);
gm = medfilt2(fn);
subplot(2,2,3); imshow(gm);
gms = medfilt2(fn, 'symmetric');
subplot(2,2,4); imshow(gms);

