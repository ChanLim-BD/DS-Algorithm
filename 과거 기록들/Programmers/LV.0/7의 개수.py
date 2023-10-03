def solution(array):
    st = list(str(array))
    answer = st.count('7')
    return answer


def main():
    print(solution('545894735894738954789574895734895'))


if __name__ == '__main__':
    main()
