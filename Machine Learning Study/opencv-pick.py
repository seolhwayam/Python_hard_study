import numpy as np
import cv2

image = cv2.imread('mandrill.png')
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

blue_low = np.array([80,0,0])
blue_high = np.array([130,255,255])

my_mask = cv2.inRange(image_hsv,blue_low,blue_high)
#범위 내에 있는 픽셀 1(흰색) , 없는 픽셀은 0(검정)

extracted = cv2.bitwise_and(image,image,mask =  my_mask)

cv2.imshow('original',image)
cv2.imshow('mask',my_mask)
cv2.imshow('extracted',extracted)

cv2.waitKey(0)
cv2.destroyAllwindows()

