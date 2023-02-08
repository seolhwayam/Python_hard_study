# file io

# 파일 열기
# 파일 객체 = open(파일 경로, 읽기 모드)
# w : 쓰기모드 / r : 읽기모드 / a : 이어쓰기 모드
# String으로 써야됨 ('파일경로','읽기모드')

# 파일 닫기
# 파일객체.close()

# 쓰기 모드(w)
# fp = open('war_flower.txt','w') # 파일 쓰기

# 1) print('글쓰기',file = 파일객체)
# print('고니',file=fp) #실제 쓰기
# print('정마담',file=fp) #실제 쓰기
# print('아귀',file=fp) #실제 쓰기
#
# 2) 파일객체.write('글쓰기')
# fp.write('너부리') # 실제 쓰기
#
# fp.close() #파일 닫기

# 읽기 모드(r)
#fp = open('wf.txt','r')

#lines = fp.readlines()
# 파일을 1행 단위의 리스트 원소로 변경(파일>리스트(1줄단위)

#1) rstrip('\n') 파일내 줄바꿈 삭제
# for line in lines:
#      print(line.rstrip('\n'))

#2) 슬라이싱 이용한 파일내 줄바꿈 삭제
# for line in lines:
#      print(line[0:-1])

#3) end옵션을 이용한 줄바꿈 삭제
# readlines()사용 후 end옵션은 쓸 수 없다.
# for line in fp:
#      print(line,end=" ")

# fp.close()

# with
#with open('파일경로') as 파일객체
#>>>>>들여쓰기 구문
# 들여쓰기 내용 실행 후 자동으로 close
# 프로그래머의 실수을 줄여줌
with open('wf.txt') as fp:
     lines = fp.readlines()
     for line in lines:
          print(line)



