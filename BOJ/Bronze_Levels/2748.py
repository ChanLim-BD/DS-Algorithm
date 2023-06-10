import sys
input = sys.stdin.readline

def fib(n):
    DP = [0, 1]
    if n == 0 or n == 1:
        return DP[n]
    else:
        for _ in range(2, n+1):  # 2, 3, 4, 5, 6, 7, 8, 9, 10
            DP.append(DP[-1] + DP[-2])
            "DP = [0, 1]"
            "DP = [0, 1, | 2, 3, 5, 8, 13, 21, 34, 55 ---]"
        return DP[-1]

x = int(input())

print(fib(x))