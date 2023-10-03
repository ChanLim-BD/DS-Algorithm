ls = list(map(int, input().split()))
result = ['ascending', 'descending', 'mixed']

asc = sorted(ls)
desc = sorted(ls, reverse=True)

if ls == asc:
    print(result[0])
elif ls == desc:
    print(result[1])
else:
    print(result[2])