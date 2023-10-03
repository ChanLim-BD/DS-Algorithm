def solution(n):
    answer = []
    for i in range(1, n+1, 2):
        answer.append(i)
    return answer


def main():
    print(solution(15))


if __name__ == '__main__':
    main()
