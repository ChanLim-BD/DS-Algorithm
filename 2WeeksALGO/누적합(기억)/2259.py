A, B = map(int, input().split()) # 숫자 갯수, 간격
arr = list(map(int, input().split()))

prefix = [0 for _ in range(A+1)] # 1칸 더 크게 만들기

for i in range(A):
    prefix[i+1] = prefix[i] + arr[i]

answer = []

for k in range(B, A+1):
    answer.append(prefix[k] - prefix[k-B])

print(max(answer))

"""
10 2
3 -2 -4 -9 0 3 7 13 8 -3

(0) 3 1 -3 -12 -12 -9 4 12 9

1 -6 -13 -9 3 16 21 18 
"""