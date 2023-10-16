import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

dic = {}
search = []

for _ in range(N):
    site, password = input().split()
    dic[site] = password

for _ in range(M):
    search.append(input())

for s in search:
    print(dic[s])