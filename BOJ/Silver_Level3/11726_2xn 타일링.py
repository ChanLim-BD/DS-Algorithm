'''
n
1 - 1
2 - 2
3 - 3
4 - 5

An = A(n-1) + A(n-2)
'''

import sys
input = sys.stdin.readline

n = int(input())
rs = [0,1,2]

for i in range(3, n+1):
    rs.append((rs[i-1] + rs[i-2]) % 10007)

print(rs[n])