가로 = 4
세로 = 5
캐릭터위치 = [0, 0]
장애물 = [[0, 1], [1, 1], [2, 3], [1, 3]]


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


make_map(가로, 세로, 캐릭터위치, 장애물)
