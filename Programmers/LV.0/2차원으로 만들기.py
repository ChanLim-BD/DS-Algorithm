def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):  # n 단위 씩 0 2 4 6 ---
        answer.append(num_list[i:i+n])  # 0 2 | 2 4 | 4 6 |
    return answer


def main():
    print(solution([1, 2, 3, 4, 5, 6, 7, 8], 2))


if __name__ == '__main__':
    main()
