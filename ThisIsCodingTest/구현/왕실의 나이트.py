locate = input()
x = int(locate[1])
y = ord(locate[0]) - ord('a') + 1

# print(N, M)
result = 0

move_types = [(2, 1), (2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2), (-2, 1), (-2, -1)]

for move in move_types:
    dy = move[0]
    dx = move[1]

    ny = y + dy
    nx = x + dx

    if ny >= 1 and nx >= 1 and ny <= 8 and nx <= 8:
        result += 1

print(result)