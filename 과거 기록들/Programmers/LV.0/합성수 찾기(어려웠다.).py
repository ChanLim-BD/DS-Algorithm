def solution(n):
    num = []
    ans = 0
    for i in range(2, n+1):
        for j in range(1, i+1):
            if i % j == 0:
                num.append(i)
        if num.count(i) >= 3:
            print(num.count(i))
            ans += 1
    print(num)
    return ans


def main():
    print(solution(10))


if __name__ == '__main__':
    main()
