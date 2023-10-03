import sys
input = sys.stdin.readline

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def dfs(x, y):
    for i in range(len(dy)):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < M) and (0 <= ny < N):
            if graph[ny][nx] == 1:
                graph[ny][nx] = -1
                dfs(nx, ny)

T = int(input())

for i in range(T):
    M, N, K = map(int, input().split())  # M:가로, N:세로, K:개수
    graph = [[0] * M for _ in range(N)]
    cnt = 0

    # 배추 위치에 1 표시
    for j in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1

    for x in range(M):
        for y in range(N):
            if graph[y][x] == 1:
                dfs(x,y)
                cnt += 1
    
    print(cnt)