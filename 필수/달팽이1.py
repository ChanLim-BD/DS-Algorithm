N = 3
board = [[0] * N for _ in range(N)]
trans = 1
cnt = 1
y, x = 0, -1

sel = True

if sel:
    while N > 0:
        for i in range(N):
            x += trans
            board[y][x] = cnt
            cnt += 1

        N -= 1

        for i in range(N):
            y += trans
            board[y][x] = cnt
            cnt += 1

        trans *= -1
else:
    y, x = -1, 0
    while N > 0:
        for i in range(N):
            y += trans
            board[y][x] = cnt
            cnt += 1
        
        N -= 1

        for i in range(N):
            x += trans
            board[y][x] = cnt
            cnt += 1

        trans *= -1

print(board)