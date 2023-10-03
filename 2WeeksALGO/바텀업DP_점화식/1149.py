
N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(N)] for _ in range(N)]

for idx in range(N):
    for RGB in range(N):
        if RGB == 0:
            dp[idx][RGB] = min(dp[idx-1][1], dp[idx-1][2]) + graph[idx][RGB]
        if RGB == 1:
            dp[idx][RGB] = min(dp[idx-1][0], dp[idx-1][2]) + graph[idx][RGB]    
        if RGB == 2:
            dp[idx][RGB] = min(dp[idx-1][0], dp[idx-1][1]) + graph[idx][RGB]

print(dp[N-1][0])