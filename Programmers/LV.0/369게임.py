def solution(order):
    answer = 0
    st = str(order)
    for s in st:
        if s == '3' or s == '6' or s == '9':
            answer += 1
    return answer
