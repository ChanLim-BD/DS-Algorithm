# 5
N = int(input())
# 2 3 1 2 2
guild = list(map(int, input().split()))
# 1 2 2 2 3
guild.sort()

answer = 0
count = 0

for i in guild:
    count += 1
    if count >= i:
        answer += 1
        count = 0

print(answer)