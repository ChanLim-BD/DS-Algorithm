N, M, K = map(int, input().split())         # 5, 8, 3
nums = list(map(int, input().split()))      # 2 4 5 4 6

nums.sort(reverse = True)                   # 6 5 4 4 2
max_num = nums[0]                           # 6
sec_num = nums[1]                           # 5

'''
6 6 6 5 6 6 6 5
'''

count = int(M / (K + 1)) * K                # 8 / (3 + 1) * 3
count += M % (K + 1)                        # += 8 % (3 + 1)

result = 0
result += count * max_num                   # 
result += (M - count) * sec_num             # 6 6 6 5 6 6 6 5

print(result)