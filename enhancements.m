%Tali Jonker

clear all; close all;

image = imread('kap.tif');
im = double(image(:, :, 3)); 
szim = size(im); %size of the image
minim = min(min(im));
maxim = max(max(im));

L = zeros(szim);
R = zeros(szim);
S = zeros(szim);
E = zeros(szim);

%For Equalization
num = 256;
count = zeros(1, 256);
for k = 1: 255
    count(k+1) = sum(sum(im==k));
end

    
prob = count/(numel(im));
s = round((num-1)*cumsum(prob));
%-------


%Running all through the image
for i = 1: szim(1)
    for j = 1: szim(2)
        L(i, j) = ((im(i, j)-minim)/(maxim-minim))*255;
        R(i, j) = (sqrt(((im(i, j)-minim)/(maxim-minim))))*255;
        S(i, j) = ((((im(i, j)-minim)/(maxim-minim)))^2)*255;
        E(i, j) = s(im(i, j)+1);
    end
end


%Writing data to individual images
imwrite(uint8(im), 'im.tif');
figure(1);  imshow('im.tif');title('Original Image Band 3');

imwrite(uint8(L), 'LEcorr.tif');
figure(2);  imshow('LEcorr.tif'); title ('Linear Enhancement Band 3');

imwrite(uint8(R), 'REcorr.tif');
figure(3); imshow('REcorr.tif');title('Square Root Enhancement Band 3'); 

imwrite(uint8(S), 'SEcorr.tif');
figure(4);imshow('SEcorr.tif'); title('Square Enhancement Band 3'); 

imwrite(uint8(E), 'EEcorr.tif');
figure(5);  imshow('EEcorr.tif');title('Equalization Enhancement Band 3');


%-----------------------------
%HISTOGRAM 
%-----------------------------
figure();
histogram(E);
xlabel('DN');
ylabel('Occurences'); 
title ('Histogram'); 
axis tight