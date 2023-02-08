# file io

# 파일 열기
# 파일 객체 = open(파일 경로, 읽기 모드)
# w : 쓰기모드 / r : 읽기모드 / a : 이어쓰기 모드
# String으로 써야됨 ('파일경로','읽기모드')

# 파일 닫기
# 파일객체.close()

# 쓰기 모드(w)
# fp = open('war_flower.txt','w') # 파일 쓰기

# # 1) print('글쓰기',file = 파일객체)
# print('고니',file=fp) #실제 쓰기
# print('정마담',file=fp) #실제 쓰기
# print('아귀',file=fp) #실제 쓰기
#
# # 2) 파일객체.write('글쓰기')
# fp.write('너부리') # 실제 쓰기
#
# fp.close() #파일 닫기

# 읽기 모드(r)
fp = open('wf.txt','r')
for line in fp:
    print(line, end='')

fp.close()

