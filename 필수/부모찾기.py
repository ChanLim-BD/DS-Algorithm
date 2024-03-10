"""
7
1 6
6 3
3 5
4 1
2 4
4 7
"""


N = int(input())

graph = [[] for _ in range(N + 1)]
par = [0 for _ in range(N + 1)]
child = [0 for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def recur(node, prv):

    par[node] = prv 

    for nxt in graph[node]:
        if nxt == prv:
            continue
        recur(nxt, node)

    child[prv] += 1

recur(1, 0)

print(par)
print(child)