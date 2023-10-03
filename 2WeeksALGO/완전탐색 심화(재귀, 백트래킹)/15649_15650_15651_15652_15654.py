# def recur(number, output):
#     if number == M:
#         print(output)
#         return
    
#     for i in range(1, N+1):
#         recur(number+1, output+str(i)+" ")

# N, M = map(int, input().split())

# recur(0, "")

def recur1(number):
    if number == M:
        print(*arr1)
        return
    
    for i in range(1, N+1):
        arr1.append(i)
        recur1(number+1)
        arr1.pop()

def recur2(number):
    if number == M:
        print(*arr2)
        return
    
    for i in range(1, N+1):
        if i in arr2:
            continue
        arr2.append(i)
        recur2(number+1)
        arr2.pop()

def recur3(number):
    if number == M:
        if arr3[0] > arr3[1] or arr3[1] > arr3[2] or arr3[0] > arr3[2]:
            return
        print(*arr3)
        return
    
    for i in range(1, N+1):
        if i in arr3:
            continue
        arr3.append(i)
        recur3(number+1)
        arr3.pop()

def recur4(number):
    if number == M:
        if arr4[0] < arr4[1] or arr4[1] < arr4[2] or arr4[0] < arr4[2]:
            return
        print(*arr4)
        return
    
    for i in range(1, N+1):
        if i in arr4:
            continue
        arr4.append(i)
        recur4(number+1)
        arr4.pop()

N, M = map(int, input().split())
arr1 = []
arr2 = []
arr3 = []
arr4 = []
recur1(0)
print()
recur2(0)
print()
recur3(0)
print()
recur4(0)