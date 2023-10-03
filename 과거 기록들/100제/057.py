data = list(map(str, range(1001)))

# print(data)
line = ''
count = 0

for i in data:
    line += i

for j in line:
    if j == '1':
        count += 1

print(count)


def count(n):
    countN = str(list(range(n+1))).count('1')
    return countN


print(count(1000))
