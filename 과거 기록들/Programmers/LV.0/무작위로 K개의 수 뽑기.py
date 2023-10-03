def solution(arr, k):
    answer = [-1] * k
    tp = []
    for i in arr:
        if i not in tp:
            tp.append(i)
    for i in range(min(k, len(tp))):
        answer[i] = tp[i]
    return answer