line = list(input())

# print(ord(line[0]))

for i in range(len(line)):
    if ord(line[i]) == 113:
        line[i] = 'e'
    print(line[i], end='')
