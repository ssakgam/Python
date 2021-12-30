# ex1_input
comm = """
input() 명령어 프롬프트에서 사용자로 부터 데이터를 입력 받을 때 사용한다.
java => Scanner, BufferedReader
블로킹함수, 블로킹 메소드 - 쓰레드 처리
"""

#print(type(input("메세지를 입력하세요.")))


# 기본 반환값은 str이다.
#msg = input("메세지를 입력하세요.")
#print(msg)

# int() 숫자로 변경
number = int(input("숫자를 입력 :"))
number = number + 10
print(number)

# 연습문제)
# 두 수를 입력을 받아서 사칙연산의 결과를 출력하시오.
# 단) 입력값은 실수로 받아서 연산하시오.

num1 = float(input("실수 a 입력 :"))
num2 = float(input("실수 b 입력 :"))

print("덧셈결과 ", (num1 + num2))
print("뺄셈결과 ", (num1 - num2))
print("곱셈결과 ", (num1 * num2))
print("나눗셈결과 ", (num1 / num2))