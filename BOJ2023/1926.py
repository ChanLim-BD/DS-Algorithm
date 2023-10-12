from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

count = 0
maxv = 0

def bfs(y, x):
    queue = deque()
    visited[y][x] = True
    queue.append((y, x))
    square = 1

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if graph[ny][nx] == 1 and visited[ny][nx] == False:
                    square += 1
                    visited[ny][nx] = True
                    queue.append((ny, nx))
    return square
        
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and visited[i][j] == False:
            count += 1
            maxv = max(maxv, bfs(i, j))

print(count)
print(maxv)