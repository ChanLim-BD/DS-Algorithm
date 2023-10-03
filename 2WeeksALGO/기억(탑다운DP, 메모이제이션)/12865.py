
def recur(idx, weight):

    # 베낭의 무게 제한 보다 높다면,
    if weight > B:
        return -9999999
    
    # 마지막 물건까지 확인
    if idx == N:
        return 0
    
    # 연산 후 결과물을 만난다면?
    if dp[idx][weight] != -1:
        return dp[idx][weight]

    # 물건을 넣은 경우와 물건을 넣지 않은 경우 중 크기 비교
    dp[idx][weight] = max(recur(idx + 1, weight + items[idx][0]) + items[idx][1], recur(idx + 1, weight))

    return dp[idx][weight]

N, B = map(int, input().split()) # 물건의 수, 배낭의 무게

items = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1 for _ in range(100_000)] for _ in range(N)]

ans = recur(0, 0)

print(ans)