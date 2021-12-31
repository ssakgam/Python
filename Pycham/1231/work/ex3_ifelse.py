if True:
    print("실행")
else:
    print("")

# python 에서는 0 은 False 와 같다. 따라서 else의 실행구문이 실행 된다.
num = 0
if num:
    print("실행1")
else:
    print("실행2")

# if: elif: else:

num = 0
if num == 0:
    print("0")
elif num == 1:
    print("1")
elif num == 2:
    print("2")
else:
    print("0, 1 이 아닌 수 => ", num)

