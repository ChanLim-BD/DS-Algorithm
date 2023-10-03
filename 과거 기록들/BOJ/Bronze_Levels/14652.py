import sys

N, M, K = map(int, sys.stdin.readline().split())

m = K % M
n = K//M

print(n, m)
