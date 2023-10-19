import sys
sys.setrecursionlimit(10**7)
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