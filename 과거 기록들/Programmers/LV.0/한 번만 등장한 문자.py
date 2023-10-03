def solution(s):
    ls = list(s)
    answer = [s for s in ls if ls.count(s) == 1]
    return "".join(sorted(answer))


def main():
    print(solution("abcabcadc"))


if __name__ == '__main__':
    main()
