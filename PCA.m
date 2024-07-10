%PCA 
clear all
B  = imread('postaug2018.tif');
b = double (B);
sz = size(b);
sz(3) = 3; 
%---
for k = 1:6 %looping through bands
    Bk = b(:, :, k); %selecting everything from the band as a 2d image
    mu(k) = sum(sum(Bk))/(numel(Bk)); %mean vector
    sKsd = sum(sum(   (Bk-mu(k)).^2  )); 
    s(k) = sqrt((1/(numel(Bk)-1))*sKsd); %standard deviation of band k (Question 5)
    var(k) = (1/(numel(Bk)-1))*(sum(sum(   (Bk-mu(k)).^2  ))); %variance
end

%var covar matrix
for k = 1:6
    for l = 1:6
        covm(k, l) = (1/(numel(b(:, :, k))))*sum(sum((b(:, :, k)-mu(k)).*((b(:, :, l)-mu(l)))));
     end
end

[R, D] = eig(covm); 

%R is the right eigenvectors
%Left and right eigenvectors are eachothers transpose. . .  (thanks
%wolfram)
%D is the eigenvalues
d = diag(D);
[z, ind] = sort(-1*d); %gives index of sorting from highest to lowest var
d = d(ind); %sort the other eigval
R = R(:, ind); %sort the eigvec %same as pca(X) COEFF seen below
%var = var(ind);
%prcomp = pca(covm);
%code referenced from https://www.mathworks.com/matlabcentral/answers/167938-how-pca-can-be-applied-to-an-image-to-reduce-its-dimensionality-with-example

X = reshape(b, sz(1)*sz(2), 6); %reshape original data matrix into 2d matrix
[COEFF, SCORE, LATENT, TSQUARED, EXPLAINED, MU] = pca(X);
PC = X*COEFF;

aprxRank1 = SCORE(:,:) * COEFF(:,:).' + repmat(MU, sz(1)*sz(2), 1); %recreation all bands
aprxRank15 = SCORE(:,1:5) * COEFF(:,1:5).' + repmat(MU, sz(1)*sz(2), 1);%recreation bands 1-5
aprxRank26 = SCORE(:,2:6) * COEFF(:,2:6).' + repmat(MU, sz(1)*sz(2), 1);%recreation bands 2-6

for i = 1:sz(3) %to view the images created imshow(------(:, :, i), []) where i is the view band
    pcaIm(:, :, i) = reshape(PC(:, i), sz(1), sz(2)); %reshaping PCs back into 3d matrix
    
    %recreation using PCs
    recIm1(:, :, i) = reshape(aprxRank1(:, i), sz(1), sz(2));
    recIm15(:, :, i) = reshape(aprxRank15(:, i), sz(1), sz(2));
    recIm26(:, :, i) = reshape(aprxRank26(:, i), sz(1), sz(2));
end



%images showing the differences for the first band
imshow(rec1(:, :, 1)-b(:, :, 1), [])
imshow(rec15(:, :, 1)-b(:, :, 1), [])
imshow(rec26(:, :, 1)-b(:, :, 1), [])