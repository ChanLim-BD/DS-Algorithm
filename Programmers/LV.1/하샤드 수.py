def solution(x):
    nums = [int(i) for i in str(x)]
    sum_nums = sum(nums)
    if x % sum_nums == 0:
        return True
    else:
        return False