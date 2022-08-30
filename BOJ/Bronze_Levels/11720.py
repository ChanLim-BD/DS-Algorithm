import sys

cnt = int(sys.stdin.readline())
num = sys.stdin.readline()
ans = 0

for i in range(cnt):
    ans += int(num[i])

print(ans)
    