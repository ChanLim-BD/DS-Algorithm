def solution(arr, flag):
    answer = []
    tmp = []
    for i in range(len(flag)):
        if flag[i] == True:
            tmp = [arr[i]] * (arr[i] * 2)
            answer.extend(tmp)
        elif flag[i] == False:
            for _ in range(arr[i]):
                answer.pop()
    return answer