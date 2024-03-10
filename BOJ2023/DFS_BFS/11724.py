import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[False] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)
answer = 0

for _ in range(M):
    u, v = map(int, input().split())
    graph[u][v] = True
    graph[v][u] = True

def dfs(idx):
    global visited, graph
    visited[idx] = True
    
    for i in range(1, N + 1):
        if not visited[i] and graph[idx][i] == True:
            dfs(i)
    return 1
    
for i in range(1, N + 1):
    if visited[i] == False:
        answer += dfs(i)

print(answer)

############################################

n, m = map(int, input().split())
graph = [[] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = 0 

def bfs(x):
    global graph, visited
    q = deque(graph[x])
    visited[x] = True

    while q:
        node = q.popleft()
        for i in graph[node]:
            if visited[i] == False:
                visited[i] = True
                q.append(i)
                
for i in range(1, n+1):
    if visited[i] == False:
        bfs(i)
        answer += 1

print(answer)