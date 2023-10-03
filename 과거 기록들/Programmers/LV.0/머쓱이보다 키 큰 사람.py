def solution(array, height):
    array.append(height)
    # [149, 180, 192, 170, 167]
    x = sorted(array, reverse=True)
    # [192, 180, 170, 167, 149]
    answer = x.index(height)
    return answer


def main():
    print(solution([149, 180, 192, 170], 167))


if __name__ == '__main__':
    main()
