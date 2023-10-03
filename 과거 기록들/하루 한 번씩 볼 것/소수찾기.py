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
    for i in range(2, int(num**(0.5)) + 1):     # 연산 시간 최소화, 특정한 자연수의 약수를 찾을 때 가운데 약수(제곱근)까지만 확인
        if num % i == 0:
            return False
    return True

def is_prime3(n):
    answer = []
    for i in range(2, n+1):
        count = 0
        for j in range(2, i // 2+1):
            if i % j == 0:
                count += 1
        if count == 0:
            answer.append(i)
    print(answer)


def main():
    primes = []
    for i in range(1, 100):
        if is_prime2(i) == True:
            primes.append(i)
    print(primes)


if __name__ == '__main__':
    main()
