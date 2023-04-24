import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    x1, x2 = numer1 * denom2 + numer2 * denom1, denom1 * denom2 
    if (math.gcd(x1 , x2) == 1):
        answer.append(x1)
        answer.append(x2)
        return answer
    else:
        div = math.gcd(x1, x2)
        x1 = int(x1 / div)
        x2 = int(x2 / div)
        answer.append(x1)
        answer.append(x2)
        return answer
    