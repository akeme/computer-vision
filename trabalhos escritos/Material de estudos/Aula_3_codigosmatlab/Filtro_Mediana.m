function [ImgFiltered] = Filtro_Mediana(img,n)

    Kernel = [n n];
    img = double(img);
    [ImgProc,a,b,M,N] = Processa_Img(img, Kernel, 'esp');
    
    ImgFiltered = zeros(M,N);
    
    for x=a+1:M+a
        for y=b+1:N+b
            vetor=[];
            for i=-a:a
                for j=-b:b
                    vetor = [vetor, ImgProc(x+i, y+j)]; %Concatena
                end
            end
            vetor_ordenado = sort(vetor);
            ImgFiltered(x-a,y-b) = vetor_ordenado((n^2+1)/2);
        end
    end
    
end
