import numpy as np
import cv2

org = cv2.imread('mandrill.png',1) #이미지 이름, 1(컬러)

averaged33 = cv2.GaussianBlur(org,(3,3),1)
averaged99 = cv2.GaussianBlur(org,(9,9),1)

cv2.imshow('averaged33',averaged33)
cv2.imshow('averaged99',averaged99)

cv2.waitKey(0)
cv2.destroyAllwindows()
