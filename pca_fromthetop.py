import rasterio
import matplotlib.pyplot as plt
import numpy as np

# for pca
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

src = rasterio.open(r"C:\Users\talij\Documents\_CODINGPROJECTS\imagery\2022_10_22_b2-7.TIF")

# more bands
array = src.read()
bands = array.shape[0]
print(type(bands))
for i in range(bands):
    band = array[i]
    type = src.dtypes[i]
    pixel_count = array.shape[1]*array.shape[2]
    # avg_pix = sum(sum(band))/pixel_count
    mean_pix = band.mean()
    min_pix = band.min()
    max_pix = band.max()
    sqdif = sum(sum((band-mean_pix)**2))
    std_dev = np.sqrt((1/(pixel_count-1))*sqdif) #    std_dev = band.std()

    var = (1/(pixel_count-1))*(sum(sum((band-mean_pix)**2))) #    var = band.var()

    print('dtype: ', type)
    print('min:', min_pix)
    print('max: ', max_pix)
    print('mean: ', mean_pix)
    print('standard dev: ', std_dev)
    print('var: ', var)
    print()

cov_matrix = np.zeros((bands, bands))
for j in range(array.shape[0]):
    for k in range(array.shape[0]):
        bandj = array[j]
        bandk = array[k]

        muj = np.mean(bandj)
        muk = np.mean(bandk)

        print(f"{muj:.10f}")
        print(muk)

        cov_matrix[j ,k] = np.mean((bandj-muj)*(bandk-muk))

print('cov matrix: \n' , cov_matrix, '\n')

D, V = np.linalg.eig(cov_matrix)
# D are eigenvalues
# V are eigenvectors
print(D)
print(V)

# creating matrix with eigvalues along diag.
diag = np.diag(D)

# print(array[1])

# pyplot.imshow(array, cmap='gist_earth')
# pyplot.show()

#-----     ----   -----   ----    ----     -----    ----     -----      -----     ---- 
# Perform PCA
pca = PCA(n_components=bands)
PC = pca.fit_transform(array.reshape(bands, -1).T)

# Reconstruct using PCA components 2 to 6
reconstructed_X = np.dot(PC[:, 1:6], pca.components_[1:6, :])
reconstructed_array = reconstructed_X.T.reshape(array.shape)

# Visualize the original and reconstructed images
plt.figure(figsize=(12, 6))

# Original Image (showing bands 1, 2, and 3)
plt.subplot(1, 2, 1)
plt.imshow(array[[0, 1, 2], :, :].transpose(1, 2, 0))
plt.title('Original Image (Bands 1, 2, 3)')
plt.axis('off')

# Reconstructed Image (showing reconstructed bands 2 to 6)
plt.subplot(1, 2, 2)
plt.imshow(reconstructed_array[1:6, :, :].transpose(1, 2, 0))
plt.title('Reconstructed Image (Bands 2 to 6)')
plt.axis('off')

plt.tight_layout()
plt.show()