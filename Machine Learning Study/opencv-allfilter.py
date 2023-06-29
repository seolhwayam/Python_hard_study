import numpy as np
import cv2

org = cv2.imread('mandrill.png',1)

image_GaussianBlur = cv2.GaussianBlur(org,(9,9),1)
image_medianBlur = cv2.medianBlur(org,9)
image_bilateralFilter = cv2.bilateralFilter(org,9,50,50)

cv2.imshow('original',org)
cv2.imshow('GaussianBlur',image_GaussianBlur)
cv2.imshow('medianBlur',image_medianBlur)
cv2.imshow('bilateralFilter',image_bilateralFilter)

cv2.waitKey(0)
cv2.destroyAllwindows()
