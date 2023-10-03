def solution(my_string):
    ans = list(my_string)
    for s in ans:
        if ans.count(s) >= 2:
            print(ans.count(s))
            ans.reverse()
            for _ in range(ans.count(s) - 1):
                ans.remove(s)
            ans.reverse()
    return ''.join(ans)


def solution1(my_string):
    answer = ''
    for i in my_string:
        if i not in answer:
            answer += i
    return answer


def main():
    print(solution("We are the world"))


if __name__ == '__main__':
    main()
