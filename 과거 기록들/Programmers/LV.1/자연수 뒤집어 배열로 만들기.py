def solution(n):
    x = list(map(int, str(n)))
    x.reverse()
    return x

def digit_reverse(n):
    return list(map(int, reversed(str(n))))