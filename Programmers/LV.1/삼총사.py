def solution(number):
    answer = []
    for i in range(len(number)):
        for j in range(i + 1, len(number)):
            for k in range(j + 1, len(number)):
                if number[i] + number[j] + number[k] == 0:
                    answer.append([number[i], number[j], number[k]])
    return len(answer)

def solution1 (number) :
    from itertools import combinations
    cnt = 0
    for i in combinations(number,3) :
        if sum(i) == 0 :
            cnt += 1
    return cnt

def main():
    print(solution([-2, 3, 0, 2, -5]))


if __name__ == '__main__':
    main()