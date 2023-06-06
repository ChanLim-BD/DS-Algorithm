# 선택 정렬

array = [7, 5, 8, 9, 1, 4, 2, 6]

for i in range(len(array)):
	min_idx = i
	for j in range(i + 1, len(array)):
		if array[min_idx] > array[j]:
			min_idx = j
	array[i], array[min_idx] = array[min_idx], array[i]

print(array)

print()

# 삽입 정렬

array = [7, 5, 8, 9, 1, 4, 2, 6]

for i in range(1, len(array)):
	for j in range(i, 0, -1):
		if array[j] < array[j - 1]:
			array[j], array[j - 1] = array[j - 1], array[j]
		else:
			break

print(array)

print()

# 퀵 정렬

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


# 계수 정렬

array = [7, 5, 8, 9, 1, 4, 2, 6, 3, 4, 1, 2, 9, 7, 8, 4, 7, 2, 1]

count = [0] * (max(array) + 1)

for i in range(len(array)):
	count[array[i]] += 1


print(count)

for i in range(len(count)):
	for j in range(count[i]):
		print(i, end=' ')