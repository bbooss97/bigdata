import numpy as np
from PIL import Image
from sklearn.decomposition import TruncatedSVD

#singular value decomposition with sklearn
#return the reconstructed image Ak and the energies retrieved in percentage ||Aki||^2 / ||A||^2
def svd(image,nComponents):
    svd = TruncatedSVD(n_components=nComponents)
    svd.fit(image)
    t=svd.transform(image)
    return svd.inverse_transform(t),svd.explained_variance_ratio_

#read image in numpy array in grayscale
def readImage(filename):
    return np.array(Image.open(filename).convert('L'))

#funtion to plot the image with matplotlib
def plotImage(image):
    # Image.fromarray(image).show()
    plt.imshow(image, cmap='gray')
    plt.show()




image=readImage('./image.jpg')
print(f"the shape of the image is {image.shape}")

image,energies=svd(image,200)
print(f"those are the energies of the components: {energies} and the total energy retrieved in percentage is: {energies.sum()}" )
plotImage(image)




