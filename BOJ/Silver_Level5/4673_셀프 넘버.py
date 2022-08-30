def fuc(n):
    return n + sum(map(int, str(n)))

N = 10000
arr = list(range(N))
for i in range(N): # 0 1 2 3 4 ... 9999
    if fuc(i) < N:
        arr[fuc(i)] = 0

for i in arr:
    if i != 0:
        print(i)