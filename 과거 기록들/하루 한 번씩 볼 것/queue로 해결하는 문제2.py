def solution(p):
    def update_block(start, panel):
        max_x, max_y = len(panel[0])-1, len(panel)-1
        queue = [start]
        while queue != []:
            x, y = queue.pop(0)
            if y != 0 and panel[y-1][x] == 0:
                queue.append([x, y-1])
            if y != max_y and panel[y+1][x] == 0:
                queue.append([x, y+1])
            if x != 0 and panel[y][x-1] == 0:
                queue.append([x-1, y])
            if x != max_x and panel[y][x+1] == 0:
                queue.append([x+1, y])
            panel[y][x] = 2
        return panel

    answer = 0
    for i in range(len(p)):
        for j in range(len(p[0])):
            if p[i][j] == 0:
                answer += 1
                p = update_block([j, i], p)
    return answer


map1 = [[0, 0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [1, 1, 0, 1, 1, 1],
        [0, 1, 0, 0, 1, 1],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 1],
        ]

print(solution(map1))
