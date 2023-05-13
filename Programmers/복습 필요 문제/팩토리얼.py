def factorial(x):
    val = 1
    for i in range(1, x+1):
        val = val * i
    return val


def solution(n):
    num = 1
    while True:
        if factorial(num) > n:
            return num - 1
        else:
            num += 1

def main():
    print(solution(100))


if __name__ == '__main__':
    main()