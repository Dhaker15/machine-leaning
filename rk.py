#!/usr/bin/python3

import cv2

#starting camera
cap=cv2.VideoCapture(0)


#to check camera is started or not
if cap.isOpened() :
   print("camera is ready to take picture")
else:
   print("check your web cam drivers")

#now we can take read input from camera
status,img=cap.read()   #it will take first picture
status1,img1=cap.read() 


#now showing
cv2.imshow('liveimage',img)
cv2.imshow('liveimage1',img)
cv2.waitkey(0)

#to close camera

cap.release()
