def solution(n, numlist):
    answer = []
    for i in numlist:
        if i % n == 0:
            answer.append(i)
    return answer


def main():
    print(solution(2, [2, 4, 56, 7, 2, 4, 2, 7, 9, 0, 4, 3]))


if __name__ == '__main__':
    main()
