import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
graph = [[] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(1, n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (n + 1)

def dfs(idx):
    visited[idx] = True
    for i in graph[idx]:
        if not visited[i]:
            parent[i] = idx
            dfs(i)

dfs(1)

for i in range(2, len(parent)):
    print(parent[i])