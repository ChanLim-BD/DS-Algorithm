K, N = map(int, input().split())
num = [int(input()) for _ in range(K)] # 802, 743, 457, 539

start = 1
end = max(num)

answer = 0

while start <= end:
    count = 0
    mid = (start + end) // 2

    for x in num:
        count += x // mid
    
    if count >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)