"""i ~ j 까지 k의 개수 구하기"""


def solution(i, j, k):
    st = []
    ans = 0
    for n in range(i, j + 1):  # 1, 2, 3, 4, 5, 6, 7 --- 13
        st.append(str(n))  # "12345678910111213"
    for s in st:
        if str(k) in s:
            ans += s.count(str(k))
    return ans


def solution1(i, j, k):
    answer = 0
    for n in range(i, j + 1):
        answer += str(n).count(str(k))
        """1 ~ 13까지 수를 str로 변환하고 count 메서드를 사용한다."""
    return answer


def main():
    print(solution(1, 13, 1))


if __name__ == '__main__':
    main()
