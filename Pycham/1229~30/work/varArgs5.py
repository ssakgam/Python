import sys
import os

# 리눅스 ls 명령어랑 동일하다.
# print(os.listdir())
print("*"*10)
print(sys.argv)
print(type(sys.argv))

#python3 varArgs5.py test hello
print("FileName :",sys.argv[0])
print("Arg1 :",sys.argv[1])
print("Arg2 :",sys.argv[2])

