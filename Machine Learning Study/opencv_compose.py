import cv2
global img1, img2

def on_change_weight(x):
    weight = x/100 # 가중치 생성 0~1 사이 값
    img_merged = cv2.addWeighted(img1, 1-weight, img2, weight ,0) # 가중치 조절하기
    cv2.imshow('Dispaly',img_merged) # 보여주기

cv2.namedWindow('Display') #창띄우기 1
cv2.createTrackbar('weight','Display',0,100,on_change_weight) # 트렉바 만들기

img1 = cv2.imread('green_back.png') # 이미지1 읽기
img2 = cv2.imread('iceberg.png') # 이미지2 읽기
img1 = cv2.resize(img1,(300,400)) # 이미지1 사이즈 조절
img2 = cv2.resize(img2,(300,400)) # 이미지2 사이즈 조절

cv2.waitKey(0)
cv2.destroyAllwindows()
