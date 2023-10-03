import itertools 

def is_prime(x):
    if x == 1 or x == 0:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    nums = [n for n in numbers]
    per = []
    
    for i in range(1, len(numbers) + 1):
        per += list(itertools.permutations(nums, i))
    
    int_nums = list(set([int("".join(p)) for p in per]))

    
    for i in int_nums:
        if is_prime(i) == True:
            answer += 1
        else:
            pass
    
    return answer