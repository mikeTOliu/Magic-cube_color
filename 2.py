import numpy as np
import cv2
import time
cap=cv2.VideoCapture(1)
ret,frame=cap.read()
cv2.namedWindow('cammera1')
time.sleep(3)
cv2.imshow('cammera1',frame)
cv2.imwrite('./cammera1.jpg',frame)
Long=len(frame)
Wite=len(frame[0])
picture_cut=[9]
Long_cut=int(Long/3)
Wite_cut=int(Wite/3)
frame_cut_1=frame[Long_cut*0:Long_cut,Wite_cut*0:Wite_cut]
frame_cut_2=frame[Long_cut*1:Long_cut*2,Wite_cut*0:Wite_cut]
frame_cut_3=frame[Long_cut*2:Long_cut*3,Wite_cut*0:Wite_cut]
frame_cut_4=frame[Long_cut*0:Long_cut,Wite_cut*1:Wite_cut]
frame_cut_5=frame[Long_cut*1:Long_cut*2,Wite_cut*1:Wite_cut]
frame_cut_6=frame[Long_cut*2:Long_cut*3,Wite_cut*1:Wite_cut]
frame_cut_7=frame[Long_cut*0:Long_cut,Wite_cut:Wite_cut]
frame_cut_8=frame[Long_cut*1:Long_cut*2,Wite_cut:Wite_cut]
frame_cut_9=frame[Long_cut*2:Long_cut*3,Wite_cut:Wite_cut]
cv2.namedWindow('cut1')
cv2.imshow('cut1',frame_cut_1)
print(Long,'*',Wite)
cv2.waitKey (0)  