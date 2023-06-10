import sys
input = sys.stdin.readline
    
for _ in range(int(input())):
    N, M = map(int, input().split())

    dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
    print(dp)
    for i in range(1, N+1):
        for j in range(1, M+1):
            if i == 1:
                dp[i][j] = j
                continue
            if i == j:
                dp[i][j] = 1
            else:
                if j > i:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
            print(dp)

    print(dp[N][M])

# 조합 (nCr)
