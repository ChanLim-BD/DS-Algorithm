def solution(array, height):
    array.append(height)
    x = sorted(array, reverse=True)
    answer = x.index(height)
    return answer


def main():
    print(solution([149, 180, 192, 170], 167))


if __name__ == '__main__':
    main()
