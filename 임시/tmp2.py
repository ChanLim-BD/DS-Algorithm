import itertools 

def is_prime(x):
    if x == 1 or x == 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


numbers = "1744"
answer = 0

nums = [n for n in numbers]
per = []

for i in range(1, len(numbers) + 1):
    per += list(itertools.permutations(nums, i))

print(per)

int_nums = list(set([int("".join(p)) for p in per]))

print(sorted(int_nums))

for i in int_nums:
    if is_prime(i) == True:
        answer += 1
    else:
        pass

print(answer)