import cv2

img_color = cv2.imread('mandrill.png',cv2.IMREAD_COLOR)
cv2.line(img_color,(0,0),(200,200),(0,0,255),5) #선 그리기
cv2.arrowedLine(img_color,(0,0),(200,200),(0,0,255),5) # 화살표 그리기
cv2.rectangle(img_color,(0,0),(200,200),(0,0,255),5) # 사각형 그리기
cv2.putText(img_color,'monkey',(70,70),fontFace =2, fontScale =1,color =(0,0,0)) # 글자 넣기

cv2.imshow('test-putText',img_color) # 보여주기

cv2.waitKey(0) # 키보드 기다리기
cv2.destroyAllwindows() # 키보드 값 입력시 모든 창 종료
