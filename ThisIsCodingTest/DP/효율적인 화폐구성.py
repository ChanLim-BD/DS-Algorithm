N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

dp = [10001] * (M + 1)

# print(lst)
dp[0] = 0
for i in range(N):
    for j in range(lst[i], M + 1):
        if dp[j - lst[i]] != 10001:
            dp[j] = min(dp[j], dp[j - lst[i]] + 1)

if dp[M] == 10001:
    print(-1)
else:
    print(dp[M])