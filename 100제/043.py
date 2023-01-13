num = int(input())

lst = []

while(1):
    if num == 0:
        break
    else:
        if num % 2 == 0:
            lst.append(0)
            num = num // 2
        elif num % 2 == 1:
            lst.append(1)
            num = num // 2

for i in list(reversed(lst)):
    print(i, end='')
