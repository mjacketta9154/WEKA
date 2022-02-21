import cv2
import numpy as np
import matplotlib.pyplot as plt



img = cv2.imread('1.jpg')

plt.imshow(img)

               #write about hsv values 

ORANGE_MIN = np.array([0, 0,120],np.uint8)        # leave first 2 blank mess with third
ORANGE_MAX = np.array([150, 190, 255],np.uint8)   # mess with first 2

hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

frame_threshed = cv2.inRange(hsv_img, ORANGE_MIN, ORANGE_MAX)
 #cv2.imshow( frame_threshed)
plt.imshow(frame_threshed)
