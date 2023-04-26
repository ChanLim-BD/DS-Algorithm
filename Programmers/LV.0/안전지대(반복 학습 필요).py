"""
https://velog.io/@seulki971227/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Lv.0-%EC%95%88%EC%A0%84%EC%A7%80%EB%8C%80-Python
"""

import numpy as np
from collections import Counter
from collections import deque


def solution0(board):
    n = len(board)
    danger = set()
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            if not x:
                continue
            danger.update((i+di, j+dj)
                          for di in [-1, 0, 1] for dj in [-1, 0, 1])
    return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)


def solution(board):
    n = len(board)
    # pad() 함수를 사용해 주어진 2차원 배열의 상하좌우 1줄씩 -1을 추가한 board_padded 생성
    board_padded = np.pad(board, ((1, 1), (1, 1)), constant_values=-1)
    danger_array = np.pad(board, ((1, 1), (1, 1)), constant_values=-1)
    for i in range(1, n+1):  # 1 2 3 4 5
        for j in range(1, n+1):  # 1 2 3 4 5
            if board_padded[i][j] == 1:
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        danger_array[x][y] = 1
    danger_list = danger_array.reshape(1, -1).squeeze() # 2차원 배열을 1차원 배열로
    print(danger_list)
    answer = Counter(danger_list)[0]
    # 결과 값 반환
    return answer


def solution1(board):
    dx = [-1, 1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]
    length = len(board)
    visited = [[False] * length for _ in range(length)]

    def bfs(x, y):
        dq = deque()
        dq.append((x, y))
        while dq:
            a, b = dq.popleft()
            visited[a][b] = True
            for i in range(8):
                nx = dx[i] + a
                ny = dy[i] + b
                # 위험지역으로 둬야함
                if 0 <= nx < length and 0 <= ny < length and not visited[nx][ny]:
                    if board[nx][ny] == 1:
                        dq.append((nx, ny))
                    else:
                        board[nx][ny] = 2  # 위험지역 처리

    for i in range(length):
        for j in range(length):
            if board[i][j] == 1:
                bfs(i, j)
    result = 0
    for i in range(length):
        result += board[i].count(0)
    return result


def main():
    print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
          0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))


if __name__ == '__main__':
    main()
