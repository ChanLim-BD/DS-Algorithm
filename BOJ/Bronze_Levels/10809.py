import sys

str = sys.stdin.readline()

d = {}

for i in str:
    if i not in d:
        d[i] = str.index(i)

alp = 'abcdefghijklmnopqrstuvwxyz'

for j in alp:
    if j in d:
        print(d[j], end=' ')
    else:
        print(-1, end=' ')
