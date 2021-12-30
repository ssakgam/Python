# 변수 정리
# 자바에서는 변수를 선언하기 전에 자료형을 선언

# 파이썬
# 변수 = 모든 자료형을 저장할 수 있다. 자료형을 선언하지 않는다.

pi = 3.141592999999999999
print(pi)
print(type(pi))
print(pi + 2) # 사칙 연산 다 됨
print(pi * pi)
print(str(pi) + "test")

# 복합대입연산자.
# a += 10
# +=, -=, *=, /=, %=, **=
print("*"*30)
number = 100
number += 10
print("110 = >", number)

print("*"*30)
# ++ 연산자 안됨!!!!!!!!!!!
#number2 = ++number
#print(number2)

string = "안녕하세요"
string += "!"
string += "*"
print("string :", string)