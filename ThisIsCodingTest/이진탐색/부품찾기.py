N = int(input())
a1 = list(map(int, input().split()))
M = int(input())
a2 = list(map(int, input().split()))

start = 0
end = len(a1)

def bina(array, target, start, end):
    if start >= end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] >= target:
        return bina(array, target, start, mid - 1)
    else:
        return bina(array, target, mid + 1, end)
    
def binaf(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = start + 1
    return None
    
for i in a2:
    result = bina(a1, i, 0, N - 1)
    if result != None:
        print("Yes", end = ' ')
    else:
        print("No", end = ' ')

for i in a2:
    result = binaf(a1, i, 0, N - 1)
    if result != None:
        print("Yes", end = ' ')
    else:
        print("No", end = ' ')
        