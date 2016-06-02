clear all ; close all; clc;

img = double(imread('foto38.jpg'))./255;

[A,B,d1,d2,imgA,imgB]=entrenamiento(imread('foto38.jpg'));

figure;
imshow(imgA)
figure;
imshow(imgB)

%%
rho = calRho(A,B);

imges=[img(:,1,:) img img(:,end,:)];
imges=[imges(1,:,:); imges ;imges(end,:,:)];
imgBorde=zeros(d1,d2,3);
tolBorde =18*var(rho);

for i=1:d1-1;
    for j=1:d2;
    
        Atemp = imges(i+1,j,:);
        Btemp = imges(i+1,j+2,:);
        rhotemp = calRho(Atemp,Btemp);
        rhotemp2=calRho(Btemp,Atemp);
        if (norm(rho-rhotemp)<tolBorde); 
            imgBorde(i+1,j+1,:)=[1 1 1];
        elseif norm(rho-rhotemp2)<tolBorde;
            imgBorde(i+1,j+1,:)=[1 1 1];
        end
        
        Atemp = imges(i,j+1,:);
        Btemp = imges(i+2,j+1,:);
        rhotemp = calRho(Atemp,Btemp);
        rhotemp2=calRho(Btemp,Atemp);
        if (norm(rho-rhotemp)<tolBorde); 
            imgBorde(i+1,j+1,:)=[1 1 1];
        elseif norm(rho-rhotemp2)<tolBorde;
            imgBorde(i+1,j+1,:)=[1 1 1];
        end
    end
    
end

imgfinal=img+imgBorde(1:d1,1:d2,:);
figure;
imshow(imgfinal)

