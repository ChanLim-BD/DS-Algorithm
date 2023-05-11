def solution(n):
    ls = []
    for i in range(1, n+1):
        if n % i == 1:
            ls.append(i)
    return min(ls)