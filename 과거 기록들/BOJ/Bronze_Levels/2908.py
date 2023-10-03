i, j = map(str, input().split())

lst = [int(i[::-1]), int(j[::-1])]

print(max(lst))