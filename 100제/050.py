def bubble(n, data):
    for i in range(n-1):
        for j in range(n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    for i in range(n):
        print(data[i], end=" ")


data = list(map(int, input().split()))
n = len(data)

bubble(n, data)

'''
 [47, 5, 65, 54, 23]
  0   1  2   3   4
  n = 5
  0 1 2 3
  4 3 2 1
 

'''
