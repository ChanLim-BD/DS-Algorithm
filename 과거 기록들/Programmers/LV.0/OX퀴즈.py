def solution(quiz):
    answer = []
    # [연산자]는 + 와 - 중 하나입니다.
    for q in quiz:
        left, right = q.split('=')
        "= 을 기준으로 왼쪽 오른쪽 나눈다."
        left = left.split()
        "(공백)을 기준으로 나누고 리스트로 저장한다."
        "['1 + 2'] -> ['1', '+', '2']"
        if left[1] == '+':  # 더하기 연산
            if int(left[0]) + int(left[2]) == int(right):
                answer.append('O')
            else:
                answer.append('X')
        elif left[1] == '-':  # 빼기 연산
            if int(left[0]) - int(left[2]) == int(right):
                answer.append('O')
            else:
                answer.append('X')
    return answer


def main():
    print(solution(["1 + 2 = 3", "42 - 32 = 10"]))


if __name__ == '__main__':
    main()
