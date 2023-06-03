def countingSort(A):
	k = max(A)	# 리스트 A[...]에서 최대값
	C = [0 for _ in range(k+1)]
	for j in range(len(A)):
		C[A[j]] += 1
	for i in range(1, k+1):
		C[i] = C[i] + C[i-1]
	B = [0 for _ in range(len(A))] 
	for j in range(len(A)-1, -1, -1):
		B[C[A[j]]-1] = A[j]
		C[A[j]] -= 1
	return B

# 코드 9-9

array = [7, 5, 8, 9, 1, 4, 2, 6, 3, 4, 1, 2, 9, 7, 8, 4, 7, 2, 1]

count = [0] * (max(array) + 1)

for i in range(len(array)):
	count[array[i]] += 1


print(count)

for i in range(len(count)):
	for j in range(count[i]):
		print(i, end=' ')