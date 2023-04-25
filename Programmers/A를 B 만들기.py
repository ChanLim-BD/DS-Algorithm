from collections import Counter


def solution(before, after):
    if Counter(before) == Counter(after):
        return 1
    else:
        return 0


def solution1(before, after):
    before = sorted(before)
    after = sorted(after)
    if before == after:
        return 1
    else:
        return 0


def main():
    print(solution("olleh", "hello"))


if __name__ == '__main__':
    main()
