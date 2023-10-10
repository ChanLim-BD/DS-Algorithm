N, M = map(int, input().split())
y, x, direction = map(int, input().split())
dp = [[0] * M for _ in range(N)] # 방문 여부
graph = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 0, 1, 0] # 북 서 남 동
dx = [0, -1, 0, 1]

def turn_left():
    global direction
    direction += 1
    if direction == 4:
        direction = 0

count = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if graph[ny][nx] == 0 and dp[ny][nx] == 0:
        dp[ny][nx] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if dp[ny][nx] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)