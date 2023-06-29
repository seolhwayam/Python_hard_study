import numpy as np
import cv2

org = cv2.imread('mandrill.png')

kernerl1 = np.ones((3,3),np.float32)/9
kernerl2 = np.ones((9,9),np.float32)/81

averaged33 = cv2.filter2D(org,-1,kernerl1)
averaged99 = cv2.filter2D(org,-1,kernerl2)

cv2.imshow('filter1',averaged33)
cv2.imshow('filter2',averaged99)

cv2.waitKey(0) # 키보드 기다리기
cv2.destroyAllwindows() # 키보드 값 입력시 모든 창 종료

