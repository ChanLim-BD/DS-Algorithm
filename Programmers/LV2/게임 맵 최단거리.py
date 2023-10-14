from collections import deque

def solution(maps):
    answer = 0

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    def bfs(y, x):
        q = deque()
        q.append((y, x))

        while q:
            y, x = q.popleft()
            for i in range(len(maps)):
                print(maps[i])
            for i in range(4): 
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or nx < 0 or ny >= len(maps) or nx >= len(maps[0]):
                    continue

                if maps[ny][nx] == 0:
                    continue

                if maps[ny][nx] == 1:
                    maps[ny][nx] = maps[y][x] + 1
                    q.append((ny, nx))

        return maps[len(maps) - 1][len(maps[0]) -1]
    answer = bfs(0, 0)

    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))