def solution(num_list):
    a, b = 0, 0
    for i in num_list:
        if i % 2 == 0:
            a += 1
        elif i % 2 == 1:
            b += 1
    answer = [a, b]
    return answer


def solution1(num_list):
    answer = [0, 0]
    for n in num_list:
        answer[n % 2] += 1
    return answer
