def solution1(my_string):
    ans = ""
    for s in my_string:
        if s in "abcdefghijklmnopqrstuvwxyz":
            ans += s.upper()
        else:
            ans += s.lower()
    return ans


def solution(my_string):
    return my_string.swapcase()


def main():
    print(solution("dmaskdjskljKLDSJSKLJKLJFkldasfdf"))


if __name__ == '__main__':
    main()
