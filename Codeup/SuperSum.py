# def SuperSum(k, n):
#     if k == 0:
#         return n
#     mysum = 0
#     for i in range(1, n+1):
#         mysum += SuperSum(k-1, i)
#     return mysum
    
# while True:
#     try:
#         K, N = map(int, input().split())
#         print(SuperSum(K,N))
#     except:
#         break

def SuperSum(k, n, dp):
    if k == 0:
        dp[0][n-1] = n
        return n
    elif k != 0:
        mysum = 0
        for i in range(n):
            if dp[k-1][i]:
                mysum += dp[k-1][i]
            else:
                t = SuperSum(k-1, i+1, dp)
                mysum += t
                dp[k-1][i] = t
        return mysum
    
while True:
    try:
        K, N = map(int, input().split())
        dp = [[0 for _ in range(N)] for _ in range(K)]
        print(SuperSum(K, N, dp))
    except EOFError:
        break