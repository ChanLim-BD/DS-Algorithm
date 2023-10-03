"""https://gomming.tistory.com/28"""


def solution(score):
    x = []
    for s in score:
        x.append(s[0] + s[1])
    # print(x) [120, 140, 153]
    y = sorted(x, reverse=True)
    # [153, 140, 120]
    p_ind = []
    for i in x:
        p_ind.append(y.index(i)+1)
        """
            x : [120, 140, 153]
            y : [153, 140, 120]
        """
    return p_ind


def main():
    print(solution([[70, 50], [60, 80], [88, 65]]))


if __name__ == '__main__':
    main()
