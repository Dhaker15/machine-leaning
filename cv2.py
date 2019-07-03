# -*- coding: utf-8 -*-
"""cv2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qBdaLEq1ftXQvy3Fhu_Z4HII4FetWaUq
"""

import cv2
import matplotlib.pyplot as plt
from google.colab.patches import cv2_imshow

print(cv2.__version__)

#image name and image property
img=cv2.imread("a.jpg",1) 
#1 means in same color channel --grb or rgb   0means no color channel --black &white --gray image
img1=cv2.imread("a.jpg",0) 
# -1 maintain image transparancy

img

img.shape

type(img)

#to display image
cv2.imshow("a.jpg",img)

#wait for window to class
cv2.waitkey(30)   #mili/micro  seconds

plt.imshow(img[0:120,12:150])

plt.imshow(img)

#split into BGR
x,y,z=cv2.split(img)

plt.imshow(x)

plt.imshow(y)

plt.imshow(z)

import numpy as np

myimage=np.zeros((512,512))

plt.imshow(myimage)

cv2.rectangle(img,(0,0),(200,200),(0,0,255),-1)

plt.imshow(img)
