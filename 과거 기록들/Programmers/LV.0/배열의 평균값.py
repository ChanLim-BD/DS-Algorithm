def solution(numbers):
    x = 0.0
    for i in numbers:
        x += i
        answer = x / len(numbers)
    return answer

def solution1(numbers):
    return sum(numbers) / len(numbers)

def main():
    print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


if __name__ == '__main__':
    main()
