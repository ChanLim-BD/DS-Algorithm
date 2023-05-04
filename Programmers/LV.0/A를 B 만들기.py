from collections import Counter
"""리스트 원소의 개수를 알고 싶을 때,"""


def solution(before, after):
    if Counter(before) == Counter(after):
        """Counter({'l': 2, 'o': 1, 'e': 1, 'h': 1}) Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})"""
        return 1
    else:
        return 0


def solution1(before, after):
    """sorted(정렬할 데이터, key 파라미터, reverse 파라미터) Default : reverse=False로 오름차순"""
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
