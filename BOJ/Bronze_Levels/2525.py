import sys
h, m = map(int, sys.stdin.readline().split(" "))
s = int(sys.stdin.readline())

m = m + s

if m >= 60:
    a = m // 60
    h = h + a
    m = m - 60*a
    if h >= 24:
        h = h - 24
        print(h, m)
    else:
        print(h, m)
else:
    print(h, m)
