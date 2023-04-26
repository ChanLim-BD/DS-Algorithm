"""
- key 옵션 (key 파라미터)
sorted 함수의 key 파라미터는 어떤 것을 기준으로 정렬할 것인가? 에 대한 기준입니다.
즉, key 값을 기준으로 비교를 하여 정렬을 하겠다는 것인데, 이것을 정해 줄 수 있는 파라미터입니다.
sorted( ~~ , key=뭐뭐)로 입력하게 되면 해당 키를 기준으로 정렬하여 반환합니다.
"""


def solution(numlist, n):
    answer = []  # n과의 거리를 저장할 리스트
    for i in numlist:
        answer.append(i - n)

    result = []  # 정렬한 배열
    # 거리가 n에 가까운 순으로 정렬, 절댓값이 같으면 양수(= 큰 값) 먼저
    print(answer[:])  # 전체 출력
    print(sorted(answer[:], key=lambda x: [abs(x), -x]))
    for i in sorted(answer[:], key=lambda x: [abs(x), -x]):
        result.append(numlist[answer.index(i)])

    return result


def main():
    print(solution([1, 2, 3, 4, 5, 6], 4))


if __name__ == '__main__':
    main()
