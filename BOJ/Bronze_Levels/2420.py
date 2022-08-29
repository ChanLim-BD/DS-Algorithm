import sys
n1, n2 = map(int, sys.stdin.readline().split())

if n1 > n2:
    print(abs(n1 - n2))
elif n1 < n2:
    print(abs(n2 - n1))
