def fun(num):
    rt = 1
    if 2 < len(num):
        d = int(num[0]) - int(num[1])
        for i in range(len(num)-1):
            d2 = int(num[i]) - int(num[i+1])
            if d != d2:
                rt = 0
    return rt

N = int(input())
cnt = 0
for i in range(1, N + 1):
    cnt += fun(str(i))

print(cnt)