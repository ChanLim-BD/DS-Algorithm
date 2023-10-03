
def recur(idx, weight):

    if weight > B:
        return -9999999
    
    if idx == N:
        return 0
    
    if dp[idx][weight] != -1:
        return dp[idx][weight]

    # 물건을 넣은 경우
    dp[idx][weight] = max(recur( idx + 1, weight + items[idx][0])  + items[idx][1], recur( idx + 1, weight))

    return dp[idx][weight]

N, B = map(int, input().split())

items = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1 for _ in range(100_000)] for _ in range(N)]

ans = recur(0, 0)

print(ans)

##########################################################################################################

dp2 = [[-1 for _ in range(100_000)] for _ in range(N)]

for idx in range(N+1):
    for weight in range(B+1):

        if weight < B :
            dp2[idx][weight] = dp2[idx-1][weight]
        else:
            dp2[idx][weight] = max(dp2[idx - 1, weight + items[idx][0]]  + items[idx][1], dp2[idx - 1, weight])
