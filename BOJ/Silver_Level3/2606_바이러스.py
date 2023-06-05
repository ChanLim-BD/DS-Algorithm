import sys
input = sys.stdin.readline

N = int(input())
Pair = int(input())
Network = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(Pair):
    a, b = map(int, input().split())
    Network[a][b] = 1
    Network[b][a] = 1

visited = [0] * (N + 1)

def dfs(v):
    visited[v] = 1
    for i in range(1, N + 1):
        if not visited[i] and Network[v][i]:
            dfs(i)

dfs(1)

print(sum(visited) - 1)