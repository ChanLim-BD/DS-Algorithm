import sys
num = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split(" ")))

M = max(score)

for i in range(len(score)):
    score[i] = score[i] / M * 100

sum = 0

for j in score:
    sum += j

print(sum / num)
