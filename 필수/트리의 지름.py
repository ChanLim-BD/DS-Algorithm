"""
12
1 2 3
1 3 2
2 4 5
3 5 11
3 6 9
4 7 1
4 8 7
5 9 15
5 10 4
6 11 6
6 12 10
"""

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n = int(input())
graph = [[] for _ in range(n + 1)]

def dfs(x, wei):
    for i in graph[x]:
        a, b = i
        if distance[a] == -1:
            distance[a] = wei + b
            dfs(a, wei + b)

# 트리 구현
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

# 1번 노드에서 가장 먼 곳을 찾는다.
distance = [-1] * (n + 1)
distance[1] = 0
dfs(1, 0)

# 위에서 찾은 노드에 대한 가장 먼 노드를 찾는다.
start = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[start] = 0
dfs(start, 0)

print(max(distance))

############################################
############################################

# BFS
from collections import deque

max_node = -1

def bfs(start_node):
    global n, max_node
    visited = [False]*(n+1)
    q = deque()
    q.append([start_node, 0])
    visited[start_node] = True
    max_dist = 0

    while q:
        now, now_dist = q.popleft()
        for child, child_dist in graph[now]:
            if not visited[child]:
                visited[child] = True
                q.append([child, now_dist + child_dist])
                if max_dist < now_dist + child_dist:
                    max_dist = now_dist + child_dist
                    max_node = child
    return max_dist
                
n = int(input())

if n == 1:
    print(0)
else:
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        # 부모, 자식, 거리
        a,b,c = map(int,input().split())
        graph[a].append([b,c])
        graph[b].append([a,c])

    bfs(1)
    print(max_node)
    print(bfs(max_node))