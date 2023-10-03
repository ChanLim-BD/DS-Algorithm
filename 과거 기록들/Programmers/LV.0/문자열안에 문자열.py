def solution(str1, str2):

    if str2 in str1:
        answer = 1
    else:
        answer = 2

    return answer


def main():
    print(solution("AbcAbcA", "AAA"))


if __name__ == '__main__':
    main()
