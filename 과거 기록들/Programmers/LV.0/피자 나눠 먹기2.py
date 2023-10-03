import math


def lcm(a, b):
    for i in range(max(a, b), (a * b) + 1):
        if i % a == 0 and i % b == 0:
            return i


def solution(n):
    if (n % 6) == 0:
        return n // 6
    else:
        return (lcm(n, 6) // 6)


def solution2(n):
    return (n * 6) // math.gcd(n, 6) // 6


def main():
    print(solution(10))


if __name__ == '__main__':
    main()
