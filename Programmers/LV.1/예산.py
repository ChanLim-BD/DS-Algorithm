def solution(d, budget):
    ans = 0
    x = 0
    for _ in range(len(d)):
        ans += d.pop(d.index(min(d))) # 리스트의 최솟값의 위치를 받고 그 위치의 값을 제거
        if ans > budget:
            break
        x += 1
    return x

def main():
    print(solution([1,3,2,5,4], 9))


if __name__ == '__main__':
    main()