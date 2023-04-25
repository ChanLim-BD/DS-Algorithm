def solution(numbers, num1, num2):
    answer = []
    for i in range(num1, num2 + 1):
        answer.append(numbers[i])
    return answer


def solution2(numbers, num1, num2):
    return numbers[num1:num2+1]
