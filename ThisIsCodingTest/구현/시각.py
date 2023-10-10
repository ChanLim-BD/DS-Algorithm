N = int(input())

result = 0

for i in range(N + 1): # 0 ~ N
    for j in range(60): # 0 ~ 59
        for k in range(60): # 0 ~ 59
            if '3' in str(i) + str(j) + str(k):
                result += 1

print(result)