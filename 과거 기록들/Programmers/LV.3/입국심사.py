def solution(n, times):
    answer = 0
    start, end, mid = 1, times[-1] * n, 0

    while start < end:
        mid = (start + end) // 2
        total = 0
        print(start, end, mid)
        for time in times:
            total += mid // time
        print(total)
        if total >= n:
            end = mid
        else:
            start = mid + 1
    answer = start
    return answer

print(solution(6, [7, 10]))