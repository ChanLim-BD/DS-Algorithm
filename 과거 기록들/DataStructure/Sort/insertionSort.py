def insertionSort(A):
	for i in range(1, len(A)):
		loc = i-1
		newItem = A[i]
		while loc >= 0 and newItem < A[loc]:
			A[loc+1] = A[loc]
			loc -= 1
		A[loc+1] = newItem

# 코드 9-3

array = [7, 5, 8, 9, 1, 4, 2, 6]

for i in range(1, len(array)):
	for j in range(i, 0, -1):
		print(array)
		if array[j] < array[j - 1]:
			array[j], array[j - 1] = array[j - 1], array[j]
		else:
			break

print(array)