def can_go(start, end, map_=None):
    arr = [start]
    while len(arr) != 0:
        # 1
        now_position = arr.pop(0)
        map_[now_position[0]][now_position[1]] = -1

        # 2                         (0, 0)
        arr = search_and_update1(now_position, map_, arr)
        if end in arr:
            return True
    return False


def get_distance(start, end, map_=None):
    arr = [start]
    distance = {tuple(start): 0}
    while len(arr) != 0:
        # 1
        now_position = arr.pop(0)
        map_[now_position[0]][now_position[1]] = -1

        # 2
        arr, distance = search_and_update2(now_position, map_, arr, distance)
        if end in arr:
            return distance[tuple(end)]
    return "cannot"

#                       (0, 0)  map1    []


def search_and_update1(now_pos, now_map, now_arr):
    h, w = len(now_map), len(now_map[0])  # 6, 5
    now_x, now_y = now_pos
    if now_map[max(now_x-1, 0)][now_y] == 0:
        now_arr.append([max(now_x-1, 0), now_y])
    if now_map[now_x][max(now_y-1, 0)] == 0:
        now_arr.append([now_x, max(now_y-1, 0)])
    if now_map[min(now_x+1, h-1)][now_y] == 0:
        now_arr.append([min(now_x+1, h-1), now_y])
    if now_map[now_x][min(now_y+1, w-1)] == 0:
        now_arr.append([now_x, min(now_y+1, w-1)])
    return now_arr


def search_and_update2(now_pos, now_map, now_arr, distance):
    h, w = len(now_map), len(now_map[0])
    now_x, now_y = now_pos
    print(now_x, now_y)
    if now_map[max(now_x-1, 0)][now_y] == 0:
        now_arr.append([max(now_x-1, 0), now_y])
        distance[(max(now_x-1, 0), now_y)] = distance[tuple(now_pos)]+1
    if now_map[now_x][max(now_y-1, 0)] == 0:
        now_arr.append([now_x, max(now_y-1, 0)])
        distance[(now_x, max(now_y-1, 0))] = distance[tuple(now_pos)]+1
    if now_map[min(now_x+1, h-1)][now_y] == 0:
        now_arr.append([min(now_x+1, h-1), now_y])
        distance[(min(now_x+1, h-1), now_y)] = distance[tuple(now_pos)]+1
    if now_map[now_x][min(now_y+1, w-1)] == 0:
        now_arr.append([now_x, min(now_y+1, w-1)])
        distance[(now_x, min(now_y+1, w-1))] = distance[tuple(now_pos)]+1
    return now_arr, distance


map1 = [[0, 1, 1, 1, 1],
        [0, 0, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0]]

map2 = [[0, 1, 1, 1, 1],
        [0, 0, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 1, 0, 0, 0]]

start, end = [0, 0], [5, 4]


def main():
    print(get_distance(start, end, map1))
    # print(can_go(start, end, map1))


if __name__ == '__main__':
    main()
