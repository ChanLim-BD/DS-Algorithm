import math
# 조합 (Combination)


def factorial(x):  # 4! = 4 * 3 * 2 * 1
    val = 1
    for i in range(1, x+1):
        val = val * i
    return val


def solution(balls, share):
    return factorial(balls) // (factorial(balls - share) * factorial(share))


def solution1(balls, share):
    return math.factorial(balls)/(math.factorial(balls-share)*math.factorial(share))
