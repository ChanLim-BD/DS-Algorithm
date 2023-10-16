import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
by_id = {}
by_name = {}

for i in range(1, N + 1):
    name = input()
    by_id[i] = name
    by_name[name] = i

for _ in range(M):
    x = input()
    if x.isdigit():
        print(by_id[int(x)])
    else:
        print(by_name[x])
