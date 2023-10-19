import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dy = [0, 1, 0, -1, 1, 1, -1, -1]
dx = [1, 0, -1, 0, 1, -1, 1, -1]

def dfs(y, x):
    global graph
    graph[y][x] = 0
    for i in range(len(dy)):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < h and 0 <= nx < w and graph[ny][nx] == 1:
            graph[ny][nx] = 0
            dfs(ny, nx)

while True:
    answer = 0
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i, j)
                answer += 1
    print(answer)