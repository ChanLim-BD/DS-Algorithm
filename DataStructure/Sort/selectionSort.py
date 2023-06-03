def selectionSort(A):
	for last in range(len(A)-1, 0, -1):
		k = theLargest(A, last)	# A[0...last] 중 가장 큰 수 A[k] 찾기
		A[k], A[last] =  A[last], A[k]

def theLargest(A, last:int) -> int:	# A[0...last]에서 가장 큰 수의 인덱스를 리턴한다
	largest = 0
	for i in range(last + 1):
		if A[i] > A[largest]:
			largest = i
	return largest

#---

array = [7, 5, 8, 9, 1, 4, 2, 6]

for i in range(len(array)):
	min_idx = i
	for j in range(i + 1, len(array)):
		if array[min_idx] > array[j]:
			min_idx = j
	array[i], array[min_idx] = array[min_idx], array[i]

print(array)