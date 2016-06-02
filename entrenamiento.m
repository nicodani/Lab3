function [A,B,fil,col,imglun,imgpiel]=entrenamiento(img);

img = double(img)./255;

masklun=roipoly(img);
s=size(masklun);
a=s(1);
b=s(2);
maskpiel=ones(a,b)-masklun;

masklun2=double(masklun);
maskpiel2=double(maskpiel);
siz=size(masklun2);
fil=siz(1);
col=siz(2);
maskp=zeros(fil,col,3);
maskl=zeros(fil,col,3);
for i=1:fil;
    
    for j=1:col;
   
        if masklun2(i,j)==1;
            
            maskl(i,j,:)=[1 1 1];
        else
            maskl(i,j,:)=[0 0 0];
        end
        
        if maskpiel2(i,j)==1;
            maskp(i,j,:)=[1 1 1];
        else
            maskp(i,j,:)=[0 0 0];
        end
    end
    
end

imglun=img.*maskl;
imgpiel=img.*maskp;

numpixskin=0;
numpixlun=0;
A=zeros(1,1,3);
B=zeros(1,1,3);
for i=1:fil;
    
    for j=1:col;
        temp1=imglun(i,j,:);
        temp2=imgpiel(i,j,:);
        if temp1~=0;
            numpixlun=numpixlun+1;
            A=A+temp1;
        end
        if temp2~=0;
            numpixskin=numpixskin+1;
            B=B+temp2;
        end
    end
    
end

A= A./numpixlun;
B= B./numpixskin;

end
