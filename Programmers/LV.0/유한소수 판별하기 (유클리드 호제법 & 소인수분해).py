"""https://chan-lab.tistory.com/34"""


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def factorization(x):
    d = 2
    output = []

    while d <= x:
        if x % d == 0:
            output.append(d)
            x /= d
        else:
            d += 1

    return output


def solution(a, b):
    divide_num = gcd(b, a)
    result = b // divide_num

    for num in factorization(result):
        if num not in [2, 5]:
            return 2
    return 1


def main():
    print(solution(7, 20))


if __name__ == '__main__':
    main()
