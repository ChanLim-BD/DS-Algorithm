import numpy as np

tc = int(input())
a, b = map(int, input().split())

city = []

for i in range(a):
    city.append(list(map(int, input().split(' '))))

s = 0

for i in range(a - b + 1):
    for j in range(b):
        if np.sum(city[i:b+i, j:b+j]) > s:
            s = np.sum(city[i:b+i, j:b+j])
print(s)
