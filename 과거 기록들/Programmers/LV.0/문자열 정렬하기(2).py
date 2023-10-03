def solution(my_string):
    return ''.join(sorted(list(my_string.lower())))


def main():
    print(solution("Python"))


if __name__ == '__main__':
    main()
