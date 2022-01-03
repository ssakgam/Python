# 56 ~, 튜플
"""
튜플(tuple) : 리스트와 비슷하지만
list => [] , tuple => ( )
tuple( ) 은 변경이 불가능 하다. 수정, 삭제가 안된다.
"""
print("*"*30)

mylist = []
print(type(mylist))

mylist = list()
print(type(mylist))

print("*"*30)
t1 = tuple()
print(type(t1))

mylist.append(1)
print(len(mylist))
print(mylist)
t1 = tuple(mylist)
# t1.append(1) x
print(type(t1))
print(t1)

# tuple 만들기 -> (1) => int 형식, (1,) => tuple , 자바에서 생성자 처럼 호출하는 방식이 특이, 데이터가 하나일때만 쉼표가 들어간다.
print("*"*10)
t1 = (1,)
print(t1)
print(type(t1))

# tuple 만들기 ->
print("*"*10)
t1 = (1,2,'a','b')
type(t1)
print(t1)
print(t1[1])
print(t1[0:2])
# t1[0] = 100 TypeError: 'tuple' object does not support item assignment 안된다.
tlist = list(t1) # 리스트로 변경
print(type(tlist))
tlist[0] = 100
t1 = tuple(tlist)
print(t1)

# tuple 연산
print("*"*10)
t1 = (1,2,'a','b')
t2 = (3,4)
t1 = t1 + t2
print(t1) # (1,2,'a','b',3,4)
print(t1 * 2) # (1, 2, 'a', 'b', 3, 4, 1, 2, 'a', 'b', 3, 4)
print(t1[1:]) # 슬라이싱
#----------------------------------------
# 튜플, 리스트 다중 반환 값 반환받기 ***
print("*"*10)

mylist = [1,2,3]
n1,n2,n3 = tuple(mylist)
print(n1,n2,n3)

# list vs tuple *****
list1 = [1]
print(list1)
tuple1 = (1,)
print(tuple1)
print('=>', tuple1[0])

# del tuple1[0] => tuple의 내부 내용은 수정 삭제 할 수 없어.

del tuple1
#print(tuple1)