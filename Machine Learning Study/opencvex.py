import cv2

img_gray = cv2.imread('mandrill.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow('test-GRAY',img_gray)

img_color = cv2.imread('mandrill.png',cv2.IMREAD_COLOR)
cv2.imshow('test-COLOR',img_color)

cv2.waitKey(0)
cv2.destroyAllwindows()

