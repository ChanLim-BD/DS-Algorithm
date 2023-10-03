from collections import Counter


def solution(array):
    ls = Counter(array)
    if len(ls) != 1:
        if ls.most_common()[0][1] == ls.most_common()[1][1]:
            return -1
    answer = ls.most_common()[0][0]
    return answer


def solution2(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0:
            return a
    return -1


def main():
    print(solution([5, 4, 5, 7, 1, 3, 2, 2, 2, 2, 2]))


if __name__ == '__main__':
    main()
