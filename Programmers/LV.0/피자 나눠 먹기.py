def solution(n):
    if (n % 7) == 0:
        return n // 7
    else:
        return (n // 7) + 1


def solution2(n):
    return (n - 1) // 7 + 1


def main():
    print(solution(7))


if __name__ == '__main__':
    main()
