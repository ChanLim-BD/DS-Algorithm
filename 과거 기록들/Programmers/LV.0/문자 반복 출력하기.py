def solution(my_string, n):
    answer = ''
    for s in my_string:
        answer += s * n
    return answer


def solution1(my_string, n):
    return ''.join(i*n for i in my_string)
