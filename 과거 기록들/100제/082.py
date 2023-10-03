def math(e):
    cnt = 0
    for i in e:
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1
        else:
            continue
    if cnt == 0:
        return True
    else:
        return False


while 1:
    order = input('데이터 입력(1), 프로그램 종료(2) : ')
    if order == '1':
        ex = input('데이터를 입력하세요 : ')
        print(math(ex))
    else:
        break
