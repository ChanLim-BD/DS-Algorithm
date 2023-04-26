def solution(bin1, bin2):
    a = int(bin1, 2)  # 이진수 -> 십진수
    b = int(bin2, 2)
    print(a, b)
    answer = bin(a+b)  # 십진수 -> 이진수
    return answer.replace("0b", "")


def main():
    print(solution("10", "11"))


if __name__ == '__main__':
    main()
