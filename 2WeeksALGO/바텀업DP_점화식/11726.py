
# DP 문제

# 2가지 유형

# 1. 완전탐색적 사고, 추론이 가능한 DP
# 2. 손코딩 ! , 아이큐테스트, DP

N = int(input())

arr = []

for i in range(N + 1):
    if i == 0 or i == 1:
        arr.append(1)
    elif i == 2:
        arr.append(2)
    else:
        arr.append(arr[i-2] + arr[i-1])

print(arr[-1])
