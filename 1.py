#contours define blue
import numpy as np
import cv2
cap=cv2.VideoCapture(1)
lower_blue=np.array([100,43,43])
upper_blue=np.array([124,255,255])
lower_green=np.array([35,43,43])
upper_green=np.array([77,255,255])
lower_yellow=np.array([26,43,46])
upper_yellow=np.array([34,255,255])
while(True):
    green=[]
    red=[]
    yellow=[]
    ret,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #ret,two=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    #img=cv2.blur(gray,(5,5))
    mask_blue=cv2.inRange(hsv,lower_blue,upper_blue)
    mask_green=cv2.inRange(hsv,lower_green,upper_green)
    mask_yellow=cv2.inRange(hsv,lower_yellow,upper_yellow)
    #blue_or=cv2.bitwise_or(frame,frame,mask_blue_blue=mask_blue_blue)
    #blue_and=cv2.bitwise_and(frame,frame,mask=mask_blue)
    #green_and=cv2.bitwise_or(frame,frame,mask=mask_green)
    #cv2.imshow('1',green_and)
    img,contours, hierarchy, = cv2.findContours(mask_blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    img,contours_green,hierarchy_green=cv2.findContours(mask_green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    img,contours_yellow, hierarchy, = cv2.findContours(mask_yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for i in contours_yellow:
        size=cv2.contourArea(i)
        if 18000>size>1200:
            yellow.append(i)
    for i in contours_green:
        size=cv2.contourArea(i)
        if 18000>size>1200:
            green.append(i)
    for i in contours:
        size=cv2.contourArea(i)
        if 18000>size>1200:
            red.append(i)
    cv2.drawContours(frame,red,-1,(0,0,255),3)
    cv2.drawContours(frame,green,-1,(255,0,0),3)
    cv2.drawContours(frame,yellow,-1,(0,255,0),3)
    #cv2.imshow('frame',frame)
    #cv2.imshow('blue_or',blue_or)
    cv2.rectangle(frame, (133, 67), (507, 440), (255, 255, 0), 2)
    cv2.imshow('frame',frame)
    #cv2.imshow('img',img)
    #cv2.imshow("two",two)
    #cv2.imshow("greay",gray)
    if cv2.waitKey(1)& 0xFF == ord('q'):
        break
cap.release()
cv2.destroyALLwindows()
