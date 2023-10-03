def solution(angle):
    if angle > 0 and angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif angle > 90 and angle < 180:
        return 3
    else:
        return 4


def main():
    print(solution(60))


if __name__ == '__main__':
    main()
