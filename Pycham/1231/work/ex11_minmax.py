import random

num = int(input("지정한 수 입력 => "))

numList = []
for i in range(1,num):
	n = random.randint(0,100)
	numList.append(n)

print(numList)

numList.sort()
print("max1 = >", numList[-1])
print("max2 = >", max(numList))
print("min1 = >", numList[0])
print("min2 = >", min(numList))