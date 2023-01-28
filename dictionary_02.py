#dictonary

# 딕셔너리 키 값 출력
# 딕셔너리 이름.keys()
# fruits.keys()

# 딕셔너리 밸류 값 출력
# 딕셔너리 이름.values()
# fruits.values()

# 딕셔너리 키,밸류 값 출력
# 딕셔너리 이름.items()
# fruits.items()

# 딕셔너리 반복문
# 기본값으로 키 값을 꺼낸다.
# for k in fruits:
#     print(k)
#=====================================================

fruits = {'apple':'사과',
          'watermelon':'수박',
          'strawberry':'딸기',
          'kiwi':'키위',
          'banana':'바나나',
          'pich':'복숭아'}


#키 값만 출력 keys()
print(fruits.keys())
#dict_keys(['apple', 'watermelon', 'strawberry', 'kiwi', 'banana'])

#밸류 값만 출력 values()
print(fruits.values())
#dict_values(['사과', '수박', '딸기', '키위', '바나나'])

#키,밸류 세트 출력 items()
print(fruits.items())
#dict_items([('apple', '사과'), ('watermelon', '수박'), ('strawberry', '딸기'), ('kiwi', '키위'), ('banana', '바나나')])

#반복문으로 키, 밸류값 찍기
for k,v in fruits.items():
    print(k,'\t',v)

#기본값으로 키 값을 꺼낸다.
for k in fruits:
    print(k)



<<<<<<< HEAD
=======

#음식 추천 프로그램 v0.2
# alcohol_foods = {'맥주':'치킨','와인':'치즈','고량주':'짬뽕','소주':'골뱅이소면'}
# while True:
#     alcohol = input('주문하실 술(맥주/와인/고량주/소주/결재)은 ?')
#     if alcohol =='결재':
#         break
#     if alcohol in alcohol_foods.keys():
#         print('{0}에 어울리는 안주는 {1}입니다.'.format(alcohol, alcohol_foods[alcohol]))
#     else:
#         print('{0}은 판매하지 않습니다. 메뉴에서 골라주세요~'.format(alcohol))


#음식 추천 프로그램 v0.3
import random
star = ['테란','저그','프로토스']
print(random.choice(star))

alcohol_foods = {'맥주':'치킨','와인':'치즈','고량주':'짬뽕','소주':'골뱅이소면'}
while True:
    alcohol = input('주문하실 술(맥주/와인/고량주/소주/아무거나/결재)은 ?')
    if alcohol =='결재':
        break
    if alcohol in alcohol_foods.keys():
        print('{0}에 어울리는 안주는 {1}입니다.'.format(alcohol, alcohol_foods[alcohol]))
    elif alcohol == '아무거나':
        print(random.choice(alcohol_foods))
    else:
        print('{0}은 판매하지 않습니다. 메뉴에서 골라주세요~'.format(alcohol))
>>>>>>> 1ad918fb815d45d948dd216afecc4d5293fa61f8
