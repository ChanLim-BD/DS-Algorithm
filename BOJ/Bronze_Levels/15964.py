import sys


def line(n, m):
    return (n+m)*(n-m)


a, b = map(int, sys.stdin.readline().split())

print(line(a, b))
