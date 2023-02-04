# 함수 (Function)
# 한 가지 작업을 수행하도록 디자인된 코드블럭 or 코드의 집합

# 가변 매개변수 / 기본 매개변수 / return

# 함수 만들기
# def 함수이름(매개변수):
#     함수 내용
#     return

# *return은 필수 아님!

def function_test(name):
    print("hi " + name)
    return '이름을 출력함'

function_test('파이썬') #Function call

print(function_test("C++"))

def minus(a, b):
    """ 두 수의 차를 구하는 함수
        매개변수는 a와 b를 받음
    """
    # ↑ 도규먼트 스트링

    return a-b

print(minus(5,3))

help(minus)
#help() ()안에 있는 것에 대한 도움말

print(minus.__doc__)
# minus에 대한 도큐먼트 스트링 출력
# __doc__

#가변 매개변수  *
#  : 인수의 갯수가 오는 것에 따라 대응하도록 하는 것
# 1. 함수안에서 1개만 사용
# 2. 가변매개변수 뒤에 일반 매개변수가 올 수 없음
def print_even(times, *values):
    for value in values:
        print(times * value)

print_even(2,-9,11,7)

# 기본 매개변수
# 1. 기본 매개변수는 일반 매개변수 뒤에 와야한다.
# (일반 매개변수 , 기본 매개변수)
def print_default(value, times=3):
    print(times * value)

print_default(5,2)
# times = 3 기본 매개변수 >> times 매개변수 입력 안할 시 자동 기본값
# times 입력시 입력된 times * value 출력



