import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def recur(y, x):

    if dp[y][x] != 0:
        return dp[y][x]

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if graph[y][x] < graph[ny][nx]:
                dp[y][x] = max(dp[y][x], recur(ny, nx) + 1)

    return dp[y][x]

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

for y in range(n):
    for x in range(n):
        recur(y, x)

print(max(map(max, dp)) + 1)