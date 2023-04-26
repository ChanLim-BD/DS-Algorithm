def solution(numbers, k):
    answer = 0
    for i in range(1, k):
        answer = numbers[2 * i % len(numbers)]
    return answer


def main():
    print(solution([1, 2, 3, 4, 5, 6], 5))


if __name__ == '__main__':
    main()
