def solution(n,a,b):
    # 1. 전체 인원을 숫자로 대표하는 리스트를 만든다
    total = [[i, i] for i in range(1, n+1)]

    # 2. 타겟에 해당하는 경우 순서쌍에 별도 표기한다
    total[a-1] = [a, 'target'] 
    total[b-1] = [b, 'target']

    # 3. 스택에 쌓으면서 반복문을 탈출하고 판별한다
    stack_for_target = [i for i in total if i[1] == 'target']
    cnt = 1
    while True:
        if stack_for_target[1][0] - stack_for_target[0][0] == 1 and stack_for_target[0][0]%2 != 0:
            return cnt
        else:
            cnt += 1
            lower = stack_for_target[0][0]; upper = stack_for_target[1][0]
            if lower % 2 != 0:
                stack_for_target[0][0] = lower//2 + 1
            else:
                stack_for_target[0][0] = lower//2
            if upper % 2 != 0:
                stack_for_target[1][0] = upper//2 + 1
            else:
                stack_for_target[1][0] = upper//2
                
def solution(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2

    return answer