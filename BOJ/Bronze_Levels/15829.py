n = int(input())
st = input()
alpha_nums = []
answer = 0

for s in st:
    alpha_nums.append(ord(s) - 96)

for i in range(n):
    answer += alpha_nums[i] * 31 ** i

print(answer % 1234567891)