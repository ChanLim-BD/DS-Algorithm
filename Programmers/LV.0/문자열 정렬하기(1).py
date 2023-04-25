def solution(my_string):
    answer = []
    for s in my_string:
        if s in "1234567890":
            answer.append(int(s))
    answer.sort()
    return answer
