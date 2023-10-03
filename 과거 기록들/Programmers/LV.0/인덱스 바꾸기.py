def solution(my_string, num1, num2):
    my_str = list(my_string)
    tmp1 = my_str[num1]
    tmp2 = my_str[num2]
    my_str.pop(num1)
    my_str.insert(num1, tmp2)
    my_str.pop(num2)
    my_str.insert(num2, tmp1)
    ans = ''.join(my_str)
    return ans


def solution1(my_string, num1, num2):
    s = list(my_string)
    s[num1], s[num2] = s[num2], s[num1]
    return ''.join(s)


def main():
    print(solution("hello", 1, 2))


if __name__ == '__main__':
    main()
