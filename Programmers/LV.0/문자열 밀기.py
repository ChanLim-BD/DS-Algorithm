def solution(A, B):
    if A == B:
        return 0
    a, b = list(A), list(B)
    for i in range(1, len(A) + 1):  # 1 ~ 5
        tmp = a.pop()
        a.insert(0, tmp)
        if a == b:
            return i
    return -1


def main():
    print(solution("hello", "ohell"))


if __name__ == '__main__':
    main()
