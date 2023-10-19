N, M = map(int, input().split())            # 5, 3
balls = list(map(int, input().split()))     # 1 3 2 3 2
count = 0

for i in range(N-1):        # 0        1      2    3
    for j in range(i+1, N): # 1 2 3 4, 2 3 4, 3 4, 4
        if balls[i] == balls[j]:
            continue
        else:
            count += 1

print(count)

##############################

N, M = map(int, input().split())
balls = list(map(int, input().split()))

array = [0] * 11

for x in balls:
    array[x] += 1

# 각 무게에 해당하는 볼링공의 개수
print(array)          # [0, 1, 2, 1, 2, 2, 0, 0, 0, 0, 0]

result = 0
for i in range(1, M + 1): # 1, 2, 3, 4, 5
    N -= array[i]         # 7, 5, 4, 2, 0
    result += array[i] * N # 7, 17, 21, 25, 25

print(result)