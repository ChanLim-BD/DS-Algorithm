"""
for i in range(2, int(num**(0.5)) + 1):

이 라인 주목,
"""


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):  # 2, 3, 4, 5, 6, 7 --- num -1
        if num % i == 0:
            return False
    return True


def is_prime2(num):
    if num == 1:
        return False
    for i in range(2, int(num**(0.5)) + 1):
        if num % i == 0:
            return False
    return True


def main():
    primes = []
    for i in range(1, 7897):
        if is_prime2(i) == True:
            primes.append(i)
    print(primes)


if __name__ == '__main__':
    main()
