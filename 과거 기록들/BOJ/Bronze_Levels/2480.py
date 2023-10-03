import sys
a, b, c = map(int, sys.stdin.readline().split(" "))

if a == b:
    if a == c:
        print(10000+a*1000)
    else:
        print(1000+a*100)
else:
    if b == c:
        print(1000+b*100)
    elif a == c:
        print(1000+a*100)
    else:
        if a > b and a > c:
            print(100*a)
        elif b > a and b > c:
            print(100*b)
        elif c > a and c > b:
            print(100*c)
