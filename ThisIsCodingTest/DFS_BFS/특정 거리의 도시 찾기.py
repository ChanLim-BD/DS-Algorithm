import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] * (n + 1) for _ in range(n + 1)]
result = [-1] * (n + 1)
result[x] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

print(graph)

def bfs(graph, result, x):
    q = deque([x])
    while q:
        now = q.popleft()
        for next_node in graph[now]:
            if result[next_node] == -1:
                result[next_node] = result[now] + 1
                q.append(next_node)

bfs(graph, result, x)

print(result)

check = False
for i in range(1, n + 1):
    if result[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)