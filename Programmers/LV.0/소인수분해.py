def prime(n):
    prime = []
    for i in range(2, n + 1):
        flag = 0
        if n <= 1:
            pass
        for j in range(2, i):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            prime.append(i)
    return prime


def solution(n):
    answer = []
    for i in prime(n+1):
        if n % i == 0:
            answer.append(i)
    return answer


def solution1(n):
    answer = []
    d = 2
    while d <= n:
        if n % d == 0:
            n /= d
            if d not in answer:
                answer.append(d)
        else:
            d += 1
    return answer


def main():
    print(solution(17))


if __name__ == '__main__':
    main()
