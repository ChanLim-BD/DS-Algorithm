def solution(my_string):
    s = my_string.split()
    print(s)
    answer = int(s[0])
    for i in range(1, len(s), 2):
        if s[i] == '+':
            answer += int(s[i+1])
        else:
            answer -= int(s[i+1])
    return answer


def main():
    print(solution("3 + 4"))


if __name__ == '__main__':
    main()
