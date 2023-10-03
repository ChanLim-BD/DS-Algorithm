가로 = 4
세로 = 5
캐릭터위치 = [0, 0]
장애물 = [[0, 1], [1, 1], [2, 3], [1, 3]]
움직임 = [2, 2, 2, 4, 4, 4]


def make_map(n, m, char, obj):
    world_map = [[0]*(n+2) for i in range(m+2)]

    for i in range(len(world_map)):
        for j in range(len(world_map[0])):
            if i == 0 or j == len(world_map[0])-1 or j == 0 or i == len(world_map)-1:
                world_map[i][j] = 2

    world_map[char[0]+1][char[1]+1] = 1
    for i in obj:
        if world_map[i[0]+1][i[1]+1] != 1:
            world_map[i[0]+1][i[1]+1] = 2
    for i in world_map:
        print(i)
    return world_map


def move(world_map, moving):
    x, y = 0, 0
    for i, m in enumerate(world_map):
        # print(i, m)
        if 1 in m:
            x, y = m.index(1), i
    # print(x, y)

    world_map[y][x] = 0

    for i in moving:
        if i == 1 and world_map[y-1][x] != 2:
            y -= 1
        elif i == 2 and world_map[y+1][x] != 2:
            y += 1
        elif i == 3 and world_map[y][x-1] != 2:
            x -= 1
        elif i == 4 and world_map[y][x+1] != 2:
            x += 1

    world_map[y][x] = 1
    for i in world_map:
        print(i)
    return [x, y]


지도 = make_map(가로, 세로, 캐릭터위치, 장애물)
print()
move(지도, 움직임)
