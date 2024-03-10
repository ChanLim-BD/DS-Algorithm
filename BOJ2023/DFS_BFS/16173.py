import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
check = [[False] * N for _ in range(N)]

dy = [1, 0]
dx = [0, 1]

def dfs(y, x):
    check[y][x] = True
    if board[y][x] == -1:
        return
    for i in range(2):
        ny = y + board[y][x] * dy[i]
        nx = x + board[y][x] * dx[i]
        if 0 <= ny < N and 0 <= nx < N and check[ny][nx] == False:
            check[ny][nx] = True
            dfs(ny, nx)

dfs(0, 0)

if check[-1][-1] == True:
    print("HaruHaru")
else:
    print("Hing")