def solution(my_string, overwrite_string, s):
    for i in range(len(overwrite_string)):
        answer = my_string.replace(my_string[s + i], overwrite_string[i], s)
    return answer


def main():
    print(solution("He11oWor1d", "lloWorl", 2))


if __name__ == '__main__':
    main()
