def knapsack(W, N, items):
    # 초기화
    W = W - 1 # 가방
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    selected = [[[] for _ in range(W + 1)] for _ in range(N + 1)]

    # 동적 계획법을 이용한 풀이
    for i in range(1, N + 1):
        name, weight, value = items[i - 1]
        print(name, weight, value)
        for j in range(1, W + 1):
            if weight > j:
                dp[i][j] = dp[i - 1][j]
                selected[i][j] = selected[i - 1][j]
            else:
                if dp[i - 1][j] > dp[i - 1][j - weight] + value:
                    dp[i][j] = dp[i - 1][j]
                    selected[i][j] = selected[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j - weight] + value
                    selected[i][j] = selected[i - 1][j - weight] + [name]

    # 선택된 아이템 추적
    max_value = dp[N][W]
    selected_items = selected[N][W]

    return [W + 1, max_value, len(selected_items)], selected_items

W = 12
N = 5
items = [["camera", 5, 10], ["smartphone", 2, 20], ["cup", 3, 5], ["towel", 4, 7], ["pants", 6, 11]]

result = knapsack(W, N, items)
print(result)
