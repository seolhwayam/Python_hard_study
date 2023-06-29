import numpy as np
import cv2

img_gray = cv2.imread('green_back.png',0)

img_adge = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,blockSize=9,C=0)

cv2.imshow('original',img_gray)
cv2.imshow('adge',img_adge)

cv2.waitKey(0)
cv2.destroyAllwindows()
