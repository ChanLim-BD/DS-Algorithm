def solution(i, j, k):
    st = []
    ans = 0
    for n in range(i, j+1):
        st.append(str(n))
    for s in st:
        if str(k) in s:
            ans += s.count(str(k))
    return ans


def solution1(i, j, k):
    answer = 0
    for n in range(i, j + 1):
        answer += str(n).count(str(k))
    return answer


def main():
    print(solution(1, 13, 1))


if __name__ == '__main__':
    main()
