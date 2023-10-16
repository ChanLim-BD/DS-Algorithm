A, B, C = map(int, input().split()) #  A, B, C  입력
dp = [0] * 101                      # DP
ans = 0

"""
0 1 2 3 4 5 6 7 8 9 10
   - - - - -
       - -
     - - - - - -
"""

for _ in range(3):  # 3번 입력
    start, end = map(int, input().split())
    for i in range(start, end):
        dp[i] += 1

print(dp)

for j in dp:
    if j == 0:
        ans += 0
    elif j == 1:
        ans +=  A * 1
    elif j == 2:
        ans +=  B * 2
    elif j == 3:
        ans +=  C * 3

print(ans)