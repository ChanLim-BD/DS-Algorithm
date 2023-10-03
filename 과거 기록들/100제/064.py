weight = int(input())

count = 0

if weight < 3:
    print(-1)
elif weight >= 3 and weight < 7:
    if weight % 3 == 0:
        count = weight // 3
        print(count)
    else:
        print(-1)
else:  # weight >= 7
    count = weight // 7
    if weight % 7 < 3:
        print(-1)
    elif weight % 7 == 3:  # weight % 7 >= 3
        print(count + 1)
    else:
        rest = weight % 7
        if rest % 3 == 0:
            tmp = rest // 3
            print(count + tmp)
        else:
            print(-1)


'''
N = int(input())
result = 0

while True:
    if N%7 ==0:
        result += N//7
        print(result)
        break
    N -= 3
    result += 1
    if N < 0:
        print(-1)
        break
'''
