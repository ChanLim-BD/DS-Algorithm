def test1(x):                       # TopDown 즉, 주어진 숫자 에서 0 또는 1까지 연산
    if x == 1 or x == 2:            # 재귀
        return 1
    if dp[x] != 0:
        return dp[x]
    dp[x] = test1(x-1) + test1(x-2)
    return dp[x]

def test2(x):                       # BottomUp 즉, 0 또는 1에서 주어진 숫자까지 연산
    dp[1], dp[2] = 1, 1             # 점화식 - 반복문 사용
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

#######################################

'''
1m 2m 네트워크 선을 갖는다.

1 2 3 5 8
'''
print()



def net1(x):
    dp[0], dp[1], dp[2] = 0, 1, 2
    for i in range(3, x+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[x]

def net2(x):
    if x == 1:
        return 1
    if x == 2:
        return 2
    if dp[x] != 0:
        return dp[x]
    dp[x] = net2(x-1) + net2(x-2)
    return dp[x]

dp = [0] * 50
print(net1(5))

dp = [0] * 50
dp[0], dp[1], dp[2] = 0, 1, 2
print(net2(5))

#####################



















