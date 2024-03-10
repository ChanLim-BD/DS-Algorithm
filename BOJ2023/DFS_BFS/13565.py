import sys
sys.setrecursionlimit(10**6)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs(y, x):
    global graph
    graph[y][x] = '2'
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < M and 0 <= nx < N and graph[ny][nx] == '0':
            graph[ny][nx] = '2'
            dfs(ny, nx)

M, N = map(int, input().split())
graph = [list(input()) for _ in range(M)]
# print(graph)

for i in range(N):
    if graph[0][i] == '0':
        dfs(0, i)

# for g in graph:
#     print(g)

if '2' in ''.join(graph[M - 1]) :
    print("YES")
else:
    print("NO")


###################################################################

from collections import deque

def bfs(y, x):
    global graph
    q = deque()
    q.append((y, x))
    graph[y][x] = '2'
    
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < M and 0 <= nx < N and graph[ny][nx] == '0':
                q.append((ny, nx))
                graph[ny][nx] = '2'
    
M, N = map(int, input().split())
graph = [list(input()) for _ in range(M)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

for i in range(N):
    if graph[0][i] == '0':
        bfs(0, i)

for g in graph:
    print(g)

print('YES' if '2' in graph[-1] else "NO")