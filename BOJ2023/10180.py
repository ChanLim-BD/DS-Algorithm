import sys
input = sys.stdin.readline

n, m = map(int, input().split())
basket = [0 for _ in range(n)]

for _ in range(m):
    i, j, k = map(int, input().split())
    for x in range(i - 1, j):
        basket[x] = k

print(*basket)