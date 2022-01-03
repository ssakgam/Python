# https://cafe.naver.com/kosmo100/71

num = int(input("단을 입력하세요 : "))
inputRange = int(input("범위를 입력하세요 : [3,5,7,9]"))
if inputRange not in [3, 5, 7, 9] :
    print("범위는 3,5,7,9 중에 하나를 선택하세요")
    raise SystemExit
for y in range(0, 10):
    for x in range(num - inputRange // 2, num + inputRange // 2+1):
        if y == 0:
            print("=={}단==".format(x), end= " ")
        else:
            str = "{:d}x{:d}={:02d}".format(x, y, y*x)
            result = "{:7s}".format(str)
            print(result, end=" ")
    print()
