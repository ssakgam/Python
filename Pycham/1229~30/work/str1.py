# """ \의 의미는 줄을 바꿔서 출력하지 않겠다 라고 선언 하는 것과 동
msg = """\
1. 동해물과 백두산이 마르고 닳도록                                                  
하느님이 보우하사 우리나라 만세                                                     
무궁화 삼천리 화려강산                                                          
대한 사람 대한으로 길이 보전하세\
"""
print("문자열의 length : ", len(msg))
print("*"* 30)
print(msg)
print("*"* 30)

# 문자열 연결 연산자 + "문자열" + "문자열"
print("안녕"+"하세요")
print("안녕하세요"+"!")

# ** 문자열과 숫자 사이에는 사용할 수 없다.
# System.out.println("hello"+10);
# System.out.println(10); #-> String.valueof()
# 문자열은 문자끼리, 숫자는 숫자끼리 연결
# 문자열과 숫자 연결해서 연산 하려면 큰 따옴표를 붙여서 문자로 인식시키던지
# str() 문자 타입으로 변환
#print("안녕"+100) type 오류
print("안녕"+str(100))
print(10,20,30)

# 문자열 반복 연산자. => 문자열을 숫자와 * 연산자로 연결 한다.
print("하이"*10)
print(10*"하이")

