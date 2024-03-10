import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M, R = map(int, input().split())
V = [i for i in range(1, N + 1)]
E = []
visited = [0] * (N + 1)
cnt = 0

for _ in range(M):
    y, x = map(int, input().split())
    E.append((y, x))

def dfs(v, e, r):
    global cnt
    cnt += 1
    visited[r] = cnt
    for i in v:
        if not visited[i] and (r, i) in e:
            dfs(v, e, i)

dfs(V, E, R)

for i in range(1, N + 1):
    print(visited[i])

##################################

def dfs(t):
    global cnt
    visited[t] = cnt
    line[t].sort()
    for i in line[t]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

N, M, R = map(int, input().split())
line = [[] for _ in range(N+1)]
visited = [0]*(N+1)  # 저장값
cnt = 1

for _ in range(M):
    a, b = map(int, input().split())
    line[a].append(b)  # 양 방향 간선
    line[b].append(a)  # 양 방향 간선

dfs(R)

for i in range(1, N+1):
    print(visited[i])


#########################

def dfs(t):
    global cnt
    visited[t] = cnt
    line[t].sort(reverse = True)
    for i in line[t]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

N, M, R = map(int, input().split())
line = [[] for _ in range(N+1)]
visited = [0] * (N+1)  # 저장값
cnt = 1           

for _ in range(M):
    a, b = map(int, input().split())
    line[a].append(b)  # 양 방향 간선
    line[b].append(a)  # 양 방향 간선

dfs(R)

for i in range(1, N+1):
    print(visited[i])