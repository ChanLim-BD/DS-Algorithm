def solution(n):
    answer = 0
    while True:
        if n != 0:
            answer += n % 10
            print(answer)
            n = n // 10
        else:
            break
    return answer


def solution(n):
    return sum(int(i) for i in str(n))


def main():
    print(solution(1234))


if __name__ == '__main__':
    main()
