def solution(my_string):
    answer = 0
    for s in my_string:
        if s in "0123456789":
            answer += int(s)
    return answer
