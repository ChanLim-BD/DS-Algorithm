l = [10, 20, 25, 27, 34, 35, 39]  # 기존 입력 값
n = int(input('순회 횟수는 :'))


def rotate(inL, inN):
    lr = inL.copy()
    for _ in range(inN):
        tmp = lr.pop()
        lr.insert(0, tmp)

    sut = []
    for i in range(len(inL)):
        sut.append(abs(inL[i] - lr[i]))

    print('index : {}'.format(sut.index(min(sut))))
    print('value : {}, {}'.format(
        inL[sut.index(min(sut))], lr[sut.index(min(sut))]))


rotate(l, n)
