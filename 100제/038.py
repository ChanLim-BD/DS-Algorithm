data = list(map(int, input().split()))

count = 0

# break_point = sorted(data, reverse=True)
# print(break_point)

if len(set(data)) <= 3:
    count = len(data)
else:
    break_point = sorted(list(set(data)), reverse=True)[3]
    data_sorted = sorted(data, reverse=True)
    for i in data_sorted:
        if break_point == i:
            break
        else:
            count += 1

print(count)
