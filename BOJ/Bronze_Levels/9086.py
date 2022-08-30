import sys

num = int(sys.stdin.readline())

for i in range(num):
    str = input()
    print(str[0]+str[len(str)-1])
