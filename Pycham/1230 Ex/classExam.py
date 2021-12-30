# print("김성태")
# py_exam1.py
from typing import List

a = 50
b = 50
#숫자 50과 숫자 50을 더해서 출력해봅시다! => 결과 100
print(a + b)
#문자열 "50"과 문자열 "50"을 더해서 출력해봅시다! => 결과 5050
print(str(a)+str(b))
#리스트 [50]과 리스트 [50]을 더해서 출력해봅시다!
a = [50]
b = [50]
print(a + b)

print("*"*30)

#py_exam2.py

# //을 이용해서 변수 intdiv에 4를 넣는 수식을 작성해봅시다.
c = 25
d = 6
intdiv = (c //  d)

# %을 이용해서 변수 modular에 1을 넣는 수식을 작성해봅시다.
e = 4
f = 3
modular = e % f

# **을 이용해서 변수 expo에 16을 넣는 수식을 작성해봅시다.
expo = 4 ** 2

#위의 세 변수를 출력해서 확인해봅시다.
print(intdiv)
print(modular)
print(expo)

print("*"*30)
#py_exam3.py

# 변수 connect_str를 선언하고, 연결 연산자를 이용해서 '덩덕쿵덕'를 넣어봅시다.
a = "덩덕"
b = "쿵덕"
connect_str = (a+b)

# 변수 iterate_str를 선언하고 반복 연산자를 이용해서 '쿵덕쿵덕'을 넣어봅시다.
c = "쿵덕"
iterate_str = 2*c


# 위 두 변수를 이용해서 '덩덕쿵덕/쿵덕쿵덕/덩덕쿵덕/쿵덕쿵덕'을 변수 jajinmori에 넣어봅시다
jajinmori = connect_str + iterate_str + connect_str + iterate_str


# 출력합니다.
print(connect_str,iterate_str,jajinmori)

print("*"*30)
#py_exam4.py

# 1. inch 단위의 자료를 입력 받아 cm를 구하시오.
# (1inch = 2.54cm)

num1 = float(input("inch를 입력하세요"))
num2 = num1 * 2.54

print(num2, "cm")

print("*"*30)
#py_exam5.py

# 2. 원의 반지름을 입력 받아 원의 둘레와 넓이를 구하는 코드입니다 (•둘레 : 2 * 원주율 * 반지름)
num1 = float(input("원의 반지름을 입력하세요"))
num2 = 2 * 3.14 * num1
print("원의 둘레는", num2)

num1 = float(input("원의 반지름을 입력하세요"))
num2 = num1 * num1 * 3.14
print("원의 넓이는", num2)

print("*"*30)
#py_exam6.py

# 다음 문자열에서 world 란 문자열이 있으면  True 를 , Kosmo100 없으면 True 를 반환 하도록 하시오.

str="Hello world"

print("world" in str) # 내용이 있으면 True or False
print("Kosmo100" not in str) # 내용이 없으면 True or False


print("*"*30)
# py_exam7.py

# 다음 변수  r 의 값을 지정한 형식으로 출력하시오.

r=8/3
#<result>
a = "{:.2f}".format(r)
#실수1: 2.67
print(a)
b = "{:.4f}".format(r)
#실수2: 2.6667
print(b)

print("*"*30)
# py_exam8.py
# 다음 문자열에서 ♡ 를 찾아서 다음과 같이 나오도록 출력하시오.
str = "Lobby news about the Hobby Lobby lawsuit. ♡ Get the latest releases, statements, and articles ♡about Hobby Lobby and their fight for religious freedom."
str1 = str.split("♡")
print(str1[2])
print(len(str1[2]))
comm = """
<result>
about Hobby Lobby and their fight for religious freedom.
문자열의 길이: 56
"""

print("*"*30)
#py_exam9.py
# 아래의 결과처럼 출력하시오.

import sys
print("name : ", sys.argv[1])
print("age : ", sys.argv[2])
print("height : ", sys.argv[3])

# index와 find의 차이를 각각 설명하시오.
"""
 find 같은 경우에는 찾는 문자나 문자열이 없을 경우에는 -1 을 return 하게 됩니다. 하지만 index 같은 경우에는 없을 경우에 오류를 발생
"""