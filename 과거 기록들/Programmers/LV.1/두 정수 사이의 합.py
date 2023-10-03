def solution(a, b):
    ans = 0
    if a <= b:
        for i in range(a, b+1):
            ans += i
        return ans
    else:
        for i in range(b, a+1):
            ans += i
        return ans
    
def adder(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))