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