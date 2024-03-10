import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def recur(y, x):

    if y == Y-1 and x == X - 1:
        return 1
    
    if dp[y][x] != -1:
        return dp[y][x]

    route = 0
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]

        if 0 <= ny < Y and 0 <= nx < X:
            if graph[y][x] > graph[ny][nx]:
                route += recur(ny, nx)
    dp[y][x] = route
    return dp[y][x]

Y, X = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(Y)]
dp = [[-1] * X for _ in range(Y)]
print(recur(0, 0))