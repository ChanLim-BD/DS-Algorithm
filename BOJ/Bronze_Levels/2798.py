from itertools import combinations

N, M = map(int, input().split())
nums = list(map(int, input().split()))
sum_comb = []

for c in list(combinations(nums, 3)):
    if sum(c) == M:
        sum_comb.append(sum(c))
        break
    if sum(c) > M:
        continue
    else:
        sum_comb.append(sum(c))
print(max(sum_comb))


    