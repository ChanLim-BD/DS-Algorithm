def solution(common):
    p, m = 0, 0
    if common[1] - common[0] == common[2] - common[1]:
        p = 1
    else:
        m = 1
    if p == 1:
        answer = common.pop() + (common[1] - common[0])
    else:
        answer = common.pop() * (common[1] // common[0])
    return answer
