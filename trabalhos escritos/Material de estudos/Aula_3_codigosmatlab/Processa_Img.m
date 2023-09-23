function [ImgProc,a,b,M,N] = Processa_Img(img, SizeKernel, type)
%SizeKernel é o tamanho da masc 
%type: 'esp' ou 'zeros'
    
    [M,N] = size(img);
    a = (SizeKernel(1) - 1)/2;
    b = (SizeKernel(2) - 1)/2;
    
    if strcmp(type,'esp') %Espelhamento nas bordas
        ImgProc = [];
        ImgProc = [flipud(img(1:a,:)); img; flipud(img(end-a+1:end,:))];
        ImgProc = [fliplr(ImgProc(:,1:b)) ImgProc fliplr(ImgProc(:,end-b+1:end))]; 
    end
    
    if strcmp(type,'zeros') %Coloca zeros nas bordas
        ImgProc = zeros(M + 2*a, N + 2*b);
        ImgProc(a+1:M+a, b+1:N+b) = img;
    end
end