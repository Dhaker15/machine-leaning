#!/usr/bin/python3

import cv2

#image read
img=cv2.imread('img3.jpg',1)
img1=cv2.imread("img4.jpg",1)
   

img2=img[50:100,100:300]

img3=img1[50:100,100:300]

img[150:200,400:600]=img3

img1[150:200,400:600]=img2

cv2.imshow("imq",img)
cv2.imshow("img",img1)


cv2.waitKey(0)














cv2.waitKey(0)   #wait for window to close
