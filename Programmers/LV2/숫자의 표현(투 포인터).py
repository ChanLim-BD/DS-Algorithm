def solution(n):
    answer, end = 0, 0
    interval_sum = 0
    nature = []
    
    for i in range(1, n+1):
        nature.append(i)
    
    for start in range(len(nature)):
        while interval_sum < n and end < len(nature):
            interval_sum += nature[end]
            end += 1
        if interval_sum == n:
            answer += 1
        interval_sum -= nature[start]
        
    return answer