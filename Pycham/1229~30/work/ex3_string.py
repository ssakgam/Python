# 교재참조 : 158 ~ 173 페이지
# upper() => 대문자로 변경, lower() => 소문자

a = "Hello Python Test...!"
print(a.upper())
print(a.lower())

msg = """
1. 동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려 강산
대한 사람 대한으로 길이 보전하세\
"""

print(len(msg))
# strip() : 문자열의 좌우 공백을 제거한다. ***
# 다른 strip() 함수로 출력 해보기
# select trim(saname) sname from sawon;
# => ' 김길동 ' lstrip : 왼쪽 공백 제거, rstrip : 오른쪽 공백 제거

msg2 = """
1. 동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려 강산
대한 사람 대한으로 길이 보전하세
"""

print(len(msg2.strip()))
print("*"*30)

"""
문자열이 소문자로만 알파벳으로만, 혹은 숫자로만 구성되어 있는지 확인 하는 메소드
"""
# isalnum() : 문자열이 문자 또는 숫자로만 구성되어있는지
# isalpha() : 문자열이 문자로만 구성되어 있는지
# isidentifier() : 문자열이 식별자로 사용할 수 있는 것인지
# isdecimal() : 문자열이 정수 형태인지
# isdigit() : 문자열이 숫자로 인식 될 수 있는지
# isspace() : 문자열이 공백으로만 구성 되어 있는지
# islower() : 문자열이 소문자로만 구성되어 있는지
# isupper() : 문자열이 대문자로만 구성되어 있는지
print("Kosmo100하".isalnum())
print("gkgk하100".isalpha())

# 숫자 확인 하기
# isdigit()

# find()******
# 첫번째 index 를 반환, 만약 해당 단어를 찾지 못하면 -1 반환 (int 형태)
# java -> String 클래스에서 : indexOf()
# index()
# 함수 뒤의 첫번째 같은 단어의 index를 반환, 해당 단어를 찾지 못하면 error
print("*"*30)
msg = "안녕하세요 안녕kosmo100기 입니다".find("안녕")
print(msg)

# 오류가 나면 try catch 로 처리 하세요
msg = "하세요 안녕kosmo100기 입니다".index("안녕")
print(msg)

print("*"*30)
msg = "안녕하세요 안녕kosmo100기".rfind("안녕")
print(msg)
# rindex, rfind는 가장 오른쪽에서 같은 문자가 나오는 index 번호
msg = "안녕하세요 안녕kosmo안녕100기".rindex("안녕")
print(msg)

# In 연산자
# - 문자열 내부에 어떤 문자열이 있는지 확인 할 때 사용함******* ture or false로 리턴함
print("안녕" in "안녕하세요")
print("잘가" in "안녕하세요")

# split() 함수
# 문자열을 특정한 문자로 잘라서 list로 반환한다.
# 자바에서 split , StringTokenizer 사용되는데  split은 없는 곳은 길이가 없는 문자열 처리, stz는 아예 삭제
print("*"*30)
msg = "10 20 30 40 50"
print(type(msg.split()))
msg = "10/20/30/40/50"
print((msg.split("/")))


