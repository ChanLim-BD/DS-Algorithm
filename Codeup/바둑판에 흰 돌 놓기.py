graph = [[0] * 19 for _ in range(19)]
n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

for gr in graph:
    for g in gr:
        print(g, end=' ')
    print()