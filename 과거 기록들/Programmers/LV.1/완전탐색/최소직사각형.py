def solution(sizes):
    long_l = []
    short_l = []
    answer = 0
    for size in sizes:
        long_l.append(max(size))
        short_l.append(min(size))
    answer = max(long_l) * max(short_l)
    return answer

def main():
    print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))


if __name__ == '__main__':
    main()