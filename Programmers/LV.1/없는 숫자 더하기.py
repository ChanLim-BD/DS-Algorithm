def solution(numbers):
    ans = 0
    for i in range(1, 10):
        if i not in numbers:
            ans += i
    return ans

def solution(numbers):
    return 45 - sum(numbers)