import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
board = []
locate = []

for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(n):
        if board[i][j] != 0:
            locate.append((board[i][j], 0, i, j))

locate.sort()

target_s, target_x, target_y = map(int, input().split())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(locate):
    q = deque(locate)
    while q:
        virus, s, x, y = q.popleft()
        if s == target_s:
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 0:
                    board[nx][ny] = virus
                    q.append((virus, s+1, nx, ny))

bfs(locate)

print(board[target_x-1][target_y-1])