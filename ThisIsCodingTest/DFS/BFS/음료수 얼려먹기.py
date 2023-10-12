N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

print(graph)
'''
방문여부 리스트가 없는 이유는 
그래프 내에 바로 체크해야하기 때문에 따로 만들 이유가 없음.

아이디어는 알겠는데, 구현하는 데 머리가 멍해진다.
'''

def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

result = 0

for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1


print(result)

