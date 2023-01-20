def sol(frame, page):
    temp = []
    runTime = 0

    if frame == 0:
        runTime = len(page) * 6
        return runTime
    # cacheSize가 0일때, cities의 크기만큼 10을 곱해주고 끝낸다

    for i in page:
        if i in temp:
					  temp.append(temp.pop(0))
            runTime += 1
        else:
            if len(temp) < frame:
                temp.append(i)
                # temp가 비었으면 무조건 넣어야 하므로 if문을 사용함
            else:
                temp = temp[1:] + [i]
                # 가장 사용되지 않은 첫번째 배열을 제거하고 맨 뒤에 입력값을 저장해준다
            runTime += 6
            # if문 실행에 상관없이 runTime은 10이 추가된다
    return runTime
