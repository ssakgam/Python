# 48 ~, 리스트 : 수치 연산을 할 때 해당 데이터를 리스트로 만들고 벡터화 한다.
# 여러 자료들을 모아서 자바에서 배열도 있지만, ArrayList, collection 같은 역할

# 56 ~, 튜플
# 58 ~, 세트
# 63 ~, 딕셔너리

## Join 함수(동작)******* (기억해야할 함수 : split, join)
### Join 함수를 사용해서 문자열(sequnce 계열), 리스트, 튜플에 값을 구분자를 기준으로
#### 문자열로 반환 해주는 함수이다.
a = ","
mlist = ['a','b','c','d','e']
print(type(mlist))
print(mlist)

#문자열
res = a.join("abcdefg")
print(res)

# 리스트
res = a.join(mlist)
print(res)
print(",".join("abcdefg"))