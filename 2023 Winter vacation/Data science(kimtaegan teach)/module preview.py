#module preview

#Built in module 내장(표준)모듈
import math
import random

#math를 이용한 ceil(올림)
print(math.ceil(3.1))

#math를 이용한 floor(내림)
print(math.floor(4.9))

#math를 이용한 sqrt(제곱근)
print(math.sqrt(16))

print(random.randint(1,6))

#===================================
#사용자 정의 모듈
# 1) import
# import 파일이름(모듈이름)
# 사용법 : 파일이름(모듈이름) . 해당함수

# import my_math
# print(my_math.factorial_loop(5))
# print(my_math.square(5))
# print(my_math.power(2,10))

#====================================
# 2) from
from my_math import fibo_recursion,power
# from 모듈이름 import 가져오고 싶은 함수 또는 변수
# 여러개 가져올 수 있다. import 함수1 , 함수2
# 사용법 : 가져온 함수 또는 변수 그대로 사용
# 모듈 이름을 생략하고 함수를 사용한다.

# from 모듈이름 import *
# 모듈이름의 모든 함수를 가져와서 사용
# 모듈 이름을 생략하고 함수를 사용한다.

# 개발자들끼리의 대화, 이 모듈의 이 함수를 쓸거야!

print(fibo_recursion(7))
print(power(5,2))

#======================================
# 3) import ~ + as
# import ~ + as 이름
# 사용법 : 이름.해당함수
import my_math as mm
print(mm.square(5))