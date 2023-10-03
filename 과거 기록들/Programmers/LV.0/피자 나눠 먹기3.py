def solution(slice, n):
    if (n % slice) == 0:
        return n // slice
    else:
        return (n // slice) + 1


def main():
    print(solution(4, 12))


if __name__ == '__main__':
    main()
