import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
target = list(map(int, input().split()))
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
result = [0] * (n + 1)

for _ in range(m):
    y, x = map(int, input().split())
    graph[y].append(x)
    graph[x].append(y)

def dfs(t):
    visited[t] = 1
    for i in graph[t]:
        if not visited[i]:
            result[i] = result[t] + 1
            dfs(i)

dfs(target[0])

print(result)

if result[target[1]] > 0:
    print(result[target[1]])
else:
    print(-1)

"""
9
7 3
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6
"""