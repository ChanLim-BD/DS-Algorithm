import sys
sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]
answer = 0

dy = [-1, 1]
dx = [-1, 1]

def dfs(y, x):
    global board, check, answer
    if board[y][x] == '-':
        board[y][x] = 'c'
        for i in range(len(dx)):
            nx = x + dx[i]
            if 0 <= nx < M and board[y][nx] == '-':
                dfs(y, nx)
                board[y][nx] = 'c' 
    else:
        board[y][x] = 'c'
        for i in range(len(dy)):
            ny = y + dy[i]
            if 0 <= ny < N and board[ny][x] == '|':
                dfs(ny, x)
                board[ny][x] = 'c'

for i in range(N):
    for j in range(M):
        if board[i][j] == '-' or board[i][j] == '|':
            dfs(i, j)
            answer += 1
        
print(answer)