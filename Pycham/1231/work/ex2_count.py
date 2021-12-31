# data
str = "안녕 하세오 오늘은 파이썬 제어문 수업 입니다. 파이썬 파이썬"
print(str.count("파이썬"))
# print(str.count("ㅁㅁ"))  0개

searchWord = input("검색 단어")
if str.count(searchWord):
    print(searchWord, ":", str.count(searchWord))
else:
    print("해당 단어는 없음")