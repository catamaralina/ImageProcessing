import cv2
import numpy as np

# Read a single-channel TIFF image
im = cv2.imread(r'C:\Users\talij\Documents\_CODINGPROJECTS\imagery\b5.tif', cv2.IMREAD_GRAYSCALE)

szim = im.shape  # Size of the image
minim = np.min(im)
maxim = np.max(im)

# Initialize arrays for different enhancements
L = np.zeros(szim, dtype=np.uint8)
R = np.zeros(szim, dtype=np.uint8)
S = np.zeros(szim, dtype=np.uint8)
E = np.zeros(szim, dtype=np.uint8)

# Linear Enhancement
L = ((im - minim) / (maxim - minim)) * 255

# Square Root Enhancement
R = np.sqrt((im - minim) / (maxim - minim)) * 255

# Square Enhancement
S = (((im - minim) / (maxim - minim)) ** 2) * 255

# Equalization Enhancement
num = 256
count = np.zeros(256)
for k in range(256):
    count[k] = np.sum(im == k)

prob = count / np.prod(szim)
s = np.round((num - 1) * np.cumsum(prob))

for i in range(szim[0]):
    for j in range(szim[1]):
        E[i, j] = s[int(im[i, j])]

# Convert arrays to uint8 for saving images
L = L.astype(np.uint8)
R = R.astype(np.uint8)
S = S.astype(np.uint8)
E = E.astype(np.uint8)

# Writing data to individual images
cv2.imwrite('b5_im.tif', im)
cv2.imwrite('b5_LEcorr.tif', L)
cv2.imwrite('b5_REcorr.tif', R)
cv2.imwrite('b5_SEcorr.tif', S)
cv2.imwrite('b5_EEcorr.tif', E)

# Displaying images
cv2.imshow('Original Image', im)
cv2.imshow('Linear Enhancement', L)
cv2.imshow('Square Root Enhancement', R)
cv2.imshow('Square Enhancement', S)
cv2.imshow('Equalization Enhancement', E)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Plot histogram of the Equalization Enhancement image
hist, _ = np.histogram(E.flatten(), bins=256, range=(0, 256))

# Plotting histogram
hist_image = np.zeros((256, 256), dtype=np.uint8)
cv2.normalize(hist, hist, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
for i in range(256):
    cv2.line(hist_image, (i, 256), (i, 256 - int(hist[i])), 255)

cv2.imshow('Histogram', hist_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
