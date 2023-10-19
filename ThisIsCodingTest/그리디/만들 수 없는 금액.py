N = int(input())
coins = list(map(int, input().split()))
coins.sort()  # 1, 1, 2, 3, 9 # 1, 2, 4, 7

target = 1
for i in coins:
    if target < i:
        # 1 < 1, 2 < 1, 3 < 2, 5 < 4, 8 < 9 
        # 1 < 1, 2 < 2, 4 < 4, 8 < 7, 15
        break
    target += i 
    # 2, 3, 5, 8, 17
    # 2, 4, 8, 15

print(target)