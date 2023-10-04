def recur_sum(x):
    if x < 2:
        return 1
    else:
        # print(f'x + recur_sum({x}-1): {x} + {x-1}')
        return x + recur_sum(x-1)
    
print(recur_sum(100))