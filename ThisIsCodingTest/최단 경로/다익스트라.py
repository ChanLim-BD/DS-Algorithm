import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)  # 10억 설정

# 노드의 개수, 간선의 개수
N, M = map(int, input().split()) 
# 시작 노드 번호
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for _ in range(N + 1)]
# 최단 거리 테이블
distance = [INF] * (N + 1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 비용을 앞에, 지점은 뒤에
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, N+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
