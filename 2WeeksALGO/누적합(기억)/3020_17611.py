import sys
input = sys.stdin.readline

n, h = map(int,input().split()) # 장애물 개수, 인간

line = [0 for _ in range(h)]

for t in range(n):
    height = int(input())
    if t % 2 == 0: # 즉, 짝수
        line[0] += 1
        line[height] -= 1 
        
    if t % 2 == 1: # 홀수
        line[h-height] += 1

print(line)

prefix = [0 for _ in range(h+1)]

for i in range(h):
    prefix[i+1] = prefix[i] + line[i]
    
prefix = prefix[1:]

print(prefix)

print(min(prefix), prefix.count(min(prefix)))
