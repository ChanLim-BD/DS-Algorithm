def solution(common):
    plus, multiple = 0, 0
    if common[1] - common[0] == common[2] - common[1]:
        plus = 1
    else:
        multiple = 1
    if plus == 1:
        answer = common.pop() + (common[1] - common[0])
    else:
        answer = common.pop() * (common[1] // common[0])
    return answer
