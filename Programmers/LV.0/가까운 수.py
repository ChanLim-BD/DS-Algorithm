def solution(array, n):
    box = []
    array.sort()
    '[3, 10, 12, 28]'
    for i in array:
        box.append(abs(n-i))
        '[17, 10, 8, 8]'
    answer = [array[box.index(min(box))]]
    # print(box.index(min(box))) 2
    if len(answer) > 1:
        return min(answer)
    else:
        return answer[0]


def main():
    print(solution([3, 10, 28, 12], 20))


if __name__ == '__main__':
    main()
