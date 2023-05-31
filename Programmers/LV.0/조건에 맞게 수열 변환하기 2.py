def solution(arr):
    tmp = arr.copy()
    cnt = 0
    while True:
        for j in range(len(arr)):
            if arr[j] >= 50 and arr[j] % 2 == 0:
                arr[j] = arr[j] // 2
            elif arr[j] < 50 and arr[j] % 2 == 1:
                arr[j] = arr[j] * 2 + 1
            else:
                pass
        if tmp == arr:
            return cnt
        else:
            tmp = arr.copy()
            cnt += 1