def div(n):
    tmp = 0
    for i in range(1, n + 1):
        if i == 1:
            tmp = 1
        elif n % i == 0:
            tmp += 1
    return tmp

###

def div(n):
    tmp = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            tmp += 1
            if i**2 != n : 
                tmp += 1
    return tmp

def solution(number, limit, power):
    answer = 0
    for i in range(1, number + 1): # 1 2 3 4 5
        if div(i) > limit:
            answer += power
        else:
            answer += div(i)
    return answer