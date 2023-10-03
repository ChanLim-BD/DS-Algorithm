st = input()

for i in range(len(st)):  # [P y t h o n]
    if i == 0:
        print(st[i], end='')
    elif i == len(st):
        break
    elif i == len(st) - 1:
        print('{}'.format(st[i]))
    else:
        print('{}\n{}'.format(st[i], st[i]), end='')

'''
data = input()

for i in range(len(data) - 1):
	print(data[i], data[i+1], sep = '')
'''
