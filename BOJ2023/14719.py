# H, W = map(int, input().split())
# land = list(map(int, input().split()))

# dp = [0] * W

# std = land.index(max(land))

# for i in range(1, std):
#     dp[i] = land[0] - land[i]

# for j in range(W - 1, std, -1):
#     dp[j] = land[-1] - land[j]

# print(dp, std)

# print(sum(dp))
################################################


H, W = map(int, input().split())
land = list(map(int, input().split()))

result = 0

for i in range(1, W - 1):           # 양 끝 수는 제외.
    # print(i)
    left_max = max(land[ :i])       
    right_max = max(land[i+1: ])

    lower = min(left_max, right_max)

    if land[i] < lower:
        result += lower - land[i]
        
print(result)