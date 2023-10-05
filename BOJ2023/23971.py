from math import ceil

H, W, N, M = map(int, input().split())
rows = ceil(H / (N + 1))
cols = ceil(W / (M + 1))
print(rows * cols)