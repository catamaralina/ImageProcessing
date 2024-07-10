# ImageProcessing
- Code created for image processing tasks, such as image enhancement. Images being used are TIF from Landsat9.
- Some code is available as MATLAB or Python, or both.

## Band Merging 
- Each band is its own TIF image. This merges the bands together into one image with multiple bands.
- Python with libraries: arcpy.

## Image Enhancement
- Reads a TIF image (currently just one band) and performs different enhancements: Linear, Square Root, Square and Equalization.
- Enhanced images are written to new TIF files.
- Python with libraries: cv2, numpy.
- MATLAB code available.

## Principal Component Analysis (PCA)
- Reads merged TIF image.
- Performs statistical analysis.
- Finds eigenvectors and values.
- Performs PCA and reconstructs the images.
- Python (currently debugging) with libraries: rasterio, matplotlib, numpy, sklearn.
- MATLAB code available.
