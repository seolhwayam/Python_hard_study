#음식 추천 프로그램 v0.1
# alcohol_foods = {'맥주':'치킨','와인':'치즈','고량주':'짬뽕','소주':'골뱅이소면'}
# alcohol = input('주문하실 술(맥주/와인/고량주/소주)은 ?')
#
# if alcohol in alcohol_foods.keys():  #알코올(입력받은)이 알코올푸드 키값에 해당한다면?
#     print('{0}에 어울리는 안주는 {1}입니다.'.format(alcohol, alcohol_foods[alcohol]))


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
#star = ['테란','저그','프로토스']
#print(random.choice(star))

alcohol_foods = {'맥주':'치킨','와인':'치즈','고량주':'짬뽕','소주':'골뱅이소면'}
while True:
    alcohol = input('주문하실 술(맥주/와인/고량주/소주/아무거나/결재)은 ?')
    if alcohol =='결재':
        break
    if alcohol in alcohol_foods.keys():
        print('{0}에 어울리는 안주는 {1}입니다.'.format(alcohol, alcohol_foods[alcohol]))
    elif alcohol == '아무거나' :
        print(random.choice(list(alcohol_foods)))
    else:
        print('{0}은 판매하지 않습니다. 메뉴에서 골라주세요~'.format(alcohol))


#=========================================================================
#복제하기

# NEW 이름 = 복제할 딕셔너리 이름
#같은 주소 참고하고 있기 때문에 변경된다!
# copy_alcohol = alcohol_foods
# copy_alcohol['소주']='두부김치'
# print(copy_alcohol)
# {'맥주': '치킨', '와인': '치즈', '고량주': '짬뽕', '소주': '두부김치'}
# print(alcohol_foods)
# {'맥주': '치킨', '와인': '치즈', '고량주': '짬뽕', '소주': '두부김치'}

#복제하기
#이름 = 복제할 이름.copy()
#copy()
#원본 변경 안됨.
copy_alcohol = alcohol_foods.copy()
copy_alcohol['소주']='두부김치'
print(copy_alcohol)
#{'맥주': '치킨', '와인': '치즈', '고량주': '짬뽕', '소주': '두부김치'}
print(alcohol_foods)
#{'맥주': '치킨', '와인': '치즈', '고량주': '짬뽕', '소주': '골뱅이소면'}