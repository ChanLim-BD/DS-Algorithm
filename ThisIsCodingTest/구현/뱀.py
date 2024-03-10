import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
graph =[[0] * (n + 1) for _ in range(n + 1)] # 맵 정보
info = [] # 방향 회전 정보

# 맵 정보(사과 있는 곳은 1로 표시)
for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1

# 방향 회전 정보 입력
l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

# 처음에는 오른쪽을 보고 있으므로(동, 남, 서, 북)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    y, x = 1, 1 # 뱀의 머리 위치
    graph[y][x] = 2 # 뱀이 존재하는 위치는 2로 표시
    direction = 0 # 처음에는 동쪽을 보고 있음
    time = 0 # 시작한 뒤에 지난 '초' 시간
    index = 0 # 다음에 회전할 정보
    q = [(y, x)] # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)

    while True:
        ny = y + dy[direction]
        nx = x + dx[direction]
        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and graph[ny][nx] != 2:
            # 사과가 없다면 이동 후에 꼬리 제거
            if graph[ny][nx] == 0:
                graph[ny][nx] = 2
                q.append((ny, nx))
                py, px = q.pop(0)
                graph[py][px] = 0
            # 사과가 있다면 이동 후에 꼬리 그대로 두기
            if graph[ny][nx] == 1:
                graph[ny][nx] = 2
                q.append((ny, nx))
        # 벽이나 뱀의 몸통과 부딪혔다면
        else:
            time += 1
            break
        y, x = ny, nx # 다음 위치로 머리를 이동
        time += 1
        if index < l and time == info[index][0]: # 회전할 시간인 경우 회전
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(graph)
print(simulate())