line = input()
words = sorted(list(set(line)))

# print(words)

for i in words:
    print('{}{}'.format(i, line.count(i)), end='')
