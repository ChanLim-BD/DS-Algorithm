import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
edge = [[] for _ in range(V+1)]
chk = [False] * (V+1)
rs = 0

for i in range(E):
    a, b, c = map(int, input().split())
    edge[a].append([c,b])
    edge[b].append([c,a])

print(edge)

heap = [[0, 1]]

while heap:
    w, eachNode = heapq.heappop(heap)
    if chk[eachNode] == False:
        chk[eachNode] = True
        rs += w
        for nextEdge in edge[eachNode]:
            if chk[nextEdge[1]] == False:
                heapq.heappush(heap, nextEdge)

print(rs)