def is_prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

M, N = map(int, input().split())

for i in range(M, N+1):
    if is_prime(i) == True:
        print(i)
    else:
        continue

import math

n = 1000
array = [True for _ in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

for i in range(2, n + 1):
    if array[i]:
        print(i, end= ' ')