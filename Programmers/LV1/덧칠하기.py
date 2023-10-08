def solution(n, m, section):
    answer = 1 # 칠하는 횟수
    paint = section[0] # 덧칠 시작점
    for i in range(1, len(section)): # 1, 2
        if section[i] - paint >= m: # 3 - 2 >= 4, 6 - 2 >= 4
            answer += 1
            paint = section[i]
    return answer