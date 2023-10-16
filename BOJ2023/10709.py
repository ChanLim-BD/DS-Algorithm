H, W = map(int, input().split())
sky = [input() for _ in range(H)]
forecast = [[0] * W for _ in range(H)]

for i in range(H):
    cloud = False
    
    for j in range(W):
        if not cloud and sky[i][j] == '.':
            forecast[i][j] = -1

        elif sky[i][j] == 'c':
            cloud = True
            forecast[i][j] = 0
            cnt = 1

        elif cloud and sky[i][j] == '.':
            forecast[i][j] = cnt
            cnt += 1

for i in forecast:
    print(*i, end=' ')
    print()
    
