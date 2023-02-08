# print 옵션
# 1) sep(separation)
# print('각','단','어',sep='구분자')
# 영단어 그대로, 분리하여 출력한다.
# 구분자 : 갈라놓을 문자

print('s','e','p',sep='@')
# s@e@p

# 2) end
# print('문장', end= " ")
# 줄바꿈을 하지 않게 된다.

print("I like",end=" ")
print("money")
#I like money

# print('문장', end='문장2')
# 문장 후 문장2 출력됨
# sep과 비슷한 기능 수행(구분자 사용 가능)

print("I like",end=" gold and")
print("money")
#I like gold andmoney

# 3)format
# - 숫자를 사용한 format
# print("{0}{1}".format(값0,값1))

print("{0}월{1}일 입니다.".format(10,31))
#10월31일 입니다.

# - % 기호를 사용한 format
# print("%s %d"%("s값","d값"))
# %s : 문자열 , %d : 정수 , %f : 실수
# 출력문과 %사이에 콤아 없음

print("%s을 %d개 주세요"%("아이스크림",10))
# 아이스크림을 10개 주세요
