N = int(input())
dp = [0] * 20

dp[0], dp[1], dp[2] = 0, 1, 2

for i in range(3, N+1):
    dp[i] = min(dp[i - 1] + 1, dp[i - 3] + 1)

if dp[N] % 2 == 1:
    print('SK')
else:
    print('CY')

print(dp)