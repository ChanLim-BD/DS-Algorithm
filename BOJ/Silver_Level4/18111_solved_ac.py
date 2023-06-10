import sys
input = sys.stdin.readline

def my_round(val):
    return int(val) + 1 if val - int(val) >= 0.5 else int(val)

n = int(input())
if n == 0:
    print(0)
else:
    levels = sorted([int(input()) for _ in range(n)])
    per15 = my_round(n * 0.15)
    print(my_round(sum(levels[per15:-(per15)] if per15 else levels) / (n - 2 * per15)))


# 부동소수점