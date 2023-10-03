num = list(map(int, input().split()))

# for i in range(1, len(num) + 1):
#     print(num[len(num) - i], end=' ')

for i in range(len(num) - 1, -1, -1):
    print(num[i], end=' ')
