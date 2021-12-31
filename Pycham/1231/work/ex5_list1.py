# 리스트
# java -> Collection의 List
# 대괄호 내부에 자료를 넣어서 선언 한다.
# 리스트는 집합
# list는 여러 자료형으로 구성 될 수 있다.

array = [100, '100기', True, 3.14, "화이팅"]
print(array) #리스트 형식으로 나온다.

print(array[0])
# print(array[5]), 오류 : IndexError: list index out of range

# slicing
print(array[1:3])
# 변경도 가능하다
array[0] = "test"
print(array)
# 음수 -1, -2, -3 넣으면 뒤에서 부터 인덱스 번호 인식
print(array[-1])
print(type(array[-2])) # float , array[3]과 같다

# 리스트를 접근
print("리스트 접근 2 : ", end="") # end 이해 다시
print(array[0])
print("리스트 접근 이후 문자열 index 2 : ", end="")
print(array[0][0])
print("*"*30)
# 리스트 안에 요소들이 리스트일 경우
array2 = [[1,2,3],[4,5,6],[7,8,9]]
print(array2[0])
print(array2[0][1])

print("*"*30)
# 리스트 연산 + : 리스트와 리스트가 연결 연산 [1,2,3,4,5,6]
a = [1,2,3]
b = [4,5,6]
c = a + b
print("c => " ,c)

#  * 반복
d = [1,2,3]
f = d * 3
print("f => " ,f)

print(str(a[2]) + "hello")

# 리스트 연산, 인덱싱, 슬라이싱의 차이
# 슬라이싱
print("*"*30)
print(type(a[1:2])) # list
print(a[1:2]) # 리스트[start:end]  start~end-1 슬라이싱
a[1:2] = ["a","b","c"] # 두번째 요소에 삽입 => list의 인자값으로
print(a)

# 인덱싱
print("*"*30)
a = [1,2,3]
print(a[1:2])
print(a[1])
a[1] = ["a","b","c"] # 두번째 요소에 삽입 => 리스트 자체가 인자값으로
print(a)

# 리스트 삭제
# del => 변수 , 리스트, 튜플 등 class를 삭제 , del 을 쓰면 삭제된다.
"""
PyDev console: starting.
Python 3.8.10 (default, Nov 26 2021, 20:14:08) 
[GCC 9.3.0] on linux
a = 10
a
10
type(a)
<class 'int'>
del a
a
"""
print("*"*30)
a = [1,2,3]
print(len(a))
print(a)
# Class 자체를 삭제
#del a
#print(a)
# list 안에 인덱스에 해당하는 값을 삭제
del a[1]
print(len(a))
print(a) # [1,3]
print("*"*30)

a = [1,2,3]
a[1:3] = [] #[1]
print(a)
# 비워둔다.

# list에 새로운 요소를 추가하기 append()*****
a = [1,2,3]
a.append(5)  # 기본 **
print(len(a),":",a)
# a[1] = [6,7] => [1,[6,7],3]
a.append([6,7]) # => [1,2,3,5,[6,7]] **** 인자값으로
print(a)

# 정렬 *****
print("*"*30)
a = [5,4,3,2,1]
a.sort()
print(a) # 오름차순
a.reverse()
print(a) # 내림차순
print("*"*30)
a = ['a','b','c']
a.sort()
print(a)
a.reverse()
print(a)

# list1.extend(list2)
# list1에 list2를 + 와 같다
print("*"*30)
a = [1,2,3]
b = [4,5]
print(a + b) # [1, 2, 3, 4, 5]
a.extend(b)
print(a)
# extend 는 리스트만 가능하다.
a.extend([6])
print(a)

# extend 와 append의 차이를 한번 비교 해보자

#a.append([6,7]) # => [1,2,3,5,[6,7]] ****
# [1,2,3].extend([4,5] => [1,2,3,4,5]

a = [1,2,3]
a.append([4,5])
# a에 인자로써 들어간다. a = [1, 2, 3, [4, 5]] , a에 맨 마지막에 들어간다.
print(a)

a.extend([6,7])
# a에 값으로 들어간다. a = [1, 2, 3, [4, 5], 6, 7]
print(a)

print("*"*30)
a=[1,2,3,4,5]
result = 2 in a # a 리스트에 값 2가 포함되어 있는가?
print(result)

result = 7 not in a # a 리스트에 값 2가 포함되어 있지 않은가?
print(result)

# insert(index,value) : 데이터를 리스트에 삽입
# 인덱스의 위치가 존재하지 않을 때는 마지막 인덱스에 추가한다.
a=[1,2,3]
print(a)
a.insert(0,4) # 0번 인덱스 위치에 4를 입력
print(a) # [4,1,2,3]
a.insert(10, 10) # [4, 1, 2, 3, 10]
print(a)

# remove(value) // del과 차이 비교
a=[1,2,3,1,2,3]
# a 리스트에서 값이 첫번째 3인 요소 처음 나오는 값 1개를 제거(1개만)
a.remove(3) # 값으로 삭제
print(a) # [1, 2, 1, 2, 3]

# pop() 리스트의 마지막 요소를 꺼내고 반환하고 리스트에서 삭제( 오려내다 )
a=[1,2,3]
a.pop()
print(a) # [1, 2]
a.pop()
print(a) # [1]

# list count
a = [1,2,3,1,2,3]
b = a.count(2)
print("2 => ", b)

# => list 기초!!!!
