import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
q = deque()

for i in range(1, N + 1):
    q.append(i)

while len(q) != 1:
    q.popleft()
    tmp = q.popleft()
    q.append(tmp)

print(q[0])
