function figure39
f = imread('Fig0308(a)(pollen).tif');
hnorm = imhist(f)./numel(f);
cdf =  cumsum(hnorm); 
x = linspace(0,1,256);
plot(x,cdf);
axis([0 1 0 1]);
set(gca, 'xtick',0:0.2:1);
set(gca, 'ytick',0:0.2:1);
xlabel('Input intensity values', 'fontsize',9);
ylabel('Output intensity values', 'fontsize',9);
% Specify text in the body of the graph;
text(0.18, 0.5, 'Transformation function', 'fontsize',9);