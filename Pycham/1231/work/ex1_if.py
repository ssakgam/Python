# 파이썬은 블록 영역이 매우 중요하다.
# tab < 시스템 마다 차이가 날 수 있다.
# 스페이스4
"""

if 조건:
----실행문
----실행문
else:
----실행문
"""

# 입력을 받은 수가 홀수 인지 짝수 인지 출력 해봅시다.
# 조건 : n % 2 == 0    false/true
# 제어문 : if: else:
# 입력 : input()
num = int(input("정수를 입력하시오"))
if  num % 2 == 0:
    print(num, "짝수")
else :
    print(num, "홀수")
