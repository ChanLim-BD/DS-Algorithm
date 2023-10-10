# N, M, B = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(N)]

# std_min_cnt = 0
# std_max_cnt = 0

# for x in range(N):
#     std_min = min(graph[x])
#     std_max = max(graph[x])
#     std_max_cnt += graph[x].count(std_max)

# std_min_cnt = N * M - std_max_cnt
    
# # print(std_min, std_max, std_max_cnt, std_min_cnt)

# if std_min_cnt < std_max_cnt:
#     if min(std_max_cnt, std_min_cnt) <= B:
#         time = min(std_max_cnt, std_min_cnt) * 1
#         print(time, max(std_max, std_min))
#     else:
#         time = max(std_max_cnt, std_min_cnt) * 2
#         print(time, min(std_max, std_min))
# else:
#     time = min(std_max_cnt, std_min_cnt) * 2
#     print(time, min(std_max, std_min))

import sys
input = sys.stdin.readline

row, col, inventory = map(int, input().split())
blocks = []
for i in range(row):
    blocks += list(map(int, input().split()))

min_time = 500*500*2*257
ans_height = blocks[0]
blocks_out = sum(blocks)
for target_h in range(max(blocks), min(blocks) - 1, -1):
    if blocks_out + inventory >= target_h * row * col:
        time = 0
        for b in blocks:
            diff = b - target_h
            if diff > 0:
                time += diff * 2
            elif diff < 0:
                time -= diff * 1

        if time < min_time:
            min_time = time
            ans_height = target_h

print(min_time, ans_height)
