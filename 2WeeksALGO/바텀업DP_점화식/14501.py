def recur(idx):

    if idx == N-1:
        return 0
    if idx > N-1:
        return -99999999999999
    if dp[idx] != -1: #이미 저장되었다면,
        return dp[idx]

    # 상담을 받거나, 안받거나, 그 중에서 더 많은 돈을 버는 경우를 내 DP 테이블에 저장하겠다.
    dp[idx] = max(recur(idx + interview[idx][0]) + interview[idx][1], recur(idx+1))

    return dp[idx]

N = int(input())

interview =[list(map(int, input().split())) for _ in range(N)]

dp = [-1 for _ in range(N + 1)]

recur(0)

print(dp)

####################################################################################################
####################################################################################################


dp2 = [0 for _ in range(N+1)]

for idx in range(N+1)[::-1]:

    if idx + interview[idx][0] > N :
        dp2[idx] = dp2[idx+1]
    else:
        dp2[idx] = max(dp2[idx + interview[idx][0]] + interview[idx][1], dp2[idx+1])

print(dp2)