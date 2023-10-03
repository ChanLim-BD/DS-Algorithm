n = int(input())

std, cnt= 1, 1
while n > std:
    std += 6 * cnt
    cnt += 1
print(cnt)