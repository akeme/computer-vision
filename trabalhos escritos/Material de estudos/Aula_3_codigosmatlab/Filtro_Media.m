function [ImgFiltered] = Filtro_Media(img,n)
%n é o tamanho da mascara utilizada.
    
    Kernel = [n n];
    img = double(img);
    [ImgProc,a,b,M,N] = Processa_Img(img, Kernel, 'esp');
    
    ImgFiltered = zeros(M,N);

    for x=1+a:M+a
        for y=1+b:N+b
            vetor=[]; %vetor criado apenas para concatenacao.
            for i=-a:a 
                for j=-b:b
                    vetor = [vetor, ImgProc(x+i, y+j)];
                end
            end
            ImgFiltered(x, y)= mean(vetor);
        end
    end
end



