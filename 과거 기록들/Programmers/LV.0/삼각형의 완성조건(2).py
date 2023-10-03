def solution(sides):
    answer = 0
    for i in range(1, max(sides)):
        if i + min(sides) > max(sides):
            answer += 1
    for j in range(max(sides), max(sides) * 2):
        if min(sides) + max(sides) > j and max(sides) <= j:
            answer += 1
    return answer


def main():
    print(solution([1, 2]))


if __name__ == '__main__':
    main()
