def solution(keyinput, board):
    x_pb = (board[0] - 1) // 2
    x_mb = -(board[0] - 1) // 2
    y_pb = (board[1] - 1) // 2
    y_mb = -(board[1] - 1) // 2
    x, y = 0, 0
    for k in keyinput:
        if k == "up":
            if y < y_pb:
                y += 1
            else:
                pass
        if k == "down":
            if y > y_mb:
                y -= 1
            else:
                pass
        if k == "right":
            if x < x_pb:
                x += 1
            else:
                pass
        if k == "left":
            if x > x_mb:
                x -= 1
            else:
                pass
    answer = [x, y]
    return answer
