def solution(emergency):
    answer = []
    order = sorted(emergency, reverse=True)
    for i in range(len(emergency)):
        for j in range(len(emergency)):
            if order[j] == emergency[i]:
                answer.append(order.index(order[j]) + 1)
    return answer


def solution1(emergency):
    e = sorted(emergency, reverse=True)
    return [e.index(i)+1 for i in emergency]


def main():
    print(solution([3, 76, 24]))


if __name__ == '__main__':
    main()
