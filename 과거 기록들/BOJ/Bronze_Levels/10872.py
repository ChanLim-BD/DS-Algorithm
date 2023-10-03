import sys

num = int(sys.stdin.readline())
val = 1

for i in range(1, num+1):
    val *= i

print(val)
