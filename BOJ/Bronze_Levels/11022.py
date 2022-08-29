import sys
num = int(sys.stdin.readline())

for i in range(1, num+1):
    a, b = map(int, sys.stdin.readline().split(" "))
    print("Case #{0}: {1} + {2} = {3}".format(i, a, b, a+b))