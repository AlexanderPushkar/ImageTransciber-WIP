import imageio # Image analysis
import imageio.v2 as imageio
import matplotlib.pyplot as plt # Used to gather data from images\
import numpy as np
from glob import glob # Used to make loading file paths for images easier


#holds Data of Images
ImagesData = []

#gets all images from folder /Images and loads into Images Data
pth = "C:/Users/18607/Desktop/HandWritingAnalysis/Images/"
for x in glob(pth+"*.png"):
    ImagesData.append(imageio.imread(x))



# function used to grayscale images to simplify analysis
gray = lambda rgb : np.dot(rgb[... , :3] , [0.299 , 0.587, 0.114]) 
#gray = gray(ImagesData[0])

figure, axis = plt.subplots(4)

for x, image in enumerate(ImagesData):
    axis[x].imshow(gray(image), cmap= plt.get_cmap(name = 'gray'), aspect='auto')
    axis[x].set(xticklabels=[])
    axis[x].set(yticklabels=[])

plt.show()    