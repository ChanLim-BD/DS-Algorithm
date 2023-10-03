def solution(strlist):
    answer = []
    for s in strlist:
        answer.append(len(s))
    return answer

def solution1(strlist):
    answer = list(map(len, strlist))
    return answer