header = "파이썬의 format 함수에 대해서 알아보자"

comm = """      - for 문을 이용하여 페이지에서 요청할 때 사용
print("doc", num)
print("doc {}".format(num))
format() 함수로 숫자를 문자열로 변환
중괄호 포함한 문자열 뒤에 마침표 찍고 format() 함수 사용하되,
중괄호 개수와 format 함수  매개변수의 개수는 반드시 같아야 함 **** 지킵니다.
문자열의 중괄호 기호가 format() 함수 괄호 안의 매개변수로 차례로 대치되면서 숫자가 문자열이 됨


string_a = "{}".format(100)
print(string_a)
print(type(string_a))
"""

format_a = "kosmo{}기".format(100)
format_b = "파이썬 및 스프링 개발자의 연본 {} 입니다.".format(5000)
format_c = "{} / {} / {}".format(3000,5000,7000)
format_d = "{} / {} / {}".format(1,"파이썬",True)

print("format_a =>", format_a)
print("format_b =>", format_b)
print("format_c =>", format_c)
print("format_d =>", format_d)
print("*"*30)

# 이럴 때는 해당 인덱스만 출력을 한다. ******
print("{0}, {4}".format(1,2,3,4,5))
print("*"*30)

# 정수 - :d (중)
# 실수 - :f
#intNum = 100.2
#ValueError: Unknown format code 'd' for object of type 'float' - 즉 정수만 받겠다.
intNum = 100
output_a = "{:d}".format(100)
print(output_a)
print(type(output_a))
print("*"*30)

# :정수d  d 앞의 정수 칸수에서부터 <- 방향으로 칸에 맞춰 작성
oriput_b = "{}".format(intNum)
output_b = "{:5d}".format(intNum) # 5칸에 출력
output_c = "{:9d}".format(intNum)

print(oriput_b)
print(output_b)
print(output_c)

print("*"*30)
# 빈 칸을 0으로 채우기
outout_d = "{:05d}".format(52)
outout_e = "{:05d}".format(-52)
print(outout_d)
print(outout_e)
print(len(outout_d))    # 부호도 자리수를 차지한다.******
print(len(outout_d))
# <결과>
"""
00052
-0052 # 부호도 자리수를 차지 한다.
"""

# 기호와 함께 출력하기
# {:+id} 앞에 + 기호를 추가하면 양수의 경우 + 붙여줌
output_f = "{:+d}".format(52) # 양수
output_g = "{:+d}".format(-52) # 음수

print(output_f)
print(output_g)

print("*"*30)
# {: d} 앞에 공백을 두면 양수일 경우 기호 위치를 생략
output_h = "{: d}".format(52) # 양수 , 기호 생략
output_i = "{:+d}".format(-52) # 음수

print(output_h)
print(output_i)

# 자리수 만큼을 기호 밀기
output_h = "{:+5d}".format(52) # 양수 , 기호 생략
output_i = "{:+5d}".format(-52) # 음수

print(output_h)
print(output_i)

# 부호 사이를 띄우는데 그 총 칸수는 정수 만큼
output_j = "{:=+5d}".format(52) # 기호를 앞으로 밀기 : 양수
output_k = "{:=+5d}".format(-52) # 기호를 앞으로 밀기 : 음수
print(output_j)
print(output_k)

# 0 채우기 => 52 => 00052**
# 부호를 맨 앞으로 보내고 사이에 0 채우기
output_l = "{:=+05d}".format(52) # 기호를 앞으로 밀기 : 양수
output_m = "{:=+05d}".format(-52) # 기호를 앞으로 밀기 : 음수
print(output_l)
print(output_m)

# 한 번 해보기 위의 코드를 다음과 같이 나오도록 하시오.
"""
 0052
-0052
"""
output_n = "{:= 05d}".format(52) # 기호를 앞으로 밀기 : 양수
output_o = "{:=+05d}".format(-52) # 기호를 앞으로 밀기 : 음수
print(output_n)
print(output_o)

# format 안의 실수를 앞의 정부 부분 만큼의 칸 수에서 소숫점 자리 수 만큼 표현 해준다.

outp_a = "{:15.3f}".format(52.273)
outp_b = "{:15.2f}".format(52.273)
outp_c = "{:15.1f}".format(52.273)

print(outp_a)
print(outp_b)
print(outp_c)

# 의미 없는 소수점 제거 하기(즉, 끝의 숫자가 0이 오거나 아주 작은 숫자일 경우 제거되거나 올림된다.)

outpp_a = 52.000
outpp_b = "{:g}".format(outpp_a)
print(outpp_b)