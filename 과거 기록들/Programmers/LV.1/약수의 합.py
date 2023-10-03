def solution(n):
    ls = []
    for i in range(1, n+1): # 1, 2, 3 ~~ 12
        if n % i == 0:
            ls.append(i)
    return sum(ls)