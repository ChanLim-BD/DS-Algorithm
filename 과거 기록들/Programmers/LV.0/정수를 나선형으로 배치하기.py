# def solution(n):
#     answer = [[None for j in range(n)] for i in range(n)]
#     move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
#     x, y, m = 0, 0, 0
#     for i in range(1, n**2 + 1):
#         answer[y][x] = i
#         if y + move[m][0] >= n or x + move[m][1] >= n or answer[y + move[m][0]][x + move[m][1]]:
#             m = (m + 1) % len(move)
#         y, x = y + move[m][0], x + move[m][1]
#     return answer

def solution(n):
    answer = [[0] * n for i in range(n)]
    
    # limit point
    left = 0
    right = n - 1
    up = 1  # i == 0 부터 순회 하므로 up의 초기 값은 1이 된다.
    down = n - 1


    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    # 0: right, 1:down, 2:left, 3:up
    direction = 0   # initialize to right

    count = 1
    i = 0
    j = 0
    
    while count <= n * n:
        answer[i][j] = count
        count += 1
        # 진행방향의 끝에 도달하면 방향 전환
        if direction % 4 == 0 and j == right:
            direction += 1
            right -= 1
        elif direction % 4 == 1 and i == down:
            direction += 1
            down -= 1
        elif direction % 4 == 2 and j == left:
            direction += 1
            left += 1
        elif direction % 4 == 3 and i == up:
            direction += 1
            up += 1
        # 다음 방문할 리스트 인덱스 설정
        i += di[direction % 4]
        j += dj[direction % 4]
        
    return answer

print(solution(4))