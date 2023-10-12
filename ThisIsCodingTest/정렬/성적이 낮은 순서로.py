N = int(input())
array = [input().split() for _ in range(N)]

array = sorted(array, key = lambda x : x[1])

for s in array:
    print(s[0], end = ' ')