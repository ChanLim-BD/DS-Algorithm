n = int(input())
y, x = 1, 1
plans = input().split()

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

'''[
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(1, 0), (1, 1), (1, 2), (1, 3)],
    [(2, 0), (2, 1), (2, 2), (2, 3)],
    [(3, 0), (3, 1), (3, 2), (3, 3)],
]
'''
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            ny = y + dy[i]
            nx = x + dx[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    y, x = ny, nx

print(y, x)