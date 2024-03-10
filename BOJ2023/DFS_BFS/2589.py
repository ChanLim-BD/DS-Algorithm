import sys
from collections import deque
input = sys.stdin.readline

Y, X = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(Y)]

maxi = 0

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

visited = [[False for _ in range(X)] for _ in range(Y)]
dist = [[0 for _ in range(X)] for _ in range(Y)]

def bfs(y, x):
    global maxi
    # BFS
    q = deque()
    q.append([y, x])
    visited[y][x] = 1

    while q:
        ey, ex = q.popleft()

        # 4방향 탐색
        for i in range(4):
            ny, nx = ey + dy[i], ex + dx[i]
            if 0 <= ny < Y and 0 <= nx < X and graph[ny][nx] == 'L'and visited[ny][nx] == False:
                visited[ny][nx] = True
                dist[ny][nx] = dist[ey][ex] + 1
                maxi = max(maxi, dist[ny][nx])
                q.append([ny, nx])

for y in range(Y):
    for x in range(X):
        if graph[y][x] == 'L':
            bfs(y, x)

print(maxi)

"""
5 7
WLLWWWL
LLLWLLL
LWLWLWW
LWLWLLL
WLLWLWW
"""