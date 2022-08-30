a = [0 for i in range(31)]
for i in range(1, 29):
    b = int(input())
    a[b] = 1
for i in range(1, 31):
    if a[i] == 0:
        print(i)
