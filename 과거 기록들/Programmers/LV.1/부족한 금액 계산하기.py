def solution(price, money, count):
    cost = 0
    for i in range(1, count+1):
        cost += price * i
    ans = money - cost
    if ans < 0:
        return abs(ans)
    else:
        return 0