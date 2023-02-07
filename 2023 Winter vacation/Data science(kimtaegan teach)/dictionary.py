#dictionary(dict)
# 리스트와 비슷하나 순서를 따지지 않는다.(index 없음)
# 키와 값이 pair가 원소가 된다.
# 키값은 유일하다.

# 딕셔너리 만들기
# 이름 = {키:밸류 , 키:밸류 }
# fruits = {'apple':'사과','watermelon':'수박'}

# 딕셔너리 불러오기
# 이름[키]
# fruits['watermelon']

#딕셔너리 추가하기
# 이름[키] = 밸류
# fruits['kiwi'] = '키위'

# 딕셔너리 수정하기
# 이름[키] = 수정할 밸류
# fruits['kiwi'] = '키위~'

# 빈 딕셔너리 만들기
# 이름 = {}
# empty = {}

#==================================================
# list >> dictionary (리스트 딕셔러리 변경)
# dict(리스트이름)
# 주의점! 갯수를 맞춰야 한다.
# dict(test)

# 딕셔너리 결합
# 딕셔너리이름A . update(결합할 딕셔너리 이름B)
# A.update(B)
# 주의점! 값은 키 값일 경우 추가되는 딕셔너리 키와 밸류로 변경됨.
# fruits.update(others)

# 딕셔너리 원소지정 삭제
# del 딕셔너리 이름[키]
# 키와 밸류 세트로 삭제됨
# del fruits['apple']

# 딕셔너리 삭제(소멸)
# del 딕셔너리 이름
# del fruits

# 딕셔너리 전체원소 삭제
# 딕셔너리이름.clear()
# fruits.clear()


fruits = {'apple':'사과','watermelon':'수박'}
print(fruits['watermelon'])
print(fruits)
fruits['kiwi'] = '키위'
print(fruits)
fruits['banana'] = '바나나~'
print(fruits)
fruits['kiwi'] = '키위~'
print(fruits)

empty = {}
print(type(fruits),type(empty))
#=====================================================
#       [   0    ,1] [    0   , 1] [   0  , 1 ]
test = [['python',3],['english',2],['dance',1]]
#       [    0    ]  [     1    ]  [    2    ]    번방
print(test[0][1])
print(dict(test))
#dict(리스트이름) >> 리스트를 딕셔너리로 변경

#      [0,1 / 0,1 / 0,1]
test = ['ab','cd','ef']
#      [  0  , 1 ,  2  ]

print(test[1][0])
print(dict(test))
#=====================================================
# 딕셔너리 결합(update)
fruits = {'apple':'사과','watermelon':'수박'}
fruits['pich']='복숭아'
others = {'strawberry':'딸기','kiwi':'키위','pich':'복쑹아'}

fruits.update(others)
print(fruits)
#값은 키 값일 경우 추가되는 딕셔너리 키와 밸류로 변경됨.
#=======================================================
#딕셔너리 원소지정삭제
del fruits['apple']
del fruits['kiwi']
print(fruits)

#딕셔너리 삭제
del fruits

#딕셔너리 전체원소 삭제
fruits.clear()
print(fruits)



