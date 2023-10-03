def quickSort(A, p:int, r:int):
	count = 0
	if p < r:
		q = partition(A, p, r)	 # 분할
		quickSort(A, p, q-1)	 # 왼쪽 부분 리스트 정렬
		quickSort(A, q+1, r)	 # 오른쪽 부분 리스트 정렬
		

def partition(A, p:int, r:int) -> int:
	x = A[r]					# x: 기준 원소
	i = p-1					# i: 1구역의 끝 지점
	for j in range(p, r):	# j: 3구역의 시작 지점
		if A[j] < x:
			i += 1
			A[i], A[j] = A[j], A[i]  # 교환
	A[i+1], A[r] = A[r], A[i+1]	   # 기준 원소와 2구역 첫 원소 교환
	return i+1

# ---

array = [7, 5, 8, 9, 1, 4, 2, 6]

def quick_sort(array, start, end):
	if start >= end:
		return
	pivot = start
	left = start + 1
	right = end
	while left <= right:
		while left <= end and array[left] <= array[pivot]:
			left += 1
		while right > start and array[right] >= array[pivot]:
			right -= 1
		if left > right:
			array[right], array[pivot] = array[pivot], array[right]
		else:
			array[left], array[right] = array[right], array[left]
	quick_sort(array, start, right - 1)
	quick_sort(array, right + 1, end)

def quick_sort_p(array):
	if len(array) <= 1:
		return array
	pivot = array[0]
	tail = array[1:]

	left_side = [x for x in tail if x <= pivot]
	right_side = [x for x in tail if x > pivot]

	return quick_sort_p(left_side) + [pivot] + quick_sort_p(right_side)

sol = quick_sort_p(array)
# quick_sort(array, 0, len(array) - 1)
print(sol)

		