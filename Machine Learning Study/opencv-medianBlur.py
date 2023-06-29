import numpy as np
import cv2

org = cv2.imread('salt_pepper.png',0)

image_medianBlur = cv2.medianBlur(org,5)

cv2.imshow('original',org)
cv2.imshow('medianBlur',image_medianBlur)

cv2.waitKey(0)
cv2.destroyAllwindows()
