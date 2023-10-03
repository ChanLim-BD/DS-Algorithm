def solution(arr1, arr2):
    arr3 = []
    tmp = []
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            tmp.append(arr1[i][j] + arr2[i][j])
        arr3.append(tmp)
        tmp = []
    return arr3


def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a,b)] for a, b in zip(A,B)]
    return answer


def sumMatrix(A,B):
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] += B[i][j]