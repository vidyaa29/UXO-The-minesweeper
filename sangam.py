import cv2
import numpy as np
import serial
import time

connected = False
ser=serial.Serial("COM2",9600)
while not connected:
    serin = ser.read()
    connected = True

#cap = cv2.VideoCapture(0)

def nothing(x):
    pass
# Creating a window for later use
cv2.namedWindow('result')

for i in range(0,30):

    #_, frame = cap.read()
    frame = cv2.imread('C:\out\%s.bmp' %(i))
    #converting to HSV
    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    ret,thresh2 = cv2.threshold(grey,250,255,cv2.THRESH_BINARY_INV)
    im2, contours, hierarchy = cv2.findContours(thresh2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
                area = cv2.contourArea(cnt)
                #print area
            #change area limit from 200 to 300
                if area > 300:
                #to find the center of the circle
                    (x,y),radius = cv2.minEnclosingCircle(cnt)
                    center = (int(x),int(y))
                    radius = int(radius)
                #draw a small circle for the center
                    cv2.circle(im2, center, 5, (255, 255, 255), -1)
                #draw the contour around the puck
                    cv2.circle(im2,center,radius,(0,255,0),2)
                    if x >= 80 and x <= 160 and y >= 120 and y <= 200:
                        print x,y
                        ser.write("1")
    cv2.imshow('contour',im2)
    cv2.imshow('image',frame)
    
    k = cv2.waitKey(0) & 0xFF
    if k == 27:
        break

#cap.release()
while ser.read() == '1':
     ser.read()
ser.close() 

cv2.destroyAllWindows()
