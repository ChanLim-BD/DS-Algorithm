data = [10, 20, 30, 40, 50, 60, 70, 80, 90]

sum_value = 0
prefix_sum = [0]

for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

left = 3
right = 4

print(prefix_sum)
print(prefix_sum[right] - prefix_sum[left - 1])

N = int(input())
arr = list(map(int, input().split()))

prefix = [0 for _ in range(N+1)]

for i in range(N):
    prefix[i+1] = max(prefix[i] + arr[i], arr[i])

print(prefix)