# def recur(number, output):
#     if number == M:
#         print(output)
#         return
    
#     for i in range(1, N+1):
#         recur(number+1, output+str(i)+" ")

# N, M = map(int, input().split())

# recur(0, "")

# -----------

def TopDown(x):
    if x == 0:
        return x
    print(x, end=' ')
    TopDown(x-1)

TopDown(10)

print()

def BottomUp(n):
    if n != 1 :
        BottomUp(n-1) 
    print(n, end=' ')

BottomUp(10)

print()

#---

a, b = 2, 7 # map(int, input().split())

def odd(x, y):
    if x == y + 1:
        return
    if x % 2 == 1:
        print(x, end=' ')
    odd(x+1, y)

odd(a, b)

print()

# ---
import sys
sys.setrecursionlimit(1000000)

def recur_sum(x):
    if x < 2:
        return 1
    else:
        # print(f'x + recur_sum({x}-1): {x} + {x-1}')
        return x + recur_sum(x-1)
    
print(recur_sum(100))

print()

# ---

def factorial(x):
    if x == 1:
        return 1
    else:
        print(f'x + factorial({x}-1): {x} * {x-1}')
        return x * factorial(x-1)
    
print(factorial(5))

print()

# ---

def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(5))

print()

# ---

def fibo_dp(x):
    if x == 1 or x == 2:
        return 1
    if dp[x] != 0:
        return dp[x]
    dp[x] = fibo_dp(x-1) + fibo_dp(x-2)
    return dp[x]

dp = [0] * 10000

print(fibo_dp(7))


# ---

def bina(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return str(bina(n // 2)) + str(n % 2)

print(bina(7))
print()

# ---

def colaz1(n):
    print(n)
    if n == 1:
        return 1
    if n % 2 == 1:
        colaz1(3*n + 1)
    if n % 2 == 0:
        colaz1(n // 2)
    
colaz1(5)
print()

#---

def colaz2(n):
    if n == 1:
        return print(n)
    if n % 2 == 1:
        colaz2(3*n + 1)
    if n % 2 == 0:
        colaz2(n // 2)
    return print(n)
    
colaz2(5)
print()

# ---
'''
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

print()
'''

# ---

def tri1(n):
    if n == 1:
        return print('*')
    tri1(n-1)
    print('*' * n)

tri1(3)

print()

def tri2(n):
    print('*' * n)
    if n == 1:
        return 
    tri2(n-1)
    
tri2(3)

# ---

def stair(n, a):
    if n == 1:
        a[1] = 1
        return a[1]
    elif n == 2:
        a[2] = 2
        return a[2]
    elif n == 3:
        a[3] = 4
        return a[3]
    
    if a[n]:
        return a[n]
    else:
        a[n] = (stair(n - 3, a) + stair(n - 2, a) + stair(n - 1, a)) % 1000
        return a[n]
    
n = int(input())
a = [0 for _ in range(n+1)]
print(stair(n,a))

#- ---