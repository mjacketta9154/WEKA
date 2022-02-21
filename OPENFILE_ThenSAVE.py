import cv2
import glob
import matplotlib.pyplot as plt
from skimage.filters import roberts
import numpy as np

a = glob.glob("CFPICS/RIBS/*.*")


list_a = []

path = "CFPICS/RIBS/*.*"
# start
for file in glob.glob(path):
    print(file)
    b = cv2.imread(file)
    
    list_a.append(b)
# read and printed files in RIBS Folder

plt.imshow(list_a[10],cmap='gray')



    