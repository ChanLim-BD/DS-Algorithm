import sys

N, K = map(int, sys.stdin.readline().split())

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    K = K + a - b

K -= K

if K == 0:
    print("비와이")
