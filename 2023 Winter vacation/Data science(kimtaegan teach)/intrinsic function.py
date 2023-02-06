# map(함수, 순환가능한 자료구조)
# 순환가능한 자료구조 : list , dictionary , 문자열 , 범위 range


# square ver_1(for버전)
# def square(n):
#     return n*n
#
# for k in range(1,6):
#     print(square(k))


# square ver_2(for버전)
def square(n):
    return n*n

result = []
for k in range(1,6):
    result.append(square(k))

print(result)



# square_map (map버전)
def square_map(n):
     return n*n

print(list(map(square_map,[1,2,3,4,5])))
#map함수 쓸때에는 list로 변환을 해야쓸 수 있다.
#for문 기능도 있는 것
#코드가 간결하다.



#filter(함수, 순환가능한 자료구조)
# 순환가능한 자료구조 : list , dictionary , 문자열 , 범위 range
def odd(n):
    return n % 2 ==1
print(list(filter(odd,[1,2,3,4,5])))
