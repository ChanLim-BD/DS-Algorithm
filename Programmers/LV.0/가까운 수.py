def solution(array, n):
    box = []
    array.sort()
    for i in array:
        box.append(abs(n-i))
    answer = [array[box.index(min(box))]]
    if len(answer) > 1:
        return min(answer)
    else:
        return answer[0]


def main():
    print(solution([3, 10, 28, 12], 20))


if __name__ == '__main__':
    main()
