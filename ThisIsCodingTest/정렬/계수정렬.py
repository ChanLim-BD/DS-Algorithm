array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8, 0, 1, 7]

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

print(array)
print(count)

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')

'''
계수 정렬은 `동일한 값을 여러 개 등장할 때 적합하다.
즉, 데이터의 크기가 한정되어 있고, 데이터의 크기가 많이 중복되어 있을수록 유리하며 항상 사용할 수 없다.
'''