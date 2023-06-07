import sys
input = sys.stdin.readline

N = int(input())
loc = []
for _ in range(N):
    loc.append(list(map(int, input().split())))
loc.sort(key=lambda x:(x[0], x[1]))

for i in range(len(loc)):
    print(loc[i][0], loc[i][1])