# 연습문제
# 다음 날짜에서 월을 숫자로 반환 받아서 계절을 출력 합니다.
# 3 ~ 5 : 봄
# 6 ~ 8 : 여름
# 9 ~ 11 : 가을
# 12 ~ 2 : 겨울
# 날짜와 시간과 관련된 모듈
import datetime

now = datetime.datetime.now()
month = now.month
print(month)
print(now)

u_month = int(input("월 입력:"))
if u_month > 12 or u_month == 0:
    print("1부터 12사이의 숫자를 입력해주세요")
elif 3<= u_month <=5:
    print("봄")
elif 6<= u_month <=8:
    print("여름")
elif 9<= u_month <=11:
    print("가을")
elif u_month:
    print("겨울")
