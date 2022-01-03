# range() : 특정 횟수 만큼 반복자를 반환
# for 문의 조건식에 많이 사용
#  자바 => for( 초기식 : 조건식 : 증감식 )
# for(String e : arr) => :는 in의 뜻
# for i in range(1, 10) :
print(range(1, 10))

# range( 초기식, 조건값-1, step)
print(list(range(1,10))) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1,10,2)))
# range 의 조건값에 매개변수로 나눗셈을 사용할 경우 오류가 발생한다.(integer여야 하니까 float나올 수 도 있어서)
#print(list(range(1,10/2))) 이건 안돼!

print(list(range(1,int(10/2)))) #이건된다
print(list(range(1,10//2)))
# for 숫자변수 in 범위 :
#   실행코드

for i in range(6):
    print(str(1)+"=반복변수")
print()
print("*"*30)
for i in range(5,10):
    print(str(i)+",",end="")
print()
for i in range(0,10,3):
    print(str(i) + "= 반복변수")
print()


