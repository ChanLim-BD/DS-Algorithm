import sys
num = int(sys.stdin.readline())

sum = 0
avg = 0
x = 0

for i in range(num):
    s = list(map(int, sys.stdin.readline().split()))
    for j in range(1, len(s)):
        sum += s[j]
    avg = sum/s[0]
    for j in range(1, len(s)):
        if avg < s[j]:
            x += 1
    print("{:.3f}%".format(x/s[0]*100))
    sum = 0
    avg = 0
    x = 0

"""
formatting!!!
"""