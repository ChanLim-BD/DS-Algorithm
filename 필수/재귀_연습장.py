def test1(x):
    if x == 1 or x == 2:
        return 1
    if dp[x] != 0:
        return dp[x]
    dp[x] = test1(x-1) + test1(x-2)
    return dp[x]

def test2(x):
    dp[1], dp[2] = 1, 1
    for i in range(3, x+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[x]

n = int(input())

dp = [0] * (n+1)
print(test1(n))   
print(dp)

dp = [0] * (n+1)
print(test2(n))   
print(dp)

