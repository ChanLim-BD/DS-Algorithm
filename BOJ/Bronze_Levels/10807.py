import sys

num = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
num2 = int(sys.stdin.readline())

print(data.count(num2))
