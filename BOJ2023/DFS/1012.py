import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())
MAX = 50 + 10

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs(y, x):
    global graph # visited
    # visited[y][x] = True

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if graph[ny][nx]: #  and not visited[ny][nx]
            graph[ny][nx] = 0
            dfs(ny, nx)

while T > 0:
    T -= 1
    M, N, K = map(int, input().split())

    graph = [[0] * MAX for _ in range(MAX)]
    # visited = [[False] * MAX for _ in range(MAX)]
    
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y + 1][x + 1] = 1

    answer = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if graph[i][j]:
                dfs(i, j)
                answer += 1

    print(answer)