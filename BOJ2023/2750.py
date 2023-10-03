n = int(input())
nums = []

for _ in range(n):
    nums.append(int(input()))
nums.sort(reverse=False)

for n in nums:
    print(n)