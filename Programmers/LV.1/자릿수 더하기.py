def solution(n):
    answer = 0

    x = list(str(n))
    for i in x:
        answer += int(i)

    return answer


def sum_digit(number):
    return sum([int(i) for i in str(number)])
print("결과 : {}".format(sum_digit(123)));