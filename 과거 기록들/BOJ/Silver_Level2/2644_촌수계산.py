import sys
input = sys.stdin.readline

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            result[i] = result[v] + 1
            dfs(i)

N = int(input())
a, b = map(int, input().split())
M = int(input())

graph = [[] for _ in range(N+1)]
visited = [False] * (N + 1)
result = [0] * (N+1)


for _ in range(M):
    x, y = map(int, input().split())  
    graph[x].append(y)
    graph[y].append(x)

dfs(a)

if result[b] > 0:
    print(result[b])
else:
    print(-1)
