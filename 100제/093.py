def solution(frame, page):
    page = page.split(' ')
    runTime = 0
    temp = []

    # frame이 0일때, page의 크기만큼 6을 곱해주고 끝낸다
    if frame == 0:
        runTime = len(page) * 6
        return runTime

    for i in page:
        if i in temp:
            runTime += 1
        else:
            # 배열이 비었으면 무조건 넣어야 하므로 if문을 사용
            if len(temp) < frame:
                temp.append(i)
            else:
                # 가장 사용되지 않은 첫번째 배열을 제거하고 맨 뒤에 입력값을 저장
                temp = temp[1:] + [i]
            # if문 실행에 상관없이 runTime은 10이 추가된다
            runTime += 6

    return runTime


f = int(input())
page = list(map(str, input()))


print(solution(f, page))
