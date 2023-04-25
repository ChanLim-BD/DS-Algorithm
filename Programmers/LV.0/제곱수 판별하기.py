def solution(n):
    flag = 1
    for i in range(n):
        if i ** 2 == n:
            return 1
        else:
            flag = 2
    return flag
