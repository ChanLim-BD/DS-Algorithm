def solution(my_string):
    for i in my_string:
        if i.isalpha():
            my_string = my_string.replace(i, ' ')
    print(my_string)
    my_string = my_string.split()
    print(my_string)
    print(list(map(int, my_string)))

    return sum(list(map(int, my_string)))


def main():
    print(solution("aAb1B2cC34oOp"))


if __name__ == '__main__':
    main()
