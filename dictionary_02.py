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



