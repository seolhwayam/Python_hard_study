#tuple
#immutable 불변, 상수의 리스트라고 할 수 있다.
#( ) 사용
#튜플의 원소를 정의한 후에는 추가, 삭제, 수정 불가

#mutable - 변경되는 객체 (객체의 상태를 변경할 수 있음)
#list, set, dictionary
#(값이 변경될 수 있는) 객체의 경우에는 모든 객체를 각각 생성해서 참조

#immutable - 변경되지 않는 객체 (객체의 상태를 변경할 수 없음)
#int, float, tuple, str, bool
#객체의 값이 같은 경우에 변수에 상관없이 동일한 곳을 참조합니다.

#리스트 [] / 딕셔너리 {} / 튜플 ()

empty = ()
numbers = (1, -9, 7)
print(numbers[1])
# tuple도 인덱스는 [] 사용

#튜플 내용 for문으로 돌리기
subjects = ('python','c++','english') # packing
for subject in subjects:
   print(subject)



# subjects = ('python','c++','english')
#               |        |        |
#              kim,     han,     tom = subject  #unpacking(풀어헤친다)
# python > kim / c++ > han / english > tom 각각 저장

kim, han, tom = subjects
print(kim ,han, tom)
# python c++ english

# packing과 unpacking은 변수 갯수가 같아야 한다.

a = input()
b = input()
t = b
b = a
a = t
print(a,b)
# a와 b를 입력받고 print(a,b)구문을 변경하지 않은 상태로 반대로 출력하기(일반)

a1 = input()
b1 = input()
a1 , b1 = b1, a1
# ↑ 튜플 간략화 버전

# a1 , b1 = (b1 , a1)
# ↑ 튜플 기존 버전
# packing과 unpacking을 동시에 수행

print(a1,b1)
# a와 b를 입력받고 print(a,b)구문을 변경하지 않은 상태로 반대로 출력하기(튜플이용 버전)

