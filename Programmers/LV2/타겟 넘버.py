def DFS(numbers, target, depth):
    answer = 0
    if depth == len(numbers):
        if sum(numbers) == target:
            return 1
        else:
            return 0
    else:
        answer += DFS(numbers, target, depth+1)
        numbers[depth] *= -1
        answer += DFS(numbers, target, depth+1)
        return answer

def solution1(numbers, target):
    answer = DFS(numbers, target, 0)
    return answer

def solution2(numbers, target):         # [1,1,1,1,1], 3
    answer = 0
    leaves = [0]
    for num in numbers:
        tmp = []                        # 
        for parent in leaves:
            tmp.append(parent + num)
            tmp.append(parent - num)
        leaves = tmp                    # [1, -1] [2, 0, 0,-2] [3, 1, 1, -1, 1, -1, -1, -3] [4, 2, 2, 0, 2, 0, 0, -2, 2, 0, 0, -2, 0, -2, -2, -4] [5, 3, 3, 1, 3, 1, 3, 1, -1, 1, -1, -1, -3, 3, 1, 1, -1, 1, -1, -3, -1, ...]
    for leaf in leaves:
        if leaf == target:
            answer += 1
    return answer

print(solution1([1,1,1,1,1], 3))