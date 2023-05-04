def get_ggeol(stock):
    high_stack = []
    ggeol = []

    for i in range(len(stock)): # 0, 1, 2, 3, 4, 5, ---
        while len(high_stack) > 0 and stock[high_stack[-1]] <= stock[i]:
            high_stack.pop(-1)

        if len(high_stack) == 0:
            ggeol.append(-1)
        else:
            ggeol.append(high_stack[-1])
        
        if i == 0 and stock[i] > stock[i+1]:                    # stock[0]이 고점일 때: stock[0] > stock[1]
            high_stack.append(i)
        elif i == len(stock)-1 and stock[i] > stock[i-1]:       # 마지막이 고점일 때:   stock[-1] > stock[-2]
            high_stack.append(i)
        elif stock[i] > stock[i-1] and stock[i] > stock[i+1]:
            high_stack.append(i)
        print("{}th high_stack = {}".format(i, high_stack))
    return ggeol

stocks = [8, 7, 6, 7, 5, 4, 5, 3, 2, 1, 2, 4, 6, 5, 7, 10, 8, 6, 5, 6, 5, 2, 2, 1, 11]
"""
ggeol  = [-1, 0, 0, 0, 3, 3, 3, 6, 6, 6, 6, 6, 3, 12, 0, -1, 15, 15, 15, 15, 19, 19, 19, 19, -1]
"""

print(get_ggeol(stocks))
        