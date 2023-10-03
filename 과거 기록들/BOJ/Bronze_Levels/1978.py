def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num**(0.5)) + 1):     # 연산 시간 최소화, 특정한 자연수의 약수를 찾을 때 가운데 약수(제곱근)까지만 확인
        if num % i == 0:
            return False
    return True

n = int(input())
nums = list(map(int, input().split()))
cnt = 0

for i in range(n):
    if is_prime(nums[i]) == True:
        cnt += 1

print(cnt)