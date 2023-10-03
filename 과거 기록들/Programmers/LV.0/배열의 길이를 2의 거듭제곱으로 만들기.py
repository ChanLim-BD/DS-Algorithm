def solution(arr):
    ln = 1
    while True:
        if ln < len(arr):
            ln *= 2
        elif ln == len(arr):
            return arr
        else:
            for _ in range(ln - len(arr)):
                arr.append(0)
            return arr