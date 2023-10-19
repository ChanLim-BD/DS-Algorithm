N = int(input())
M = int(input())

graph = [[False] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)
answer = 0

for _ in range(M):
    y, x = map(int, input().split())
    graph[y][x] = True
    graph[x][y] = True


def dfs(idx):
    global visited, graph, answer
    visited[idx] = True
    answer += 1

    for i in range(1, N + 1):
        if not visited[i] and graph[idx][i] == True:
            dfs(i)

dfs(1)

print(answer - 1)