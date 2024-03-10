# 두 개의 마우스 커서, 포인터

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr = sorted(arr)

s = 0
e = n - 1

cnt = 0

while s < e:
    if arr[s] + arr[e] == x:
        cnt += 1

    if arr[s] + arr[e] >= x:
        e -= 1
    else:
        s += 1

print(cnt)