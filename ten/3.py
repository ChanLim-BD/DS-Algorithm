def calculateScoreDifference(n, board):
    # n x n 크기의 2차원 리스트 dp를 생성하고 모든 요소를 0으로 초기화합니다.
    dp = [[0] * n for _ in range(n)]

    # 부분 문제의 길이를 1부터 n까지 순회합니다.
    for length in range(1, n + 1):
        # 시작 인덱스 i와 끝 인덱스 j를 계산합니다.
        for i in range(n - length + 1):
            j = i + length - 1

            # 길이가 1인 경우, 해당 위치의 점수를 dp[i][j]에 저장합니다.
            if length == 1:
                dp[i][j] = board[i]
            # 길이가 2인 경우, 두 사람 중 더 큰 점수를 dp[i][j]에 저장합니다.
            elif length == 2:
                dp[i][j] = max(board[i], board[j])
            else:
                # 왼쪽을 선택했을 때의 점수 차이와 오른쪽을 선택했을 때의 점수 차이를 계산합니다.
                pick_left = board[i] - min(dp[i + 1][j], dp[i + 2][j])
                pick_right = board[j] - min(dp[i][j - 1], dp[i][j - 2])
                # 두 경우 중 더 큰 점수 차이를 dp[i][j]에 저장합니다.
                dp[i][j] = max(pick_left, pick_right)

    # 두 사람의 최종 점수 차이인 dp[0][n-1]을 반환합니다.
    print(dp)
    return dp[0][n - 1]


# n = 5
# board = [-1000, -1000, -3, -1000, -1000]

# n = 6
# board = [100, -1000, -1000, 100, -1000, -1000]

n = 10
board =  [7, -5, 8, 5, 1, -4, -8, 6, 7, 9]
score_difference = calculateScoreDifference(n, board)
print("결과:", score_difference)

