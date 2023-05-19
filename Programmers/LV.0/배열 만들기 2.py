def solution(l, r):
    answer = []
    for num in range(l, r + 1):
        if not set(str(num)) - set(['0', '5']):
            print(num)
            answer.append(num)
    return answer if answer else [-1]

def main():
    print(solution(5, 555))


if __name__ == '__main__':
    main()