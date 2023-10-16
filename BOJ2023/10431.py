T = int(input())

for _ in range(T):
    steps = 0

    tmp = list(map(int, input().split()))
    TC = tmp[0] 
    array = tmp[1:]

    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
                array[i], array[min_index] = array[min_index], array[i]
                steps += 1
            else:
                continue

    print(TC, steps)


P = int(input())
for _ in range(P):
    arr = list(map(int,input().split()))
    total = 0
    for i in range(1, len(arr)-1):
        for j in range(i + 1, len(arr)): # i 뒤에 애들과 전부 비교해서
            if arr[i] > arr[j]:  # i가 더 크면
                arr[i],arr[j] = arr[j],arr[i]  # 자리바꾸기
                total+=1
    print(arr[0], total)