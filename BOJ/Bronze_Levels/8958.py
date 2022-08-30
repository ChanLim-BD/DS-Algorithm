import sys
num = int(sys.stdin.readline())

k = []

for i in range(num):
    s = sys.stdin.readline()
    for j in range(len(s)):
        if j == 0:
            if s[j] == 'O':
                k.append(1)
            else:
                k.append(0)
        if j > 0:
            if s[j] == 'O':
                k.append(k[j-1]+1)
            else:
                k.append(0)
    print(sum(k))
    k = []
