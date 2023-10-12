N, K = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

# print(arr1, arr2)

# for _ in range(K):
#     # min(arr1) <-> max(arr2)
#     tmp1 = min(arr1)
#     arr1[arr1.index(min(arr1))] = max(arr2)
#     arr2[arr2.index(max(arr2))] = tmp1

# print(sum(arr1))

arr1.sort()
arr2.sort(reverse=True)

for i in range(K):
    if arr1[i] < arr2[i]:
        arr1[i], arr2[i] = arr2[i], arr1[i]
    else:
        break

print(sum(arr1))