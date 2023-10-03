while True:
    i = list(input())
    if i == ['0']:
        break
    elif i == i[::-1]:
        print('yes')
    elif i != i[::-1]:
        print('no')