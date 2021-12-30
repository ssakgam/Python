# cafe에 비교연산자 코딩 하기
"""
== 같다
!= 다르다
<   작다
>   크다
<=  작거나 같다
>=  크거나 같다
"""
###################################
print("김길동" == "김길동")
name = "하하"
print("김길동" != name)    # True
print("김길동" < name)     # 김길동 < 하하 True ( 즉, ㄱ 보다 ㅎ 이 더 큰 문자열 유니코드 숫자)
print("김길동" > name)     # False

print("*"*30)

hungry = True
sleepy = False
print(type(hungry)) # 자료형
print(not hungry)   # 논리부정
print(hungry and sleepy) # A and B : A, B 가 모두 True 가 되어야 True
print(hungry or sleepy)  # A or B  : 둘 중 하나만 True