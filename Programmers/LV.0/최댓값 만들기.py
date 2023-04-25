def solution(numbers):
    numbers.sort(numbers, reverse=True)
    return numbers[0] * numbers[1]
