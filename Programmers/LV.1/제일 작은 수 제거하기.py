def solution(arr):
    if len(arr) == 1:
        return [-1]
    min_n = min(arr)
    arr.remove(min_n)
    return arr

def rm_small(mylist):
    return [i for i in mylist if i > min(mylist)]