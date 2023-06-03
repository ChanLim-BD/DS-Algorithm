def solution(board, k):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if i+j<=k:
                answer+=board[i][j]
    return answer

'''
def solution(board, k):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if i+j<=k:
                answer+=board[i][j]
    return answer
'''

# 첫 번째 코드에서는 range(len(board[0]))를 사용하여 board[0]의 길이에 따라 두 번째 for 루프의 범위가 결정됩니다. 
# 이 경우 board의 각 행의 길이가 동일한 경우에만 정상적으로 동작합니다. 만약 board의 행의 길이가 다르다면 오류가 발생할 수 있습니다.
# 두 번째 코드에서는 range(len(board))를 사용하여 board의 길이에 따라 두 번째 for 루프의 범위가 결정됩니다. 
# 이 경우 board의 각 행의 길이가 다르더라도 정상적으로 동작합니다.

# 따라서 첫 번째 코드는 board의 각 행의 길이가 동일할 때 사용하고, 두 번째 코드는 board의 각 행의 길이가 다를 수 있을 때 사용하는 것이 좋습니다.