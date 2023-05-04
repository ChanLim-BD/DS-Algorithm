def solution1(lines):
    table = [set([]) for _ in range(200)]  # -100~100까지 각 선분들의 등장 count 초기화
    # print(table)
    for index, line in enumerate(lines):  # 1 [0, 1], 2 [2, 5], 3 [3, 9]
        x1, x2 = line
        for x in range(x1, x2):
            table[x + 100].add(index)  # 선분에 음수가 들어있을 수도 있으므로 +100
    print(table)
    answer = 0
    for line in table:
        if len(line) > 1:
            answer += 1
    return answer


def solution(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    # print(sets)
    """
        {0}
        {2, `3, 4`}
        {`3, 4`, 5, 6, 7, 8}
    """
    print(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])


def solution2(lines):
    s1 = set(i for i in range(lines[0][0], lines[0][1]))
    s2 = set(i for i in range(lines[1][0], lines[1][1]))
    s3 = set(i for i in range(lines[2][0], lines[2][1]))
    return len((s1 & s2) | (s2 & s3) | (s1 & s3))


def main():
    print(solution([[0, 1], [2, 5], [3, 9]]))


if __name__ == '__main__':
    main()
