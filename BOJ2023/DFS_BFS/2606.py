import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
# 인접 행렬 ver.

# N = int(input())
# M = int(input())

# graph = [[False] * (N + 1) for _ in range(N + 1)]
# visited = [0] * (N + 1)
# answer = 0

# for _ in range(M):
#     y, x = map(int, input().split())
#     graph[y][x] = True
#     graph[x][y] = True


# def dfs(idx):
#     global visited, graph, answer
#     visited[idx] = True
#     answer += 1

#     for i in range(1, N + 1):
#         if not visited[i] and graph[idx][i] == True:
#             dfs(i)

# dfs(1)

# print(answer - 1)

# ######################################
# # 인접 리스트 ver.

# n = int(input())
# m = int(input())
# graph = [[] * (n + 1) for _ in range(n + 1)]
# visited = [False] * (n + 1)

# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# answer = 0 

# def dfs(x):
#     global graph, visited, answer
#     visited[x] = True
#     answer += 1

#     for i in graph[x]:
#         if not visited[i]:
#             dfs(i)
# dfs(1)
# print(visited)
# print(answer - 1)

######################################
### BFS

import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = 0 

def bfs(graph, visited, x):
    global answer
    q = deque(graph[x])
    visited[x] = True

    while q:
        node = q.popleft()
        for i in graph[node]:
            if visited[i] == False:
                visited[i] = True
                q.append(i)
                answer += 1
                
bfs(graph, visited, 1)

print(answer)