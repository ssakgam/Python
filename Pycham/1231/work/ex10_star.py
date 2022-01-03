num = int(input("1-아래로, 2-위로 :"))
lineNum = int(input("line Num => "))

printRange = range(1, lineNum+1)
if num == 2:
    printRange = range(lineNum, 0, -1)

for l in printRange:
    for n in range(1, l+1):
        print("*", end="")
    print()