def solution(s):
    answer = ''
    x = sorted(list(s), reverse=True)
    for s in x:
        answer += s
    return answer