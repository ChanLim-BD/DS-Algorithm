import sys
s = int(sys.stdin.readline())

for i in range(1, 10):
    print("{0} * {1} = {2}".format(s, i, s*i))
